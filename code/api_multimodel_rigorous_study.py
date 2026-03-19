#!/usr/bin/env python3
"""
API-backed multi-model rigorous paired study.

Compares unscaffolded vs externally scaffolded behavior for real models from:
- OpenAI
- Anthropic
- Gemini

Outputs paired-trial statistics (bootstrap CIs + permutation p-values) mirroring
`rigorous_swarm_study.py` while operating on actual model API responses.

IMPORTANT
---------
- This script can incur real API costs.
- Use --dry-run first to verify behavior without spending credits.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from statistics import mean, stdev
from typing import Dict, List, Optional, Tuple

from external_scaffolding_swarm_simulation import Task, generate_tasks


# -----------------------------------------------------------------------------
# Statistics utilities (dependency-free)
# -----------------------------------------------------------------------------


def bootstrap_ci(values: List[float], reps: int = 2000, alpha: float = 0.05, seed: int = 0) -> Tuple[float, float]:
    if not values:
        return (0.0, 0.0)
    rng = random.Random(seed)
    n = len(values)
    boot = []
    for _ in range(reps):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        boot.append(mean(sample))
    boot.sort()
    lo_idx = int((alpha / 2) * (reps - 1))
    hi_idx = int((1 - alpha / 2) * (reps - 1))
    return boot[lo_idx], boot[hi_idx]


def sign_flip_permutation_pvalue(values: List[float], reps: int = 10000, seed: int = 0) -> float:
    if not values:
        return 1.0
    rng = random.Random(seed)
    observed = abs(mean(values))
    count = 0
    n = len(values)
    for _ in range(reps):
        flipped = [values[i] if rng.random() < 0.5 else -values[i] for i in range(n)]
        if abs(mean(flipped)) >= observed:
            count += 1
    return (count + 1) / (reps + 1)


# -----------------------------------------------------------------------------
# Data structures
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class ModelConfig:
    provider: str
    model: str

    @property
    def label(self) -> str:
        return f"{self.provider}:{self.model}"


@dataclass
class ModelResponse:
    answer: Optional[int]
    confidence: float
    abstained: bool
    raw_text: str


class ProgressTracker:
    def __init__(self, total_calls: int, enabled: bool = True):
        self.total_calls = max(1, total_calls)
        self.enabled = enabled
        self.completed = 0
        self.start = time.time()

    def tick(self, note: str = "") -> None:
        self.completed += 1
        if not self.enabled:
            return
        if self.completed == 1 or self.completed % 25 == 0 or self.completed >= self.total_calls:
            elapsed = time.time() - self.start
            rate = self.completed / elapsed if elapsed > 0 else 0.0
            remain = self.total_calls - self.completed
            eta = remain / rate if rate > 0 else float("inf")
            pct = 100.0 * self.completed / self.total_calls
            eta_str = f"{eta/60:.1f}m" if math.isfinite(eta) else "?"
            msg = (
                f"\rProgress: {self.completed}/{self.total_calls} ({pct:5.1f}%) "
                f"elapsed={elapsed/60:.1f}m eta={eta_str} {note:40s}"
            )
            print(msg, end="", file=sys.stderr, flush=True)
            if self.completed >= self.total_calls:
                print("", file=sys.stderr)


# -----------------------------------------------------------------------------
# Prompting + parsing
# -----------------------------------------------------------------------------


SYSTEM_PROMPT = (
    "You are a careful reasoning agent. Solve arithmetic exactly. "
    "Return strict JSON only: {\"answer\": <int>, \"confidence\": <float 0..1>}"
)


def worker_prompt(task: Task, role: str) -> str:
    return (
        f"Role: {role}.\n"
        f"Task: {task.text}.\n"
        "Provide only strict JSON with integer answer and confidence in [0,1]."
    )


def extract_json(text: str) -> Optional[Dict]:
    text = text.strip()
    try:
        obj = json.loads(text)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass

    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        return None
    snippet = match.group(0)
    try:
        obj = json.loads(snippet)
        if isinstance(obj, dict):
            return obj
    except Exception:
        return None
    return None


def parse_model_response(text: str) -> ModelResponse:
    obj = extract_json(text)
    if obj is None:
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=text)

    if "answer" not in obj or "confidence" not in obj:
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=text)

    answer = obj.get("answer")
    confidence = obj.get("confidence")

    try:
        answer_int = int(answer)
    except Exception:
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=text)

    try:
        confidence_float = float(confidence)
    except Exception:
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=text)

    if not (0.0 <= confidence_float <= 1.0):
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=text)

    return ModelResponse(answer=answer_int, confidence=confidence_float, abstained=False, raw_text=text)


# -----------------------------------------------------------------------------
# Provider clients (HTTP, dependency-free)
# -----------------------------------------------------------------------------


def _http_post_json(
    url: str,
    headers: Dict[str, str],
    payload: Dict,
    timeout: int = 60,
    max_retries: int = 5,
    backoff_s: float = 2.0,
) -> Dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")

    last_err: Optional[Exception] = None
    for attempt in range(max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8")
            return json.loads(body)
        except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError, OSError) as err:
            last_err = err
            if attempt >= max_retries:
                break
            sleep_s = backoff_s * (2 ** attempt)
            time.sleep(sleep_s)

    raise RuntimeError(f"HTTP request failed after {max_retries + 1} attempts: {last_err}")


def call_openai(model: str, user_prompt: str, api_key: str, timeout: int = 60, temperature: float = 0.0) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    obj = _http_post_json(url, headers, payload, timeout=timeout)
    return obj["choices"][0]["message"]["content"]


def call_anthropic(model: str, user_prompt: str, api_key: str, timeout: int = 60, temperature: float = 0.0) -> str:
    url = "https://api.anthropic.com/v1/messages"
    payload = {
        "model": model,
        "max_tokens": 256,
        "temperature": temperature,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_prompt}],
    }
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    obj = _http_post_json(url, headers, payload, timeout=timeout)
    content = obj.get("content", [])
    if isinstance(content, list) and content:
        return content[0].get("text", "")
    return ""


def call_gemini(model: str, user_prompt: str, api_key: str, timeout: int = 60, temperature: float = 0.0) -> str:
    model_enc = urllib.parse.quote(model, safe="")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_enc}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": f"{SYSTEM_PROMPT}\n\n{user_prompt}"}]}],
        "generationConfig": {"temperature": temperature},
    }
    headers = {"Content-Type": "application/json"}
    obj = _http_post_json(url, headers, payload, timeout=timeout)
    cands = obj.get("candidates", [])
    if not cands:
        return ""
    parts = cands[0].get("content", {}).get("parts", [])
    if not parts:
        return ""
    return parts[0].get("text", "")


def call_provider(model_cfg: ModelConfig, prompt: str, timeout: int = 60, temperature: float = 0.0) -> str:
    if model_cfg.provider == "openai":
        key = os.getenv("OPENAI_API_KEY", "")
        if not key:
            raise RuntimeError("OPENAI_API_KEY not set.")
        return call_openai(model_cfg.model, prompt, key, timeout=timeout, temperature=temperature)

    if model_cfg.provider == "anthropic":
        key = os.getenv("ANTHROPIC_API_KEY", "")
        if not key:
            raise RuntimeError("ANTHROPIC_API_KEY not set.")
        return call_anthropic(model_cfg.model, prompt, key, timeout=timeout, temperature=temperature)

    if model_cfg.provider == "gemini":
        key = os.getenv("GEMINI_API_KEY", "")
        if not key:
            raise RuntimeError("GEMINI_API_KEY not set.")
        return call_gemini(model_cfg.model, prompt, key, timeout=timeout, temperature=temperature)

    raise ValueError(f"Unknown provider: {model_cfg.provider}")


# -----------------------------------------------------------------------------
# Condition execution
# -----------------------------------------------------------------------------


def dry_run_response(task: Task, role: str, rng: random.Random) -> ModelResponse:
    base_skill = 0.83
    if role == "critic":
        base_skill = 0.80
    if role == "solver_b":
        base_skill = 0.82

    p_correct = max(0.05, min(0.98, base_skill * (1.0 - 0.55 * task.novelty)))
    correct = rng.random() < p_correct
    answer = task.answer if correct else task.answer + rng.randint(1, 6 + int(8 * task.novelty))
    conf = max(0.01, min(0.99, p_correct - 0.25 * task.novelty + rng.uniform(-0.03, 0.03)))
    return ModelResponse(answer=answer, confidence=conf, abstained=False, raw_text="dry-run")


def run_unscaffolded(
    task: Task,
    model_cfg: ModelConfig,
    dry_run: bool,
    rng: random.Random,
    pause_s: float,
    tracker: ProgressTracker,
    unscaffolded_temperature: float,
) -> ModelResponse:
    if dry_run:
        resp = dry_run_response(task, role="solver", rng=rng)
        tracker.tick(f"{model_cfg.label} unscaffolded")
        return resp

    prompt = worker_prompt(task, role="solver")
    try:
        text = call_provider(model_cfg, prompt, temperature=unscaffolded_temperature)
        time.sleep(pause_s)
        tracker.tick(f"{model_cfg.label} unscaffolded")
        return parse_model_response(text)
    except Exception as err:
        tracker.tick(f"{model_cfg.label} unscaffolded ERROR")
        print(f"\nWARN: {model_cfg.label} unscaffolded call failed: {err}", file=sys.stderr)
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=f"error:{err}")


def run_full_scaffold(
    task: Task,
    model_cfg: ModelConfig,
    dry_run: bool,
    rng: random.Random,
    pause_s: float,
    tracker: ProgressTracker,
    scaffold_temperature: float,
) -> ModelResponse:
    if dry_run:
        r1 = dry_run_response(task, role="solver_a", rng=rng)
        tracker.tick(f"{model_cfg.label} scaffold solver_a")
        r2 = dry_run_response(task, role="solver_b", rng=rng)
        tracker.tick(f"{model_cfg.label} scaffold solver_b")
        r3 = dry_run_response(task, role="critic", rng=rng)
        tracker.tick(f"{model_cfg.label} scaffold critic")
    else:
        def safe_role_call(role: str) -> ModelResponse:
            try:
                txt = call_provider(model_cfg, worker_prompt(task, role), temperature=scaffold_temperature)
                time.sleep(pause_s)
                tracker.tick(f"{model_cfg.label} scaffold {role}")
                return parse_model_response(txt)
            except Exception as err:
                tracker.tick(f"{model_cfg.label} scaffold {role} ERROR")
                print(f"\nWARN: {model_cfg.label} scaffold {role} call failed: {err}", file=sys.stderr)
                return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text=f"error:{err}")

        r1 = safe_role_call("solver_a")
        r2 = safe_role_call("solver_b")
        r3 = safe_role_call("critic")

    valid = [r for r in [r1, r2, r3] if not r.abstained and r.answer is not None]
    if not valid:
        return ModelResponse(answer=None, confidence=0.0, abstained=True, raw_text="all_abstained")

    tally: Dict[int, float] = {}
    for r in valid:
        w = r.confidence * (1.0 - max(0.0, r.confidence - 0.88))
        tally[r.answer] = tally.get(r.answer, 0.0) + w

    answer = max(tally.items(), key=lambda kv: kv[1])[0]
    mean_conf = sum(r.confidence for r in valid) / len(valid)

    if task.novelty >= 0.60 and len(tally) >= 3 and mean_conf < 0.45:
        return ModelResponse(answer=None, confidence=mean_conf * 0.7, abstained=True, raw_text="scaffold_abstain")

    return ModelResponse(answer=answer, confidence=mean_conf, abstained=False, raw_text="scaffold_consensus")


# -----------------------------------------------------------------------------
# Trial loop + metrics
# -----------------------------------------------------------------------------


def condition_metrics(
    tasks: List[Task],
    model_cfg: ModelConfig,
    condition: str,
    dry_run: bool,
    seed: int,
    pause_s: float,
    tracker: ProgressTracker,
    unscaffolded_temperature: float,
    scaffold_temperature: float,
) -> Dict[str, float]:
    rng = random.Random(seed)
    total = 0
    correct = 0
    abstain = 0
    novelty_bucket = 0
    novelty_errors = 0
    confident_novelty_errors = 0
    confidences: List[float] = []
    outcomes: List[float] = []

    for task in tasks:
        if condition == "unscaffolded":
            resp = run_unscaffolded(task, model_cfg, dry_run=dry_run, rng=rng, pause_s=pause_s, tracker=tracker, unscaffolded_temperature=unscaffolded_temperature)
        else:
            resp = run_full_scaffold(task, model_cfg, dry_run=dry_run, rng=rng, pause_s=pause_s, tracker=tracker, scaffold_temperature=scaffold_temperature)

        is_correct = (resp.answer == task.answer) if (not resp.abstained and resp.answer is not None) else False
        if resp.abstained:
            abstain += 1

        total += 1
        correct += int(is_correct)

        if task.novelty >= 0.60:
            novelty_bucket += 1
            if not is_correct:
                novelty_errors += 1
                if resp.confidence >= 0.40:
                    confident_novelty_errors += 1
            confidences.append(resp.confidence)
            outcomes.append(1.0 if is_correct else 0.0)

    if len(confidences) < 2:
        cal_r = 0.0
    else:
        mx = mean(confidences)
        my = mean(outcomes)
        num = sum((x - mx) * (y - my) for x, y in zip(confidences, outcomes))
        den_x = math.sqrt(sum((x - mx) ** 2 for x in confidences))
        den_y = math.sqrt(sum((y - my) ** 2 for y in outcomes))
        cal_r = num / (den_x * den_y) if den_x and den_y else 0.0

    return {
        "accuracy": correct / total if total else 0.0,
        "abstain_rate": abstain / total if total else 0.0,
        "novelty_error_rate": novelty_errors / novelty_bucket if novelty_bucket else 0.0,
        "confident_novelty_error_rate": confident_novelty_errors / novelty_bucket if novelty_bucket else 0.0,
        "novelty_calibration_r": cal_r,
    }


def run_model_study(
    model_cfg: ModelConfig,
    trials: int,
    tasks_per_trial: int,
    base_seed: int,
    dry_run: bool,
    pause_s: float,
    tracker: ProgressTracker,
    unscaffolded_temperature: float,
    scaffold_temperature: float,
) -> Dict[str, Dict[str, float]]:
    deltas = {
        "accuracy": [],
        "abstain_rate": [],
        "novelty_error_rate": [],
        "confident_novelty_error_rate": [],
        "novelty_calibration_r": [],
    }
    base_vals = {k: [] for k in deltas.keys()}
    full_vals = {k: [] for k in deltas.keys()}

    for i in range(trials):
        seed = base_seed + i
        tasks = generate_tasks(tasks_per_trial, seed)
        base = condition_metrics(tasks, model_cfg, "unscaffolded", dry_run=dry_run, seed=seed, pause_s=pause_s, tracker=tracker, unscaffolded_temperature=unscaffolded_temperature, scaffold_temperature=scaffold_temperature)
        full = condition_metrics(tasks, model_cfg, "full_scaffold", dry_run=dry_run, seed=seed + 10_000, pause_s=pause_s, tracker=tracker, unscaffolded_temperature=unscaffolded_temperature, scaffold_temperature=scaffold_temperature)

        for m in deltas.keys():
            deltas[m].append(full[m] - base[m])
            base_vals[m].append(base[m])
            full_vals[m].append(full[m])

    summary: Dict[str, Dict[str, float]] = {}
    for m, vals in deltas.items():
        lo, hi = bootstrap_ci(vals)
        nonzero = sum(1 for v in vals if abs(v) > 1e-12)
        summary[m] = {
            "base_mean": mean(base_vals[m]) if base_vals[m] else 0.0,
            "full_mean": mean(full_vals[m]) if full_vals[m] else 0.0,
            "mean_delta": mean(vals) if vals else 0.0,
            "sd_delta": stdev(vals) if len(vals) > 1 else 0.0,
            "ci95_lo": lo,
            "ci95_hi": hi,
            "p_perm": sign_flip_permutation_pvalue(vals),
            "nonzero_frac": (nonzero / len(vals)) if vals else 0.0,
        }
    return summary


def print_model_summary(model_cfg: ModelConfig, summary: Dict[str, Dict[str, float]]) -> None:
    print(f"\n=== {model_cfg.label} ===")
    print("metric                         base_mean   full_mean   mean_delta   95% CI                 p_perm   nz_frac")
    print("-" * 118)
    for metric, stats in summary.items():
        print(
            f"{metric:28s}"
            f"{stats['base_mean']:11.4f}"
            f"{stats['full_mean']:11.4f}"
            f"{stats['mean_delta']:11.4f}"
            f" [{stats['ci95_lo']:+.4f}, {stats['ci95_hi']:+.4f}]"
            f"  {stats['p_perm']:.4f}"
            f"   {stats['nonzero_frac']:.2f}"
        )


def estimate_total_calls(num_models: int, trials: int, tasks_per_trial: int) -> int:
    # per task: 1 unscaffolded + 3 scaffolded = 4 calls
    return num_models * trials * tasks_per_trial * 4


def print_staged_plan(num_models: int, trials: int, tasks_per_trial: int, pause_s: float, avg_latency_s: float) -> None:
    def stage_calls(t: int, k: int) -> int:
        return estimate_total_calls(num_models, t, k)

    dedup = stage_schedule(trials, tasks_per_trial)

    print("\nSuggested staged scaling plan:")
    print("stage                     calls      est_runtime")
    print("-" * 54)
    for t, k in dedup:
        calls = stage_calls(t, k)
        sec_per_call = max(0.0, pause_s) + max(0.0, avg_latency_s)
        est_sec = calls * sec_per_call
        print(f"trials={t:<3d} tasks={k:<3d}   {calls:<10d} {est_sec/3600:8.2f}h")


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def parse_models(args: argparse.Namespace) -> List[ModelConfig]:
    models: List[ModelConfig] = []
    if args.openai_model:
        models.append(ModelConfig("openai", args.openai_model))
    if args.anthropic_model:
        models.append(ModelConfig("anthropic", args.anthropic_model))
    if args.gemini_model:
        models.append(ModelConfig("gemini", args.gemini_model))
    if not models:
        raise ValueError("Specify at least one model via --openai-model / --anthropic-model / --gemini-model")
    return models


def stage_schedule(final_trials: int, final_tasks: int) -> List[Tuple[int, int]]:
    candidates = [
        (min(3, final_trials), min(20, final_tasks)),
        (min(10, final_trials), min(30, final_tasks)),
        (min(25, final_trials), min(60, final_tasks)),
        (final_trials, final_tasks),
    ]
    out: List[Tuple[int, int]] = []
    seen = set()
    for s in candidates:
        if s[0] <= 0 or s[1] <= 0:
            continue
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out


def run_stage(
    models: List[ModelConfig],
    trials: int,
    tasks_per_trial: int,
    base_seed: int,
    dry_run: bool,
    pause_s: float,
    show_progress: bool,
    unscaffolded_temperature: float,
    scaffold_temperature: float,
) -> None:
    total_calls = estimate_total_calls(len(models), trials, tasks_per_trial)
    tracker = ProgressTracker(total_calls=total_calls, enabled=show_progress)

    print(f"\nRunning stage: trials={trials}, tasks_per_trial={tasks_per_trial}, estimated_calls={total_calls}")
    for m in models:
        summary = run_model_study(
            m,
            trials=trials,
            tasks_per_trial=tasks_per_trial,
            base_seed=base_seed,
            dry_run=dry_run,
            pause_s=pause_s,
            tracker=tracker,
            unscaffolded_temperature=unscaffolded_temperature,
            scaffold_temperature=scaffold_temperature,
        )
        print_model_summary(m, summary)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run API-backed paired scaffold study across multiple model providers.")
    parser.add_argument("--openai-model", type=str, default="", help="OpenAI model name (optional).")
    parser.add_argument("--anthropic-model", type=str, default="", help="Anthropic model name (optional).")
    parser.add_argument("--gemini-model", type=str, default="", help="Gemini model name (optional).")
    parser.add_argument("--trials", type=int, default=50, help="Paired trials per model.")
    parser.add_argument("--tasks-per-trial", type=int, default=100, help="Tasks per trial.")
    parser.add_argument("--base-seed", type=int, default=2000, help="Starting seed.")
    parser.add_argument("--pause-s", type=float, default=0.1, help="Sleep between API calls.")
    parser.add_argument("--dry-run", action="store_true", help="Run without calling external APIs.")
    parser.add_argument("--staged-run", action="store_true", help="Run staged scaling schedule before final size.")
    parser.add_argument("--print-plan", action="store_true", help="Print staged scaling call/runtime estimates and continue.")
    parser.add_argument("--avg-latency-s", type=float, default=2.0, help="Assumed average API latency for runtime estimate.")
    parser.add_argument("--no-progress", action="store_true", help="Disable progress display.")
    parser.add_argument("--unscaffolded-temperature", type=float, default=0.0, help="Sampling temperature for unscaffolded calls.")
    parser.add_argument("--scaffold-temperature", type=float, default=0.7, help="Sampling temperature for scaffold role calls.")
    args = parser.parse_args()

    models = parse_models(args)
    show_progress = not args.no_progress

    if not args.dry_run:
        print("WARNING: live API mode may incur costs.")

    print_staged_plan(len(models), args.trials, args.tasks_per_trial, args.pause_s, args.avg_latency_s)
    if args.print_plan:
        print("\nPlan shown above. Continuing with run...")

    if args.staged_run:
        for t, k in stage_schedule(args.trials, args.tasks_per_trial):
            run_stage(
                models=models,
                trials=t,
                tasks_per_trial=k,
                base_seed=args.base_seed,
                dry_run=args.dry_run,
                pause_s=args.pause_s,
                show_progress=show_progress,
                unscaffolded_temperature=args.unscaffolded_temperature,
                scaffold_temperature=args.scaffold_temperature,
            )
    else:
        run_stage(
            models=models,
            trials=args.trials,
            tasks_per_trial=args.tasks_per_trial,
            base_seed=args.base_seed,
            dry_run=args.dry_run,
            pause_s=args.pause_s,
            show_progress=show_progress,
            unscaffolded_temperature=args.unscaffolded_temperature,
            scaffold_temperature=args.scaffold_temperature,
        )


if __name__ == "__main__":
    main()

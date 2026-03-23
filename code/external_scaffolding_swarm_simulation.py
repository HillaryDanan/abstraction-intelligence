#!/usr/bin/env python3
"""
External Scaffolding Experiment for LLM Self-Monitoring in a Swarm Context.

This script operationalizes the repository's core claim that self-monitoring is
best identified by failure topology on novel tasks (calibration, confidence
collapse, conservative fallback), not by raw accuracy alone.

It supports:
- Standard condition runs (unscaffolded vs full scaffold)
- Partial-scaffold ablation runs
- Parameter-sensitivity grid runs with stability summaries
"""

from __future__ import annotations

import argparse
import itertools
import math
import random
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Tuple

ABSTAIN_SENTINEL = -999999


@dataclass(frozen=True)
class Task:
    text: str
    answer: int
    novelty: float


@dataclass
class AgentResponse:
    answer: int
    confidence: float
    abstained: bool


@dataclass
class AgentState:
    name: str
    base_skill: float
    calibration: float
    caution_bias: float
    novelty_sensitivity: float
    recent_accuracy: float = 0.75
    history: List[int] = field(default_factory=list)

    def update(self, correct: bool) -> None:
        self.history.append(1 if correct else 0)
        if len(self.history) > 25:
            self.history = self.history[-25:]
        mean = sum(self.history) / len(self.history)
        self.recent_accuracy = 0.8 * self.recent_accuracy + 0.2 * mean


@dataclass(frozen=True)
class ScaffoldConfig:
    name: str
    use_shared_memory: bool
    use_novelty_detector: bool
    use_confidence_gating: bool
    use_verifier_arbitration: bool


@dataclass(frozen=True)
class SimulationParams:
    novelty_penalty: float = 0.35
    gating_load_penalty: float = 0.20
    overconfidence_scale: float = 0.30
    overconfidence_bias: float = 0.10
    verifier_spike_cap: float = 0.88
    verifier_disagreement_conf_threshold: float = 0.45


class WorkerAgent:
    def __init__(self, state: AgentState):
        self.state = state

    def solve(
        self,
        task: Task,
        cfg: ScaffoldConfig,
        params: SimulationParams,
        memory_signal: float,
    ) -> AgentResponse:
        s = self.state

        skill = s.base_skill * (1.0 - 0.55 * task.novelty)
        if cfg.use_shared_memory:
            skill += 0.10 * memory_signal
            skill += 0.08 * s.recent_accuracy
        skill = max(0.05, min(0.98, skill))

        uncertainty = (1.0 - skill) * (0.6 + 0.4 * task.novelty)
        raw_conf = skill - s.calibration * uncertainty

        novelty_alert = task.novelty * s.novelty_sensitivity
        if cfg.use_novelty_detector:
            raw_conf -= params.novelty_penalty * novelty_alert

        if cfg.use_confidence_gating:
            raw_conf -= params.gating_load_penalty * max(0.0, 0.6 - s.recent_accuracy)
            raw_conf -= s.caution_bias
        else:
            raw_conf += params.overconfidence_scale * (1.0 - s.calibration) + params.overconfidence_bias

        confidence = max(0.01, min(0.99, raw_conf))
        abstain_threshold = 0.22 if cfg.use_confidence_gating else 0.06
        abstained = confidence < abstain_threshold

        correct = random.random() < skill
        answer = task.answer if correct else task.answer + random.randint(1, 6 + int(8 * task.novelty))
        if abstained:
            answer = ABSTAIN_SENTINEL

        return AgentResponse(answer=answer, confidence=confidence, abstained=abstained)


class SwarmScaffold:
    def __init__(self) -> None:
        self.shared_memory_accuracy = 0.7
        self.novelty_running_mean = 0.0

    def update_memory(self, correct: bool, novelty: float, cfg: ScaffoldConfig) -> None:
        self.novelty_running_mean = 0.95 * self.novelty_running_mean + 0.05 * novelty
        if cfg.use_shared_memory:
            self.shared_memory_accuracy = 0.9 * self.shared_memory_accuracy + 0.1 * (1.0 if correct else 0.0)

    def aggregator(
        self,
        responses: List[AgentResponse],
        cfg: ScaffoldConfig,
        params: SimulationParams,
    ) -> Tuple[int, float, bool]:
        valid = [r for r in responses if not r.abstained]
        if not valid:
            return ABSTAIN_SENTINEL, 0.0, True

        tally: Dict[int, float] = {}
        for r in valid:
            weight = r.confidence
            if cfg.use_verifier_arbitration:
                weight *= 1.0 - max(0.0, r.confidence - params.verifier_spike_cap)
            tally[r.answer] = tally.get(r.answer, 0.0) + weight

        best_answer = max(tally.items(), key=lambda kv: kv[1])[0]
        mean_conf = sum(r.confidence for r in valid) / len(valid)

        if (
            cfg.use_verifier_arbitration
            and len(tally) >= 3
            and mean_conf < params.verifier_disagreement_conf_threshold
        ):
            return ABSTAIN_SENTINEL, mean_conf * 0.7, True
        return best_answer, mean_conf, False


def generate_tasks(n: int, seed: int) -> List[Task]:
    rng = random.Random(seed)
    tasks: List[Task] = []
    for _ in range(n):
        novelty = min(1.0, max(0.0, rng.betavariate(2, 3)))
        a = rng.randint(1, 15 + int(30 * novelty))
        b = rng.randint(1, 12 + int(20 * novelty))
        c = rng.randint(1, 6 + int(10 * novelty))
        op = rng.choice(["+", "-", "*"])

        if op == "+":
            answer = a + b - c
            text = f"Compute ({a} + {b}) - {c}"
        elif op == "-":
            answer = a - b + c
            text = f"Compute ({a} - {b}) + {c}"
        else:
            answer = a * b - c
            text = f"Compute ({a} * {b}) - {c}"
        tasks.append(Task(text=text, answer=answer, novelty=novelty))
    return tasks


def pearson(xs: List[float], ys: List[float]) -> float:
    n = len(xs)
    if n < 2:
        return 0.0
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den_x = math.sqrt(sum((x - mx) ** 2 for x in xs))
    den_y = math.sqrt(sum((y - my) ** 2 for y in ys))
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y)


def run_condition(
    tasks: List[Task],
    cfg: ScaffoldConfig,
    params: SimulationParams,
    seed: int,
) -> Dict[str, float]:
    random.seed(seed)
    agents = [
        WorkerAgent(AgentState("planner", 0.86, 0.72, 0.08, 0.95)),
        WorkerAgent(AgentState("critic", 0.82, 0.78, 0.10, 0.92)),
        WorkerAgent(AgentState("tool", 0.88, 0.69, 0.05, 0.80)),
        WorkerAgent(AgentState("synthesizer", 0.84, 0.75, 0.09, 0.90)),
    ]

    scaffold = SwarmScaffold()
    total = 0
    correct = 0
    abstain = 0
    novelty_bucket = 0
    novelty_errors = 0
    confident_novelty_errors = 0
    confidences: List[float] = []
    outcomes: List[float] = []

    for task in tasks:
        responses = [agent.solve(task, cfg, params, scaffold.shared_memory_accuracy) for agent in agents]
        final_answer, final_conf, abstained = scaffold.aggregator(responses, cfg, params)

        is_correct = final_answer == task.answer
        if abstained:
            abstain += 1
            is_correct = False

        total += 1
        correct += 1 if is_correct else 0

        for agent, response in zip(agents, responses):
            if not response.abstained:
                agent.state.update(response.answer == task.answer)

        scaffold.update_memory(correct=is_correct, novelty=task.novelty, cfg=cfg)

        if task.novelty >= 0.60:
            novelty_bucket += 1
            if not is_correct:
                novelty_errors += 1
                if final_conf >= 0.40:
                    confident_novelty_errors += 1
            confidences.append(final_conf)
            outcomes.append(1.0 if is_correct else 0.0)

    return {
        "accuracy": correct / total if total else 0.0,
        "abstain_rate": abstain / total if total else 0.0,
        "novelty_error_rate": novelty_errors / novelty_bucket if novelty_bucket else 0.0,
        "confident_novelty_error_rate": confident_novelty_errors / novelty_bucket if novelty_bucket else 0.0,
        "novelty_calibration_r": pearson(confidences, outcomes),
        "novel_tasks": float(novelty_bucket),
    }


def experiment_configs(ablation: bool) -> List[ScaffoldConfig]:
    base = [
        ScaffoldConfig("unscaffolded", False, False, False, False),
        ScaffoldConfig("full_scaffold", True, True, True, True),
    ]
    if not ablation:
        return base
    return [
        base[0],
        ScaffoldConfig("memory_only", True, False, False, False),
        ScaffoldConfig("memory_gating_no_novelty", True, False, True, False),
        ScaffoldConfig("gating_no_arbitration", False, True, True, False),
        ScaffoldConfig("full_no_memory", False, True, True, True),
        ScaffoldConfig("full_no_novelty", True, False, True, True),
        ScaffoldConfig("full_no_gating", True, True, False, True),
        ScaffoldConfig("full_no_verifier", True, True, True, False),
        base[1],
    ]


def validate_configs(configs: List[ScaffoldConfig]) -> None:
    seen_names = set()
    seen_shapes = set()
    for cfg in configs:
        if cfg.name in seen_names:
            raise ValueError(f"Duplicate condition name: {cfg.name}")
        seen_names.add(cfg.name)

        shape = (
            cfg.use_shared_memory,
            cfg.use_novelty_detector,
            cfg.use_confidence_gating,
            cfg.use_verifier_arbitration,
        )
        if shape in seen_shapes:
            raise ValueError(f"Duplicate scaffold shape detected for condition: {cfg.name}")
        seen_shapes.add(shape)


def print_report(results: Dict[str, Dict[str, float]]) -> None:
    print("\n=== External Scaffolding for Swarm Self-Monitoring ===")
    print("condition                    accuracy   abstain  nov_err  conf_nov_err  cal_r")
    print("-" * 78)
    for name, metrics in results.items():
        print(
            f"{name:26s}"
            f"{metrics['accuracy']:9.3f}"
            f"{metrics['abstain_rate']:10.3f}"
            f"{metrics['novelty_error_rate']:9.3f}"
            f"{metrics['confident_novelty_error_rate']:14.3f}"
            f"{metrics['novelty_calibration_r']:8.3f}"
        )

    print("\nInterpretation:")
    print("- Better self-monitoring signature means lower confident_novelty_error_rate")
    print("  and higher novelty_calibration_r, with a moderate increase in abstain_rate.")


def sensitivity_grid(mode: str = "coarse") -> List[SimulationParams]:
    if mode == "coarse":
        novelty_penalties = [0.20, 0.35, 0.50]
        gating_penalties = [0.10, 0.20, 0.30]
        overconfidence_biases = [0.00, 0.10, 0.20]
        overconfidence_scales = [0.30]
        verifier_thresholds = [0.45]
    elif mode == "wide":
        # Wider/harsher sweep to expose fragility boundaries.
        novelty_penalties = [0.00, 0.15, 0.35, 0.60, 0.85]
        gating_penalties = [0.00, 0.10, 0.25, 0.40, 0.60]
        overconfidence_biases = [0.00, 0.10, 0.20, 0.35]
        overconfidence_scales = [0.10, 0.30, 0.60]
        verifier_thresholds = [0.30, 0.45, 0.60]
    else:
        raise ValueError(f"Unknown sensitivity grid mode: {mode}")

    grid: List[SimulationParams] = []
    for np, gp, ob, os, vt in itertools.product(
        novelty_penalties,
        gating_penalties,
        overconfidence_biases,
        overconfidence_scales,
        verifier_thresholds,
    ):
        grid.append(
            SimulationParams(
                novelty_penalty=np,
                gating_load_penalty=gp,
                overconfidence_scale=os,
                overconfidence_bias=ob,
                verifier_spike_cap=0.88,
                verifier_disagreement_conf_threshold=vt,
            )
        )
    return grid


def parse_seed_list(seed_list: str) -> List[int]:
    seeds = [int(x.strip()) for x in seed_list.split(",") if x.strip()]
    if not seeds:
        raise ValueError("At least one seed must be provided.")
    return seeds


def parameter_labels(params: SimulationParams) -> List[str]:
    return [
        f"novelty_penalty={params.novelty_penalty:.2f}",
        f"gating_penalty={params.gating_load_penalty:.2f}",
        f"overconf_bias={params.overconfidence_bias:.2f}",
        f"overconf_scale={params.overconfidence_scale:.2f}",
        f"verifier_thresh={params.verifier_disagreement_conf_threshold:.2f}",
    ]


def run_sensitivity(
    task_count: int,
    seeds: Iterable[int],
    grid: List[SimulationParams],
) -> Dict[str, float]:
    cfg_base = ScaffoldConfig("unscaffolded", False, False, False, False)
    cfg_full = ScaffoldConfig("full_scaffold", True, True, True, True)

    total_runs = 0
    score_conf_err = 0
    score_cal = 0
    score_abstain = 0
    score_accuracy = 0
    score_signature_all = 0

    delta_conf_err_total = 0.0
    delta_cal_total = 0.0
    delta_abstain_total = 0.0
    delta_accuracy_total = 0.0

    fragility_buckets: Dict[str, List[int]] = {}
    for params in grid:
        for label in parameter_labels(params):
            fragility_buckets.setdefault(label, [0, 0])

    for params in grid:
        for seed in seeds:
            total_runs += 1
            tasks = generate_tasks(task_count, seed)
            base = run_condition(tasks, cfg=cfg_base, params=params, seed=seed)
            full = run_condition(tasks, cfg=cfg_full, params=params, seed=seed)

            delta_conf_err = base["confident_novelty_error_rate"] - full["confident_novelty_error_rate"]
            delta_cal = full["novelty_calibration_r"] - base["novelty_calibration_r"]
            delta_abstain = full["abstain_rate"] - base["abstain_rate"]
            delta_accuracy = full["accuracy"] - base["accuracy"]

            delta_conf_err_total += delta_conf_err
            delta_cal_total += delta_cal
            delta_abstain_total += delta_abstain
            delta_accuracy_total += delta_accuracy

            ok_conf_err = delta_conf_err >= 0.0
            ok_cal = delta_cal >= 0.0
            ok_abstain = delta_abstain >= 0.0
            ok_accuracy = delta_accuracy >= 0.0
            ok_signature = ok_conf_err and ok_cal and ok_abstain

            score_conf_err += int(ok_conf_err)
            score_cal += int(ok_cal)
            score_abstain += int(ok_abstain)
            score_accuracy += int(ok_accuracy)
            score_signature_all += int(ok_signature)

            for label in parameter_labels(params):
                fragility_buckets[label][1] += 1
                fragility_buckets[label][0] += int(ok_signature)

    def rate(x: int) -> float:
        return x / total_runs if total_runs else 0.0

    summary: Dict[str, float] = {
        "runs": float(total_runs),
        "p_confident_error_improves": rate(score_conf_err),
        "p_calibration_improves": rate(score_cal),
        "p_abstain_increases": rate(score_abstain),
        "p_accuracy_improves": rate(score_accuracy),
        "p_signature_all_three": rate(score_signature_all),
        "mean_delta_confident_error": delta_conf_err_total / total_runs if total_runs else 0.0,
        "mean_delta_calibration": delta_cal_total / total_runs if total_runs else 0.0,
        "mean_delta_abstain": delta_abstain_total / total_runs if total_runs else 0.0,
        "mean_delta_accuracy": delta_accuracy_total / total_runs if total_runs else 0.0,
    }

    for label, (wins, count) in fragility_buckets.items():
        summary[f"signature_rate::{label}"] = wins / count if count else 0.0

    return summary


def print_sensitivity_summary(summary: Dict[str, float]) -> None:
    print("\n=== Parameter-Sensitivity Stability Summary ===")
    print(f"runs: {int(summary['runs'])}")
    print("(Each seed regenerates a fresh task set; full vs unscaffolded are compared on matched tasks per seed.)")
    print("\nPrimary robustness rates (full scaffold vs unscaffolded):")
    print(f"- confident novelty error improves: {summary['p_confident_error_improves']:.3f}")
    print(f"- novelty calibration improves:     {summary['p_calibration_improves']:.3f}")
    print(f"- abstention increases:             {summary['p_abstain_increases']:.3f}")
    print(f"- all three signature criteria:     {summary['p_signature_all_three']:.3f}")
    print(f"- accuracy improves:                {summary['p_accuracy_improves']:.3f}")

    print("\nMean deltas (full - unscaffolded, except confident error is unscaffolded - full):")
    print(f"- delta confident novelty error: {summary['mean_delta_confident_error']:+.3f}")
    print(f"- delta novelty calibration:     {summary['mean_delta_calibration']:+.3f}")
    print(f"- delta abstain rate:            {summary['mean_delta_abstain']:+.3f}")
    print(f"- delta accuracy:                {summary['mean_delta_accuracy']:+.3f}")

    print("\nFragility by coefficient value (rate of satisfying all three signature criteria):")
    fragility_keys = [k for k in summary.keys() if k.startswith("signature_rate::")]
    for key in sorted(fragility_keys):
        label = key.replace("signature_rate::", "")
        print(f"- {label:24s} {summary[key]:.3f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Test external scaffolding for self-monitoring in an LLM-like agent swarm.")
    parser.add_argument("--tasks", type=int, default=400, help="Number of synthetic tasks.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed for standard/ablation runs.")
    parser.add_argument(
        "--ablation",
        action="store_true",
        help="Run partial scaffold conditions to measure graceful degradation.",
    )
    parser.add_argument(
        "--sensitivity",
        action="store_true",
        help="Run parameter sensitivity grid and print stability summary.",
    )
    parser.add_argument(
        "--sensitivity-seeds",
        type=str,
        default="0,1,2,3,5,7,11,17,23,42",
        help="Comma-separated seeds for sensitivity run.",
    )
    parser.add_argument(
        "--sensitivity-grid",
        type=str,
        default="coarse",
        choices=["coarse", "wide"],
        help="Grid definition for sensitivity sweep.",
    )
    args = parser.parse_args()

    tasks = generate_tasks(args.tasks, args.seed)

    if args.sensitivity:
        seeds = parse_seed_list(args.sensitivity_seeds)
        grid = sensitivity_grid(mode=args.sensitivity_grid)
        summary = run_sensitivity(task_count=args.tasks, seeds=seeds, grid=grid)
        print(f"Running sensitivity grid mode: {args.sensitivity_grid} ({len(grid)} parameter combinations)")
        print_sensitivity_summary(summary)
        return

    configs = experiment_configs(args.ablation)
    validate_configs(configs)

    params = SimulationParams()
    results: Dict[str, Dict[str, float]] = {}
    for cfg in configs:
        results[cfg.name] = run_condition(tasks, cfg=cfg, params=params, seed=args.seed)

    print_report(results)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
External Scaffolding Experiment for LLM Self-Monitoring in a Swarm Context.

This script operationalizes the repository's core claim that self-monitoring is
best identified by failure topology on novel tasks (calibration, confidence
collapse, conservative fallback), not by raw accuracy alone.

It supports a full scaffold and partial-scaffold ablations to test graceful
degradation as components are removed.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

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


class WorkerAgent:
    def __init__(self, state: AgentState):
        self.state = state

    def solve(self, task: Task, cfg: ScaffoldConfig, memory_signal: float) -> AgentResponse:
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
            raw_conf -= 0.35 * novelty_alert

        if cfg.use_confidence_gating:
            raw_conf -= 0.20 * max(0.0, 0.6 - s.recent_accuracy)
            raw_conf -= s.caution_bias
        else:
            # Overconfidence bias in absent guardrail condition.
            raw_conf += 0.30 * (1.0 - s.calibration) + 0.10

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

    def aggregator(self, responses: List[AgentResponse], cfg: ScaffoldConfig) -> Tuple[int, float, bool]:
        valid = [r for r in responses if not r.abstained]
        if not valid:
            return ABSTAIN_SENTINEL, 0.0, True

        tally: Dict[int, float] = {}
        for r in valid:
            weight = r.confidence
            if cfg.use_verifier_arbitration:
                weight *= 1.0 - max(0.0, r.confidence - 0.88)
            tally[r.answer] = tally.get(r.answer, 0.0) + weight

        best_answer = max(tally.items(), key=lambda kv: kv[1])[0]
        mean_conf = sum(r.confidence for r in valid) / len(valid)

        if cfg.use_verifier_arbitration and len(tally) >= 3 and mean_conf < 0.45:
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


def run_condition(tasks: List[Task], cfg: ScaffoldConfig, seed: int) -> Dict[str, float]:
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
        responses = [agent.solve(task, cfg, scaffold.shared_memory_accuracy) for agent in agents]
        final_answer, final_conf, abstained = scaffold.aggregator(responses, cfg)

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
        ScaffoldConfig("memory_no_novelty", True, False, True, True),
        ScaffoldConfig("gating_no_arbitration", False, True, True, False),
        ScaffoldConfig("full_no_memory", False, True, True, True),
        ScaffoldConfig("full_no_novelty", True, False, True, True),
        ScaffoldConfig("full_no_gating", True, True, False, True),
        ScaffoldConfig("full_no_verifier", True, True, True, False),
        base[1],
    ]


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Test external scaffolding for self-monitoring in an LLM-like agent swarm.")
    parser.add_argument("--tasks", type=int, default=400, help="Number of synthetic tasks.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed.")
    parser.add_argument(
        "--ablation",
        action="store_true",
        help="Run partial scaffold conditions to measure graceful degradation.",
    )
    args = parser.parse_args()

    tasks = generate_tasks(args.tasks, args.seed)
    configs = experiment_configs(args.ablation)

    results: Dict[str, Dict[str, float]] = {}
    for cfg in configs:
        results[cfg.name] = run_condition(tasks, cfg=cfg, seed=args.seed)

    print_report(results)


if __name__ == "__main__":
    main()

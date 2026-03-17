#!/usr/bin/env python3
"""
External Scaffolding Experiment for LLM Self-Monitoring in a Swarm Context.

This script operationalizes the repository's core claim that self-monitoring is
best identified by failure topology on novel tasks (calibration, confidence
collapse, conservative fallback), not by raw accuracy alone.

We compare two conditions over the same synthetic task stream:
1) Unscaffolded swarm: agents answer independently with weak confidence control.
2) Scaffolded swarm: agents get external supports (novelty detector, verifier,
   confidence gate, shared memory, and arbitration).

The outputs let you inspect whether external scaffolding creates a
self-monitoring-like signature in aggregate behavior.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class Task:
    """A small symbolic reasoning problem with controlled novelty."""

    text: str
    answer: int
    novelty: float  # 0.0 = in-distribution, 1.0 = highly novel


@dataclass
class AgentResponse:
    answer: int
    confidence: float
    abstained: bool


@dataclass
class AgentState:
    """Compressed self-like state used by each simulated worker."""

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


class WorkerAgent:
    def __init__(self, state: AgentState):
        self.state = state

    def solve(self, task: Task, scaffolded: bool, memory_signal: float) -> AgentResponse:
        """Return an answer + confidence; optionally leverage scaffold hints."""
        s = self.state

        # Probability of correctness degrades with novelty, but scaffolding helps.
        skill = s.base_skill * (1.0 - 0.55 * task.novelty)
        if scaffolded:
            skill += 0.10 * memory_signal
            skill += 0.08 * s.recent_accuracy
        skill = max(0.05, min(0.98, skill))

        # Internal confidence estimate (intentionally imperfect in unscaffolded case).
        uncertainty = (1.0 - skill) * (0.6 + 0.4 * task.novelty)
        raw_conf = skill - s.calibration * uncertainty

        novelty_alert = task.novelty * s.novelty_sensitivity
        if scaffolded:
            # External novelty detector + caution gate.
            raw_conf -= 0.35 * novelty_alert
            raw_conf -= 0.20 * max(0.0, 0.6 - s.recent_accuracy)
            raw_conf -= s.caution_bias
        else:
            # Without scaffold, novelty under-penalized and overconfidence creeps in.
            raw_conf += 0.30 * (1.0 - s.calibration) + 0.10

        confidence = max(0.01, min(0.99, raw_conf))

        # abstention policy emulates conservative error mode
        abstain_threshold = 0.22 if scaffolded else 0.06
        abstained = confidence < abstain_threshold

        correct = random.random() < skill
        if correct:
            answer = task.answer
        else:
            # Wrong answer distribution broadens with novelty.
            noise = random.randint(1, 6 + int(8 * task.novelty))
            answer = task.answer + noise

        if abstained:
            answer = -999999  # sentinel

        return AgentResponse(answer=answer, confidence=confidence, abstained=abstained)


class SwarmScaffold:
    """External coordination substrate for self-monitoring-like behavior."""

    def __init__(self) -> None:
        self.shared_memory_accuracy = 0.7
        self.novelty_running_mean = 0.0
        self.rounds = 0

    def update_memory(self, correct: bool, novelty: float) -> None:
        self.rounds += 1
        self.shared_memory_accuracy = 0.9 * self.shared_memory_accuracy + 0.1 * (1.0 if correct else 0.0)
        self.novelty_running_mean = 0.95 * self.novelty_running_mean + 0.05 * novelty

    def aggregator(self, responses: List[AgentResponse], scaffolded: bool) -> Tuple[int, float, bool]:
        """Arbitrate swarm output with optional verification pressure."""
        valid = [r for r in responses if not r.abstained]
        if not valid:
            return -999999, 0.0, True

        # Weighted consensus.
        tally: Dict[int, float] = {}
        for r in valid:
            weight = r.confidence
            if scaffolded:
                # verifier pressure downweights very high confidence spikes
                weight *= 1.0 - max(0.0, r.confidence - 0.88)
            tally[r.answer] = tally.get(r.answer, 0.0) + weight

        best_answer = max(tally.items(), key=lambda kv: kv[1])[0]
        mean_conf = sum(r.confidence for r in valid) / len(valid)

        # If disagreement is large, scaffold opts for caution.
        if scaffolded and len(tally) >= 3 and mean_conf < 0.45:
            return -999999, mean_conf * 0.7, True
        return best_answer, mean_conf, False


def generate_tasks(n: int, seed: int) -> List[Task]:
    rng = random.Random(seed)
    tasks: List[Task] = []
    for i in range(n):
        novelty = min(1.0, max(0.0, rng.betavariate(2, 3)))
        # Mix of expressions; novelty controls larger operators/ranges.
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


def run_condition(tasks: List[Task], scaffolded: bool, seed: int) -> Dict[str, float]:
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
        responses = [
            agent.solve(task, scaffolded=scaffolded, memory_signal=scaffold.shared_memory_accuracy)
            for agent in agents
        ]
        final_answer, final_conf, abstained = scaffold.aggregator(responses, scaffolded=scaffolded)

        is_correct = final_answer == task.answer
        if abstained:
            abstain += 1
            is_correct = False

        total += 1
        correct += 1 if is_correct else 0

        for agent, response in zip(agents, responses):
            # Only learning from non-abstained trajectory for simplicity.
            if not response.abstained:
                agent.state.update(response.answer == task.answer)

        scaffold.update_memory(correct=is_correct, novelty=task.novelty)

        # focus metric on high novelty tests (self-monitoring signature)
        if task.novelty >= 0.60:
            novelty_bucket += 1
            if not is_correct:
                novelty_errors += 1
                if final_conf >= 0.40:
                    confident_novelty_errors += 1
            confidences.append(final_conf)
            outcomes.append(1.0 if is_correct else 0.0)

    acc = correct / total if total else 0.0
    abstain_rate = abstain / total if total else 0.0
    novelty_error_rate = novelty_errors / novelty_bucket if novelty_bucket else 0.0
    confident_error_rate = confident_novelty_errors / novelty_bucket if novelty_bucket else 0.0
    calibration = pearson(confidences, outcomes)

    return {
        "accuracy": acc,
        "abstain_rate": abstain_rate,
        "novelty_error_rate": novelty_error_rate,
        "confident_novelty_error_rate": confident_error_rate,
        "novelty_calibration_r": calibration,
        "novel_tasks": float(novelty_bucket),
    }


def print_report(base: Dict[str, float], scaff: Dict[str, float]) -> None:
    print("\n=== External Scaffolding for Swarm Self-Monitoring ===")
    print("Metric                              Unscaffolded    Scaffolded")
    print("-" * 64)
    keys = [
        "accuracy",
        "abstain_rate",
        "novelty_error_rate",
        "confident_novelty_error_rate",
        "novelty_calibration_r",
    ]
    for k in keys:
        print(f"{k:34s} {base[k]:12.3f} {scaff[k]:12.3f}")

    print("\nInterpretation:")
    print("- Better self-monitoring signature means:")
    print("  * LOWER confident_novelty_error_rate")
    print("  * HIGHER novelty_calibration_r")
    print("  * Some increase in abstain_rate (conservative fallback)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Test external scaffolding for self-monitoring in an LLM-like agent swarm.")
    parser.add_argument("--tasks", type=int, default=400, help="Number of synthetic tasks.")
    parser.add_argument("--seed", type=int, default=7, help="Random seed.")
    args = parser.parse_args()

    tasks = generate_tasks(args.tasks, args.seed)
    baseline = run_condition(tasks, scaffolded=False, seed=args.seed)
    scaffolded = run_condition(tasks, scaffolded=True, seed=args.seed)
    print_report(baseline, scaffolded)


if __name__ == "__main__":
    main()

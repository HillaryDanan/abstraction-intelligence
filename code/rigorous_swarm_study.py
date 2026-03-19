#!/usr/bin/env python3
"""
Rigorous statistical study wrapper for the external scaffolding swarm simulation.

This script runs repeated paired trials (matched tasks per seed) and reports:
- Mean effects between full_scaffold and unscaffolded
- Nonparametric bootstrap confidence intervals
- Paired sign-flip permutation p-values
- Approximate minimum sample size estimates for 80%/90% power

It is designed as a reproducible analysis layer on top of
`external_scaffolding_swarm_simulation.py`.
"""

from __future__ import annotations

import argparse
import csv
import math
import random
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, stdev
from typing import Callable, Dict, List, Tuple

from external_scaffolding_swarm_simulation import (
    ScaffoldConfig,
    SimulationParams,
    generate_tasks,
    run_condition,
)


@dataclass(frozen=True)
class MetricSpec:
    name: str
    better_direction: str  # "higher" or "lower"


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
    """Two-sided sign-flip permutation test on paired differences."""
    if not values:
        return 1.0
    rng = random.Random(seed)
    observed = abs(mean(values))
    n = len(values)
    count = 0
    for _ in range(reps):
        flipped = [v if rng.random() < 0.5 else -v for v in values]
        if abs(mean(flipped)) >= observed:
            count += 1
    return (count + 1) / (reps + 1)


def approximate_required_n(effect_mean: float, effect_sd: float, alpha: float = 0.05, power: float = 0.8) -> float:
    """Normal-approx paired design sample size estimate."""
    if effect_sd <= 0:
        return 1.0
    effect = abs(effect_mean)
    if effect < 1e-12:
        return float("inf")

    # z-scores for common power levels (kept dependency-free)
    z_alpha = 1.96 if alpha == 0.05 else 1.96
    if abs(power - 0.8) < 1e-9:
        z_beta = 0.84
    elif abs(power - 0.9) < 1e-9:
        z_beta = 1.28
    else:
        z_beta = 0.84

    n = ((z_alpha + z_beta) * effect_sd / effect) ** 2
    return max(2.0, n)


def run_paired_trials(
    trials: int,
    tasks_per_trial: int,
    params: SimulationParams,
    base_seed: int,
) -> Tuple[List[Dict[str, float]], Dict[str, List[float]]]:
    cfg_base = ScaffoldConfig("unscaffolded", False, False, False, False)
    cfg_full = ScaffoldConfig("full_scaffold", True, True, True, True)

    rows: List[Dict[str, float]] = []
    deltas: Dict[str, List[float]] = {
        "accuracy": [],
        "abstain_rate": [],
        "novelty_error_rate": [],
        "confident_novelty_error_rate": [],
        "novelty_calibration_r": [],
    }

    for i in range(trials):
        seed = base_seed + i
        tasks = generate_tasks(tasks_per_trial, seed)
        base = run_condition(tasks, cfg=cfg_base, params=params, seed=seed)
        full = run_condition(tasks, cfg=cfg_full, params=params, seed=seed)

        row = {"trial": float(i), "seed": float(seed)}
        for metric in deltas.keys():
            row[f"base_{metric}"] = base[metric]
            row[f"full_{metric}"] = full[metric]
            row[f"delta_{metric}"] = full[metric] - base[metric]
            deltas[metric].append(row[f"delta_{metric}"])
        rows.append(row)

    return rows, deltas


def summarize_metric(values: List[float], metric: MetricSpec) -> Dict[str, float]:
    m = mean(values) if values else 0.0
    sd = stdev(values) if len(values) >= 2 else 0.0
    ci_lo, ci_hi = bootstrap_ci(values)
    p = sign_flip_permutation_pvalue(values)

    # power estimates based on observed pilot effect/variance
    n80 = approximate_required_n(m, sd, alpha=0.05, power=0.8)
    n90 = approximate_required_n(m, sd, alpha=0.05, power=0.9)

    # "success" direction for reporting
    if metric.better_direction == "higher":
        success = m > 0
    else:  # lower is better -> delta should be negative
        success = m < 0

    return {
        "mean_delta": m,
        "sd_delta": sd,
        "ci95_lo": ci_lo,
        "ci95_hi": ci_hi,
        "p_permutation": p,
        "n80_estimate": n80,
        "n90_estimate": n90,
        "directionally_favorable": 1.0 if success else 0.0,
    }


def write_csv(path: Path, rows: List[Dict[str, float]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_summary(trials: int, tasks_per_trial: int, summary: Dict[str, Dict[str, float]]) -> None:
    print("\n=== Rigorous Paired Study Summary ===")
    print(f"trials: {trials}")
    print(f"tasks_per_trial: {tasks_per_trial}")
    print("comparison: full_scaffold - unscaffolded (paired by seed+task set)")

    print("\nmetric                         mean_delta   95% CI                 p_perm    n80_est   n90_est")
    print("-" * 98)
    for metric, stats in summary.items():
        print(
            f"{metric:28s}"
            f"{stats['mean_delta']:11.4f}"
            f" [{stats['ci95_lo']:+.4f}, {stats['ci95_hi']:+.4f}]"
            f"  {stats['p_permutation']:.4f}"
            f"  {stats['n80_estimate']:8.1f}"
            f"  {stats['n90_estimate']:8.1f}"
        )

    print("\nInterpretation note:")
    print("- For accuracy/calibration/abstain_rate, positive mean_delta means full > base.")
    print("- For novelty_error_rate/confident_novelty_error_rate, negative mean_delta means full is better.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a statistically rigorous paired study for scaffold effects.")
    parser.add_argument("--trials", type=int, default=300, help="Number of paired trials (seeds).")
    parser.add_argument("--tasks-per-trial", type=int, default=400, help="Tasks per trial.")
    parser.add_argument("--base-seed", type=int, default=1000, help="Starting seed for trial generation.")
    parser.add_argument(
        "--out-csv",
        type=str,
        default="artifacts/rigorous_swarm_study_trials.csv",
        help="Output CSV for per-trial metrics.",
    )
    args = parser.parse_args()

    params = SimulationParams()
    rows, deltas = run_paired_trials(
        trials=args.trials,
        tasks_per_trial=args.tasks_per_trial,
        params=params,
        base_seed=args.base_seed,
    )

    metric_specs = [
        MetricSpec("accuracy", "higher"),
        MetricSpec("abstain_rate", "higher"),
        MetricSpec("novelty_error_rate", "lower"),
        MetricSpec("confident_novelty_error_rate", "lower"),
        MetricSpec("novelty_calibration_r", "higher"),
    ]

    summary = {
        spec.name: summarize_metric(deltas[spec.name], spec)
        for spec in metric_specs
    }

    write_csv(Path(args.out_csv), rows)
    print_summary(args.trials, args.tasks_per_trial, summary)
    print(f"\nSaved per-trial results to: {args.out_csv}")


if __name__ == "__main__":
    main()

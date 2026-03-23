# External Scaffolding and Self-Monitoring Signatures in Agent Swarms: A Simulation Study

## Structured Abstract

**Background:** The Abstraction Primitive Hypothesis (APH) argues that self-monitoring is best identified by failure topology under novelty rather than aggregate success.  
**Objective:** Test whether externally scaffolded agent swarms show distinct novelty signatures relative to unscaffolded swarms.  
**Methods:** We ran paired synthetic trials (matched task sets per seed) comparing full-scaffold and unscaffolded conditions, and estimated uncertainty via bootstrap confidence intervals and sign-flip permutation tests.  
**Results (to be filled after local run):** Insert trial count, mean deltas, CIs, and p-values for calibration, confident novelty error, abstention, and accuracy.  
**Conclusions:** External scaffolding can improve calibration-oriented self-monitoring signatures while trading off raw accuracy in some regimes; robustness is parameter-dependent.

## Main Text Draft

### Introduction
The present repository frames intelligence as recursive abstraction and proposes that self-monitoring is revealed by behavior under novelty. To operationalize this claim, we test whether external scaffolding in a swarm architecture changes failure topology: confidence calibration on novel tasks, reduction of confident novel errors, and conservative fallback (abstention).

### Methods

#### Simulation and conditions
We evaluate two primary conditions:
1. **Unscaffolded** swarm baseline.
2. **Full scaffold** with shared memory, novelty-aware confidence shaping, confidence gating, and verifier arbitration.

#### Outcomes
Primary outcomes:
- Novelty calibration correlation (`novelty_calibration_r`),
- Confident novelty error rate (`confident_novelty_error_rate`),
- Abstention rate (`abstain_rate`).

Secondary outcome:
- Overall accuracy.

#### Statistical design
We use a **paired design** over trial seeds:
- For each trial seed, generate a task set,
- Evaluate both conditions on that matched task set,
- Compute trial-level deltas (full - unscaffolded),
- Estimate uncertainty with bootstrap 95% CIs,
- Compute two-sided sign-flip permutation p-values.

#### Power guidance
The study script estimates required trial counts for 80% and 90% power from observed effect/variance in the paired deltas (normal approximation). These are planning estimates, not definitive preregistered guarantees.

### Results Template

Run locally:

```bash
python3 code/rigorous_swarm_study.py --trials 300 --tasks-per-trial 400
```

Report:
- Mean delta, 95% CI, p-value for each primary endpoint,
- Directional consistency across endpoints,
- Accuracy tradeoff if present,
- Estimated N for 80%/90% power.

### Discussion
Interpret findings in terms of APH predictions:
- If calibration improves and confident novel errors decrease while abstention rises, results support scaffold-induced self-monitoring signatures.
- If improvements disappear under wide/harsher parameter sweeps, report fragility and boundary conditions explicitly.
- Clarify external validity limits: synthetic arithmetic-style tasks do not establish direct transfer to production LLM systems.

### Limitations
- Toy environment and synthetic novelty generation,
- No direct token-level LLM outputs,
- Statistical assumptions in power approximation,
- Potential model-dependent behavior outside this simulator.

### Future work
- Scale the included `code/api_multimodel_rigorous_study.py` pipeline to preregistered real-model runs (OpenAI/Anthropic/Gemini),
- Pre-register endpoints and stopping rules,
- Add hierarchical models for condition effects,
- Evaluate robustness to alternative novelty definitions.

# Abstraction-Intelligence

**What makes something intelligent?**

The **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure—and requires *self-state* for genuine construction beyond pattern matching.

---

## The Core Claim

**Abstraction is the recursive process of forming and composing symbols.**

```
[Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                     ▲                                              │
                     └──────────── [Feedback] ──────────────────────┘
```

Not symbols alone. Not composition alone. Their **mutual refinement through iteration**.

---

## Two Frameworks: Developmental Stages and Composition Types

The framework distinguishes **how abstract** (developmental stages) from **what kind of composition** (composition types). These are related but orthogonal dimensions.

### Developmental Stages of Abstraction

|Stage|Capacity|What It Enables|
|-----|--------|---------------|
|1. Pattern Extraction|Detect statistical regularities|Compression, prediction|
|2. Symbol Formation|Discrete, recombinable representations|Compositional generalization|
|3. Recursive Composition|Abstractions as inputs to abstraction|Hierarchical depth, analogy|
|4. Self-Referential|Abstraction over one's own abstraction|Metacognition, verification, hold-and-check|

See [Paper 7: The Developmental Spectrum](papers/abstraction_developmental_spectrum.md) for full treatment.

### Composition Types (A–D)

|Type|Structure|Example|Required Stage|
|----|---------|-------|--------------|
|**A: Concatenative**|A + B → AB|"blue bird"|Stage 2|
|**B: Role-filler**|R(x) + S(y) → R(x)S(y)|AGENT(dog) + ACTION(chased)|Stage 2|
|**C: Recursive**|A contains [B contains C]|"The dog [that chased the cat [that…]]"|Stage 3|
|**D: Analogical**|Structure(X) → Structure(Y)|atom:nucleus :: solar system:sun|Stage 3|

**Key insight:** Types A–D describe *compositional operations*. Stages 1–4 describe *levels of abstraction capacity*. Stage 4 (self-referential) is **orthogonal** to composition type—it monitors and verifies any compositional operation.

---

## Empirical Findings

> **Note:** All findings below are from preliminary studies with limited sample sizes (N=100-700). These are initial tests; interpretations are working hypotheses requiring replication with larger samples and cross-model testing.

### What's Confirmed (Effects)

|Finding|Evidence|Interpretation|
|-------|--------|--------------|
|Pattern-matchable C–D at ceiling|Bracket depth, pointer chase: 100%|Stage 3 operations work when pattern-cached|
|Novel operators cause failure|Recursive eval with invented ops: 50%|Stage 3 fails without cached pattern|
|Multi-constraint relations cause failure|Relation mapping: 28%|Constraint satisfaction exceeds pattern-matching|
|Generation-verification asymmetries exist|See studies below|Task-specific; mechanism varies (see below)|
|Scaffolding shows task-specific effects|N=600, see below|**Cognitive overhead account** (working hypothesis)|

### What's Been Reinterpreted

|Original Claim|New Evidence|Updated Interpretation|
|--------------|------------|----------------------|
|Arithmetic verification deficit = Stage 4 hold-and-check failure|Prompt variant study (N=150): "Does it equal?" achieves 96.7% vs. 10% for "Is X=Y?" format|**Pragmatic inference artifact** (Grice, 1975), not computational limitation. Question format implies doubt, biasing toward rejection.|

**Critical finding:** Reversing question polarity ("Is X≠Y?") also failed (20%), ruling out simple response bias. The deficit is prompt-format dependent, not a fundamental verification incapacity.

### What Didn't Replicate

|Finding|Pilot|Extended|
|-------|-----|--------|
|A–B vs. C–D uniform dissociation|d=0.71|d=0.00|

**Interpretation:** Composition type alone doesn't predict failure. What matters is whether the operation is pattern-matchable (Stage 3 question) and whether self-monitoring is required (Stage 4 question).

### The Generation-Verification Study (N=700)

|Task|Generation|Verification|Δ|Pattern|
|----|----------|------------|--|-------|
|Arithmetic|100%|76%|+24%|Verification deficit|
|Multistep|100%|74%|+26%|Verification deficit|
|Logic|56%|100%|-44%|Generation deficit|
|Word count|82%|100%|-18%|Generation deficit|
|Others|~100%|~100%|0%|No asymmetry|

**Overall:** 91.1% vs 92.6%, p=0.58 (null)

**Updated interpretation:** 
- **Arithmetic verification deficit:** Now understood as **pragmatic inference artifact** based on follow-up testing (N=150). Neutral prompt framing ("Does it equal?") restores verification to 96.7%. This is NOT evidence for hold-and-check failure.
- **Logic generation deficit:** Mechanism untested for prompt effects. May reflect genuine Stage 4 limit OR may also be prompt-dependent. Requires similar prompt-variant testing.

### The Scaffolding Asymmetry Study (N=600)

|Task|Baseline|Self-Monitor|Constraint|
|----|--------|------------|----------|
|Arithmetic (Claude)|70%|**98%** (+28%)|60% (-10%)|
|Logic (Claude)|64%|32% (-32%)|34% (-30%)|
|Arithmetic (GPT-4o)|88%|90% (+2%)|66% (-22%)|
|Logic (GPT-4o)|66%|60% (-6%)|58% (-8%)|

**Key finding:** Self-monitoring scaffolds dramatically improve arithmetic verification (+28%, p<.001), but **all scaffolding degrades generation**. Crossed scaffold-task pairings hurt worst.

**Interpretation (Cognitive Overhead Account):** Scaffolding imposes processing costs. When the scaffold addresses the task's bottleneck, benefit > cost. When it doesn't, cost dominates.

**Caution:** Given the pragmatic artifact findings, the +28% scaffolding benefit for arithmetic may partially reflect prompt framing effects (the scaffold avoids doubt-implying question structure) rather than "prosthetic self-state." Further testing needed.

---

## The Self-State Hypothesis

### Why Embeddedness Matters

```
Embedded agents (survival stakes)          Disembodied systems (prediction loss)
            ↓                                          ↓
Self/world distinction required            No self/world distinction needed
            ↓                                          ↓
Persistent self-state architecture         No persistent self-state
            ↓                                          ↓
Stage 4 capacity develops                  Stage 4 systematically limited
```

**The core claim:** LLMs lack Stage 4 capacity because they were never under pressure requiring self/world distinction. Survival stakes create asymmetric costs that select for self-monitoring. Prediction loss is symmetric—no selection pressure for self-state.

**Evidence status:**
- Embeddedness → self-state: **Hypothesis** (evolutionary argument, not directly tested)
- LLMs lack Stage 4: **Partially supported** (miscalibration, some task failures) but **arithmetic verification deficit ruled out as evidence** (it's a prompt artifact)
- Scaffolding provides prosthetic self-state: **Uncertain** (may be prompt framing effects)

### Active Maintenance ≠ Attention

|Active Maintenance (Stage 4)|Attention|
|----------------------------|---------|
|Explicit holding and checking|Weighted retrieval from context|
|Working memory central executive (Baddeley, 2000)|Memory access mechanism|
|Continuous comparison during inference|Requires explicit re-retrieval|

LLMs have attention. Whether they lack the central executive function that enables hold-and-check remains an open question—the arithmetic evidence previously cited does not support this claim.

---

## The LLM Profile: "Disembodied Abstraction"

|Stage|LLM Capacity|Evidence|
|-----|------------|--------|
|Stage 1: Pattern Extraction|**Full**|Foundation of operation|
|Stage 2: Symbol Formation|**Substantial**|Compositional generalization (imperfect)|
|Stage 3: Recursive Composition|**Partial, context-dependent**|Pattern-matchable C–D succeeds; novel fails|
|Stage 4: Self-Referential|**Unclear**|Some evidence (miscalibration, logic generation deficit) but arithmetic verification deficit ruled out|

This profile—strong at Stages 1–2, partial at Stage 3, uncertain at Stage 4—is what we term **disembodied abstraction** (working characterization pending further testing).

---

## Predictions

### Confirmed
- Pattern-matchable C–D succeeds regardless of formal complexity
- Genuinely novel operators/constraints cause failure (Stage 3 limit)
- Task-specific generation/verification asymmetries exist (mechanism varies)
- Prompt framing dramatically affects verification accuracy

### Falsified
- Uniform verification < generation
- Composition type (A–D) as primary predictor
- Scaffolding uniformly helps (it has task-specific costs)
- **Arithmetic verification deficit as evidence for hold-and-check failure** (it's a pragmatic inference artifact)

### Open Hypotheses
- Embeddedness is necessary (not just sufficient) for Stage 4
- Scaling does not produce Stage 4 capacity
- Lighter-touch scaffolds reduce overhead costs
- **Which gen/ver asymmetries reflect genuine Stage 4 limits vs. prompt artifacts?**
- **Does the logic generation deficit survive prompt-controlled testing?**

---

## Visualizations

| Visualization | Description |
|---------------|-------------|
| [Self-State in the Information Plane](visualizations/self_state_abstraction.html) | Interactive 3D: pattern-matching vs. self-state abstraction |

---

## Papers

**Core (1–10):**

|#|Paper|
|-|-----|
|1|[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)|
|2|[The Computational Structure of Abstraction](papers/abstraction_defined.md)|
|3|[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)|
|4|[Abstraction Constrained](papers/abstraction_constrained.md)|
|5|[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)|
|6|[Recursive Abstraction](papers/recursive_abstraction.md)|
|7|[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)|
|8|[Embeddedness and Self/World](papers/embedded_abstraction.md)|
|9|[Self and World](papers/self_world_abstraction.md)|
|10|[Survival Pressure and the Origins of Abstraction](papers/survival_pressure.md)|

**Extensions (11–18):**

|#|Paper|
|-|-----|
|11|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|
|12|[The Hard Problem Reframed](papers/hard_problem_reframed.md)|
|13|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)|
|14|[Emotion as Embedded Information](papers/emotion_embedded_information.md)|
|15|[Social Dynamics](papers/social_dynamics.md)|
|16|[Beyond Large Language Models](papers/beyond_llms.md)|
|17|[Dual-Process Theory Reconsidered](papers/dual_process_abstraction.md)|
|18|[Neurochemistry as Self-State Abstraction](papers/mind_body_neurochemistry.md)|

**Empirical:**

|#|Paper|
|-|-----|
|19|[Pilot Study: Compositional Hierarchy in LLMs](papers/pilot_composition_study.md)|
|20|[Hold-and-Check: Task-Specific Dissociations](papers/hold_and_check_study.md)|
|21|[Scaffolding Asymmetry: Generation vs. Verification](papers/scaffolding_asymmetry.md)|
|22|[Verification Deficit as Pragmatic Artifact](papers/verification_pragmatic_artifact.md) *(new)*|

**Theoretical:**

|#|Paper|
|-|-----|
|23|[The Geometry of Self-Reference](papers/information_geometry.md)|
|24|[Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md) *(new)*|


**For Physicists/Engineers:**

|Document|Purpose|
|--------|-------|
|[Theoretical Guide for Physicists](papers/theoretical_guide_for_physicists.md)|Framework mapped to control theory, information theory, dynamical systems|
|[Self-Referential Computation (Python)](code/self_referential_computation_for_physicists.py)|Executable demonstrations|

---

## Empirical Research Program

### 🧠 Core Framework
[abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) · [composition-testing](https://github.com/HillaryDanan/composition-testing) · [composition-type-dissociation](https://github.com/HillaryDanan/composition-type-dissociation) · [compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction) · [compositional-dual-process](https://github.com/HillaryDanan/compositional-dual-process) · [embeddedness-calibration](https://github.com/HillaryDanan/embeddedness-calibration) · [emergent-factorization](https://github.com/HillaryDanan/emergent-factorization) · [reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum) · [scaffolding-asymmetry](https://github.com/HillaryDanan/scaffolding-asymmetry)

### 🔬 Verification Studies
[verification-deficit-replication](https://github.com/HillaryDanan/verification-deficit-replication) · [verification-prompt-variants](https://github.com/HillaryDanan/verification-prompt-variants)

### 🔄 Self-Reference
[self-referential-dynamics](https://github.com/HillaryDanan/self-referential-dynamics) · [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction) · [ouroboros-learning](https://github.com/HillaryDanan/ouroboros-learning) · [recursive-reality](https://github.com/HillaryDanan/recursive-reality) · [geometry-self-reference](https://github.com/HillaryDanan/geometry-self-reference)

### ⏱️ Temporal
[TIDE](https://github.com/HillaryDanan/TIDE) · [TIDE-resonance](https://github.com/HillaryDanan/TIDE-resonance) · [TIDE-analysis](https://github.com/HillaryDanan/TIDE-analysis) · [temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm) · [temporal-myopia-llm](https://github.com/HillaryDanan/temporal-myopia-llm) · [llm-time-decay](https://github.com/HillaryDanan/llm-time-decay) · [curved-cognition](https://github.com/HillaryDanan/curved-cognition)

### 🌍 Embodiment
[embodied-cognition](https://github.com/HillaryDanan/embodied-cognition) · [physical-grounding-llm](https://github.com/HillaryDanan/physical-grounding-llm) · [TERRA-embodied-interpretability](https://github.com/HillaryDanan/TERRA-embodied-interpretability)

### 🪞 Consciousness
[BIND](https://github.com/HillaryDanan/BIND) · [comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms) · [hexagonal-consciousness-suite](https://github.com/HillaryDanan/hexagonal-consciousness-suite) · [computational-emergence-theory](https://github.com/HillaryDanan/computational-emergence-theory)

### 👥 Social
[reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence) · [game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite) · [trust-calibration-framework](https://github.com/HillaryDanan/trust-calibration-framework)

### 🗣️ Language
[linguistic-dynamics-theory](https://github.com/HillaryDanan/linguistic-dynamics-theory) · [linguistic-memory-framework](https://github.com/HillaryDanan/linguistic-memory-framework) · [cross-linguistic-attention-dynamics](https://github.com/HillaryDanan/cross-linguistic-attention-dynamics) · [benign-violations](https://github.com/HillaryDanan/benign-violations)

### 🔬 Geometry
[causal-attention-geometry](https://github.com/HillaryDanan/causal-attention-geometry) · [multi-geometric-attention](https://github.com/HillaryDanan/multi-geometric-attention) · [relativistic-interpretability](https://github.com/HillaryDanan/relativistic-interpretability) · [spectral-representations](https://github.com/HillaryDanan/spectral-representations)

### 🧪 LLM Testing
[llm-habituation-patterns](https://github.com/HillaryDanan/llm-habituation-patterns) · [nonlinear-dialogue-dynamics](https://github.com/HillaryDanan/nonlinear-dialogue-dynamics) · [paradox-induced-oscillations](https://github.com/HillaryDanan/paradox-induced-oscillations) · [retroactive-causality](https://github.com/HillaryDanan/retroactive-causality) · [claude-emergence-patterns](https://github.com/HillaryDanan/claude-emergence-patterns)

### 🔧 Architecture
[information-atoms](https://github.com/HillaryDanan/information-atoms) · [hexagonal-vision-research](https://github.com/HillaryDanan/hexagonal-vision-research) · [computational-substrates](https://github.com/HillaryDanan/computational-substrates) · [cognitive-architectures-ai](https://github.com/HillaryDanan/cognitive-architectures-ai)

### 📊 Tools
[pattern-analyzer](https://github.com/HillaryDanan/pattern-analyzer) · [concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)

---

## Key References

Baddeley, A. (2000). The episodic buffer. *Trends in Cognitive Sciences*, 4(11), 417-423.

Chollet, F. (2019). On the measure of intelligence. *arXiv:1911.01547*.

Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87-114.

Curtis, C. E., & D'Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics* (Vol. 3, pp. 41–58). Academic Press.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity. *Behavioral and Brain Sciences*, 21(6), 803-831.

Lake, B., & Baroni, M. (2018). Generalization without systematicity. *ICML*.

Oberauer, K., Farrell, S., Jarrold, C., & Lewandowsky, S. (2016). What limits working memory capacity? *Psychological Bulletin*, 142(7), 758-799.

Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*.

---

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

---

*"Abstraction is all you need ;)"*

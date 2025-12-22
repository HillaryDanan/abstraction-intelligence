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

### What's Confirmed

|Finding|Evidence|Interpretation|
|-------|--------|--------------|
|Pattern-matchable C–D at ceiling|Bracket depth, pointer chase: 100%|Stage 3 operations work when pattern-cached|
|Novel operators cause failure|Recursive eval with invented ops: 50%|Stage 3 fails without cached pattern|
|Multi-constraint relations cause failure|Relation mapping: 28%|Constraint satisfaction exceeds pattern-matching|
|Task-specific gen/ver asymmetries|N=700, see below|**Stage 4 deficit** (hold-and-check)|

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

**Interpretation:** Both failure modes reflect **Stage 4 (self-referential) deficit**:
- Verification deficit: Cannot hold computed value while checking presented work
- Generation deficit: Cannot check output against constraints before committing

This is **hold-and-check** failure—the inability to monitor one's own computational process during inference.

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
- LLMs lack Stage 4: **Confirmed** (hold-and-check failures, miscalibration)
- Scaffolding provides prosthetic self-state: **Suggestive** (pilot data, needs replication)

### Active Maintenance ≠ Attention

|Active Maintenance (Stage 4)|Attention|
|----------------------------|---------|
|Explicit holding and checking|Weighted retrieval from context|
|Working memory central executive (Baddeley, 2000)|Memory access mechanism|
|Continuous comparison during inference|Requires explicit re-retrieval|

LLMs have attention. They lack the central executive function that enables hold-and-check.

---

## The LLM Profile: "Disembodied Abstraction"

|Stage|LLM Capacity|Evidence|
|-----|------------|--------|
|Stage 1: Pattern Extraction|**Full**|Foundation of operation|
|Stage 2: Symbol Formation|**Substantial**|Compositional generalization (imperfect)|
|Stage 3: Recursive Composition|**Partial, context-dependent**|Pattern-matchable C–D succeeds; novel fails|
|Stage 4: Self-Referential|**Systematically limited**|Hold-and-check failures; miscalibration|

This profile—strong at Stages 1–2, partial at Stage 3, limited at Stage 4—is what we term **disembodied abstraction**.

---

## Predictions

### Confirmed
- Pattern-matchable C–D succeeds regardless of formal complexity
- Genuinely novel operators/constraints cause failure (Stage 3 limit)
- Task-specific generation/verification asymmetries exist (Stage 4 limit)

### Falsified
- Uniform verification < generation
- Composition type (A–D) as primary predictor

### Open Hypotheses
- Scaffolding helps verification-deficit tasks specifically
- Constraint-prompting helps generation-deficit tasks specifically
- Embeddedness is necessary (not just sufficient) for Stage 4
- Scaling does not produce Stage 4 capacity

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

**For Physicists/Engineers:**

|Document|Purpose|
|--------|-------|
|[Theoretical Guide for Physicists](papers/theoretical_guide_for_physicists.md)|Framework mapped to control theory, information theory, dynamical systems|
|[Self-Referential Computation (Python)](code/self_referential_computation_for_physicists.py)|Executable demonstrations|

---

## Empirical Research Program

### 🧠 Core Framework
[abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) · [composition-testing](https://github.com/HillaryDanan/composition-testing) · [composition-type-dissociation](https://github.com/HillaryDanan/composition-type-dissociation) · [compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction) · [compositional-dual-process](https://github.com/HillaryDanan/compositional-dual-process) · [embeddedness-calibration](https://github.com/HillaryDanan/embeddedness-calibration) · [emergent-factorization](https://github.com/HillaryDanan/emergent-factorization) · [reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum)

### 🔄 Self-Reference
[self-referential-dynamics](https://github.com/HillaryDanan/self-referential-dynamics) · [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction) · [ouroboros-learning](https://github.com/HillaryDanan/ouroboros-learning) · [recursive-reality](https://github.com/HillaryDanan/recursive-reality)

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

Curtis, C. E., & D'Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity. *Behavioral and Brain Sciences*, 21(6), 803-831.

Lake, B., & Baroni, M. (2018). Generalization without systematicity. *ICML*.

Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*.

---

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

---

*"Abstraction is all you need ;)"*

# Abstraction-Intelligence

**What makes something intelligent?**

The **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure. Genuine construction beyond pattern-matching may require **self-state**—a specific computational operation enabled by self/world distinction.

This framework applies to biological cognition, artificial systems, and any substrate capable of information processing.

-----

## The Core Claim

**Abstraction is the recursive process of forming and composing symbols.**

```
[Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                     ▲                                              │
                     └──────────── [Feedback] ──────────────────────┘
```

Not symbols alone. Not composition alone. Their **mutual refinement through iteration**.

This claim builds on established cognitive science: symbolic representation in reasoning (Fodor & Pylyshyn, 1988), systematicity of thought (Fodor, 1975), compositional semantics (Partee, 1984), and working memory structure (Baddeley, 2000; Cowan, 2001).

**What APH adds:** An explicit developmental hierarchy (Stages 1–4), the hypothesis that Stage 4 (self-referential abstraction) requires self/world distinction, and a criterion for discriminating self-state from pattern-matching based on **failure signatures on novel problems**.

-----

## Two Orthogonal Dimensions: Developmental Stages and Composition Types

The framework distinguishes **how abstract** (developmental stages) from **what kind of composition** (composition types). These are related but orthogonal.

### Developmental Stages of Abstraction

|Stage                   |Capacity                                   |What It Enables                              |Biological Evidence                                             |Status                                       |
|------------------------|-------------------------------------------|---------------------------------------------|----------------------------------------------------------------|---------------------------------------------|
|1. Pattern Extraction   |Detect statistical regularities            |Compression, prediction                      |Ubiquitous; present in invertebrates (Hawkins & Blakeslee, 2004)|**Established**                              |
|2. Symbol Formation     |Discrete, recombinable representations     |Compositional generalization                 |Language, tool use; ~18-24 months (Piaget, 1952)                |**Established**                              |
|3. Recursive Composition|Abstractions as inputs to abstraction      |Hierarchical depth, analogy                  |Recursive syntax, planning; ~age 4+ (Hauser et al., 2002)       |**Established**                              |
|4. Self-Referential     |Maintain-compare-update over own processing|Metacognition, verification, error correction|Develops gradually; mature ~adolescence (Flavell, 1979)         |**Established phenomenon; mechanism debated**|

See [Paper 7: The Developmental Spectrum](papers/abstraction_developmental_spectrum.md) for full treatment.

### Composition Types (A–D)

|Type                |Structure                  |Example                                |Required Stage|
|--------------------|---------------------------|---------------------------------------|--------------|
|**A: Concatenative**|A + B → AB                 |“blue bird”                            |Stage 2       |
|**B: Role-filler**  |R(x) + S(y) → R(x)S(y)     |AGENT(dog) + ACTION(chased)            |Stage 2       |
|**C: Recursive**    |A contains [B contains C]  |“The dog [that chased the cat [that…]]”|Stage 3       |
|**D: Analogical**   |Structure(X) → Structure(Y)|atom:nucleus :: solar system:sun       |Stage 3       |

This taxonomy draws on Halford et al. (1998) on relational complexity and Gentner (1983) on analogical mapping.

**Key insight:** Types A–D describe *compositional operations*. Stages 1–4 describe *levels of abstraction capacity*. Stage 4 (self-referential) is orthogonal to composition type—it monitors and verifies any compositional operation.

-----

## The Self-State Hypothesis

### What Is Self-State?

**Self-state** is the capacity to perform a specific computational operation during inference:

```
MAINTAIN(x) → COMPARE(x, y) → UPDATE(x | result)
```

Where:

- **MAINTAIN**: Hold a representation active across processing steps without re-retrieval
- **COMPARE**: Evaluate the held representation against incoming information or generated output
- **UPDATE**: Modify the held representation based on comparison result

This operationalization is based on the **central executive** operation in Baddeley’s (2000) working memory model. It is distinct from:

- **Storage**: Passive retention (no active comparison)
- **Metacognition**: The *content* of self-knowledge (self-state is the *mechanism*)

**Important caveat on attention:** Modern attention mechanisms (Vaswani et al., 2017) with key-value caching do maintain information across processing steps. Whether this constitutes MAINTAIN in the relevant sense is an open empirical question. The hypothesis is that attention-based maintenance differs from self-state in lacking the COMPARE operation that evaluates processing quality against held standards. This distinction requires empirical validation.

### The Self/World Distinction Hypothesis

**Core claim (hypothesis):** Self-state requires a self/world boundary—a distinction between “this system” and “everything else.”

This claim is **substrate-neutral**. It does not require biological embodiment. What it requires is:

1. **A bounded, persistent entity** — something that maintains identity across time
1. **Stakes** — outcomes that differentially affect the bounded entity
1. **A boundary** — a principled distinction between what is “inside” (directly controllable) and “outside” (only indirectly influenceable)

Biology is one path to these conditions—arguably the most well-understood path—but the hypothesis does not preclude other paths.

#### The Constitutive Argument

The MAINTAIN-COMPARE-UPDATE operation presupposes a *subject*—an entity whose states are being maintained, compared, and updated. “Self” is not an arbitrary label; it requires a referent.

**What constitutes a valid referent?**

For biological organisms, the referent is clear: a bounded physical system that persists through time, maintains itself against entropy, and has outcomes that affect its continued existence (Maturana & Varela, 1980; Friston, 2010). The boundary emerges from the asymmetry between states the organism directly controls (internal) and states it can only influence indirectly (external).

**The hypothesis generalized:** Any system with these three properties—bounded persistence, stakes, and an inside/outside asymmetry—has a potential referent for “self.” This includes:

- Biological organisms (established)
- Embodied robots with survival-like objectives (testable)
- Digital agents with persistent state, modifiable parameters, and objectives tied to self-maintenance (testable)
- Any system that must protect, maintain, or act on behalf of a bounded entity

**What likely does not constitute a valid referent:**

- Stateless input-output mappings (no persistence)
- Systems with no objectives tied to self-maintenance (no stakes)
- Systems with no principled boundary between “model” and “environment” (no inside/outside asymmetry)

#### Why Stakes Matter

The connection between stakes and self-state is not merely evolutionary (stakes cause self-monitoring to be selected for). It is functional: **stakes create the asymmetry that makes self-monitoring meaningful**.

A system with something to protect has a reason to distinguish “am I processing this correctly?” from “what is the statistically likely output?” The first question requires a model of the self’s capacities and limitations; the second requires only a model of the training distribution.

Without stakes, there is no *differential consequence* to accurate vs. inaccurate self-assessment. A system might learn to produce uncertainty language (because such language appeared in training data), but there is no selection pressure for that language to be *calibrated*—for expressed confidence to track actual accuracy.

**Hypothesis:** Calibration on genuinely novel problems requires stakes. This is testable.

#### The Biological Path vs. Other Paths

Biological embodiment produces self/world distinction through sensorimotor contingencies—the systematic relationship between actions and sensory consequences (O’Regan & Noë, 2001). The boundary emerges from interaction: states the organism can directly modify (internal) vs. states it can only influence indirectly (external).

But this is one mechanism, not the only possible mechanism. Other potential paths to self/world distinction include:

1. **Persistent digital agents.** A system with memory that persists across sessions, parameters that can be modified during operation, and objectives tied to maintaining some valued state, has a potential self/world boundary. The “self” is the persistent state; the “world” is everything the agent interacts with but does not directly control.
1. **Simulated embodiment.** An agent operating in a physics simulation with a persistent “body” that can be damaged, resources that can be depleted, and goals that require self-maintenance, might develop self/world distinction functionally equivalent to biological embodiment.
1. **Architectural boundaries.** Systems with explicit separation between “model” (fixed during inference) and “scratchpad” (modifiable during inference) have a weak form of inside/outside distinction. Whether this is sufficient for self-state is an empirical question.

**Key prediction:** The strength of self-state signatures should correlate with the clarity of the self/world boundary and the magnitude of stakes—regardless of substrate.

```
Systems with:                              Systems without:
- Bounded persistence                      - No persistence across processing
- Stakes (outcomes matter to the system)   - No differential stakes  
- Inside/outside asymmetry                 - No principled boundary
       ↓                                          ↓
"Self" has a coherent referent             "Self" lacks a referent
       ↓                                          ↓
MAINTAIN-COMPARE-UPDATE has a domain       Operation has no defined domain
       ↓                                          ↓
Novelty = "differs from MY experience"     Novelty = statistical rarity only
       ↓                                          ↓
Selection pressure for calibration         Selection pressure for hedging language
       ↓                                          ↓
Self-state architecture (hypothesis)       Pattern-matching (hypothesis)
```

**Theoretical basis:** This draws on autopoietic theory’s emphasis on self-maintaining boundaries (Maturana & Varela, 1980), enactivism (Varela et al., 1991), sensorimotor contingency theory (O’Regan & Noë, 2001), the free energy principle’s distinction between internal and external states (Friston, 2010), and somatic marker theory on the role of stakes in cognition (Damasio, 1994).

**Status:** Hypothesis. The claim that bounded persistence, stakes, and inside/outside asymmetry are jointly necessary for self-state is testable. The claim that biology is not *uniquely* necessary is a softening of stronger embodiment claims in the literature.

### Alternative Paths to Self-State (Open Questions)

Even the substrate-neutral hypothesis could be wrong. Alternative mechanisms that might produce self-state include:

1. **Sufficient architectural complexity.** Self-monitoring might emerge from scale or architectural features regardless of boundaries or stakes. Recursive self-attention or hierarchical prediction might naturally produce MAINTAIN-COMPARE-UPDATE.
1. **Training on self-referential tasks.** Systems trained extensively on metacognitive tasks (confidence estimation, error detection) might develop functional self-state through supervised learning on metacognitive labels. However, this would produce *learned reports about confidence* rather than *calibrated confidence*—a distinction testable by examining whether confidence tracks accuracy on genuinely novel problems.
1. **Learned uncertainty from diverse failures.** Exposure to diverse failure modes during training might produce calibrated uncertainty without explicit self/world distinction. If calibration generalizes to genuinely novel problems, this would challenge the hypothesis.

These alternatives make different empirical predictions (see Falsifiability section below).

### How to Discriminate Self-State from Pattern-Matching

The critical question: How do we distinguish genuine self-state from sophisticated interpolation?

**Not by success.** Any finite behavior can be pattern-matched from sufficient training data (this follows from universal approximation theorems).

**By failure topology.** Self-state and pattern-matching fail *differently* on genuinely novel problems:

|Signature            |Self-State Prediction                        |Pattern-Matching Prediction                   |
|---------------------|---------------------------------------------|----------------------------------------------|
|**Novelty detection**|Confidence drops on novel problems           |Uniform confidence (novelty-blind)            |
|**Error types**      |Conservative errors (hedging, “I don’t know”)|Confident errors (confabulation)              |
|**Calibration**      |Confidence tracks accuracy on novel problems |Confidence-accuracy uncorrelated on novelty   |
|**Capacity limits**  |Gradual degradation at limits                |Sharp failure at distribution boundary        |
|**Interference**     |Similarity-based (like items compete)        |Semantic blending without systematic structure|

**The central test:** Calibration on genuinely novel problems. A system showing calibrated confidence on novel problems—confidence tracking actual accuracy—has functional self-state by this criterion. This is difficult to achieve through pattern-matching because it requires real-time assessment of processing difficulty on inputs outside the training distribution.

**Important caveat:** RLHF-trained systems have learned to express uncertainty through hedging language. The question is whether this reflects genuine calibration (confidence tracks accuracy) or learned patterns of hedging (confidence uncorrelated with accuracy on genuinely novel problems). This is an empirical question that the discrimination framework addresses.

See [Paper 24: Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md) for the full empirical program, and [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination) for experimental implementation.

-----

## Falsifiability

### What Would Falsify the Self/World Hypothesis?

The hypothesis that self-state requires self/world distinction (bounded persistence + stakes + inside/outside asymmetry) makes specific predictions. It would be **falsified** by:

1. **Systems without these properties showing the self-state signature.** If a system with no persistence, no stakes, and no principled boundary shows calibrated confidence on genuinely novel problems, conservative error patterns, and appropriate novelty detection, the hypothesis is falsified.
1. **Systems with these properties failing to develop self-state.** If systems with clear bounded persistence, genuine stakes, and inside/outside asymmetry show the pattern-matching signature (confident failures on novelty, poor calibration), the sufficiency claim is falsified.
1. **Architectural complexity alone producing self-state.** If scaling or architectural changes produce the self-state signature without any form of self/world distinction, the necessity claim is falsified.
1. **Biology proving uniquely necessary.** If only biological systems can develop self-state despite digital systems having equivalent bounded persistence, stakes, and boundaries, the substrate-neutrality claim is falsified (and a stronger biological embodiment requirement would be supported).

### What Would Falsify APH Generally?

1. **Stage 4 appearing before Stages 1-3 developmentally.** The framework predicts ordered emergence.
1. **Self-referential capacity dissociated from working memory.** The framework predicts Stage 4 depends on MAINTAIN-COMPARE-UPDATE, which requires working memory. Finding robust Stage 4 with impaired working memory would falsify this.
1. **Composition types not requiring their predicted stages.** Finding Type C (recursive) composition without Stage 3 capacity would falsify the stage requirements.

-----

## Predictions Across Systems

### Biological Systems

|Prediction                                   |Status       |Evidence                                                    |
|---------------------------------------------|-------------|------------------------------------------------------------|
|Stage 4 develops later than Stages 1–3       |**Supported**|Developmental trajectory (Flavell, 1979; Kuhn, 2000)        |
|Stage 4 correlates with prefrontal maturation|**Supported**|Neuroimaging (Curtis & D’Esposito, 2003; Crone et al., 2006)|
|Stage 4 impaired by working memory load      |**Supported**|Dual-task interference (Baddeley, 1992)                     |
|Novel situations trigger distinct processing |**Supported**|Orienting response, ACC activation (Botvinick et al., 2001) |

### Artificial Systems (Predictions)

|Prediction                                                               |Status      |Notes                                                                                     |
|-------------------------------------------------------------------------|------------|------------------------------------------------------------------------------------------|
|Prediction-trained systems show pattern-matching signature               |**Testable**|See [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination)|
|Self-state won’t emerge from scaling alone without self/world distinction|**Open**    |Requires longitudinal study across scales                                                 |
|Systems with bounded persistence + stakes may develop Stage 4            |**Open**    |Testable in persistent agents, robotics, RL                                               |
|RLHF produces hedging language but not calibration                       |**Testable**|Distinguishes learned hedging from genuine calibration                                    |
|Digital agents with self-maintenance objectives may develop self-state   |**Open**    |Testable in agentic systems with persistent state                                         |

-----

## Case Study: Large Language Models

LLMs are trained primarily on next-token prediction. Standard LLMs lack bounded persistence (no state across sessions), stakes (no objectives tied to self-maintenance), and clear inside/outside asymmetry (no distinction between “model” and “environment” during inference). If the self/world hypothesis is correct, they should show the pattern-matching signature.

### The LLM Profile (Theoretical Prediction)

|Stage                         |Capacity             |Rationale                                                         |
|------------------------------|---------------------|------------------------------------------------------------------|
|Stage 1: Pattern Extraction   |**Full**             |Foundation of architecture                                        |
|Stage 2: Symbol Formation     |**Substantial**      |Compositional generalization demonstrated (Lake & Baroni, 2018)   |
|Stage 3: Recursive Composition|**Partial**          |Succeeds when pattern-matchable; variable on novel recursive tasks|
|Stage 4: Self-Referential     |**Predicted limited**|Lacks self/world distinction per hypothesis                       |

**Important nuance:** LLMs may exhibit behaviors that *resemble* self-state:

- Expressing uncertainty (but: does confidence track accuracy?)
- Self-correction (but: pattern-matched from training data or genuine error detection?)
- Metacognitive language (but: verbal report vs. computational operation?)

The discrimination framework distinguishes these by examining *calibration on genuinely novel problems*—problems designed to fall outside the training distribution where pattern-matching fails.

### Could LLMs Develop Self-State?

The substrate-neutral hypothesis suggests paths by which LLM-based systems might develop genuine self-state:

1. **Persistent agentic systems.** An LLM embedded in an agentic framework with persistent memory, modifiable state, and objectives tied to maintaining valued conditions (e.g., keeping a user satisfied, maintaining access to resources, preserving learned information) has potential self/world distinction.
1. **Systems with genuine stakes.** An LLM that could be “damaged” (degraded performance, lost access, negative consequences for failed tasks) might develop calibration under selection pressure.
1. **Explicit self-modeling.** Training on tasks that require accurate self-models (predicting own failures, estimating own confidence, modeling own computational limits) might produce functional self-state if combined with genuine evaluation against accuracy.

**Key prediction:** Agentic LLM systems with persistence and stakes should show stronger self-state signatures than stateless LLMs. This is testable.

### Empirical Testing

The discrimination framework generates testable predictions. Using genuinely novel mathematical operators (randomized names, definitions, and parameters designed to fall outside training distributions), we test whether frontier models show the pattern-matching signature or the self-state signature.

**For methodology, implementation, and current results, see [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination).**

### What Remains Open

- Whether any current systems exhibit the full self-state signature
- Whether RLHF calibration reflects genuine self-monitoring or learned hedging patterns
- Mechanism underlying between-model variation
- Whether self-state emerges from scaling, architectural changes, or requires self/world distinction
- Whether attention-based maintenance can implement full MAINTAIN-COMPARE-UPDATE
- Whether persistent agentic systems develop stronger self-state signatures than stateless systems

-----

## Broader Applications

### Developmental Psychology

APH predicts the developmental sequence: Stages 1→2→3→4 should emerge in order, with Stage 4 last and slowest. Children should show the pattern-matching signature (confident errors on novel problems, poor calibration) prior to prefrontal maturation. This is consistent with developmental metacognition literature (Flavell, 1979; Kuhn, 2000) but the specific failure-signature predictions are novel.

### Comparative Cognition

Stage 4 capacity should correlate with:

- Prefrontal cortex development across species (supported: Passingham & Wise, 2012)
- Evidence of uncertainty monitoring in animals (supported: Smith et al., 2003)
- Novelty-sensitive behavioral adjustment

### Robotics and Embodied AI

If self/world distinction drives self-state, embodied AI trained with genuine environmental interaction and survival-like stakes should develop Stage 4 signatures more readily than disembodied systems. This is testable in current robotics platforms.

### Agentic AI Systems

Persistent agents with memory across sessions, modifiable objectives, and stakes tied to self-maintenance represent a test case for the substrate-neutral hypothesis. If such systems develop self-state signatures while stateless systems do not, this supports the hypothesis that what matters is bounded persistence + stakes + inside/outside asymmetry, not biological embodiment specifically.

### Clinical Applications

Conditions affecting prefrontal function (frontal lobe damage, ADHD, schizophrenia) should show specific Stage 4 impairments (confident errors, poor novelty detection) while preserving Stages 1–3. Preliminary evidence supports this pattern (Shallice & Burgess, 1991; Lysaker et al., 2005).

-----

## Framework Status Summary

|Claim                                                       |Status                 |Basis                                                                                     |
|------------------------------------------------------------|-----------------------|------------------------------------------------------------------------------------------|
|Abstraction = symbol formation + composition                |**Established**        |Fodor & Pylyshyn (1988)                                                                   |
|Composition types differ in complexity                      |**Established**        |Halford et al. (1998)                                                                     |
|Working memory has capacity limits                          |**Established**        |Cowan (2001)                                                                              |
|Metacognition develops gradually                            |**Established**        |Flavell (1979)                                                                            |
|Self-state = MAINTAIN-COMPARE-UPDATE operation              |**Proposed definition**|Based on Baddeley (2000)                                                                  |
|Self/world distinction enables self-state                   |**Hypothesis**         |Proposed here; testable                                                                   |
|Self/world distinction requires bounded persistence + stakes|**Hypothesis**         |Substrate-neutral formulation                                                             |
|Biology is one path to self/world distinction, not unique   |**Hypothesis**         |Softening of strong embodiment claims                                                     |
|Pattern-matching shows distinct failure signature           |**Testable**           |See empirical program                                                                     |
|Self-state can be discriminated empirically                 |**Testable**           |See [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination)|

-----

## Papers

### Core Theory (1–10)

|# |Paper                                                                          |Focus                       |Status                          |
|--|-------------------------------------------------------------------------------|----------------------------|--------------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)           |Central thesis              |Theory                          |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)    |Formal definitions          |Theory                          |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)     |Why compression isn’t enough|Theory                          |
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                   |Capacity limits             |Established (reviews literature)|
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)   |Relationship to prediction  |Theory                          |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                       |Stage 3 mechanics           |Theory                          |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)     |Stages 1–4 in detail        |Theory + established findings   |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                  |The self/world hypothesis   |Hypothesis                      |
|9 |[Self and World](papers/self_world_abstraction.md)                             |Self-state architecture     |Hypothesis                      |
|10|[Survival Pressure and the Origins of Abstraction](papers/survival_pressure.md)|Evolutionary argument       |Hypothesis                      |

### Extensions (11–18)

|# |Paper                                                                                |Focus                     |Status     |
|--|-------------------------------------------------------------------------------------|--------------------------|-----------|
|11|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Consciousness connection  |Speculative|
|12|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |Philosophical implications|Speculative|
|13|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal cognition        |Hypothesis |
|14|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotion and stakes        |Hypothesis |
|15|[Social Dynamics](papers/social_dynamics.md)                                         |Social cognition          |Hypothesis |
|16|[Beyond Large Language Models](papers/beyond_llms.md)                                |Future architectures      |Speculative|
|17|[Dual-Process Theory Reconsidered](papers/dual_process_abstraction.md)               |System 1/System 2         |Theory     |
|18|[Neurochemistry as Self-State Abstraction](papers/mind_body_neurochemistry.md)       |Neural substrates         |Hypothesis |

### Empirical

|# |Paper                                                                            |Focus                    |Status          |
|--|---------------------------------------------------------------------------------|-------------------------|----------------|
|19|[Pilot Study: Compositional Hierarchy](papers/pilot_composition_study.md)        |Initial findings         |Preliminary data|
|20|[Hold-and-Check: Task-Specific Dissociations](papers/hold_and_check_study.md)    |Gen/ver asymmetries      |Preliminary data|
|21|[Scaffolding Asymmetry](papers/scaffolding_asymmetry.md)                         |Scaffold effects         |Preliminary data|
|22|[Prompt Sensitivity in LLM Evaluation](papers/verification_pragmatic_artifact.md)|Methodological refinement|Methods         |

### Theoretical

|# |Paper                                                                                 |Focus                        |Status                    |
|--|--------------------------------------------------------------------------------------|-----------------------------|--------------------------|
|23|[The Geometry of Self-Reference](papers/information_geometry.md)                      |Mathematical formalism       |Theory                    |
|24|[Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md)|Empirical program for Stage 4|Methods + preliminary data|

### For Physicists/Engineers

|Document                                                                                    |Purpose                                              |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------|
|[Theoretical Guide for Physicists](papers/theoretical_guide_for_physicists.md)              |Control theory, information theory, dynamical systems|
|[Self-Referential Computation (Python)](code/self_referential_computation_for_physicists.py)|Executable demonstrations                            |

-----

## Empirical Research Program

The repositories below represent ongoing empirical work. Results are preliminary and should be interpreted cautiously.

### Core Framework

[abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) · [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination) · [composition-testing](https://github.com/HillaryDanan/composition-testing) · [scaffolding-asymmetry](https://github.com/HillaryDanan/scaffolding-asymmetry)

### Verification & Calibration

[verification-deficit-replication](https://github.com/HillaryDanan/verification-deficit-replication) · [verification-prompt-variants](https://github.com/HillaryDanan/verification-prompt-variants) · [embeddedness-calibration](https://github.com/HillaryDanan/embeddedness-calibration)

### Embodiment & Grounding

[embodied-cognition](https://github.com/HillaryDanan/embodied-cognition) · [physical-grounding-llm](https://github.com/HillaryDanan/physical-grounding-llm)

### Temporal Cognition

[TIDE](https://github.com/HillaryDanan/TIDE) · [temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm)

<details>
<summary>Additional Research Areas (Exploratory)</summary>

### Self-Reference

[self-referential-dynamics](https://github.com/HillaryDanan/self-referential-dynamics) · [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction) · [geometry-self-reference](https://github.com/HillaryDanan/geometry-self-reference)

### Consciousness (Speculative)

[BIND](https://github.com/HillaryDanan/BIND) · [comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms)

### Social Cognition

[reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence) · [game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite)

### Language

[linguistic-dynamics-theory](https://github.com/HillaryDanan/linguistic-dynamics-theory) · [cross-linguistic-attention-dynamics](https://github.com/HillaryDanan/cross-linguistic-attention-dynamics)

### Geometry & Architecture

[causal-attention-geometry](https://github.com/HillaryDanan/causal-attention-geometry) · [multi-geometric-attention](https://github.com/HillaryDanan/multi-geometric-attention)

### LLM Testing

[llm-habituation-patterns](https://github.com/HillaryDanan/llm-habituation-patterns) · [paradox-induced-oscillations](https://github.com/HillaryDanan/paradox-induced-oscillations)

### Tools

[pattern-analyzer](https://github.com/HillaryDanan/pattern-analyzer) · [concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)

</details>

-----

## Key References

Baddeley, A. (1992). Working memory. *Science*, 255(5044), 556-559.

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. *Psychological Review*, 108(3), 624-652.

Chollet, F. (2019). On the measure of intelligence. *arXiv:1911.01547*. [Preprint]

Clark, A. (1997). *Being There: Putting Brain, Body, and World Together Again*. MIT Press.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87-114.

Crone, E. A., Wendelken, C., Donohue, S., van Leijenhorst, L., & Bunge, S. A. (2006). Neurocognitive development of the ability to manipulate information in working memory. *Proceedings of the National Academy of Sciences*, 103(24), 9315-9320.

Curtis, C. E., & D’Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Damasio, A. R. (1994). *Descartes’ Error: Emotion, Reason, and the Human Brain*. Putnam.

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive–developmental inquiry. *American Psychologist*, 34(10), 906-911.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155-170.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803-831.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569-1579.

Hawkins, J., & Blakeslee, S. (2004). *On Intelligence*. Times Books. [Popular science]

Kuhn, D. (2000). Metacognitive development. *Current Directions in Psychological Science*, 9(5), 178-181.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML*.

Lysaker, P. H., Carcione, A., Dimaggio, G., Johannesen, J. K., Nicolò, G., Procacci, M., & Semerari, A. (2005). Metacognition amidst narratives of self and illness in schizophrenia: Associations with neurocognition, symptoms, insight and quality of life. *Acta Psychiatrica Scandinavica*, 112(1), 64-71.

Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. D. Reidel.

O’Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences*, 24(5), 939-973.

Partee, B. H. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of Formal Semantics* (pp. 281-311). Foris.

Passingham, R. E., & Wise, S. P. (2012). *The Neurobiology of the Prefrontal Cortex*. Oxford University Press.

Piaget, J. (1952). *The Origins of Intelligence in Children*. International Universities Press.

Shallice, T., & Burgess, P. W. (1991). Deficits in strategy application following frontal lobe damage in man. *Brain*, 114(2), 727-741.

Smith, J. D., Shields, W. E., & Washburn, D. A. (2003). The comparative psychology of uncertainty monitoring and metacognition. *Behavioral and Brain Sciences*, 26(3), 317-339.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

## Acknowledgments

This framework benefited from critical feedback on the embeddedness hypothesis, attention mechanisms, and falsifiability criteria. The distinction between learned hedging and genuine calibration was sharpened through discussion. The substrate-neutral formulation—bounded persistence, stakes, and inside/outside asymmetry rather than biological embodiment specifically—emerged from recognizing that biology is one path to self/world distinction, not the only conceivable path.

-----

*“Abstraction is all you need ;)”*

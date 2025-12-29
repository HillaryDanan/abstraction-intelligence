# Abstraction-Intelligence

**What makes something intelligent?**

The **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure—and requires *self-state* for genuine construction beyond pattern matching.

This framework applies to biological cognition, artificial systems, and any substrate capable of information processing. The current empirical program uses large language models (LLMs) as one testbed, but the theoretical claims are general.

-----

## The Core Claim

**Abstraction is the recursive process of forming and composing symbols.**

```
[Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                     ▲                                              │
                     └──────────── [Feedback] ──────────────────────┘
```

Not symbols alone. Not composition alone. Their **mutual refinement through iteration**.

This claim draws on established work in cognitive science: the role of symbolic representation in human reasoning (Fodor & Pylyshyn, 1988), the systematicity of thought (Fodor, 1975), compositional semantics (Partee, 1984), and the structure of working memory (Baddeley, 2000; Cowan, 2001).

**What APH adds:** An explicit developmental hierarchy (Stages 1–4) and the hypothesis that Stage 4 (self-referential abstraction) requires *embeddedness*—a system with stakes in its own outcomes.

-----

## Two Orthogonal Dimensions: Developmental Stages and Composition Types

The framework distinguishes **how abstract** (developmental stages) from **what kind of composition** (composition types). These are related but orthogonal.

### Developmental Stages of Abstraction

|Stage                   |Capacity                              |What It Enables                              |Biological Evidence                                                                |
|------------------------|--------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------|
|1. Pattern Extraction   |Detect statistical regularities       |Compression, prediction                      |Ubiquitous; present in invertebrates (Hawkins & Blakeslee, 2004)                   |
|2. Symbol Formation     |Discrete, recombinable representations|Compositional generalization                 |Language, tool use; emerges in human development ~18-24 months (Piaget, 1952)      |
|3. Recursive Composition|Abstractions as inputs to abstraction |Hierarchical depth, analogy                  |Recursive syntax, planning; ~age 4+ (Hauser et al., 2002)                          |
|4. Self-Referential     |Abstraction over one’s own processing |Metacognition, verification, error correction|Develops gradually; mature ~adolescence (Flavell, 1979; Metcalfe & Shimamura, 1994)|

**Theoretical status:** Stages 1–3 are well-established in cognitive science. Stage 4 as a *distinct computational capacity* (rather than just “thinking about thinking”) is a working hypothesis. See [Paper 7: The Developmental Spectrum](papers/abstraction_developmental_spectrum.md).

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

### The Core Idea

**Self-state** is the capacity to maintain, monitor, and modify representations of one’s own processing during inference—not just as output, but as functional architecture.

This is related to but distinct from:

- **Working memory** (Baddeley, 2000): Self-state is the *executive* component, not the storage buffers
- **Metacognition** (Flavell, 1979): Self-state is the *mechanism* enabling metacognition, not metacognition itself
- **Theory of mind** (Premack & Woodruff, 1978): Self-state is self-directed; ToM applies it to others

### Why Embeddedness Might Matter (Hypothesis)

```
Embedded agents (survival stakes)          Disembodied systems (prediction loss)
            ↓                                          ↓
Self/world distinction required            No self/world distinction needed
            ↓                                          ↓
Asymmetric error costs                     Symmetric error costs
            ↓                                          ↓
Selection pressure for self-monitoring     No selection pressure for self-monitoring
            ↓                                          ↓
Self-state architecture develops           Self-state may not develop
```

**The hypothesis:** Systems that must act in the world with stakes in outcomes develop self-state because errors are costly and asymmetric. Systems optimizing symmetric loss functions (like prediction error) lack this selection pressure.

**Theoretical status:** This is a hypothesis, not established fact. It draws on:

- Evolutionary arguments about the function of consciousness (Dennett, 1991)
- Embodied cognition research (Clark, 1997; Varela et al., 1991)
- Control theory (systems that act need self-models; Conant & Ashby, 1970)

**What would falsify it:**

- A disembodied system developing robust Stage 4 capacity
- An embedded system failing to develop Stage 4 despite adequate training
- Self-state emerging purely from scaling without architectural change

### Active Maintenance ≠ Attention

|Active Maintenance (Stage 4)            |Attention (Retrieval)          |
|----------------------------------------|-------------------------------|
|Explicit holding during comparison      |Weighted retrieval from storage|
|Central executive (Baddeley, 2000)      |Memory access mechanism        |
|Continuous comparison during inference  |Discrete query-and-retrieve    |
|Capacity-limited (~4 items; Cowan, 2001)|Context-window limited         |

This distinction matters because systems can have sophisticated attention without having self-state.

-----

## Predictions Across Systems

The framework makes predictions for any system capable of abstraction:

### Biological Systems

|Prediction                                   |Status       |Evidence                                |
|---------------------------------------------|-------------|----------------------------------------|
|Stage 4 develops later than Stages 1–3       |**Supported**|Developmental trajectory (Flavell, 1979)|
|Stage 4 correlates with prefrontal maturation|**Supported**|Neuroimaging (Curtis & D’Esposito, 2003)|
|Stage 4 impaired by working memory load      |**Supported**|Dual-task interference (Baddeley, 1992) |
|Stage 4 shows ~4-item capacity limit         |**Supported**|Cowan (2001), Oberauer et al. (2016)    |

### Artificial Systems (General Predictions)

|Prediction                                                      |Status                 |Notes                                    |
|----------------------------------------------------------------|-----------------------|-----------------------------------------|
|Systems trained on prediction alone will show Stage 4 limits    |**Open**               |Testable across architectures            |
|Stage 4 capacity won’t emerge from scaling alone                |**Open**               |Requires longitudinal study across scales|
|Embodied training (robotics, RL with stakes) may produce Stage 4|**Open**               |Testable in embodied AI                  |
|Scaffolding can provide “prosthetic” Stage 4                    |**Partially supported**|See LLM case study below                 |

-----

## Case Study: Large Language Models

LLMs provide a useful testbed for APH because they are sophisticated pattern-matchers trained on a symmetric loss function (next-token prediction) without embodiment. If the embeddedness hypothesis is correct, LLMs should show systematic Stage 4 limitations despite strong Stage 1–3 performance.

> **Note:** All findings below are from preliminary studies (N=100-700). Interpretations are working hypotheses requiring replication.

### Summary of Findings

|Stage                         |LLM Capacity   |Evidence                                                                               |
|------------------------------|---------------|---------------------------------------------------------------------------------------|
|Stage 1: Pattern Extraction   |**Full**       |Foundation of architecture                                                             |
|Stage 2: Symbol Formation     |**Substantial**|Compositional generalization (Lake & Baroni, 2018)                                     |
|Stage 3: Recursive Composition|**Partial**    |Succeeds when pattern-matchable; fails on novel operators                              |
|Stage 4: Self-Referential     |**Unclear**    |Some evidence (miscalibration, generation deficits); key evidence ruled out as artifact|

This profile—strong at Stages 1–2, partial at Stage 3, uncertain at Stage 4—is what we term **disembodied abstraction**.

### What’s Been Confirmed

|Finding                                          |Evidence                               |
|-------------------------------------------------|---------------------------------------|
|Pattern-matchable recursive tasks at ceiling     |Bracket depth, pointer chase: 100%     |
|Novel operators cause failure                    |Invented operators: 50% (Stage 3 limit)|
|Multi-constraint relations cause failure         |Relation mapping: 28%                  |
|Task-specific generation/verification asymmetries|See Paper 20                           |
|Prompt framing dramatically affects performance  |10% → 96.7% based on question format   |

### What’s Been Ruled Out

|Original Claim                                   |New Evidence                                                      |Updated Interpretation                                                 |
|-------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------|
|Arithmetic verification deficit = Stage 4 failure|Prompt variant study (N=150): neutral framing restores performance|**Pragmatic inference artifact** (Grice, 1975), not computational limit|

**Methodological lesson:** Apparent cognitive deficits may reflect prompt artifacts. This finding (Paper 22) argues for prompt-controlled testing before attributing failures to architectural limits.

### What Remains Open

- Does the logic generation deficit survive prompt-controlled testing?
- Which generation/verification asymmetries reflect genuine Stage 4 limits vs. artifacts?
- Can scaffolding provide genuine “prosthetic self-state” or is it prompt-framing effects?

See [Paper 24: Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md) for an empirical program to address these questions.

### Detailed Empirical Results

<details>
<summary>Generation-Verification Study (N=700)</summary>

|Task      |Generation|Verification|Δ   |Pattern             |
|----------|----------|------------|----|--------------------|
|Arithmetic|100%      |76%         |+24%|Verification deficit|
|Multistep |100%      |74%         |+26%|Verification deficit|
|Logic     |56%       |100%        |-44%|Generation deficit  |
|Word count|82%       |100%        |-18%|Generation deficit  |
|Others    |~100%     |~100%       |0%  |No asymmetry        |

**Overall:** 91.1% vs 92.6%, p=0.58 (null)

**Updated interpretation:** Arithmetic verification deficit is a prompt artifact. Logic generation deficit mechanism untested.

</details>

<details>
<summary>Scaffolding Asymmetry Study (N=600)</summary>

|Task               |Baseline|Self-Monitor  |Constraint|
|-------------------|--------|--------------|----------|
|Arithmetic (Claude)|70%     |**98%** (+28%)|60% (-10%)|
|Logic (Claude)     |64%     |32% (-32%)    |34% (-30%)|
|Arithmetic (GPT-4o)|88%     |90% (+2%)     |66% (-22%)|
|Logic (GPT-4o)     |66%     |60% (-6%)     |58% (-8%) |

**Interpretation (Cognitive Overhead Account):** Scaffolding imposes processing costs. Benefit > cost only when scaffold addresses the task’s bottleneck.

</details>

<details>
<summary>What Didn't Replicate</summary>

|Finding                         |Pilot |Extended|
|--------------------------------|------|--------|
|A–B vs. C–D uniform dissociation|d=0.71|d=0.00  |

Composition type alone doesn’t predict failure.

</details>

-----

## Broader Applications

### Developmental Psychology

APH predicts the developmental sequence: Stages 1→2→3→4 should emerge in order, with Stage 4 last and slowest. This aligns with Piaget’s stages and subsequent work on metacognitive development (Flavell, 1979).

**Testable:** Children should show the same failure signatures on Stage 4 tasks that we observe in LLMs, prior to prefrontal maturation.

### Comparative Cognition

APH predicts that Stage 4 capacity should correlate with:

- Prefrontal cortex development across species
- Evidence of metacognition in animals (uncertainty monitoring; Smith et al., 2003)
- Flexible behavioral control (not just learned patterns)

### Robotics and Embodied AI

If embeddedness drives self-state, embodied AI trained with survival-like stakes should develop Stage 4 capacity more readily than disembodied systems.

**Testable:** Compare reinforcement learning agents with genuine costs (physical damage, resource depletion) to simulated-cost agents on Stage 4 tasks.

### Clinical Applications

Conditions affecting prefrontal function (ADHD, frontal lesions, schizophrenia) should show specific Stage 4 impairments while preserving Stages 1–3.

-----

## Framework Status: What’s Established vs. Hypothesized

|Claim                                              |Status                 |Basis                                |
|---------------------------------------------------|-----------------------|-------------------------------------|
|Abstraction involves symbol formation + composition|**Established**        |Fodor & Pylyshyn (1988), Fodor (1975)|
|Composition types differ in complexity             |**Established**        |Halford et al. (1998)                |
|Working memory has ~4-item capacity limit          |**Established**        |Cowan (2001)                         |
|Metacognition develops gradually                   |**Established**        |Flavell (1979)                       |
|Stage 4 as distinct computational capacity         |**Hypothesis**         |Proposed here; needs testing         |
|Embeddedness necessary for Stage 4                 |**Hypothesis**         |Proposed here; needs testing         |
|LLMs systematically lack Stage 4                   |**Partially supported**|Some evidence; key evidence ruled out|
|Scaling won’t produce Stage 4                      |**Open**               |Untested                             |

-----

## Visualizations

|Visualization                                                                    |Description                                                |
|---------------------------------------------------------------------------------|-----------------------------------------------------------|
|[Self-State in the Information Plane](visualizations/self_state_abstraction.html)|Interactive 3D: pattern-matching vs. self-state abstraction|

-----

## Papers

### Core Theory (1–10)

|# |Paper                                                                          |Focus                       |
|--|-------------------------------------------------------------------------------|----------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)           |Central thesis              |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)    |Formal definitions          |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)     |Why compression isn’t enough|
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                   |Capacity limits             |
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)   |Relationship to prediction  |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                       |Stage 3 mechanics           |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)     |Stages 1–4 in detail        |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                  |The embeddedness hypothesis |
|9 |[Self and World](papers/self_world_abstraction.md)                             |Self-state architecture     |
|10|[Survival Pressure and the Origins of Abstraction](papers/survival_pressure.md)|Evolutionary argument       |

### Extensions (11–18)

|# |Paper                                                                                |Focus                     |
|--|-------------------------------------------------------------------------------------|--------------------------|
|11|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Consciousness connection  |
|12|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |Philosophical implications|
|13|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal cognition        |
|14|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotion and stakes        |
|15|[Social Dynamics](papers/social_dynamics.md)                                         |Social cognition          |
|16|[Beyond Large Language Models](papers/beyond_llms.md)                                |Future architectures      |
|17|[Dual-Process Theory Reconsidered](papers/dual_process_abstraction.md)               |System 1/System 2         |
|18|[Neurochemistry as Self-State Abstraction](papers/mind_body_neurochemistry.md)       |Neural substrates         |

### Empirical (LLM Case Study)

|# |Paper                                                                                  |Focus                    |
|--|---------------------------------------------------------------------------------------|-------------------------|
|19|[Pilot Study: Compositional Hierarchy](papers/pilot_composition_study.md)              |Initial findings         |
|20|[Hold-and-Check: Task-Specific Dissociations](papers/hold_and_check_study.md)          |Gen/ver asymmetries      |
|21|[Scaffolding Asymmetry](papers/scaffolding_asymmetry.md)                               |Scaffold effects         |
|22|[Verification Deficit as Pragmatic Artifact](papers/verification_pragmatic_artifact.md)|Methodological correction|

### Theoretical

|# |Paper                                                                                 |Focus                        |
|--|--------------------------------------------------------------------------------------|-----------------------------|
|23|[The Geometry of Self-Reference](papers/information_geometry.md)                      |Mathematical formalism       |
|24|[Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md)|Empirical program for Stage 4|

### For Physicists/Engineers

|Document                                                                                    |Purpose                                              |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------|
|[Theoretical Guide for Physicists](papers/theoretical_guide_for_physicists.md)              |Control theory, information theory, dynamical systems|
|[Self-Referential Computation (Python)](code/self_referential_computation_for_physicists.py)|Executable demonstrations                            |

-----

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

-----

## Key References

Baddeley, A. (1992). Working memory. *Science*, 255(5044), 556-559.

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Chollet, F. (2019). On the measure of intelligence. *arXiv:1911.01547*.

Clark, A. (1997). *Being There: Putting Brain, Body, and World Together Again*. MIT Press.

Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89-97.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87-114.

Curtis, C. E., & D’Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown and Company.

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive–developmental inquiry. *American Psychologist*, 34(10), 906-911.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155-170.

Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics* (Vol. 3, pp. 41-58). Academic Press.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803-831.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569-1579.

Hawkins, J., & Blakeslee, S. (2004). *On Intelligence*. Times Books.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML*.

Metcalfe, J., & Shimamura, A. P. (Eds.). (1994). *Metacognition: Knowing About Knowing*. MIT Press.

Oberauer, K., Farrell, S., Jarrold, C., & Lewandowsky, S. (2016). What limits working memory capacity? *Psychological Bulletin*, 142(7), 758-799.

Partee, B. H. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of Formal Semantics* (pp. 281-311). Foris.

Piaget, J. (1952). *The Origins of Intelligence in Children*. International Universities Press.

Premack, D., & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences*, 1(4), 515-526.

Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*.

Smith, J. D., Shields, W. E., & Washburn, D. A. (2003). The comparative psychology of uncertainty monitoring and metacognition. *Behavioral and Brain Sciences*, 26(3), 317-339.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

*“Abstraction is all you need ;)”*

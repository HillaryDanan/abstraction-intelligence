# Abstraction-Intelligence

**What makes something intelligent?**

The **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure—and requires *self-state* for genuine construction beyond pattern matching.

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

**What APH adds:** An explicit developmental hierarchy (Stages 1–4), the hypothesis that Stage 4 (self-referential abstraction) requires *embeddedness*—a system with stakes in its own outcomes—and a criterion for discriminating self-state from pattern-matching based on **response to novelty under stakes**.

-----

## Two Orthogonal Dimensions: Developmental Stages and Composition Types

The framework distinguishes **how abstract** (developmental stages) from **what kind of composition** (composition types). These are related but orthogonal.

### Developmental Stages of Abstraction

|Stage                   |Capacity                                   |What It Enables                              |Biological Evidence                                             |
|------------------------|-------------------------------------------|---------------------------------------------|----------------------------------------------------------------|
|1. Pattern Extraction   |Detect statistical regularities            |Compression, prediction                      |Ubiquitous; present in invertebrates (Hawkins & Blakeslee, 2004)|
|2. Symbol Formation     |Discrete, recombinable representations     |Compositional generalization                 |Language, tool use; ~18-24 months (Piaget, 1952)                |
|3. Recursive Composition|Abstractions as inputs to abstraction      |Hierarchical depth, analogy                  |Recursive syntax, planning; ~age 4+ (Hauser et al., 2002)       |
|4. Self-Referential     |Maintain-compare-update over own processing|Metacognition, verification, error correction|Develops gradually; mature ~adolescence (Flavell, 1979)         |

See [Paper 7: The Developmental Spectrum](papers/abstraction_developmental_spectrum.md) for full treatment.

### Composition Types (A–D)

|Type                |Structure                  |Example                                |Required Stage|
|--------------------|---------------------------|---------------------------------------|--------------|
|**A: Concatenative**|A + B → AB                 |"blue bird"                            |Stage 2       |
|**B: Role-filler**  |R(x) + S(y) → R(x)S(y)     |AGENT(dog) + ACTION(chased)            |Stage 2       |
|**C: Recursive**    |A contains [B contains C]  |"The dog [that chased the cat [that…]]"|Stage 3       |
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

This is the **central executive** operation in Baddeley's (2000) working memory model. It is distinct from:

- **Attention**: Weighted retrieval (no persistent holding)
- **Storage**: Passive retention (no active comparison)
- **Metacognition**: The *content* of self-knowledge (self-state is the *mechanism*)

### Why Embeddedness Matters (Hypothesis)

The key insight: **for an embedded agent, novelty is a threat signal.**

```
Embedded agents (survival stakes)          Disembodied systems (prediction loss)
            ↓                                          ↓
Novelty = potential danger                 Novelty = unfamiliar input
            ↓                                          ↓
Selection pressure for:                    No selection pressure for:
  - Novelty detection                        - Novelty detection
  - Conservative behavior under uncertainty  - Stakes-sensitive behavior
  - Calibrated confidence                    - Calibrated confidence
            ↓                                          ↓
Self-state architecture develops           Self-state may not develop
```

An organism that treats novel situations the same as familiar ones dies. Novelty must trigger a distinct processing mode—heightened monitoring, reduced confidence, behavioral caution. This requires self-state: the system must *detect* that the current situation falls outside familiar patterns and *adjust* behavior accordingly.

Prediction loss is symmetric: errors on novel and familiar inputs contribute equally. There is no selection pressure for novelty detection per se.

**Theoretical status:** Hypothesis. Draws on evolutionary function of consciousness (Dennett, 1991), embodied cognition (Clark, 1997; Varela et al., 1991), and the good regulator theorem (Conant & Ashby, 1970).

### How to Discriminate Self-State from Pattern-Matching

The critical question: How do we distinguish genuine self-state from sophisticated interpolation?

**Not by success.** Any finite behavior can be pattern-matched from sufficient training data.

**By failure topology.** Self-state and pattern-matching fail *differently* on novel problems:

|Signature             |Self-State Prediction                              |Pattern-Matching Prediction                   |
|----------------------|---------------------------------------------------|----------------------------------------------|
|**Novelty detection** |Confidence drops on novel problems                 |Uniform confidence (novelty-blind)            |
|**Error types**       |Conservative errors (hedging, "I don't know")      |Confident errors (confabulation)              |
|**Stakes sensitivity**|Behavior changes when stakes described             |Behavior unchanged (stake-blind)              |
|**Calibration**       |Confidence tracks actual accuracy on novel problems|No confidence-accuracy relationship           |
|**Capacity limits**   |Principled limits with gradual degradation         |Distribution-bounded limits with cliff-edge   |
|**Interference**      |Similarity-based (like items compete)              |Semantic blending without systematic structure|

**The central test:** Calibration on genuinely novel problems. A system that shows calibrated confidence on novel problems—confidence tracking actual accuracy—has functional self-state. This is very difficult to pattern-match because it requires real-time assessment of processing difficulty.

See [Paper 24: Discriminating Self-State from Pattern-Matching](papers/self_state_discrimination.md) for the full empirical program, and [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination) for experimental implementation and preliminary data.

-----

## Predictions Across Systems

### Biological Systems

|Prediction                                    |Status       |Evidence                                                       |
|----------------------------------------------|-------------|---------------------------------------------------------------|
|Stage 4 develops later than Stages 1–3        |**Supported**|Developmental trajectory (Flavell, 1979)                       |
|Stage 4 correlates with prefrontal maturation |**Supported**|Neuroimaging (Curtis & D'Esposito, 2003)                       |
|Stage 4 impaired by working memory load       |**Supported**|Dual-task interference (Baddeley, 1992)                        |
|Novel situations trigger heightened monitoring|**Supported**|Orienting response, uncertainty monitoring (Smith et al., 2003)|

### Artificial Systems (Predictions)

|Prediction                                                     |Status       |Notes                                            |
|---------------------------------------------------------------|-------------|-------------------------------------------------|
|Systems without stakes show confident failure on novelty       |**Testable** |See [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination) for empirical program|
|Self-state won't emerge from scaling prediction-trained systems|**Open**     |Requires longitudinal study across model scales  |
|Embodied training with genuine stakes may produce Stage 4      |**Open**     |Testable in robotics/RL with survival-like stakes|
|Scaffolding can provide "prosthetic" self-state                |**Open**     |External monitors may substitute for internal    |

-----

## Case Study: Large Language Models

LLMs are trained on symmetric prediction loss without embodiment. If the embeddedness hypothesis is correct, they should show the pattern-matching signature: confident failure on novel problems, stake-blindness, poor calibration outside the training distribution.

### The LLM Profile (Theoretical Prediction)

|Stage                         |Capacity                            |Evidence                                                  |
|------------------------------|------------------------------------|---------------------------------------------------------|
|Stage 1: Pattern Extraction   |**Full**                            |Foundation of architecture                                |
|Stage 2: Symbol Formation     |**Substantial**                     |Compositional generalization (Lake & Baroni, 2018)        |
|Stage 3: Recursive Composition|**Partial**                         |Succeeds when pattern-matchable; variable on novel tasks  |
|Stage 4: Self-Referential     |**Predicted absent**                |Systems lack embeddedness; see empirical testing below    |

The embeddedness hypothesis predicts LLMs should show the pattern-matching signature (novelty-blind confidence, confident errors, poor calibration on genuinely novel problems) because they lack survival stakes.

### Empirical Testing

The discrimination framework above generates testable predictions. Using genuinely novel mathematical operators (randomized names, definitions, and parameters designed to fall outside training distributions), we test whether frontier models show the pattern-matching signature or the self-state signature.

**For methodology, implementation, and current results, see [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination).**

The empirical repo contains:
- Experimental paradigms for novelty detection, error types, stakes sensitivity, and calibration
- Code for testing GPT-4o, Gemini, Claude, and other models
- Preliminary data (N=150 per paradigm per model) with statistical analysis
- Discussion of findings and their interpretation

**Theoretical status:** Theory and data are maintained separately. The framework's validity does not depend on any particular model's performance—it provides testable predictions that empirical work can support, refute, or complicate.

### What Remains Open

- Whether any current systems exhibit the full self-state signature profile
- Mechanism underlying between-model variation in calibration
- Stakes sensitivity with genuine (not described) consequences
- Longitudinal study of whether self-state emerges from scaling
- Embodied training paradigms with survival-like stakes

<details>
<summary>Additional Empirical Results</summary>

**Generation-Verification Study (N=700)**

|Task      |Generation|Verification|Δ   |
|----------|----------|------------|----|
|Arithmetic|100%      |76%         |+24%|
|Multistep |100%      |74%         |+26%|
|Logic     |56%       |100%        |-44%|
|Word count|82%       |100%        |-18%|
|Others    |~100%     |~100%       |0%  |

Task-specific asymmetries exist; mechanisms vary by task.

**Scaffolding Asymmetry Study (N=600)**

|Task               |Baseline|Self-Monitor|Constraint|
|-------------------|--------|------------|----------|
|Arithmetic (Claude)|70%     |98%         |60%       |
|Logic (Claude)     |64%     |32%         |34%       |
|Arithmetic (GPT-4o)|88%     |90%         |66%       |
|Logic (GPT-4o)     |66%     |60%         |58%       |

Scaffolds help when addressing the task's bottleneck; otherwise they add overhead.

**Composition Type Dissociation**

Pilot: d=0.71; Extended: d=0.00. Composition type alone doesn't predict failure.

</details>

-----

## Broader Applications

### Developmental Psychology

APH predicts the developmental sequence: Stages 1→2→3→4 should emerge in order, with Stage 4 last and slowest. Children should show the pattern-matching signature (confident errors on novel problems, poor calibration) prior to prefrontal maturation.

### Comparative Cognition

Stage 4 capacity should correlate with:

- Prefrontal cortex development across species
- Evidence of uncertainty monitoring in animals (Smith et al., 2003)
- Novelty-sensitive behavioral adjustment

### Robotics and Embodied AI

If embeddedness drives self-state, embodied AI trained with survival-like stakes should develop Stage 4 signatures: lower confidence on novel situations, conservative errors, functional stakes sensitivity.

### Clinical Applications

Conditions affecting prefrontal function should show specific Stage 4 impairments (confident errors, poor novelty detection) while preserving Stages 1–3.

-----

## Framework Status

|Claim                                            |Status                 |Basis                                          |
|-------------------------------------------------|-----------------------|-----------------------------------------------|
|Abstraction = symbol formation + composition     |**Established**        |Fodor & Pylyshyn (1988)                        |
|Composition types differ in complexity           |**Established**        |Halford et al. (1998)                          |
|Working memory has capacity limits               |**Established**        |Cowan (2001)                                   |
|Metacognition develops gradually                 |**Established**        |Flavell (1979)                                 |
|Self-state = MAINTAIN-COMPARE-UPDATE operation   |**Proposed definition**|Based on Baddeley (2000)                       |
|Novelty-under-stakes drives self-state selection |**Hypothesis**         |Proposed here                                  |
|Pattern-matching shows distinct failure signature|**Testable**           |See [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination)|

-----

## Visualizations

|Visualization                                                                    |Description                                                          |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------|
|[Self-State in the Information Plane](visualizations/self_state_abstraction.html)|Interactive 3D: pattern-matching vs. self-state (theoretical model) |

Note: The visualization illustrates the theoretical distinction being empirically tested. See [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination) for current findings.

-----

## Papers

### Core Theory (1–10)

|# |Paper                                                                          |Focus                       |
|--|-------------------------------------------------------------------------------|----------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)           |Central thesis              |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)    |Formal definitions          |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)     |Why compression isn't enough|
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

### Empirical

|# |Paper                                                                            |Focus                    |
|--|---------------------------------------------------------------------------------|-------------------------|
|19|[Pilot Study: Compositional Hierarchy](papers/pilot_composition_study.md)        |Initial findings         |
|20|[Hold-and-Check: Task-Specific Dissociations](papers/hold_and_check_study.md)    |Gen/ver asymmetries      |
|21|[Scaffolding Asymmetry](papers/scaffolding_asymmetry.md)                         |Scaffold effects         |
|22|[Prompt Sensitivity in LLM Evaluation](papers/verification_pragmatic_artifact.md)|Methodological refinement|

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

### 🔬 Verification & Calibration Studies

[verification-deficit-replication](https://github.com/HillaryDanan/verification-deficit-replication) · [verification-prompt-variants](https://github.com/HillaryDanan/verification-prompt-variants) · [self-state-discrimination](https://github.com/HillaryDanan/self-state-discrimination)

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

Curtis, C. E., & D'Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown and Company.

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive–developmental inquiry. *American Psychologist*, 34(10), 906-911.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155-170.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803-831.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569-1579.

Hawkins, J., & Blakeslee, S. (2004). *On Intelligence*. Times Books.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML*.

Metcalfe, J., & Shimamura, A. P. (Eds.). (1994). *Metacognition: Knowing About Knowing*. MIT Press.

Oberauer, K., Farrell, S., Jarrold, C., & Lewandowsky, S. (2016). What limits working memory capacity? *Psychological Bulletin*, 142(7), 758-799.

Partee, B. H. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of Formal Semantics* (pp. 281-311). Foris.

Piaget, J. (1952). *The Origins of Intelligence in Children*. International Universities Press.

Smith, J. D., Shields, W. E., & Washburn, D. A. (2003). The comparative psychology of uncertainty monitoring and metacognition. *Behavioral and Brain Sciences*, 26(3), 317-339.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

*"Abstraction is all you need ;)"*

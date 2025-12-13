# Abstraction-Intelligence

**What makes something intelligent?**

The **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure.

-----

## The Core Claim

**Abstraction is the recursive process of forming and composing symbols.**

```
    [Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                         ▲                                              │
                         └──────────── [Feedback] ──────────────────────┘
```

Not symbols alone. Not composition alone. Their **mutual refinement through iteration**.

-----

## The Composition Hierarchy

|Type                 |Structure                  |Example                                   |
|---------------------|---------------------------|------------------------------------------|
|**3a: Concatenative**|A + B → AB                 |“blue bird”                               |
|**3b: Role-filler**  |R(x) + S(y) → R(x)S(y)     |AGENT(dog) + ACTION(chased) + PATIENT(cat)|
|**3c: Recursive**    |A contains [B contains C]  |“The dog [that chased the cat [that…]]”   |
|**3d: Analogical**   |Structure(A) → Structure(B)|atom:nucleus :: solar system:sun          |

**Prediction:** Systems show 3a-3b success with 3c-3d failure. Bees do role-filler (waggle dance), not recursion. LLMs degrade faster on recursive depth than role-filler novelty.

-----

## Embeddedness

Strong interaction requires **novelty detection**—recognizing unfamiliar against a background of familiar.

Novelty is relational. An input isn’t novel in itself—it’s novel *to a subject*. This requires:

1. **Persistent self** → accumulated experience (“what’s familiar to me”)
1. **Self/world distinction** → reference frame for locating novelty
1. **Embeddedness** → what makes persistence and self/world possible

```
Embeddedness → Persistent self → Familiar/unfamiliar distinction → Novelty detection → Pressure to expand primitives → Strong interaction
```

**Five components of embeddedness:**

- Action-consequence contingency
- Feedback closure
- Temporal persistence
- Self-boundary awareness
- Environmental stability

**Operationalizing novelty detection:** To avoid circularity, we specify four measurable criteria independent of embeddedness:

|Criterion                     |Operationalization                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------|
|**Calibration**               |Confidence decreases appropriately for OOD inputs (Guo et al., 2017)                     |
|**Processing differentiation**|Novel inputs trigger distinct internal processing, not just lower confidence             |
|**Response systematicity**    |Novel combinations of familiar components yield appropriate outputs (Lake & Baroni, 2018)|
|**Uncertainty propagation**   |Input novelty propagates to output uncertainty rather than confident confabulation       |

The hypothesis: embeddedness/stakes is necessary for meeting these criteria. Empirically testable.

**Why stakes matter (hypothesis):**

Survival pressure creates asymmetric costs—misclassifying threat as familiar can be fatal; false alarms merely waste energy (Öhman et al., 2001). But why *different architecture* rather than just stronger optimization?

- **Phylogenetic vs. ontogenetic:** Stakes during *evolution* select for architectures; stakes during *operation* modulate which capacities are used. The claim: selection under stakes produced architecture capable of construction. LLMs weren’t selected; they were optimized on symmetric loss.
- **Asymmetric vs. symmetric pressure:** Symmetric loss (prediction error) rewards compression—minimizing average error. Asymmetric loss (survival) rewards worst-case handling—novel threats must be addressed even at efficiency cost. This selects for construction as a hedge against unbounded novelty. *(Testable: compare architectures trained under symmetric vs. asymmetric loss.)*
- **Candidate architectural feature:** Gating mechanisms that switch between retrieval and construction based on novelty. The locus coeruleus-norepinephrine system modulates exploration vs. exploitation based on uncertainty (Aston-Jones & Cohen, 2005). Biological cognition gates processing mode; LLMs apply identical forward passes regardless of input novelty.
- **On necessity:** Stakes are the known path to construction-capable architecture. Whether alternative paths exist is open. We claim *sufficiency* with confidence; *necessity* remains hypothesis.

**Why 3c-3d specifically (hypothesis):**

- **3a-3b:** Bounded combinatorial space. Can be encountered in training and stored. Pattern matching suffices.
- **3c-3d:** Unbounded generative space. Recursive depth extends indefinitely; analogical mappings span arbitrary domains. Cannot be precomputed.

When target space is unbounded, retrieval fails—*online construction* required. (See [Paper 10](papers/survival_pressure.md).)

**Compression vs. Generation:**

|              |Compression                                    |Generation                                    |
|--------------|-----------------------------------------------|----------------------------------------------|
|**Definition**|Finding structure within training distribution |Constructing outputs with no training coverage|
|**Operation** |Interpolation between known points             |Extrapolation into unbounded space            |
|**3a-3b**     |Sufficient (bounded space is coverable)        |Not required                                  |
|**3c-3d**     |Insufficient (unbounded space exceeds coverage)|Required                                      |

**Prediction:** Compression asymptotes on 3c-3d as coverable space is exhausted. Generation doesn’t asymptote because it’s not coverage-limited. Scaling improves compression; it doesn’t produce generation.

**On LLMs:** Within a conversation, LLMs have weak temporal persistence and action-consequence contingency. But they lack self-boundary awareness, cross-context stability, gating mechanisms, and stakes. This predicts principled 3c-3d limitations that scaling alone cannot overcome—hypothesis pending empirical test. Whether alternative paths to 3c-3d exist remains open.

-----

## Predictions

|Prediction                                                                                      |Falsification                                                        |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|Composition types dissociate (3a-3b vs. 3c-3d)                                                  |No differences found                                                 |
|Recursive depth degrades faster than role-filler novelty                                        |Identical degradation curves                                         |
|Bees: role-filler yes, recursive no                                                             |Bees succeed at recursion                                            |
|Non-embedded systems fail novelty criteria (calibration, systematicity, uncertainty propagation)|System without embeddedness meets all four criteria                  |
|Systematicity failure: novel combinations fail despite component competence                     |Novel combinations succeed proportionally to component familiarity   |
|Systems without stakes plateau on 3c-3d despite scaling                                         |Scaled systems show continued 3c-3d improvement proportional to scale|
|Asymmetric loss training improves 3c-3d over symmetric loss                                     |No difference between loss types                                     |

-----

## Papers

**Core (1–10):**

|# |Paper                                                                          |
|--|-------------------------------------------------------------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)           |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)    |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)     |
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                   |
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)   |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                       |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)     |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                  |
|9 |[Self and World](papers/self_world_abstraction.md)                             |
|10|[Survival Pressure and the Origins of Abstraction](papers/survival_pressure.md)|

**Extensions (11–17):**

|# |Paper                                                                                |
|--|-------------------------------------------------------------------------------------|
|11|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|
|12|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |
|13|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |
|14|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |
|15|[Social Dynamics](papers/social_dynamics.md)                                         |
|16|[Beyond Large Language Models](papers/beyond_llms.md)                                |
|17|[Dual-Process Theory Reconsidered](papers/dual_process_abstraction.md)               |

-----

## Empirical Research Program

### 🧠 Core Framework

[abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) ·
[composition-type-dissociation](https://github.com/HillaryDanan/composition-type-dissociation) ·
[compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction) ·
[compositional-dual-process](https://github.com/HillaryDanan/compositional-dual-process) ·
[embeddedness-calibration](https://github.com/HillaryDanan/embeddedness-calibration) ·
[emergent-factorization](https://github.com/HillaryDanan/emergent-factorization) ·
[reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum)

### 🔄 Self-Reference

[self-referential-dynamics](https://github.com/HillaryDanan/self-referential-dynamics) ·
[computational-self-construction](https://github.com/HillaryDanan/computational-self-construction) ·
[ouroboros-learning](https://github.com/HillaryDanan/ouroboros-learning) ·
[recursive-reality](https://github.com/HillaryDanan/recursive-reality)

### ⏱️ Temporal

[TIDE](https://github.com/HillaryDanan/TIDE) ·
[TIDE-resonance](https://github.com/HillaryDanan/TIDE-resonance) ·
[TIDE-analysis](https://github.com/HillaryDanan/TIDE-analysis) ·
[temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm) ·
[temporal-myopia-llm](https://github.com/HillaryDanan/temporal-myopia-llm) ·
[llm-time-decay](https://github.com/HillaryDanan/llm-time-decay) ·
[curved-cognition](https://github.com/HillaryDanan/curved-cognition)

### 🌍 Embodiment

[embodied-cognition](https://github.com/HillaryDanan/embodied-cognition) ·
[physical-grounding-llm](https://github.com/HillaryDanan/physical-grounding-llm) ·
[TERRA-embodied-interpretability](https://github.com/HillaryDanan/TERRA-embodied-interpretability)

### 🪞 Consciousness

[BIND](https://github.com/HillaryDanan/BIND) ·
[comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms) ·
[hexagonal-consciousness-suite](https://github.com/HillaryDanan/hexagonal-consciousness-suite) ·
[computational-emergence-theory](https://github.com/HillaryDanan/computational-emergence-theory)

### 👥 Social

[reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence) ·
[game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite) ·
[trust-calibration-framework](https://github.com/HillaryDanan/trust-calibration-framework)

### 🗣️ Language

[linguistic-dynamics-theory](https://github.com/HillaryDanan/linguistic-dynamics-theory) ·
[linguistic-memory-framework](https://github.com/HillaryDanan/linguistic-memory-framework) ·
[cross-linguistic-attention-dynamics](https://github.com/HillaryDanan/cross-linguistic-attention-dynamics) ·
[benign-violations](https://github.com/HillaryDanan/benign-violations)

### 🔬 Geometry

[causal-attention-geometry](https://github.com/HillaryDanan/causal-attention-geometry) ·
[multi-geometric-attention](https://github.com/HillaryDanan/multi-geometric-attention) ·
[relativistic-interpretability](https://github.com/HillaryDanan/relativistic-interpretability) ·
[spectral-representations](https://github.com/HillaryDanan/spectral-representations)

### 🧪 LLM Testing

[llm-habituation-patterns](https://github.com/HillaryDanan/llm-habituation-patterns) ·
[nonlinear-dialogue-dynamics](https://github.com/HillaryDanan/nonlinear-dialogue-dynamics) ·
[paradox-induced-oscillations](https://github.com/HillaryDanan/paradox-induced-oscillations) ·
[retroactive-causality](https://github.com/HillaryDanan/retroactive-causality) ·
[claude-emergence-patterns](https://github.com/HillaryDanan/claude-emergence-patterns)

### 🔧 Architecture

[information-atoms](https://github.com/HillaryDanan/information-atoms) ·
[hexagonal-vision-research](https://github.com/HillaryDanan/hexagonal-vision-research) ·
[computational-substrates](https://github.com/HillaryDanan/computational-substrates) ·
[cognitive-architectures-ai](https://github.com/HillaryDanan/cognitive-architectures-ai)

### 📊 Tools

[pattern-analyzer](https://github.com/HillaryDanan/pattern-analyzer) ·
[concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)

-----

## References

Aston-Jones, G., & Cohen, J. D. (2005). An integrative theory of locus coeruleus-norepinephrine function: Adaptive gain and optimal performance. *Annual Review of Neuroscience*, 28, 403-450.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *ICML*.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML*.

Öhman, A., Flykt, A., & Esteves, F. (2001). Emotion drives attention: Detecting the snake in the grass. *Journal of Experimental Psychology: General*, 130(3), 466-478.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

*“Abstraction is all you need ;)”*

# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: the proposal that intelligence, across substrates, is fundamentally the capacity to form compositional representations—representations that combine via systematic rules to generate novel meaningful structures. A reflex arc attends; it does not abstract. The hypothesis: intelligence begins where composition begins.

-----

## The Core Idea

**Abstraction is the formation of compositional representations.**

A representation is compositional when:

1. It consists of parts (constituents) that are themselves meaningful
1. The meaning of the whole is determined by the meanings of the parts and their mode of combination
1. The same parts can recombine to form different wholes with different meanings

This is a *single criterion*, not a list of components. The hypothesis: a system abstracts if and only if it forms representations that compose. The test is **systematicity**—the capacity to understand or produce novel combinations of familiar elements (Fodor & Pylyshyn, 1988).

**Relation to existing frameworks:** APH draws on language of thought (Fodor), global workspace theory (Baars), predictive processing (Friston), and compositional semantics (Montague). The contribution is treating compositional representation as the *single primitive* from which other cognitive operations derive, grounding it in measurable systematicity, and generating architectural predictions. Whether this synthesis advances beyond existing frameworks or relabels them is a fair question—the papers attempt to show where APH makes different predictions.

**Enabling conditions vs. the criterion:**

- **Enabling conditions** (necessary but not distinctive): temporal stabilization, attentional selection
- **Implementation requirements** (how systems achieve compositionality): token formation, combinatorial syntax
- **The criterion** (what abstraction *is*): compositional representation

Stabilization and attention are required for abstraction but don’t constitute it—many non-abstractive processes require them. What makes abstraction abstractive is compositionality.

**Why compositionality matters:** It enables unbounded representational capacity from finite primitives. This solves combinatorial explosion—you can’t store a lookup table for every possible situation, but you can compose representations of novel situations from known components. Compositionality is what allows finite systems to handle infinite possibility spaces.

**The threshold problem:** If compositionality exists on a spectrum, where does abstraction “begin”? Learned embeddings like word2vec support limited composition (vector arithmetic produces “king - man + woman ≈ queen”), and these are genuine novel combinations with predictable meanings. A candidate distinction: *generative* composition supports unboundedly many novel structures through recursive combination and role-filler independence, while *interpolative* composition operates within a pre-shaped space with fixed operations. But this needs rigorous operationalization—word2vec’s limitation may be the fixed operation set (only arithmetic), not the representations themselves. The threshold remains genuinely unresolved.

-----

## Key Claims

### Compositionality as the Proposed Criterion

Previous versions of this framework proposed four components (stabilization, discretization, binding, structural decoupling). Critical analysis revealed problems: these mix enabling conditions with defining features, assume symbolic representations, and may not be separable. The revised framework proposes a single criterion: **does the system form compositional representations?**

This is a hypothesis, not a stipulation. We’re claiming that compositionality is what matters for intelligence—not defining intelligence as compositionality. The claim is falsifiable: if systems we’d recognize as intelligent lack compositionality, or if compositional systems fail to exhibit what intelligence should produce, the framework is wrong.

**The test:** Can the system generalize to novel combinations of familiar elements? If it understands “John loves Mary,” can it understand “Mary loves John”? If it can represent RED and SQUARE separately, can it combine them into RED SQUARE?

**Empirically supported:** Compositional generalization requires end-to-end compositional structure—factorized input encoding AND compositional output; factorized representations alone prove insufficient. These results warrant replication but provide initial support.

### Embeddedness: Five Necessary Components

What enables self-referential abstraction (Stage 4) isn’t having a body—it’s being **embedded**. But embeddedness is more demanding than simple action-consequence coupling.

**Five components are necessary:**

|Component                         |Definition                      |Why Necessary                            |
|----------------------------------|--------------------------------|-----------------------------------------|
|**Action-consequence contingency**|Outputs affect subsequent inputs|Creates need for self/world decomposition|
|**Feedback closure**              |Consequences return to agent    |Enables learning from consequences       |
|**Temporal persistence**          |Agent continues across time     |Enables accumulation of self-model       |
|**Self-boundary awareness**       |Access to own limits/constraints|Enables modeling where self ends         |
|**Environmental stability**       |Consistent regularities in world|Enables modeling what world contributes  |

Bodies naturally provide all five—they persist, have sensable boundaries (proprioception, interoception), exist in stable physical environments, and their actions have consequences. But embodiment is *instrumental*, not *constitutive*. The relational structure is what matters.

**Why current LLMs face limitations:** They lack *all five* components:

- No action-consequence during training (static corpus)
- No persistence (session ends; no continuity)
- No self-boundary awareness (can’t see token limits, capability constraints)
- No environmental stability (each conversation is different)

This predicts Stage 4 limitations—but current LLMs do show some self-modeling (calibrated confidence, uncertainty estimation). The framework must explain this: either as pattern-matching on human self-reports in training data, or as partial self-modeling that falls short of full Stage 4. This distinction needs sharper empirical criteria.

### Developmental Spectrum

Abstraction capacity develops through stages: pattern extraction → symbol formation → recursive composition → self-referential abstraction. Each stage enables operations impossible at prior stages. Stage progression is sequential in prerequisites—Stage N requires Stage N-1—though development may show parallelism and temporary regression.

The self/world distinction is the **foundational abstraction** from which higher self-modeling cascades: body schema → agency → perspective → mental state attribution → metacognition → Stage 4.

-----

## Papers

|# |Paper                                                                                |Description                                                                                                                           |
|--|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                 |The general framework: abstraction as the fundamental primitive                                                                       |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)          |Single-criterion definition: compositional representation; enabling conditions vs. implementation requirements                        |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)           |Compositionality as distinguishing operation; metrics; architectural conditions                                                       |
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                         |What abstraction is not: distinguishing from input and downstream operations                                                          |
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)         |Why prediction presupposes representational content                                                                                   |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                             |Self-reference and the mathematics of *e*                                                                                             |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)           |Staged development from pattern extraction to self-referential cognition                                                              |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                        |Five components of embeddedness; why it enables Stage 4; the self-modeling cascade                                                    |
|9 |[Self and World](papers/self_world_abstraction.md)                                   |The foundational abstraction                                                                                                          |
|10|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Self-monitoring as computational necessity                                                                                            |
|11|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |Experience as embedded information format (argues the problem is reframed by embeddedness, not that phenomenal experience is illusory)|
|12|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal reasoning and embeddedness                                                                                                   |
|13|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotions as action-formatted self-world information                                                                                   |
|14|[Social Dynamics](papers/social_dynamics.md)                                         |Multi-agent recursive abstraction                                                                                                     |
|15|[Beyond Large Language Models](papers/beyond_llms.md)                                |Architectural implications for AI                                                                                                     |

**Recommended reading order:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15

Papers 1–5 establish the core framework. Papers 6–8 address self-reference and embeddedness. Papers 9–14 extend to consciousness, time, emotion, and social cognition. Paper 15 applies the framework to AI architecture.

-----

## Falsifiable Predictions

**Architecture** *(initial empirical support—replication needed)*

- ✓ Compositional generalization requires factorized input AND compositional output
- ✓ Factorized representations alone insufficient (high decodability, low generalization)
- ✓ Compression ratio threshold exists (~5×)

**Development**

- Stage progression is sequential in prerequisites: no Stage N capacity without prior Stage N-1 (though regression possible)
- Stage-specific tasks should cluster; within-stage correlations exceed across-stage

**LLM-Specific**

- Performance degrades with hierarchical depth in ways human performance does not
- Scaling improves Stage 1–2 more than Stage 3–4
- Self-modeling capacity shows ceiling in non-embedded systems—a strong prediction that could be falsified by sufficient scale. Current models already show non-trivial self-modeling (calibrated uncertainty, knowing what they’re likely wrong about). If scaled models show robust, general self-modeling without embeddedness, the framework needs revision.

**Embeddedness (five-component model)**

- Systems lacking *any* of the five components should show Stage 4 limitations
- Systems with action-consequence coupling but without self-boundary awareness should show partial self/world distinction
- Giving LLMs access to their own token limits and capability constraints should modestly improve self-modeling
- Episodic systems (reset each session) should show less developed self-models than persistent systems with equivalent interaction volume
- Stage 4 without self/world distinction would falsify the framework

-----

## Open Questions

The framework is offered as a research program, not a finished theory. Key unresolved issues:

- **Discovered or stipulated?** Is “intelligence is compositional representation” an empirical claim or a definition? The framework intends it as a hypothesis—a proposed criterion that could be wrong. Evidence against: finding systems we’d call intelligent that lack compositionality, or finding that compositionality fails to predict the outcomes intelligence should predict. But the risk of circularity (defining intelligence as what we measure, measuring what we defined) is real and requires ongoing vigilance.
- **Single criterion vs. components:** The revised framework proposes compositionality as the single criterion, with enabling conditions and implementation requirements separated. Is this decomposition correct? Could alternative framings prove superior?
- **Operationalizing embeddedness:** The five-component model is more precise than “action-consequence contingency” alone, but thresholds remain unclear. How much persistence, how much self-boundary awareness, how much environmental stability?
- **Compositionality thresholds:** Generative vs. interpolative composition is proposed as a candidate boundary, but needs rigorous operationalization. Word2vec shows that statistical spaces can support some composition—the framework needs sharper criteria for what’s missing.
- **The Hard Problem:** The framework argues that embeddedness reframes the explanatory gap, but a functional account of self-modeling doesn’t obviously address what philosophers mean by phenomenal consciousness—why modeling *feels like something*. The honest question: does this advance beyond existing functionalism?
- **Replication:** Core empirical results come from limited experimental contexts and need independent replication.

-----

## Empirical Research Program

**Architecture & Compositionality:** [emergent-factorization](https://github.com/HillaryDanan/emergent-factorization), [compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction)

**Temporal Reasoning:** [temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm), [curved-cognition](https://github.com/HillaryDanan/curved-cognition), [embodied-cognition](https://github.com/HillaryDanan/embodied-cognition)

**Self/World & Consciousness:** [BIND](https://github.com/HillaryDanan/BIND), [comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms), [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction)

**Developmental Stages:** [reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum), [concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)

**Social & Multi-Agent:** [game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite), [reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence)

-----

## Status

These are **working theoretical papers**—hypotheses with testable predictions, not established results. The framework is offered for discussion, critique, and empirical testing.

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

-----

*“You cannot model yourself without knowing where you end.”*

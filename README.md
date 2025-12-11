# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: intelligence is the capacity to transform attended information into compositional symbols. A reflex arc attends; it does not abstract. Intelligence begins where composition begins.

-----

## The Core Idea

Abstraction is the operation that converts selected information into symbols that can be *combined to form new symbols*. This is what distinguishes a sensor from a mind.

**Four components define abstraction:**

1. **Stabilization** — representation persists beyond the stimulus
1. **Discretization** — continuous input becomes discrete symbols
1. **Binding** — features cohere into units
1. **Structural decoupling** — roles separate from fillers, enabling recombination

**The test is compositionality.** Systems that genuinely abstract can combine known primitives in novel ways. Systems that merely compress typically cannot—though the boundary is sharper in principle than in practice. (Learned embeddings like word2vec occupy an intermediate zone: they compress *and* support limited composition. Whether this constitutes “real” abstraction or composition-preserving compression is a live question.) A JPEG doesn’t compose with another JPEG to generate meaningful novel structure. Concepts do. This criterion is measurable and—crucially—admits degrees.

-----

## Key Contributions

### Compositionality as the Distinguishing Feature

Compression reduces information; abstraction generates combinatorial capacity. The framework provides metrics (compositional generalization rate, systematicity, transfer efficiency) and identifies architectural conditions under which compression yields abstraction.

**Empirically supported:** Compositional generalization requires end-to-end compositional structure—factorized input encoding AND compositional output (interaction effect d = 11.95; factorized representations alone insufficient). This result warrants replication and scrutiny of experimental design, but provides initial support for the architectural claims.

**Important caveat:** Compositionality exists on a spectrum. LLMs show *some* compositional generalization—the question is not binary presence/absence but degree and systematicity. The framework proposes that this partial compositionality reflects partial instantiation of the four components, particularly structural decoupling. This interpretation requires further testing.

### Embeddedness, Not Embodiment

What enables self-referential abstraction isn’t having a body—it’s being embedded in an environment with action-consequence contingency. Embeddedness creates computational pressure for the self/world distinction, the foundational abstraction from which self-modeling cascades. This reframes debates about “embodied AI” in tractable, testable terms.

**Open question:** How “embedded” gets operationalized matters enormously. One could argue that language itself constitutes a kind of environment with action-consequence structure (say something, get a response). The framework requires precise criteria distinguishing embedded from non-embedded training—this is an active area of development, not a settled question.

### Developmental Spectrum

Abstraction capacity develops through stages: pattern extraction → symbol formation → recursive composition → self-referential abstraction. Each stage enables operations impossible at prior stages. Stage progression is sequential in prerequisites—Stage N capacity requires prior Stage N-1 capacity—though development may show parallelism and temporary regression. Current LLMs show substantial capacity at early stages with systematic limitations at later stages—not because they lack bodies, but because they lack embedded interaction forcing self/world differentiation.

-----

## Papers

|# |Paper                                                                                |Description                                                                                                                           |
|--|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                 |The general framework: abstraction as the fundamental primitive                                                                       |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)          |Precise operational definition: four components; distinction from attention and compression                                           |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)           |Compositionality as distinguishing operation; metrics; architectural conditions                                                       |
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                         |What abstraction is not: distinguishing from input and downstream operations                                                          |
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)         |Why prediction presupposes representational content                                                                                   |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                             |Self-reference and the mathematics of *e*                                                                                             |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)           |Staged development from pattern extraction to self-referential cognition                                                              |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                        |Why embeddedness enables Stage 4; the self-modeling cascade                                                                           |
|9 |[Self and World](papers/self_world_abstraction.md)                                   |The foundational abstraction                                                                                                          |
|10|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Self-monitoring as computational necessity                                                                                            |
|11|[The Hard Problem Dissolved](papers/hard_problem_dissolution.md)                     |Experience as embedded information format (argues the problem is reframed by embeddedness, not that phenomenal experience is illusory)|
|12|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal reasoning and embeddedness                                                                                                   |
|13|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotions as action-formatted self-world information                                                                                   |
|14|[Social Dynamics](papers/social_dynamics.md)                                         |Multi-agent recursive abstraction                                                                                                     |
|15|[Beyond Large Language Models](papers/beyond_llms.md)                                |Architectural implications for AI                                                                                                     |

**Recommended reading order:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15

Papers 1–5 establish the core framework. Papers 6–8 address self-reference and embeddedness. Papers 9–14 extend to consciousness, time, emotion, and social cognition. Paper 15 applies the framework to AI architecture.

-----

## Falsifiable Predictions

The framework generates testable predictions. Selected examples:

**Architecture** *(initial empirical support—replication needed)*

- ✓ Compositional generalization requires factorized input AND compositional output (d = 11.95)
- ✓ Factorized representations alone insufficient (93% decodability, 0% generalization)
- ✓ Compression ratio threshold exists (~5×)

**Development**

- Stage progression is sequential in prerequisites: no Stage N capacity without prior Stage N-1 (though regression possible)
- Stage-specific tasks should cluster; within-stage correlations exceed across-stage

**LLM-Specific**

- Performance degrades with hierarchical depth in ways human performance does not
- Scaling improves Stage 1–2 more than Stage 3–4
- Self-modeling capacity shows ceiling in non-embedded systems—a strong prediction contingent on operationalizing “embedded,” and one that could be falsified by sufficient scale

**Embeddedness**

- Action-consequence contingency is necessary for self/world distinction
- Embedded training should improve self-modeling capacity vs. non-embedded at equivalent compute
- Stage 4 without self/world distinction would falsify the framework

See individual papers for complete predictions and falsification criteria.

-----

## Open Questions

The framework is offered as a research program, not a finished theory. Key unresolved issues:

- **Operationalizing embeddedness:** What counts as sufficient action-consequence contingency? Does conversational interaction qualify? What’s the threshold?
- **Compositionality thresholds:** At what point does partial compositionality become “genuine” abstraction? Is there a phase transition or continuous graduation? Where do learned embeddings (which compress *and* compose to a degree) fall?
- **The Hard Problem:** The framework argues that embeddedness dissolves the explanatory gap, but this may reframe rather than resolve what philosophers mean by phenomenal consciousness. The claim requires engagement with existing positions.
- **Replication:** Core empirical results (d = 11.95 for end-to-end compositionality) come from limited experimental contexts and need independent replication across tasks and architectures.

-----

## Empirical Research Program

The theoretical framework is accompanied by empirical repositories testing specific predictions:

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

*“A reflex arc attends but does not abstract. Intelligence begins where composition begins.”*

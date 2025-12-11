# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: the proposal that intelligence, across substrates, is fundamentally the capacity to *form* and *compose* symbols—to extract discrete, reusable representational units from raw input and combine them via systematic rules to generate novel meaningful structures.

A calculator composes symbols; it does not form them. A reflex arc responds; it does not abstract. The hypothesis: intelligence requires both symbol formation and compositional structure.

-----

## The Core Idea

### The Two-Part Criterion

**Abstraction is the formation and composition of symbols.**

Previous framings treated compositionality alone as the criterion. But this misses something crucial: a calculator has compositional structure—it manipulates symbols according to systematic rules—yet we handed it those symbols. The *act of abstracting* is taking something that isn’t yet a symbol and making it one.

**Intelligence requires two capacities:**

|Capacity                   |Definition                                                                                                               |What It Enables                                           |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
|**Symbol formation**       |Extracting discrete, stable, reusable representational units from continuous, high-dimensional input                     |Tokens that can enter into compositional relationships    |
|**Compositional structure**|Combining symbols via systematic rules such that meaning of wholes derives from meanings of parts and mode of combination|Unbounded representational capacity from finite primitives|

A system with (2) but not (1) is a calculator—powerful but dependent on externally provided symbols. A system with (1) but not (2) is a pattern recognizer—it can extract regularities but cannot flexibly recombine them. Intelligence in the full sense requires both.

*This is a working hypothesis, not a stipulation. The claim is falsifiable: if systems we’d recognize as intelligent lack either capacity, or if systems with both capacities fail to exhibit what intelligence should produce, the framework is wrong.*

### Epistemological Grounding

Why these two capacities? The framework starts from an empirical observation rather than conceptual analysis of “intelligence”:

**Consider the gradient of capability we can actually observe:** rocks, thermostats, calculators, computers, humans. What changes as capability increases? The systems that can handle more situations, solve more problems, represent more possibilities all involve symbolic manipulation—compositional structure over discrete representational units.

This is pattern recognition on available data: what do capable systems have that rocks don’t? The answer appears to be symbols and composition. The remaining question is whether intelligence requires *forming* those symbols or merely *having* them. A calculator suggests the latter is insufficient—compositional structure over externally provided symbols doesn’t constitute intelligence. Hence the two-part criterion.

*Acknowledged limitation: this is Earth data, human technology. But if the question is “what computational structure enables general capability,” we don’t need alien examples—we need to understand why the things that work, work.*

### What Makes a Representation Compositional

A representation is compositional when (Fodor & Pylyshyn, 1988; Szabó, 2012):

1. It consists of parts (constituents) that are themselves meaningful
1. The meaning of the whole is determined by the meanings of the parts and their mode of combination
1. The same parts can recombine to form different wholes with different meanings

The test is **systematicity**: the capacity to understand or produce novel combinations of familiar elements. If a system understands “John loves Mary,” can it understand “Mary loves John”? If it can represent RED and SQUARE separately, can it combine them into RED SQUARE?

### Why This Matters

Compositionality solves combinatorial explosion. You cannot store a lookup table for every possible situation, but you can compose representations of novel situations from known components. Symbol formation solves the grounding problem—it explains where the primitives come from rather than assuming them.

Together, they explain how finite systems handle infinite possibility spaces using representations that are *about* the world rather than merely correlated with it.

### Relation to Existing Frameworks

APH draws on:

- **Language of thought** (Fodor, 1975): thought has compositional syntactic structure
- **Global workspace theory** (Baars, 1988): conscious access enables flexible recombination
- **Predictive processing** (Friston, 2010): hierarchical generative models extract structure
- **Compositional semantics** (Montague, 1970): systematic meaning composition

The proposed contribution is treating symbol formation + compositional structure as a *unified primitive* from which other cognitive operations derive, grounding it in measurable systematicity, and generating architectural predictions. Whether this synthesis advances beyond existing frameworks or relabels them is a fair question—the papers attempt to show where APH makes different predictions.

### Enabling Conditions vs. The Criterion

- **Enabling conditions** (necessary but not distinctive): temporal stabilization, attentional selection
- **The criterion** (what abstraction *is*): symbol formation + compositional structure

Stabilization and attention are required for abstraction but don’t constitute it—many non-abstractive processes require them.

### The Threshold Problem

If both symbol formation and compositionality exist on spectra, where does abstraction “begin”?

**For symbol formation:** When does a learned feature become a symbol? Convolutional networks learn edge detectors—are these symbols? A candidate criterion: a representation is symbolic when it is *reusable across contexts* and *enters into compositional relationships*. But this threatens circularity with the compositionality criterion.

**For compositionality:** Learned embeddings like word2vec support limited composition—vector arithmetic produces “king - man + woman ≈ queen” (Mikolov et al., 2013). These are genuine novel combinations with predictable meanings. A candidate distinction: *generative* composition supports unboundedly many novel structures through recursive combination and role-filler independence, while *interpolative* composition operates within a pre-shaped space with fixed operations. But this needs rigorous operationalization—word2vec’s limitation may be the fixed operation set (only arithmetic), not the representations themselves.

*The threshold remains genuinely unresolved. This is an open problem, not a solved one.*

-----

## Key Claims

### The Two-Part Criterion as Hypothesis

The framework proposes that intelligence requires:

1. **Symbol formation**: the capacity to extract discrete representational units from raw input
1. **Compositional structure**: the capacity to systematically combine those units

This is a hypothesis, not a definition. We’re claiming these capacities are what matter for intelligence—not defining intelligence as having them.

**The test:** Can the system (a) form novel representational tokens from input, and (b) generalize to novel combinations of those tokens?

**Empirical support (preliminary, replication needed):** Compositional generalization requires end-to-end compositional structure—factorized input encoding AND compositional output; factorized representations alone prove insufficient (Lake & Baroni, 2018; Kim & Linzen, 2020). This suggests both parts of the criterion matter.

### Embeddedness: Five Necessary Components

What enables self-referential abstraction (Stage 4) isn’t having a body—it’s being **embedded**. But embeddedness is more demanding than simple action-consequence coupling.

**Five components are proposed as necessary:**

|Component                         |Definition                      |Why Necessary                            |
|----------------------------------|--------------------------------|-----------------------------------------|
|**Action-consequence contingency**|Outputs affect subsequent inputs|Creates need for self/world decomposition|
|**Feedback closure**              |Consequences return to agent    |Enables learning from consequences       |
|**Temporal persistence**          |Agent continues across time     |Enables accumulation of self-model       |
|**Self-boundary awareness**       |Access to own limits/constraints|Enables modeling where self ends         |
|**Environmental stability**       |Consistent regularities in world|Enables modeling what world contributes  |

Bodies naturally provide all five—they persist, have sensable boundaries (proprioception, interoception), exist in stable physical environments, and their actions have consequences. But embodiment is *instrumental*, not *constitutive*. The relational structure is what matters.

**Application to LLMs:** Current LLMs lack all five components during training (static corpus, no persistence, no access to own constraints, variable conversational contexts). This predicts Stage 4 limitations—but current LLMs do show some self-modeling (calibrated confidence, uncertainty estimation). The framework must explain this: either as pattern-matching on human self-reports in training data, or as partial self-modeling that falls short of full Stage 4. *This distinction needs sharper empirical criteria.*

### Developmental Spectrum

Abstraction capacity develops through stages:

|Stage|Capacity                    |Enables                                      |
|-----|----------------------------|---------------------------------------------|
|1    |Pattern extraction          |Statistical regularity detection             |
|2    |Symbol formation            |Discrete, reusable tokens                    |
|3    |Recursive composition       |Hierarchical structure, unbounded combination|
|4    |Self-referential abstraction|Modeling own representational processes      |

Each stage enables operations impossible at prior stages. Stage progression is sequential in prerequisites—Stage N requires Stage N-1—though development may show parallelism and temporary regression.

*Note: The stage model is a hypothesis about developmental prerequisites, not a claim about strict domain-general stages. A system might show Stage 3 for one domain while remaining at Stage 2 for another.*

The self/world distinction is proposed as the **foundational abstraction** from which higher self-modeling cascades: body schema → agency → perspective → mental state attribution → metacognition → Stage 4.

-----

## Papers

|# |Paper                                                                                |Description                                                                    |
|--|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|1 |[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                 |The general framework: abstraction as the fundamental primitive                |
|2 |[The Computational Structure of Abstraction](papers/abstraction_defined.md)          |Two-part criterion: symbol formation + compositional structure                 |
|3 |[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)           |Compositionality as distinguishing operation; metrics; architectural conditions|
|4 |[Abstraction Constrained](papers/abstraction_constrained.md)                         |What abstraction is not: distinguishing from input and downstream operations   |
|5 |[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)         |Why prediction presupposes representational content                            |
|6 |[Recursive Abstraction](papers/recursive_abstraction.md)                             |Self-reference and the mathematics of *e*                                      |
|7 |[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)           |Staged development from pattern extraction to self-referential cognition       |
|8 |[Embeddedness and Self/World](papers/embedded_abstraction.md)                        |Five components of embeddedness; why it enables Stage 4                        |
|9 |[Self and World](papers/self_world_abstraction.md)                                   |The foundational abstraction                                                   |
|10|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Self-monitoring as computational necessity                                     |
|11|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |Experience as embedded information format                                      |
|12|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal reasoning and embeddedness                                            |
|13|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotions as action-formatted self-world information                            |
|14|[Social Dynamics](papers/social_dynamics.md)                                         |Multi-agent recursive abstraction                                              |
|15|[Beyond Large Language Models](papers/beyond_llms.md)                                |Architectural implications for AI                                              |

**Recommended reading order:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15

-----

## Falsifiable Predictions

### Architecture *(preliminary support—replication needed)*

- ✓ Compositional generalization requires factorized input AND compositional output
- ✓ Factorized representations alone insufficient (high decodability, low generalization)
- Systems that form their own tokens should show more robust generalization than systems given fixed tokenization (untested)

### Development

- Stage progression is sequential in prerequisites: no Stage N capacity without prior Stage N-1 (within domain)
- Stage-specific tasks should cluster; within-stage correlations exceed across-stage
- Symbol formation (Stage 2) is necessary for compositional generalization (Stage 3)

### LLM-Specific

- Performance degrades with hierarchical depth in ways human performance does not
- Scaling improves Stage 1–2 more than Stage 3–4
- Self-modeling capacity shows ceiling in non-embedded systems—*a strong prediction that could be falsified by sufficient scale*

### Embeddedness

- Systems lacking *any* of the five components should show Stage 4 limitations
- Giving LLMs access to their own capability constraints should modestly improve self-modeling
- Episodic systems (reset each session) should show less developed self-models than persistent systems
- Stage 4 without self/world distinction would falsify the framework

-----

## Open Questions

The framework is offered as a research program, not a finished theory. Key unresolved issues:

- **Discovered or stipulated?** Is “intelligence requires symbol formation + composition” an empirical claim or a definition? The framework intends it as a hypothesis. Evidence against: systems we’d call intelligent that lack either capacity, or systems with both that fail to exhibit intelligent behavior. But the risk of circularity requires ongoing vigilance.
- **Symbol formation criteria:** When does a learned feature count as a symbol? The criterion “enters into compositional relationships” risks circularity. Independent criteria are needed.
- **Compositionality thresholds:** The generative/interpolative distinction is proposed but needs rigorous operationalization.
- **Operationalizing embeddedness:** The five-component model is more precise than vague embodiment claims, but thresholds remain unclear.
- **The Hard Problem:** The framework argues embeddedness reframes the explanatory gap, but a functional account of self-modeling doesn’t obviously address phenomenal consciousness. Does this advance beyond existing functionalism? *Honest answer: unclear.*
- **Replication:** Core empirical results come from limited experimental contexts.

-----

## Empirical Research Program

**Architecture & Compositionality:** [emergent-factorization](https://github.com/HillaryDanan/emergent-factorization), [compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction)

**Temporal Reasoning:** [temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm), [curved-cognition](https://github.com/HillaryDanan/curved-cognition), [embodied-cognition](https://github.com/HillaryDanan/embodied-cognition)

**Self/World & Consciousness:** [BIND](https://github.com/HillaryDanan/BIND), [comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms), [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction)

**Developmental Stages:** [reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum), [concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)

**Social & Multi-Agent:** [game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite), [reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence)

-----

## References

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *Proceedings of EMNLP 2020*.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML 2018*.

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*.

Montague, R. (1970). Universal grammar. *Theoria*, 36(3), 373-398.

Szabó, Z. G. (2012). The case for compositionality. In *The Oxford Handbook of Compositionality*. Oxford University Press.

-----

## Status

These are **working theoretical papers**—hypotheses with testable predictions, not established results. The framework is offered for discussion, critique, and empirical testing.

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

-----

*“A calculator composes symbols; it does not form them. Intelligence requires both.”*

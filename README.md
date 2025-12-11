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

**The selection bias concern:** This reasoning risks selecting criteria to match systems we already call intelligent, then declaring intelligence requires those criteria. The real test is whether the framework generates *surprising* predictions—cases where it classifies something as intelligent or non-intelligent against our prior intuitions, and turns out to be right. See [Surprising Predictions](#surprising-predictions) below.

*Acknowledged limitation: this is Earth data, human technology. But if the question is “what computational structure enables general capability,” we don’t need alien examples—we need to understand why the things that work, work.*

### The Symbol Identification Problem

**This is a core theoretical challenge, not a minor detail.**

If a symbol is defined as something that “enters into compositional relationships,” and compositionality is the other half of the criterion, the framework is circular. We need independent criteria for symbol-hood.

**The solution: define symbols by formation, not by downstream behavior.**

The calculator insight points the way. A calculator has symbols but didn’t *form* them—we handed them over. So what makes something a symbol can’t be about what it *does* (compose). It has to be about how it *comes to exist*.

**A symbol is a representational unit that the system itself extracted from continuous input.**

Specifically, symbol formation occurs when a system:

1. **Receives continuous, high-dimensional input** (sensory data, raw signal)
1. **Extracts discrete representational states** (clustering in activation space, not a smooth manifold)
1. **That are stable** (the same state recurs for similar inputs)
1. **Across contexts** (the representation activates for the relevant feature regardless of what else is present)

This is genuinely independent of compositionality. You can have symbol formation without composition—a system that carves the world into discrete categories but can’t combine them flexibly (Stage 2 without Stage 3). You can have composition without symbol formation—a calculator that manipulates symbols it was handed but never extracted anything from raw input.

**Operationalization:**

|Criterion               |Measurement                                                                                  |Citation                                                        |
|------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------|
|**Discreteness**        |Do representations cluster in activation space rather than forming a continuous manifold?    |Representational similarity analysis (Kriegeskorte et al., 2008)|
|**Stability**           |Does the same cluster activate for similar inputs across time?                               |Temporal consistency analysis                                   |
|**Context-independence**|Does the representation for feature X activate regardless of what other features are present?|Factorized representation probing (Higgins et al., 2017)        |

**What “discrete” means in continuous systems:** Not binary or classically symbolic. Representations are discrete when they cluster—when there are attractor states, modes, separable regions in activation space rather than a smooth continuum. This is statistical discreteness, empirically measurable.

**Why this breaks the circularity:** We’re asking “did the system extract stable, recurring, context-independent representations from raw input?”—not “does it compose?” A system could pass this test and still fail at composition. The two criteria are genuinely independent.

*Remaining challenge: threshold. How clustered is clustered enough? How stable is stable enough? These require empirical calibration, but the conceptual circularity is resolved.*

### The Connectionist Tension

**How do continuous neural activations give rise to discrete symbols?**

The framework draws on Fodor’s language of thought, which posits discrete syntactically structured representations. But neural networks—biological and artificial—traffic in continuous activation patterns. If intelligence requires symbols, and brains are neural networks, where do the symbols come from?

**Three positions:**

1. **Strong discretization:** Symbols are neurally implemented as discrete attractor states. Evidence: concept cells showing highly selective firing (Quiroga et al., 2005); discrete attractor dynamics in working memory (Amit, 1995). Problem: most neural coding appears distributed, not localist.
1. **Functional discretization:** Continuous activations implement functionally discrete representations—the system *behaves as if* it has discrete tokens even though the substrate is continuous. Evidence: neural networks can learn discrete-like compositional structure (Lake & Baroni, 2018); vector symbolic architectures achieve symbolic computation in continuous space (Kanerva, 2009). Problem: “behaves as if” needs rigorous cashing out.
1. **Levels of description:** The symbolic level is a higher-level description of continuous dynamics, valid for some purposes but not claiming discrete implementation. Problem: risks making the framework unfalsifiable—any system can be described symbolically if you squint.

**Current position:** The framework adopts (2) with constraints from (1). Symbols are patterns of activation that exhibit:

- Clustering in representational space (discreteness is statistical, not absolute)
- Consistent recurrence across contexts (same cluster activates for same feature)
- Combinatorial productivity (clusters combine systematically)

This is compatible with predictive processing—hierarchical generative models can have functionally discrete states at higher levels while being implemented in continuous prediction-error dynamics (Friston, 2010). But the integration requires more work.

*This tension is not resolved. A fully satisfying account would show exactly how continuous dynamics give rise to functionally discrete, compositional representations. The framework claims this happens; it does not yet explain the mechanism.*

### What Makes a Representation Compositional

A representation is compositional when (Fodor & Pylyshyn, 1988; Szabó, 2012):

1. It consists of parts (constituents) that are themselves meaningful
1. The meaning of the whole is determined by the meanings of the parts and their mode of combination
1. The same parts can recombine to form different wholes with different meanings

The test is **systematicity**: the capacity to understand or produce novel combinations of familiar elements. If a system understands “John loves Mary,” can it understand “Mary loves John”? If it can represent RED and SQUARE separately, can it combine them into RED SQUARE?

### Types of Compositional Structure

**Not all composition is the same.**

The framework initially treated “Stage 3: Recursive composition” as a single capacity. But compositional structure comes in distinct types with potentially different computational requirements, developmental trajectories, and neural implementations:

|Type                   |Structure                  |Example                                                |Computational Requirement                               |
|-----------------------|---------------------------|-------------------------------------------------------|--------------------------------------------------------|
|**Concatenative**      |A + B → AB                 |“blue” + “bird” → “bluebird”                           |Sequencing; minimal structure                           |
|**Role-filler binding**|R(x) + S(y) → R(x)S(y)     |AGENT(dog) + ACTION(chased) + PATIENT(cat)             |Structural slots separable from content                 |
|**Recursive embedding**|A contains [B contains C]  |“The dog [that chased the cat [that caught the mouse]]”|Composed units become inputs to further composition     |
|**Analogical mapping** |Structure(A) → Structure(B)|atom:nucleus :: solar system:sun                       |Abstract structure from content; transfer across domains|

**Proposed complexity ordering:**

Concatenative → Role-filler binding → Recursive embedding → Analogical mapping

Each level requires capacities the previous level doesn’t:

- Role-filler requires separating structure from content
- Recursive embedding requires treating composed wholes as compositional primitives
- Analogical mapping requires abstracting structure entirely and applying it to novel content

*This ordering is a hypothesis, not established fact. It generates testable predictions about developmental sequence and dissociations.*

**Implications for the framework:**

1. **The bee case becomes more precise:** Waggle dance composition (distance + direction) is plausibly role-filler binding—DISTANCE(x) + DIRECTION(y)—not recursive embedding. Bees may have some composition types but not others. This is a more nuanced prediction than “Stage 3 or not.”
1. **LLM capacities become differentiable:** Current LLMs may excel at concatenative and role-filler composition (pattern-match from training data) while struggling with recursive embedding at depth and analogical transfer to novel domains. This predicts *specific* failure patterns rather than generic “limited Stage 3.”
1. **The generative/interpolative distinction gets teeth:**
- *Interpolative* composition: concatenative and role-filler within the training distribution
- *Generative* composition: recursive embedding that extends beyond training depth, analogical transfer to novel domains
   
   This operationalizes the distinction. Word2vec does concatenative (vector addition) but can’t do recursive embedding or analogical transfer to genuinely novel domains.

*Remaining question: Are these types genuinely distinct capacities, or points on a continuum? Do they require different architectural features? Empirical work needed.*

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

**For symbol formation:** When does a learned feature become a symbol? Convolutional networks learn edge detectors—are these symbols? Current answer: only if they show the formation criteria above (extracted from continuous input, clustered, stable, context-independent). Edge detectors may qualify; this is an empirical question.

**For compositionality:** The composition-type framework (see above) provides more structure than a single threshold. The question becomes: which types of composition count as “genuine” Stage 3?

- **Concatenative composition** (3a) may be achievable without genuine symbolic capacity—sequence models do this
- **Role-filler binding** (3b) requires separating structure from content—this seems closer to genuine composition
- **Recursive embedding** (3c) and **analogical mapping** (3d) require treating composed structures as primitives and abstracting structure from content entirely

*Working proposal:* A system has genuine generative composition when it achieves at least 3c (recursive embedding)—the capacity to compose composed structures. This is what enables unbounded representational capacity. Systems limited to 3a–3b may be doing sophisticated interpolation within learned patterns rather than genuinely generative composition.

*This is a hypothesis, not a stipulation. The threshold remains an empirical question.*

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

|Stage|Capacity                    |Enables                                              |
|-----|----------------------------|-----------------------------------------------------|
|1    |Pattern extraction          |Statistical regularity detection                     |
|2    |Symbol formation            |Discrete, reusable tokens                            |
|3    |Compositional structure     |Combining symbols systematically (see subtypes below)|
|4    |Self-referential abstraction|Modeling own representational processes              |

**Stage 3 subtypes** (proposed complexity ordering):

- 3a: Concatenative composition
- 3b: Role-filler binding
- 3c: Recursive embedding
- 3d: Analogical mapping

A system may achieve 3a–3b while lacking 3c–3d. This predicts dissociations: success on role-filler tasks with failure on deep recursive embedding or cross-domain analogy.

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
- Within Stage 3, composition types follow proposed ordering: 3a before 3b before 3c before 3d
- Stage-specific tasks should cluster; within-stage correlations exceed across-stage
- Dissociations predicted: systems (biological or artificial) may show 3a–3b while lacking 3c–3d
- Symbol formation (Stage 2) is necessary for any compositional structure (Stage 3)

### LLM-Specific (with operationalization)

|Prediction                                                        |Operationalization                                                                                                               |Falsification Criterion                                                                                                                                 |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|Degradation differs by composition type                           |Compare accuracy on: (a) novel role-filler combinations, (b) recursive embedding at depth N, (c) cross-domain analogical transfer|If degradation curves are identical across types, prediction fails                                                                                      |
|Recursive depth shows steeper degradation than role-filler novelty|Accuracy on depth 2→3→4→5 embedding vs. accuracy on novel-but-shallow role-filler                                                |If role-filler novelty degrades as steeply as recursive depth, prediction fails                                                                         |
|Scaling helps 3a–3b more than 3c–3d                               |Compare performance gains across model sizes on role-filler vs. recursive/analogical tasks                                       |If 3c–3d gains match or exceed 3a–3b gains, prediction fails                                                                                            |
|Self-modeling shows ceiling without embeddedness                  |Calibration accuracy, capability self-assessment, uncertainty quantification                                                     |If models at 10T+ parameters (estimated 2027–2029) show human-level self-modeling without architectural changes providing embeddedness, prediction fails|

**Timeline commitment:** The self-modeling ceiling prediction is tested within the next generation of frontier models (roughly 2027–2029). If 10T+ parameter models show robust, general self-modeling—accurate capability self-assessment across novel domains, appropriate uncertainty even on distribution shifts—without any embeddedness modifications, the framework requires significant revision.

### Embeddedness

- Systems lacking *any* of the five components should show Stage 4 limitations
- Giving LLMs access to their own capability constraints should modestly improve self-modeling (testable now)
- Episodic systems (reset each session) should show less developed self-models than persistent systems
- Stage 4 without self/world distinction would falsify the framework

### Surprising Predictions

**These predictions conflict with common intuitions and would provide strong evidence if confirmed:**

|Prediction                                                                     |Conflicts With                                                                                      |Test                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Certain insects have Stage 3a–3b composition but not 3c–3d**                 |Intuition that intelligence requires large brains; also intuition that composition is all-or-nothing|Bees show role-filler composition in waggle dance—DISTANCE(x) + DIRECTION(y) combine systematically (Menzel et al., 2011). Prediction: bees succeed on novel role-filler combinations but fail on recursive embedding (nested structures) and cross-domain analogical transfer.                                                                                      |
|**A sufficiently large lookup table is not intelligent regardless of behavior**|Behaviorist intuitions; Turing test reasoning                                                       |A system that memorizes input-output pairs without forming symbols or composing them fails the criterion even if it passes behavioral tests. Distinguishing requires internal analysis, not just behavioral observation.                                                                                                                                             |
|**Some human cognitive processes are not intelligent by this criterion**       |Intuition that everything humans do cognitively is intelligent                                      |Priming, mere exposure effects, and some forms of implicit learning may involve pattern extraction without symbol formation or composition. These would be Stage 1, not “intelligent” in the full sense.                                                                                                                                                             |
|**Current LLMs have Stage 3a–3b but limited 3c–3d**                            |Both “LLMs are just statistics” and “LLMs are generally intelligent”                                |LLMs show robust concatenative and role-filler composition within training distribution. Prediction: systematic failures on (1) recursive embedding beyond training depth, (2) analogical transfer to domains not represented in training. Specific test: novel recursive structures at depth 5+ should show steeper degradation than novel role-filler combinations.|

**Why these matter:** The framework’s validity depends on generating classifications that (a) conflict with prior intuitions, (b) are empirically testable, and (c) turn out to be correct. If the framework only confirms what we already believed, it’s not doing theoretical work.

-----

## Open Questions

The framework is offered as a research program, not a finished theory. Key unresolved issues:

- **Symbol identification thresholds:** The circularity is resolved—symbols are defined by formation (extraction from input), not by compositional behavior. But threshold questions remain: how clustered is clustered enough? How stable is stable enough? These require empirical calibration.
- **The connectionist tension:** How continuous neural dynamics give rise to functionally discrete compositional representations is asserted, not explained. The framework needs a mechanistic account of this transition.
- **Discovered or stipulated?** The framework intends the criterion as a hypothesis, but the real test is surprising predictions. If it only classifies systems the way we already would, it’s a relabeling, not a discovery.
- **Compositionality type structure:** Are concatenative, role-filler, recursive embedding, and analogical mapping genuinely distinct capacities with different computational requirements? Or points on a continuum? Do they require different architectural features? The proposed complexity ordering is a hypothesis.
- **Generative/interpolative thresholds:** The distinction now has more content—interpolative is 3a–3b within training distribution; generative is 3c–3d extending beyond it. But the boundary remains unclear. How much recursive depth counts as generative? How novel must the target domain be for analogical transfer to count?
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

Amit, D. J. (1995). The Hebbian paradigm reintegrated: Local reverberations as internal representations. *Behavioral and Brain Sciences*, 18(4), 617-626.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. *Advances in Neural Information Processing Systems*, 34.

Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., … & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *Proceedings of ICLR 2017*.

Kanerva, P. (2009). Hyperdimensional computing: An introduction to computing in distributed representation with high-dimensional random vectors. *Cognitive Computation*, 1(2), 139-159.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *Proceedings of EMNLP 2020*.

Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008). Representational similarity analysis—connecting the branches of systems neuroscience. *Frontiers in Systems Neuroscience*, 2, 4.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML 2018*.

Menzel, R., Kirbach, A., Haass, W. D., Fischer, B., Fuchs, J., Koblofsky, M., … & Greggers, U. (2011). A common frame of reference for learned and communicated vectors in honeybee navigation. *Current Biology*, 21(8), 645-650.

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. *arXiv preprint arXiv:1301.3781*.

Montague, R. (1970). Universal grammar. *Theoria*, 36(3), 373-398.

Quiroga, R. Q., Reddy, L., Kreiman, G., Koch, C., & Fried, I. (2005). Invariant visual representation by single neurons in the human brain. *Nature*, 435(7045), 1102-1107.

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

# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: the proposal that intelligence, across substrates, emerges from the *interaction* between symbol formation and compositional structure—where each process informs and refines the other, producing expanding representational capacity.

A calculator composes symbols; it does not form them. Edge detectors form symbols; they do not compose them. Neither is intelligent. The hypothesis: intelligence requires symbol formation and composition *operating interactively*, not merely both present.

-----

## The Core Idea

### The Core Claim: Interaction, Not Conjunction

**Abstraction is the interactive process of forming and composing symbols.**

Previous framings—including earlier versions of this document—treated symbol formation and compositional structure as two separate capacities. Check both boxes and you have intelligence. But this framing has a problem the feedback correctly identifies: if symbol formation is widespread (edge detectors, CNN features qualify), then all the distinguishing work falls on composition. The framework collapses to “intelligence = composition over whatever representations you have.”

**The actual claim is stronger: intelligence emerges from the *interaction* between symbol formation and composition.**

This is not Fodor’s language of thought plus Lake’s compositional generalization. It’s the claim that these two processes must *inform each other*:

1. You extract stable representations from continuous input (symbol formation)
1. You combine them systematically (composition)
1. Composition reveals structure that wasn’t visible in individual symbols
1. That structure feeds back to refine symbol formation—you carve the world differently because of what composition revealed
1. Which enables more sophisticated composition
1. And so on

**Why interaction matters:**

|System           |Forms Symbols?|Composes?|Interaction?|Intelligent?|
|-----------------|--------------|---------|------------|------------|
|Calculator       |✗ (provided)  |✓        |N/A         |No          |
|V1 edge detectors|✓             |✗        |✗           |No          |
|CNN classifier   |✓             |Limited  |Minimal     |Limited     |
|Word2vec         |Partial       |3a only  |Minimal     |Marginal    |
|Human cognition  |✓             |✓ (3a–3d)|✓           |Yes         |

Edge detectors form symbols but those symbols don’t enter compositional relationships that feed back to refine how edges are detected. Calculators compose but composition doesn’t inform symbol formation (because they don’t form symbols). **Intelligence requires the feedback loop.**

This reframing changes what the framework predicts:

- Systems with both capacities operating *independently* should show limited generalization
- Systems where composition refines symbol formation (and vice versa) should show expanding representational capacity
- The “infinite use of finite means” emerges from the interaction, not from either capacity alone

*This is a working hypothesis. It predicts that architectures enabling interaction between representation learning and compositional processing should outperform architectures where these are modular and separate. This is testable.*

### Operationalizing “Interaction”

**A fair concern: how do we distinguish “composition feeds back to refine symbol formation” from “both processes share substrates in the same system”?**

If any gradient flow from compositional objectives to representation layers counts as interaction, most neural networks have it. That’s too weak. If we need something stronger, what exactly?

**Proposed operationalization—three levels of interaction:**

|Level     |Definition                                                                            |Example                                                                          |Test                                                                 |
|----------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|
|**Weak**  |Gradient flow exists from compositional loss to representations                       |Standard neural network training                                                 |Present in most systems; not distinctive                             |
|**Medium**|Representations demonstrably *change* in response to compositional demands            |Pre-training → fine-tuning on compositional task changes representation structure|Measure representation similarity before/after compositional training|
|**Strong**|System develops *new representational primitives* in response to compositional failure|Encountering novel composition demands → new symbol types emerge                 |Track vocabulary/representation space expansion over time            |

**APH’s claim is that intelligence requires at least medium-level interaction, and genuine generativity requires strong interaction.**

Weak interaction is ubiquitous and uninteresting. The question is whether composition *actually reshapes* representations (medium) or merely uses them, and whether novel compositional demands can *create* new representational resources (strong).

**Empirical tests:**

1. **Medium interaction test:** Train system A with representations frozen after initial learning, system B with ongoing representation updates during compositional training. APH predicts B outperforms A on novel compositions—not just in accuracy, but in the *structure* of generalization errors.
1. **Strong interaction test:** Present compositional demands that can’t be satisfied with existing representational vocabulary. Does the system (a) fail, (b) approximate with existing resources, or (c) develop new representational distinctions? APH predicts embedded systems are more likely to show (c).

*This is more demanding than “gradient flow exists” but less mysterious than “genuine understanding.” It’s measurable.*

### Why This Isn’t Just “Composition Over Learned Representations”

The feedback worry: if symbol formation is widespread, the framework reduces to “composition (of the right type) over whatever stable representations the system has formed.”

The interaction reframing addresses this:

**Symbol formation without compositional feedback** produces representations optimized for the input statistics, not for compositional usefulness. Edge detectors are tuned to retinal statistics. They’re not refined by downstream compositional demands.

**Composition over static representations** is limited to recombining what’s already there. You can’t compose your way to genuinely new representational capacity if the primitives are fixed.

**Interactive symbol formation and composition** produces representations that are *shaped by* compositional demands. The system learns to carve the world in ways that support productive composition. This is what enables generativity—not composition alone, not symbol formation alone, but their mutual refinement.

*Empirical prediction: Systems where representation learning is informed by compositional objectives should show better generalization than systems where representations are learned first and composed later. This aligns with findings that end-to-end training outperforms pipeline approaches (Lake & Baroni, 2018), but the interaction framing makes a stronger claim about why.*

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

**Important implication: Stage 2 may be widespread.**

Edge detectors in early visual cortex arguably meet these criteria: extracted from continuous retinal input, clustered (edge vs. non-edge), stable, context-independent (fire for edges regardless of scene content). Similarly, learned features in convolutional networks may qualify.

This is not a bug in the framework—it’s the point of the *dual* criterion. **Symbol formation is necessary but not sufficient for intelligence.** Early visual cortex has Stage 2. It’s not intelligent. That’s exactly what the framework predicts: intelligence requires symbol formation *plus* compositional structure (and specifically the generative types—see below).

The question “does system X form symbols?” may often have the answer “yes.” The question that matters is: “does it form symbols *and* compose them generatively?”

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
- *Interpolative* composition (3a–3b): finite combinatorial space; could in principle be captured by a sufficiently large lookup table
- *Generative* composition (3c–3d): unbounded combinatorial space; requires genuinely generative mechanisms
   
   This operationalizes the distinction. Word2vec does concatenative (vector addition) but can’t do recursive embedding. The boundary is principled: finite vs. infinite generative capacity (see Threshold Problem below).

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

**What does APH add?**

|Framework            |Core Claim                                                |APH Difference                                                                                                                      |
|---------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
|Language of Thought  |Thought has compositional syntax                          |LOT assumes symbols exist; APH asks where they come from and requires formation-composition *interaction*                           |
|Global Workspace     |Conscious access enables flexible combination             |GWT explains *access*; APH explains *what* gets accessed (formed, interactively composed symbols)                                   |
|Predictive Processing|Brain minimizes prediction error via hierarchical models  |PP explains learning dynamics; APH makes specific claims about composition types and their ordering                                 |
|Lake & Baroni        |Compositional generalization requires systematic structure|L&B tests for compositionality; APH claims the *interaction* between formation and composition is key, not just compositional output|

**Specific differential predictions:**

1. **vs. LOT:** LOT doesn’t distinguish composition types or predict the 3a→3b→3c→3d ordering. APH predicts specific dissociations (3a-3b success with 3c-3d failure) that LOT doesn’t.
1. **vs. Global Workspace:** GWT predicts that conscious access enables flexible recombination, but doesn’t predict that *interactive* formation-composition should outperform modular architectures. APH does.
1. **vs. Lake & Baroni:** L&B’s empirical work shows compositional generalization requires compositional structure. APH makes the stronger claim that *feedback from composition to representation learning* is what produces generativity—not just having both, but their interaction.

*If these differential predictions fail—if LOT or GWT already predict everything APH predicts—then APH is relabeling, not discovering. The empirical program tests this.*

### Enabling Conditions vs. The Criterion

- **Enabling conditions** (necessary but not distinctive): temporal stabilization, attentional selection
- **The criterion** (what abstraction *is*): interactive symbol formation and composition

Stabilization and attention are required for abstraction but don’t constitute it—many non-abstractive processes require them.

### The Threshold Problem

If both symbol formation and compositionality exist on spectra, where does abstraction “begin”?

**For symbol formation:** When does a learned feature become a symbol? Convolutional networks learn edge detectors—are these symbols? Current answer: only if they show the formation criteria above (extracted from continuous input, clustered, stable, context-independent). Edge detectors may qualify; this is an empirical question.

**For compositionality:** The composition-type framework (see above) provides more structure than a single threshold. The question becomes: which types of composition count as “genuine” generative intelligence?

- **Concatenative composition** (3a) may be achievable without genuine symbolic capacity—sequence models do this
- **Role-filler binding** (3b) requires separating structure from content—this seems closer to genuine composition
- **Recursive embedding** (3c) and **analogical mapping** (3d) require treating composed structures as primitives and abstracting structure from content entirely

**The original argument for 3c: finite vs. unbounded generative capacity**

|Composition Type                  |Generative Capacity          |Implication                                                               |
|----------------------------------|-----------------------------|--------------------------------------------------------------------------|
|3a–3b (concatenative, role-filler)|Finite combinatorial space   |A sufficiently large lookup table could, in principle, capture all outputs|
|3c–3d (recursive, analogical)     |Unbounded combinatorial space|No finite lookup table can capture the space                              |

This draws on Chomsky (1957): “infinite use of finite means.”

**A fair objection:** Humans don’t actually generate infinitely deep structures. We tap out at 3-4 center embeddings. If practical human capacity is finite (just large), why isn’t “very large finite” sufficient for intelligence?

**Reframing: unboundedness through novelty, not depth**

The unboundedness that matters may not be infinite recursive depth in any single structure. It’s the *open-ended capacity to expand* in response to novelty:

|Aspect                |Depth-Based View                       |Novelty-Based View                                   |
|----------------------|---------------------------------------|-----------------------------------------------------|
|**What’s unbounded**  |Recursive depth of single structures   |Ongoing expansion of representational capacity       |
|**Mechanism**         |Recursion enables arbitrary nesting    |Novelty creates pressure for new symbols/compositions|
|**Why humans qualify**|Can generate deep structures (disputed)|Continuously encounter novelty and update            |
|**Why LLMs might not**|May handle deep structures             |Don’t encounter novelty; recombine within fixed space|

*This reframes the criterion: what matters isn’t 3c specifically, but the capacity for novelty-driven expansion. 3c (recursive embedding) may be important because it provides the compositional machinery to handle the structural complexity that novelty often presents—but it’s the openness to novelty, not the depth per se, that distinguishes intelligence.*

This connects to embeddedness: embedded systems encounter genuine novelty because they have a self/world distinction. Non-embedded systems recombine within their training distribution.

*This is a hypothesis drawing on linguistic theory (Chomsky, 1957; Hauser, Chomsky & Fitch, 2002) but reinterpreted through the novelty lens. Whether this reframing holds is an empirical question.*

-----

## Key Claims

### The Interaction Criterion

The framework proposes that intelligence emerges from the *interaction* between:

1. **Symbol formation**: extracting discrete representational units from raw input
1. **Compositional structure**: systematically combining those units

The key claim is not that both are present, but that they *inform each other*: composition shapes what gets formed; formation enables new compositions.

**The test:** Does composition feed back to refine symbol formation? Does the system develop new representational primitives in response to compositional demands?

**Empirical support (preliminary, replication needed):** Compositional generalization requires end-to-end compositional structure—factorized input encoding AND compositional output; factorized representations alone prove insufficient (Lake & Baroni, 2018; Kim & Linzen, 2020). This supports the interaction claim: representations must be shaped by compositional objectives, not learned independently.

### Embeddedness and Novelty Generation

**Why does embeddedness matter for intelligence? Not just for self-modeling—for *novelty*.**

The interaction criterion claims intelligence emerges from a feedback loop: composition refines symbol formation, which enables new compositions. But what *drives* this loop? Why would a system need to refine its symbol vocabulary?

**The answer: encountering genuine novelty.**

Novelty creates compositional demands the current symbol vocabulary can’t handle. This is what creates pressure for the formation-composition feedback loop. Without novelty, you just recombine existing symbols in existing ways. With novelty, you must either:

- Fail (can’t represent the new thing)
- Form new symbols / refine existing ones (update to accommodate novelty)
- Compose existing symbols in new ways (generative response)

**Embeddedness is what enables recognizing novelty.**

|Component              |Role in Novelty Recognition                                                                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|Self/world distinction |Without it, everything is just input—you can’t distinguish “familiar” from “novel” because there’s no stable self against which to measure|
|Temporal persistence   |Novelty requires comparison to what came before; ephemeral systems can’t accumulate the baseline                                          |
|Environmental stability|If everything is chaos, nothing is specifically novel—novelty requires stable background against which anomalies stand out                |
|Action-consequence     |Your actions produce expected consequences; novelty is when consequences diverge from expectations                                        |

**This connects embeddedness to the interaction criterion:**

1. Embedded system encounters world
1. World presents something that doesn’t fit current representations (novelty)
1. Current compositional capacity fails or is strained
1. Pressure to refine symbol formation and/or develop new compositional strategies
1. Updated system can now handle this class of inputs
1. Encounters next novelty → cycle continues

**Why LLMs may be limited:**

LLMs don’t *encounter* novelty in the relevant sense:

- During training: static corpus, no ongoing world interaction
- During inference: no persistence, no accumulating self against which to measure novelty

They recombine within a learned space. They can produce outputs not in their training data (recombination), but they don’t *experience* inputs as novel because there’s no stable self that persists and encounters an external world.

*This is a hypothesis about why embeddedness matters for intelligence—not just for self-modeling, but for the generative pressure that drives the formation-composition feedback loop.*

**Recombination vs. Novelty Generation:**

|             |Recombination                          |Novelty Generation                                                       |
|-------------|---------------------------------------|-------------------------------------------------------------------------|
|**Source**   |Elements already in the space          |Pressure from encountering what’s outside the space                      |
|**Mechanism**|New combinations of existing primitives|New primitives formed in response to novel input                         |
|**Requires** |Compositional structure                |Embeddedness (to recognize novelty) + interaction (to update in response)|
|**Bound**    |The learned space                      |Potentially unbounded (world keeps presenting novelty)                   |

*This reframes the 3c threshold question: maybe what matters isn’t infinite recursive depth, but the capacity for ongoing expansion in response to novelty. Humans don’t actually generate infinitely deep structures—we tap out at 3-4 center embeddings. But we do continuously encounter novelty and update. The unboundedness isn’t in any single structure; it’s in the open-ended process of novelty-driven refinement.*

**Five components are proposed as necessary:**

|Component                         |Definition                      |Why Necessary                            |
|----------------------------------|--------------------------------|-----------------------------------------|
|**Action-consequence contingency**|Outputs affect subsequent inputs|Creates need for self/world decomposition|
|**Feedback closure**              |Consequences return to agent    |Enables learning from consequences       |
|**Temporal persistence**          |Agent continues across time     |Enables accumulation of self-model       |
|**Self-boundary awareness**       |Access to own limits/constraints|Enables modeling where self ends         |
|**Environmental stability**       |Consistent regularities in world|Enables modeling what world contributes  |

**Deriving Level 4 from embeddedness:**

The connection between these five components and self-referential abstraction is not merely asserted—it follows from what self-reference requires:

1. **Self-referential abstraction requires a self/world distinction.** You cannot model your own representational processes without distinguishing *your* processes from *world* processes.
1. **A self/world distinction requires all five components:**
- *Action-consequence contingency*: If your outputs don’t affect your inputs, you have no basis for distinguishing “what I did” from “what happened.” The causal asymmetry creates the distinction.
- *Feedback closure*: The consequences must return to you—otherwise you can’t learn where you end and world begins.
- *Temporal persistence*: The self/world model must accumulate over time. An ephemeral system can’t build a stable self-representation.
- *Self-boundary awareness*: You need access to your own limits (what you can/can’t do, what you do/don’t know) to model where self ends.
- *Environmental stability*: If the world is chaotic noise, you can’t model “what world contributes”—there’s nothing stable to model.
1. **Each component is individually necessary.** Remove any one:
- No action-consequence → no basis for self/world distinction
- No feedback closure → no learning from the distinction
- No persistence → no accumulated self-model
- No self-boundary awareness → can’t locate the boundary
- No environmental stability → can’t model the world side

Bodies naturally provide all five—they persist, have sensable boundaries (proprioception, interoception), exist in stable physical environments, and their actions have consequences. But embodiment is *instrumental*, not *constitutive*. The relational structure is what matters.

**Application to LLMs:** Current LLMs lack all five components during training (static corpus, no persistence, no access to own constraints, variable conversational contexts). This predicts Level 4 limitations—but current LLMs do show some self-modeling (calibrated confidence, uncertainty estimation).

Two possible explanations:

1. **Pattern-matching:** LLMs reproduce self-referential *language* learned from training data without genuine self-modeling
1. **Partial self-modeling:** Some self-knowledge is possible without full embeddedness, but it’s limited and fragile

*Distinguishing test: Pattern-matching predicts self-modeling should fail on out-of-distribution capabilities. Partial self-modeling predicts graceful degradation. This is testable.*

### Developmental Spectrum

**The interaction between symbol formation and composition operates at multiple levels of complexity.**

Earlier framings treated symbol formation as Stage 2 and composition as Stage 3—sequential capacities. But the interaction framing suggests something different: formation and composition interact at *every* level, with increasing sophistication.

|Level|Formation-Composition Interaction                                                                                    |Example                                                                                              |
|-----|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|1    |Pattern extraction (pre-symbolic)                                                                                    |Statistical regularities without discrete tokens                                                     |
|2    |Basic interaction: formed symbols enter simple compositions; composition demands shape what gets extracted           |Edge + edge → contour; contour detection refines edge sensitivity                                    |
|3    |Generative interaction: recursive composition feeds back to produce hierarchically organized symbol formation        |Syntactic structure shapes phonological representation; compositional demands create new symbol types|
|4    |Self-referential interaction: the system’s own representational processes become objects of formation and composition|Metacognition; modeling one’s own abstractions                                                       |

**What changes across levels is the depth of interaction**, not the presence/absence of either capacity:

- Level 2: Composition uses formed symbols; feedback is local
- Level 3: Composition creates pressure for new symbol types; feedback reshapes the representational vocabulary
- Level 4: The interaction itself becomes an object of representation

**Composition subtypes** (proposed complexity ordering, applying at Levels 2–4):

- 3a: Concatenative composition
- 3b: Role-filler binding
- 3c: Recursive embedding
- 3d: Analogical mapping

A system may achieve 3a–3b interaction while lacking 3c–3d. This predicts dissociations: success on role-filler tasks with failure on deep recursive embedding or cross-domain analogy.

*Note: The level model is a hypothesis about complexity of formation-composition interaction, not a claim about strict domain-general stages. A system might show Level 3 interaction in one domain while remaining at Level 2 in another.*

The self/world distinction is proposed as the **foundational abstraction** enabling Level 4: without distinguishing what comes from the system versus the environment, self-referential interaction is impossible.

-----

## Papers

**Core framework (Papers 1–9):** These develop the main theoretical machinery—the interaction criterion, composition types, embeddedness requirements.

|#|Paper                                                                       |Description                                                                    |
|-|----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|1|[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)        |The general framework: abstraction as the fundamental primitive                |
|2|[The Computational Structure of Abstraction](papers/abstraction_defined.md) |Interaction criterion: symbol formation + compositional structure              |
|3|[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)  |Compositionality as distinguishing operation; metrics; architectural conditions|
|4|[Abstraction Constrained](papers/abstraction_constrained.md)                |What abstraction is not: distinguishing from input and downstream operations   |
|5|[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)|Why prediction presupposes representational content                            |
|6|[Recursive Abstraction](papers/recursive_abstraction.md)                    |Self-reference and the mathematics of *e*                                      |
|7|[The Developmental Spectrum](papers/abstraction_developmental_spectrum.md)  |Levels of formation-composition interaction                                    |
|8|[Embeddedness and Self/World](papers/embedded_abstraction.md)               |Five components of embeddedness; derivation of Level 4 requirements            |
|9|[Self and World](papers/self_world_abstraction.md)                          |The foundational abstraction                                                   |

**Speculative extensions (Papers 10–14):** These apply the framework to consciousness, time, emotion, and social cognition. They are more speculative—the core framework doesn’t depend on them, and the author’s uncertainty about whether they advance beyond existing functionalism is genuine.

|# |Paper                                                                                |Description                                        |Status                                           |
|--|-------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------|
|10|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Self-monitoring as computational necessity         |Speculative                                      |
|11|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |Experience as embedded information format          |Speculative; may not advance beyond functionalism|
|12|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Temporal reasoning and embeddedness                |Extension                                        |
|13|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Emotions as action-formatted self-world information|Extension                                        |
|14|[Social Dynamics](papers/social_dynamics.md)                                         |Multi-agent recursive abstraction                  |Extension                                        |

**Applications (Paper 15):**

|# |Paper                                                |Description                      |
|--|-----------------------------------------------------|---------------------------------|
|15|[Beyond Large Language Models](papers/beyond_llms.md)|Architectural implications for AI|

**Recommended reading order:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → (optionally 10–14) → 15

-----

## Falsifiable Predictions

### Architecture *(preliminary support—replication needed)*

- ✓ Compositional generalization requires factorized input AND compositional output
- ✓ Factorized representations alone insufficient (high decodability, low generalization)
- **Interaction prediction:** Architectures enabling feedback from composition to representation learning should outperform modular architectures where these are separate (testable via architectural ablations)
- Systems that form their own tokens should show more robust generalization than systems given fixed tokenization (untested)

### Development

- Level progression reflects increasing depth of formation-composition interaction
- Within Level 3+, composition types follow proposed ordering: 3a before 3b before 3c before 3d
- Level-specific tasks should cluster; within-level correlations exceed across-level
- Dissociations predicted: systems (biological or artificial) may show 3a–3b while lacking 3c–3d
- **Interaction prediction:** Systems where compositional training shapes representation learning should show better out-of-distribution generalization than systems trained sequentially (representation → composition)

### LLM-Specific (with operationalization)

|Prediction                                                        |Operationalization                                                                                                               |Falsification Criterion                                                                                                                                 |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|Degradation differs by composition type                           |Compare accuracy on: (a) novel role-filler combinations, (b) recursive embedding at depth N, (c) cross-domain analogical transfer|If degradation curves are identical across types, prediction fails                                                                                      |
|Recursive depth shows steeper degradation than role-filler novelty|Accuracy on depth 2→3→4→5 embedding vs. accuracy on novel-but-shallow role-filler                                                |If role-filler novelty degrades as steeply as recursive depth, prediction fails                                                                         |
|Scaling helps 3a–3b more than 3c–3d                               |Compare performance gains across model sizes on role-filler vs. recursive/analogical tasks                                       |If 3c–3d gains match or exceed 3a–3b gains, prediction fails                                                                                            |
|Self-modeling shows ceiling without embeddedness                  |Calibration accuracy, capability self-assessment, uncertainty quantification                                                     |If models at 10T+ parameters (estimated 2027–2029) show human-level self-modeling without architectural changes providing embeddedness, prediction fails|

**Timeline commitment:** The self-modeling ceiling prediction is tested within the next generation of frontier models (roughly 2027–2029). If 10T+ parameter models show robust, general self-modeling—accurate capability self-assessment across novel domains, appropriate uncertainty even on distribution shifts—without any embeddedness modifications, the framework requires significant revision.

### Embeddedness

- Systems lacking *any* of the five components should show Level 4 limitations
- Giving LLMs access to their own capability constraints should modestly improve self-modeling (testable now)
- Episodic systems (reset each session) should show less developed self-models than persistent systems
- Level 4 without self/world distinction would falsify the framework

### Surprising Predictions

**These predictions would provide evidence for APH if confirmed:**

|Prediction                                                                                   |Surprise Level                                                                                                             |Test                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Certain insects have Level 2–3 interaction with 3a–3b composition but not 3c–3d**          |**Genuinely surprising**: conflicts with intuition that intelligence requires large brains                                 |Bees show role-filler composition in waggle dance—DISTANCE(x) + DIRECTION(y) combine systematically (Menzel et al., 2011). Prediction: bees succeed on novel role-filler combinations but fail on recursive embedding and cross-domain analogical transfer.|
|**Interactive architectures outperform modular ones even when both have same total capacity**|**Surprising if true**: most engineering intuition favors modularity                                                       |Compare: (A) representation learning → composition vs. (B) joint training with composition-to-representation feedback. APH predicts B outperforms A on out-of-distribution generalization, controlling for parameters.                                     |
|**Embedded systems show novelty-driven expansion; non-embedded systems don’t**               |**Central prediction of novelty framing**                                                                                  |Give both systems genuinely novel inputs (outside training distribution). Embedded systems should show representational expansion (new distinctions formed). Non-embedded systems should show failure or approximation with existing resources.            |
|**A sufficiently large lookup table is not intelligent regardless of behavior**              |**Philosophically surprising**: conflicts with behaviorism                                                                 |A system that memorizes input-output pairs has no formation-composition interaction. It fails the criterion even if it passes behavioral tests. Distinguishing requires internal analysis.                                                                 |
|**LLMs show formation-composition interaction limits**                                       |**Moderately surprising**: conflicts with “LLMs are generally intelligent” camp; *not* surprising to “just statistics” camp|Prediction: (1) recursive embedding degrades faster than role-filler novelty, (2) representations don’t adapt to novel compositional demands at test time, (3) self-modeling fails on out-of-distribution capabilities (vs. graceful degradation).         |

**Honest assessment:** The genuinely distinctive predictions are: (1) the bee dissociation, (2) interactive > modular architectures, (3) embedded systems show novelty-driven expansion, and (4) the specific pattern-matching vs. partial-self-modeling test for LLM self-knowledge.

**Why predictions matter:** The framework’s validity depends on generating classifications that (a) conflict with at least some prior intuitions, (b) are empirically testable, and (c) turn out to be correct. Refinement > revolution is an acceptable outcome, but the framework must do *some* theoretical work that competing frameworks don’t.

-----

## Open Questions

The framework is offered as a research program, not a finished theory. Key unresolved issues:

- **Operationalizing interaction:** Now more specific: weak (gradient flow), medium (representations change in response to compositional demands), strong (new representational primitives emerge). The claim is that intelligence requires at least medium-level interaction. Tests proposed, but not yet run.
- **Novelty recognition vs. recombination:** The framework now claims embeddedness enables novelty recognition, which drives the interaction loop. But how do we distinguish a system that *recognizes* novelty from one that just fails on out-of-distribution inputs? Proposed: novelty recognition leads to representational expansion; simple failure doesn’t.
- **The 3c threshold reframing:** Originally: 3c matters because recursive depth gives unbounded generativity. Reframed: what matters is novelty-driven expansion, not depth per se. Humans don’t generate infinitely deep structures, but we continuously encounter novelty and update. Is this reframing correct? Does 3c still mark an important boundary, or is it epiphenomenal?
- **Symbol identification thresholds:** Symbols are defined by formation (extraction from input), not compositional behavior. This may mean symbol formation is widespread. Under the interaction + novelty framing, that’s fine—widespread formation without novelty-driven feedback doesn’t constitute intelligence. But threshold questions remain.
- **The connectionist tension:** How continuous neural dynamics give rise to functionally discrete compositional representations is asserted, not explained. The framework needs a mechanistic account.
- **Discovered or stipulated?** The real test is surprising predictions. The framework now predicts: (1) bee dissociation, (2) interactive > modular architectures, (3) embedded systems show novelty-driven expansion, (4) specific failure patterns in LLM self-modeling. If these fail, the framework is doing less than claimed.
- **The Hard Problem:** Papers 10–11 argue embeddedness reframes the explanatory gap, but a functional account of self-modeling doesn’t obviously address phenomenal consciousness. *Honest answer: unclear. These papers are flagged as speculative.*
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

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Geiger, A., Lu, H., Icard, T., & Potts, C. (2021). Causal abstractions of neural networks. *Advances in Neural Information Processing Systems*, 34.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569-1579.

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

*“Intelligence is not symbol formation plus composition. It’s their interaction—each refining the other.”*

# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure.

**Current state of the framework:**

| Component | Status | Testability |
|-----------|--------|-------------|
| Composition type hierarchy (3a→3b→3c→3d) | **Load-bearing** | Directly testable; predicts specific dissociations |
| Recursive interaction framing | **Core idea** | Needs sharper operationalization |
| Strong interaction (novelty-driven expansion) | **Underdeveloped** | "New primitive" vs "novel configuration" is slippery |
| Embeddedness claims | **Exploratory** | Interesting but may collapse into simpler accounts |

**Honest assessment:** The framework's ambition (a theory of intelligence) currently outpaces its content (a taxonomy of composition plus underdeveloped ideas about interaction). The taxonomy is testable and potentially valuable. The interaction and embeddedness claims need more development before they're proper hypotheses.

-----

## The Core Idea

### The Core Claim: Recursive Interaction, Not Conjunction

**Abstraction is the recursive process of forming and composing symbols.**

Previous framings—including earlier versions of this document—treated symbol formation and compositional structure as two separate capacities. Check both boxes and you have intelligence. But this framing has a problem the feedback correctly identifies: if symbol formation is widespread (edge detectors, CNN features qualify), then all the distinguishing work falls on composition. The framework collapses to "intelligence = composition over whatever representations you have."

**A clarification for connectionists:** The framework *concedes* that symbols exist and matter—that discrete, stable, reusable representations are extracted from continuous input. This is a substantive concession; strong connectionism has historically resisted symbolic vocabulary. But the claim is not that symbol formation alone constitutes intelligence. Symbol formation is necessary. Composition is necessary. What's *sufficient* is their recursive interaction.

**An honest dilemma the framework doesn't fully escape:**

If symbol formation criteria are *stringent* (requiring something CNNs lack), the criteria risk being gerrymandered to exclude systems we've already decided aren't intelligent. If the criteria are *loose* (CNNs qualify), then the framework collapses to "composition matters"—which isn't novel.

This document accepts the loose criteria. The framework then tries to recover distinctiveness through:
1. The composition type hierarchy (load-bearing, testable)
2. Strong interaction claims (needs sharper operationalization)
3. Embeddedness claims (exploratory)

**If (2) and (3) don't pan out, what remains is (1): a taxonomy of compositional operations.** That's valuable but more modest than "a theory of intelligence." This is an honest assessment of where the framework currently stands.

**The actual claim is stronger: intelligence emerges from the *recursive interaction* between symbol formation and composition.**

This is not Fodor's language of thought plus Lake's compositional generalization. It's the claim that these two processes must *inform each other iteratively*:

1. You extract stable representations from continuous input (symbol formation)
2. You combine them systematically (composition)
3. Composition reveals structure that wasn't visible in individual symbols
4. That structure feeds back to refine symbol formation—you carve the world differently because of what composition revealed
5. Which enables more sophisticated composition
6. **Return to step 2 with refined symbols → iterate**

**The computational structure is a feedback loop:**

```
         ┌─────────────────────────────────────┐
         │                                     │
         ▼                                     │
    [Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                         ▲                                              │
                         │                                              │
                         └──── [Compositional demands/failures] ────────┘
```

This isn't metaphorical. It's a claim about computational architecture: the outputs of composition must be able to influence the processes that form symbols, and this must iterate. One-shot influence doesn't suffice—what produces expanding representational capacity is the *ongoing cycle*.

**Why interaction matters:**

| System | Forms Symbols? | Composes? | Interaction? | Intelligent? |
|--------|----------------|-----------|--------------|--------------|
| Calculator | ✗ (provided) | ✓ | N/A | No |
| V1 edge detectors | ✓ | ✗ | ✗ | No |
| CNN classifier | ✓ | Limited | Medium (training-time) | Limited |
| Word2vec | Partial | 3a only | Minimal | Marginal |
| LLM | ✓ | ✓ (3a-3b, limited 3c-3d) | Medium (training-time) | ? |
| Human cognition | ✓ | ✓ (3a–3d) | Strong (ongoing) | Yes |

**Honest problem with the calculator example:**

The calculator case is clear: we handed it symbols, it didn't form them. But CNNs and LLMs *learn* representations from data. If learned representations count as symbol formation—and by the criteria given (clustered, stable, extracted from continuous input), they do—then the calculator disanalogy stops doing much work.

What distinguishes a CNN from something intelligent? Not symbol formation (CNNs form symbols). Not composition (CNNs do limited composition). The answer has to be:

1. **Interaction type:** CNNs have medium interaction (training-time gradient flow). They lack strong interaction (novelty-driven expansion at inference).
2. **Embeddedness:** CNNs are not embedded—they don't encounter novelty, don't have self/world distinction, don't expand in response to novel inputs.

This is an honest acknowledgment: once we accept learned representations as symbols, **the framework's weight shifts almost entirely to the strong interaction + embeddedness claims**. Symbol formation becomes a necessary filter, not the distinctive criterion.

Edge detectors form symbols but those symbols don't enter compositional relationships that feed back to refine how edges are detected. Calculators compose but composition doesn't inform symbol formation (because they don't form symbols). CNNs and LLMs have both, with medium interaction. **APH's claim is that strong interaction—novelty-driven expansion, requiring embeddedness—is what produces genuine intelligence.**

This reframing changes what the framework predicts:
- Systems with both capacities operating *independently* should show limited generalization
- Systems where composition refines symbol formation (and vice versa) should show expanding representational capacity
- The "infinite use of finite means" emerges from the interaction, not from either capacity alone

*This is a working hypothesis. It predicts that architectures enabling interaction between representation learning and compositional processing should outperform architectures where these are modular and separate. This is testable.*

### Operationalizing "Interaction"

**A fair concern: how do we distinguish "composition feeds back to refine symbol formation" from "both processes share substrates in the same system"?**

If any gradient flow from compositional objectives to representation layers counts as interaction, most neural networks have it. That's too weak. If we need something stronger, what exactly?

**Proposed operationalization—three levels of interaction:**

| Level | Definition | Example | Distinctiveness |
|-------|------------|---------|-----------------|
| **Weak** | Gradient flow exists from compositional loss to representations | Standard backpropagation | Ubiquitous; not distinctive |
| **Medium** | Representations demonstrably *change* in response to compositional demands | End-to-end training changes representation structure | **Also not distinctive**—this is standard neural network training |
| **Strong** | System develops *new representational primitives* in response to novel inputs that don't fit existing vocabulary | Encountering genuinely novel compositional demands → new symbol types emerge that persist | **This is APH's distinctive claim** |

**Honest acknowledgment:** Medium interaction is what end-to-end training provides. Lake & Baroni (2018) already showed this matters. APH doesn't add much at the medium level.

**APH's actual distinctive claim is about strong interaction: novelty-driven representational expansion.**

**Important implication:** This makes intelligence a *diachronic* property (systems-over-time) rather than a *synchronic* property (snapshots of architecture). You can't look at a system at one moment and determine if it's intelligent—you need to observe it encountering novelty and watch for expansion.

This is a significant commitment. It means:
- Intelligence isn't a property of architectures, but of architectures-in-interaction-with-environments-over-time
- Testing requires longitudinal observation, not just benchmark performance
- A system might be "intelligent" in one environment (where it encounters novelty) but not another

Is this the right framing? It's consistent with developmental and ecological views of cognition, but it complicates testing considerably.

This is where the framework either succeeds or fails. The claim is:
1. Strong interaction (not just medium) is what produces genuine generativity
2. Strong interaction requires encountering novelty
3. Recognizing novelty requires embeddedness (self/world distinction)
4. Therefore: non-embedded systems can achieve medium interaction but not strong

**The load-bearing problem:** "New representational primitives" vs. "novel configurations of existing primitives" is doing critical work here, but it's genuinely slippery. 

What's the computational signature that distinguishes them? Candidates:
- Persistence and transfer to new contexts (but novel configurations can also transfer)
- Changes to the representational space itself, not just activations within it (but how do we measure this?)
- Ability to compose the new primitive with existing ones (but this might just be reconfiguration)

**Honest assessment:** This distinction needs sharper operationalization before it's a proper hypothesis rather than an intuition. The composition hierarchy is testable now; the strong interaction claim isn't yet.

If medium interaction turns out to be sufficient for everything we care about, APH is wrong—not refined, *wrong*.

**Empirical tests:**

1. **Medium interaction test:** Train system A with representations frozen after initial learning, system B with ongoing representation updates during compositional training. APH predicts B outperforms A on novel compositions—not just in accuracy, but in the *structure* of generalization errors.

2. **Strong interaction test:** Present compositional demands that can't be satisfied with existing representational vocabulary. Does the system (a) fail, (b) approximate with existing resources, or (c) develop new representational distinctions? APH predicts embedded systems are more likely to show (c).

*This is more demanding than "gradient flow exists" but less mysterious than "genuine understanding." It's measurable.*

### Why This Isn't Just "Composition Over Learned Representations"

The feedback worry: if symbol formation is widespread, the framework reduces to "composition (of the right type) over whatever stable representations the system has formed."

The interaction reframing addresses this:

**Symbol formation without compositional feedback** produces representations optimized for the input statistics, not for compositional usefulness. Edge detectors are tuned to retinal statistics. They're not refined by downstream compositional demands.

**Composition over static representations** is limited to recombining what's already there. You can't compose your way to genuinely new representational capacity if the primitives are fixed.

**Interactive symbol formation and composition** produces representations that are *shaped by* compositional demands. The system learns to carve the world in ways that support productive composition. This is what enables generativity—not composition alone, not symbol formation alone, but their mutual refinement.

*Empirical prediction: Systems where representation learning is informed by compositional objectives should show better generalization than systems where representations are learned first and composed later. This aligns with findings that end-to-end training outperforms pipeline approaches (Lake & Baroni, 2018), but the interaction framing makes a stronger claim about why.*

### Epistemological Grounding

Why these two capacities? The framework starts from an empirical observation rather than conceptual analysis of "intelligence":

**Consider the gradient of capability we can actually observe:** rocks, thermostats, calculators, computers, humans. What changes as capability increases? The systems that can handle more situations, solve more problems, represent more possibilities all involve symbolic manipulation—compositional structure over discrete representational units.

This is pattern recognition on available data: what do capable systems have that rocks don't? The answer appears to be symbols and composition. The remaining question is whether intelligence requires *forming* those symbols or merely *having* them. A calculator suggests the latter is insufficient—compositional structure over externally provided symbols doesn't constitute intelligence. Hence the two-part criterion.

**The selection bias concern:** This reasoning risks selecting criteria to match systems we already call intelligent, then declaring intelligence requires those criteria. The real test is whether the framework generates *surprising* predictions—cases where it classifies something as intelligent or non-intelligent against our prior intuitions, and turns out to be right. See [Surprising Predictions](#surprising-predictions) below.

*Acknowledged limitation: this is Earth data, human technology. But if the question is "what computational structure enables general capability," we don't need alien examples—we need to understand why the things that work, work.*

### The Symbol Identification Problem

**This is a core theoretical challenge, not a minor detail.**

If a symbol is defined as something that "enters into compositional relationships," and compositionality is the other half of the criterion, the framework is circular. We need independent criteria for symbol-hood.

**The solution: define symbols by formation, not by downstream behavior.**

The calculator insight points the way. A calculator has symbols but didn't *form* them—we handed them over. So what makes something a symbol can't be about what it *does* (compose). It has to be about how it *comes to exist*.

**A symbol is a representational unit that the system itself extracted from continuous input.**

Specifically, symbol formation occurs when a system:

1. **Receives continuous, high-dimensional input** (sensory data, raw signal)
2. **Extracts discrete representational states** (clustering in activation space, not a smooth manifold)
3. **That are stable** (the same state recurs for similar inputs)
4. **Across contexts** (the representation activates for the relevant feature regardless of what else is present)

This is genuinely independent of compositionality. You can have symbol formation without composition—a system that carves the world into discrete categories but can't combine them flexibly (Stage 2 without Stage 3). You can have composition without symbol formation—a calculator that manipulates symbols it was handed but never extracted anything from raw input.

**Operationalization:**

| Criterion | Measurement | Citation |
|-----------|-------------|----------|
| **Discreteness** | Do representations cluster in activation space rather than forming a continuous manifold? | Representational similarity analysis (Kriegeskorte et al., 2008) |
| **Stability** | Does the same cluster activate for similar inputs across time? | Temporal consistency analysis |
| **Context-independence** | Does the representation for feature X activate regardless of what other features are present? | Factorized representation probing (Higgins et al., 2017) |

**What "discrete" means in continuous systems:** Not binary or classically symbolic. Representations are discrete when they cluster—when there are attractor states, modes, separable regions in activation space rather than a smooth continuum. This is statistical discreteness, empirically measurable.

**Why this breaks the circularity:** We're asking "did the system extract stable, recurring, context-independent representations from raw input?"—not "does it compose?" A system could pass this test and still fail at composition. The two criteria are genuinely independent.

**Important implication: Stage 2 may be widespread.**

Edge detectors in early visual cortex arguably meet these criteria: extracted from continuous retinal input, clustered (edge vs. non-edge), stable, context-independent (fire for edges regardless of scene content). Similarly, learned features in convolutional networks may qualify.

This is not a bug in the framework—it's the point of the *dual* criterion. **Symbol formation is necessary but not sufficient for intelligence.** Early visual cortex has Stage 2. It's not intelligent. That's exactly what the framework predicts: intelligence requires symbol formation *plus* compositional structure (and specifically the generative types—see below).

The question "does system X form symbols?" may often have the answer "yes." The question that matters is: "does it form symbols *and* compose them generatively?"

*Remaining challenge: threshold. How clustered is clustered enough? How stable is stable enough? These require empirical calibration, but the conceptual circularity is resolved.*

### The Connectionist Tension

**How do continuous neural activations give rise to discrete symbols?**

The framework draws on Fodor's language of thought, which posits discrete syntactically structured representations. But neural networks—biological and artificial—traffic in continuous activation patterns. If intelligence requires symbols, and brains are neural networks, where do the symbols come from?

**Three positions:**

1. **Strong discretization:** Symbols are neurally implemented as discrete attractor states. Evidence: concept cells showing highly selective firing (Quiroga et al., 2005); discrete attractor dynamics in working memory (Amit, 1995). Problem: most neural coding appears distributed, not localist.

2. **Functional discretization:** Continuous activations implement functionally discrete representations—the system *behaves as if* it has discrete tokens even though the substrate is continuous. Evidence: neural networks can learn discrete-like compositional structure (Lake & Baroni, 2018); vector symbolic architectures achieve symbolic computation in continuous space (Kanerva, 2009). Problem: "behaves as if" needs rigorous cashing out.

3. **Levels of description:** The symbolic level is a higher-level description of continuous dynamics, valid for some purposes but not claiming discrete implementation. Problem: risks making the framework unfalsifiable—any system can be described symbolically if you squint.

**Current position:** The framework adopts (2) with constraints from (1). Symbols are patterns of activation that exhibit:
- Clustering in representational space (discreteness is statistical, not absolute)
- Consistent recurrence across contexts (same cluster activates for same feature)
- Combinatorial productivity (clusters combine systematically)

This is compatible with predictive processing—hierarchical generative models can have functionally discrete states at higher levels while being implemented in continuous prediction-error dynamics (Friston, 2010). But the integration requires more work.

*This tension is not resolved. A fully satisfying account would show exactly how continuous dynamics give rise to functionally discrete, compositional representations. The framework claims this happens; it does not yet explain the mechanism.*

### What Makes a Representation Compositional

A representation is compositional when (Fodor & Pylyshyn, 1988; Szabó, 2012):

1. It consists of parts (constituents) that are themselves meaningful
2. The meaning of the whole is determined by the meanings of the parts and their mode of combination
3. The same parts can recombine to form different wholes with different meanings

The test is **systematicity**: the capacity to understand or produce novel combinations of familiar elements. If a system understands "John loves Mary," can it understand "Mary loves John"? If it can represent RED and SQUARE separately, can it combine them into RED SQUARE?

### Types of Compositional Structure

**Not all composition is the same.**

The framework initially treated "Stage 3: Recursive composition" as a single capacity. But compositional structure comes in distinct types with potentially different computational requirements, developmental trajectories, and neural implementations:

| Type | Structure | Example | Computational Requirement |
|------|-----------|---------|--------------------------|
| **Concatenative** | A + B → AB | "blue" + "bird" → "bluebird" | Sequencing; minimal structure |
| **Role-filler binding** | R(x) + S(y) → R(x)S(y) | AGENT(dog) + ACTION(chased) + PATIENT(cat) | Structural slots separable from content |
| **Recursive embedding** | A contains [B contains C] | "The dog [that chased the cat [that caught the mouse]]" | Composed units become inputs to further composition |
| **Analogical mapping** | Structure(A) → Structure(B) | atom:nucleus :: solar system:sun | Abstract structure from content; transfer across domains |

**Proposed complexity ordering:**

Concatenative → Role-filler binding → Recursive embedding → Analogical mapping

Each level requires capacities the previous level doesn't:
- Role-filler requires separating structure from content
- Recursive embedding requires treating composed wholes as compositional primitives
- Analogical mapping requires abstracting structure entirely and applying it to novel content

*This ordering is a hypothesis, not established fact. It generates testable predictions about developmental sequence and dissociations.*

**Implications for the framework:**

1. **The bee case becomes more precise:** Waggle dance composition (distance + direction) is plausibly role-filler binding—DISTANCE(x) + DIRECTION(y)—not recursive embedding. Bees may have some composition types but not others. This is a more nuanced prediction than "Stage 3 or not."

2. **LLM capacities become differentiable:** Current LLMs may excel at concatenative and role-filler composition (pattern-match from training data) while struggling with recursive embedding at depth and analogical transfer to novel domains. This predicts *specific* failure patterns rather than generic "limited Stage 3."

3. **The generative/interpolative distinction gets teeth:** 
   - *Interpolative* composition (3a–3b): finite combinatorial space; could in principle be captured by a sufficiently large lookup table
   - *Generative* composition (3c–3d): unbounded combinatorial space; requires genuinely generative mechanisms
   
   This operationalizes the distinction. Word2vec does concatenative (vector addition) but can't do recursive embedding. The boundary is principled: finite vs. infinite generative capacity (see Threshold Problem below).

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

| Framework | Core Claim | APH Difference |
|-----------|------------|----------------|
| Language of Thought | Thought has compositional syntax | LOT assumes symbols exist; APH asks where they come from and requires formation-composition *recursive interaction* |
| Global Workspace | Conscious access enables flexible combination | GWT explains *access*; APH explains *what* gets accessed and claims the recursive loop is what produces generativity |
| Predictive Processing | Brain minimizes prediction error via hierarchical models | PP explains learning dynamics; APH makes specific claims about composition types and the role of novelty |
| Lake & Baroni | Compositional generalization requires systematic structure | See detailed comparison below |

**APH vs. Lake & Baroni—a detailed comparison:**

L&B's finding: End-to-end training with compositional structure outperforms pipeline approaches (learn representations → learn composition separately).

This supports medium-level interaction. But APH's distinctive claim is about *strong* interaction, which L&B don't address.

**APH vs. "Sophisticated Interpolation" Frameworks:**

A critical question: does APH predict anything that "LLMs are sophisticated interpolators over training distribution" doesn't?

| Prediction | Interpolation Framework | APH | Differential? |
|------------|------------------------|-----|---------------|
| LLMs fail on OOD inputs | ✓ Predicts failure | ✓ Predicts failure | **No** |
| LLMs struggle with deep recursion | ✓ (beyond training depth) | ✓ | **No** |
| Scaling helps within-distribution | ✓ | ✓ | **No** |
| **Composition type dissociations** | Unclear—might predict uniform degradation | Predicts *specific* pattern: 3a-3b preserved, 3c-3d degrades | **Maybe** |
| **Embedded systems show expansion, not just failure** | Doesn't address | Predicts embedded systems *expand* repertoire on novelty | **Yes** |
| **Bees: specific dissociation pattern** | Doesn't address | Predicts role-filler success, recursive failure | **Yes** |
| **Self-modeling pattern** | Predicts failure on OOD | Predicts specific pattern: reproduces training-distribution self-knowledge, fails on novel capabilities | **Weak** |

**Honest assessment of differential predictions:**

- **Strong differential:** Embedded systems should show *expansion* (new primitives) on novel inputs, not just failure or approximation. Interpolation frameworks predict failure; APH predicts embedded systems do something qualitatively different.
- **Moderate differential:** Composition type dissociations with specific ordering. Interpolation might predict degradation, but not the specific 3a-3b vs. 3c-3d pattern.
- **Weak differential:** LLM predictions largely overlap with "sophisticated interpolation."

**The framework's real bet:** The strong differential prediction—that embeddedness enables *expansion* rather than failure on novelty—is what distinguishes APH from simpler frameworks. If this doesn't hold, APH collapses into "interpolation + grounding critique."

*If these differential predictions fail—if competing frameworks already predict everything APH predicts—then APH is sophisticated relabeling, not discovery. The empirical program tests this.*

### Enabling Conditions vs. The Criterion

- **Enabling conditions** (necessary but not distinctive): temporal stabilization, attentional selection
- **The criterion** (what abstraction *is*): recursive interaction between symbol formation and composition

Stabilization and attention are required for abstraction but don't constitute it—many non-abstractive processes require them.

### The Threshold Problem

If both symbol formation and compositionality exist on spectra, where does abstraction "begin"?

**For symbol formation:** When does a learned feature become a symbol? Convolutional networks learn edge detectors—are these symbols? Current answer: only if they show the formation criteria above (extracted from continuous input, clustered, stable, context-independent). Edge detectors may qualify; this is an empirical question.

**For compositionality:** The composition-type framework (see above) provides more structure than a single threshold. The question becomes: which types of composition count as "genuine" generative intelligence?

- **Concatenative composition** (3a) may be achievable without genuine symbolic capacity—sequence models do this
- **Role-filler binding** (3b) requires separating structure from content—this seems closer to genuine composition
- **Recursive embedding** (3c) and **analogical mapping** (3d) require treating composed structures as primitives and abstracting structure from content entirely

**The original argument for 3c: finite vs. unbounded generative capacity**

| Composition Type | Generative Capacity | Implication |
|------------------|---------------------|-------------|
| 3a–3b (concatenative, role-filler) | Finite combinatorial space | A sufficiently large lookup table could, in principle, capture all outputs |
| 3c–3d (recursive, analogical) | Unbounded combinatorial space | No finite lookup table can capture the space |

This draws on Chomsky (1957): "infinite use of finite means."

**A fair objection:** Humans don't actually generate infinitely deep structures. We tap out at 3-4 center embeddings. If practical human capacity is finite (just large), why isn't "very large finite" sufficient for intelligence?

**Reframing: unboundedness through novelty, not depth**

The unboundedness that matters may not be infinite recursive depth in any single structure. It's the *open-ended capacity to expand* in response to novelty:

| Aspect | Depth-Based View | Novelty-Based View |
|--------|------------------|-------------------|
| **What's unbounded** | Recursive depth of single structures | Ongoing expansion of representational capacity |
| **Mechanism** | Recursion enables arbitrary nesting | Novelty creates pressure for new symbols/compositions |
| **Why humans qualify** | Can generate deep structures (disputed) | Continuously encounter novelty and update |
| **Why LLMs might not** | May handle deep structures | Don't encounter novelty; recombine within fixed space |

*This reframes the criterion: what matters isn't 3c specifically, but the capacity for novelty-driven expansion. 3c (recursive embedding) may be important because it provides the compositional machinery to handle the structural complexity that novelty often presents—but it's the openness to novelty, not the depth per se, that distinguishes intelligence.*

This connects to embeddedness: embedded systems encounter genuine novelty because they have a self/world distinction. Non-embedded systems recombine within their training distribution.

*This is a hypothesis drawing on linguistic theory (Chomsky, 1957; Hauser, Chomsky & Fitch, 2002) but reinterpreted through the novelty lens. Whether this reframing holds is an empirical question.*

-----

## Key Claims

### The Recursive Interaction Criterion

The framework proposes that intelligence emerges from the *recursive interaction* between:
1. **Symbol formation**: extracting discrete representational units from raw input
2. **Compositional structure**: systematically combining those units

The key claim is not that both are present, but that they *inform each other iteratively*: composition shapes what gets formed; formation enables new compositions; the loop repeats.

**The test:** Does composition feed back to refine symbol formation? Does the system develop new representational primitives in response to compositional demands? Does this iterate?

**Empirical support (preliminary, replication needed):** Compositional generalization requires end-to-end compositional structure—factorized input encoding AND compositional output; factorized representations alone prove insufficient (Lake & Baroni, 2018; Kim & Linzen, 2020). This supports the interaction claim: representations must be shaped by compositional objectives, not learned independently.

**What APH adds to Lake & Baroni:** Their finding is that end-to-end training beats pipeline approaches. APH interprets this as evidence for recursive interaction—but makes the stronger claim that *ongoing* iteration (not just training-time gradient flow) is what produces genuine generativity. This predicts that systems with persistent, novelty-driven iteration should outperform systems with only training-time interaction.

### Embeddedness and Novelty Generation (Exploratory)

**This section is exploratory, not load-bearing. The composition type hierarchy stands independently.**

The idea: Strong interaction might require encountering genuine novelty, which might require a stable self against which to measure. If so, embeddedness (persistence, self/world distinction) would enable what non-embedded systems can't achieve.

**The argument sketch:**
1. Recursive interaction needs pressure to iterate
2. Pressure comes from encountering novelty  
3. Recognizing novelty requires distinguishing "fits my model" from "doesn't fit"
4. That might require a stable self-model
5. A stable self-model might require embeddedness

**The honest problem:**

Why isn't "far from training distribution" computationally equivalent to "something I haven't encountered"? The proposed distinction—embedded systems *expand* while non-embedded systems *fail*—is interesting but hard to operationalize. What counts as expansion vs. sophisticated approximation?

This distinction might collapse entirely. If it does, embeddedness becomes unnecessary for novelty recognition, and the framework loses this prediction. But the composition type hierarchy remains.

**Status:** Worth exploring, but has too many interpretive degrees of freedom to be a clean test. Don't treat this as load-bearing.

**Application to LLMs (exploratory):**

If the embeddedness idea has merit, LLMs would be limited because:
- Static training corpus (no ongoing world interaction)
- No persistence at inference (no accumulating self-model)
- ICL is recombination within a fixed space, not expansion

But this is all contingent on the embeddedness distinction holding up—which it might not.

### Five Embeddedness Components (Exploratory)

**If the embeddedness idea has merit**, these components might be relevant:

| Component | Definition |
|-----------|------------|
| Action-consequence contingency | Outputs affect subsequent inputs |
| Feedback closure | Consequences return to agent |
| Temporal persistence | Agent continues across time |
| Self-boundary awareness | Access to own limits/constraints |
| Environmental stability | Consistent regularities in world |

Bodies naturally provide all five. But this is exploratory—we don't know if these components are necessary, sufficient, or even relevant to the novelty question.

### Developmental Spectrum

**The interaction between symbol formation and composition operates at multiple levels of complexity.**

Earlier framings treated symbol formation as Stage 2 and composition as Stage 3—sequential capacities. But the interaction framing suggests something different: formation and composition interact at *every* level, with increasing sophistication.

| Level | Formation-Composition Interaction | Example |
|-------|-----------------------------------|---------|
| 1 | Pattern extraction (pre-symbolic) | Statistical regularities without discrete tokens |
| 2 | Basic interaction: formed symbols enter simple compositions; composition demands shape what gets extracted | Edge + edge → contour; contour detection refines edge sensitivity |
| 3 | Generative interaction: recursive composition feeds back to produce hierarchically organized symbol formation | Syntactic structure shapes phonological representation; compositional demands create new symbol types |
| 4 | Self-referential interaction: the system's own representational processes become objects of formation and composition | Metacognition; modeling one's own abstractions |

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

| # | Paper | Description |
|---|-------|-------------|
| 1 | [Abstraction Is All You Need](papers/abstraction_is_all_you_need.md) | The general framework: abstraction as the fundamental primitive |
| 2 | [The Computational Structure of Abstraction](papers/abstraction_defined.md) | Interaction criterion: symbol formation + compositional structure |
| 3 | [Abstraction Beyond Compression](papers/abstraction_beyond_compression.md) | Compositionality as distinguishing operation; metrics; architectural conditions |
| 4 | [Abstraction Constrained](papers/abstraction_constrained.md) | What abstraction is not: distinguishing from input and downstream operations |
| 5 | [Prediction Requires Abstraction](papers/prediction_requires_abstraction.md) | Why prediction presupposes representational content |
| 6 | [Recursive Abstraction](papers/recursive_abstraction.md) | Self-reference and the mathematics of *e* |
| 7 | [The Developmental Spectrum](papers/abstraction_developmental_spectrum.md) | Levels of formation-composition interaction |
| 8 | [Embeddedness and Self/World](papers/embedded_abstraction.md) | Five components of embeddedness; derivation of Level 4 requirements |
| 9 | [Self and World](papers/self_world_abstraction.md) | The foundational abstraction |

**Adjacent explorations (Papers 10–14):** 

These papers explore connections to consciousness, time, emotion, and social cognition. They're adjacent to the core framework—potentially interesting but not load-bearing. The core claims (Papers 1–9) stand independently.

| # | Paper | Description |
|---|-------|-------------|
| 10 | [Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md) | Self-monitoring as computational necessity |
| 11 | [The Hard Problem Reframed](papers/hard_problem_reframed.md) | Experience as embedded information format |
| 12 | [Time as Embodied Abstraction](papers/time_embodied_abstraction.md) | Temporal reasoning and embeddedness |
| 13 | [Emotion as Embedded Information](papers/emotion_embedded_information.md) | Emotions as action-formatted self-world information |
| 14 | [Social Dynamics](papers/social_dynamics.md) | Multi-agent recursive abstraction |

**Applications (Paper 15):**

| # | Paper | Description |
|---|-------|-------------|
| 15 | [Beyond Large Language Models](papers/beyond_llms.md) | Architectural implications for AI |

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

| Prediction | Operationalization | Falsification Criterion |
|------------|-------------------|------------------------|
| Degradation differs by composition type | Compare accuracy on: (a) novel role-filler combinations, (b) recursive embedding at depth N, (c) cross-domain analogical transfer | If degradation curves are identical across types, prediction fails |
| Recursive depth shows steeper degradation than role-filler novelty | Accuracy on depth 2→3→4→5 embedding vs. accuracy on novel-but-shallow role-filler | If role-filler novelty degrades as steeply as recursive depth, prediction fails |
| Scaling helps 3a–3b more than 3c–3d | Compare performance gains across model sizes on role-filler vs. recursive/analogical tasks | If 3c–3d gains match or exceed 3a–3b gains, prediction fails |
| Self-modeling shows ceiling without embeddedness | Calibration accuracy, capability self-assessment, uncertainty quantification | If models at 10T+ parameters (estimated 2027–2029) show human-level self-modeling without architectural changes providing embeddedness, prediction fails |

**Timeline commitment:** The self-modeling ceiling prediction is tested within the next generation of frontier models (roughly 2027–2029). If 10T+ parameter models show robust, general self-modeling—accurate capability self-assessment across novel domains, appropriate uncertainty even on distribution shifts—without any embeddedness modifications, the framework requires significant revision.

### Embeddedness (Exploratory Predictions)

These are interesting to explore but not load-bearing:

- Giving LLMs access to their own capability constraints might improve self-modeling (testable now)
- Episodic systems (reset each session) might show less developed self-models than persistent systems
- Systems with action-consequence loops might show different learning dynamics

**Status:** If these don't pan out, it narrows the framework to the composition claims. It doesn't falsify APH.

### Predictions Summary

**Ranked by testability and load-bearing status:**

| Prediction | Testability | Status |
|------------|-------------|--------|
| **Composition dissociations: 3a-3b success with 3c-3d failure** | **High** | **Load-bearing**—if this fails, APH's main claim fails |
| **Bee dissociation: role-filler yes, recursive no** | **High** | Load-bearing—specific test of composition hierarchy |
| **Recursive embedding degrades faster than role-filler novelty in LLMs** | **High** | Load-bearing—testable now |
| **Interactive > modular architectures (matched capacity)** | **Medium** | Core claim—requires controlled comparison |
| **Embedded systems expand, non-embedded fail** | **Low** | **Exploratory**—too many confounds for clean test |

**Recommendation:** Focus on composition type predictions. They're tractable and would be valuable findings independent of the broader framework. The embeddedness predictions are interesting to explore but shouldn't be treated as tests of APH.

### What Would Make APH Wrong

| Claim | Falsification |
|-------|---------------|
| **Composition types dissociate** | No 3a-3b vs. 3c-3d differences found across systems |
| **Hierarchy ordering matters** | Dissociations exist but ordering is wrong (e.g., 3c easier than 3b) |

**Note:** The embeddedness claims are exploratory. Finding that non-embedded systems can expand wouldn't falsify APH—it would just show that part of the exploration didn't pan out. The composition hierarchy is what APH lives or dies on.

-----

## Open Questions

**On the load-bearing claims (composition hierarchy):**

- Will dissociations be clean or messy? Likely: partial 3c success, degraded 3d. The question is whether the *pattern* confirms the hierarchy even if boundaries aren't sharp.
- Does the ordering hold across domains? Language vs. vision vs. reasoning may show different patterns.

**On the interaction claims (needs work):**

- "New primitive" vs. "novel configuration" is load-bearing but slippery. What's the computational signature? This needs sharper operationalization before it's testable.
- The diachronic framing (intelligence as systems-over-time, not snapshots) complicates testing. Is this the right commitment?

**On embeddedness (exploratory):**

- The "OOD detection" vs. "novelty recognition" distinction might collapse. If so, embeddedness is interesting but not necessary.
- This is worth exploring but shouldn't be treated as testing APH.

**The meta-question:**

What does APH add to "interpolation critique + grounding critique"? 

- The composition hierarchy probably adds something—it's a testable taxonomy with specific predictions.
- The strong interaction and embeddedness claims are intuitions that need development, not yet proper hypotheses.

**Honest summary:** The framework's ambition (a theory of intelligence) currently outpaces its content (a taxonomy of composition plus underdeveloped ideas about interaction). The taxonomy is valuable on its own terms. The rest needs work.

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

Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., ... & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *Proceedings of ICLR 2017*.

Kanerva, P. (2009). Hyperdimensional computing: An introduction to computing in distributed representation with high-dimensional random vectors. *Cognitive Computation*, 1(2), 139-159.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *Proceedings of EMNLP 2020*.

Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008). Representational similarity analysis—connecting the branches of systems neuroscience. *Frontiers in Systems Neuroscience*, 2, 4.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML 2018*.

Menzel, R., Kirbach, A., Haass, W. D., Fischer, B., Fuchs, J., Koblofsky, M., ... & Greggers, U. (2011). A common frame of reference for learned and communicated vectors in honeybee navigation. *Current Biology*, 21(8), 645-650.

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

*"The composition hierarchy is testable now. The interaction claims need sharper operationalization. Test the former; develop the latter."*

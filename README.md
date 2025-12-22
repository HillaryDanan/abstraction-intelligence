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

**Scoping the claim:** Non-abstractive processing exists—pure reactive systems with stimulus-response mappings but no symbol formation (thermostats, tropisms, basic reflexes). The framework's load-bearing element is not "abstraction" as a label, but the *composition hierarchy* and its predicted dissociations. The claim: 3c-3d requires something beyond pattern matching. That's testable independent of terminology.

**Biological grounding:** Neurochemical systems appear to implement compositional self-state abstraction—factorized dimensions (serotonin, dopamine, norepinephrine, GLP-1) that combine with world-state to produce context-appropriate behavior (see [Paper 18](papers/mind_body_neurochemistry.md)). This provides biological evidence that intelligent systems represent internal state compositionally, not as holistic snapshots.

-----

## The Composition Hierarchy

|Type                 |Structure                  |Example                                   |
|---------------------|---------------------------|------------------------------------------|
|**3a: Concatenative**|A + B → AB                 |"blue bird"                               |
|**3b: Role-filler**  |R(x) + S(y) → R(x)S(y)     |AGENT(dog) + ACTION(chased) + PATIENT(cat)|
|**3c: Recursive**    |A contains [B contains C]  |"The dog [that chased the cat [that…]]"   |
|**3d: Analogical**   |Structure(A) → Structure(B)|atom:nucleus :: solar system:sun          |

**Computational framing:**

|Type  |Mechanism                            |Complexity                                                           |Formal basis                            |
|------|-------------------------------------|---------------------------------------------------------------------|----------------------------------------|
|**3a**|Sequence concatenation               |O(1) per operation                                                   |Finite automata                         |
|**3b**|Slot-filling / template instantiation|O(1) per slot                                                        |Finite automata                         |
|**3c**|Stack-based self-reference           |O(n) space for depth n                                               |Context-free grammars, pushdown automata|
|**3d**|Constraint satisfaction over mappings|Worst-case exponential (related to subgraph isomorphism, NP-complete)|Structure-mapping, graph matching       |

**The 3a-3b vs. 3c-3d divide:**

- **3a-3b:** Bounded combinatorial space. O(1) operations, finite state machines suffice. Pattern matching covers the space.
- **3c-3d:** Unbounded spaces. Require mechanisms beyond finite state. Pattern matching cannot precompute all cases.

### Empirical Refinement: Training-Relative Novelty

**Pilot study findings** (n=304 trials, Claude Sonnet): The predicted 3a-3b vs. 3c-3d dissociation was confirmed (Cohen's d = 0.71, p < 0.0001). However, the pattern was more nuanced than uniform 3c-3d degradation:

|Task                |Type|Accuracy|Interpretation                          |
|--------------------|----|--------|----------------------------------------|
|Concatenation       |3a  |100%    |Trivially pattern-matchable             |
|Slot-filling        |3b  |100%    |Trivially pattern-matchable             |
|Bracket depth       |3c  |100%    |Matches code-parsing patterns           |
|Pointer chasing     |3c  |100%    |Matches linked-list patterns            |
|**Recursive eval**  |3c  |**50%** |Novel operator—no cached pattern        |
|Graph isomorphism   |3d  |100%    |Small scale, learnable heuristics       |
|Rule transfer       |3d  |100%    |Simple rules inferrable from examples   |
|**Relation mapping**|3d  |**28%** |Multi-constraint—genuinely hard         |

**Refined hypothesis:** The critical boundary is not formal complexity class alone, but **training-relative novelty**:

|                        |Pattern-Matchable                              |Genuinely Novel                            |
|------------------------|-----------------------------------------------|-------------------------------------------|
|**Structure**           |Matches training distribution                  |No applicable cached pattern               |
|**LLM performance**     |High (even if formally 3c-3d)                  |Degraded                                   |
|**Examples**            |Bracket matching, pointer following, simple rules|Novel operators, multi-relational constraints|
|**Mechanism**           |Retrieval from compressed representations      |Requires online construction               |

**What this means:** LLMs have learned some recursive/relational operations from code training (bracket matching, linked-list traversal). They can apply these *learned patterns* to novel symbols. They fail when the *operation itself* is novel or when constraint satisfaction exceeds pattern-matching capacity.

**The refined prediction:** Failure occurs when:
1. The **operator/rule** is genuinely novel (not just novel symbols in familiar structure)
2. **Multiple constraints** must be satisfied simultaneously
3. The structure **doesn't map to code/text idioms** in training data

This is more precise than "3c-3d is hard"—it identifies *what makes* something hard for compression-based systems.

-----

### 3c and 3d: Unity or Dissociation?

**Original hypothesis:** 3c (recursive) and 3d (analogical) failures should co-occur because both require relational representation.

**Pilot finding:** Partial support. Both showed selective failures, but on different subtasks:
- 3c failure: recursive evaluation with novel operators
- 3d failure: relation mapping with multiple constraints

**Refined hypothesis:** 3c and 3d share the property of requiring *structure-sensitive operations*, but the specific failure mode differs:
- **3c fails** when the *recursive rule itself* is novel
- **3d fails** when *constraint space* exceeds pattern-matching capacity

Both reflect limits of compression, but in different dimensions. The unity is at the level of "requires construction beyond pattern-matching," not "identical failure patterns."

-----

**Clarification on the boundary:** The claim is not "unlimited 3c-3d vs. zero"—humans also degrade on recursive depth (Gibson, 1998). The distinction is *construction with graceful degradation* vs. *pattern-matching with hard limits*:

|                 |Embedded (humans)                                        |Non-embedded (LLMs)                                      |
|-----------------|---------------------------------------------------------|---------------------------------------------------------|
|Degradation curve|Graceful                                                 |Threshold collapse on genuinely novel structures         |
|Error structure  |Preserves recursive structure (shallower but grammatical)|Loses structural coherence when patterns don't apply     |
|Scaffolding      |External memory extends capacity                         |Helps on some tasks (suggestive interaction, needs power)|

**Operationalizing construction vs. interpolation:** Depth alone isn't the test—succeeding at depth 6 after training on 1-5 could be interpolation. The signatures:

- **Systematicity:** Novel combinations of familiar components (A[B] + C[D] → A[D]) when that combination wasn't trained
- **Error structure:** When failing, does output preserve structural coherence or collapse randomly?
- **Generalization pattern:** Does performance track training distribution boundaries (interpolation) or extend beyond (construction)?
- **Novel operator handling:** Can the system apply a genuinely new rule recursively, or only rules similar to training?

**On falsifiability:** The framework predicts *qualitative* signatures (error structure, systematicity), not just quantitative differences. The pilot study provides initial falsification tests: if the 3a-3b vs. 3c-3d dissociation had not appeared, or if novel operators showed ceiling performance, the framework would require revision. The selective failure pattern (some 3c-3d at ceiling, others degraded) refines rather than falsifies the framework—it sharpens the prediction from "formal class" to "training-relative novelty."

-----

## Embeddedness

Strong interaction requires **novelty detection**—recognizing unfamiliar against a background of familiar.

Novelty is relational. An input isn't novel in itself—it's novel *to a subject*. This requires:

1. **Persistent self** → accumulated experience ("what's familiar to me")
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

**On the five components:** These are proposed based on what seems necessary for novelty detection to matter. Whether all five are jointly necessary, have independent effects, or interact is hypothesis—not established. Partial embeddedness predictions are underspecified: would an LLM agent with strong temporal persistence and action-consequence contingency but no survival stakes show partial 3c-3d capacity? Worth testing.

**Operationalizing novelty detection:** To avoid circularity, we specify four measurable criteria independent of embeddedness:

|Criterion                     |Operationalization                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------|
|**Calibration**               |Confidence decreases appropriately for OOD inputs (Guo et al., 2017)                     |
|**Processing differentiation**|Novel inputs trigger distinct internal processing, not just lower confidence             |
|**Response systematicity**    |Novel combinations of familiar components yield appropriate outputs (Lake & Baroni, 2018)|
|**Uncertainty propagation**   |Input novelty propagates to output uncertainty rather than confident confabulation       |

**Empirical status:** These are not definitional assertions—LLM failures on these criteria are empirically documented. Calibration failures: Guo et al. (2017). Systematicity failures: Lake & Baroni (2018). Confident confabulation: extensive hallucination literature. The hypothesis that embeddedness is *necessary* for meeting these criteria remains testable.

-----

### Active Maintenance and Verification

Beyond the construction vs. pattern-matching distinction, a distinct failure mode emerges: **inability to actively maintain and verify intermediate results during computation.**

**Observed signature:** In graph isomorphism tasks, LLMs correctly compute degree sequences (e.g., both graphs yield [3,3,2,2,2]), then conclude they don't match—despite the correct computation being present in the model's own output. This is not a capability failure (the computation was performed correctly) nor a compositional failure (the subtask was pattern-matchable). It is a *verification* failure: the model does not hold what it just computed while generating subsequent tokens.

**The core problem:** Autoregressive generation flows forward token-by-token. Attention provides access to prior context, but attention is not equivalent to *active maintenance*. The distinction maps onto established cognitive architecture:

|                      |Active Maintenance                                      |Attention-Based Access                        |
|----------------------|--------------------------------------------------------|----------------------------------------------|
|**Mechanism**         |Explicit, persistent representation updated and checked |Weighted retrieval from context               |
|**Cognitive analogue**|Working memory central executive (Baddeley, 2000)       |Long-term memory retrieval                    |
|**Failure mode**      |Capacity limits, interference                           |Decay with distance, salience competition     |
|**Checking behavior** |Continuous comparison against held state                |Requires explicit re-retrieval and comparison |

**Cognitive science grounding:** Baddeley's working memory model (Baddeley & Hitch, 1974; Baddeley, 2000) distinguishes storage components (phonological loop, visuospatial sketchpad) from the central executive, which performs attentional control, monitoring, and verification. The verification failure suggests LLMs lack central executive function—they can generate and retrieve, but not actively maintain-and-check.

**Neural implementation:** The prefrontal cortex implements active maintenance through persistent neural firing that bridges temporal gaps (Funahashi, Bruce, & Goldman-Rakic, 1989; Curtis & D'Esposito, 2003). This mechanism is metabolically expensive and capacity-limited, but provides genuine *holding* of information in an active state. Transformers lack an analogous mechanism—information persists in context but is not "held" in the sense of being continuously maintained and monitored.

**Why attention alone may be insufficient (hypothesis):**

1. **Attention is competitive:** Tokens compete for attention weight; intermediate results may lose salience as generation proceeds (Vaswani et al., 2017 describe the mechanism; the salience competition follows from softmax normalization)
2. **Attention is not mandatory:** The model may attend weakly or not at all to relevant prior computation
3. **Attention is not verification:** Retrieving a value and *checking* current output against that value are distinct operations—the latter requires comparison, not just access

**Relation to self-state:** This extends the embeddedness argument. The framework argues that novelty detection requires persistent self-state *across contexts*. The verification failure suggests that even *within* a single computation, something analogous is needed: an active register that maintains intermediate results and enables continuous checking, rather than just a context window available for probabilistic retrieval.

**Relation to scaffolding findings:** The pilot study found scaffolding + framing yielded 91.1% accuracy vs. 76.8% for scaffolding alone on 3c-3d tasks. If scaffolding provides *external* working memory (explicit state tracking in the prompt), this is consistent with the active maintenance hypothesis—the scaffolding substitutes for missing internal maintenance capacity. Chain-of-thought prompting (Wei et al., 2022) and scratchpad methods (Nye et al., 2021) may succeed partly by externalizing working memory into the context where it can be attended to, rather than requiring internal active maintenance.

**Empirical predictions:**

|Prediction                                         |Operationalization                                                                              |Falsification criterion                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
|Verification < Generation accuracy                 |Same problem, two framings: "Compute X" vs. "Is this computation of X correct? [with subtle error]"|Equal or higher accuracy on verification                   |
|Verification degrades with context distance        |Errors increase when the value to check is further back in context                              |Uniform error rate regardless of distance                  |
|Explicit maintenance scaffolding helps verification|External scratchpad with "current value to check: X" reduces verification errors               |Scaffolding provides no benefit for verification           |
|Verification errors show confident confabulation   |Model concludes incorrectly with high confidence rather than expressing uncertainty             |Verification failures accompanied by calibrated uncertainty|

**Alternative explanations (must be ruled out):**

- **Training distribution:** Verification tasks may be underrepresented relative to generation tasks in training data
- **Prompt sensitivity:** Verification framing may trigger learned patterns that happen to perform worse
- **Task difficulty:** Verification may simply be harder (more cognitive load) than generation, even for humans

These alternatives are testable. If the failure is architectural (absence of active maintenance mechanism), it should persist across training interventions and prompt variations. If distributional or superficial, targeted interventions should help.

**Hypothesis status:** The verification failure pattern is *observed* and replicable. The explanation—absence of active maintenance mechanism analogous to working memory—is *hypothesis*. The framework predicts this is architectural, not merely distributional, but acknowledges that distinguishing these requires further experimentation.

-----

### Why Stakes Matter (Hypothesis)

Survival pressure creates asymmetric costs—misclassifying threat as familiar can be fatal; false alarms merely waste energy (Öhman et al., 2001). But why *different architecture* rather than just stronger optimization?

- **Phylogenetic vs. ontogenetic:** Stakes during *evolution* select for architectures; stakes during *operation* modulate which capacities are used. The claim: selection under stakes produced architecture capable of construction. LLMs weren't selected; they were optimized on symmetric loss.
- **Asymmetric vs. symmetric pressure:** Symmetric loss (prediction error) rewards compression—minimizing average error. Asymmetric loss (survival) rewards worst-case handling—novel threats must be addressed even at efficiency cost. This selects for construction as a hedge against unbounded novelty. *(Testable: compare architectures trained under symmetric vs. asymmetric loss.)*
- **On the mechanism gap:** The prediction is that asymmetric pressure produces construction-capable architecture. The *full mechanism*—why asymmetric pressure yields construction rather than just more robust pattern-matching with better tail coverage—is not yet specified. The LC-NE gating hypothesis is suggestive but incomplete. This is an honest gap.
- **Candidate architectural feature:** Gating mechanisms that switch between retrieval and construction based on novelty. The locus coeruleus-norepinephrine system modulates exploration vs. exploitation based on uncertainty (Aston-Jones & Cohen, 2005). Biological cognition gates processing mode; LLMs apply identical forward passes regardless of input novelty.
- **Broader neurochemical evidence:** The LC-NE system is one instance of a general pattern: neurochemical systems provide factorized self-state signals that compose with world-state. Serotonin (metabolic adequacy), dopamine (incentive salience), norepinephrine (arousal), cortisol (resource mobilization), and GLP-1 (appetitive intensity) appear to encode distinct dimensions that combine with environmental context for action guidance. This suggests biological intelligence implements compositional self-state abstraction—not holistic state snapshots, but factorized dimensions enabling systematic combination with world-state. See [Paper 18](papers/mind_body_neurochemistry.md) for detailed treatment. If confirmed, this provides biological evidence that compositional structure extends to internal state representation, not just external world modeling.
- **On necessity:** Stakes are the known path to construction-capable architecture. Whether alternative paths exist is open. We claim *sufficiency* with confidence; *necessity* remains hypothesis.

**Why genuinely novel structures specifically (refined hypothesis):**

- **Pattern-matchable structures:** Can be encountered in training (even if formally recursive) and handled via learned procedures. LLMs trained on code learn bracket-matching, pointer-following, etc.
- **Genuinely novel structures:** Novel operators, complex multi-relational constraints, rules unlike training distribution. Cannot be retrieved—must be constructed.

When the structure exceeds training coverage, retrieval fails—*online construction* required. The boundary is training-relative, not formal-class-relative.

**Compression vs. Generation (refined):**

|              |Compression                                           |Generation                                    |
|--------------|------------------------------------------------------|----------------------------------------------|
|**Definition**|Retrieving/interpolating within training distribution |Constructing outputs with no training coverage|
|**Operation** |Pattern-matching against learned structures           |Online construction of novel procedures       |
|**When sufficient**|Structure matches training (even if formally 3c-3d)|—                                             |
|**When fails**|—                                                     |Structure is genuinely novel                  |

**Prediction:** Compression handles trained-structure 3c-3d (bracket matching, simple analogies). Compression fails on genuinely-novel 3c-3d (novel operators, complex constraints). The distinction isn't formal class but training coverage.

**On emergent capabilities:** Some argue LLMs show discontinuous capability jumps with scale, challenging the asymptote prediction. The empirical record is contested—Schaeffer et al. (2023) argue apparent emergence often disappears with continuous metrics. The pilot study suggests some 3c-3d tasks (bracket depth, pointer chase) may be "solved" via pattern-matching from code training, appearing as emergent 3c-3d capacity but actually reflecting training coverage expansion. Whether genuine construction emerges with scale is an open empirical question—the framework predicts not, but takes contrary evidence seriously.

**On LLMs:** Within a conversation, LLMs have weak temporal persistence and action-consequence contingency. But they lack self-boundary awareness, cross-context stability, gating mechanisms, active maintenance architecture, and stakes. This predicts principled limitations on *genuinely novel* 3c-3d that scaling alone cannot overcome—hypothesis pending further empirical test. The pilot study supports this: novel operators and complex constraints show impaired performance regardless of scale.

**On in-context learning:** ICL shows within-context adaptation, including some systematic properties like inferring novel rules from examples. The pilot study found rule transfer at 100% accuracy—but for simple rules (reverse, rotate) that may be pattern-matchable. The open question: does ICL extend to genuinely novel rules with no training analogue? The framework predicts not; testing needed.

-----

## Relation to Other Frameworks

**Chollet's ARC-AGI:** Chollet (2019) also emphasizes abstraction as core to intelligence, focusing on program synthesis and skill-acquisition efficiency.

|          |APH                                                       |Chollet/ARC                                                 |
|----------|----------------------------------------------------------|------------------------------------------------------------|
|Core claim|Composition hierarchy matters; genuinely novel 3c-3d requires construction|Intelligence = skill-acquisition efficiency over novel tasks|
|Mechanism |Embeddedness → gating → construction                      |Program synthesis over core-knowledge priors                |
|Key test  |Pattern-matchable vs. genuinely novel structures          |Few-shot generalization on novel tasks                      |

**Relationship:** Compatible, not competing. ARC tasks likely probe genuinely novel 3c-3d (novel analogical mappings that don't match code patterns). Chollet's efficiency focus and APH's composition focus address different aspects. Program synthesis could be one *implementation* of construction. LLM failures on ARC despite scale are consistent with APH predictions—ARC tasks are designed to be genuinely novel.

-----

## Predictions

### Core Predictions (confirmed in pilot)

|Prediction                                                                                      |Status          |Evidence                                    |
|------------------------------------------------------------------------------------------------|----------------|--------------------------------------------|
|Composition types dissociate (3a-3b vs. 3c-3d)                                                  |**Confirmed**   |d=0.71, p<0.0001                            |
|Some 3c-3d tasks show ceiling performance (pattern-matchable)                                   |**Confirmed**   |Bracket depth, pointer chase, graph iso: 100%|
|Genuinely novel operators cause failure                                                         |**Confirmed**   |Recursive eval with novel ops: 50%          |
|Multi-constraint relational tasks cause failure                                                 |**Confirmed**   |Relation mapping: 28%                       |

### Predictions Requiring Further Testing

|Prediction                                                                                      |Status          |Next Steps                                  |
|------------------------------------------------------------------------------------------------|----------------|--------------------------------------------|
|3c and 3d failures co-occur (relational representation unity)                                   |Partial support |Both showed failures but on different subtasks; test with matched difficulty|
|Scaffolding + framing interaction improves genuinely novel 3c-3d                                |Suggestive      |Full: 91%, others: 73-79%; needs power (n=100+)|
|Recursive depth degrades when rule is novel                                                     |Untested        |Vary depth specifically for novel operators |
|Systems without stakes plateau on genuinely novel 3c-3d despite scaling                         |Hypothesis      |Test across model scales                    |
|Asymmetric loss training improves genuinely novel 3c-3d over symmetric loss                     |Hypothesis      |Requires training experiments               |
|Neurochemical modulation shows cross-domain effects, dissociations, transfer structure          |Emerging        |GLP-1 trials ongoing (see Paper 18)         |
|**Verification accuracy < Generation accuracy on matched problems**                             |**Hypothesis**  |Same problems, generation vs. verification framing|
|**Verification errors increase with context distance**                                          |**Hypothesis**  |Vary distance between computed value and check|
|**Verification errors show confident confabulation rather than calibrated uncertainty**         |**Hypothesis**  |Measure confidence on incorrect verification responses|

### Refined Predictions (from pilot findings)

|Prediction                                                                                      |Falsification                                                        |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|LLMs succeed on formally-3c-3d tasks that match code/training patterns                          |Failure on bracket matching, pointer chasing despite code training   |
|LLMs fail on genuinely novel operators even at shallow depth                                    |Success on novel operators proportional to depth (just capacity limit)|
|Multi-constraint relational problems are harder than single-constraint regardless of complexity |Single-constraint problems equally difficult                         |
|Novelty gradient: performance degrades with structural novelty, not just depth                  |Depth alone predicts difficulty; novelty doesn't add                 |
|Scaffolding helps more on genuinely novel tasks than pattern-matchable tasks                    |Scaffolding helps equally or more on pattern-matchable               |

### Distinguishing Embeddedness from Architectural Explanation

The 2x2 pilot was underpowered but suggestive:

|Condition                  |Accuracy (3c-3d)|Interpretation                              |
|---------------------------|----------------|--------------------------------------------|
|Baseline                   |78.6%           |—                                           |
|Framing only               |73.2%           |Stakes framing alone doesn't help           |
|Scaffolding only           |76.8%           |Scaffolding alone doesn't help              |
|**Full (framing+scaffold)**|**91.1%**       |Possible interaction—needs power            |

**Next step:** Replicate with n=100+ per cell to adequately power interaction detection. If interaction is real, suggests both attention (stakes) and explicit working memory (scaffolding) are needed for construction on genuinely novel tasks.

**RL agents as test case:** If embeddedness is necessary for genuinely novel 3c-3d, RL agents trained under survival-like pressure in complex environments should develop construction capacity for novel operators and complex constraints. If they don't, stakes may be necessary but not sufficient—or phylogenetic timescales may matter in ways training runs can't replicate.

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

**Extensions (11–18):**

|# |Paper                                                                                |
|--|-------------------------------------------------------------------------------------|
|11|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|
|12|[The Hard Problem Reframed](papers/hard_problem_reframed.md)                         |
|13|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |
|14|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |
|15|[Social Dynamics](papers/social_dynamics.md)                                         |
|16|[Beyond Large Language Models](papers/beyond_llms.md)                                |
|17|[Dual-Process Theory Reconsidered](papers/dual_process_abstraction.md)               |
|18|[Neurochemistry as Self-State Abstraction](papers/mind_body_neurochemistry.md)       |

**Empirical:**

|# |Paper                                                                                |
|--|-------------------------------------------------------------------------------------|
|19|[Pilot Study: Compositional Hierarchy in LLMs](papers/pilot_composition_study.md)    |

-----

## Empirical Research Program

### 🧠 Core Framework

[abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) ·
[composition-testing](https://github.com/HillaryDanan/composition-testing) ·
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

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Baddeley, A. D., & Hitch, G. (1974). Working memory. In G. H. Bower (Ed.), *The psychology of learning and motivation* (Vol. 8, pp. 47-89). Academic Press.

Chollet, F. (2019). On the measure of intelligence. *arXiv preprint arXiv:1911.01547*.

Curtis, C. E., & D'Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415-423.

Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1-63.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Funahashi, S., Bruce, C. J., & Goldman-Rakic, P. S. (1989). Mnemonic coding of visual space in the monkey's dorsolateral prefrontal cortex. *Journal of Neurophysiology*, 61(2), 331-349.

Gibson, E. (1998). Linguistic complexity: Locality of syntactic dependencies. *Cognition*, 68(1), 1-76.

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. *Proceedings of the 34th International Conference on Machine Learning (ICML)*, 1321-1330.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of the 35th International Conference on Machine Learning (ICML)*, 2873-2882.

Nye, M., Andreassen, A. J., Gur-Ari, G., Michalewski, H., Austin, J., Biber, D., ... & Odena, A. (2021). Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*.

Öhman, A., Flykt, A., & Esteves, F. (2001). Emotion drives attention: Detecting the snake in the grass. *Journal of Experimental Psychology: General*, 130(3), 466-478.

Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *Advances in Neural Information Processing Systems (NeurIPS)*, 36.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS)*, 30.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems (NeurIPS)*, 35, 24824-24837.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

*"Abstraction is all you need ;)"*

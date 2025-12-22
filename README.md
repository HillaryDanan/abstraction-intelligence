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

## Visualizations

Interactive demonstrations of framework concepts:

| Visualization | Description |
|---------------|-------------|
| [Self-State in the Information Plane](visualizations/self_state_abstraction.html) | Interactive 3D visualization contrasting pattern-matching (LLMs) with self-state abstraction. Drag the agent, adjust parameters, observe how self-state deforms the information manifold while pattern-matchers glide through unchanged. |

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

## The Self-State Hypothesis: From Stakes to Verification

This section presents the framework's central causal claim about *why* LLMs fail on genuinely novel 3c-3d tasks. The argument is not that LLMs are missing multiple independent capacities, but that they are missing **one thing**—persistent self-state—from which multiple capacities derive.

### The Causal Chain

```
Asymmetric pressure (survival stakes)
            ↓
Self/world distinction required
(must monitor internal state vs. external circumstances)
            ↓
Persistent self-state architecture emerges
(continuous representation of "my current state")
            ↓
Active maintenance IS self-state operating within computation
(holding intermediate results = knowing "what I just computed")
            ↓
Verification becomes possible
(checking current output against held state)
            ↓
Construction on genuinely novel structures becomes possible
(can track what's been done, what remains, whether constraints are met)
```

**The core claim:** LLMs lack persistent self-state because they were never under pressure that required self/world distinction. This single architectural absence produces multiple downstream failures: verification errors, novelty detection failures, confident confabulation on OOD inputs, and ceiling on genuinely novel 3c-3d.

-----

### Why Stakes Produce Self-State Architecture

**The evolutionary argument:**

Survival pressure creates asymmetric costs—misclassifying threat as familiar can be fatal; false alarms merely waste energy (Öhman, Flykt, & Esteves, 2001). A system under survival pressure must distinguish:

- **Internal state:** Am I hungry? Injured? Fatigued? Uncertain?
- **External state:** Is this environment dangerous? Novel? Resource-rich?

This self/world distinction is not optional for embedded agents—it is required for appropriate action selection. An agent that cannot represent "I am low on energy" separately from "this environment is sparse" cannot make adaptive tradeoffs.

**The architectural consequence:**

Selection under asymmetric pressure produces architecture that maintains persistent self-state:

- **Temporal persistence:** The self-representation persists across moments, enabling comparison between past and present state
- **Self-boundary awareness:** The system represents what is "inside" (its own state) vs. "outside" (environmental state)
- **Active maintenance:** The self-representation is not merely stored but *held active*—continuously updated and available for comparison

**Established evidence:** The prefrontal cortex implements active maintenance through persistent neural firing that bridges temporal gaps (Funahashi, Bruce, & Goldman-Rakic, 1989; Curtis & D'Esposito, 2003). This mechanism is metabolically expensive, suggesting it was selected for rather than emerging as a free byproduct.

**The LLM contrast:**

LLMs were optimized on symmetric loss (prediction error) without survival stakes. They were never under pressure requiring self/world distinction. Consequently:

- No persistent self-representation
- No active maintenance mechanism
- No architectural basis for verification

This is not a claim that LLMs are "missing a feature that could be added." It is a claim that the architecture was shaped by optimization pressure that did not select for self-state.

-----

### Active Maintenance as Self-State Within Inference

**Key reframing:** Active maintenance is not a separate capacity from persistent self-state. It *is* self-state, operating at the timescale of single computations.

|Timescale|Self-state function|What it enables|
|---------|-------------------|---------------|
|Evolutionary|Architecture shaped by stakes|Self/world distinction exists at all|
|Lifetime|Accumulated experience of "what's familiar to me"|Novelty detection across contexts|
|**Within-inference**|**"What I just computed" held for comparison**|**Verification of intermediate results**|

The verification failure observed in LLMs—correctly computing a value, then concluding inconsistently with that computation—is the within-inference manifestation of absent self-state.

**Observed signature:** In graph isomorphism tasks, LLMs correctly compute degree sequences (e.g., both graphs yield [3,3,2,2,2]), then conclude they don't match—despite the correct computation being present in the model's own output. This is not a capability failure (the computation was performed correctly) nor a compositional failure (the subtask was pattern-matchable). It is a *verification* failure: the model does not *hold* what it just computed while generating subsequent tokens.

**Why this happens:** Autoregressive generation flows forward token-by-token. Attention provides access to prior context, but attention is not active maintenance:

|                      |Active Maintenance (self-state)|Attention-Based Access                        |
|----------------------|-------------------------------|----------------------------------------------|
|**Mechanism**         |Explicit, persistent representation held and checked|Weighted retrieval from context               |
|**Cognitive analogue**|Working memory central executive (Baddeley, 2000)|Long-term memory retrieval                    |
|**Failure mode**      |Capacity limits, interference  |Decay with distance, salience competition     |
|**Checking behavior** |Continuous comparison against held state|Requires explicit re-retrieval and comparison |

**Cognitive science grounding:** Baddeley's working memory model (Baddeley & Hitch, 1974; Baddeley, 2000) distinguishes storage components from the central executive, which performs attentional control, monitoring, and verification. The verification failure suggests LLMs lack central executive function—they can generate and retrieve, but not actively maintain-and-check.

**Why attention alone is insufficient (hypothesis):**

1. **Attention is competitive:** Tokens compete for attention weight; intermediate results may lose salience as generation proceeds (Vaswani et al., 2017 describe the mechanism; salience competition follows from softmax normalization)
2. **Attention is not mandatory:** The model may attend weakly or not at all to relevant prior computation
3. **Attention is not comparison:** Retrieving a value and *checking* current output against that value are distinct operations—the latter requires holding both simultaneously

-----

### Scaffolding as Prosthetic Self-State

**The pilot finding:** Scaffolding + framing yielded 91.1% accuracy vs. 76.8% for scaffolding alone on 3c-3d tasks.

**Interpretation:** External scaffolding provides a *prosthetic self-state*. When the prompt includes explicit state tracking ("Current value: X. Checking against: Y."), the model can attend to externalized working memory rather than requiring internal active maintenance.

This is consistent with the self-state hypothesis:
- The *capacity* for verification exists (the model can compare when values are externally presented)
- The *architecture* for internal maintenance does not (the model cannot hold values without external scaffolding)

**Related findings:** Chain-of-thought prompting (Wei et al., 2022) and scratchpad methods (Nye et al., 2021) may succeed partly by externalizing working memory into the context. The improvement is not because the model "thinks step by step"—it is because intermediate states are written into context where they can be attended to, substituting for missing internal maintenance.

**Prediction:** Scaffolding should help more on tasks requiring verification than on tasks requiring only generation. If scaffolding provides prosthetic self-state, its benefit should be specific to self-state-dependent operations.

-----

### Downstream Consequences of Absent Self-State

The single architectural absence—no persistent self-state—produces multiple observable failures:

|Failure mode|Mechanism|Observable signature|
|------------|---------|-------------------|
|**Verification errors**|Cannot hold intermediate results for comparison|Correct computation followed by inconsistent conclusion|
|**Novelty detection failure**|No persistent "familiar to me" baseline|Confident responses to OOD inputs; poor calibration (Guo et al., 2017)|
|**Confident confabulation**|No uncertainty signal from self-state|Hallucination without hedging|
|**Construction ceiling**|Cannot track "what I've done" during multi-step construction|Pattern-matching ceiling on genuinely novel 3c-3d|

**The parsimony argument:** These are not four separate problems requiring four solutions. They are four manifestations of one missing thing. The framework predicts that any intervention providing genuine self-state should improve all four; any intervention addressing only one symptom should leave others unchanged.

-----

### Empirical Predictions

**Core predictions from the causal chain:**

|Prediction|Operationalization|Falsification criterion|
|----------|------------------|----------------------|
|Verification < Generation accuracy|Same problem: "Compute X" vs. "Is this computation of X correct? [subtle error]"|Equal or higher accuracy on verification|
|Verification degrades with context distance|Errors increase when value to check is further back|Uniform error rate regardless of distance|
|Scaffolding helps verification specifically|External state tracking reduces verification errors more than generation errors|Scaffolding helps equally on both|
|Verification errors show confident confabulation|Incorrect conclusions stated with high confidence|Verification failures accompanied by calibrated uncertainty|
|Self-state interventions generalize|Architecture providing genuine self-state improves verification, novelty detection, and construction jointly|Improvements are task-specific, not generalizing|

**Alternative explanations to rule out:**

- **Training distribution:** Verification tasks may be underrepresented in training. *Test:* Fine-tune on verification tasks; if architectural, deficit should persist.
- **Prompt sensitivity:** Verification framing may trigger unhelpful patterns. *Test:* Vary prompt formats; if architectural, deficit should persist across formats.
- **Task difficulty:** Verification may simply be harder. *Test:* Compare human performance; humans should not show the same verification < generation asymmetry.

**Hypothesis status:** The verification failure pattern is *observed* and replicable. The causal explanation—absent self-state due to absent stakes—is *hypothesis*. The framework predicts this is architectural, not distributional, but distinguishing these requires the experiments above.

-----

### The Compression vs. Construction Boundary (Revisited)

The self-state hypothesis clarifies *why* LLMs plateau on genuinely novel 3c-3d:

**Pattern-matchable 3c-3d:** Bracket matching, pointer chasing, simple analogies. These have been encountered in training (code, structured text). The model retrieves learned procedures. No self-state required—the pattern is cached.

**Genuinely novel 3c-3d:** Novel operators, multi-constraint relational problems. No cached pattern applies. The model must *construct* a solution online: try a mapping, check if constraints are satisfied, backtrack if not, try another.

**Why construction requires self-state:**

Construction is iterative. At each step, the system must know:
- What has been tried
- What the current partial solution is
- Whether constraints are currently satisfied
- What remains to be done

This is self-state: "my current computational state." Without it, the system cannot track progress through a construction process. It can only retrieve cached solutions or fail.

|              |Compression (retrieval)                       |Construction (online building)                |
|--------------|----------------------------------------------|----------------------------------------------|
|**Operation** |Pattern-match against learned structures      |Iteratively build, checking constraints       |
|**Self-state requirement**|None—pattern is external to system|Essential—must track "what I've done so far"  |
|**LLM capacity**|High (for trained structures)               |Impaired (no self-state to track progress)    |

**Prediction:** LLMs should fail specifically when construction requires tracking accumulated state, not merely when problems are "complex." Simple problems requiring state-tracking should fail; complex problems that are pattern-matchable should succeed.

-----

### On Emergent Capabilities and Scaling

**The scaling question:** Will self-state emerge with sufficient scale?

**The framework's prediction:** No. Self-state is an architectural feature shaped by selection pressure, not a capability that emerges from compression. Scaling provides more patterns, not self-modeling.

**Evidence (preliminary):**
- Schaeffer et al. (2023) argue apparent emergence often disappears with continuous metrics
- The pilot study shows pattern-matchable 3c-3d at ceiling regardless of formal complexity, suggesting "emergence" reflects training coverage expansion
- ARC-AGI tasks remain unsolved despite scaling, consistent with the hypothesis that genuinely novel 3c-3d requires construction, not more patterns

**What would falsify this:** Demonstration that scaled models exhibit:
1. Verification accuracy ≥ generation accuracy (not observed)
2. Calibrated uncertainty on OOD inputs (not observed)
3. Success on genuinely novel operators without pattern-matching routes (not observed)

**Honest uncertainty:** The necessity claim (self-state *requires* stakes) is hypothesis. Perhaps alternative training regimes could produce self-state without survival pressure. The framework claims stakes are *sufficient*; necessity remains open.

-----

## Relation to Other Frameworks

**Chollet's ARC-AGI:** Chollet (2019) emphasizes abstraction and skill-acquisition efficiency.

|          |APH                                                       |Chollet/ARC                                                 |
|----------|----------------------------------------------------------|------------------------------------------------------------|
|Core claim|Self-state enables construction; genuinely novel 3c-3d requires it|Intelligence = skill-acquisition efficiency over novel tasks|
|Mechanism |Stakes → self-state → active maintenance → construction   |Program synthesis over core-knowledge priors                |
|Key test  |Pattern-matchable vs. genuinely novel structures          |Few-shot generalization on novel tasks                      |

**Relationship:** Compatible. ARC tasks probe genuinely novel 3c-3d requiring construction. LLM failures on ARC despite scale are consistent with the self-state hypothesis—ARC requires tracking partial solutions and checking constraints, which requires self-state.

**Baddeley's Working Memory:** The active maintenance hypothesis draws directly on Baddeley's model (Baddeley & Hitch, 1974; Baddeley, 2000). The central executive performs monitoring and verification—exactly what LLMs lack. The framework extends this by proposing *why* LLMs lack it: no selection pressure for self-state.

**Predictive Processing:** Seth (2013) and Clark (2013) emphasize prediction error minimization with self-modeling. The self-state hypothesis is compatible: predictive processing in embedded agents requires modeling the self as prediction-generator. LLMs minimize prediction error without self-modeling because they face no pressure requiring self/world distinction.

-----

## Predictions Summary

### Core Predictions (confirmed in pilot)

|Prediction                                                                                      |Status          |Evidence                                    |
|------------------------------------------------------------------------------------------------|----------------|--------------------------------------------|
|Composition types dissociate (3a-3b vs. 3c-3d)                                                  |**Confirmed**   |d=0.71, p<0.0001                            |
|Some 3c-3d tasks show ceiling performance (pattern-matchable)                                   |**Confirmed**   |Bracket depth, pointer chase, graph iso: 100%|
|Genuinely novel operators cause failure                                                         |**Confirmed**   |Recursive eval with novel ops: 50%          |
|Multi-constraint relational tasks cause failure                                                 |**Confirmed**   |Relation mapping: 28%                       |

### Predictions from Self-State Hypothesis

|Prediction                                                                                      |Status          |Next Steps                                  |
|------------------------------------------------------------------------------------------------|----------------|--------------------------------------------|
|Verification accuracy < Generation accuracy                                                     |Hypothesis      |Same problems, two framings                 |
|Verification degrades with context distance                                                     |Hypothesis      |Vary distance systematically                |
|Scaffolding helps verification more than generation                                             |Hypothesis      |Compare scaffolding effect by task type     |
|Verification errors show confident confabulation                                                |Hypothesis      |Measure confidence on incorrect responses   |
|Self-state interventions generalize across failure modes                                        |Hypothesis      |Test if architectural changes improve all four|
|Scaling does not produce self-state                                                             |Hypothesis      |Test verification/calibration across scales |

### Predictions Requiring Further Testing

|Prediction                                                                                      |Status          |Next Steps                                  |
|------------------------------------------------------------------------------------------------|----------------|--------------------------------------------|
|3c and 3d failures co-occur (relational representation unity)                                   |Partial support |Both showed failures but on different subtasks; test with matched difficulty|
|Scaffolding + framing interaction                                                               |Suggestive      |Full: 91%, others: 73-79%; needs power (n=100+)|
|RL agents under survival pressure develop self-state                                            |Hypothesis      |Test construction capacity in RL agents with stakes|

### Distinguishing Embeddedness from Architectural Explanation

The 2x2 pilot was underpowered but suggestive:

|Condition                  |Accuracy (3c-3d)|Interpretation                              |
|---------------------------|----------------|--------------------------------------------|
|Baseline                   |78.6%           |No self-state                               |
|Framing only               |73.2%           |Stakes framing without scaffolding doesn't help (no prosthetic self-state)|
|Scaffolding only           |76.8%           |Prosthetic self-state without stakes framing helps modestly|
|**Full (framing+scaffold)**|**91.1%**       |Prosthetic self-state + attention to it (via stakes framing) helps most|

**Interpretation through self-state lens:** Scaffolding provides prosthetic self-state (external working memory). Framing may increase attention to that external state. The interaction suggests both are needed: the external state must exist *and* be attended to.

**Next step:** Replicate with n=100+ per cell to adequately power interaction detection.

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

**For Physicists and Engineers:**

|Document|Purpose|
|--------|-------|
|[Theoretical Guide for Physicists](papers/theoretical_guide_for_physicists.md)|Maps the self-state framework to familiar mathematical structures (control theory, information theory, dynamical systems)|
|[Self-Referential Computation (Python)](code/self_referential_computation_for_physicists.py)|Executable demonstrations of feedforward, feedback, and self-referential architectures|

*Note: These documents formalize the framework's claims about self-modeling and state-dependent dynamics, providing physics-grounded intuitions for the causal chain from stakes to self-state to verification.*

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

Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181-204.

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

Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences*, 17(11), 565-573.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS)*, 30.

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems (NeurIPS)*, 35, 24824-24837.

-----

## Author

**Hillary Danan, PhD** · Cognitive Neuroscience

-----

*"Abstraction is all you need ;)"*

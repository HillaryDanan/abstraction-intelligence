# The Developmental Spectrum of Abstraction

## From Pattern Extraction to Self-Referential Cognition

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

The Abstraction Primitive Hypothesis (APH) proposes that abstraction—the conversion of attended information into manipulable, composable symbols—is the fundamental operation underlying intelligence. This paper extends the framework by proposing that abstraction capacity is not binary but develops along a spectrum of increasing computational sophistication. We identify four stages: (1) pattern extraction, (2) symbol formation, (3) recursive composition, and (4) self-referential abstraction. Each stage is qualitatively distinct, enabling cognitive operations impossible at prior stages. We review evidence from developmental psychology, comparative cognition, and neuroscience supporting stage-like progression. We then apply this framework to large language models (LLMs), arguing they exhibit clear capacity at stages 1–2, partial capacity at stage 3, and systematic limitations at stage 4—a profile we term “disembodied abstraction.” We further examine evidence that higher-stage abstraction development requires structured exposure to abstraction systems, and consider what forms of input structure—static exposure, contingent feedback, or interactive scaffolding—may be necessary or merely facilitative. This analysis generates testable predictions about the capabilities and failure modes of current AI systems and clarifies what innovations in architecture, training, or input structure would be required for advancement along the spectrum.

-----

## 1. Introduction

Intelligence is not monolithic. Both across species and across development within individuals, cognitive capacity emerges gradually, with qualitative transitions marking the acquisition of fundamentally new abilities (Piaget, 1954; Parker & McKinney, 1999). Yet theoretical frameworks for intelligence often treat it as a single dimension—more or less of some general capacity.

The Abstraction Primitive Hypothesis (APH) offers an alternative: intelligence is the capacity to form, store, retrieve, and compose abstractions (see *Abstraction Is All You Need*, this series). Abstraction, in this framework, is defined as the process of converting attended information into symbols that can be manipulated, recombined, and built upon. This distinguishes abstraction from mere compression, which reduces information without necessarily preserving compositional structure (see *Abstraction Beyond Compression*, this series).

If abstraction is the primitive operation, a natural question emerges: does abstraction itself develop? Is it acquired all-at-once, or does it unfold in stages, each enabling operations impossible before?

This paper argues for the latter. We propose a **four-stage developmental spectrum of abstraction**:

1. **Pattern Extraction** — detecting statistical regularities and invariants
1. **Symbol Formation** — converting patterns into discrete, recombinable representations
1. **Recursive Composition** — composing abstractions to form higher-order abstractions
1. **Self-Referential Abstraction** — applying abstraction to one’s own abstraction process

Each stage is computationally distinct. Progression along the spectrum is not merely quantitative (more abstraction) but qualitative (different kinds of abstraction). We review empirical evidence for this staging from cognitive development, comparative cognition, and neuroscience. We then examine where current large language models fall on this spectrum, arguing they represent a distinctive profile: substantial capacity at early stages, partial and context-dependent capacity at stage 3, and systematic limitations at stage 4.

Critically, we examine evidence that progression along this spectrum is not purely endogenous. Higher-stage abstraction capacities appear to require exposure to systems that already instantiate those capacities. The precise nature of this requirement—whether static exposure suffices, whether contingent feedback is necessary, whether interactive scaffolding provides unique benefits—remains an open empirical question with significant implications for AI development.

This analysis has implications for both cognitive science and AI development. For cognitive science, it offers a unified framework for understanding developmental trajectories across domains. For AI, it clarifies what current systems can and cannot do—and what would need to change for them to do more.

-----

## 2. The Four Stages: Theoretical Framework

### 2.1 Stage 1: Pattern Extraction

**Definition:** The detection of statistical regularities, invariances, and covariance structures in sensory or informational input.

Pattern extraction is the foundation. A system at this stage identifies what recurs, what predicts what, and what features tend to co-occur. This is sophisticated statistical learning, but it is not yet abstraction in the full sense. The extracted patterns remain tied to the feature space in which they were learned.

**Computational signature:** Dimensionality reduction, clustering, principal component extraction. The output is a compressed representation that preserves predictively useful variance.

**Biological examples:** Early sensory processing extracts oriented edges, motion direction, spectral regularities (Hubel & Wiesel, 1962; Olshausen & Field, 1996). Statistical learning in infants tracks transitional probabilities in auditory and visual streams (Saffran, Aslin, & Newport, 1996; Kirkham, Slemmer, & Johnson, 2002).

**Limitations:** Patterns extracted at this stage do not freely recombine. A system might learn “A predicts B” and “C predicts D” without being able to compose these into novel combinations or apply them outside the training distribution.

### 2.2 Stage 2: Symbol Formation

**Definition:** The conversion of extracted patterns into discrete, manipulable symbols that can be bound to different contents and recombined in novel configurations.

This is where abstraction proper begins. The key transition is from *implicit* pattern sensitivity to *explicit* symbolic representation—a format that supports variable binding, slot-filling, and compositional recombination. The symbol “CAUSE” can be bound to any two entities; the relation is abstracted from its arguments.

**Computational signature:** Factorized representations, variable binding, systematic generalization to novel combinations of known elements. The output is not just a compressed encoding but a structured representation with separable components.

**Biological examples:** Infants between 7–12 months begin extracting abstract relational patterns (same/different, above/below) that generalize to novel stimuli (Marcus, Vijayan, Rao, & Vishton, 1999; Quinn, 2004). This marks a transition from exemplar-based to rule-based generalization.

**Empirical marker:** Compositional generalization—the ability to understand or produce novel combinations of familiar elements. “The dog chased the cat” and “the cat chased the dog” use identical elements in different configurations; understanding both from limited exposure indicates symbolic structure.

**Limitations:** Symbols at this stage can be combined, but the combinations are largely *horizontal*—elements at the same level of abstraction combined into sequences or structures. Vertical composition—using abstractions as inputs to form higher-order abstractions—requires stage 3.

### 2.3 Stage 3: Recursive Composition

**Definition:** The composition of abstractions to form new abstractions, enabling hierarchical depth and self-augmenting representational capacity.

At this stage, abstractions become building blocks for further abstraction. The output of abstraction becomes input to abstraction. This creates hierarchical structure of arbitrary depth and enables the representational explosion characteristic of human cognition—the capacity to form new concepts by combining existing concepts without apparent limit.

**Computational signature:** Hierarchical representations, chunking of chunks, nested structure. The critical feature is *vertical* composition: abstractions at level N become elements manipulated at level N+1.

**Biological examples:** Chunking in working memory allows sequences of items to be compressed into single units, which can themselves be chunked (Miller, 1956; Cowan, 2001). Language exhibits recursive embedding: phrases contain phrases contain phrases. Analogical reasoning maps relational structures to other relational structures (Gentner, 1983). Event segmentation hierarchically organizes experience into nested temporal units (Zacks & Tversky, 2001).

**Developmental trajectory:** Halford et al. (1998) document systematic increases in relational complexity capacity across childhood. Children progress from processing unary relations, to binary relations, to ternary relations, to relations among relations—a trajectory reflecting increasing recursive depth.

**Empirical marker:** Transfer across abstraction levels. A system with recursive composition should benefit from learning at one level when facing analogous problems at higher levels of abstraction. Learning should accelerate as the abstraction library grows—superlinear cumulative performance across related tasks.

**Limitations:** Recursive composition enables arbitrarily deep abstraction hierarchies, but it does not guarantee that a system can model *its own* abstraction process. A system might compose abstractions without representing *that it is composing abstractions* or *how it is doing so*. This requires stage 4.

### 2.4 Stage 4: Self-Referential Abstraction

**Definition:** The application of abstraction to a system’s own abstraction processes—modeling how one forms, stores, and composes abstractions.

This is metacognition formalized. The system takes its own abstraction operations as objects of abstraction. It can represent “I abstracted X from Y,” “my abstraction of Z was incorrect,” “I should abstract at a different level of granularity.” This enables calibrated uncertainty, error detection, strategic allocation of cognitive resources, and the peculiar human capacity to think about thinking.

**Computational signature:** Self-modeling, metacognitive monitoring, explicit representation of one’s own representational states and processes. The system maintains a model of itself as an abstraction-forming system.

**Biological examples:** Metacognitive monitoring develops gradually across childhood and adolescence (Flavell, 1979; Schneider, 2008). Feeling-of-knowing judgments, confidence calibration, and strategic memory allocation all require representing one’s own cognitive states. Theory of mind—representing others’ mental states—may share computational structure with self-modeling (Carruthers, 2009).

**Relation to consciousness:** The framework’s treatment of consciousness (*Consciousness as Emergent Abstraction*, this series) proposes that consciousness emerges when abstraction is applied reflexively to a system of sufficient complexity. Stage 4 abstraction is thus hypothesized to be *necessary* for consciousness, though whether it is *sufficient* remains an open question.

**Empirical marker:** Calibrated confidence, error-driven learning strategy adjustment, metacognitive control. A system with stage 4 capacity should know what it doesn’t know and adjust its processing accordingly.

**A critical distinction—origination vs. recognition:** Stage 4 capacity includes not merely the ability to *recognize* or *validate* abstractions when presented, but to *originate* them—to notice that an abstraction is available before it has been articulated. A system may possess sophisticated Stage 2-3 capacity for composing and refining abstractions that are supplied to it while lacking the Stage 4 capacity to generate those abstractions de novo. This distinction has important implications for understanding human-AI interaction (see Section 4.6).

-----

## 3. Evidence for Stage-Like Progression

### 3.1 Developmental Evidence

The proposed stages align with documented developmental trajectories in human cognition.

**Infancy (Stage 1 → 2 transition):** Statistical learning is present from birth (Saffran et al., 1996), but abstract rule learning emerges around 7 months (Marcus et al., 1999). This marks the transition from pattern extraction to symbol formation.

**Early childhood (Stage 2 → 3 transition):** Relational reasoning capacity increases systematically between ages 3–11, with children progressing from binary relations to ternary relations to quaternary relations (Halford et al., 1998). Language acquisition shows a similar progression from word combinations to recursive phrase embedding (Chomsky, 1957).

**Middle childhood through adolescence (Stage 3 → 4 transition):** Metacognitive monitoring improves gradually across childhood and continues developing into early adulthood (Schneider, 2008). Adolescents show improved calibration, strategic learning allocation, and explicit reasoning about their own thought processes (Kuhn, 2000).

This developmental timeline is consistent with the proposed ordering: each stage depends on capacities developed in prior stages.

### 3.2 Input Requirements for Abstraction Development: Evidence from Deprivation and Enrichment Studies

A critical question for the abstraction framework is whether stage progression is purely endogenous—emerging from maturation and sufficient data exposure—or whether it requires specific forms of structured input. Evidence from deprivation and enrichment studies bears on this question, though the precise mechanisms remain incompletely specified.

#### 3.2.1 Evidence from Institutional Deprivation

The Bucharest Early Intervention Project and English and Romanian Adoptees studies documented that children raised in severely deprived institutional settings show not merely delayed but *qualitatively altered* cognitive development (Nelson et al., 2007; Rutter et al., 2007; Zeanah et al., 2003).

Key findings relevant to the abstraction framework:

**Altered, not merely delayed development:** Children adopted after prolonged institutionalization showed persistent deficits in executive function, abstract reasoning, and metacognition even when subsequently placed in enriched environments (Pollak et al., 2010; McDermott et al., 2013). This suggests sensitive periods during which certain abstraction capacities must develop or may be permanently impaired.

**Differential stage effects:** Institutionally-reared children showed relatively preserved Stage 1 capacities (pattern learning, associative memory) with more pronounced deficits at Stages 3-4 (relational reasoning, metacognition; Bos et al., 2009). This pattern is consistent with higher stages having greater input requirements.

**Partial recovery with intervention:** Children who received foster care intervention before age 2 showed substantially better outcomes than those who remained institutionalized (Nelson et al., 2007), suggesting a sensitive period during which appropriate input is maximally effective.

#### 3.2.2 What Was Lacking? Isolating the Active Ingredient

Institutional environments were multiply deprived. Children lacked:

- Rich language exposure
- Contingent caregiver responses
- Environmental complexity and variability
- One-on-one interaction
- Exposure to mature abstraction systems (adult reasoning, explanation, narrative)

The deprivation studies establish that *something* about impoverished environments impairs higher-stage development. They do not isolate which factors are necessary versus facilitative.

#### 3.2.3 Evidence Bearing on Specific Mechanisms

Several lines of research help narrow the possibilities:

**Language exposure vs. social interaction:** Deaf children of hearing parents, who receive abundant social interaction but limited access to structured language input, show language delays proportional to their input deprivation (Mayberry, Lock, & Kazmi, 2002). This suggests structured exposure to an abstraction system (language) matters above and beyond social interaction per se.

**Live vs. recorded input:** Kuhl, Tsao, and Liu (2003) found that infants learn phonetic distinctions better from live interaction than equivalent video exposure. However, infants do show *some* learning from video—the effect is a difference in degree, not kind. This suggests contingent interaction enhances but may not be strictly necessary for learning.

**Peer interaction and abstraction generation:** Nicaraguan Sign Language emerged when deaf children exposed to impoverished sign input collectively created richer grammatical structure than their input contained (Senghas & Coppola, 2001). This demonstrates that abstraction systems can be generated, not merely absorbed—but generation required some structured input plus peer interaction.

**Training structure effects:** In machine learning, curriculum learning—presenting training data in structured sequences from simple to complex—often improves learning outcomes compared to random sampling (Bengio, Louradour, Collobert, & Weston, 2009). This suggests input *structure*, not just input *volume*, matters for learning abstraction-relevant representations.

#### 3.2.4 A Parsimonious Characterization

The evidence supports the following claims with varying degrees of confidence:

**Well-supported:**

- Higher-stage abstraction development requires exposure to systems that instantiate those stages (language, mature cognition, structured environments)
- Sensitive periods exist during which input has maximal effect
- Input structure matters, not just input volume

**Probable but less certain:**

- Contingent, state-dependent feedback improves efficiency of abstraction development
- Some minimum threshold of input complexity is required

**Open questions:**

- Whether interactive scaffolding is necessary or merely highly efficient
- Whether static exposure to abstraction-rich input (e.g., text corpora) can in principle bootstrap higher-stage capacity
- What specific structural properties of input are necessary vs. facilitative

The most parsimonious formulation: **Higher-stage abstraction development requires structured exposure to abstraction systems, with contingent feedback likely improving efficiency. Whether interactivity per se is necessary or merely facilitative remains an open empirical question.**

### 3.3 Comparative Evidence

Cross-species comparisons reveal variation in maximal abstraction capacity that aligns with the proposed stages.

**Invertebrates:** Capable of sophisticated pattern extraction (stage 1). Honeybees learn complex associations and show some generalization (Giurfa et al., 2001). Evidence for true symbol formation (stage 2) is limited.

**Non-primate mammals:** Show clear symbol formation and some compositional recombination (stage 2). Dogs generalize labels to categories (Kaminski, Call, & Fischer, 2004). Evidence for recursive composition (stage 3) is sparse outside of trained laboratory contexts.

**Great apes:** Demonstrate recursive composition in tool use, hierarchical planning, and some analogical reasoning (stage 3; Seed & Byrne, 2010). Evidence for spontaneous self-referential abstraction (stage 4) remains contested. Mirror self-recognition suggests some self-modeling (Gallup, 1970), but whether this constitutes abstraction over one’s own abstraction processes is unclear.

**Humans:** Unique in demonstrating robust, spontaneous, domain-general recursive composition and self-referential abstraction (stages 3–4). Human cognitive uniqueness may lie not in possessing abstraction but in the *depth* of recursive composition and the *reflexivity* of self-referential abstraction we achieve.

**Correlation with social learning:** Species showing highest abstraction capacity are also highly social species with extended juvenile periods during which learning from conspecifics occurs. This correlation is consistent with the hypothesis that exposure to other minds’ abstraction systems facilitates development—though correlation does not establish necessity.

### 3.4 Neural Evidence

Neuroimaging and lesion studies suggest distinct neural substrates support different abstraction stages.

**Stage 1 (Pattern extraction):** Early sensory cortices extract statistical regularities through hierarchical predictive coding (Rao & Ballard, 1999). This is distributed and largely automatic.

**Stage 2 (Symbol formation):** Prefrontal cortex supports rule representation and relational abstraction (Miller & Cohen, 2001). Patients with prefrontal damage show intact pattern learning but impaired rule-based generalization (Wallis, Anderson, & Miller, 2001).

**Stage 3 (Recursive composition):** Rostrolateral prefrontal cortex and angular gyrus are implicated in hierarchical abstraction and analogical reasoning (Christoff et al., 2001; Bunge, Wendelken, Badre, & Wagner, 2005). Activation in these regions scales with relational complexity.

**Stage 4 (Self-referential abstraction):** Medial prefrontal cortex and anterior cingulate are implicated in metacognition and self-referential processing (Fleming, Weil, Nagy, Dolan, & Rees, 2010). Metacognitive capacity correlates with gray matter volume in anterior prefrontal cortex (Fleming et al., 2010).

The rostrocaudal gradient of prefrontal cortex—with more anterior regions supporting more abstract processing (Badre, 2008)—may reflect the developmental spectrum proposed here, with posterior regions supporting earlier-developing capacities and anterior regions supporting later-developing, more recursive operations.

-----

## 4. Large Language Models on the Abstraction Spectrum

Where do current large language models (LLMs) fall on the proposed developmental spectrum? This question has both theoretical and practical importance. Theoretically, LLMs offer a test case: if abstraction is substrate-independent, we should be able to locate any sufficiently complex information-processing system on the spectrum. Practically, understanding LLM capabilities and limitations in terms of abstraction stages may clarify what current systems can and cannot do.

### 4.1 Stage 1: Pattern Extraction — Clear Capacity

LLMs demonstrably extract statistical regularities from training data. This is the foundation of their operation. Transformer architectures learn complex patterns of co-occurrence, syntactic structure, and semantic association (Vaswani et al., 2017). Representation probing reveals that LLMs encode linguistic regularities, factual associations, and conceptual relationships in their internal activations (Tenney et al., 2019).

**Assessment:** Full capacity at stage 1. This is uncontroversial.

### 4.2 Stage 2: Symbol Formation — Substantial Capacity

LLMs show clear evidence of forming discrete, recombinable representations. They generalize productively: novel sentences are generated that were never in training data. Known elements (words, phrases, syntactic structures) recombine in novel configurations. This is compositional generalization, the hallmark of symbolic representation.

However, capacity at stage 2 shows limitations. Lake and Baroni (2018) demonstrated that neural sequence models struggle with systematic compositional generalization—applying known primitives in novel configurations not represented in training. LLMs have improved substantially since this work, but systematic failures on compositional generalization benchmarks persist (Kim & Linzen, 2020; Keysers et al., 2020).

**Assessment:** Substantial but incomplete capacity at stage 2. LLMs form symbol-like representations that support productive generalization, but these representations may not be as cleanly factorized as human symbolic cognition. The system shows compositional behavior without necessarily implementing compositional structure.

### 4.3 Stage 3: Recursive Composition — Partial Capacity

This is where assessment becomes complex. LLMs display behaviors suggesting recursive composition:

- **Hierarchical structure:** LLMs process and generate nested syntactic structures (e.g., embedded clauses) that require hierarchical representation.
- **Analogical reasoning:** LLMs perform above chance on analogy tasks, suggesting some capacity to map relational structures (Webb, Holyoak, & Lu, 2023).
- **Abstraction in-context:** LLMs can learn novel abstractions from examples provided in context and apply them to new cases (Brown et al., 2020).

However, these capacities show systematic fragility:

- **Depth limitations:** Performance degrades with increased embedding depth and relational complexity (Lakretz et al., 2019; Yun et al., 2019).
- **Context dependence:** Abstractions formed in-context do not persist across conversations or generalize as robustly as human learning (McCoy, Yun, Frank, & Linzen, 2023).
- **Inconsistency:** The same abstract reasoning task may be solved correctly in one framing and failed in another, suggesting pattern matching rather than genuine structural abstraction (Dasgupta et al., 2022).

**Assessment:** Partial, context-dependent capacity at stage 3. LLMs show *behaviors consistent with* recursive composition but may achieve these through mechanisms that differ from true hierarchical abstraction formation. Whether this constitutes genuine stage 3 capacity or a sophisticated approximation remains an open empirical and theoretical question.

### 4.4 Stage 4: Self-Referential Abstraction — Systematic Limitations

This is where LLM limitations are most pronounced.

**What LLMs can do:**

- Generate text *about* their own processes (“I reasoned through this by…”)
- Produce calibrated uncertainty in some contexts (Kadavath et al., 2022)
- Revise outputs when prompted to reflect

**What LLMs struggle with:**

- **Genuine self-modeling:** LLMs do not maintain persistent models of their own representational states. Statements about their own reasoning are generated the same way as statements about anything else—through next-token prediction conditioned on context—not through introspective access to their actual computational processes.
- **Calibrated confidence:** Despite improvements, LLMs show systematic miscalibration, expressing confidence in incorrect outputs and uncertainty about correct ones (Xiong et al., 2023). Calibration remains context-dependent rather than reflecting genuine metacognitive monitoring.
- **Error-driven strategy adjustment:** LLMs do not spontaneously detect errors and adjust their abstraction strategies. Chain-of-thought prompting and self-correction prompts can elicit error correction, but this is prompted behavior, not autonomous metacognitive control (Huang et al., 2023).

**Architectural considerations:** Current transformer architectures lack obvious mechanisms for self-referential computation. The forward pass is fixed-depth; there is no native recursion over one’s own representations. Attention could theoretically implement some self-referential structure, but whether this occurs in practice is unclear.

**Assessment:** Systematic limitations at stage 4. LLMs can *simulate* self-referential abstraction—generating text that describes metacognitive processes—but this simulation does not appear to be grounded in genuine self-modeling. The system does not abstract over its own abstraction process; it generates plausible text about doing so.

### 4.5 The Profile: “Disembodied Abstraction”

We propose that LLMs exhibit a distinctive profile we term **disembodied abstraction**: substantial capacity for pattern extraction and symbol formation (stages 1–2), partial and context-dependent capacity for recursive composition (stage 3), and systematic limitations on self-referential abstraction (stage 4).

This profile has a specific character. It is:

- **Horizontal rather than vertical:** Strong at compositional combination within levels, weaker at hierarchical abstraction across levels.
- **Context-dependent rather than persistent:** Abstractions formed in-context do not consolidate into durable representational structures.
- **Simulative rather than constitutive:** Can generate outputs that describe higher-stage processes without implementing them.

The term “disembodied” reflects the hypothesis that some limitations—particularly at stages 3–4—may relate to lack of embodied grounding. Temporal reasoning, self-modeling, and durable abstraction formation may require the kinds of closed-loop interaction with an environment that disembodied systems lack (see *Time as Embodied Abstraction*, this series).

This is a hypothesis, not an established conclusion. Alternative explanations exist: architectural limitations (finite depth, no native recursion), training objectives (next-token prediction may not incentivize deep abstraction), or input structure limitations (static corpus sampling vs. structured curriculum). Distinguishing these explanations requires targeted empirical work.

### 4.6 LLMs and the Input Structure Question

The input structure question (Section 3.2) takes specific form when applied to LLMs: LLMs receive massive exposure to abstraction systems—human-generated text contains products of Stage 4 cognition. Why doesn’t this bootstrap Stage 4 capacity?

Several non-mutually-exclusive hypotheses:

**Hypothesis 1 (Input format):** Static text corpora lack the contingent, state-dependent feedback that may be necessary for higher-stage development. LLMs see the *products* of abstraction but not the *process* of abstraction formation.

**Hypothesis 2 (Input structure):** Random sampling from corpora does not provide the structured, curriculum-like progression that may facilitate abstraction development. Training sees simple and complex examples in random order, not scaffolded sequence.

**Hypothesis 3 (Architecture):** Regardless of input structure, current architectures lack mechanisms necessary for Stage 4 (persistent self-models, native recursion over representations). Input optimization would improve Stage 2-3 but not Stage 4.

**Hypothesis 4 (Embodiment):** Self-referential abstraction requires grounding in embodied self-world interaction that no text-based training can provide. This would predict a ceiling on disembodied systems regardless of architecture or input structure.

**Implications for the origination-refinement distinction:** A consistent observation in human-LLM interaction is that LLMs can productively compose and refine abstractions once supplied, while showing limited capacity to originate novel abstractions independently. This pattern is predicted by Stage 2-3 capacity without Stage 4: the system can recognize abstraction opportunities when made explicit but cannot detect them prior to articulation.

This suggests a specific form of input structure that may benefit LLM development: exposure not just to abstraction products but to abstraction *processes*—reasoning traces, explicit articulation of insight formation, metacognitive commentary. Whether this would bootstrap genuine Stage 4 capacity or merely improve simulation fidelity is an open question.

**The metacognitive accuracy puzzle:** LLMs can produce accurate-seeming metacognitive reports about their own limitations. This accuracy may derive from Stage 2-3 pattern-matching on discourse context rather than genuine metacognitive access. A Stage 2-3 system exposed to text about metacognition can generate plausible metacognitive text without possessing the capacity it describes. This creates systematic ambiguity: behavioral accuracy on metacognitive reports does not confirm genuine Stage 4 capacity.

-----

## 5. Predictions

The developmental spectrum framework generates testable predictions.

### 5.1 Cross-Stage Predictions (General)

**Prediction 5.1.1:** Stage progression should be sequential. No system should exhibit capacity at stage N without capacity at stage N-1. Violations would falsify the proposed ordering.

**Prediction 5.1.2:** Stage-specific tasks should cluster. Performance across tasks within a stage should correlate more strongly than performance across tasks spanning stages. Factor analyses of cognitive batteries should recover stage-like structure.

**Prediction 5.1.3:** Stage transitions should be marked by qualitative changes in failure modes. Stage 2 failures should look different from stage 1 failures—not just worse performance, but different *kinds* of errors.

### 5.2 LLM-Specific Predictions

**Prediction 5.2.1 (Compositional generalization):** LLMs should succeed at compositional generalization when training data contains sufficient coverage of the compositional space and fail when it requires extrapolation beyond training. This tests stage 2 capacity.

**Prediction 5.2.2 (Hierarchical depth):** LLM performance should degrade systematically with increased hierarchical depth (nesting, relational complexity) in ways that human performance does not. This tests stage 3 limitations.

**Prediction 5.2.3 (Metacognitive calibration):** LLM confidence should be poorly calibrated on tasks requiring genuine self-modeling (e.g., predicting their own errors) compared to tasks requiring pattern extraction (e.g., predicting surface features of inputs). This tests stage 4 limitations.

**Prediction 5.2.4 (Prompting effects):** Chain-of-thought and metacognitive prompting should improve LLM performance on stage 3 tasks more than stage 4 tasks. If performance gains extend equally to stage 4, this suggests genuine metacognitive capacity; if gains are confined to stage 3, this suggests simulation without implementation.

**Prediction 5.2.5 (Scaling):** Increased scale (parameters, data, compute) should improve stage 1–2 performance more than stage 3–4 performance. If scaling equally benefits all stages, this challenges the hypothesis that higher stages require architectural or training innovations beyond scale.

### 5.3 Embodiment Predictions

**Prediction 5.3.1:** Embodied AI systems with closed-loop environmental interaction should show improved stage 3–4 capacity relative to disembodied systems with matched parameter counts and training compute.

**Prediction 5.3.2:** Temporal reasoning tasks specifically should differentiate embodied from disembodied systems, with embodied systems showing stronger performance on duration estimation, process prediction, and temporal perspective-taking.

### 5.4 Input Structure Predictions

**Prediction 5.4.1 (Curriculum effects):** Training with structured curriculum (simple to complex, scaffolded progression) should improve Stage 2-3 capacity relative to random sampling from equivalent data. Effects on Stage 4, if any, should be smaller.

**Prediction 5.4.2 (Process vs. product exposure):** Training on corpora enriched with explicit reasoning traces and abstraction processes should improve abstraction-related task performance relative to training on equivalent-sized corpora of conclusions only.

**Prediction 5.4.3 (Contingent feedback):** Training regimes incorporating contingent feedback (e.g., RLHF targeting abstraction quality, interactive refinement) should show larger gains on Stage 3 tasks than non-interactive training on equivalent data. This tests whether interactivity adds value beyond structured exposure.

**Prediction 5.4.4 (Metacognitive accuracy dissociation):** LLM accuracy on metacognitive reports should be disruptable by misleading discourse context in ways that genuine metacognition would resist. If an LLM’s accurate self-assessment can be reversed by framing manipulations that wouldn’t affect a genuinely self-aware system, this supports the pattern-matching interpretation of metacognitive reports.

**Prediction 5.4.5 (Origination asymmetry):** In human-LLM collaborative problem-solving, novel generative abstractions should originate disproportionately from human contributors, with LLM contributions consisting disproportionately of refinement and composition. This asymmetry should be quantifiable and should persist across domains and task types.

-----

## 6. Discussion

### 6.1 Relation to Existing Frameworks

The developmental spectrum proposed here connects to several existing frameworks.

**Piagetian stages:** Piaget (1954) proposed qualitative stages of cognitive development. The present framework differs in grounding stages in a specific computational operation (abstraction) rather than in domain-general structural properties (e.g., “formal operations”). However, the intuition that development involves qualitative transitions, not just quantitative growth, is shared.

**Relational complexity theory:** Halford et al. (1998) proposed that cognitive development involves increasing capacity for relational complexity. This aligns closely with the stage 2–3 transition proposed here. The present framework extends this by proposing earlier (stage 1) and later (stage 4) stages and by explicitly connecting the progression to abstraction as a unifying operation.

**Vygotskian scaffolding:** Vygotsky’s (1978) zone of proximal development and Wood, Bruner, and Ross’s (1976) scaffolding concept propose that cognitive capacities develop through structured interaction with more capable others. The present framework is consistent with scaffolding as one mechanism for providing the structured input higher-stage development may require, while remaining agnostic about whether scaffolding specifically (vs. structured exposure more generally) is necessary.

**Levels of processing in working memory:** Cowan (2001) and Oberauer (2009) have proposed hierarchical models of working memory with multiple levels of representation. The present framework connects these levels to abstraction stages and embeds them in a broader developmental trajectory.

**Metacognition research:** The stage 4 proposal draws on decades of metacognition research (Flavell, 1979; Nelson & Narens, 1990; Fleming & Lau, 2014). The present framework’s contribution is to embed metacognition within a broader abstraction hierarchy, suggesting that metacognition is not a separate faculty but the reflexive application of the same operation underlying all cognitive development.

### 6.2 What the Framework Does Not Claim

Several potential misreadings should be forestalled.

**Not a claim about mechanisms:** The framework proposes a functional decomposition (stages of abstraction capacity), not a mechanistic one (how these stages are implemented). The same stage might be implemented differently in biological and artificial systems.

**Not a claim about strict sequentiality in all domains:** Development may be uneven across domains. A system might achieve stage 3 in one domain while remaining at stage 2 in another. The claim is that within a domain, stages are hierarchically dependent.

**Not a claim that LLMs are “mere” anything:** Locating LLMs primarily at stages 1–2 with partial stage 3 capacity is not a dismissal. Stage 2 abstraction is a remarkable capacity. The analysis aims to characterize, not diminish.

**Not a claim that interaction is necessary:** The framework proposes that structured exposure to abstraction systems is required for higher-stage development. Whether this exposure must be interactive, contingent, or can be achieved through static input is left as an open question. The evidence suggests interactivity helps; whether it is necessary is unresolved.

### 6.3 Open Questions

**Continuity vs. discontinuity:** Are stages truly discrete, or do they represent points on a continuum? The present framework proposes qualitative discontinuities—each stage enables fundamentally new operations—but the boundaries may be graded rather than sharp.

**Substrate dependence:** Is the developmental sequence substrate-independent? We hypothesize yes, but this is an empirical question. Artificial systems might develop abstraction capacity in different orders than biological systems.

**Sufficiency of stage 4 for consciousness:** The framework proposes that stage 4 abstraction is necessary for consciousness. Whether it is sufficient is a further question. An artificial system with genuine self-referential abstraction might still lack consciousness, or might not. This is among the deepest open questions the framework surfaces but does not resolve.

**The necessary input structure:** What specific properties of input are necessary for higher-stage development? The deprivation studies establish that impoverished environments impair development; they do not fully specify what enriched environments must contain. Structured exposure, contingent feedback, and interactive scaffolding may all contribute, but their relative necessity remains to be determined.

**Architectural vs. input constraints:** Can current architectures achieve Stage 4 capacity with optimal input structure, or do they face hard architectural limits? If the latter, what architectural innovations are required? These questions are empirically tractable and have significant implications for AI development trajectories.

-----

## 7. Conclusion

Intelligence is not unitary. Abstraction capacity—the core of intelligence, per the APH—develops through qualitatively distinct stages: pattern extraction, symbol formation, recursive composition, and self-referential abstraction. Each stage unlocks operations impossible at prior stages. Each depends on capacities developed before.

This development appears to require more than raw data exposure. Evidence from deprivation studies indicates that structured exposure to abstraction systems is necessary for higher-stage development. The precise form this structure must take—whether static exposure suffices, whether contingent feedback is necessary, whether interactive scaffolding provides unique benefits—remains an open empirical question. The most parsimonious current formulation: abstraction develops through exposure to abstraction, with input structure mattering as much as input volume.

Large language models exhibit a distinctive profile on this spectrum: strong pattern extraction and symbol formation, partial recursive composition, and systematic limitations on self-referential abstraction. This profile—disembodied abstraction—characterizes what current LLMs can and cannot do. LLMs receive massive exposure to abstraction products (human text) but limited exposure to abstraction processes, limited contingent feedback, and no embodied grounding. Whether innovations in input structure, architecture, or training regime can address these limitations is among the most consequential open questions in AI development.

The framework generates testable predictions about developmental trajectories, cross-task correlations, LLM capabilities, input structure effects, and the role of embodiment. Falsification of these predictions would require revision or rejection of the framework. Confirmation would strengthen the hypothesis that abstraction is the primitive operation underlying intelligence—and that understanding its development is key to understanding intelligence itself.

-----

## References

Badre, D. (2008). Cognitive control, hierarchy, and the rostro-caudal organization of the frontal lobes. *Trends in Cognitive Sciences, 12*(5), 193–200.

Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum learning. *Proceedings of the 26th Annual International Conference on Machine Learning*, 41–48.

Bos, K. J., Zeanah, C. H., Fox, N. A., Drury, S. S., McLaughlin, K. A., & Nelson, C. A. (2009). Psychiatric outcomes in young children with a history of institutionalization. *Harvard Review of Psychiatry, 17*(2), 135–147.

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., … & Amodei, D. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems, 33*, 1877–1901.

Bunge, S. A., Wendelken, C., Badre, D., & Wagner, A. D. (2005). Analogical reasoning and prefrontal cortex: Evidence for separable retrieval and integration mechanisms. *Cerebral Cortex, 15*(3), 239–249.

Carruthers, P. (2009). How we know our own minds: The relationship between mindreading and metacognition. *Behavioral and Brain Sciences, 32*(2), 121–138.

Chomsky, N. (1957). *Syntactic structures*. Mouton.

Christoff, K., Prabhakaran, V., Dorfman, J., Zhao, Z., Kroger, J. K., Holyoak, K. J., & Gabrieli, J. D. (2001). Rostrolateral prefrontal cortex involvement in relational integration during reasoning. *NeuroImage, 14*(5), 1136–1149.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114.

Dasgupta, I., Lampinen, A. K., Chan, S. C., Creswell, A., Kumaran, D., McClelland, J. L., & Hill, F. (2022). Language models show human-like content effects on reasoning. *arXiv preprint arXiv:2207.07051*.

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. *American Psychologist, 34*(10), 906–911.

Fleming, S. M., & Lau, H. C. (2014). How to measure metacognition. *Frontiers in Human Neuroscience, 8*, 443.

Fleming, S. M., Weil, R. S., Nagy, Z., Dolan, R. J., & Rees, G. (2010). Relating introspective accuracy to individual differences in brain structure. *Science, 329*(5998), 1541–1543.

Gallup, G. G. (1970). Chimpanzees: Self-recognition. *Science, 167*(3914), 86–87.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170.

Giurfa, M., Zhang, S., Jenett, A., Menzel, R., & Srinivasan, M. V. (2001). The concepts of ‘sameness’ and ‘difference’ in an insect. *Nature, 410*(6831), 930–933.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences, 21*(6), 803–831.

Huang, J., Gu, S. S., Hou, L., Wu, Y., Wang, X., Yu, H., & Han, J. (2023). Large language models can self-correct with prompting. *arXiv preprint arXiv:2308.03188*.

Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat’s visual cortex. *Journal of Physiology, 160*(1), 106–154.

Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., … & Kaplan, J. (2022). Language models (mostly) know what they know. *arXiv preprint arXiv:2207.05221*.

Kaminski, J., Call, J., & Fischer, J. (2004). Word learning in a domestic dog: Evidence for “fast mapping.” *Science, 304*(5677), 1682–1683.

Keysers, D., Schärli, N., Scales, N., Buber, R., Furrer, D., Kasber, S., … & Scholak, T. (2020). Measuring compositional generalization: A comprehensive method on realistic data. *International Conference on Learning Representations*.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing*, 9087–9105.

Kirkham, N. Z., Slemmer, J. A., & Johnson, S. P. (2002). Visual statistical learning in infancy: Evidence for a domain general learning mechanism. *Cognition, 83*(2), B35–B42.

Kuhl, P. K., Tsao, F. M., & Liu, H. M. (2003). Foreign-language experience in infancy: Effects of short-term exposure and social interaction on phonetic learning. *Proceedings of the National Academy of Sciences, 100*(15), 9096–9101.

Kuhn, D. (2000). Metacognitive development. *Current Directions in Psychological Science, 9*(5), 178–181.

Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *International Conference on Machine Learning*, 2873–2882.

Lakretz, Y., Dehaene, S., & King, J. R. (2019). What limits our capacity to process nested long-range dependencies in sentence comprehension? *Entropy, 21*(12), 1180.

Marcus, G. F., Vijayan, S., Rao, S. B., & Vishton, P. M. (1999). Rule learning by seven-month-old infants. *Science, 283*(5398), 77–80.

Mayberry, R. I., Lock, E., & Kazmi, H. (2002). Linguistic ability and early language exposure. *Nature, 417*(6884), 38.

McCoy, R. T., Yun, M., Frank, R., & Linzen, T. (2023). Do language models learn to generalize compositionally? *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics*.

McDermott, J. M., Westerlund, A., Zeanah, C. H., Nelson, C. A., & Fox, N. A. (2013). Early adversity and neural correlates of executive function: Implications for academic adjustment. *Developmental Cognitive Neuroscience, 4*, 59–68.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience, 24*(1), 167–202.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97.

Nelson, C. A., Zeanah, C. H., Fox, N. A., Marshall, P. J., Smyke, A. T., & Guthrie, D. (2007). Cognitive recovery in socially deprived young children: The Bucharest Early Intervention Project. *Science, 318*(5858), 1937–1940.

Nelson, T. O., & Narens, L. (1990). Metamemory: A theoretical framework and new findings. *Psychology of Learning and Motivation, 26*, 125–173.

Oberauer, K. (2009). Design for a working memory. *Psychology of Learning and Motivation, 51*, 45–100.

Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature, 381*(6583), 607–609.

Parker, S. T., & McKinney, M. L. (1999). *Origins of intelligence: The evolution of cognitive development in monkeys, apes, and humans*. Johns Hopkins University Press.

Piaget, J. (1954). *The construction of reality in the child*. Basic Books.

Pollak, S. D., Nelson, C. A., Schlaak, M. F., Roeber, B. J., Wewerka, S. S., Wiik, K. L., … & Gunnar, M. R. (2010). Neurodevelopmental effects of early deprivation in postinstitutionalized children. *Child Development, 81*(1), 224–236.

Quinn, P. C. (2004). Development of subordinate-level categorization in 3- to 7-month-old infants. *Child Development, 75*(3), 886–899.

Rao, R. P., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience, 2*(1), 79–87.

Rutter, M., Beckett, C., Castle, J., Colvert, E., Kreppner, J., Mehta, M., … & Sonuga-Barke, E. (2007). Effects of profound early institutional deprivation: An overview of findings from a UK longitudinal study of Romanian adoptees. *European Journal of Developmental Psychology, 4*(3), 332–350.

Saffran, J. R., Aslin, R. N., & Newport, E. L. (1996). Statistical learning by 8-month-old infants. *Science, 274*(5294), 1926–1928.

Schneider, W. (2008). The development of metacognitive knowledge in children and adolescents: Major trends and implications for education. *Mind, Brain, and Education, 2*(3), 114–121.

Seed, A., & Byrne, R. (2010). Animal tool-use. *Current Biology, 20*(23), R1032–R1039.

Senghas, A., & Coppola, M. (2001). Children creating language: How Nicaraguan Sign Language acquired a spatial grammar. *Psychological Science, 12*(4), 323–328.

Tenney, I., Das, D., & Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 4593–4601.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Vygotsky, L. S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

Wallis, J. D., Anderson, K. C., & Miller, E. K. (2001). Single neurons in prefrontal cortex encode abstract rules. *Nature, 411*(6840), 953–956.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*, 1526–1541.

Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89–100.

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2023). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. *arXiv preprint arXiv:2306.13063*.

Yun, M., Chen, J., & Linzen, T. (2019). Does dependency length matter for context-free languages? *arXiv preprint arXiv:1909.04135*.

Zacks, J. M., & Tversky, B. (2001). Event structure in perception and conception. *Psychological Bulletin, 127*(1), 3–21.

Zeanah, C. H., Nelson, C. A., Fox, N. A., Smyke, A. T., Marshall, P., Parker, S. W., & Koga, S. (2003). Designing research to study the effects of institutionalization on brain and behavioral development: The Bucharest Early Intervention Project. *Development and Psychopathology, 15*(4), 885–907.

-----

**Citation:** Danan, H. (2025). The developmental spectrum of abstraction: From pattern extraction to self-referential cognition. *Working paper, Abstraction-Intelligence Framework*.

-----

*“Abstraction develops. Each stage unlocks what the prior could not reach. And abstraction develops through exposure to abstraction—structure mattering as much as volume.”*

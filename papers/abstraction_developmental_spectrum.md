# The Developmental Spectrum of Abstraction

## From Pattern Extraction to Self-Referential Cognition

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

The Abstraction Primitive Hypothesis (APH) proposes that abstraction—the conversion of attended information into manipulable, composable symbols—is the fundamental operation underlying intelligence. This paper extends the framework by proposing that abstraction capacity is not binary but develops along a spectrum of increasing computational sophistication. We identify four stages: (1) pattern extraction, (2) symbol formation, (3) recursive composition, and (4) self-referential abstraction. Each stage is qualitatively distinct, enabling cognitive operations impossible at prior stages. We review evidence from developmental psychology, comparative cognition, and neuroscience supporting stage-like progression. We then apply this framework to large language models (LLMs), arguing they exhibit clear capacity at stages 1–2, partial capacity at stage 3, and systematic limitations at stage 4—a profile we term “disembodied abstraction.” This analysis generates testable predictions about the capabilities and failure modes of current AI systems and clarifies what architectural or training innovations would be required for advancement along the spectrum.

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

-----

## 3. Evidence for Stage-Like Progression

### 3.1 Developmental Evidence

The proposed stages align with documented developmental trajectories in human cognition.

**Infancy (Stage 1 → 2 transition):** Statistical learning is present from birth (Saffran et al., 1996), but abstract rule learning emerges around 7 months (Marcus et al., 1999). This marks the transition from pattern extraction to symbol formation.

**Early childhood (Stage 2 → 3 transition):** Relational reasoning capacity increases systematically between ages 3–11, with children progressing from binary relations to ternary relations to quaternary relations (Halford et al., 1998). Language acquisition shows a similar progression from word combinations to recursive phrase embedding (Chomsky, 1957).

**Middle childhood through adolescence (Stage 3 → 4 transition):** Metacognitive monitoring improves gradually across childhood and continues developing into early adulthood (Schneider, 2008). Adolescents show improved calibration, strategic learning allocation, and explicit reasoning about their own thought processes (Kuhn, 2000).

This developmental timeline is consistent with the proposed ordering: each stage depends on capacities developed in prior stages.

### 3.2 Comparative Evidence

Cross-species comparisons reveal variation in maximal abstraction capacity that aligns with the proposed stages.

**Invertebrates:** Capable of sophisticated pattern extraction (stage 1). Honeybees learn complex associations and show some generalization (Giurfa et al., 2001). Evidence for true symbol formation (stage 2) is limited.

**Non-primate mammals:** Show clear symbol formation and some compositional recombination (stage 2). Dogs generalize labels to categories (Kaminski, Call, & Fischer, 2004). Evidence for recursive composition (stage 3) is sparse outside of trained laboratory contexts.

**Great apes:** Demonstrate recursive composition in tool use, hierarchical planning, and some analogical reasoning (stage 3; Seed & Byrne, 2010). Evidence for spontaneous self-referential abstraction (stage 4) remains contested. Mirror self-recognition suggests some self-modeling (Gallup, 1970), but whether this constitutes abstraction over one’s own abstraction processes is unclear.

**Humans:** Unique in demonstrating robust, spontaneous, domain-general recursive composition and self-referential abstraction (stages 3–4). Human cognitive uniqueness may lie not in possessing abstraction but in the *depth* of recursive composition and the *reflexivity* of self-referential abstraction we achieve.

### 3.3 Neural Evidence

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

This is a hypothesis, not an established conclusion. Alternative explanations exist: architectural limitations (finite depth, no native recursion), training objectives (next-token prediction may not incentivize deep abstraction), or data limitations (text may not contain sufficient signal for higher-stage abstraction). Distinguishing these explanations requires targeted empirical work.

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

-----

## 6. Discussion

### 6.1 Relation to Existing Frameworks

The developmental spectrum proposed here connects to several existing frameworks.

**Piagetian stages:** Piaget (1954) proposed qualitative stages of cognitive development. The present framework differs in grounding stages in a specific computational operation (abstraction) rather than in domain-general structural properties (e.g., “formal operations”). However, the intuition that development involves qualitative transitions, not just quantitative growth, is shared.

**Relational complexity theory:** Halford et al. (1998) proposed that cognitive development involves increasing capacity for relational complexity. This aligns closely with the stage 2–3 transition proposed here. The present framework extends this by proposing earlier (stage 1) and later (stage 4) stages and by explicitly connecting the progression to abstraction as a unifying operation.

**Levels of processing in working memory:** Cowan (2001) and Oberauer (2009) have proposed hierarchical models of working memory with multiple levels of representation. The present framework connects these levels to abstraction stages and embeds them in a broader developmental trajectory.

**Metacognition research:** The stage 4 proposal draws on decades of metacognition research (Flavell, 1979; Nelson & Narens, 1990; Fleming & Lau, 2014). The present framework’s contribution is to embed metacognition within a broader abstraction hierarchy, suggesting that metacognition is not a separate faculty but the reflexive application of the same operation underlying all cognitive development.

### 6.2 What the Framework Does Not Claim

Several potential misreadings should be forestalled.

**Not a claim about mechanisms:** The framework proposes a functional decomposition (stages of abstraction capacity), not a mechanistic one (how these stages are implemented). The same stage might be implemented differently in biological and artificial systems.

**Not a claim about strict sequentiality in all domains:** Development may be uneven across domains. A system might achieve stage 3 in one domain while remaining at stage 2 in another. The claim is that within a domain, stages are hierarchically dependent.

**Not a claim that LLMs are “mere” anything:** Locating LLMs primarily at stages 1–2 with partial stage 3 capacity is not a dismissal. Stage 2 abstraction is a remarkable capacity. The analysis aims to characterize, not diminish.

### 6.3 Open Questions

**Continuity vs. discontinuity:** Are stages truly discrete, or do they represent points on a continuum? The present framework proposes qualitative discontinuities—each stage enables fundamentally new operations—but the boundaries may be graded rather than sharp.

**Substrate dependence:** Is the developmental sequence substrate-independent? We hypothesize yes, but this is an empirical question. Artificial systems might develop abstraction capacity in different orders than biological systems.

**Sufficiency of stage 4 for consciousness:** The framework proposes that stage 4 abstraction is necessary for consciousness. Whether it is sufficient is a further question. An artificial system with genuine self-referential abstraction might still lack consciousness, or might not. This is among the deepest open questions the framework surfaces but does not resolve.

-----

## 7. Conclusion

Intelligence is not unitary. Abstraction capacity—the core of intelligence, per the APH—develops through qualitatively distinct stages: pattern extraction, symbol formation, recursive composition, and self-referential abstraction. Each stage unlocks operations impossible at prior stages. Each depends on capacities developed before.

Large language models exhibit a distinctive profile on this spectrum: strong pattern extraction and symbol formation, partial recursive composition, and systematic limitations on self-referential abstraction. This profile—disembodied abstraction—characterizes what current LLMs can and cannot do and clarifies what innovations would be required for further advancement.

The framework generates testable predictions about developmental trajectories, cross-task correlations, LLM capabilities, and the role of embodiment. Falsification of these predictions would require revision or rejection of the framework. Confirmation would strengthen the hypothesis that abstraction is the primitive operation underlying intelligence—and that understanding its development is key to understanding intelligence itself.

-----

## References

Badre, D. (2008). Cognitive control, hierarchy, and the rostro-caudal organization of the frontal lobes. *Trends in Cognitive Sciences, 12*(5), 193–200.

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

Kuhn, D. (2000). Metacognitive development. *Current Directions in Psychological Science, 9*(5), 178–181.

Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *International Conference on Machine Learning*, 2873–2882.

Lakretz, Y., Dehaene, S., & King, J. R. (2019). What limits our capacity to process nested long-range dependencies in sentence comprehension? *Entropy, 21*(12), 1180.

Marcus, G. F., Vijayan, S., Rao, S. B., & Vishton, P. M. (1999). Rule learning by seven-month-old infants. *Science, 283*(5398), 77–80.

McCoy, R. T., Yun, M., Frank, R., & Linzen, T. (2023). Do language models learn to generalize compositionally? *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics*.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience, 24*(1), 167–202.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97.

Nelson, T. O., & Narens, L. (1990). Metamemory: A theoretical framework and new findings. *Psychology of Learning and Motivation, 26*, 125–173.

Oberauer, K. (2009). Design for a working memory. *Psychology of Learning and Motivation, 51*, 45–100.

Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature, 381*(6583), 607–609.

Parker, S. T., & McKinney, M. L. (1999). *Origins of intelligence: The evolution of cognitive development in monkeys, apes, and humans*. Johns Hopkins University Press.

Piaget, J. (1954). *The construction of reality in the child*. Basic Books.

Quinn, P. C. (2004). Development of subordinate-level categorization in 3- to 7-month-old infants. *Child Development, 75*(3), 886–899.

Rao, R. P., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience, 2*(1), 79–87.

Saffran, J. R., Aslin, R. N., & Newport, E. L. (1996). Statistical learning by 8-month-old infants. *Science, 274*(5294), 1926–1928.

Schneider, W. (2008). The development of metacognitive knowledge in children and adolescents: Major trends and implications for education. *Mind, Brain, and Education, 2*(3), 114–121.

Seed, A., & Byrne, R. (2010). Animal tool-use. *Current Biology, 20*(23), R1032–R1039.

Tenney, I., Das, D., & Pavlick, E. (2019). BERT rediscovers the classical NLP pipeline. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 4593–4601.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems, 30*.

Wallis, J. D., Anderson, K. C., & Miller, E. K. (2001). Single neurons in prefrontal cortex encode abstract rules. *Nature, 411*(6840), 953–956.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour, 7*, 1526–1541.

Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2023). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. *arXiv preprint arXiv:2306.13063*.

Yun, M., Chen, J., & Linzen, T. (2019). Does dependency length matter for context-free languages? *arXiv preprint arXiv:1909.04135*.

Zacks, J. M., & Tversky, B. (2001). Event structure in perception and conception. *Psychological Bulletin, 127*(1), 3–21.

-----

**Citation:** Danan, H. (2025). The developmental spectrum of abstraction: From pattern extraction to self-referential cognition. *Working paper, Abstraction-Intelligence Framework, Paper #10*.

-----

*“Abstraction develops. Each stage unlocks what the prior could not reach.”*

# Beyond Large Language Models: Architectural Principles from the Abstraction Primitive Hypothesis

**Paper 13 in the Abstraction-Intelligence Series**

Hillary Danan, PhD

*Working Draft*

-----

## Abstract

Large language models (LLMs) have achieved remarkable performance across diverse tasks, yet exhibit systematic limitations in compositional generalization, temporal reasoning, and recursive self-reference. This paper argues that these limitations are not contingent engineering challenges but structural consequences of architectures optimized for compression rather than abstraction. Drawing on the Abstraction Primitive Hypothesis (APH)—the claim that abstraction is the fundamental operation underlying intelligence—we derive architectural principles for systems that genuinely abstract rather than merely compress. We review empirical evidence for LLM limitations, propose design principles grounded in the distinction between compression and compositional abstraction, and generate testable predictions for next-generation architectures. This framework suggests that progress beyond current capabilities requires not simply scaling existing architectures but incorporating structural features that promote factorized, compositional, recombinable representations.

-----

## 1. Introduction

The rapid advancement of large language models has forced a reckoning in artificial intelligence research. Systems like GPT-4 (OpenAI, 2023), Claude (Anthropic, 2024), and PaLM (Chowdhery et al., 2022) demonstrate capabilities that were considered decades away just years prior. Yet alongside these achievements, systematic failure modes have emerged that resist scaling solutions (McKenzie et al., 2023; Wei et al., 2022a).

This paper proposes that understanding these limitations—and charting a path beyond them—requires engaging with a foundational question: what computational operation underlies intelligence itself?

The Abstraction Primitive Hypothesis (APH) offers a candidate answer: intelligence, across substrates, is fundamentally the capacity to form, store, retrieve, and compose abstractions (see Paper 1, this series). Critically, APH distinguishes abstraction from compression: while compression reduces information, abstraction creates compositional building blocks that combine to form new abstractions, enabling self-augmenting representational capacity.

If APH is correct, it yields a diagnosis: current LLMs are powerful compression engines that achieve sophisticated pattern matching without genuine compositional abstraction. It also yields a prescription: architectures optimized for abstraction require structural features absent from current designs.

This paper develops that argument in five parts. Section 2 reviews empirical evidence for systematic LLM limitations. Section 3 analyzes these limitations through the APH framework. Section 4 derives architectural principles for abstraction-promoting systems. Section 5 proposes testable predictions. Section 6 addresses objections and limitations.

We are explicit throughout about epistemic status: established empirical findings are cited; the APH framework and derived architectural principles are presented as working theory requiring empirical validation.

-----

## 2. Systematic Limitations of Current LLMs

### 2.1 Compositional Generalization Failures

The most extensively documented limitation concerns compositional generalization—the ability to understand and produce novel combinations of known primitives.

Lake and Baroni (2018) demonstrated that sequence-to-sequence models trained on a simple instruction-following task (SCAN) failed catastrophically on novel compositions of familiar commands, despite near-perfect performance on the training distribution. Humans, by contrast, generalize compositionally by default.

This finding has proven robust. Keysers et al. (2020) introduced the COGS benchmark and found that transformers achieved only 35% accuracy on compositional generalization tasks despite 99% accuracy on in-distribution items. Kim and Linzen (2020) showed that BERT-based models fail to generalize syntactic rules to novel lexical items. Dziri et al. (2023) demonstrated that even state-of-the-art LLMs fail at multi-step compositional reasoning, with accuracy degrading multiplicatively with reasoning depth.

Importantly, scaling provides limited remedy. Furrer et al. (2020) found that increased model size yielded only modest improvements on compositional generalization benchmarks, with performance plateauing well below human levels. Press et al. (2023) showed that compositional reasoning failures persist in models orders of magnitude larger than those originally tested.

**Epistemic status**: These findings are well-established empirically across multiple research groups and benchmarks.

### 2.2 Temporal and Causal Reasoning Limitations

LLMs exhibit systematic difficulties with temporal reasoning beyond sequence representation.

Jin et al. (2023) found that LLMs struggle with temporal commonsense reasoning, particularly tasks requiring understanding of duration, frequency, and typical temporal orderings. Vashishtha et al. (2020) demonstrated failures in temporal relation extraction even when syntactic processing is successful.

Causal reasoning shows similar patterns. Kıcıman et al. (2023) found that while LLMs can identify correlational patterns, they systematically fail at distinguishing causation from correlation and at reasoning about interventions. Zhang et al. (2023) showed that LLM performance on causal reasoning tasks degrades significantly when surface correlations are manipulated to conflict with causal structure.

**Epistemic status**: Well-documented empirically, though interpretation of underlying mechanisms remains debated.

### 2.3 Self-Reference and Metacognitive Limitations

LLMs show characteristic failures on tasks requiring self-reference or accurate self-modeling.

Kadavath et al. (2022) found that LLM confidence calibration is systematically poor, particularly on out-of-distribution queries—models cannot accurately assess what they know and don’t know. Lin et al. (2022) demonstrated that LLMs exhibit “sycophancy,” adjusting stated beliefs based on user feedback rather than maintaining consistent self-models.

Berglund et al. (2023) documented the “reversal curse”—models trained on “A is B” fail to infer “B is A”—suggesting representations that lack the symmetric, manipulable quality characteristic of genuine abstraction.

**Epistemic status**: Well-documented empirically. Connection to self-reference specifically is interpretive.

### 2.4 The Scaling Hypothesis and Its Limits

The dominant response to LLM limitations has been the scaling hypothesis: that sufficient increases in parameters, data, and compute will yield emergent capabilities addressing current failures (Kaplan et al., 2020; Hoffmann et al., 2022).

Scaling has indeed produced surprising capability gains. Wei et al. (2022b) documented “emergent abilities” appearing discontinuously at scale. However, recent work suggests limits to this paradigm.

McKenzie et al. (2023) identified “inverse scaling” phenomena—tasks where larger models perform *worse* than smaller ones, suggesting that scale amplifies certain failure modes rather than resolving them. Schaeffer et al. (2023) argued that claimed emergent abilities may be artifacts of metric choice rather than genuine phase transitions.

Crucially for our argument, Dziri et al. (2023) demonstrated that compositional reasoning accuracy degrades multiplicatively with reasoning depth regardless of scale, suggesting an architectural rather than capacity limitation.

**Epistemic status**: Scaling benefits are well-documented; limits to scaling are increasingly documented but remain contested.

-----

## 3. Diagnosis: Compression Without Abstraction

### 3.1 The Abstraction Primitive Hypothesis

The Abstraction Primitive Hypothesis (APH) proposes that abstraction—the formation of compositional, manipulable, recombinable representations—is the fundamental operation underlying intelligence (see Paper 1, this series).

APH distinguishes abstraction from compression:

- **Compression** reduces information, producing holistic representations that capture statistical regularities but do not compose.
- **Abstraction** produces factorized representations that function as building blocks—they combine to form new abstractions, enabling generative, self-augmenting representational capacity.

The key signature of abstraction is **compositionality**: abstractions combine systematically to produce meanings determined by their constituents and combination rules (Fodor & Pylyshyn, 1988; Szabó, 2022).

**Epistemic status**: APH is a theoretical framework—working hypothesis, not established fact. The compression/abstraction distinction draws on established concepts in information theory and cognitive science but the specific formulation is novel.

### 3.2 LLMs as Compression Engines

We propose that current LLMs are optimized for compression rather than abstraction.

The transformer architecture (Vaswani et al., 2017) and autoregressive training objective optimize for next-token prediction—a compression task. The model learns to encode statistical regularities in training data that enable accurate prediction.

This optimization can produce remarkable capabilities. Compression requires capturing genuine structure; better compression often requires better world models (Hutter, 2005). However, compression does not require—and may not produce—compositional representations.

Evidence that LLM representations are compressive rather than compositional:

1. **Holistic encoding**: Analyses of LLM representations suggest distributed, superposed encoding where concepts are not cleanly factorized (Elhage et al., 2022; Arora et al., 2018). This is efficient for compression but impedes composition.
1. **Compositional generalization failures**: The pattern documented in Section 2.1—excellent in-distribution performance, poor compositional generalization—is precisely what APH predicts for sophisticated compression without abstraction.
1. **Context-dependence**: LLM representations of concepts vary substantially with context in ways that suggest holistic pattern matching rather than stable, manipulable symbols (Ethayarajh, 2019).
1. **Absence of symbolic manipulation**: Mechanistic interpretability research suggests LLMs implement soft attention over distributed representations rather than discrete symbol manipulation (Olsson et al., 2022).

**Epistemic status**: The characterization of LLMs as compression engines is interpretive. The cited empirical findings are established; the APH-based interpretation is working theory.

### 3.3 Stage-Specific Limitations

APH proposes that abstraction capacity develops through qualitatively distinct stages (see Paper 6, this series):

1. **Stage 1: Pattern Extraction** — Recognition of statistical regularities
1. **Stage 2: Symbol Formation** — Binding patterns into manipulable units
1. **Stage 3: Recursive Composition** — Combining symbols to form new symbols
1. **Stage 4: Self-Referential Abstraction** — Applying abstraction to one’s own cognitive processes

We hypothesize that current LLMs achieve sophisticated Stage 1 performance and partial Stage 2 capacity, with systematic limitations at Stages 3 and 4.

This predicts:

- Strong performance on pattern recognition and retrieval
- Mixed performance on symbol manipulation (some successes, systematic failures)
- Poor compositional generalization (Stage 3 limitation)
- Poor metacognitive calibration (Stage 4 limitation)

This pattern matches the empirical profile documented in Section 2.

**Epistemic status**: The stage model is theoretical, derived from developmental and comparative cognition literatures but not directly validated for artificial systems. The mapping to LLM limitations is hypothetical.

-----

## 4. Architectural Principles for Abstraction

If the diagnosis in Section 3 is correct, progress requires architectures that promote abstraction rather than (merely) compression. We derive principles from APH and supporting literature.

### 4.1 Factorization Pressure

**Principle**: Architectures should include explicit pressure toward factorized representations where distinct features are encoded independently.

**Rationale**: Compositional abstraction requires representations that decompose along semantically meaningful dimensions. Without factorization pressure, optimization favors distributed, superposed encoding that is efficient for compression but impedes composition.

**Supporting evidence**: Work on disentangled representation learning demonstrates that explicit factorization pressure yields representations with improved compositional generalization and transfer.

Higgins et al. (2017) showed that β-VAE architectures with increased pressure on the latent bottleneck produce more disentangled representations. Locatello et al. (2019) demonstrated that while fully unsupervised disentanglement may be impossible, inductive biases promoting factorization improve downstream task performance. Van Steenkiste et al. (2019) found that disentangled representations enable systematic generalization on object-centric reasoning tasks.

**Architectural implementations**:

- Information bottlenecks with factorization penalties (β-VAE; Higgins et al., 2017)
- Sparse coding constraints (Olshausen & Field, 1996)
- Slot-based object representations (Locatello et al., 2020)
- Modular network architectures with limited cross-module communication

**Epistemic status**: The benefits of factorized representations are empirically supported; specific architectural implementations vary in maturity.

### 4.2 Compositional Bottlenecks

**Principle**: Architectures should include structural bottlenecks that force composition of primitive elements.

**Rationale**: APH proposes that abstraction is distinguished from compression by compositionality—the capacity to combine primitives into novel structures. Architectural bottlenecks that require such combination provide training signal for compositional capacity.

**Supporting evidence**: Neural module networks and related architectures demonstrate that structural composition constraints improve systematic generalization.

Andreas et al. (2016) showed that neural module networks—which compose specialized modules according to explicit structure—outperform monolithic networks on compositional visual reasoning tasks. Bahdanau et al. (2019) demonstrated that architectures with explicit compositional structure generalize better on the CLEVR benchmark. Lake (2019) showed that architectures incorporating symbolic structure achieve human-like compositional generalization on the SCAN benchmark.

**Architectural implementations**:

- Neural module networks (Andreas et al., 2016)
- Neuro-symbolic architectures (Garcez et al., 2019)
- Structured attention mechanisms (Kim et al., 2017)
- Compositional world models (Kipf et al., 2020)

**Epistemic status**: Benefits of compositional structure are empirically supported; integration with large-scale language models remains an open research problem.

### 4.3 Recombination Exposure

**Principle**: Training should systematically expose systems to recombinations of primitives, not merely exemplars.

**Rationale**: Compositional abstraction requires learning that primitives can combine in multiple ways. Training distributions that present primitives only in fixed combinations do not provide signal for compositional structure.

**Supporting evidence**: Data augmentation and curriculum design affect compositional generalization.

Akyürek et al. (2021) demonstrated that training data diversity significantly affects compositional generalization in sequence-to-sequence models. Andreas (2020) showed that compositional data augmentation—systematically generating recombinations—improves generalization on SCAN-like tasks. Gordon et al. (2020) found that curriculum learning strategies exposing models to increasing compositional complexity improve systematic generalization.

**Architectural implications**:

- Training data generation emphasizing compositional diversity
- Curriculum learning from primitives to compositions
- Data augmentation via systematic recombination
- Multi-task training across compositionally related tasks

**Epistemic status**: Effects of training distribution on compositionality are empirically supported; optimal strategies remain under investigation.

### 4.4 Multi-Task Compositional Structure

**Principle**: Training across multiple tasks that share compositional structure should improve abstraction capacity.

**Rationale**: If the same primitive abstractions are useful across tasks, multi-task learning provides pressure to extract those primitives explicitly rather than encoding task-specific holistic patterns.

**Supporting evidence**: Multi-task and meta-learning paradigms demonstrate transfer benefits when tasks share structure.

Finn et al. (2017) showed that meta-learning (MAML) enables rapid adaptation to new tasks by learning transferable representations. Ruder (2017) reviewed evidence that multi-task learning improves generalization when tasks share underlying structure. Lake et al. (2017) argued that human-like compositional learning requires exposure to structured task distributions.

**Architectural implementations**:

- Meta-learning frameworks (Finn et al., 2017)
- Multi-task learning with shared representations (Caruana, 1997)
- Instruction-tuning across diverse task types (Wei et al., 2022c)
- Compositional task curricula

**Epistemic status**: Multi-task learning benefits are well-established; specific designs for compositional abstraction require further development.

### 4.5 Grounding and Embodiment

**Principle**: Architectures should incorporate grounding in perception-action loops or embodied simulation.

**Rationale**: APH proposes that certain abstraction stages—particularly those involving temporal reasoning, causal understanding, and self-world distinction—are grounded in embodied experience (see Papers 8-10, this series). Disembodied text-only training may impose ceilings on these capacities.

**Supporting evidence**: Embodied and grounded approaches improve certain reasoning capacities.

Bisk et al. (2020) argued that language understanding requires grounding in perception and action, documenting systematic failures in ungrounded language models on physical reasoning tasks. Hill et al. (2020) demonstrated that agents trained in embodied environments develop more robust object representations than those trained on static data. Zellers et al. (2021) showed that video-language pretraining improves physical commonsense reasoning.

**Architectural implementations**:

- Multimodal architectures with perceptual grounding (Alayrac et al., 2022)
- Embodied agent training in simulated environments (Savva et al., 2019)
- World models with predictive perception-action dynamics (Ha & Schmidhuber, 2018)
- Physics-informed neural architectures (Raissi et al., 2019)

**Epistemic status**: Benefits of grounding are supported for specific domains; generality and optimal implementation remain open questions. The APH-specific claims about embodiment and abstraction stages are theoretical.

### 4.6 Explicit Self-Modeling

**Principle**: Architectures should include mechanisms for explicit self-representation and self-reference.

**Rationale**: APH proposes that the highest abstraction stages involve self-referential abstraction—applying the abstraction operation to one’s own cognitive processes (see Papers 5 and 7, this series). Current architectures lack explicit self-models, limiting metacognitive capacity.

**Supporting evidence**: Self-modeling improves calibration and enables adaptive behavior.

Nagabandi et al. (2018) demonstrated that agents with learned self-models show improved adaptation to changing embodiment. Amos et al. (2018) showed that differentiable self-models enable model-predictive control. In the LLM context, Kadavath et al. (2022) found that explicit self-evaluation prompting improves calibration, suggesting that architectures natively incorporating self-reference might yield further benefits.

**Architectural implementations**:

- Learned self-models (Nagabandi et al., 2018)
- Internal simulation and prediction of own outputs
- Explicit uncertainty representation (Gal & Ghahramani, 2016)
- Metacognitive architectures with distinct object-level and meta-level processing

**Epistemic status**: Self-modeling benefits are demonstrated in specific domains; the connection to APH’s abstraction stages is theoretical; implementation in language models is nascent.

-----

## 5. Testable Predictions

The APH framework generates specific, falsifiable predictions distinguishing it from alternatives.

### 5.1 Architectural Predictions

**Prediction 5.1.1**: Architectures with explicit factorization pressure (e.g., β-VAE-style bottlenecks integrated into language models) should show improved compositional generalization compared to standard transformers at equivalent scale.

**Falsification**: If factorization pressure yields no improvement or degrades compositional generalization, this disconfirms the factorization principle.

**Prediction 5.1.2**: Architectures with compositional bottlenecks (e.g., neural module networks, neuro-symbolic hybrids) should show improved systematicity on compositional generalization benchmarks, with the magnitude of improvement increasing with compositional complexity.

**Falsification**: If compositional bottlenecks provide no advantage over distributed architectures at equivalent capacity, this disconfirms the compositional bottleneck principle.

**Prediction 5.1.3**: Multi-task training across compositionally related tasks should produce superlinear cumulative performance gains (learning task N+1 should be faster given tasks 1-N than predicted from independent learning rates).

**Falsification**: If multi-task learning on compositionally related tasks shows only linear or sublinear cumulative benefits, this disconfirms the compositional transfer principle.

### 5.2 Scaling Predictions

**Prediction 5.2.1**: Scaling standard transformer architectures should improve Stage 1-2 performance (pattern recognition, retrieval, simple symbol manipulation) more than Stage 3-4 performance (compositional generalization, metacognitive calibration).

**Falsification**: If scaling improves Stage 3-4 performance at equivalent or greater rates than Stage 1-2 performance, this disconfirms the stage-specific scaling prediction.

**Prediction 5.2.2**: Architectural modifications promoting abstraction (factorization, compositional bottlenecks, self-modeling) should show greater benefits at Stages 3-4 than scaling alone.

**Falsification**: If architectural modifications provide no Stage 3-4 advantage over equivalent-cost scaling, this disconfirms the architecture-over-scaling prediction for higher stages.

### 5.3 Grounding Predictions

**Prediction 5.3.1**: Systems trained with embodied grounding should outperform text-only systems on temporal reasoning tasks involving duration, process dynamics, and temporal perspective-taking—but not on sequence logic or explicit temporal relation tasks.

**Falsification**: If embodied training provides no selective advantage on grounded temporal tasks, or if it improves sequence logic equally, this disconfirms the grounding-specificity prediction.

**Prediction 5.3.2**: Systems with learned self-models should show improved metacognitive calibration (confidence-accuracy correlation) compared to systems without explicit self-models.

**Falsification**: If explicit self-models provide no calibration advantage, this disconfirms the self-modeling principle.

### 5.4 Compositionality Metrics

**Prediction 5.4.1**: Compositionality metrics—Compositional Generalization Rate (CGR), Systematicity Index (SI), Transfer Efficiency Ratio (TER), Compositional Depth (CD), and Reuse Frequency (RF) (see Paper 2, this series)—should correlate with each other and jointly predict downstream task performance better than compression metrics (reconstruction error, encoding length) alone.

**Falsification**: If compositionality metrics do not form a coherent factor, or if compression metrics predict downstream performance equally well, this disconfirms the compositionality-as-distinctive-signature claim.

-----

## 6. Objections and Limitations

### 6.1 The Scaling Objection

**Objection**: Sufficient scaling may yield emergent abstraction capacity without architectural modification. The history of deep learning favors scaling and data over architectural innovation.

**Response**: This is an empirical question the predictions in Section 5 are designed to address. We note that compositional generalization failures persist across orders of magnitude of scale (Dziri et al., 2023), and inverse scaling phenomena suggest some limitations are amplified rather than resolved by scale (McKenzie et al., 2023). However, we acknowledge that future scaling results could disconfirm our predictions.

### 6.2 The Implementation Objection

**Objection**: The architectural principles in Section 4 are abstract; concrete implementations may prove intractable or yield unforeseen costs.

**Response**: Valid concern. We have cited existing implementations where available, but integration into large-scale language models remains an open research challenge. The principles should be understood as research directions, not engineering specifications.

### 6.3 The Parsimony Objection

**Objection**: The APH framework adds theoretical complexity. Simpler accounts (e.g., “LLMs need more diverse training data”) may suffice.

**Response**: Parsimony favors simpler theories only when explanatory power is equal. The APH framework unifies diverse observations—compositional generalization failures, temporal reasoning limitations, metacognitive miscalibration—under a single diagnostic account. If training data manipulations alone resolve these limitations, this would indeed favor the simpler account. Section 5 predictions are designed to discriminate.

### 6.4 The Measurement Objection

**Objection**: “Abstraction” and “compositionality” are difficult to measure operationally, risking unfalsifiability.

**Response**: Paper 2 in this series proposes specific operationalizations: Compositional Generalization Rate (novel combination accuracy / training accuracy), Systematicity Index (consistency of rule application), Transfer Efficiency Ratio (transfer performance / direct training performance), Compositional Depth (maximum nesting with maintained accuracy), and Reuse Frequency (primitive recombination count). These are measurable. We acknowledge that operationalization may imperfectly capture theoretical constructs—a limitation shared by all cognitive science.

### 6.5 Limitations of This Paper

We acknowledge several limitations:

1. **Theoretical framework**: APH is a working hypothesis, not established theory. The architectural principles derived from it inherit this epistemic status.
1. **Implementation gap**: We propose principles but not complete implementations. Engineering realization may surface unforeseen challenges.
1. **Empirical validation**: Predictions await testing. Negative results would require framework revision.
1. **Scope**: We focus on architectural principles; other factors (training objectives, data quality, optimization methods) also matter.

-----

## 7. Research Agenda

We propose a phased research agenda for empirical validation.

### Phase 1: Benchmarking and Metrics

1. Develop standardized benchmarks for each abstraction stage
1. Validate compositionality metrics (Paper 2) across architectures
1. Establish baselines for current LLMs at each stage

### Phase 2: Architectural Experiments

1. Integrate factorization pressure into transformer architectures
1. Develop compositional bottleneck variants
1. Compare abstraction-promoting architectures to scaling baselines

### Phase 3: Grounding and Embodiment

1. Compare embodied vs. disembodied training on temporal reasoning benchmarks
1. Develop self-modeling architectures for language models
1. Test grounding benefits across abstraction stages

### Phase 4: Integration and Scaling

1. Combine successful architectural modifications
1. Scale abstraction-promoting architectures
1. Evaluate on comprehensive intelligence benchmarks

-----

## 8. Conclusion

Large language models represent a remarkable achievement in artificial intelligence—and a natural experiment in what sophisticated compression without guaranteed compositional abstraction produces. The systematic limitations documented here—compositional generalization failures, temporal reasoning deficits, metacognitive miscalibration—are, we propose, diagnostic of architectures optimized for compression rather than abstraction.

The Abstraction Primitive Hypothesis offers both diagnosis and prescription. If abstraction is the fundamental operation underlying intelligence, and if abstraction is distinguished from compression by compositionality, then progress beyond current limitations requires architectures that promote factorized, compositional, recombinable representations.

We have derived architectural principles from this framework: factorization pressure, compositional bottlenecks, recombination exposure, multi-task compositional structure, grounding, and explicit self-modeling. These are not speculative wishes but principled derivations generating testable predictions.

The question is empirical: will abstraction-promoting architectures outperform scaling alone? The predictions in Section 5 are designed to answer it.

If the APH framework proves correct, it suggests that the path beyond large language models runs not through ever-larger transformers but through architectures that learn to abstract—forming the compositional building blocks that enable genuine generalization, transfer, and self-understanding.

The scaling era has taught us what compression can achieve. The abstraction era may teach us what intelligence requires.

-----

## References

Akyürek, E., Akyürek, A., Andreas, J. (2021). Learning to recombine and resample data for compositional generalization. *ICLR*.

Alayrac, J.B., et al. (2022). Flamingo: A visual language model for few-shot learning. *NeurIPS*.

Amos, B., Jimenez, I., Sacks, J., Boots, B., Kolter, J.Z. (2018). Differentiable MPC for end-to-end planning and control. *NeurIPS*.

Andreas, J. (2020). Good-enough compositional data augmentation. *ACL*.

Andreas, J., Rohrbach, M., Darrell, T., Klein, D. (2016). Neural module networks. *CVPR*.

Arora, S., Li, Y., Liang, Y., Ma, T., Risteski, A. (2018). Linear algebraic structure of word senses, with applications to polysemy. *TACL*.

Bahdanau, D., Murty, S., Noukhovitch, M., Nguyen, T.H., de Vries, H., Courville, A. (2019). Systematic generalization: What is required and can it be learned? *ICLR*.

Berglund, L., et al. (2023). The reversal curse: LLMs trained on “A is B” fail to learn “B is A.” *arXiv preprint arXiv:2309.12288*.

Bisk, Y., et al. (2020). Experience grounds language. *EMNLP*.

Caruana, R. (1997). Multitask learning. *Machine Learning*, 28(1), 41-75.

Chowdhery, A., et al. (2022). PaLM: Scaling language modeling with pathways. *arXiv preprint arXiv:2204.02311*.

Dziri, N., et al. (2023). Faith and fate: Limits of transformers on compositionality. *NeurIPS*.

Elhage, N., et al. (2022). Toy models of superposition. *Transformer Circuits Thread*.

Ethayarajh, K. (2019). How contextual are contextualized word representations? *EMNLP*.

Finn, C., Abbeel, P., Levine, S. (2017). Model-agnostic meta-learning for fast adaptation of deep networks. *ICML*.

Fodor, J.A., Pylyshyn, Z.W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Furrer, D., van Zee, M., Scales, N., Schärli, N. (2020). Compositional generalization in semantic parsing: Pre-training vs. specialized architectures. *arXiv preprint arXiv:2007.08970*.

Gal, Y., Ghahramani, Z. (2016). Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. *ICML*.

Garcez, A.D., et al. (2019). Neural-symbolic computing: An effective methodology for principled integration of machine learning and reasoning. *Journal of Applied Logics*, 6(4), 611-632.

Gordon, J., Lopez-Paz, D., Baroni, M., Bouchacourt, D. (2020). Permutation equivariant models for compositional generalization in language. *ICLR*.

Ha, D., Schmidhuber, J. (2018). World models. *arXiv preprint arXiv:1803.10122*.

Higgins, I., et al. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *ICLR*.

Hill, F., et al. (2020). Environmental drivers of systematicity and generalization in a situated agent. *ICLR*.

Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*.

Hutter, M. (2005). *Universal artificial intelligence: Sequential decisions based on algorithmic probability*. Springer.

Jin, W., et al. (2023). CLadder: Assessing causal reasoning in language models. *NeurIPS*.

Kadavath, S., et al. (2022). Language models (mostly) know what they know. *arXiv preprint arXiv:2207.05221*.

Kaplan, J., et al. (2020). Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*.

Keysers, D., et al. (2020). Measuring compositional generalization: A comprehensive method on realistic data. *ICLR*.

Kıcıman, E., et al. (2023). Causal reasoning and large language models: Opening a new frontier for causality. *arXiv preprint arXiv:2305.00050*.

Kim, J., et al. (2017). Structured attention networks. *ICLR*.

Kim, N., Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *EMNLP*.

Kipf, T., van der Pol, E., Welling, M. (2020). Contrastive learning of structured world models. *ICLR*.

Lake, B.M. (2019). Compositional generalization through meta sequence-to-sequence learning. *NeurIPS*.

Lake, B.M., Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML*.

Lake, B.M., Ullman, T.D., Tenenbaum, J.B., Gershman, S.J. (2017). Building machines that learn and think like people. *Behavioral and Brain Sciences*, 40, e253.

Lin, S., Hilton, J., Evans, O. (2022). TruthfulQA: Measuring how models mimic human falsehoods. *ACL*.

Locatello, F., et al. (2019). Challenging common assumptions in the unsupervised learning of disentangled representations. *ICML*.

Locatello, F., et al. (2020). Object-centric learning with slot attention. *NeurIPS*.

McKenzie, I.R., et al. (2023). Inverse scaling: When bigger isn’t better. *TMLR*.

Nagabandi, A., et al. (2018). Learning to adapt in dynamic, real-world environments through meta-reinforcement learning. *ICLR*.

Olshausen, B.A., Field, D.J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*, 381(6583), 607-609.

Olsson, C., et al. (2022). In-context learning and induction heads. *Transformer Circuits Thread*.

OpenAI. (2023). GPT-4 technical report. *arXiv preprint arXiv:2303.08774*.

Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N.A., Lewis, M. (2023). Measuring and narrowing the compositionality gap in language models. *EMNLP*.

Raissi, M., Perdikaris, P., Karniadakis, G.E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, 378, 686-707.

Ruder, S. (2017). An overview of multi-task learning in deep neural networks. *arXiv preprint arXiv:1706.05098*.

Savva, M., et al. (2019). Habitat: A platform for embodied AI research. *ICCV*.

Schaeffer, R., Miranda, B., Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*.

Szabó, Z.G. (2022). Compositionality. *Stanford Encyclopedia of Philosophy*.

Van Steenkiste, S., et al. (2019). Are disentangled representations helpful for abstract visual reasoning? *NeurIPS*.

Vashishtha, S., Durrett, G., Tu, J. (2020). What do neural networks learn about event knowledge? *CoNLL*.

Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS*.

Wei, J., et al. (2022a). Inverse scaling can become U-shaped. *arXiv preprint arXiv:2211.02011*.

Wei, J., et al. (2022b). Emergent abilities of large language models. *TMLR*.

Wei, J., et al. (2022c). Finetuned language models are zero-shot learners. *ICLR*.

Zellers, R., et al. (2021). MERLOT: Multimodal neural script knowledge models. *NeurIPS*.

Zhang, C., et al. (2023). Understanding causality with large language models: Feasibility and opportunities. *arXiv preprint arXiv:2304.05524*.

-----

*Acknowledgments*: This paper builds on twelve prior papers in the Abstraction-Intelligence series. See the [repository](https://github.com/HillaryDanan/abstraction-intelligence) for the complete framework.

-----

**Epistemic Status Summary**

|Claim Type                                 |Status                                                                       |
|-------------------------------------------|-----------------------------------------------------------------------------|
|LLM compositional generalization failures  |Established (peer-reviewed)                                                  |
|LLM temporal/causal reasoning limitations  |Established (peer-reviewed)                                                  |
|LLM metacognitive miscalibration           |Established (peer-reviewed)                                                  |
|Limits of scaling for compositional tasks  |Emerging evidence (peer-reviewed, debated)                                   |
|Abstraction Primitive Hypothesis           |Working theory (this series)                                                 |
|LLMs as compression vs. abstraction engines|Interpretive (supported by evidence, not proven)                             |
|Abstraction stage model                    |Theoretical (derived from cognitive science, not validated for AI)           |
|Architectural principles                   |Theoretically derived, empirically supported components, untested integration|
|Predictions                                |Falsifiable, awaiting testing                                                |

-----

*“Compression reduces. Abstraction grows.”*

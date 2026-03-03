# Testing the Internal/External Semantic Axis in Large Language Model Representations: A Feature-Based Representational Similarity Analysis

**Hillary J. Danan**

*Working Draft — March 2026*

---

## Abstract

The human brain organizes abstract concepts along an internal-to-self versus external-to-self dimension, with internal features (emotion, morality, thought, social) mapping onto the default mode network and external features (space, time, quantity) mapping onto task-positive regions (Troche et al., 2017; Danan [Levinson], 2021). Whether large language models (LLMs) develop a comparable organizational structure is unknown. Representational similarity analysis (RSA) has become the standard methodology for comparing neural and artificial representations (Kriegeskorte et al., 2008; Caucheteux & King, 2022), but no study has applied RSA to test for the internal/external axis specifically. Here I propose a systematic study to (1) extract LLM hidden-state representations for concepts rated on the 14-feature semantic model validated in Danan (2021), (2) construct representational dissimilarity matrices (RDMs) for the internal, external, and concrete factors, and (3) test whether LLM representational geometry recapitulates the three-factor structure found in human behavioral ratings and neural data. I present pilot behavioral validation data, describe the proposed computational pipeline, and articulate explicit predictions and their theoretical significance. This approach directly tests the hypothesis that distributional language statistics recover the internal semantic dimension—which is neurally processed in networks decoupled from sensory input—better than the external or concrete dimensions.

---

## 1. Introduction

### 1.1 The gap

A rapidly growing literature uses RSA and related methods to compare the internal representations of large language models to human brain activity measured by fMRI and electrophysiology (Caucheteux & King, 2022; Goldstein et al., 2022; Schrimpf et al., 2021). These studies have established several important findings: transformer embeddings predict neural activity in language regions with surprising accuracy (Schrimpf et al., 2021); lower layers align with temporal cortices while higher layers predict frontoparietal activity (Caucheteux & King, 2022); brain prediction performance scales logarithmically with model size (Antonello & Huth, 2024); and geometric alignment between brain and LLM embedding spaces can be demonstrated at the level of individual participants (Goldstein et al., 2024).

However, these comparisons have overwhelmingly focused on the *aggregate* alignment between LLM representations and brain activity during naturalistic language processing. They have not tested whether specific *organizational principles* of the human semantic system are recapitulated in LLMs. In particular, no study has tested whether LLMs develop representations that differentiate abstract concepts along the internal/external dimension—a dimension that has been validated behaviorally (Troche et al., 2017) and neurally (Danan [Levinson], 2021; Huth et al., 2012, 2016).

This gap matters for two reasons. First, knowing whether LLMs spontaneously develop the internal/external axis would inform the grounding debate: if this axis emerges from distributional statistics alone, it would suggest that the brain's organization of abstract concepts along this dimension reflects statistical regularities in language rather than (or in addition to) embodied experience. Second, as I have argued elsewhere (Danan, 2026, in preparation), the internal/external axis may predict where LLM-brain alignment is strongest versus weakest, given that the internal dimension is processed in networks (DMN) that are functionally decoupled from sensory input.

### 1.2 What we know and what we do not know

We know that LLMs recover some aspects of human conceptual structure. Xu et al. (2025) demonstrated that LLM-human alignment is strongest for non-sensorimotor features and weakest for motor features, using the Glasgow and Lancaster norm datasets. This finding is consistent with the hypothesis that the internal semantic dimension should be well-represented in LLMs—since internal features (emotion, morality, thought, social) are all non-sensorimotor. However, Xu et al. did not test the internal/external distinction specifically; their analyses grouped all non-sensorimotor features together.

We also know that LLMs develop structured semantic spaces with interpretable dimensions. Probing studies have identified directions in LLM embedding spaces that correspond to sentiment, concreteness, and other semantic features (e.g., Grand et al., 2022). But whether these features spontaneously organize into the three-factor structure (internal, external, concrete) found in human behavioral ratings and neural data is an open question.

We do not know whether the *relational structure* among concepts as organized by their internal/external/concrete features is preserved in LLMs. This is the question that RSA is uniquely suited to address, because RSA compares the geometry of representational spaces rather than individual feature values (Kriegeskorte et al., 2008).

### 1.3 Approach

The proposed study has three components:

1. **Behavioral validation**: Replicate the 14-feature semantic ratings from Danan (2021) on the stimulus set, confirming the three-factor structure, and extend ratings to additional concepts to improve power.

2. **LLM representation extraction**: Extract hidden-state representations from multiple LLM families (GPT-4, Claude, LLaMA-3, Gemma) for the same concepts, across layers, to construct RDMs.

3. **RSA comparison**: Test whether the three-factor structure (internal, external, concrete) predicts LLM representational geometry, and if so, which factors are best recovered.

## 2. Materials

### 2.1 The 14-feature semantic model

The feature model, originally developed by Binder et al. (2016) and adapted by Troche et al. (2017), comprises 14 semantic features that span sensory, motor, affective, social, and cognitive domains. In Danan (2021), I collected behavioral ratings on these features for 400 word concepts, using the following features (grouped by the factor structure that emerged from exploratory factor analysis):

**Internal factor features**: emotion, polarity (valence), morality, sociality, thought

**External factor features**: time, space, quantity/number

**Concrete factor features**: visual form, color, auditory, tactile, smell/taste, self-motion

This three-factor solution was confirmed by parallel analysis and exploratory factor analysis with oblimin rotation. Hierarchical cluster analysis further supported a primary division between abstract (internal + external) and concrete features, with a secondary division within abstract features between internal and external factors (Danan [Levinson], 2021).

### 2.2 Stimulus set

The original stimulus set comprised 400 word concepts selected to span the concrete-abstract continuum and to sample broadly within abstract space along the internal/external dimension. Words were controlled for word frequency, word length, orthographic neighborhood density, and age of acquisition (Danan [Levinson], 2021). For the proposed study, we will use the same 400 words to enable direct comparison with existing behavioral and neural data, and will extend the set to 600 words to improve statistical power for factor-level analyses.

### 2.3 Candidate models

To test for generality across architectures and training regimes, we will extract representations from:

- **GPT-4** (OpenAI): Decoder-only transformer; the model for which the most extensive brain-alignment data exists (Strachan et al., 2024; Xu et al., 2025)
- **Claude 3.5 Sonnet** (Anthropic): Decoder-only transformer with constitutional AI training
- **LLaMA-3 70B** (Meta): Open-weights decoder-only transformer, enabling full hidden-state access
- **Gemma 2 27B** (Google): Open-weights model from a different training pipeline

For closed models (GPT-4, Claude), we will extract representations via API embeddings and/or prompt-based rating approaches following Xu et al. (2025). For open models (LLaMA-3, Gemma), we will extract hidden-state activations at each layer, enabling layer-wise analysis.

## 3. Methods

### 3.1 Behavioral ratings

**Participants.** We will recruit N = 200 participants (50 per word batch of 150 words, with overlapping anchor items) via Prolific, following the same inclusion criteria as Danan (2021): native English speakers, 18–65 years old, no history of neurological or psychiatric conditions.

**Procedure.** Each participant will rate a subset of words on all 14 features using 7-point scales, with feature definitions matched to those in Danan (2021) and Binder et al. (2016). Feature order will be counterbalanced across participants.

**Analysis.** We will conduct confirmatory factor analysis (CFA) testing the three-factor model (internal, external, concrete) against alternative models (unidimensional, two-factor concrete/abstract, four-factor, five-factor). Model fit will be assessed using standard indices (CFI > .95, RMSEA < .06, SRMR < .08; Hu & Bentler, 1999). We will also compute representational dissimilarity matrices (RDMs) based on the rated features, separately for internal, external, and concrete feature subsets.

### 3.2 LLM representation extraction

**Prompt-based ratings (all models).** Following Xu et al. (2025), we will prompt each LLM to rate all 600 words on each of the 14 features, using instructions matched to those given to human participants. Each word will be rated in four independent sessions per model to assess consistency. This yields prompt-based feature vectors that are directly comparable to human ratings.

**Hidden-state extraction (open models).** For LLaMA-3 and Gemma, we will present each word in a neutral sentence frame ("The concept of [WORD] is...") and extract the hidden-state activation at the position of [WORD] from every layer. For each model, this yields a set of activation vectors (one per word per layer) that can be used to construct neural-style RDMs.

**Embedding extraction (all models).** We will also extract embedding-level representations using standard API calls, where available, to test whether the factor structure is present at the output embedding level.

### 3.3 Representational similarity analysis

**RDM construction.** For each representation type (human behavioral ratings, LLM prompt-based ratings, LLM hidden states), we will construct RDMs using 1 minus the Pearson correlation between feature vectors (for behavioral and prompt-based ratings) or activation vectors (for hidden states) across all word pairs. This yields one RDM per representation type.

**Factor-specific model RDMs.** We will construct three model RDMs from the human behavioral data, each using only the features belonging to one factor:
- *Internal RDM*: Based on emotion, polarity, morality, sociality, thought ratings
- *External RDM*: Based on time, space, quantity ratings
- *Concrete RDM*: Based on visual, color, auditory, tactile, smell/taste, self-motion ratings

**RSA tests.** For each LLM representation, we will compute the Spearman rank correlation between the LLM RDM and each of the three factor-specific model RDMs. This yields a measure of how well each factor predicts the LLM's representational geometry. We will test whether:
1. All three factors are significantly correlated with LLM representations
2. The internal factor shows significantly stronger correlation than the external or concrete factors
3. The concrete factor shows the weakest correlation
4. These patterns hold across layers (for open models)

**Statistical inference.** Significance will be assessed using permutation tests (10,000 permutations, shuffling word labels) to establish null distributions for each RSA correlation. Differences between factor correlations will be tested using bootstrapped confidence intervals on the difference scores.

**Partial RSA.** Following recommendations in Danan (2021), we will also conduct partial RSA to assess the unique contribution of each factor after controlling for the other two. This is important because the three factors are not fully orthogonal (e.g., concrete words tend to have lower internal ratings).

### 3.4 Layer-wise analysis (open models only)

For LLaMA-3 and Gemma, we will conduct the RSA at each transformer layer to test how factor-specific alignment varies across the processing hierarchy. Based on Caucheteux and King (2022), who found that higher layers better predict frontoparietal (including DMN) activity, we predict:

- Internal factor alignment should increase with layer depth, peaking at higher layers that correspond to more abstract, integrative computations
- Concrete factor alignment should peak at lower or middle layers, corresponding to more surface-level representations
- External factor alignment should show an intermediate pattern

This prediction is motivated by the neuroimaging finding that DMN regions (which encode the internal factor) correspond to higher-level, integrative processing, while sensorimotor regions (encoding concrete features) correspond to more primary processing stages.

## 4. Predictions and Their Theoretical Significance

### 4.1 Primary predictions

**H1: LLMs will show significant correspondence to the three-factor structure.**

*Rationale*: If the internal/external/concrete distinction reflects statistical regularities in how these concepts co-occur and are used in language (as well as, or instead of, embodied experience), then models trained on large language corpora should capture this structure.

*What it would mean if confirmed*: The organizational structure of abstract semantics is at least partially recoverable from distributional language statistics, consistent with Dove's (2024) argument that some aspects of conceptual structure are "ungrounded."

*What it would mean if disconfirmed*: The three-factor structure depends on embodied experience or neural architecture in ways that distributional statistics alone cannot recover.

**H2: The internal factor will show the strongest LLM correspondence.**

*Rationale*: Internal-dimension concepts (emotion, morality, thought, social) are neurally processed in DMN regions decoupled from sensory input (Danan [Levinson], 2021), and LLMs show the strongest alignment with human representations on non-sensorimotor features (Xu et al., 2025). Therefore, the representational structure of internal-dimension concepts should be most recoverable from language alone.

*What it would mean if confirmed*: The internal dimension of abstract semantics may be fundamentally linguistic rather than embodied in nature—or, more precisely, the representational geometry imposed by language co-occurrence statistics may approximate the geometry imposed by the neural processing of self-referential, social, and emotional concepts.

*What it would mean if disconfirmed*: Even non-sensorimotor abstract concepts may require experiential (interoceptive, social-interactive) grounding that language alone cannot provide. This would be important evidence against strong distributional semantics positions.

**H3: The concrete factor will show the weakest LLM correspondence.**

*Rationale*: Concrete features (visual form, color, sound, touch, smell, self-motion) depend on sensorimotor experience, which LLMs lack. Xu et al. (2025) demonstrated this gradient directly at the individual-feature level.

*What it would mean if confirmed*: Replication of Xu et al. (2025) at the level of representational geometry rather than individual feature correlations, providing a different and more stringent test of the sensorimotor grounding gap.

### 4.2 Secondary predictions

**H4: Multimodal models will selectively improve on the concrete factor.**

*Rationale*: Models with visual training should partially close the gap on visual, color, and form features while leaving internal features unchanged (since internal features are already well-recovered from language).

**H5: Layer-wise analysis will show dissociable depth profiles for internal versus concrete factors.**

*Rationale*: Higher transformer layers, which align best with higher-order brain regions including DMN (Caucheteux & King, 2022), should show peak alignment with the internal factor. Lower layers should show relatively stronger alignment with concrete features.

### 4.3 Exploratory analyses

We will also conduct several exploratory analyses that are theoretically motivated but for which we do not have strong directional predictions:

- **Individual concept analysis**: Which specific words show the largest LLM-human divergence on each factor? We predict that concepts simultaneously high on internal and concrete features (e.g., "pain," "hunger") may be particularly informative about the limits of distributional semantics.

- **Cross-model consistency**: How consistent is the factor structure across different LLM families? High consistency would suggest the factor structure reflects general properties of language; low consistency would suggest it is architecture- or training-dependent.

- **Prompt sensitivity**: Does the factor structure in prompt-based ratings change substantially with prompt variation? High sensitivity would raise concerns about the validity of prompt-based evaluation.

## 5. Methodological Challenges and Mitigations

### 5.1 The feature-to-activation mapping problem

The most significant methodological challenge is that behavioral semantic features (rated on 7-point scales) do not map one-to-one onto learned LLM representations. Human raters can introspect on whether a word feels "emotional" or "spatial"; LLM hidden states encode these properties (if they do) in distributed, potentially entangled ways.

We address this in two ways. First, the prompt-based rating approach (following Xu et al., 2025) asks LLMs to produce ratings in the same format as human participants, providing a behaviorally-comparable output measure. Second, the RSA approach on hidden states does not require identifying individual features—it tests whether the *relational structure* among concepts imposed by each factor is reflected in the geometry of hidden-state activations, regardless of how individual features are encoded.

### 5.2 Concerns about prompt-based evaluation validity

Xu et al. (2025) validated their prompt-based approach by demonstrating that LLM ratings were internally consistent across sessions and showed meaningful patterns when analyzed at the group level. We will replicate these validation checks and add two additional controls: (a) testing whether LLM ratings are sensitive to prompt wording variation, and (b) testing whether ratings shift meaningfully with temperature parameter variation (higher temperature = more stochastic sampling).

A deeper concern, raised by Millière and Mollo (2024), is whether prompt-based ratings reflect genuine internal representations or merely the model's ability to predict what a human rater would say. This concern is mitigated in our study by the hidden-state RSA, which bypasses the output generation process entirely. If the factor structure is present in hidden states (not just prompt outputs), this addresses the "parrot" concern more directly.

### 5.3 Statistical power considerations

With 400 words and pairwise comparisons (yielding 79,800 unique pairs), RSA analyses will have high power for detecting moderate effect sizes. The extension to 600 words increases pair count to 179,700. Based on effect sizes observed in Danan (2021) for the neural RSA (where significant clusters were detected at voxelwise p < .005 with approximately 100 words per condition), we expect adequate power. However, we will conduct formal power analyses using simulated data with varying levels of factor recovery to establish minimum detectable effect sizes.

### 5.4 Multiple comparisons

With three factors, multiple LLMs, multiple layers, and multiple comparison approaches, the family-wise error rate is substantial. We will control for this using the following strategy: (a) primary hypotheses (H1–H3) will be tested with Holm-Bonferroni correction across the three factors; (b) secondary hypotheses (H4–H5) will be tested with separate Holm-corrected families; (c) exploratory analyses will be reported with uncorrected p-values clearly labeled as exploratory.

## 6. Relation to Existing Work

### 6.1 Positioning relative to Xu et al. (2025)

Our study extends Xu et al. (2025) in three specific ways. First, we use a more granular feature model (14 features vs. the Glasgow/Lancaster norm dimensions) that has been validated neurally, not just behaviorally. Second, we test the *factor structure* (internal/external/concrete) rather than individual dimensions, asking whether LLMs recover the organizational principles of the semantic space rather than just individual feature values. Third, we include hidden-state RSA for open models, testing whether the factor structure is present in internal representations rather than just behavioral outputs.

### 6.2 Positioning relative to brain-LLM RSA work

Our study complements the Caucheteux and King (2022) and Goldstein et al. (2024) brain-LLM alignment work by testing a specific semantic organizational principle rather than aggregate alignment. If the internal/external factor structure is confirmed in LLMs, a natural follow-up study would apply the same factor-specific RSA to jointly model brain and LLM representations, testing whether the brain regions that encode the internal factor (dmPFC, PCC, AG) are the same regions where LLM-brain alignment is strongest.

### 6.3 Positioning relative to the grounding debate

The study is explicitly designed to adjudicate between positions in the grounding debate. A strong embodied cognition position predicts that all three factors should be poorly recovered by LLMs, since all conceptual knowledge depends on sensorimotor experience (Barsalou, 2008). Dove's (2024) "symbol ungrounding" position predicts that the internal factor should be well-recovered (since internal concepts are inherently linguistic/ungrounded) while the concrete factor should not be. A strong distributional semantics position predicts that all three factors should be recovered, since they reflect statistical regularities in language. Our study tests these predictions against each other using a single, well-controlled paradigm.

## 7. Limitations

**We are testing representational geometry, not understanding.** Even if LLMs perfectly recapitulate the three-factor structure, this does not demonstrate that they "understand" abstract concepts the way humans do. The phenomenological and functional questions remain separate from the representational-geometric question. We are explicit about this constraint.

**The feature model is not exhaustive.** The 14-feature model captures important variance in semantic space but does not include all possible features. For example, features related to interoception (heartbeat awareness, proprioception) and metacognition (certainty, source monitoring) are not included. These features may be particularly relevant to the internal dimension and could differentiate human and LLM representations in ways our model misses.

**Closed-model access limitations.** For GPT-4 and Claude, we cannot extract hidden states, limiting us to prompt-based and embedding-level analyses. This is a significant constraint, as prompt-based outputs may reflect learned response patterns rather than genuine internal representations. Our mitigation (testing open models in parallel) is necessary but not fully equivalent, since different model families may have qualitatively different internal organizations.

**The factor structure may be language-dependent.** The three-factor model was validated in English. Whether the internal/external/concrete distinction is universal or language-specific is an open empirical question. Cross-linguistic validation would strengthen the framework but is beyond the scope of this proposal.

## 8. Significance

This study would provide the first direct test of whether LLMs develop the internal/external/concrete organizational structure that characterizes human abstract semantic representation. If the internal factor is preferentially recovered—as predicted by the convergent logic of Dove's (2024) ungrounding hypothesis, the DMN-internal dimension mapping (Danan [Levinson], 2021), and the Xu et al. (2025) sensorimotor gradient—this would constitute evidence that the representational geometry of internally-directed, socially-embedded, emotionally-valenced concepts is substantially recoverable from language statistics.

This finding would have implications for both cognitive science and AI. For cognitive science, it would suggest that the brain's organization of abstract concepts along the internal/external axis partially reflects the statistical structure of language exposure, not (only) the structure of embodied experience. For AI, it would identify the internal dimension as the domain where LLMs have the strongest claim to human-like conceptual representation—and, by implication, the concrete and external dimensions as the domains where grounding interventions (multimodal training, embodiment) are most needed.

More practically, a validated feature-based model for evaluating LLM semantic representations would provide a diagnostic tool that goes beyond aggregate accuracy benchmarks. Rather than asking "Does the model understand this concept?" we could ask "Which *features* of this concept does the model represent, and which are missing?" This granular diagnostic is directly useful for understanding when and why LLMs succeed or fail at semantic tasks.

---

## References

Antonello, R., & Huth, A. G. (2024). Scaling laws for language encoding models in fMRI. *Advances in Neural Information Processing Systems*, 36.

Barsalou, L. W. (2008). Grounded cognition. *Annual Review of Psychology*, 59, 617–645.

Binder, J. R., Conant, L. L., Humphries, C. J., Fernandino, L., Simons, S. B., Aguilar, M., & Desai, R. H. (2016). Toward a brain-based componential semantic representation. *Cognitive Neuropsychology*, 33(3-4), 130–174.

Caucheteux, C., & King, J.-R. (2022). Brains and algorithms partially converge in natural language processing. *Communications Biology*, 5(1), 134.

Danan [Levinson], H. J. (2021). *The neural representation of abstract concepts in typical and atypical cognition* [Doctoral dissertation, Rutgers University–Newark].

Dove, G. (2024). Symbol ungrounding: What the successes (and failures) of large language models reveal about human cognition. *Philosophical Transactions of the Royal Society B*, 379(1915), 20230149.

Goldstein, A., Zada, Z., Buchnik, E., Schain, M., Price, A., Aubrey, B., ... & Hasson, U. (2022). Shared computational principles for language processing in humans and deep language models. *Nature Neuroscience*, 25(3), 369–380.

Goldstein, A., Ham, E., Schain, M., Nastase, S. A., Zada, Z., Dabush, A., ... & Hasson, U. (2024). Alignment of brain embeddings and artificial contextual embeddings in natural language points to common geometric patterns. *Nature Communications*, 15, 2768.

Grand, G., Blank, I. A., Pereira, F., & Fedorenko, E. (2022). Semantic projection recovers rich human knowledge of multiple object features from word embeddings. *Nature Human Behaviour*, 6(7), 975–987.

Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. *Structural Equation Modeling*, 6(1), 1–55.

Huth, A. G., Nishimoto, S., Vu, A. T., & Gallant, J. L. (2012). A continuous semantic space describes the representation of thousands of object and action categories across the human brain. *Neuron*, 76(6), 1210–1224.

Huth, A. G., de Heer, W. A., Griffiths, T. L., Theunissen, F. E., & Gallant, J. L. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex. *Nature*, 532(7600), 453–458.

Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008). Representational similarity analysis—Connecting the branches of systems neuroscience. *Frontiers in Systems Neuroscience*, 2, 4.

Millière, R., & Mollo, D. C. (2024). The vector grounding problem. *arXiv preprint*, arXiv:2304.01481v3.

Schrimpf, M., Blank, I. A., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., ... & Fedorenko, E. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. *Proceedings of the National Academy of Sciences*, 118(45), e2105646118.

Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., ... & Becchio, C. (2024). Testing theory of mind in large language models and humans. *Nature Human Behaviour*, 8(7), 1285–1295.

Troche, J., Crutch, S., & Reilly, J. (2017). Defining a conceptual topography of word concreteness: Clustering properties of emotion, sensation, and magnitude among 750 English words. *Frontiers in Psychology*, 8, 1787.

Xu, Q., Peng, Y., Nastase, S. A., Chodorow, M., Wu, M., & Li, P. (2025). Large language models without grounding recover non-sensorimotor but not sensorimotor features of human concepts. *Nature Human Behaviour*, 9(9), 1871–1886.

---

*Correspondence: Hillary J. Danan. [email to be added]*

*Acknowledgments: The 14-feature semantic model and original behavioral/neural validation data were collected under the mentorship of Dr. William Graves at Rutgers University–Newark. I thank Drs. Miriam Rosenberg-Lee, Mauricio Delgado, Michael Cole, and Lisa Conant for their contributions to the original research program.*

*Competing interests: The author declares no competing interests.*

*Data availability: Original behavioral ratings from 400 word concepts and associated fMRI data are available upon reasonable request. Code for RSA pipeline will be made available on GitHub upon publication.*

*Open science statement: This study will be preregistered prior to data collection. All analysis code, de-identified data, and model outputs will be shared publicly upon completion.*

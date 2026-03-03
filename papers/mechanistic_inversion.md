# The Mechanistic Inversion: Opposite Representational Deficits in Autism and Large Language Models Converge on the Computational Difficulty of Abstract Social Cognition

**Hillary J. Danan**

*Working Draft — March 2026*

---

## Abstract

Autism spectrum disorder (ASD) and large language models (LLMs) exhibit strikingly similar behavioral profiles in abstract social cognition—both struggle with figurative language, social inference, and context-dependent pragmatics—yet arrive at these failures through opposite representational mechanisms. Neuroimaging evidence demonstrates that ASD involves over-recruitment of concrete, perceptual processing regions (thalamus, ventral anterior temporal lobe) when abstract social-semantic networks should be engaged (Danan [Levinson], 2021). LLMs, conversely, lack any perceptual or sensorimotor grounding whatsoever and show systematic divergence from human representations that increases from non-sensorimotor to sensory to motor domains (Xu et al., 2025). Here I argue that this *mechanistic inversion*—too much concrete grounding versus none at all—producing convergent behavioral deficits constitutes evidence that abstract social cognition is computationally difficult independent of substrate. I connect this framework to Dove's (2024) "symbol ungrounding" hypothesis and prior neuroimaging evidence that abstract, self-referential concepts map onto the default mode network (DMN)—a network defined by its decoupling from external sensory input. The inversion framework generates testable predictions: (1) LLMs should align best with human neural representations in DMN regions processing internal/self-referential concepts, where grounding is least required; (2) ASD and LLM failures should dissociate on tasks requiring perceptual simulation versus tasks requiring compositional abstraction from social context; and (3) multimodal models should close the gap with human representations selectively in external/concrete dimensions while leaving internal/social dimensions relatively unchanged. This perspective reframes the grounding debate and offers a neuroscience-derived diagnostic framework for understanding AI failure modes.

---

## 1. Introduction

A peculiar convergence has emerged across two very different fields. In clinical neuroscience, decades of research document that individuals with autism spectrum disorder (ASD) struggle with figurative language comprehension, social inference, and pragmatic communication, despite intact or superior performance on tasks requiring pattern recognition and detail-oriented processing (Kalandadze et al., 2018; Vulchanova et al., 2015). In artificial intelligence, large language models—systems that process language with unprecedented fluency—show a remarkably similar profile: strong performance on literal, factual, and pattern-matching tasks, paired with fragile and sometimes illusory competence on social reasoning, figurative language, and pragmatic inference (Shapira et al., 2024; Strachan et al., 2024).

This behavioral overlap has been noted informally but has not been subjected to rigorous theoretical analysis. In this paper, I argue that examining the *mechanisms* underlying these convergent behavioral profiles—rather than just the profiles themselves—reveals something important about why abstract social cognition is computationally hard. The central claim is what I term the *mechanistic inversion*: ASD and LLMs fail at similar tasks for opposite reasons. ASD involves over-reliance on concrete, perceptual, bottom-up processing strategies when top-down, abstract, socially-specialized networks should be engaged. LLMs fail because they have no perceptual or embodied grounding at all. The behavioral surface looks similar; the representational deficit is inverted.

This inversion is not merely a curious parallel. It offers three contributions. First, it provides a principled framework for understanding which aspects of abstract cognition depend on sensorimotor grounding and which do not—directly informing the grounding debate in AI and cognitive science. Second, it generates testable predictions about where brain-LLM alignment should be strongest and weakest, building on the finding that abstract concepts organize along an internal-to-self versus external-to-self dimension in the human brain (Danan [Levinson], 2021; Troche et al., 2017). Third, it offers a neuroscience-derived diagnostic vocabulary for categorizing AI failure modes in semantic processing—one that goes beyond "the model got it wrong" to specify *how* the representational strategy fails.

## 2. The Neural Architecture of Abstract Semantics

### 2.1 The internal/external semantic axis

Human conceptual knowledge is not organized as a simple concrete-to-abstract continuum. Behavioral and neuroimaging evidence supports a multidimensional space in which abstract concepts themselves differentiate along at least two axes: an *internal-to-self* dimension encompassing emotion, morality, social relationships, and thought, and an *external-to-self* dimension encompassing space, time, quantity, and causality (Troche et al., 2017; Danan [Levinson], 2021).

Using a 14-feature semantic model rated across 400 concept words, followed by fMRI with representational similarity analysis (RSA), I previously demonstrated three key findings (Danan [Levinson], 2021). First, exploratory factor analysis on behavioral ratings replicated the three-factor structure (internal, external, concrete) reported by Troche et al. (2017), with high internal consistency. Second, principal component analysis of neural data revealed a 3-component space underlying semantic content, with the first component showing strong correspondence to the internal factor—correlating positively with morality, thought, emotion, and polarity ratings, and negatively with sensory features. Third, the neural regions associated with this internal component (dorsomedial prefrontal cortex [dmPFC], middle cingulate cortex/posterior cingulate cortex [PCC], and inferior parietal lobule near angular gyrus) correspond closely to core hubs of the default mode network (DMN).

This mapping is significant because the DMN is, by definition, a network that activates during internally-directed cognition and deactivates during externally-directed, perceptually-demanding tasks (Raichle, 2015). The internal semantic dimension, then, is processed by a network that is functionally *decoupled* from sensory input. This observation becomes central to the argument developed below.

### 2.2 Abstract semantics in ASD: Concrete processing invades abstract space

In a series of studies examining semantic processing in ASD (Danan [Levinson], 2021), I found convergent evidence that ASD involves atypical over-extension of concrete/perceptual processing into abstract semantic territory.

At the network level, resting-state functional connectivity analysis using the ABIDE-II dataset revealed that the right ventral anterior temporal lobe (vATL)—a region associated with concrete semantic processing (Hoffman & Lambon Ralph, 2018)—showed aberrant connectivity in ASD. Specifically, the right vATL was positively connected to the right anterior superior temporal sulcus (aSTS, an abstract social processing region) in ASD, whereas in neurotypical (NT) controls, the right superior ATL (sATL) showed this connectivity pattern (Danan [Levinson], 2021; cf. Jackson et al., 2016). The right vATL also showed atypical positive connectivity with the PCC in ASD, a region frequently found to be hypo-activated during social processing in ASD (Padmanabhan et al., 2017).

At the task level, when participants processed figurative versus literal phrases in the scanner, the ASD group showed significantly greater activation in the thalamus for figurative relative to literal phrases. In NT, this thalamic region is associated with perceptual processing of visual stimuli and direct, concrete experience (Christensen et al., 2006). This finding suggests that individuals with ASD recruit perceptual/concrete processing regions to perform tasks that, in NT, engage abstract linguistic networks.

Follow-up ROI analyses partly confirmed this pattern: the ASD group showed marginally greater activation in the right vATL for social relative to nonsocial phrases compared to NT, consistent with the hypothesis that the concrete semantic network "over-extends" into abstract semantic space in ASD. Multivariate RSA results further revealed that NT participants showed neural correspondence to social phrase-level features in the bilateral fusiform gyri (a region linked to face processing; Blonder et al., 2004), while the ASD group showed correspondence to nonsocial phrase features in the right supplementary motor area—consistent with fundamentally different representational strategies for the same stimuli.

The overall pattern is clear: when abstract, social, or figurative semantic demands are placed on the ASD system, it compensates by deploying concrete, perceptual processing resources. The abstract semantic networks that NT brains recruit for these tasks are either under-engaged or differently organized.

## 3. LLMs: The Mirror Image

### 3.1 The systematic sensorimotor gap

If ASD represents a system with intact perceptual grounding that over-applies it to abstract contexts, LLMs represent the inverse: a system with no perceptual grounding that must handle all concepts—including concrete ones—through distributional language statistics alone.

Xu et al. (2025) provided the most comprehensive empirical demonstration of this asymmetry. Comparing multidimensional representations of approximately 4,442 lexical concepts between humans and state-of-the-art LLMs (GPT-3.5, GPT-4, PaLM, Gemini), they found a systematic gradient: model-human alignment was strongest in non-sensorimotor domains (emotional arousal, valence, concreteness, familiarity), weaker in sensory domains (vision, audition, touch, taste/smell), and minimal in motor domains (hand, foot, mouth actions). This gradient was consistent across all models tested and persisted after controlling for word concreteness.

Critically, models that included visual training (GPT-4, Gemini) showed selectively enhanced alignment in vision-related dimensions, directly demonstrating that the deficit is tied to the absence of specific modalities rather than a general representational limitation.

### 3.2 Theory of mind: Fragile competence through surface heuristics

The parallel to ASD in social cognition is perhaps most striking in theory of mind (ToM). Strachan et al. (2024) tested GPT-4 and LLaMA-2 against 1,907 human participants on a comprehensive ToM battery including false beliefs, indirect requests, irony, strange stories, and faux pas detection. GPT-4 matched or exceeded average human performance on most tasks but struggled specifically with faux pas detection—recognizing when a speaker unwittingly says something socially hurtful. Faux pas detection is also a well-documented area of difficulty in ASD (Baron-Cohen et al., 1999).

However, follow-up analyses revealed that GPT-4's faux pas failures reflected hyperconservative alignment guardrails rather than a genuine inability to represent the relevant mental states: when questions were rephrased in terms of likelihood rather than categorical judgment, GPT-4 performed perfectly (Strachan et al., 2024). This result is important for the mechanistic inversion argument because it reveals a qualitatively different *kind* of failure from ASD. In ASD, the difficulty with faux pas reflects genuine processing differences in social-semantic networks. In LLMs, it can reflect training-imposed behavioral patterns that obscure underlying competence—or lack thereof.

More fundamentally, Shapira et al. (2024) demonstrated that LLM ToM competence is often illusory, driven by surface heuristics rather than robust social reasoning. Across six different ToM tasks, they showed that models relied on shallow cues rather than genuine mentalizing—a pattern they termed the "Clever Hans" effect after the horse that appeared to perform arithmetic by reading its handler's body language. Ullman (2023) reinforced this finding by showing that trivial, logically irrelevant modifications to false-belief vignettes caused models to fail on items they had previously answered correctly.

### 3.3 The inversion crystallized

The behavioral convergence between ASD and LLMs can now be stated precisely:

**In ASD**: The system *has* sensorimotor and perceptual grounding but *over-applies* it in abstract contexts. Concrete processing regions (thalamus, vATL) are recruited for figurative and social language tasks where NT brains engage abstract semantic networks (perisylvian cortices, IFG, mPFC, ATL, AG).

**In LLMs**: The system *lacks* sensorimotor and perceptual grounding entirely. It can approximate abstract, non-sensorimotor semantic relationships through distributional statistics but systematically fails on concepts that, in humans, depend on embodied experience (Xu et al., 2025).

**Both** show: difficulty with figurative language, pragmatic inference, faux pas detection, and context-dependent social reasoning, paired with intact or superior performance on literal, pattern-based, and detail-oriented tasks.

**Both** show fragility under adversarial testing: ASD performance on abstract social tasks degrades when tasks require integration across social context (Vulchanova et al., 2015); LLM performance degrades under trivial perturbation of task surface features (Ullman, 2023; Shapira et al., 2024).

**Both** exhibit what might be called a "Clever Hans" pattern: apparent competence on standardized tests that breaks down under systematic probing, because the underlying processing strategy uses available but insufficient representational resources (concrete perception in ASD; statistical pattern matching in LLMs) as substitutes for genuinely abstract social-semantic computation.

## 4. Implications for the Grounding Debate

### 4.1 Symbol ungrounding and the DMN

The mechanistic inversion illuminates a nuanced resolution to the grounding debate. Dove (2024) introduced the concept of "symbol ungrounding"—the idea that language provides humans with access to a form of cognition that is productively *detached* from sensorimotor experience. Rather than treating grounded and distributional semantics as competitors, Dove argues that human cognition requires both: grounded representations for concepts tied to perception and action, and "ungrounded" linguistic representations for concepts that cannot be directly perceived (justice, morality, democracy, irony).

This framework maps onto the internal/external axis with remarkable precision. The internal dimension—emotion, morality, thought, social relationships—encompasses concepts that are, by their nature, not directly perceivable through sensory channels. You cannot see justice, touch morality, or hear a belief. These concepts are processed in the DMN, a network defined by its decoupling from external sensory input. The external dimension—space, time, quantity—encompasses concepts that, while often abstract, maintain stronger ties to perceivable magnitudes and spatial relationships.

The implications for LLMs follow directly. If internal/self-referential concepts were never primarily grounded in perception, then a system trained exclusively on language should be *most* competent at representing precisely these concepts. Xu et al.'s (2025) finding that LLMs align best with human representations on non-sensorimotor dimensions—including emotional, evaluative, and social-cognitive features—is exactly what this framework predicts.

### 4.2 A prediction the dissertation data anticipated

The following convergence is notable. In 2021, I demonstrated that abstract concepts with high internal-to-self features (emotion, morality, thought, social) are processed in DMN regions that are functionally decoupled from sensory input (Danan [Levinson], 2021). In 2024, Dove articulated the theoretical position that language provides access to "ungrounded cognition" for concepts that cannot be perceived. In 2025, Xu et al. empirically showed that LLMs—systems with no sensory grounding—best approximate human representations on exactly the non-sensorimotor, evaluative, and abstract dimensions that constitute the internal factor.

This convergence suggests a hypothesis: **the internal/self-referential dimension of abstract semantics is the domain where distributional language statistics most closely approximate the neural representations of human concepts, precisely because these concepts are neurally represented in networks that are themselves decoupled from direct sensory input.**

This is not to say that LLMs "understand" internal concepts the way humans do—the phenomenological question is separate from the representational one. Rather, it predicts that RSA comparing LLM hidden-state representations to fMRI data should show the highest brain-LLM correspondence in DMN regions for internal-dimension concepts, and the lowest correspondence in sensorimotor regions for concrete concepts. This prediction is testable and, to our knowledge, has not been directly examined.

## 5. Testable Predictions

The mechanistic inversion framework generates several specific, falsifiable predictions:

**Prediction 1: Selective brain-LLM alignment by semantic dimension.** If LLM representations are compared to neural representations using RSA, alignment should be highest for internal-dimension concepts (emotion, morality, thought, social) in DMN regions, intermediate for external-dimension concepts (space, time, quantity) in task-positive network regions, and lowest for concrete concepts in sensorimotor regions. Existing evidence from Caucheteux and King (2022) showing that higher transformer layers best predict frontoparietal activity is consistent with this prediction but has not been tested with the internal/external dimension specifically.

**Prediction 2: ASD-LLM dissociation on perceptual versus compositional tasks.** ASD and LLM failures should dissociate on tasks that orthogonally vary perceptual simulation demands and compositional abstraction demands. Specifically: (a) on tasks requiring perceptual simulation for comprehension (e.g., understanding action verbs like "grasp," processing spatial metaphors grounded in body experience), LLMs should fail while ASD should succeed; (b) on tasks requiring compositional abstraction from social context (e.g., interpreting faux pas, understanding irony in social settings), both should struggle; (c) on tasks requiring integration of perceptual detail into abstract wholes (e.g., understanding metaphors that link sensory experience to abstract emotion), ASD should show the pattern of concrete region recruitment documented above, while LLMs should show a qualitatively different error pattern reflecting statistical approximation rather than perceptual over-application.

**Prediction 3: Multimodal models should selectively close the external/concrete gap.** Adding visual or sensorimotor inputs to LLMs should improve alignment with human representations selectively on the external and concrete dimensions, while leaving internal-dimension alignment relatively unchanged (since internal concepts are already well-represented through language alone). Xu et al.'s (2025) finding that visual training selectively enhanced alignment on vision-related dimensions is consistent with this prediction, but it has not been tested using the full internal/external/concrete factor structure.

**Prediction 4: ASD connectivity patterns predict LLM representation gaps.** The specific regions where ASD shows over-connectivity of concrete semantic networks into abstract processing areas (right vATL to aSTS, right vATL to PCC) should correspond to regions where LLM-brain alignment is weakest—since these are the regions where concrete processing substitutes for abstract processing that LLMs cannot perform via a different route.

## 6. Limitations and Honest Caveats

Several important limitations constrain this framework and must be acknowledged.

**The analogy is structural, not mechanistic.** ASD involves a biological brain with specific neural architecture; LLMs are statistical models with transformer architecture. Saying they "fail similarly" does not imply they fail for similar computational reasons at the implementation level. The claim is more constrained: both converge on the behavioral difficulty of abstract social cognition because both lack the *appropriate representational strategy* for that domain, and both compensate with available but insufficient alternatives.

**The ASD neuroimaging results have statistical limitations.** The between-group comparisons in my dissertation studies were underpowered (approximately 20 participants per group) and several key results were at uncorrected thresholds or marginally significant after correction for multiple comparisons. The patterns described here—thalamic recruitment for figurative language, right vATL over-extension—are real trends consistent with existing literature, but they require replication with larger samples. The framework's strength lies in the *convergence* across multiple analytic approaches (univariate, RSA, resting-state connectivity), not any single underpowered contrast.

**LLM capabilities are rapidly evolving.** The ToM and figurative language performance of frontier LLMs has improved substantially between GPT-3.5 and GPT-4 (Strachan et al., 2024), and further improvements may narrow the behavioral gaps described here. This does not invalidate the mechanistic inversion—it specifies it further. As LLMs improve on social-cognitive benchmarks, the question becomes whether improvement reflects genuine representational change or more sophisticated surface heuristics.

**The "Clever Hans" critique applies bidirectionally.** Just as LLM ToM performance may reflect heuristics rather than genuine mentalizing (Shapira et al., 2024), some ASD ToM performance may reflect learned compensatory strategies rather than the modular ToM processes assumed by classical frameworks (Livingston et al., 2019). The mechanistic inversion framework is compatible with this possibility—it argues about representational strategies, not modular cognitive capacities.

**The internal/external axis has not been tested in LLMs.** This is the most important limitation and also the most important opportunity. The predictions in Section 5 are untested. The framework stands or falls on whether the 14-feature semantic model, when applied to LLM hidden states via RSA, reveals the predicted pattern of selective alignment. This is the subject of a companion proposal (Danan, 2026, in preparation).

## 7. Conclusion

The mechanistic inversion between ASD and LLMs is not a metaphor—it is a precise, testable claim about representational strategies. ASD over-recruits concrete/perceptual processing for abstract social cognition because its abstract semantic networks are atypically organized. LLMs approximate abstract social cognition through distributional statistics without any perceptual processing at all. Both arrive at similar behavioral profiles because abstract social cognition is genuinely computationally difficult: it requires representational resources that cannot be fully substituted by either perceptual processing or statistical pattern matching.

The framework connects to the grounding debate through a specific route: the internal/self-referential dimension of abstract semantics is neurally processed in networks (DMN) that are functionally decoupled from sensory input, suggesting that these concepts were never primarily grounded in perception. LLMs should therefore align best with human neural representations for these concepts—a prediction supported by existing data (Xu et al., 2025) but not yet tested at the neural level with the appropriate semantic dimensions.

More broadly, the inversion framework offers cognitive neuroscience and AI research a shared vocabulary. When an LLM fails at social inference, we can ask whether the failure pattern looks like "concrete compensation" (surface-level pattern matching substituting for genuine abstraction) or "genuine representational gap" (no available strategy at all). When an ASD individual struggles with figurative language, we can ask whether the neural pattern of concrete region recruitment has a computational analog in how LLMs process the same stimuli. These cross-domain comparisons are not just intellectually interesting—they are empirically tractable through the shared methodology of RSA.

---

## References

Baron-Cohen, S., O'Riordan, M., Stone, V., Jones, R., & Plaisted, K. (1999). Recognition of faux pas by normally developing children and children with Asperger syndrome or high-functioning autism. *Journal of Autism and Developmental Disorders*, 29(5), 407–418.

Binder, J. R., Desai, R. H., Graves, W. W., & Conant, L. L. (2009). Where is the semantic system? A critical review and meta-analysis of 120 functional neuroimaging studies. *Cerebral Cortex*, 19(12), 2767–2796.

Blonder, L. X., Smith, C. D., Davis, C. E., Kesler-West, M. L., Garrity, T. F., Avison, M. J., & Andersen, A. H. (2004). Regional brain response to faces of humans and dogs. *Cognitive Brain Research*, 20(3), 384–394.

Caucheteux, C., & King, J.-R. (2022). Brains and algorithms partially converge in natural language processing. *Communications Biology*, 5(1), 134.

Christensen, M. S., Ramsøy, T. Z., Lund, T. E., Madsen, K. H., & Rowe, J. B. (2006). An fMRI study of the neural correlates of graded visual perception. *NeuroImage*, 31(4), 1711–1725.

Danan [Levinson], H. J. (2021). *The neural representation of abstract concepts in typical and atypical cognition* [Doctoral dissertation, Rutgers University–Newark].

Dove, G. (2024). Symbol ungrounding: What the successes (and failures) of large language models reveal about human cognition. *Philosophical Transactions of the Royal Society B*, 379(1915), 20230149.

Hoffman, P., & Lambon Ralph, M. A. (2018). From percept to concept in the ventral temporal lobes: Graded hemispheric specialisation based on stimulus and task. *Cortex*, 101, 107–118.

Jackson, R. L., Hoffman, P., Pobric, G., & Lambon Ralph, M. A. (2016). The semantic network at work and rest: Differential connectivity of anterior temporal lobe subregions. *Journal of Neuroscience*, 36(5), 1490–1501.

Kalandadze, T., Norbury, C., Nærland, T., & Næss, K.-A. B. (2018). Figurative language comprehension in individuals with autism spectrum disorder: A meta-analytic review. *Autism*, 22(2), 99–117.

Livingston, L. A., Shah, P., & Happé, F. (2019). Compensatory strategies below the behavioural surface in autism: A qualitative study. *Molecular Autism*, 10(1), 47.

Padmanabhan, A., Lynch, C. J., Schaer, M., & Menon, V. (2017). The default mode network in autism. *Biological Psychiatry: Cognitive Neuroscience and Neuroimaging*, 2(6), 476–486.

Raichle, M. E. (2015). The brain's default mode network. *Annual Review of Neuroscience*, 38, 433–447.

Shapira, N., Levy, M., Alavi, S. H., Zhou, X., Choi, Y., Goldberg, Y., Sap, M., & Shwartz, V. (2024). Clever Hans or neural theory of mind? Stress testing social reasoning in large language models. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics* (pp. 2257–2273).

Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). Testing theory of mind in large language models and humans. *Nature Human Behaviour*, 8(7), 1285–1295.

Troche, J., Crutch, S., & Reilly, J. (2017). Defining a conceptual topography of word concreteness: Clustering properties of emotion, sensation, and magnitude among 750 English words. *Frontiers in Psychology*, 8, 1787.

Ullman, T. (2023). Large language models fail on trivial alterations to theory-of-mind tasks. *arXiv preprint*, arXiv:2302.08399.

Vulchanova, M., Saldaña, D., Chahboun, S., & Vulchanov, V. (2015). Figurative language processing in atypical populations: The ASD perspective. *Frontiers in Human Neuroscience*, 9, 24.

Xu, Q., Peng, Y., Nastase, S. A., Chodorow, M., Wu, M., & Li, P. (2025). Large language models without grounding recover non-sensorimotor but not sensorimotor features of human concepts. *Nature Human Behaviour*, 9(9), 1871–1886.

---

*Correspondence: Hillary J. Danan. [email to be added]*

*Acknowledgments: The neuroimaging studies described in Section 2 were conducted under the direction of Dr. William Graves at Rutgers University–Newark. I thank Drs. Miriam Rosenberg-Lee, Mauricio Delgado, Michael Cole, and Lisa Conant for their contributions to the original dissertation research.*

*Competing interests: The author declares no competing interests.*

*Data availability: Original fMRI data from the dissertation studies are available upon reasonable request. LLM alignment analyses proposed in Section 5 have not yet been conducted.*

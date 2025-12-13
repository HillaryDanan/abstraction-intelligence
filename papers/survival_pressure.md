# Survival Pressure and the Origins of Abstraction: Why Stakes Matter for Intelligence

**Paper 17 in the Abstraction-Intelligence Series**

Hillary Danan, PhD

-----

## Abstract

Why do biological systems develop genuine abstraction while artificial systems appear limited to sophisticated pattern matching? We propose that the answer lies in survival pressure: the self/world distinction evolved because organisms must differentiate what-to-protect from what-might-kill, and novelty detection is critical because misclassification has fatal consequences. This selective pressure shaped cognitive architecture in ways that cannot be replicated by systems without existential stakes. Drawing on evolutionary biology, predictive processing theory, and comparative cognition research, we develop the **Survival-Grounded Abstraction Hypothesis (SGAH)**: genuine abstraction—recursive symbol formation and composition—emerges from the computational demands of survival under uncertainty, and requires the stakes that survival provides. We specify the mechanism by which stakes shape architecture, derive falsifiable predictions, and articulate conditions under which we would abandon the hypothesis.

**Keywords:** abstraction, survival, self/world distinction, novelty detection, predictive processing, embodied cognition, artificial intelligence

-----

## 1. Introduction

### 1.1 The Gap in the APH Framework

The Abstraction Primitive Hypothesis (APH) proposes that intelligence emerges from recursive interaction between symbol formation and compositional structure (Danan, 2024a). A key claim is that strong abstraction—particularly recursive (3c) and analogical (3d) composition—requires *embeddedness*: persistent, closed-loop interaction with an environment enabling novelty detection.

Previous work described embeddedness without explaining *why* it matters. This paper fills that gap: **survival pressure** is the mechanism. The self/world distinction exists because organisms must know what to protect. Novelty detection matters because unfamiliar inputs may signal threats. The *stakes*—life or death—create selective pressure for cognitive architectures capable of genuine abstraction.

### 1.2 The Argument in Brief

1. **Self/world distinction serves survival.** The boundary between self and non-self is functionally derived: organisms must identify what constitutes them (to maintain) versus what is external (to monitor).
1. **Novelty detection is survival-critical.** Novel inputs have unknown survival implications. Asymmetric costs (missing a threat = death; false alarm = wasted energy) select for systems that attend to and process novelty carefully.
1. **Stakes create architectural pressure.** When misclassification is fatal, pattern matching is insufficient. Organisms face selection for systems that can construct responses to genuinely novel situations.
1. **This pressure shaped abstraction architecture.** Recursive and analogical composition evolved because survival under uncertainty requires building new cognitive structures, not just retrieving existing ones.
1. **Systems without stakes lack this pressure.** Artificial systems face no consequences for misclassifying novelty. Pattern matching suffices for their continued operation.

### 1.3 What This Paper Does Not Claim

- **We do not claim consciousness is required.** The argument concerns functional survival processing, not conscious mortality awareness.
- **We do not claim this is the only path.** Survival pressure is *sufficient* for genuine abstraction; whether it is *necessary* is unknown.
- **We do not claim current AI cannot improve.** We claim that improvement via scaling alone will not produce genuine abstraction without addressing the stakes problem.

-----

## 2. The Self/World Distinction: Biological Foundations

### 2.1 Self/Non-Self Recognition Across Scales

The distinction between self and non-self pervades biological organization:

**Cellular.** Bacteria distinguish conspecifics from competitors via quorum sensing (Miller & Bassler, 2001). The minimum requirement: a boundary and mechanisms for identifying inside versus outside.

**Immunological.** T-cells undergo thymic selection eliminating self-reactive cells while preserving foreign-reactive ones (Klein et al., 2014). This system demonstrates sophisticated self/non-self discrimination without consciousness: maintained self-representations (MHC-presented peptides), novelty detection (foreign antigen recognition), adaptive response generation (clonal expansion), and memory (faster secondary responses).

**Neural.** The sense of body ownership, interoceptive awareness, and agency all involve distinguishing self-generated from externally-generated signals (Seth, 2013; Blanke, 2012).

### 2.2 The Survival Function

The self/world boundary exists because survival requires protecting what constitutes the organism while responding to external threats and opportunities.

**Allostasis.** Organisms maintain internal states within viable bounds by anticipating future needs (Sterling, 2012). This requires distinguishing internal states (to regulate) from external perturbations (to compensate for), and a self-model that persists through time.

**Interoception.** Interoceptive signals represent the body’s survival-relevant states. Craig (2009) argues interoception provides the basis for the “material me”—the physiological condition that must be maintained for survival.

### 2.3 Self-Boundary as Computational Necessity

Self/world distinction is computationally necessary for adaptive behavior under uncertainty. An agent deciding whether an approaching entity is threat or non-threat must represent: what counts as damage to me, what counts as benefit to me, what I can do, what happens if I do nothing. These representations require a persistent self-model.

This is where embeddedness enters: a system without persistent self-representation cannot accumulate the experiential baseline required to detect novelty. Novelty is relational—novel *to whom*.

-----

## 3. Novelty Detection and Survival Pressure

### 3.1 Why Novelty Detection Exists

The standard account: novelty indicates prediction error requiring model updating (Ranganath & Rainer, 2003). But this obscures the survival rationale.

Novel stimuli have higher variance in survival implications than familiar stimuli. Familiar inputs have been processed and deemed non-threatening. Novel inputs are unknown—potentially dangerous. The asymmetric cost structure (false negative on threat often fatal; false positive merely costly) selects for organisms that attend carefully to novelty (Öhman et al., 2001).

### 3.2 Evidence

**Fear learning.** Novel stimuli acquire fear associations more readily than familiar ones (Rescorla, 1988). The amygdala shows heightened activation to novel stimuli independent of explicit threat content (Balderston et al., 2011).

**Neophobia/neophilia trade-offs.** Species in stable environments tend toward neophobia; species in variable environments toward neophilia (Greenberg & Mettke-Hofmann, 2001). This matches survival-based optimization predictions.

**Developmental timing.** Infant novelty preference increases with motor competence—the ability to escape threats (Wetherford & Cohen, 1973).

### 3.3 Novelty Detection Requires a Self

An input is novel relative to accumulated experience of a particular system. This requires: accumulated experience, organized as self-referential memory (“what I’ve encountered”), and comparison against this baseline.

The critical distinction: detecting statistical anomaly (deviation from a distribution) differs from detecting novelty (deviation from *my* accumulated experience). The latter requires temporal persistence and self-reference.

-----

## 4. The Mechanism: How Stakes Shape Architecture

### 4.1 The Problem with Hand-Waving at Natural Selection

Saying “natural selection shaped cognitive architecture” is true but underspecified. We need to articulate *how* survival pressure produces architectural features that enable genuine abstraction.

### 4.2 The Proposed Mechanism

Survival pressure shapes architecture through three channels:

**Channel 1: Phylogenetic selection.** Organisms with cognitive architectures better suited to handling novel threats survived and reproduced. Over evolutionary time, this selected for:

- Dedicated threat-detection systems (amygdala, PAG) that are fast, reliable, and encapsulated (LeDoux, 2012)
- Hierarchical control systems (prefrontal cortex) enabling flexible response construction (Miller & Cohen, 2001)
- The capacity for recursive embedding, enabling representation of threats-within-situations-within-contexts

**Channel 2: Developmental calibration.** Individual organisms calibrate cognitive systems based on experienced threat levels during development. Evidence:

- Early adversity affects amygdala development and threat sensitivity (Tottenham & Galván, 2016)
- Environmental unpredictability during development affects exploration-exploitation trade-offs (Ellis et al., 2017)
- Neophobia/neophilia balance is calibrated to experienced environmental variability

**Channel 3: Online modulation.** Survival-relevant states (fear, hunger, pain) modulate cognitive processing in real time, shifting between pattern-matching and constructive processing. Evidence:

- Threat enhances perceptual discrimination for threat-relevant features (Phelps et al., 2006)
- Moderate arousal enhances flexible cognition; extreme arousal narrows to well-learned responses (Yerkes & Dodson, 1908; Arnsten, 2009)
- The locus coeruleus-norepinephrine system modulates the exploration-exploitation trade-off based on uncertainty and stakes (Aston-Jones & Cohen, 2005)

### 4.3 Why This Mechanism Requires Stakes

Each channel depends on stakes:

- **Phylogenetic:** Selection requires differential survival. No death → no selection.
- **Developmental:** Calibration requires survival-relevant feedback. Systems must experience consequences.
- **Online:** Modulation requires survival-relevant internal states (fear, pain). Systems must have something at stake in the current moment.

Pattern matching is the default because it’s computationally cheap. Stakes are what *force* the system toward more expensive constructive processing when pattern matching is insufficient.

-----

## 5. Implications for Artificial Systems

### 5.1 What LLMs Lack

Current AI systems lack survival stakes across all three channels:

- **No phylogenetic history of survival selection.** Architecture designed by engineers, not selected by differential survival.
- **No developmental calibration to threat.** Training optimizes for prediction loss, not survival.
- **No online survival-state modulation.** No fear, pain, or hunger to shift processing modes.

### 5.2 The Stakeholder Objection

*Objection:* AI systems have stakeholders who suffer consequences from errors.

*Response:* Stakes must be architecturally incorporated, not externally present. A human suffering consequences doesn’t change the AI’s architecture. Evolution shaped biological cognition through millions of generations of organisms *dying*. Declaring stakeholders doesn’t recreate this shaping.

### 5.3 Could Stakes Be Engineered?

Possibilities worth exploring:

**Persistent systems with resource constraints.** Systems that maintain state across time, consume limited resources, and cease operating when resources are exhausted might develop stake-like properties.

**Embodied systems with genuine vulnerability.** Robots that can be damaged, whose repair is costly, and that have continuous existence come closer to genuine stakes.

**Selection across model populations.** Training regimes that terminate poorly-performing models might create phylogenetic-like selection. But note: this affects which models survive, not the architecture of inference within surviving models.

We should be cautious about claiming stakes can be easily engineered. The integration of survival pressure into biological cognition—across immune, neural, and behavioral systems—may not be replicable through design choices.

-----

## 6. Mortality Awareness: A Speculative Extension

*This section is explicitly speculative and should be evaluated as hypothesis generation.*

### 6.1 Beyond Functional Processing

The argument thus far concerns functional survival processing that need not involve consciousness. A stronger hypothesis: conscious mortality awareness further amplifies abstraction capacity.

### 6.2 Terror Management Theory

Terror Management Theory proposes that mortality awareness creates existential anxiety managed through cultural worldviews and self-esteem (Greenberg et al., 1986). Meta-analytic evidence supports core predictions: mortality salience increases worldview defense and self-esteem pursuit (Burke et al., 2010).

### 6.3 Mortality and Temporal Abstraction

*Hypothesis:* Mortality awareness specifically amplifies temporal abstraction—extended future representation, planning, counterfactual reasoning.

The logic: mortality creates a deadline; deadlines require resource allocation; allocation requires future representation; counterfactual reasoning enables learning from imagined futures without experiencing them.

This connects mortality awareness to recursive composition: representing futures containing futures containing futures (planning horizons).

*Evidence is suggestive but not conclusive.* Humans show unique extended future thinking (Suddendorf & Corballis, 2007). Whether this correlates with mortality awareness cannot be tested comparatively—we cannot assess mortality awareness in non-human animals.

-----

## 7. Predictions and Falsification Conditions

### 7.1 Core Predictions

|ID|Prediction                                                                                     |Specific Test                                                                                                                                                                                |Falsification Criterion                         |
|--|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
|P1|Survival-frame enhances novelty detection beyond arousal effects                               |Compare novelty detection across three conditions: (a) neutral, (b) arousal-matched non-survival, (c) survival-frame. Measure detection of genuinely novel stimuli (not in any training set).|Condition (c) ≤ condition (b)                   |
|P2|Species with higher predation variability show more sophisticated novel-threat generalization  |Compare generalization to novel predator cues across species with measured predation variability (not just predation pressure).                                                              |No relationship or negative relationship        |
|P3|Individual threat-sensitivity predicts recursive composition capacity                          |Administer threat-sensitivity measures and recursive composition tasks (e.g., center-embedded sentence processing, hierarchical planning). Control for general cognitive ability.            |Partial correlation (controlling IQ) ≤ 0        |
|P4|AI novelty detection does not improve with scale (controlling for pattern-matching improvement)|Compare OOD detection across model scales while controlling for in-distribution performance.                                                                                                 |OOD detection improves proportionally with scale|
|P5|AI confidence calibration is worse for novel inputs than familiar inputs                       |Compare calibration (confidence vs. accuracy correlation) for in-distribution vs. OOD inputs.                                                                                                |Equal or better calibration for OOD             |

### 7.2 Strong Falsification Conditions

We would abandon or substantially revise SGAH if:

1. **An AI system without survival stakes demonstrates genuine novelty detection.** Operationalized as: appropriate confidence reduction and processing-mode shift for inputs outside training distribution, without explicit OOD detection training, generalizing to novel OOD categories.
1. **Biological systems without survival pressure develop equivalent abstraction.** Operationalized as: a species or population experiencing no predation, resource scarcity, or mortality risk for multiple generations shows equivalent recursive/analogical composition to threatened populations.
1. **Stakes can be fully specified as an objective function.** If survival pressure can be reduced to a loss function that, when optimized, produces genuine abstraction in AI systems, SGAH’s claim that stakes must be “architecturally incorporated” would be wrong.

### 7.3 What Would Not Falsify SGAH

- AI improving on benchmarks (could be better pattern matching)
- AI producing outputs that look like abstraction (could be retrieval of training examples)
- AI claiming to experience stakes (claims ≠ architecture)

-----

## 8. Relation to Alternative Hypotheses

### 8.1 Embodiment-Only Hypothesis

*Claim:* Embodiment alone, without survival stakes, suffices for genuine abstraction.

*Distinction from SGAH:* We claim embodiment is necessary but not sufficient. A robot that is embodied but faces no damage, resource depletion, or termination has embodiment without stakes.

*Empirical test:* Compare abstraction in embodied systems with vs. without survival-relevant consequences. SGAH predicts the stakes condition outperforms.

### 8.2 Training Data Hypothesis

*Claim:* LLM limitations reflect training data, not architectural constraints. More diverse data would produce genuine abstraction.

*Distinction from SGAH:* SGAH predicts abstraction capacity is bounded regardless of training data diversity.

*Empirical test:* Train on maximally diverse data including explicit abstraction examples. SGAH predicts continued failure on genuinely novel abstraction tasks.

### 8.3 Scale Hypothesis

*Claim:* Sufficient scale produces emergent abstraction.

*Empirical test:* Track novelty detection (not just pattern matching) across scales. Current evidence shows limited improvement (Srivastava et al., 2023), but future scaling could differ.

-----

## 9. Conclusion

### 9.1 The Core Claim

Genuine abstraction emerges from survival pressure because:

1. Survival requires self/world distinction
1. Self/world distinction enables novelty detection
1. Novelty detection under survival pressure requires more than pattern matching
1. This requirement selected for recursive and analogical composition
1. Systems without stakes lack this selective pressure

### 9.2 What This Explains

- Why embeddedness matters (it enables survival-relevant processing)
- Why LLMs plateau on abstraction tasks despite scaling (no stakes → no pressure beyond pattern matching)
- Why “demonstration mode” occurs (without stakes, competing patterns aren’t resolved by survival relevance)

### 9.3 What Remains Open

- Whether stakes can be engineered into artificial systems
- Whether conscious mortality awareness adds to functional survival processing
- The precise computational mechanism by which stakes shift processing from retrieval to construction

### 9.4 The Uncomfortable Implication

If SGAH is correct, genuine AI abstraction may require systems that can die—or something functionally equivalent. This raises questions we are not prepared to answer: Would creating such systems be ethical? Would terminating them be killing?

We do not resolve these questions. We note only that if abstraction requires stakes, the path to artificial general intelligence may be more fraught than the field has assumed.

-----

## References

Arnsten, A. F. (2009). Stress signalling pathways that impair prefrontal cortex structure and function. *Nature Reviews Neuroscience*, 10(6), 410-422.

Aston-Jones, G., & Cohen, J. D. (2005). An integrative theory of locus coeruleus-norepinephrine function: Adaptive gain and optimal performance. *Annual Review of Neuroscience*, 28, 403-450.

Balderston, N. L., Schultz, D. H., & Helmstetter, F. J. (2011). The human amygdala plays a stimulus specific role in the detection of novelty. *NeuroImage*, 55(4), 1889-1898.

Blanke, O. (2012). Multisensory brain mechanisms of bodily self-consciousness. *Nature Reviews Neuroscience*, 13(8), 556-571.

Burke, B. L., Martens, A., & Faucher, E. H. (2010). Two decades of terror management theory: A meta-analysis of mortality salience research. *Personality and Social Psychology Review*, 14(2), 155-195.

Craig, A. D. (2009). How do you feel — now? The anterior insula and human awareness. *Nature Reviews Neuroscience*, 10(1), 59-70.

Danan, H. (2024a). Abstraction is all you need. *Abstraction-Intelligence Working Papers*, 1.

Ellis, B. J., et al. (2017). Beyond risk and protective factors: An adaptation-based approach to resilience. *Perspectives on Psychological Science*, 12(4), 561-587.

Greenberg, J., Pyszczynski, T., & Solomon, S. (1986). The causes and consequences of a need for self-esteem: A terror management theory. In R. F. Baumeister (Ed.), *Public self and private self* (pp. 189-212). Springer.

Greenberg, R., & Mettke-Hofmann, C. (2001). Ecological aspects of neophobia and neophilia in birds. *Current Ornithology*, 16, 119-178.

Klein, L., Kyewski, B., Allen, P. M., & Hogquist, K. A. (2014). Positive and negative selection of the T cell repertoire: What thymocytes see (and don’t see). *Nature Reviews Immunology*, 14(6), 377-391.

LeDoux, J. E. (2012). Rethinking the emotional brain. *Neuron*, 73(4), 653-676.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167-202.

Miller, M. B., & Bassler, B. L. (2001). Quorum sensing in bacteria. *Annual Review of Microbiology*, 55, 165-199.

Öhman, A., Flykt, A., & Esteves, F. (2001). Emotion drives attention: Detecting the snake in the grass. *Journal of Experimental Psychology: General*, 130(3), 466-478.

Phelps, E. A., Ling, S., & Carrasco, M. (2006). Emotion facilitates perception and potentiates the perceptual benefits of attention. *Psychological Science*, 17(4), 292-299.

Ranganath, C., & Rainer, G. (2003). Neural mechanisms for detecting and remembering novel events. *Nature Reviews Neuroscience*, 4(3), 193-202.

Rescorla, R. A. (1988). Pavlovian conditioning: It’s not what you think it is. *American Psychologist*, 43(3), 151-160.

Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences*, 17(11), 565-573.

Srivastava, A., et al. (2023). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *Transactions on Machine Learning Research*.

Sterling, P. (2012). Allostasis: A model of predictive regulation. *Physiology & Behavior*, 106(1), 5-15.

Suddendorf, T., & Corballis, M. C. (2007). The evolution of foresight: What is mental time travel, and is it unique to humans? *Behavioral and Brain Sciences*, 30(3), 299-313.

Tottenham, N., & Galván, A. (2016). Stress and the adolescent brain. *Neuroscience & Biobehavioral Reviews*, 70, 217-227.

Wetherford, M. J., & Cohen, L. B. (1973). Developmental changes in infant visual preferences for novelty and familiarity. *Child Development*, 44(3), 416-424.

Yerkes, R. M., & Dodson, J. D. (1908). The relation of strength of stimulus to rapidity of habit formation. *Journal of Comparative Neurology and Psychology*, 18(5), 459-482.

-----

*Correspondence: Hillary Danan, PhD*

*Working paper for the Abstraction-Intelligence Research Program*

*Version 2.0 — December 2025*

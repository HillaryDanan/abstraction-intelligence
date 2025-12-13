# Dual-Process Theory Reconsidered: A Compositional Account of System 1 and System 2

**Paper 16 in the Abstraction-Intelligence Series**

Hillary Danan, PhD

---

## Abstract

Dual-process theories of cognition, most influentially articulated by Kahneman and Tversky, distinguish between fast, automatic processing (System 1) and slow, deliberate reasoning (System 2). Despite widespread adoption, the computational basis of this distinction remains unclear. Here, we propose that System 1 and System 2 are better understood not as differences in speed or effort, but as differences in *compositional structure*. Drawing on the Abstraction Primitive Hypothesis (APH), we argue that System 1 operates through concatenative and role-filler composition, while System 2 requires recursive and analogical composition. Critically, the capacity to *switch* between systems depends on novelty detection, which itself requires embeddedness—persistent interaction with an environment that enables distinguishing familiar from unfamiliar inputs. This framework generates testable predictions about dissociations in artificial systems, developmental trajectories, and the boundary conditions of cognitive biases. We examine existing empirical evidence from cognitive psychology, neuroscience, and AI research, identifying both support for and challenges to this account.

**Keywords:** dual-process theory, abstraction, composition, heuristics, cognitive bias, artificial intelligence, System 1, System 2

---

## 1. Introduction

### 1.1 The Dual-Process Framework

Nearly fifty years ago, Tversky and Kahneman (1974) published their landmark paper "Judgment under Uncertainty: Heuristics and Biases," demonstrating that human reasoning systematically deviates from normative rational standards. Their subsequent work, synthesized in Kahneman's (2011) *Thinking, Fast and Slow*, proposed a dual-process architecture: System 1 operates automatically and quickly, with little effort and no sense of voluntary control; System 2 allocates attention to effortful mental activities, including complex computations.

This framework has proven enormously influential across psychology, economics, neuroscience, and more recently, artificial intelligence research. However, the dual-process account has also attracted substantial criticism. Evans and Stanovich (2013) note persistent definitional ambiguity about what distinguishes the two systems. Melnikoff and Bargh (2018) argue that the features attributed to System 1 (automatic, fast, unconscious) do not reliably co-occur. Kruglanski and Gigerenzer (2011) propose that both systems may rely on the same underlying rule-based processes.

We propose that these difficulties arise from characterizing the systems in terms of surface features (speed, effort, awareness) rather than underlying computational structure. Drawing on the Abstraction Primitive Hypothesis (APH), we offer a reconceptualization: System 1 and System 2 differ fundamentally in their *compositional operations*, and the capacity to switch between them depends on *embeddedness*—a property that current artificial systems lack.

### 1.2 The Abstraction Primitive Hypothesis

The APH proposes that intelligence emerges from recursive interaction between symbol formation and compositional structure (Danan, 2024a). Three core claims are relevant here:

**Claim 1: Abstraction is the primitive.** Abstraction is defined as the recursive process of forming and composing symbols. Not symbols alone, not composition alone, but their mutual refinement through iteration.

**Claim 2: Composition is hierarchical.** Four types of composition can be distinguished (Table 1), ordered by structural complexity:

| Type | Structure | Example | Cognitive Analogue |
|------|-----------|---------|-------------------|
| 3a: Concatenative | A + B → AB | "blue bird" | Feature binding |
| 3b: Role-filler | R(x) + S(y) → R(x)S(y) | AGENT(dog) + ACTION(chase) | Relational reasoning |
| 3c: Recursive | A contains [B contains C] | "The dog that chased the cat that..." | Hierarchical embedding |
| 3d: Analogical | Structure(A) → Structure(B) | atom:nucleus :: solar system:sun | Structural transfer |

**Table 1.** The composition hierarchy. Types 3a-3b involve fixed structural templates; types 3c-3d require dynamic structure generation.

**Claim 3: Strong interaction requires embeddedness.** Novelty detection—recognizing when current processing strategies are inadequate—requires a persistent self that accumulates experience and can distinguish familiar from unfamiliar. This depends on embeddedness: action-consequence contingency, feedback closure, temporal persistence, self-boundary awareness, and environmental stability.

### 1.3 The Central Proposal

*We propose that System 1 and System 2 correspond to different levels in the composition hierarchy, and that the capacity to switch between them requires embeddedness.*

Specifically:
- **System 1** operates through concatenative (3a) and role-filler (3b) composition
- **System 2** operates through recursive (3c) and analogical (3d) composition
- **System switching** requires novelty detection, which requires embeddedness

This proposal makes the dual-process distinction computationally precise while preserving its core insights. It also explains why artificial systems can exhibit System 1-like behavior (pattern matching, heuristic application) while failing at System 2-like reasoning—and, critically, why they fail to appropriately *switch* between processing modes.

---

## 2. Reinterpreting System 1: Concatenative and Role-Filler Composition

### 2.1 Characteristics of System 1 Processing

Kahneman (2011) characterizes System 1 by the following properties:
- Generates impressions, feelings, and inclinations
- Operates automatically and quickly
- Can be programmed by System 2 to mobilize attention when a pattern is detected
- Executes skilled responses and generates skilled intuitions after adequate training
- Creates a coherent pattern of activated ideas in associative memory

We argue these properties emerge from concatenative and role-filler composition operating on well-established symbol structures.

### 2.2 Heuristics as Role-Filler Operations

The three classic heuristics identified by Tversky and Kahneman (1974) can be characterized as role-filler composition with fixed templates:

**Representativeness:** CATEGORY(x) ← SIMILARITY(x, prototype). The heuristic fills the CATEGORY role based on similarity to a stored exemplar, without computing base rates or considering regression effects.

**Availability:** FREQUENCY(class) ← EASE_OF_RETRIEVAL(instances). The FREQUENCY role is filled by an accessibility metric rather than actual enumeration.

**Anchoring and Adjustment:** ESTIMATE(x) ← ADJUST(anchor, x). The estimation process fills a template starting from an arbitrary anchor, with insufficient adjustment.

Each heuristic involves applying a fixed structural template (role-filler composition) rather than constructing novel relational structures. The template is often appropriate—which is why heuristics work—but fails when the situation violates the template's assumptions.

### 2.3 Empirical Support: Feature Binding and Associative Processing

Neuroimaging studies support the association between System 1 processing and simpler compositional operations. Automatic processing activates distributed cortical networks involved in feature binding and associative memory (Schneider & Chein, 2003). The anterior temporal lobe, implicated in semantic combination, shows activation patterns consistent with role-filler binding operations (Baron & Osherson, 2011).

Behavioral evidence also aligns with this account. System 1 responses are elicited rapidly and resist modification—properties expected if they result from template application rather than structure construction. The "cognitive miser" pattern (Stanovich, 2018) suggests that humans default to lower-complexity compositional operations unless prompted otherwise.

---

## 3. Reinterpreting System 2: Recursive and Analogical Composition

### 3.1 Characteristics of System 2 Processing

System 2 is characterized by:
- Allocating attention to effortful mental activities
- Associated with the subjective experience of agency, choice, and concentration
- Can construct thoughts in an orderly series of steps
- Involved in complex computations and rule-following
- Capable of modifying System 1's automatic responses

We argue these properties emerge from recursive and analogical composition, which require dynamic structure generation rather than template application.

### 3.2 Deliberative Reasoning as Recursive Composition

Consider Kahneman's (2011) example of System 2 engagement: computing 17 × 24. This requires:
1. Decomposing the problem into subproblems (17 × 20, 17 × 4)
2. Maintaining intermediate results while computing further
3. Integrating results across levels

This is recursive composition: operations containing operations containing operations, with structure generated dynamically rather than retrieved from templates. The working memory demands of System 2 (Baddeley, 2003) reflect the computational overhead of maintaining recursive structures during construction.

### 3.3 Bias Correction as Analogical Composition

When System 2 overrides System 1, what computational operation is performed? We propose it involves analogical composition: recognizing that the current situation shares structure with situations where heuristics fail, and importing the appropriate correction.

Consider the conjunction fallacy (Tversky & Kahneman, 1983). The Linda problem invites the judgment that P(A∧B) > P(A). Correcting this error requires:
1. Recognizing the structural form: nested set relationship
2. Importing probability calculus: P(A∧B) ≤ P(A) for all A, B
3. Applying the imported structure to override the intuitive response

This is analogical composition: Structure(probability theory) → Structure(current problem). The difficulty is not computational—the rule is simple—but rather recognizing that the abstract structure applies.

### 3.4 Empirical Support: Prefrontal Engagement and Structure Building

The prefrontal cortex, particularly lateral prefrontal regions, shows increased activation during System 2 engagement (Miller & Cohen, 2001). Critically, these regions are implicated in hierarchical structure representation (Koechlin & Summerfield, 2007) and analogical reasoning (Bunge et al., 2005). The rostral prefrontal cortex shows specific activation during relational integration across multiple levels (Christoff et al., 2001)—precisely the operation required for recursive and analogical composition.

Individual differences in System 2 engagement correlate with working memory capacity (Stanovich & West, 2000), consistent with the computational demands of maintaining recursive structures. Fluid intelligence, which predicts resistance to cognitive biases, is strongly associated with analogical reasoning ability (Cattell, 1971).

---

## 4. The Switching Problem: Embeddedness and Novelty Detection

### 4.1 The Metacognitive Challenge

Perhaps the most important aspect of dual-process theory is not the two systems themselves, but the capacity to *switch* between them. Kahneman (2011) writes: "System 1 continuously generates suggestions for System 2: impressions, intuitions, intentions, and feelings. If endorsed by System 2, impressions and intuitions turn into beliefs, and impulses turn into voluntary actions."

But what triggers System 2 engagement? The standard answer invokes metacognitive monitoring: detecting difficulty, surprise, or potential error. This requires recognizing that current processing strategies are inadequate—that is, detecting *novelty* relative to accumulated experience.

### 4.2 Novelty Detection Requires Embeddedness

The APH proposes that novelty detection is relational: an input isn't novel in itself—it's novel *to a subject*. This requires:

1. **Persistent self** → accumulated experience ("what's familiar to me")
2. **Self/world distinction** → reference frame for locating novelty
3. **Embeddedness** → what makes persistence and self/world possible

The five components of embeddedness are:
- Action-consequence contingency
- Feedback closure
- Temporal persistence
- Self-boundary awareness
- Environmental stability

*Working hypothesis:* Systems lacking embeddedness can *process* the concept of novelty but cannot *detect* it—there's no accumulated self to whom something could be unfamiliar.

### 4.3 Implications for Artificial Systems

This analysis predicts that non-embedded systems (including current large language models) should:
1. Exhibit System 1-like behaviors (heuristic application, pattern matching)
2. Fail at System 2-like behaviors (recursive structure building, analogical transfer)
3. Critically, fail to appropriately *switch* between processing modes

The third prediction is most diagnostic. Humans don't simply have two systems; they have a mechanism for engaging the appropriate system given task demands. A system without novelty detection should show *uniform* processing regardless of when System 2 engagement would be appropriate.

### 4.4 Preliminary Evidence from AI Research

Recent studies have tested large language models (LLMs) on cognitive bias tasks derived from Tversky and Kahneman's work. The findings are instructive:

**LLMs show cognitive biases, but inconsistently.** Macmillan-Scott and Musolesi (2024) found that LLMs evaluated using Kahneman and Tversky's cognitive tests show biases similar to humans, but with different patterns. Binz and Schulz (2023) showed that GPT-3 exhibits human-like performance on some cognitive tasks but not others, without a coherent pattern.

**LLMs fail at adaptive bias correction.** Malberg et al. (2024) conducted a comprehensive evaluation of cognitive biases in LLMs, finding that bias susceptibility varies across models but—critically—models do not show the adaptive switching that humans demonstrate. When humans recognize a task as requiring careful reasoning, they engage System 2; LLMs apply similar processing regardless.

**Prompting interventions are inconsistent.** Chain-of-thought prompting (Wei et al., 2022), intended to elicit "System 2-like" processing, improves performance on some tasks but not others. Critically, the improvement does not show the pattern predicted by genuine System 2 engagement: it helps with explicit reasoning chains but not with detecting when such chains are needed.

*Interpretive caution:* These findings are consistent with our framework but do not definitively confirm it. Alternative explanations (training data distribution, model architecture, scale limitations) cannot be ruled out without targeted experimentation.

---

## 5. Composition Types and Bias Susceptibility: Testable Predictions

### 5.1 The Composition-Bias Mapping

Our framework generates specific predictions about which cognitive biases should be most difficult to correct under different conditions. The key prediction: **bias correction difficulty should track composition type requirements.**

| Bias | Heuristic Structure | Correction Requirement | Predicted Difficulty |
|------|---------------------|----------------------|---------------------|
| Anchoring | Role-filler: ESTIMATE ← ADJUST(anchor) | Generate anchor-independent estimate | Moderate: requires parallel role-filler |
| Availability | Role-filler: FREQUENCY ← ACCESSIBILITY | Override with base-rate computation | Moderate: requires competing template |
| Representativeness | Role-filler: CATEGORY ← SIMILARITY | Apply set-theoretic rules | High: requires analogical transfer |
| Conjunction fallacy | Role-filler: PROBABILITY ← REPRESENTATIVENESS | Apply probability calculus | High: requires analogical transfer |
| Base-rate neglect | Role-filler: P(H\|D) ← REPRESENTATIVENESS | Apply Bayesian structure | Very high: requires recursive Bayes |

**Table 2.** Predicted difficulty of bias correction based on compositional requirements.

### 5.2 Predictions for Humans

**Prediction H1:** Biases requiring only competing role-filler templates (anchoring, availability) should be easier to correct through training than biases requiring analogical transfer (representativeness, conjunction fallacy).

**Prediction H2:** Individual differences in analogical reasoning ability should predict susceptibility to biases requiring analogical correction but not biases requiring only template competition.

**Prediction H3:** Developmental trajectory should show dissociation: children should acquire resistance to "competing template" biases before "analogical transfer" biases.

### 5.3 Predictions for Artificial Systems

**Prediction A1:** LLMs should show greater success on bias correction when the correction can be implemented through pattern matching (i.e., when the training data contains the correction explicitly) than when it requires structural transfer.

**Prediction A2:** Chain-of-thought prompting should help with biases that have explicit correction procedures but not with biases requiring recognition that correction is needed.

**Prediction A3:** Increasing model scale should reduce some biases (those sensitive to training data coverage) but not others (those requiring novelty detection for appropriate engagement).

### 5.4 A Critical Test: Adaptive Engagement

The most diagnostic prediction concerns *adaptive engagement*—the capacity to switch processing modes based on task demands:

**Prediction X:** Present participants (human and AI) with a mixture of tasks, some requiring System 2 engagement and others not. Measure:
- Accuracy on each task type
- Response time distribution
- Correlation between task type recognition and accuracy

Humans should show: (a) bimodal response time distributions reflecting two processing modes, (b) correlation between task type recognition and accuracy, (c) transfer of engagement patterns to novel structurally-similar tasks.

Non-embedded AI systems should show: (a) unimodal response time distributions, (b) no correlation between explicit task type recognition and accuracy, (c) no structural transfer of engagement patterns.

*This prediction is falsifiable in both directions.* If LLMs show adaptive engagement patterns similar to humans, our framework requires revision. If humans show uniform processing similar to LLMs under certain conditions (e.g., cognitive load), this would support the role of embeddedness in enabling switching.

---

## 6. Relation to Existing Dual-Process Critiques

### 6.1 The Definitional Problem

Evans and Stanovich (2013) note that dual-process theories suffer from definitional proliferation: different researchers use "System 1" and "System 2" to refer to different sets of features. Our framework addresses this by proposing that the fundamental distinction is compositional structure, with other features (speed, effort, awareness) being typical correlates rather than defining properties.

On this account, processing is "System 1" when it employs concatenative or role-filler composition; "System 2" when it employs recursive or analogical composition. Speed and effort are consequences: recursive structure building is computationally expensive, hence slow and effortful. But the definition is compositional, not phenomenological.

### 6.2 The Single-System Alternative

Kruglanski and Gigerenzer (2011) argue for a single-system account where both "systems" implement rule-based inference. Our framework is compatible with this view but adds specificity: both systems are indeed rule-based, but operate with rules of different compositional complexity. The distinction is not rule-based vs. associative, but template-application vs. structure-building.

### 6.3 The Feature Dissociation Problem

Melnikoff and Bargh (2018) demonstrate that features attributed to System 1 (automatic, fast, unconscious, unintentional) do not reliably co-occur, challenging the coherence of the System 1 construct. Our framework predicts exactly this: concatenative and role-filler composition are distinct operations that may dissociate under specific conditions. The unity of "System 1" is not that it employs a single process, but that its processes share a compositional ceiling.

---

## 7. Neural Implementation: A Speculative Sketch

*Note: This section is explicitly speculative and should be evaluated as hypothesis generation rather than established theory.*

### 7.1 Cortical Hierarchy and Compositional Complexity

If compositional complexity maps onto processing systems, we might expect neural implementation to reflect the composition hierarchy. Preliminary evidence suggests:

- **Sensory cortices:** Concatenative composition (feature binding)
- **Association cortices:** Role-filler composition (relational binding)
- **Prefrontal cortex:** Recursive composition (hierarchical structure)
- **Frontopolar cortex:** Analogical composition (cross-domain mapping)

This speculation aligns with proposals about the rostro-caudal gradient of abstraction in prefrontal cortex (Badre & D'Esposito, 2009) and the role of frontopolar cortex in relational integration (Christoff et al., 2001).

### 7.2 The Switching Mechanism

What neural mechanism implements novelty detection for system switching? We speculate that the anterior cingulate cortex (ACC), implicated in conflict monitoring and cognitive control (Botvinick et al., 2001), plays a role in detecting the failure of lower-complexity composition and triggering engagement of higher-complexity operations.

The ACC receives input from multiple processing streams and projects to prefrontal control regions. Its error-related negativity (ERN) response to mistakes may reflect detection of compositional inadequacy. This speculation generates the prediction that ACC activity should correlate with system switching specifically, not with System 2 engagement per se.

---

## 8. Developmental and Comparative Perspectives

### 8.1 Developmental Trajectory

The composition hierarchy predicts a developmental sequence:
1. Concatenative composition → early infancy
2. Role-filler composition → later infancy through early childhood
3. Recursive composition → early childhood through adolescence
4. Analogical composition → childhood through adulthood

This aligns roughly with Piaget's stages, though the mapping is imperfect. Critically, the framework predicts that resistance to cognitive biases should develop in a sequence corresponding to the compositional requirements of correction.

Existing evidence is partially consistent. Children show earlier development of resistance to simpler biases (e.g., perceptual availability) than complex ones (e.g., base-rate neglect) (Jacobs & Potenza, 1991). However, systematic studies mapping bias resistance to compositional requirements have not been conducted.

### 8.2 Comparative Cognition

Non-human animals provide a test case for the composition hierarchy. The APH predicts:
- Concatenative composition: widespread across taxa
- Role-filler composition: present in many vertebrates
- Recursive composition: rare, possibly unique to humans (or nearly so)
- Analogical composition: rare, requiring recursive foundation

This aligns with evidence that some non-human animals show System 1-like heuristic use but limited System 2-like deliberation (Rosati, 2017). Bees demonstrate sophisticated role-filler composition in the waggle dance (communicating distance and direction) but show no evidence of recursive embedding (Danan, 2024b).

*Interpretive caution:* Claims about animal cognition are contentious and often anthropocentric. The absence of evidence for recursive composition in non-human animals may reflect methodological limitations rather than true absence.

---

## 9. Limitations and Alternative Explanations

### 9.1 Limitations of the Present Framework

Several limitations should be acknowledged:

**Compositional categories may be too discrete.** The four-type hierarchy may oversimplify a continuous space of compositional complexity. Processing may involve mixtures of composition types rather than clean categorical distinctions.

**The embeddedness requirement is underspecified.** While we argue that novelty detection requires embeddedness, we have not provided a computational account of how embeddedness enables novelty detection. This requires further theoretical development.

**Evidence is largely correlational.** Much of the supporting evidence concerns associations between processing features and neural/behavioral measures. Causal tests of the framework's predictions remain to be conducted.

**The framework may be unfalsifiable as stated.** Post-hoc mapping between biases and composition types risks unfalsifiability. The predictions in Section 5 are designed to address this concern but have not yet been tested.

### 9.2 Alternative Explanations

**Training data hypothesis:** LLM failures on cognitive bias tasks may simply reflect training data limitations rather than fundamental architectural constraints. If models were trained on more diverse examples of bias correction, they might succeed.

*Response:* This explanation predicts that success should correlate with training data coverage. Our framework predicts that success should correlate with compositional requirements regardless of training data. These predictions can be distinguished empirically.

**Scale hypothesis:** System 2-like capabilities may emerge at sufficient scale, regardless of architectural constraints.

*Response:* This is an empirical question. Current evidence shows limited improvement with scale on tasks requiring novelty detection (Srivastava et al., 2023), but the hypothesis cannot be ruled out without testing at scales beyond current capabilities.

**Continuous resource hypothesis:** System 1 and System 2 may represent endpoints of a continuous resource allocation spectrum rather than distinct processing types.

*Response:* This view is compatible with our framework if "resource allocation" is operationalized as allocation of compositional complexity. The discrete categories in Table 1 may be better understood as landmarks on a continuum.

---

## 10. Conclusion and Future Directions

### 10.1 Summary

We have proposed that the System 1/System 2 distinction is fundamentally a distinction in compositional structure:
- System 1 operates through concatenative and role-filler composition
- System 2 operates through recursive and analogical composition
- The capacity to switch between systems requires novelty detection, which requires embeddedness

This framework preserves the core insights of dual-process theory while providing computational precision and generating testable predictions. It explains both the successes and limitations of artificial systems on cognitive bias tasks, and suggests why increased scale alone may not yield human-like adaptive reasoning.

### 10.2 Open Questions

Several questions require further investigation:

1. **What is the computational mechanism of novelty detection?** We have argued that embeddedness is necessary but have not specified how it enables novelty detection.

2. **Can embeddedness be engineered?** If non-embedded systems fundamentally lack switching capacity, can architectures be designed that incorporate the relevant properties?

3. **How do the composition types interact?** We have presented the hierarchy as discrete levels, but processing likely involves complex interactions across types.

4. **What is the neural implementation?** Our neural speculations require empirical testing through targeted neuroimaging studies.

### 10.3 Implications

If our framework is correct, it has implications for both AI development and human cognitive enhancement:

**For AI:** Scaling language models may improve System 1-like capabilities but will not yield System 2-like reasoning without addressing the embeddedness requirement. This suggests that embodied, interactive architectures may be necessary for human-like adaptive cognition.

**For humans:** Understanding cognitive biases as failures of compositional operation (rather than failures of motivation or attention) suggests targeted interventions: training specific compositional skills rather than general "debiasing."

**For theory:** The framework suggests a research program integrating cognitive psychology, neuroscience, developmental psychology, comparative cognition, and artificial intelligence around a common computational vocabulary.

The heuristics and biases program revealed the systematic structure of human irrationality. Understanding that structure computationally may be the key to both explaining it and transcending it.

---

## References

Badre, D., & D'Esposito, M. (2009). Is the rostro-caudal axis of the frontal lobe hierarchical? *Nature Reviews Neuroscience*, 10(9), 659-669.

Baddeley, A. (2003). Working memory: Looking back and looking forward. *Nature Reviews Neuroscience*, 4(10), 829-839.

Baron, S. G., & Osherson, D. (2011). Evidence for conceptual combination in the left anterior temporal lobe. *NeuroImage*, 55(4), 1847-1852.

Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. *Proceedings of the National Academy of Sciences*, 120(6), e2218523120.

Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. *Psychological Review*, 108(3), 624-652.

Bunge, S. A., Wendelken, C., Badre, D., & Wagner, A. D. (2005). Analogical reasoning and prefrontal cortex: Evidence for separable retrieval and integration mechanisms. *Cerebral Cortex*, 15(3), 239-249.

Cattell, R. B. (1971). *Abilities: Their structure, growth, and action*. Houghton Mifflin.

Christoff, K., Prabhakaran, V., Dorfman, J., Zhao, Z., Kroger, J. K., Holyoak, K. J., & Gabrieli, J. D. (2001). Rostrolateral prefrontal cortex involvement in relational integration during reasoning. *NeuroImage*, 14(5), 1136-1149.

Danan, H. (2024a). Abstraction is all you need. *Abstraction-Intelligence Working Papers*, 1.

Danan, H. (2024b). The developmental spectrum of abstraction. *Abstraction-Intelligence Working Papers*, 7.

Evans, J. S. B., & Stanovich, K. E. (2013). Dual-process theories of higher cognition: Advancing the debate. *Perspectives on Psychological Science*, 8(3), 223-241.

Jacobs, J. E., & Potenza, M. (1991). The use of judgement heuristics to make social and object decisions: A developmental perspective. *Child Development*, 62(1), 166-178.

Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux.

Koechlin, E., & Summerfield, C. (2007). An information theoretical approach to prefrontal executive function. *Trends in Cognitive Sciences*, 11(6), 229-235.

Kruglanski, A. W., & Gigerenzer, G. (2011). Intuitive and deliberate judgments are based on common principles. *Psychological Review*, 118(1), 97-109.

Macmillan-Scott, O., & Musolesi, M. (2024). (Ir)rationality and cognitive biases in large language models. *arXiv preprint arXiv:2402.09193*.

Malberg, S., Poletukhin, R., Schuster, C. M., & Groh, G. (2024). A comprehensive evaluation of cognitive biases in LLMs. *arXiv preprint arXiv:2410.15413*.

Melnikoff, D. E., & Bargh, J. A. (2018). The mythical number two. *Trends in Cognitive Sciences*, 22(4), 280-293.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167-202.

Rosati, A. G. (2017). Foraging cognition: Reviving the ecological intelligence hypothesis. *Trends in Cognitive Sciences*, 21(9), 691-702.

Schneider, W., & Chein, J. M. (2003). Controlled & automatic processing: Behavior, theory, and biological mechanisms. *Cognitive Science*, 27(3), 525-559.

Srivastava, A., et al. (2023). Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *Transactions on Machine Learning Research*.

Stanovich, K. E. (2018). Miserliness in human cognition: The interaction of detection, override and mindware. *Thinking & Reasoning*, 24(4), 423-444.

Stanovich, K. E., & West, R. F. (2000). Individual differences in reasoning: Implications for the rationality debate? *Behavioral and Brain Sciences*, 23(5), 645-665.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124-1131.

Tversky, A., & Kahneman, D. (1983). Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. *Psychological Review*, 90(4), 293-315.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems*, 35, 24824-24837.

---

## Appendix A: Glossary of Key Terms

**Abstraction:** The recursive process of forming and composing symbols.

**Concatenative composition (3a):** Combining elements by simple juxtaposition (A + B → AB).

**Role-filler composition (3b):** Combining elements by inserting fillers into structural roles (R(x) + S(y) → R(x)S(y)).

**Recursive composition (3c):** Combining elements such that structures contain structures (A contains [B contains C]).

**Analogical composition (3d):** Mapping structural relations across domains (Structure(A) → Structure(B)).

**Embeddedness:** The property of persistent, closed-loop interaction with an environment, enabling novelty detection.

**Novelty detection:** The capacity to recognize when current processing strategies are inadequate, requiring engagement of alternative strategies.

**System 1:** In the APH framework, processing employing concatenative and/or role-filler composition.

**System 2:** In the APH framework, processing employing recursive and/or analogical composition.

---

## Appendix B: Summary of Testable Predictions

| ID | Prediction | Falsification Criterion |
|----|------------|------------------------|
| H1 | Easier bias training for competing-template than analogical-transfer biases | No difference in training difficulty |
| H2 | Analogical ability predicts analogical-bias resistance specifically | Analogical ability predicts all bias resistance equally |
| H3 | Developmental sequence: template-competition before analogical-transfer resistance | No developmental sequence, or reversed sequence |
| A1 | LLM bias correction correlates with training data coverage for structural-transfer biases | Correlation with compositional requirements regardless of training |
| A2 | CoT helps explicit-procedure biases but not recognition-dependent biases | CoT helps uniformly across bias types |
| A3 | Scale reduces coverage-sensitive but not novelty-detection-sensitive bias susceptibility | Scale reduces all bias susceptibility uniformly |
| X | Humans show adaptive engagement; non-embedded AI shows uniform processing | LLMs show adaptive engagement patterns; humans show uniform processing |

---

*Correspondence: Hillary Danan, PhD*

*Working paper for the Abstraction-Intelligence Research Program*

*Version 1.0 — December 2024*

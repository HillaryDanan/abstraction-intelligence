# The Computational Structure of Abstraction

## Defining the Operation That Distinguishes Intelligence from Reactivity

-----

**Abstract**

What precisely is abstraction? Despite its centrality to theories of intelligence, the term remains underspecified—sometimes conflated with compression, categorization, or attention itself. This paper offers a precise operational definition: abstraction is the transformation of attended information into stabilized, discrete, bound representations that exhibit role-filler independence. We identify four component operations—stabilization, discretization, binding, and structural decoupling—and argue that their conjunction constitutes the minimal sufficient machinery for compositional thought. We distinguish abstraction sharply from attention (which selects but does not transform) and from compression (which reduces but does not compose). This definition generates falsifiable predictions about dissociations between attentional and abstractive deficits, developmental sequences, and architectural requirements for compositional generalization in artificial systems. We review evidence from cognitive neuroscience, developmental psychology, and machine learning, noting where empirical support is strong and where the framework remains hypothetical.

-----

## 1. Introduction

The capacity to form and manipulate abstract representations is widely regarded as central to intelligence (Halford et al., 1998; Penn et al., 2008; Gentner, 1983). Yet the term “abstraction” is used inconsistently across literatures—sometimes denoting categorization, sometimes compression, sometimes the formation of concepts, sometimes analogical mapping. This ambiguity impedes both theoretical progress and empirical testing.

We propose a precise definition: **abstraction is the operation that transforms attended sensory information into compositionally manipulable symbols**. This definition distinguishes abstraction from the input processes that feed it (perception, attention) and from the downstream operations that consume its products (memory storage, reasoning, decision-making).

The central claim is not that abstraction is important—this is uncontroversial—but that abstraction is a *specific computational operation* with identifiable component processes, neural substrates, and architectural requirements. A system that performs attention without abstraction reacts; a system that performs abstraction reasons.

### 1.1 Scope and Claims

This paper advances both established findings and theoretical proposals. We distinguish these carefully:

**Established (empirical support from multiple independent studies):**

- Attention and categorization are dissociable processes (Posner & Petersen, 1990; Warrington & Shallice, 1984)
- Prefrontal cortex encodes abstract rules and categories (Freedman et al., 2001; Wallis et al., 2001)
- Working memory maintains information beyond stimulus offset (Baddeley, 2003)
- Feature binding requires attentional resources (Treisman, 1998)
- Compositional generalization in neural networks depends on architectural structure (Lake & Baroni, 2018)

**Proposed (theoretical framework requiring further testing):**

- The four-component definition of abstraction (stabilization, discretization, binding, structural decoupling)
- The claim that these four components are jointly necessary and sufficient
- The claim that attention is necessary but not sufficient for abstraction
- Specific predictions about dissociation patterns

-----

## 2. Defining Abstraction: Four Component Operations

We propose that abstraction consists of four component operations, each necessary and jointly sufficient for the formation of compositionally manipulable representations.

### 2.1 Stabilization

**Definition:** The maintenance of a representation beyond the duration of the eliciting stimulus.

A purely reactive system responds to stimuli as they occur. Abstraction requires that selected information be held in a format accessible for subsequent processing. This is not mere persistence (which describes any physical trace) but *functional availability*—the representation remains poised to influence ongoing computation.

**Empirical grounding:** Working memory research demonstrates that humans maintain approximately four discrete items in an active state (Cowan, 2001), and that this maintenance depends on sustained neural activity in prefrontal and parietal cortices (Curtis & D’Esposito, 2003). Delay-period activity in prefrontal neurons maintains category and rule information across temporal gaps (Freedman et al., 2001; Wallis et al., 2001).

**Relation to attention:** Attention selects information for processing; stabilization retains selected information for continued processing. Selection without stabilization yields reflexive response. The distinction is supported by dissociations: patients with intact attentional orienting can show impaired maintenance (Malhotra et al., 2005), and maintenance can occur for attended and unattended items (Soto et al., 2008).

### 2.2 Discretization

**Definition:** The transformation of continuous sensory input into representations with determinate identity conditions—units that are either present or absent, this symbol or that symbol.

Sensory input is continuous and high-dimensional. Abstraction requires carving this continuum into discrete units that can be counted, compared, and combined. This is the transition from analog to symbolic.

**Empirical grounding:** Categorical perception demonstrates that continuous physical variation is perceived as discrete categories (Harnad, 1987). Neurophysiological studies show that prefrontal neurons encode discrete category membership rather than continuous stimulus features (Freedman et al., 2001; Roy et al., 2010). The “number sense” literature demonstrates that even approximate numerical representations are encoded as discrete magnitudes with characteristic noise properties (Nieder & Dehaene, 2009).

**Theoretical status:** The claim that discretization is specifically a component of abstraction (rather than perception) is partially supported. Categorical perception occurs early in processing, suggesting some discretization is perceptual. However, the flexible formation of *novel* categories, and the assignment of arbitrary stimuli to abstract roles, appears to require prefrontal involvement (Freedman & Assad, 2006). We propose that perceptual categorization and abstractive discretization are distinct processes that may produce similar outputs—a hypothesis requiring further testing.

### 2.3 Binding

**Definition:** The integration of separately processed features into unified representations.

A red square and a blue circle present four features (red, blue, square, circle). Abstraction requires binding red-with-square and blue-with-circle, such that the features cohere as units rather than floating free.

**Empirical grounding:** The binding problem is well-established (Treisman, 1996). Feature Integration Theory demonstrates that accurate binding requires focused attention (Treisman & Gelade, 1980). Illusory conjunctions (mis-bindings of features) occur under attentional load (Treisman & Schmidt, 1982). Neural synchrony has been proposed as a binding mechanism (Singer & Gray, 1995; Engel et al., 2001), though the evidence remains contested (Shadlen & Movshon, 1999).

**Relation to attention:** Binding is attention-dependent: features are bound when attention is directed to their shared location or object. However, binding is not attention itself—attention can be directed without binding (to a single feature), and binding produces a structured representation that outlasts the attentional episode. The product of binding is a candidate for stabilization; the binding operation itself requires attentional resources.

### 2.4 Structural Decoupling (Role-Filler Independence)

**Definition:** The separation of structural roles from their fillers, enabling the same symbol to occupy different structural positions and different symbols to occupy the same structural position.

This is the most distinctively symbolic component. In the proposition “the cat chased the dog,” the role AGENT is filled by CAT and the role PATIENT by DOG. Structural decoupling is the capacity to distinguish these roles such that “the dog chased the cat” is a different proposition with the same constituents. Without this separation, representations are bound to specific configurations and cannot be systematically recombined.

**Empirical grounding:** Fodor and Pylyshyn (1988) argued that systematicity—the capacity to understand novel combinations of familiar elements—requires compositional structure with role-filler separation. Marcus (2001) demonstrated that neural networks without explicit variable binding fail systematic generalization tasks. Recent work shows that transformers exhibit some compositional generalization but fail systematically on tasks requiring role-filler independence (Lake & Baroni, 2018; Kim & Linzen, 2020).

**Theoretical status:** The claim that structural decoupling is a distinct component of abstraction (rather than an emergent property of the other three) is theoretical. Some accounts treat compositionality as arising from binding alone (Smolensky, 1990). We propose that structural decoupling is a fourth operation because binding can produce holistic representations that do not decompose—a bound representation of “red square” does not automatically yield separate “red” and “square” tokens that can recombine with other shapes and colors. This remains a hypothesis requiring empirical adjudication.

-----

## 3. Abstraction Is Not Attention

The distinction between attention and abstraction is the crux of the present framework. We argue that attention is necessary for abstraction but does not constitute it.

### 3.1 Attention Selects; Abstraction Transforms

Attention is a selective process that modulates the gain of neural responses to favored stimuli (Desimone & Duncan, 1995; Reynolds & Chelazzi, 2004). Attended stimuli are processed more thoroughly, but this processing can terminate in immediate response without forming a durable, compositional representation.

Consider a reflex arc: a stimulus elicits a response. The stimulus is in some sense “attended”—it is the input that controls behavior. But no symbol is formed. The response is coupled to the stimulus without intermediary representation.

Abstraction interposes a new kind of entity between stimulus and response: a symbol that is (a) stabilized beyond the stimulus, (b) discretized from continuous input, (c) bound into a coherent unit, and (d) structurally decoupled such that it can combine with other symbols.

### 3.2 Evidence for Dissociation

If attention and abstraction are distinct processes, they should dissociate under appropriate conditions.

**Attentional deficits with intact abstraction:** Patients with hemispatial neglect show profound deficits in attending to contralesional space but can form abstract concepts and reason about them (Driver & Mattingley, 1998). The deficit is in selection, not symbol formation.

**Abstractive deficits with intact attention:** Category-specific semantic deficits show the reverse pattern: patients can attend to and perceive stimuli normally but cannot access or form categorical representations (Warrington & Shallice, 1984; Caramazza & Shelton, 1998). Frontal lobe lesions impair abstract rule use while sparing basic attentional orienting (Stuss & Knight, 2002).

**Developmental dissociation:** Infants show sophisticated attentional orienting from birth (Johnson, 1990) but abstract reasoning develops over years (Halford et al., 1998). If attention were sufficient for abstraction, the developmental sequence would be unexplained.

**Architectural dissociation in artificial systems:** Neural networks can implement attention mechanisms (Bahdanau et al., 2015; Vaswani et al., 2017) without achieving compositional generalization (Lake & Baroni, 2018). Attention improves performance but does not guarantee systematicity.

### 3.3 The Transition Point

We propose that the transition from attention to abstraction is a qualitative shift, not a quantitative intensification. More attention does not yield abstraction; abstraction requires additional computational operations.

This proposal is consistent with but not proven by available evidence. Alternative accounts might hold that abstraction emerges from sufficiently sustained or distributed attention. The question is empirical: do systems exist that show maximal attentional engagement without abstractive products? We suggest that simple organisms and basic artificial neural networks provide existence proofs, but this remains to be demonstrated rigorously with appropriate controls.

-----

## 4. Abstraction Is Not Compression

Compression reduces information by exploiting statistical regularities. Abstraction might appear similar—both produce more compact representations than raw input. However, we argue these are distinct operations with different computational products.

### 4.1 Compression Reduces; Abstraction Composes

The output of compression is a code that reconstructs the input with minimal loss given resource constraints. The code is evaluated by reconstruction fidelity relative to encoding cost (Shannon, 1948). Nothing in this framework requires that compressed representations combine productively.

Abstraction produces symbols that compose. “Red” and “square” combine to yield “red square”; “red square” and “left of” combine to yield representational structures that support novel inferences. The generative capacity of abstraction exceeds its input.

**Formal distinction:** Compression is measured by description length relative to reconstruction accuracy. Compositionality is measured by generalization to novel combinations. These metrics can dissociate: a system may achieve excellent compression without compositional generalization, or exhibit compositional structure without minimal encoding (Higgins et al., 2017; Montero et al., 2021).

### 4.2 Empirical Evidence for Dissociation

Deep autoencoders can achieve excellent compression (low reconstruction error) while learning representations that do not support compositional generalization (Locatello et al., 2019). Conversely, compositional representations may be less efficient for reconstruction of specific training inputs but generalize better to novel combinations (Lake & Baroni, 2018).

Disentangled representation learning attempts to produce representations that are both compressed and compositional, but achieving this combination requires specific inductive biases—it does not emerge automatically from compression objectives (Higgins et al., 2017; Locatello et al., 2019).

**Hypothesis:** Compression yields abstraction only when additional architectural constraints enforce compositional structure. This hypothesis is supported by recent results showing that compositional generalization requires both factorized encoding and compositional output structure (see companion paper “Abstraction Beyond Compression”).

-----

## 5. Neural Substrates of Abstraction

If abstraction is a specific computational operation, it should have identifiable neural substrates distinct from those supporting attention and perception.

### 5.1 Prefrontal Cortex and Abstract Representation

Prefrontal cortex (PFC) is consistently implicated in abstract representation:

**Category encoding:** Neurons in PFC encode learned categories independently of specific visual features (Freedman et al., 2001; Freedman & Assad, 2006). This encoding is more abstract than sensory cortex representations, which remain feature-bound.

**Rule encoding:** PFC neurons encode abstract rules (e.g., “match” vs. “non-match”) that apply across stimulus dimensions (Wallis et al., 2001; Bunge et al., 2003).

**Relational encoding:** PFC represents relations between stimuli (greater than, same as) rather than stimulus features per se (Christoff et al., 2001).

**Structural decoupling:** PFC activity distinguishes role from filler—the same region encodes “agent” across different agents (Frankland & Greene, 2020).

### 5.2 Interaction Between PFC and Posterior Cortices

Abstraction likely emerges from interaction between frontal and posterior regions:

**Top-down modulation:** PFC provides top-down signals that bias processing in sensory cortices toward task-relevant features (Miller & Cohen, 2001). This could implement discretization by imposing categorical boundaries on continuous representations.

**Working memory:** The stabilization component requires sustained activity, which involves PFC-parietal networks (Curtis & D’Esposito, 2003).

**Binding:** Temporal synchronization between regions has been proposed to implement binding, with PFC potentially coordinating synchronization across posterior areas (Engel et al., 2001).

### 5.3 Developmental and Evolutionary Considerations

PFC is phylogenetically recent and shows prolonged developmental trajectory (Diamond, 2002). This is consistent with abstraction being a derived capacity that builds on but exceeds basic attentional mechanisms.

However, abstraction may not be strictly localized to PFC. Hippocampus is implicated in relational binding (Eichenbaum, 2000), and posterior cortices may support some categorical structure (Tanaka, 1996). The proposal is not that PFC alone implements abstraction, but that the abstractive operations require PFC involvement as a necessary component.

-----

## 6. Abstraction in Artificial Systems

The proposed definition of abstraction generates predictions for artificial intelligence architectures.

### 6.1 Current Large Language Models

Large language models (LLMs) implement attention mechanisms and achieve impressive compression of training data. Under the present framework, we can ask: do they abstract?

**Evidence for partial abstraction:** LLMs show some compositional generalization, analogical reasoning, and novel conceptual combination (Webb et al., 2023). This suggests at least partial instantiation of abstractive operations.

**Evidence for limitations:** LLMs fail systematically on tasks requiring strict compositional generalization, particularly with novel role-filler combinations (Lake & Baroni, 2018; Kim & Linzen, 2020). Performance degrades with relational complexity in ways that suggest limits on structural decoupling (Dziri et al., 2023).

**Interpretation:** LLMs may implement stabilization (representations persist across tokens), discretization (tokens are discrete units), and some binding (attention aggregates information). Structural decoupling may be partially implemented but not fully achieved, resulting in context-dependent “soft” compositionality rather than strict systematicity.

**Theoretical status:** This interpretation is speculative. LLMs are complex systems, and attributing specific computational operations requires careful analysis. The present framework suggests specific empirical tests—e.g., whether LLM failures cluster around structural decoupling tasks rather than other abstractive components.

### 6.2 Architectural Requirements

**Hypothesis:** Architectures that explicitly implement all four abstractive operations should outperform standard architectures on compositional generalization tasks.

This generates predictions:

- **Factorized representations:** Architectures with explicit factorization (e.g., slot-based attention, disentangled VAEs) should show improved discretization and structural decoupling (Locatello et al., 2020; Goyal et al., 2021).
- **Compositional output structure:** Generalization requires not just factorized encoding but compositional decoding (see companion paper “Abstraction Beyond Compression”).
- **Working memory modules:** Explicit maintenance mechanisms should improve stabilization-dependent tasks (Graves et al., 2014).
- **Role-filler separation:** Architectures with explicit variable binding should show improved systematicity (Webb et al., 2020).

-----

## 7. Falsifiable Predictions

The present framework generates predictions that can be tested and potentially falsified.

### 7.1 Dissociation Predictions

**Prediction 1:** Abstractive deficits should be dissociable from attentional deficits. Specifically:

- Patients with severe attentional deficits (e.g., hemispatial neglect) should show preserved abstraction for attended stimuli.
- Patients with category-specific deficits should show preserved attention to the deficient category.

**Prediction 2:** The four components of abstraction should be separable. We predict the possibility (not necessity) of:

- Stabilization deficits with preserved binding (information not maintained but correctly integrated when present)
- Binding deficits with preserved discretization (features processed categorically but mis-bound)
- Structural decoupling deficits with preserved binding (bound representations formed but not combinable)

### 7.2 Developmental Predictions

**Prediction 3:** Abstractive operations should develop sequentially. Proposed order (speculative):

1. Binding (emerges early, attention-dependent)
1. Stabilization (develops with working memory, early childhood)
1. Discretization (develops with categorization, early childhood)
1. Structural decoupling (develops with relational reasoning, middle childhood)

This ordering is consistent with developmental data (Halford et al., 1998; Diamond, 2002) but requires systematic testing across all four components.

### 7.3 Architectural Predictions

**Prediction 4:** Artificial systems should show component-specific failures.

- Autoregressive models without explicit memory should show stabilization limitations.
- Systems without attention mechanisms should show binding failures.
- Systems without factorized representations should show structural decoupling limitations.

**Prediction 5:** Architectures implementing all four components should outperform standard architectures on compositional generalization benchmarks (SCAN, COGS, etc.), even at equivalent parameter count.

-----

## 8. Limitations and Open Questions

### 8.1 Is Four Components the Right Number?

The four-component decomposition may be too coarse (missing subcomponents) or too fine (combining operations that are better described as one). Alternative decompositions are possible:

- **Lumping:** Binding and structural decoupling might both be aspects of a single “compositional structure” operation.
- **Splitting:** Stabilization might decompose into maintenance (holding active) and consolidation (forming durable traces).

The present decomposition is proposed as a working hypothesis. Empirical dissociations will determine the appropriate grain of analysis.

### 8.2 Is Abstraction Substrate-Independent?

We have described abstraction in computational terms without specifying physical implementation. This implies substrate independence—any system implementing these operations would abstract, regardless of whether it is biological, silicon-based, or otherwise constituted.

This is a strong claim. It may be that biological implementation provides capacities (e.g., analog computation, neurochemical modulation) that our computational description fails to capture. We note this as an open question, not a claim we can currently adjudicate.

### 8.3 What About Non-Symbolic Abstraction?

Some cognitive scientists argue for “graded” or “sub-symbolic” abstraction—representations that show abstraction-like properties without discrete symbols (Smolensky, 1988; Rogers & McClelland, 2004). Our four-component analysis may be biased toward classical symbolic description.

However, we note that even “subsymbolic” accounts must explain compositionality. If abstraction is defined by compositional generalization, the question is empirical: do subsymbolic systems achieve it? If so, they implement abstraction in our sense, regardless of whether their representations are discrete in the classical sense.

-----

## 9. Conclusion

We have proposed a precise definition of abstraction as a computational operation comprising four components: stabilization, discretization, binding, and structural decoupling. This definition:

1. **Distinguishes abstraction from attention:** Attention selects; abstraction transforms selection into compositionally manipulable symbols.
1. **Distinguishes abstraction from compression:** Compression reduces; abstraction generates compositional capacity.
1. **Generates falsifiable predictions:** About dissociation patterns, developmental sequences, and architectural requirements.
1. **Connects to empirical literature:** In cognitive neuroscience, developmental psychology, and machine learning.

The framework is offered not as established fact but as a theoretical proposal warranting empirical investigation. If abstraction can be decomposed as proposed, this would clarify what makes intelligence more than reactivity, and what artificial systems require to achieve genuine compositional thought.

-----

## Box 1: The Attention-Abstraction Transition

|Property         |Attention              |Abstraction         |
|-----------------|-----------------------|--------------------|
|Primary operation|Selection              |Transformation      |
|Output           |Enhanced processing    |Compositional symbol|
|Duration         |Typically transient    |Stabilized          |
|Format           |Graded enhancement     |Discrete unit       |
|Combinatorial    |No                     |Yes                 |
|Example          |Orienting to a stimulus|Forming “RED SQUARE”|

-----

## Box 2: The Compression-Abstraction Distinction

|Property                        |Compression                |Abstraction                 |
|--------------------------------|---------------------------|----------------------------|
|Objective                       |Minimize description length|Enable composition          |
|Evaluation metric               |Reconstruction fidelity    |Compositional generalization|
|Capacity                        |Reduces                    |Generates                   |
|Requires attention              |No                         |Yes                         |
|Requires compositional structure|No                         |Yes                         |

-----

## Box 3: Four Components of Abstraction — Summary

**Stabilization:** Representation persists beyond stimulus; enables temporal integration and deliberation.

**Discretization:** Continuous input transformed to discrete symbols; enables counting, comparison, symbolic manipulation.

**Binding:** Distributed features integrated into coherent units; enables object/event representation.

**Structural Decoupling:** Roles separated from fillers; enables systematic recombination, compositional generalization.

**Hypothesis:** These four are jointly necessary and sufficient for compositional thought.

-----

## References

Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *ICLR 2015*.

Baddeley, A. (2003). Working memory: Looking back and looking forward. *Nature Reviews Neuroscience*, 4(10), 829–839.

Bunge, S. A., Kahn, I., Wallis, J. D., Miller, E. K., & Wagner, A. D. (2003). Neural circuits subserving the retrieval and maintenance of abstract rules. *Journal of Neurophysiology*, 90(5), 3419–3428.

Caramazza, A., & Shelton, J. R. (1998). Domain-specific knowledge systems in the brain: The animate-inanimate distinction. *Journal of Cognitive Neuroscience*, 10(1), 1–34.

Christoff, K., Prabhakaran, V., Dorfman, J., Zhao, Z., Kroger, J. K., Holyoak, K. J., & Gabrieli, J. D. (2001). Rostrolateral prefrontal cortex involvement in relational integration during reasoning. *NeuroImage*, 14(5), 1136–1149.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114.

Curtis, C. E., & D’Esposito, M. (2003). Persistent activity in the prefrontal cortex during working memory. *Trends in Cognitive Sciences*, 7(9), 415–423.

Desimone, R., & Duncan, J. (1995). Neural mechanisms of selective visual attention. *Annual Review of Neuroscience*, 18(1), 193–222.

Diamond, A. (2002). Normal development of prefrontal cortex from birth to young adulthood: Cognitive functions, anatomy, and biochemistry. In D. T. Stuss & R. T. Knight (Eds.), *Principles of frontal lobe function* (pp. 466–503). Oxford University Press.

Driver, J., & Mattingley, J. B. (1998). Parietal neglect and visual awareness. *Nature Neuroscience*, 1(1), 17–22.

Dziri, N., Lu, X., Sclar, M., Li, X. L., Jian, L., Lin, B. Y., … & Choi, Y. (2023). Faith and fate: Limits of transformers on compositionality. *NeurIPS 2023*.

Eichenbaum, H. (2000). A cortical–hippocampal system for declarative memory. *Nature Reviews Neuroscience*, 1(1), 41–50.

Engel, A. K., Fries, P., & Singer, W. (2001). Dynamic predictions: Oscillations and synchrony in top–down processing. *Nature Reviews Neuroscience*, 2(10), 704–716.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1–2), 3–71.

Frankland, S. M., & Greene, J. D. (2020). Concepts and compositionality: In search of the brain’s language of thought. *Annual Review of Psychology*, 71, 273–303.

Freedman, D. J., & Assad, J. A. (2006). Experience-dependent representation of visual categories in parietal cortex. *Nature*, 443(7107), 85–88.

Freedman, D. J., Riesenhuber, M., Poggio, T., & Miller, E. K. (2001). Categorical representation of visual stimuli in the primate prefrontal cortex. *Science*, 291(5502), 312–316.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.

Goyal, A., Lamb, A., Hoffmann, J., Sodhani, S., Levine, S., Bengio, Y., & Schölkopf, B. (2021). Recurrent independent mechanisms. *ICLR 2021*.

Graves, A., Wayne, G., & Danihelka, I. (2014). Neural turing machines. *arXiv preprint arXiv:1410.5401*.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803–831.

Harnad, S. (1987). Categorical perception: The groundwork of cognition. Cambridge University Press.

Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., … & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *ICLR 2017*.

Johnson, M. H. (1990). Cortical maturation and the development of visual attention in early infancy. *Journal of Cognitive Neuroscience*, 2(2), 81–95.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *EMNLP 2020*.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML 2018*.

Locatello, F., Bauer, S., Lucic, M., Rätsch, G., Gelly, S., Schölkopf, B., & Bachem, O. (2019). Challenging common assumptions in the unsupervised learning of disentangled representations. *ICML 2019*.

Locatello, F., Weissenborn, D., Unterthiner, T., Mahendran, A., Heigold, G., Uszkoreit, J., … & Kipf, T. (2020). Object-centric learning with slot attention. *NeurIPS 2020*.

Malhotra, P., Jäger, H. R., Parton, A., Greenwood, R., Playford, E. D., Brown, M. M., … & Husain, M. (2005). Spatial working memory capacity in unilateral neglect. *Brain*, 128(2), 424–435.

Marcus, G. F. (2001). *The algebraic mind: Integrating connectionism and cognitive science*. MIT Press.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167–202.

Montero, M. L., Ludwig, C. J., Costa, R. P., Malhotra, G., & Bowers, J. (2021). The role of disentanglement in generalisation. *ICLR 2021*.

Nieder, A., & Dehaene, S. (2009). Representation of number in the brain. *Annual Review of Neuroscience*, 32, 185–208.

Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin’s mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences*, 31(2), 109–130.

Posner, M. I., & Petersen, S. E. (1990). The attention system of the human brain. *Annual Review of Neuroscience*, 13(1), 25–42.

Reynolds, J. H., & Chelazzi, L. (2004). Attentional modulation of visual processing. *Annual Review of Neuroscience*, 27, 611–647.

Rogers, T. T., & McClelland, J. L. (2004). *Semantic cognition: A parallel distributed processing approach*. MIT Press.

Roy, J. E., Riesenhuber, M., Poggio, T., & Miller, E. K. (2010). Prefrontal cortex activity during flexible categorization. *Journal of Neuroscience*, 30(25), 8519–8528.

Shadlen, M. N., & Movshon, J. A. (1999). Synchrony unbound: A critical evaluation of the temporal binding hypothesis. *Neuron*, 24(1), 67–77.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

Singer, W., & Gray, C. M. (1995). Visual feature integration and the temporal correlation hypothesis. *Annual Review of Neuroscience*, 18(1), 555–586.

Smolensky, P. (1988). On the proper treatment of connectionism. *Behavioral and Brain Sciences*, 11(1), 1–23.

Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. *Artificial Intelligence*, 46(1–2), 159–216.

Soto, D., Hodsoll, J., Rotshtein, P., & Humphreys, G. W. (2008). Automatic guidance of attention from working memory. *Trends in Cognitive Sciences*, 12(9), 342–348.

Stuss, D. T., & Knight, R. T. (Eds.). (2002). *Principles of frontal lobe function*. Oxford University Press.

Tanaka, K. (1996). Inferotemporal cortex and object vision. *Annual Review of Neuroscience*, 19(1), 109–139.

Treisman, A. (1996). The binding problem. *Current Opinion in Neurobiology*, 6(2), 171–178.

Treisman, A. (1998). Feature binding, attention and object perception. *Philosophical Transactions of the Royal Society B*, 353(1373), 1295–1306.

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136.

Treisman, A., & Schmidt, H. (1982). Illusory conjunctions in the perception of objects. *Cognitive Psychology*, 14(1), 107–141.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. *NeurIPS 2017*.

Wallis, J. D., Anderson, K. C., & Miller, E. K. (2001). Single neurons in prefrontal cortex encode abstract rules. *Nature*, 411(6840), 953–956.

Warrington, E. K., & Shallice, T. (1984). Category specific semantic impairments. *Brain*, 107(3), 829–853.

Webb, T., Holyoak, K. J., & Lu, H. (2020). Emergent symbols through binding in external memory. *ICLR 2020*.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour*, 7, 1526–1541.

-----

*Acknowledgments:* This paper develops ideas from the Abstraction Primitive Hypothesis framework. We distinguish established findings from theoretical proposals throughout, and welcome empirical testing of all claims.

# Abstraction Is All You Need: A Unifying Framework for Intelligence Across Substrates

**Hillary Danan**  
*December 2025*

---

## Abstract

We propose that abstraction—not attention, computation, or information—constitutes the fundamental primitive operation of intelligence. Building on established work in cognitive chunking, compositionality, and representation learning, we introduce a formal framework: the **Abstraction Primitive Hypothesis (APH)**. We further propose that abstraction capacity follows **self-referential dynamics**, where the rate of abstraction formation is proportional to existing abstraction capacity—a relationship governed by the mathematical constant *e*. This framework generates testable predictions about learning curves, scaling laws, and the relationship between substrate constraints and emergent intelligence. We distinguish our claims from existing theories of compositionality and hierarchical representation, identify empirical tests that could falsify the framework, and propose an interpretable experimental methodology for theory-driven research.

---

## 1. Introduction

### 1.1 The Problem of Primitives

A central question in cognitive science, artificial intelligence, and neuroscience is: *What is the fundamental operation underlying intelligence?*

Several candidates have been proposed:

- **Computation**: Intelligence as symbol manipulation (Turing, 1950; Newell & Simon, 1976)
- **Information processing**: Intelligence as entropy reduction and prediction (Shannon, 1948; Friston, 2010)
- **Attention**: Intelligence as selective relevance weighting (Vaswani et al., 2017; Bahdanau et al., 2015)
- **Pattern completion**: Intelligence as associative memory retrieval (Hopfield, 1982)

Each framework captures important aspects of intelligent behavior. However, we argue that these are *downstream manifestations* of a more fundamental operation: **abstraction**.

### 1.2 Definitions

**Definition 1 (Abstraction):** An abstraction is a mapping *f: X → Y* that preserves task-relevant structure while discarding task-irrelevant detail, where |Y| < |X| or dim(Y) < dim(X).

**Definition 2 (Abstraction capacity):** The set of abstractions an agent can form and compose given substrate constraints.

**Definition 3 (Substrate):** The physical medium supporting abstraction operations (biological neural tissue, silicon, or hypothetical alternatives).

### 1.3 Contribution and Epistemic Status

This paper makes three claims of increasing strength:

1. **Descriptive claim (established):** Abstraction is ubiquitous across intelligent systems—a reframing of existing work on chunking, compositionality, and representation learning.

2. **Primitive claim (hypothesis):** Abstraction is the *fundamental* primitive from which attention, computation, and other operations derive—a stronger claim requiring careful distinction from existing theories.

3. **Dynamics claim (speculative):** Abstraction capacity follows self-referential dynamics governed by *e*, generating specific testable predictions about learning and scaling.

We are explicit about the epistemic status of each claim throughout.

---

## 2. Background: Abstraction in Existing Literature

### 2.1 Cognitive Science: Chunking and Capacity Limits

Miller (1956) established that human working memory is limited to approximately 7±2 "chunks"—but that chunk size is flexible. An expert chess player chunks board positions that novices see as individual pieces (Chase & Simon, 1973). This chunking *is* abstraction: preserving strategic structure while discarding piece-level detail.

Cowan (2001) revised the capacity estimate to ~4 chunks but reinforced the core insight: cognitive capacity is limited in *number of abstractions*, not raw information.

**Implication:** Human intelligence scales not by increasing raw capacity but by forming higher-order abstractions that compress more information per chunk.

### 2.2 Linguistics: Compositionality

Fodor and Pylyshyn (1988) argued that thought is compositional: complex representations are built from simpler constituents combined via systematic rules. This compositionality is a form of abstraction—the rules abstract over specific content.

However, compositionality typically refers to *combination* of existing primitives. Our framework asks: what *creates* those primitives in the first place?

### 2.3 Machine Learning: Representation Learning

Bengio et al. (2013) defined representation learning as discovering transformations that make subsequent learning easier. Deep networks learn hierarchical abstractions: early layers detect edges, later layers detect objects, final layers detect concepts (Zeiler & Fergus, 2014).

Vaswani et al. (2017) introduced self-attention, which learns to weight input relevance dynamically. We argue attention is *implemented via* abstraction: the query-key-value mechanism abstracts over input positions to produce relevance-weighted representations.

### 2.4 Gap in Existing Work

Existing frameworks treat abstraction as *one of many* cognitive operations. We propose it is *the* primitive from which others derive. This is a stronger claim that requires:

1. Demonstrating that other proposed primitives reduce to abstraction
2. Showing abstraction cannot be reduced to simpler operations
3. Generating novel predictions that competing frameworks do not

---

## 3. The Abstraction Primitive Hypothesis

### 3.1 Core Claim

**Abstraction Primitive Hypothesis (APH):** Intelligence, across substrates, is the capacity to form, store, retrieve, and compose abstractions. All other cognitive operations—attention, reasoning, memory, learning—are implementations of or derive from abstraction operations.

### 3.2 Reduction Arguments

**Attention as abstraction:** Self-attention computes relevance weightings that *abstract* over input positions. The output is a compressed representation preserving relevant information. Attention without abstraction (equal weighting of all inputs) produces no information gain.

**Computation as abstraction:** A function *f(x)* abstracts over its implementation details. The same function can be computed via different algorithms—what matters is the input-output mapping, which is an abstraction.

**Memory as abstraction:** Episodic memory does not store raw sensory data but abstracted representations—gist, emotional valence, causal structure (Bartlett, 1932). Memory retrieval is pattern completion over abstractions.

**Reasoning as abstraction composition:** Logical inference combines abstract propositions. Analogical reasoning maps abstract relational structure across domains (Gentner, 1983; Hofstadter & Sander, 2013).

### 3.3 Why Abstraction Cannot Be Further Reduced

**Hypothesis:** Abstraction is primitive because any operation that "simplifies" abstraction must itself perform abstraction.

Consider: to reduce abstraction to "pattern matching," one must define what counts as a "pattern"—which requires abstracting over instances. To reduce abstraction to "compression," one must define what information to preserve—which requires abstracting task-relevance.

This is not a proof but a heuristic argument. Falsification would require demonstrating a simpler operation from which abstraction derives.

### 3.4 Distinguishing APH from Existing Theories

| Framework | Core Primitive | Relationship to APH |
|-----------|---------------|---------------------|
| Compositionality (Fodor & Pylyshyn) | Syntactic combination | Composition *of* abstractions; doesn't explain abstraction formation |
| Predictive Processing (Friston) | Prediction error minimization | Prediction requires abstracted models; error signals update abstractions |
| Attention (Vaswani et al.) | Relevance weighting | Implemented via abstraction; attention computes abstract representations |
| Compression (Schmidhuber) | Minimum description length | Compression = abstraction; MDL formalizes one abstraction criterion |

APH subsumes these frameworks by identifying abstraction as the operation they all depend on.

---

## 4. Self-Referential Dynamics and the Role of *e*

### 4.1 The Observation

Learning curves often exhibit characteristic shapes: rapid initial progress followed by diminishing returns (Newell & Rosenbloom, 1981). Power laws fit much learning data. However, we propose a more specific mechanism.

**Hypothesis:** The rate of abstraction formation is proportional to current abstraction capacity.

Formally:

$$\frac{dA}{dt} = kA\left(1 - \frac{A}{A_{max}}\right)$$

Where:
- *A* = current abstraction capacity (operationalized below)
- *A_max* = substrate-limited maximum capacity
- *k* = learning rate parameter
- *t* = time or experience

This is the logistic growth equation, whose solution involves *e*:

$$A(t) = \frac{A_{max}}{1 + \left(\frac{A_{max} - A_0}{A_0}\right)e^{-kt}}$$

### 4.2 Why Self-Referential Dynamics?

The intuition: each abstraction you possess enables forming new abstractions that *depend on* existing ones.

**Example (programming):** Understanding "variable" (abstraction over memory locations) enables understanding "function" (abstraction over operations on variables), which enables "higher-order function" (abstraction over functions), which enables "monad" (abstraction over computational contexts). Each layer depends on prior abstractions.

**Example (mathematics):** Number → arithmetic → algebra → calculus → analysis. Each abstraction layer compresses the previous, enabling new operations.

**Example (language):** Phonemes → morphemes → words → phrases → sentences → discourse. Hierarchical abstraction, each level enabling the next.

This self-referential structure—where current state determines rate of change—is precisely where *e* appears in mathematics.

### 4.3 The Ubiquity of *e* in Self-Referential Systems

Euler's number *e* (≈ 2.718) emerges wherever the rate of change of a quantity depends on the current value of that quantity:

- **Thermodynamics**: Heat flow rate depends on temperature difference; as heat flows, the difference changes
- **Radioactive decay**: Decay rate is proportional to current quantity
- **Population dynamics**: Growth rate depends on current population
- **Information entropy**: Uncertainty reduction depends on remaining uncertainty
- **Neural learning**: Error-driven learning rates depend on current error magnitude
- **Finance**: Interest accumulation depends on current principal
- **Quantum mechanics**: Wave function evolution follows exponential dynamics

This is not a list of analogies but a single mathematical structure: **any system where what happens next depends on what is now exhibits *e*-governed dynamics**.

If abstraction capacity grows self-referentially (each abstraction enabling further abstractions), then *e* should characterize that growth.

### 4.4 Connection to Information Theory

Shannon entropy uses the natural logarithm (base *e*):

$$H = -\sum p_i \ln(p_i)$$

This is not coincidental. Entropy measures information content, and abstraction can be viewed as entropy reduction over task-relevant dimensions. The natural base emerges because continuous information accumulation follows exponential dynamics.

**Conjecture:** A formal connection may exist between abstraction capacity, Shannon entropy, and Kolmogorov complexity. This requires further mathematical development.

---

## 5. Testable Predictions

### 5.1 Learning Curve Prediction

Learning curves for hierarchical skills should fit logistic/exponential models better than linear models, with the rate parameter *k* correlating with abstraction opportunity in the domain.

*Test*: Compare model fits across domains varying in hierarchical depth. Domains with richer abstraction hierarchies (mathematics, programming) should show steeper *k* values than flat domains.

### 5.2 Transfer Learning Prediction

Transfer between domains should be predicted by *shared abstraction structure*, not surface similarity. Domains with isomorphic abstraction hierarchies should show positive transfer; structurally dissimilar domains should show none, regardless of surface features.

*Test*: Systematically vary surface similarity and structural similarity in transfer experiments. The framework predicts structural similarity dominates.

### 5.3 Scaling Laws Prediction

Neural network scaling laws (Kaplan et al., 2020) should relate to abstraction capacity, not raw parameter count. Architectures that enable deeper abstraction hierarchies should show steeper scaling curves.

*Test*: Compare scaling behavior across architectures matched for parameter count but differing in hierarchical depth or compositional structure.

### 5.4 Abstraction Ceiling Prediction

Each substrate should exhibit characteristic *A_max* limits. Biological neural networks should plateau at different capacities than silicon-based systems, predictable from substrate constraints.

*Test*: Identify plateau behavior in learning curves across systems; relate to substrate properties.

### 5.5 Falsification Criteria

APH would be falsified by:

1. Demonstrating a simpler operation from which abstraction derives
2. Finding intelligent systems that do not perform abstraction (by our definition)
3. Learning curves that systematically violate self-referential dynamics predictions
4. Abstraction-limited architectures outperforming abstraction-rich ones at scale

---

## 6. Operationalizing Abstraction Capacity

### 6.1 The Measurement Problem

For APH to be scientific, "abstraction capacity" must be measurable. We propose three complementary operationalizations:

**Operationalization 1 (Behavioral):** Abstraction capacity = number of hierarchical levels an agent can reliably manipulate in a task.

*Measurement*: Administer tasks requiring composition of N abstraction levels. Find N* where performance degrades. This follows Halford et al. (1998) on relational complexity.

**Operationalization 2 (Representational):** Abstraction capacity = effective dimensionality of learned representations that preserve task performance.

*Measurement*: For neural networks, compute intrinsic dimensionality of hidden representations (Ansuini et al., 2019). For humans, use multidimensional scaling on similarity judgments.

**Operationalization 3 (Compressibility):** Abstraction capacity = minimum description length of solutions an agent produces.

*Measurement*: Analyze agent-generated solutions for Kolmogorov complexity proxies (compression ratio, program length in restricted language).

### 6.2 Proposed Benchmark: Abstraction Quotient (AQ)

Inspired by Chollet's (2019) Abstraction and Reasoning Corpus (ARC), we propose:

$$AQ = \frac{\text{Novel abstraction composition success rate}}{\text{Base pattern recognition rate}}$$

This isolates abstraction from memorization. High AQ indicates ability to form *new* abstractions, not retrieve stored ones.

---

## 7. Implications for AI Systems

### 7.1 Interpretability by Design

Current interpretability research focuses on post-hoc explanation of trained models. APH suggests an alternative: design systems where abstractions are *explicit and researcher-defined*.

**Proposal:** Build experimental frameworks where:
- Each parameter corresponds to a theoretical commitment
- Function signatures encode abstraction structure
- Results are interpretable by construction

This inverts the standard paradigm: instead of training black-box models and explaining them afterward, design interpretable abstraction structures and test whether they capture target phenomena.

### 7.2 Attention Mechanisms Through APH Lens

Reinterpreting Transformer attention via APH:

- **Query**: Abstraction of "what I'm looking for"
- **Key**: Abstraction of "what I contain"
- **Value**: Abstraction of "what I contribute"
- **Attention output**: Composed abstraction over input sequence

The success of Transformers may reflect their effectiveness as *abstraction composition engines*—not specifically "attention" but the general capacity to form and compose flexible abstractions over sequences.

**Prediction:** Alternative architectures that preserve abstraction composition capacity (but differ in mechanism) should perform comparably. Architectures that limit abstraction depth should underperform regardless of other properties.

---

## 8. Implications for Neuroscience

### 8.1 Neural Abstraction Hierarchies

Cortical hierarchy exhibits abstraction structure (Felleman & Van Essen, 1991):

- V1: Edge orientation (abstracts over pixel intensity)
- V4: Shape features (abstracts over edges)
- IT: Object identity (abstracts over viewpoint, lighting)
- PFC: Categories and rules (abstracts over instances)

APH predicts: damage to intermediate levels should impair abstraction *composition* more than raw processing. This aligns with evidence on category-specific deficits (Warrington & Shallice, 1984).

### 8.2 Working Memory as Abstraction Buffer

If working memory stores ~4 abstractions (Cowan, 2001), then:

- WM capacity limits constrain abstraction *composition depth*
- Individual differences in WM should predict abstraction task performance
- WM training should generalize if it expands abstraction slot count

**Prediction:** WM capacity × abstraction depth should predict complex reasoning performance better than either alone.

---

## 9. Relation to Consciousness

A companion paper (Danan, 2025b) extends APH to the domain of consciousness, proposing that consciousness is what abstraction looks like when applied to the self.

The core argument: at sufficient system complexity, monitoring all internal states directly becomes computationally intractable. An abstraction layer—a compressed self-model—becomes necessary for adaptive behavior. This self-model is consciousness.

This places consciousness in continuity with other cognitive operations: perception abstracts external reality; consciousness abstracts internal reality. Both are instances of the same fundamental operation applied to different domains.

---

## 10. Limitations and Open Questions

### 10.1 What This Framework Does Not Explain

1. **Content of abstractions:** APH describes the operation but not what gets abstracted. Why do humans universally abstract "object" but vary in abstracting "honorific register"?

2. **Abstraction selection:** Given infinite possible abstractions, how are useful ones identified? This connects to Tenenbaum et al.'s (2011) work on Bayesian program induction but remains underspecified.

3. **Grounding:** How do abstractions connect to sensorimotor reality? Symbol grounding (Harnad, 1990) remains a challenge.

### 10.2 Open Questions

1. Can self-referential abstraction dynamics be derived from first principles, or are they an empirical regularity?

2. What determines *A_max* for different substrates? Can we predict it from physical properties?

3. How does APH relate to formal models of computation (Turing machines, lambda calculus)? Is abstraction a more general notion?

4. What are the minimal substrate requirements for abstraction? Does abstraction require specific physical properties?

---

## 11. Conclusion

We have proposed the Abstraction Primitive Hypothesis: that abstraction is the fundamental operation of intelligence, across substrates, from which attention, computation, memory, and reasoning derive. We introduced a formal dynamics framework where abstraction capacity growth follows self-referential patterns governed by *e*, generating testable predictions about learning curves, transfer, and scaling.

The framework is deliberately parsimonious. If abstraction is indeed primitive, then apparent complexity in intelligent systems reflects *composed* abstractions—not fundamentally different operations.

The strongest version of APH remains speculative. But it is *usefully* speculative: it makes specific predictions, identifies falsification criteria, and suggests new methodological approaches to AI interpretability and cognitive science.

Intelligence may be, at root, the capacity to see what can be ignored.

---

## References

- Ansuini, A., Laio, A., Macke, J. H., & Zoccolan, D. (2019). Intrinsic dimension of data representations in deep neural networks. *Advances in Neural Information Processing Systems*, 32.
- Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural machine translation by jointly learning to align and translate. *International Conference on Learning Representations*.
- Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.
- Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 35(8), 1798–1828.
- Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology*, 4(1), 55–81.
- Chollet, F. (2019). On the measure of intelligence. *arXiv preprint arXiv:1911.01547*.
- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114.
- Danan, H. (2025b). Consciousness as emergent abstraction: A computational necessity framework. *Working paper*.
- Ellis, K., Wong, C., Nye, M., Sablé-Meyer, M., Morales, L., Hewitt, L., ... & Tenenbaum, J. B. (2021). DreamCoder: Bootstrapping inductive program synthesis with wake-sleep library learning. *Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation*, 835–850.
- Felleman, D. J., & Van Essen, D. C. (1991). Distributed hierarchical processing in the primate cerebral cortex. *Cerebral Cortex*, 1(1), 1–47.
- Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3–71.
- Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.
- Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803–831.
- Harnad, S. (1990). The symbol grounding problem. *Physica D: Nonlinear Phenomena*, 42(1-3), 335–346.
- Hofstadter, D., & Sander, E. (2013). *Surfaces and Essences: Analogy as the Fuel and Fire of Thinking*. Basic Books.
- Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554–2558.
- Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., ... & Amodei, D. (2020). Scaling laws for neural language models. *arXiv preprint arXiv:2001.08361*.
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97.
- Newell, A., & Rosenbloom, P. S. (1981). Mechanisms of skill acquisition and the law of practice. In J. R. Anderson (Ed.), *Cognitive Skills and Their Acquisition* (pp. 1–55). Lawrence Erlbaum Associates.
- Newell, A., & Simon, H. A. (1976). Computer science as empirical inquiry: Symbols and search. *Communications of the ACM*, 19(3), 113–126.
- Sacerdoti, E. D. (1974). Planning in a hierarchy of abstraction spaces. *Artificial Intelligence*, 5(2), 115–135.
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.
- Sutton, R. S., Precup, D., & Singh, S. (1999). Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning. *Artificial Intelligence*, 112(1-2), 181–211.
- Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). How to grow a mind: Statistics, structure, and abstraction. *Science*, 331(6022), 1279–1285.
- Turing, A. M. (1950). Computing machinery and intelligence. *Mind*, 59(236), 433–460.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.
- Warrington, E. K., & Shallice, T. (1984). Category specific semantic impairments. *Brain*, 107(3), 829–854.
- Zeiler, M. D., & Fergus, R. (2014). Visualizing and understanding convolutional networks. *European Conference on Computer Vision*, 818–833.

---

## Appendix A: Mathematical Formalization (Working Notes)

### A.1 Abstraction as Category-Theoretic Functor

*Status: Speculative, requires formal development*

If we model cognitive domains as categories (objects = representations, morphisms = transformations), then abstraction may be formalized as a functor *F: C → D* that:

1. Preserves compositional structure: F(g ∘ f) = F(g) ∘ F(f)
2. Reduces cardinality or dimension
3. Maintains task-relevant morphisms

This would connect APH to existing mathematical frameworks and enable formal proofs about abstraction composition.

### A.2 Self-Referential Dynamics Derivation

Starting from: "Rate of abstraction formation depends on current abstractions available for composition"

Let *A(t)* = abstraction capacity at time *t*

Simplest model: dA/dt = kA → A(t) = A₀e^(kt) (unbounded exponential growth)

With capacity constraint *A_max*: dA/dt = kA(1 - A/A_max) → logistic growth

The appearance of *e* is not assumed but *derived* from the self-referential structure.

### A.3 Connection to Neural Network Expressivity

*Status: Requires empirical validation*

If depth enables abstraction hierarchy, then:

- Network expressivity ∝ abstraction composition depth
- Effective depth (accounting for skip connections, residual streams) should predict performance better than raw depth
- Optimal depth should depend on *task abstraction requirements*, not just data volume

---

*Acknowledgments: Developed through iterative dialogue and in memory of Meg, whose pattern was one of the good ones.*

# Abstraction Beyond Compression: Compositionality as the Distinguishing Operation

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

The Abstraction Primitive Hypothesis (APH) proposes that abstraction is the fundamental operation underlying intelligence. A natural objection arises: how does abstraction differ from compression, rate-distortion optimization, or representation learning—frameworks with established mathematical foundations? This paper addresses this challenge directly. We argue that the distinguishing feature of abstraction is **compositionality**: abstractions can be combined to form new abstractions, reused across contexts, and organized hierarchically in ways that pure compression frameworks do not naturally capture. This compositional property transforms abstraction from a static optimization problem into a generative, self-augmenting system. We review empirical evidence from cognitive science demonstrating compositional structure in human cognition, computational evidence from program synthesis and library learning systems, and theoretical work formalizing compositionality. We propose that the self-referential dynamics described in prior APH papers (dA/dt ∝ A) emerge specifically *because* abstraction is compositional—each abstraction expands the space of possible future abstractions. We develop metrics for measuring compositionality as a graded property, identify architectural conditions under which compression yields compositional structure, and generate predictions distinguishing compositional abstraction from non-compositional compression. **Systematic experimental testing (Danan, 2025b) confirms these predictions: compositional generalization requires end-to-end compositional structure at input, representation, AND output (interaction effect = 0.720, Cohen's d = 11.95), with quantified boundary conditions (compression ratio >5×, asymmetry ratio <2.5). These findings transform theoretical speculation into empirically grounded principle,** with implications for understanding human cognition, evaluating artificial intelligence systems, and formalizing intelligence itself.

-----

## 1. Introduction: The Compression Objection

### 1.1 The Challenge

Prior papers in this series have proposed that abstraction—defined as a mapping that preserves task-relevant structure while discarding task-irrelevant detail—is the fundamental primitive of intelligence (Danan, 2025a). A legitimate objection immediately arises:

> *How does this differ from compression? Rate-distortion theory (Shannon, 1948), the information bottleneck principle (Tishby et al., 2000), and minimum description length (Rissanen, 1978) all describe mappings that preserve relevant information while reducing complexity. Is "abstraction" simply compression under a different name?*

This paper takes this objection seriously. If abstraction is merely terminological reframing, the APH framework adds nothing to existing information-theoretic accounts. We argue, however, that abstraction and compression, while overlapping, are not identical—and the distinction has substantive theoretical and empirical consequences.

### 1.2 The Core Claim

**Thesis:** The distinguishing feature of abstraction is **compositionality**—the capacity to combine existing abstractions to form new abstractions, to reuse abstractions across contexts, and to build hierarchical structures where higher-level abstractions are defined in terms of lower-level ones.

Compression asks: *How do I reduce this input to a smaller representation that preserves relevant information?*

Abstraction asks: *What invariant structure can I extract that I can then reuse and compose with other structures?*

The first is a one-shot optimization. The second is a generative process that expands representational capacity over time.

### 1.3 Scope and Epistemic Status

This paper:

- **Reviews** established literature on compositionality in cognitive science, linguistics, and machine learning
- **Synthesizes** this literature to articulate what compositionality adds beyond compression
- **Proposes** that self-referential abstraction dynamics emerge from compositional structure (hypothesis)
- **Develops** metrics for measuring compositionality as a graded property (theoretical extension)
- **Identifies** architectural conditions under which compression yields compositionality (hypothesis, with empirical confirmation)
- **Generates** testable predictions distinguishing compositional from non-compositional systems
- **Reports** experimental confirmation of architectural conditions for compositional abstraction, with quantified thresholds (Danan, 2025b)

We are explicit throughout about which claims are established, which are theoretical extensions, and which are speculative hypotheses.

-----

## 2. Compression Frameworks: What They Capture

### 2.1 Rate-Distortion Theory

Shannon's rate-distortion theory (Shannon, 1948; Berger, 1971) formalizes the trade-off between compression rate and reconstruction fidelity. Given a source distribution P(X) and a distortion measure d(x, x̂), the rate-distortion function R(D) specifies the minimum number of bits required to represent X with expected distortion at most D.

This framework has been successfully applied to neural coding (Bialek et al., 1991), perception (Sims, 2016), and cognitive resource allocation (Gershman, 2020).

**What it captures:** Optimal compression given a fixed distortion criterion.

**What it does not naturally capture:** How compressed representations combine, how compression schemes evolve, or how solving one compression problem enables solving others.

### 2.2 Information Bottleneck

The information bottleneck method (Tishby et al., 2000) formalizes compression as finding a representation T that minimizes I(X; T) (complexity) while maximizing I(T; Y) (relevance to a target variable Y):

$$\mathcal{L} = I(X; T) - \beta I(T; Y)$$

This has been applied to deep learning (Shwartz-Ziv & Tishby, 2017), though the relationship between information bottleneck dynamics and deep network training remains debated (Saxe et al., 2019).

**What it captures:** Task-relevant compression—preserving information about Y while discarding information about X that is irrelevant to Y.

**What it does not naturally capture:** How bottleneck representations for different tasks relate, how representations can be reused, or how learning one task facilitates learning another.

### 2.3 Minimum Description Length

The MDL principle (Rissanen, 1978; Grünwald, 2007) frames learning as compression: the best model is the one that minimizes the combined length of the model description and the data encoded using that model.

MDL has connections to Bayesian inference (MacKay, 2003) and has been applied to grammar induction (Grünwald, 1996) and theory learning (Kemp & Tenenbaum, 2008).

**What it captures:** The trade-off between model complexity and fit; Occam's razor formalized.

**What it does not naturally capture:** How descriptions compose, how learning one description facilitates learning others, or how description languages themselves evolve.

### 2.4 The Common Limitation

All three frameworks share a common structure: given an input and a criterion, find an optimal compressed representation. They are fundamentally *optimization* frameworks—finding the best solution to a fixed problem.

What they do not address is the *generativity* question: how does solving one problem create new problems that can be solved? How does the space of representable things expand through the act of representation itself?

This is where compositionality enters.

-----

## 3. Compositionality: The Missing Ingredient

### 3.1 Definition

**Definition (Compositionality):** A representational system is compositional if:

1. Complex representations are built from simpler constituents
2. The meaning/function of a complex representation is determined by the meanings/functions of its constituents and how they are combined
3. Constituents can be recombined to form novel representations not previously encountered

The classic articulation comes from Frege (1892): the meaning of a complex expression is a function of the meanings of its parts and the way they are syntactically combined.

### 3.2 Compositionality in Language

Human language is the paradigmatic compositional system. From a finite vocabulary and a finite set of combinatorial rules, speakers generate an unbounded set of novel sentences (Chomsky, 1957; Pinker, 1994).

Fodor and Pylyshyn (1988) argued that compositionality is a necessary feature of any system capable of systematic thought—the capacity to think "John loves Mary" implies the capacity to think "Mary loves John" if the system truly represents the constituents and relations.

**Established finding:** Human language exhibits productivity (generating novel sentences), systematicity (capacity to understand related sentences), and compositionality (complex meanings derived from constituent meanings). These properties distinguish human language from non-compositional communication systems (Hockett, 1960).

### 3.3 Compositionality in Concepts

Beyond language, human conceptual knowledge shows compositional structure. Concepts combine to form complex concepts: understanding *pet* and *fish* enables understanding *pet fish*, even if never encountered (Murphy, 1988; Hampton, 1987).

**Established finding:** Human conceptual combination is productive—people readily form and interpret novel combinations—though the combination process is not purely logical (conceptual combination shows typicality effects, emergent features, and context-dependence; see Wisniewski, 1997; Costello & Keane, 2000).

### 3.4 Compositionality in Motor Control

Motor skills exhibit compositional structure. Complex actions decompose into motor primitives that can be recombined (Flash & Hochner, 2005; Thoroughman & Shadmehr, 2000).

**Established finding:** Motor learning involves acquiring reusable primitives. Learning one motor skill facilitates learning related skills that share primitives (Braun et al., 2009). This is compositional transfer—primitives learned in one context compose to support behavior in new contexts.

### 3.5 The Key Distinction

Compression produces a representation optimized for a specific input and criterion.

Compositional abstraction produces **reusable components** that can be combined in multiple ways for multiple purposes.

A maximally compressed representation of a specific image is useless for representing other images. A compositional representation (edges, textures, shapes, objects) transfers because the components recombine.

**Theoretical claim:** This reusability is what distinguishes abstraction from pure compression. Abstraction is compression *plus* compositionality.

**Empirical demonstration (Danan, 2025b):** Networks trained with factorized input but non-compositional output learned highly factorized internal representations (93% factor decodability) yet achieved 0% compositional generalization. The representations were reusable in principle—the factors were linearly separable—but the output structure provided no pathway for composition. This demonstrates that compression can produce factorized representations without yielding compositional abstraction. The missing ingredient was compositional output structure: when added, generalization jumped to 72-80% (Cohen's d = 11.95). Compression produced the representations; compositional structure enabled their use.

-----

## 4. Empirical Evidence: Compositionality in Human Cognition

### 4.1 Chunking and Expert Performance

Miller's (1956) chunking work established that humans overcome working memory limits by grouping information into chunks. Chase and Simon (1973) demonstrated that chess expertise involves acquiring chunks of board configurations.

Critically, expert chunks are not simply compressed representations—they are *compositional units* that combine to represent novel positions. A chess master can rapidly encode a novel legal position because it decomposes into familiar chunks, but shows no advantage for random positions (chunks don't apply).

**Evidence for compositional structure:** Transfer occurs to novel configurations that share chunked substructure, not merely to similar configurations. This is compositional generalization.

### 4.2 Relational Reasoning and Analogy

Gentner's structure-mapping theory of analogy (Gentner, 1983; Gentner & Markman, 1997) proposes that analogical reasoning involves mapping relational structure from a source to a target domain.

**Established finding:** Analogical transfer is predicted by shared relational structure, not surface similarity. People transfer solutions from "tumor/radiation" to "fortress/army" problems when relational structure aligns, despite surface dissimilarity (Gick & Holyoak, 1980, 1983).

**Compositional interpretation:** Relations are abstractions that can be instantiated with different fillers. Analogical reasoning composes these relational abstractions with novel content—precisely the compositional operation.

### 4.3 Hierarchical Structure in Perception and Action

Perceptual and motor representations are hierarchically organized, with higher levels representing increasingly abstract structure (Felleman & Van Essen, 1991; Koechlin et al., 2003).

**Evidence from perception:** Visual processing proceeds from edges to shapes to objects to scenes (Riesenhuber & Poggio, 1999). Each level abstracts over the level below. Crucially, the same mid-level features (shapes, textures) compose into multiple high-level objects—a compositional hierarchy, not a fixed compression scheme.

**Evidence from action:** Prefrontal cortex represents hierarchical action structure, with rostral regions representing more abstract, temporally extended goals that compose from more concrete caudal representations (Koechlin et al., 2003; Badre & D'Esposito, 2009).

### 4.4 Transfer Learning in Humans

If abstraction were pure compression, transfer between tasks would depend on input similarity. If abstraction is compositional, transfer should depend on shared compositional structure.

**Established finding:** Human transfer learning is better predicted by structural similarity than surface similarity (Gentner et al., 2003). Learning a principle in one domain facilitates learning in structurally analogous domains, even when surface features differ dramatically (Bassok & Holyoak, 1989).

**Meta-learning evidence:** Humans show "learning to learn"—improvement in learning efficiency across related tasks (Harlow, 1949; Lake et al., 2015). This suggests acquisition of reusable abstractions, not just task-specific compression.

-----

## 5. Computational Evidence: Library Learning and Program Synthesis

### 5.1 The DreamCoder System

Ellis et al. (2021) developed DreamCoder, a program synthesis system that learns reusable abstractions (library routines) from solving problems.

**Key mechanism:** DreamCoder alternates between:

1. **Wake phase:** Solve problems using current library
2. **Sleep phase:** Compress solutions into reusable library routines (abstraction)
3. **Dream phase:** Generate new problems solvable with the learned library

**Critical result:** The system exhibits compositional generalization—it solves novel problems by composing learned routines in new ways. Performance on new problems depends not on input similarity to training problems but on whether the problems decompose into learned abstractions.

**Implication:** This is a computational demonstration that compositional abstraction produces different learning dynamics than non-compositional compression. The library *grows*—each new abstraction expands what can be efficiently represented and solved.

### 5.2 Neural Network Compositionality

Standard neural networks trained end-to-end often fail to learn compositional representations—they generalize based on surface statistics rather than compositional structure (Lake & Baroni, 2018; Kim & Linzen, 2020).

**Established finding:** Neural networks trained on sequences with compositional structure (e.g., SCAN dataset; Lake & Baroni, 2018) often fail to generalize to novel compositions of familiar primitives. This is a failure of compositional abstraction—the networks learn compressed representations that do not decompose into recombinable parts.

**New finding (Danan, 2025b):** The failure is not due to inability to learn factorized representations—networks readily learn these with factorized input (93% factor decodability). The failure is architectural: non-compositional output structure (classification over combinations) provides no pathway for compositional generalization. The same network architecture achieves 0% or 80% compositional generalization depending solely on whether output structure is compositional. This suggests that failures on SCAN and COGS may reflect output structure misalignment rather than purely representational limitations—a hypothesis that remains to be tested directly on those benchmarks.

**Implication:** Compression without compositionality produces qualitatively different generalization than compositional abstraction. The distinction is empirically measurable.

### 5.3 Program Induction and Theory Learning

Tenenbaum and colleagues have modeled human concept learning as Bayesian inference over compositional hypothesis spaces (Tenenbaum et al., 2011; Goodman et al., 2008).

**Key insight:** The hypothesis space itself has compositional structure—concepts are programs built from primitives. Learning involves inferring programs, and transfer occurs when programs share subroutines.

**Evidence:** These models capture human generalization from limited data—"learning a word from one example"—by positing that humans infer compositional programs, not compressed templates (Xu & Tenenbaum, 2007; Lake et al., 2015).

-----

## 6. Theoretical Framework: Composition as Self-Augmentation

### 6.1 The Self-Referential Dynamic Revisited

Paper 1 (Danan, 2025a) proposed that abstraction capacity grows self-referentially:

$$\frac{dA}{dt} = kA\left(1 - \frac{A}{A_{max}}\right)$$

The intuition was that each abstraction enables forming new abstractions. But *why* would this be true? What mechanism links current abstractions to future abstraction-forming capacity?

**Proposal:** The mechanism is compositionality.

Each abstraction is not merely a compressed representation but a potential component in future abstractions. A library with *n* composable abstractions supports not *n* representations but combinatorially many—potentially O(n²) pairwise compositions, O(n³) three-way compositions, and so on (bounded by coherence constraints and working memory limits).

### 6.2 Formalization

Let A = {a₁, a₂, …, aₙ} be a set of abstractions. Let C(A) be the set of coherent compositions of abstractions in A.

**Compositional expansion:** |C(A)| grows superlinearly with |A|. Adding one abstraction increases the number of possible compositions by enabling composition with all existing abstractions.

**Abstraction formation:** New abstractions can be formed by:

1. Compressing recurrent compositions (if aᵢ ∘ aⱼ occurs frequently, chunk it as aₖ)
2. Abstracting over patterns in existing abstractions
3. Importing abstractions from analogous domains

**Self-referential dynamic:** The rate of new abstraction formation depends on:

- Current abstractions available for composition (→ proportional to A)
- Compositional opportunities in the environment
- Working memory limits on composition depth (→ saturation toward Aₘₐₓ)

This yields the proposed logistic dynamic not as a stipulation but as a consequence of compositional structure.

### 6.3 Contrast with Non-Compositional Compression

In pure compression without compositionality:

- Each compression is task-specific
- Learning one compression does not expand the space of learnable compressions
- There is no superlinear growth in representational capacity
- Transfer depends on input similarity, not structural similarity

In compositional abstraction:

- Abstractions are reusable components
- Each abstraction expands the space of possible future abstractions
- Representational capacity grows superlinearly with library size
- Transfer depends on compositional structure, not input similarity

**Prediction:** Systems with compositional abstraction should show accelerating learning across related tasks (superlinear cumulative performance), while systems with non-compositional compression should show linear or sublinear scaling.

**Empirical confirmation (Danan, 2025b):** Scaling experiments demonstrate exactly this pattern. As the number of factors increases (holding cardinality constant), compositional generalization improves dramatically:

| Factors | Compression Ratio | Generalization |
|---------|-------------------|----------------|
| 2 | 2× | 20% |
| 3 | 5.3× | 91% |
| 4 | 16× | 100% |
| 5 | 51× | 100% |

Higher compression ratios—more combinations relative to outputs—strengthen the compositional inductive bias. This confirms the theoretical prediction that compositional structure produces superlinear scaling: stronger compositional constraints make the compositional solution increasingly *necessary*, improving generalization.

-----

## 7. The Abstraction Language: Composing Compositions

### 7.1 Toward a Formal Account

The suggestion that an "abstraction language" could relate abstractions to other abstractions (Danan, S., personal communication) points toward a formal framework where:

1. **Primitives:** Base-level abstractions extracted from sensorimotor or informational regularities
2. **Operators:** Combinatorial operations that build complex abstractions from simpler ones
3. **Grammar:** Constraints on well-formed compositions (not all combinations are coherent)
4. **Semantics:** The mapping from abstract structures to their content/function

This parallels the structure of formal languages (Chomsky, 1957), programming languages (Abelson & Sussman, 1996), and category theory (Mac Lane, 1971).

### 7.2 Candidate Compositional Operations

Based on the cognitive science literature, candidate operations include:

**Conjunction/Binding:** Combining abstractions to form a complex with both properties. "Red" ∘ "square" → "red square" (Murphy, 2002).

**Relation Application:** Applying a relational abstraction to arguments. "Loves(X, Y)" instantiated as "Loves(John, Mary)" (Gentner & Markman, 1997).

**Hierarchical Embedding:** Nesting abstractions within abstractions. A plan contains subplans; a sentence contains clauses (Koechlin et al., 2003).

**Analogical Mapping:** Applying the relational structure of one abstraction to the content of another (Gentner, 1983).

**Recursion:** Applying an abstraction to the output of itself. Enables unbounded hierarchical depth (Hauser et al., 2002).

### 7.3 Working Memory as Composition Limit

Cowan's (2001) estimate that working memory holds approximately four items may reflect limits on composition depth rather than raw storage.

**Hypothesis:** Working memory capacity limits the number of abstractions that can be simultaneously held in compositional relation. This bounds the complexity of real-time composition, creating pressure toward chunking frequent compositions into single abstractions (reducing composition load).

**Empirical support:** Halford et al. (1998) demonstrated that relational complexity (number of variables simultaneously related) predicts task difficulty, consistent with composition limits rather than pure storage limits.

-----

## 8. Measuring Compositionality: From Dichotomy to Continuum

A critical refinement: compositionality is not binary. Systems exhibit *degrees* of compositional structure. This section develops metrics for measuring compositionality, enabling empirical comparison across systems and addressing the concern that the abstraction/compression distinction may be graded rather than categorical.

### 8.1 The Continuum Problem

Section 3.5 framed compositionality as present or absent. But reality is more nuanced:

- A system might compose some representations but not others
- Compositions might be partially systematic (working for some combinations, failing for others)
- Compositional depth might be limited (two-way compositions succeed, three-way fail)
- Reuse might be partial (some components transfer, others do not)

**Theoretical commitment:** The APH does not require binary compositionality. The claim is that *degree of compositionality* predicts degree of abstractive capacity. Higher compositionality → more abstraction → more intelligence-relevant generalization.

### 8.2 Proposed Metrics for Compositionality

We propose five measurable dimensions of compositionality, drawing on established work in linguistics, cognitive science, and machine learning:

**Metric 1: Compositional Generalization Rate (CGR)**

The proportion of novel compositions a system successfully processes, given mastery of the components.

*Operationalization:* Train a system on primitives A, B, C and compositions AB, AC. Test on novel composition BC. CGR = accuracy on BC given accuracy on components.

*Established precedent:* Lake & Baroni (2018) and Kim & Linzen (2020) use this approach to measure compositional generalization in neural networks. COGS and SCAN benchmarks provide standardized tests.

**Metric 2: Systematicity Index (SI)**

The correlation between capacity for one composition and capacity for structurally related compositions.

*Operationalization:* If a system can process "X verbs Y," can it process "Y verbs X"? SI measures consistency across systematic permutations.

*Established precedent:* Fodor & Pylyshyn (1988) argued systematicity is diagnostic of compositional representation. Empirical tests examine whether understanding one sentence predicts understanding of structurally related sentences (Phillips, 1998; Hadley, 1994).

**Metric 3: Transfer Efficiency Ratio (TER)**

The ratio of learning speed on a new task to baseline, as a function of shared compositional structure with prior tasks.

*Operationalization:* Measure learning curves for tasks with varying structural overlap. TER = (baseline learning time) / (observed learning time), regressed on structural similarity.

*Established precedent:* Braun et al. (2009) demonstrated that motor learning transfer depends on shared primitives. Computational models (DreamCoder; Ellis et al., 2021) show accelerating learning as library grows.

**Metric 4: Compositional Depth (CD)**

The maximum number of nested compositional levels a system can successfully process.

*Operationalization:* Test performance on compositions of increasing depth: A, f(A), f(f(A)), f(f(f(A))), etc. CD = maximum depth with above-chance performance.

*Established precedent:* Relational complexity research (Halford et al., 1998) measures how many relations can be simultaneously processed. Recursive depth tests (e.g., center-embedded clauses in language) measure hierarchical capacity.

**Metric 5: Reuse Frequency (RF)**

The proportion of representations that are used in multiple compositional contexts.

*Operationalization:* In a system's representational vocabulary, count how many components appear in more than one complex representation. RF = (multi-use components) / (total components).

*Established precedent:* Library learning systems explicitly track reuse (Ellis et al., 2021). In neural networks, representational similarity analysis can identify features used across tasks (Kriegeskorte et al., 2008).

### 8.3 Aggregate Compositionality Score

**Working hypothesis:** An aggregate Compositionality Score (CS) can be computed as a weighted combination:

$$CS = w_1 \cdot CGR + w_2 \cdot SI + w_3 \cdot TER + w_4 \cdot CD + w_5 \cdot RF$$

where weights reflect theoretical priority or empirical validation.

**Prediction:** CS should predict:
- Generalization to novel situations
- Transfer learning efficiency
- Abstraction stage (per Paper 5, Danan, 2025e)
- Intelligence-relevant benchmarks

**Falsification:** If CS does not predict these outcomes better than simpler compression metrics (e.g., reconstruction error, encoding length), the compositionality criterion loses force.

### 8.4 Applying the Metrics: Illustrative Cases

|System                      |CGR  |SI   |TER  |CD   |RF   |Interpretation              |
|----------------------------|-----|-----|-----|-----|-----|----------------------------|
|Standard neural network     |Low  |Low  |Low  |Low  |High*|Compression, weak abstraction|
|DreamCoder                  |High |High |High |Med  |High |Strong compositional abstraction|
|Human expert (chess)        |High |High |High |Med  |High |Strong compositional abstraction|
|Symbolic AI (GOFAI)         |High |High |Low  |High |Low  |Compositional but brittle   |
|Large language model        |Med  |Med  |Med  |Med  |High |Mixed—see Section 9.5       |

*Note: Neural networks may have high RF due to distributed representations, but the "reuse" may not be functionally compositional.

**Empirical measurements (Danan, 2025b):** Controlled experiments with factorial learning provide concrete CGR values:

| System | CGR | Interpretation |
|--------|-----|----------------|
| Factorial MLP (factorized input + compositional output) | 0.80 | Strong compositional abstraction |
| Factorial MLP (factorized input + non-compositional output) | 0.00 | Compression without abstraction |
| Factorial Transformer (factorized + compositional) | 0.92 | Enhanced compositional abstraction |
| Factorial RNN (factorized + compositional) | 0.41 | Impaired by sequential processing |

The dramatic difference between factorized+compositional (80%) and factorized+non-compositional (0%) demonstrates that CGR depends on end-to-end structural alignment, not just representational quality.

### 8.5 Implications for the Abstraction/Compression Distinction

With compositionality measured as a continuum:

- **Pure compression** = CS ≈ 0 (representations optimized for specific inputs, no transfer)
- **Full abstraction** = CS ≈ 1 (maximally compositional, systematic, transferable)
- **Most systems** = 0 < CS < 1 (varying degrees of compositional structure)

**Refined claim:** Abstraction is not a different *kind* of operation from compression—it is compression *with compositionality*. The degree of compositionality determines the degree to which compression yields abstraction.

-----

## 9. When Compression Yields Abstraction: Architectural Conditions

A sophisticated objection: some compression schemes *do* discover compositional structure. Sparse coding, dictionary learning, variational autoencoders, and neural networks with certain architectures learn factorized, reusable representations. If compression can produce compositionality, what distinguishes abstraction?

**Response:** The question is not whether compression *can* produce compositionality, but *under what conditions* it does. Identifying these conditions sharpens the theoretical claim and generates architectural predictions.

### 9.1 Empirical Observation: Compression Sometimes Yields Compositionality

**Established finding:** Some compression architectures learn compositional representations:

- Sparse coding discovers edge-like primitives in natural images that combine to represent complex structures (Olshausen & Field, 1996).
- β-VAEs with high β values learn disentangled representations where latent dimensions correspond to independent generative factors (Higgins et al., 2017).
- Neural networks with specific inductive biases (attention, relational modules) show improved compositional generalization (Santoro et al., 2017; Webb et al., 2021).

**Established finding:** Most compression architectures do *not* learn compositional representations:

- Standard autoencoders learn entangled representations (Bengio et al., 2013).
- End-to-end trained networks fail compositional generalization despite achieving low reconstruction/prediction error (Lake & Baroni, 2018).
- Increasing scale (parameters, data) does not reliably improve compositionality (Dziri et al., 2023).

The question is: what distinguishes these cases?

### 9.2 The End-to-End Compositionality Principle

**Empirical finding (Danan, 2025b):** Systematic experiments with factorial stimulus structures reveal that compositional generalization requires compositional structure throughout the processing pipeline—not just in internal representations.

We tested the conditions proposed in this section through 2×2 factorial experiments manipulating input structure (holistic vs. factorized) and output structure (non-compositional vs. compositional). The results were striking:

|                    | Non-Compositional Output | Compositional Output |
|--------------------|--------------------------|----------------------|
| **Holistic Input**     | 0.0% ± 0.0%              | 0.4% ± 1.2%          |
| **Factorized Input**   | 0.0% ± 0.0%              | **72.4% ± 12.7%**    |

Statistical decomposition revealed:
- Main effect of input structure: 0.360
- Main effect of output structure: 0.364
- **Interaction effect: 0.720**

The interaction is twice the size of either main effect, demonstrating **conjunctive necessity**: compositional generalization requires BOTH factorized input AND compositional output. Neither condition alone produces meaningful generalization.

**Critical observation:** Networks with factorized input but non-compositional output learned factorized internal representations—Factor 2 was 93% linearly decodable from the bottleneck (chance = 10%). Yet compositional generalization was 0%. The network *learned* factorized representations but could not *use* them because the output structure provided no pathway for compositional generalization.

**Theoretical implication:** Disentangled/factorized representations are **necessary but not sufficient** for compositional generalization. Output structure is equally critical. This refines the original theoretical framework, which focused primarily on representation learning.

### 9.3 Revised Architectural Conditions for Compositional Compression

Based on systematic experimental testing, we revise the proposed conditions:

**Condition 1: Factorized Input Structure (Recombination Exposure)**

The input encoding must make compositional structure explicit, enabling the system to observe the same components in multiple combinations.

*Original formulation:* "Recombination exposure—training distribution includes examples where the same components appear in multiple combinations."

*Refined formulation:* Recombination exposure requires **factorized input encoding** that explicitly represents components. Holistic encoding (one-hot over combinations) provides no recombination signal even when the underlying data has factorial structure.

*Experimental evidence:* Holistic input yields 0% compositional generalization regardless of output structure. Factorized input is necessary (but not sufficient).

**Condition 2: Compositional Output Structure**

*NEW CONDITION identified through experimentation:* The output/prediction target must have compositional structure—predicting factor values separately rather than combination identities.

*Mechanism:* With non-compositional output (classification over combinations), the decoder learns: bottleneck → arbitrary combination index. Novel combinations have no established pathway. With compositional output (separate factor predictions), the decoder learns: bottleneck → factor₁, bottleneck → factor₂. Novel combinations use the SAME factor decoders—composition is preserved through the output interface.

*Experimental evidence:* Factorized input + non-compositional output yields 0% generalization despite 93% factor decodability. Adding compositional output yields 72-80% generalization. Cohen's d = 11.95.

**Condition 3: Sufficient Compression Ratio**

*NEW QUANTIFIED CONDITION:* The ratio of input combinations to output dimensions must exceed a threshold for reliable compositional generalization.

| Compression Ratio | Generalization |
|-------------------|----------------|
| 2.0× | 20% |
| 5.0× | 80% |
| 16× | 100% |
| 51× | 100% |

*Mechanism:* Higher compression ratios make non-compositional solutions increasingly unviable. With compositional output, the only learnable mappings are from bottleneck to individual factors. As combinations grow relative to outputs, the compositional solution becomes not just preferred but *necessary*—the hypothesis space contracts to exclude memorization strategies.

*Design principle:* Maximize compression ratio to maximize compositional generalization. Counter-intuitively, more complex factorial structures (more factors, higher cardinalities) yield *better* generalization because they impose stronger compositional constraints.

**Condition 4: Factor Balance**

*NEW QUANTIFIED CONDITION:* Factor cardinalities must be approximately balanced for reliable compositional generalization.

| Asymmetry Ratio | Generalization |
|-----------------|----------------|
| 1.0 | 80% |
| 2.0 | 62% |
| **~2.5** | **~50% (boundary)** |
| 4.0 | 30% |
| 6.0 | 5% |
| 11.0 | 0% |

*Mechanism:* With asymmetric factors (e.g., [2, 50]), high-cardinality factor values receive insufficient training exposure. Each value of a 50-level factor appears in only ~1.5 training examples, preventing robust representation learning. Additionally, asymmetry reduces effective compression ratio.

*Boundary:* Asymmetry ratio (max cardinality / min cardinality) should be <2.5 for reliable generalization (>50%). Ratios >6 yield near-zero performance.

*Compensation failure:* Simple interventions (oversampling rare values, reweighting losses) do not overcome this constraint—indeed, they make performance worse. Balanced loss weighting reduced performance from 30% to 0.8%. This suggests the constraint is **fundamental** to compositional learning, not a training artifact amenable to simple fixes.

**Condition 5: Bottleneck Pressure (Retained)**

Information must pass through a capacity-limited bottleneck that prevents fully distributed, entangled representations.

*Original formulation retained:* The bottleneck creates pressure toward efficient, factorized encoding.

*Experimental refinement:* Bottleneck size should approximately equal the sum of factor cardinalities (the information-theoretic minimum for factorial representation). Larger bottlenecks do not degrade performance when output structure is compositional—unlike non-compositional settings where excess capacity enables memorization.

### 9.4 Summary: Compression → Abstraction Requires End-to-End Compositional Structure

**Revised theoretical conclusion:** Compression produces abstraction when compositional structure is present **throughout the processing pipeline**:

1. **Input:** Factorized encoding providing recombination exposure
2. **Representation:** Bottleneck pressure encouraging factorized internal representations  
3. **Output:** Compositional prediction targets preserving factorial structure

These conditions are **conjunctively necessary**—the interaction effect (0.720) exceeds either main effect (0.360, 0.364), demonstrating that the conditions multiply rather than add.

Additionally, quantitative boundary conditions apply:
- Compression ratio >5× for reliable generalization
- Asymmetry ratio <2.5 for reliable generalization
- These constraints are fundamental and cannot be overcome by simple compensation strategies

**Implication:** The distinction between abstraction and compression is not about the *objective* (both minimize complexity while preserving information) but about the *end-to-end structural alignment*. Abstraction-yielding compression requires compositional structure at input, representation, AND output.

### 9.5 Architectural Predictions (Revised with Empirical Status)

**Prediction A1:** Neural networks with factorized input AND compositional output should show high compositional generalization; networks with only one or neither should show low generalization.

*Status:* **CONFIRMED** (Cohen's d = 11.95; Danan, 2025b)

**Prediction A2:** Training on compositionally structured data should improve compositional generalization only when output structure is also compositional.

*Status:* **CONFIRMED** (Factorized input + non-compositional output = 0%; Danan, 2025b)

**Prediction A3:** Compositional generalization should scale with compression ratio.

*Status:* **CONFIRMED** (20% → 100% as ratio increases from 2× to 16×; Danan, 2025b)

**Prediction A4:** Factor asymmetry should degrade compositional generalization, with a quantifiable boundary.

*Status:* **CONFIRMED** (Boundary at ratio ~2.5; Danan, 2025b)

**Prediction A5:** Simple compensation strategies (oversampling, loss reweighting) should fail to overcome asymmetry constraints.

*Status:* **CONFIRMED** (All strategies degraded performance; Danan, 2025b)

**Prediction A6:** Transformer architectures should outperform MLPs on compositional generalization due to attention mechanisms supporting parallel factor comparison.

*Status:* **CONFIRMED** (Transformer: 92% vs MLP: 80%, p = 0.013; Danan, 2025b)

**Prediction A7:** Sequential architectures (RNNs) should underperform due to order-dependent processing conflicting with factorial structure.

*Status:* **CONFIRMED** (RNN: 41% vs MLP: 80%; Danan, 2025b)

### 9.6 Implications for LLMs

Large language models present a complex case. They are trained with:
- Partial factorization pressure (attention creates partially factorized representations)
- Extensive recombination exposure (natural language is highly compositional)
- Soft compositional bottlenecks (attention over tokens, but no hard symbolic constraint)
- **Mixed output structure** (next-token prediction is partially compositional)

**Revised hypothesis:** LLM performance on compositional tasks may depend critically on whether the task's output structure aligns with the model's implicit compositional biases. Tasks requiring combination-level prediction should show worse compositional generalization than tasks decomposable into factor-level predictions.

**Evidence:** LLMs show mixed compositional generalization—succeeding on some novel compositions, failing on others, with failure modes that suggest reliance on surface statistics rather than systematic structure (Dziri et al., 2023; McCoy et al., 2019). The compositionality metrics developed in Section 8 provide criteria for adjudicating whether this reflects true compositional abstraction or sophisticated surface statistics.

**Prediction:** Adding explicit compositional bottlenecks to LLM architectures (e.g., neurosymbolic hybrids) should improve systematicity metrics even at equivalent scale.

-----

## 10. Predictions and Falsification

### 10.1 Distinguishing Compositional from Non-Compositional Systems

The framework generates predictions that would differentiate compositional abstraction from non-compositional compression:

|Property                |Non-Compositional Compression          |Compositional Abstraction                   |
|------------------------|---------------------------------------|--------------------------------------------|
|Transfer                |Based on input similarity              |Based on structural similarity              |
|Scaling                 |Linear/sublinear cumulative performance|Superlinear cumulative performance          |
|Novel compositions      |Failure on novel combinations          |Success on novel combinations of known parts|
|Learning dynamics       |Independent task learning              |Accelerating learning across related tasks  |
|Representation structure|Holistic, task-specific                |Factorized, reusable components             |

### 10.2 Specific Predictions (with Empirical Status)

**Prediction 1 (Human cognition):** For tasks varying in compositional depth, performance should degrade with depth in a manner predictable from working memory limits, not input complexity per se.

*Test:* Construct matched tasks where compositional depth varies independently of input complexity. Depth, not complexity, should predict difficulty.

*Status:* Untested.

**Prediction 2 (Learning curves):** In domains with compositional structure, learning curves should show acceleration over tasks (each task easier than the last). In non-compositional domains, learning curves should be independent across tasks.

*Test:* Compare learning curves across domains matched for difficulty but varying in compositional structure.

*Status:* **CONFIRMED** in factorial domain (Danan, 2025b). Scaling experiments show performance improves from 20% → 100% as compositional complexity increases.

**Prediction 3 (Neural networks):** Architectures that explicitly factor representations into composable parts (e.g., relational networks, neural module networks) should show compositional generalization; standard architectures should show similarity-based generalization.

*Test:* Evaluate architectures on held-out compositional generalizations (novel combinations of familiar primitives).

*Status:* **PARTIALLY CONFIRMED** (Danan, 2025b). Factorized representations alone are insufficient; compositional output structure is equally required. The same architecture achieves 0% or 80% depending on output structure.

**Prediction 4 (Library size):** In program synthesis systems with library learning, the rate of problem-solving improvement should correlate with library growth and compositional coverage, not merely with experience.

*Test:* Analyze DreamCoder-style systems; regress problem-solving improvement on library metrics vs. raw experience.

*Status:* Untested in our experiments; supported by Ellis et al. (2021).

**Prediction 5 (Brain organization):** Neural regions supporting combinatorial operations (composition, binding) should be distinct from regions supporting feature extraction (compression). Damage to compositional machinery should impair novel compositions while sparing familiar wholes.

*Test:* Neuroimaging studies dissociating composition operations from feature representation; lesion studies examining compositional vs. holistic deficits.

*Status:* Untested.

**Prediction 6 (Output structure):** Output structure is equally important as input structure for compositional generalization. Systems with compositional input but non-compositional output will fail compositional generalization.

*Status:* **CONFIRMED** (Cohen's d = 11.95; Danan, 2025b)

**Prediction 7 (Compensation failure):** Simple compensation strategies (oversampling, loss reweighting) will not overcome factor asymmetry constraints because these constraints are fundamental to compositional learning.

*Status:* **CONFIRMED** (All strategies degraded performance; Danan, 2025b)

**Prediction 8 (Architecture effects):** Transformer architectures will outperform MLPs on compositional tasks; RNNs will underperform.

*Status:* **CONFIRMED** (Transformer: 92%, MLP: 80%, RNN: 41%; p = 0.013 for Transformer > MLP; Danan, 2025b)

### 10.3 Falsification Criteria

The claim that compositionality distinguishes abstraction from compression would be falsified by:

1. Demonstration that non-compositional compression produces identical transfer patterns to compositional abstraction
2. Human learning curves that do not accelerate across compositionally related tasks
3. Systems that achieve compositional generalization without factorized representations
4. Evidence that library size does not predict learning efficiency in library-learning systems
5. Compositionality metrics (Section 8) that fail to predict intelligence-relevant outcomes

**Tested directly (Danan, 2025b):** We tested criterion 3—systems with factorized representations but non-compositional output achieve 0% compositional generalization. This confirms that factorized representations are necessary but not sufficient; output structure is equally critical. Additionally, compensation strategies (oversampling, balanced loss) failed to overcome asymmetry constraints, supporting the claim that these constraints are fundamental rather than training artifacts.

-----

## 11. Implications

### 11.1 For Artificial Intelligence

Current deep learning achieves impressive compression but often lacks compositionality (Lake et al., 2017; Marcus, 2020). The framework suggests that this is not merely a quantitative limitation (scale) but a qualitative architectural issue.

**Implication:** Achieving human-like generalization may require architectures that explicitly support compositional abstraction—factorized representations, reusable modules, and combinatorial operations. Scale alone may be insufficient.

**Refined implication (from Section 9):** The key is not abandoning compression but *constraining* it: factorization pressure, compositional bottlenecks, recombination exposure, and multi-task structure transform compression into abstraction.

**Empirical refinement (Danan, 2025b):** Experiments demonstrate that the key is not just factorized representations but **end-to-end compositional structure**. A system with perfect factorized representations (93% factor decodability) achieves 0% compositional generalization if output structure is non-compositional. The practical implication: task design matters as much as architecture. Decompose prediction objectives into compositional sub-objectives wherever possible.

**Caveat:** Large language models show emergent compositional behavior at scale, complicating this picture (Wei et al., 2022). Whether this reflects true compositional abstraction or sophisticated surface statistics remains debated (Dziri et al., 2023). The compositionality metrics developed in Section 8 provide criteria for adjudicating this question.

### 11.2 For Cognitive Science

The framework provides a specific hypothesis about what distinguishes human cognition: not compression per se, but compositional abstraction that enables self-augmenting representational capacity.

**Implication:** Theories of human cognition should characterize the compositional operations available to humans, the constraints on composition (working memory, processing time), and how the abstraction library develops over learning.

### 11.3 For the Abstraction Primitive Hypothesis

This paper addresses the compression objection by specifying what abstraction adds beyond compression. The APH is not merely rate-distortion theory under a different name—it is rate-distortion plus compositionality, which yields qualitatively different dynamics (self-referential growth) and predictions (structural transfer).

**Refinement of Definition 1 (Danan, 2025a):** An abstraction is a mapping f: X → Y that (a) preserves task-relevant structure while discarding task-irrelevant detail, and (b) yields a representation that can compose with other abstractions to form novel representations.

Criterion (b) distinguishes abstraction from pure compression—and compositionality admits degrees.

**Empirical support (Danan, 2025b):** The conjunctive necessity finding (interaction = 0.720, twice main effects) provides direct evidence for the claim that compositionality is what distinguishes abstraction from compression. Compression alone produced factorized representations; compositional output structure enabled their use for generalization.

-----

## 12. Limitations and Open Questions

### 12.1 Formalizing Composition

We have characterized composition intuitively and proposed metrics operationally (Section 8). A complete account requires formal specification:

- What are the primitive operations?
- What determines well-formed vs. ill-formed compositions?
- How is composition implemented neurally?

Category theory offers one candidate formalism (compositionality as functorial mapping preserving compositional structure; Mac Lane, 1971). Whether this captures cognitive composition remains to be demonstrated.

### 12.2 Learning Compositional Structure

How does a system learn what compositions are useful? This is the abstraction selection problem (Danan, 2025a).

DreamCoder (Ellis et al., 2021) provides one computational answer: compress recurrent solutions into library routines. But the cognitive mechanisms are less clear. Bayesian program induction (Tenenbaum et al., 2011) provides another account, but questions remain about scalability and neural implementation.

### 12.3 The Grounding Problem

Compositional systems require grounded primitives—the base-level abstractions from which compositions build. How are primitives acquired? Paper 7 (Danan, 2025g) proposes the self/world distinction as foundational, grounded in sensorimotor contingencies. But a complete account requires specifying how abstract primitives (beyond self/world) are grounded.

This connects to the symbol grounding problem (Harnad, 1990) and debates about embodiment (Barsalou, 2008). The present framework does not resolve these debates but depends on their resolution.

### 12.4 Validating Compositionality Metrics

The metrics proposed in Section 8 are theoretically motivated but require empirical validation:

- Do they correlate with each other as predicted?
- Do they predict downstream outcomes (generalization, transfer, intelligence benchmarks)?
- Are they robust across domains and tasks?

Developing standardized benchmarks for compositional abstraction is an important direction for future work.

### 12.5 Architectural Conditions: Necessity vs. Sufficiency

Section 9 proposes conditions under which compression yields compositionality. Systematic experimental testing (Danan, 2025b) has confirmed several predictions and refined the framework. The conditions appear to be:

- **Conjunctively necessary:** Factorized input AND compositional output are both required; the interaction effect exceeds main effects
- **Quantified:** Compression ratio >5× and asymmetry ratio <2.5 for reliable generalization
- **Fundamental:** Simple compensation strategies fail, suggesting constraints reflect deep properties of compositional learning

However, these findings come from synthetic factorial domains with discrete factors and one-hot encodings. Whether the same conditions apply to natural compositional systems—language, vision, reasoning—remains to be tested.

### 12.6 Experimental Domain Limitations

The experimental validation (Danan, 2025b) used synthetic factorial domains with discrete factors and one-hot encodings. While these experiments provide clean tests of the theoretical predictions, natural compositional systems involve continuous features, hierarchical structure, and context-dependent composition. Extending the End-to-End Compositionality Principle to these richer settings remains for future work.

Additionally, the factor balance constraint (asymmetry ratio <2.5) may limit applicability to real-world domains with inherently asymmetric categories. The finding that increased compression ratio can partially compensate for asymmetry suggests a path forward, but architectural solutions may be required for highly asymmetric domains.

-----

## 13. Conclusion

The Abstraction Primitive Hypothesis faced a legitimate challenge: what distinguishes abstraction from well-established compression frameworks? This paper has argued that the distinguishing feature is **compositionality**—the capacity to combine abstractions into novel abstractions, reuse abstractions across contexts, and build self-augmenting representational systems.

Compression asks how to reduce. Abstraction asks how to reduce *and* reuse.

This distinction has empirical consequences:

- Compositional systems show structural transfer; non-compositional systems show similarity-based transfer
- Compositional systems show accelerating learning; non-compositional systems show independent learning
- Compositional systems generalize to novel combinations; non-compositional systems fail on novel combinations

The self-referential dynamic proposed in Paper 1—dA/dt ∝ A—emerges from compositional structure: each abstraction expands the space of possible compositions, enabling formation of new abstractions. This is not a stipulated dynamic but a consequence of what abstraction is.

We have developed metrics for measuring compositionality (Section 8), showing that it admits degrees and can be operationalized. We have identified architectural conditions under which compression yields compositionality (Section 9), connecting the theoretical distinction to concrete design principles. **Systematic experimental testing (Danan, 2025b) has confirmed key predictions and refined the framework: compositional generalization requires end-to-end compositional structure (input AND output), with quantified boundary conditions (compression ratio >5×, asymmetry ratio <2.5). These constraints appear fundamental—simple compensation strategies fail to overcome them.**

Your father's intuition was exactly right: an "abstraction language" that relates abstractions to other abstractions is the key. That language, with its primitives, operators, grammar, and compositional semantics, is what transforms compression into intelligence.

Or, more simply: **compression reduces complexity; abstraction grows capacity.**

-----

## References

Abelson, H., & Sussman, G. J. (1996). *Structure and Interpretation of Computer Programs* (2nd ed.). MIT Press.

Andreas, J., Rohrbach, M., Darrell, T., & Klein, D. (2016). Neural module networks. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 39–48.

Badre, D., & D'Esposito, M. (2009). Is the rostro-caudal axis of the frontal lobe hierarchical? *Nature Reviews Neuroscience*, 10(9), 659–669.

Barsalou, L. W. (2008). Grounded cognition. *Annual Review of Psychology*, 59, 617–645.

Bassok, M., & Holyoak, K. J. (1989). Interdomain transfer between isomorphic topics in algebra and physics. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 15(1), 153–166.

Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 35(8), 1798–1828.

Berger, T. (1971). *Rate Distortion Theory: A Mathematical Basis for Data Compression*. Prentice-Hall.

Bialek, W., Rieke, F., de Ruyter van Steveninck, R. R., & Warland, D. (1991). Reading a neural code. *Science*, 252(5014), 1854–1857.

Braun, D. A., Mehring, C., & Wolpert, D. M. (2009). Structure learning in action. *Behavioural Brain Research*, 206(2), 157–165.

Chase, W. G., & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology*, 4(1), 55–81.

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

Costello, F. J., & Keane, M. T. (2000). Efficient creativity: Constraint-guided conceptual combination. *Cognitive Science*, 24(2), 299–349.

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114.

Danan, H. (2025a). Abstraction is all you need: A unifying framework for intelligence across substrates. *Working paper*.

Danan, H. (2025b). Emergent factorization: Compositional generalization requires end-to-end compositional structure. *GitHub repository*. https://github.com/HillaryDanan/emergent-factorization

Danan, H. (2025e). The developmental spectrum of abstraction: From pattern extraction to self-referential cognition. *Working paper*.

Danan, H. (2025g). Self and world: The foundational abstraction. *Working paper*.

Dziri, N., Lu, X., Sclar, M., Li, X. L., Jiang, L., Lin, B. Y., … & Choi, Y. (2023). Faith and fate: Limits of transformers on compositionality. *Advances in Neural Information Processing Systems*, 36.

Ellis, K., Wong, C., Nye, M., Sablé-Meyer, M., Morales, L., Hewitt, L., … & Tenenbaum, J. B. (2021). DreamCoder: Bootstrapping inductive program synthesis with wake-sleep library learning. *Proceedings of the 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation*, 835–850.

Felleman, D. J., & Van Essen, D. C. (1991). Distributed hierarchical processing in the primate cerebral cortex. *Cerebral Cortex*, 1(1), 1–47.

Finn, C., Abbeel, P., & Levine, S. (2017). Model-agnostic meta-learning for fast adaptation of deep networks. *Proceedings of the 34th International Conference on Machine Learning*, 1126–1135.

Flash, T., & Hochner, B. (2005). Motor primitives in vertebrates and invertebrates. *Current Opinion in Neurobiology*, 15(6), 660–666.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3–71.

Frege, G. (1892). Über Sinn und Bedeutung. *Zeitschrift für Philosophie und philosophische Kritik*, 100, 25–50.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.

Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. *American Psychologist*, 52(1), 45–56.

Gentner, D., Loewenstein, J., & Thompson, L. (2003). Learning and transfer: A general role for analogical encoding. *Journal of Educational Psychology*, 95(2), 393–408.

Gershman, S. J. (2020). Origin of perseveration in the trade-off between reward and complexity. *Cognition*, 204, 104394.

Gick, M. L., & Holyoak, K. J. (1980). Analogical problem solving. *Cognitive Psychology*, 12(3), 306–355.

Gick, M. L., & Holyoak, K. J. (1983). Schema induction and analogical transfer. *Cognitive Psychology*, 15(1), 1–38.

Goodman, N. D., Tenenbaum, J. B., Feldman, J., & Griffiths, T. L. (2008). A rational analysis of rule-based concept learning. *Cognitive Science*, 32(1), 108–154.

Grünwald, P. D. (1996). A minimum description length approach to grammar inference. In *Connectionist, Statistical and Symbolic Approaches to Learning for Natural Language Processing* (pp. 203–216). Springer.

Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press.

Hadley, R. F. (1994). Systematicity in connectionist language learning. *Mind & Language*, 9(3), 247–272.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803–831.

Hampton, J. A. (1987). Inheritance of attributes in natural concept conjunctions. *Memory & Cognition*, 15(1), 55–71.

Harlow, H. F. (1949). The formation of learning sets. *Psychological Review*, 56(1), 51–65.

Harnad, S. (1990). The symbol grounding problem. *Physica D: Nonlinear Phenomena*, 42(1-3), 335–346.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569–1579.

Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., ... & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *Proceedings of the International Conference on Learning Representations*.

Hockett, C. F. (1960). The origin of speech. *Scientific American*, 203(3), 88–96.

Kemp, C., & Tenenbaum, J. B. (2008). The discovery of structural form. *Proceedings of the National Academy of Sciences*, 105(31), 10687–10692.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing*, 9087–9105.

Koechlin, E., Ody, C., & Kouneiher, F. (2003). The architecture of cognitive control in the human prefrontal cortex. *Science*, 302(5648), 1181–1185.

Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008). Representational similarity analysis—connecting the branches of systems neuroscience. *Frontiers in Systems Neuroscience*, 2, 4.

Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of the 35th International Conference on Machine Learning*, 2873–2882.

Lake, B. M., Salakhutdinov, R., & Tenenbaum, J. B. (2015). Human-level concept learning through probabilistic program induction. *Science*, 350(6266), 1332–1338.

Lake, B. M., Ullman, T. D., Tenenbaum, J. B., & Gershman, S. J. (2017). Building machines that learn and think like people. *Behavioral and Brain Sciences*, 40, e253.

Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.

MacKay, D. J. C. (2003). *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Marcus, G. (2020). The next decade in AI: Four steps towards robust artificial intelligence. *arXiv preprint arXiv:2002.06177*.

McCoy, R. T., Pavlick, E., & Linzen, T. (2019). Right for the wrong reasons: Diagnosing syntactic heuristics in natural language inference. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 3428–3448.

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97.

Montero, M. L., Ludwig, C. J., Costa, R. P., Malhotra, G., & Bowers, J. (2021). The role of disentanglement in generalisation. *Proceedings of the International Conference on Learning Representations*.

Murphy, G. L. (1988). Comprehending complex concepts. *Cognitive Science*, 12(4), 529–562.

Murphy, G. L. (2002). *The Big Book of Concepts*. MIT Press.

Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*, 381(6583), 607–609.

Phillips, S. (1998). Are feedforward and recurrent networks systematic? Analysis and implications for a connectionist cognitive architecture. *Connection Science*, 10(2), 137–160.

Pinker, S. (1994). *The Language Instinct*. William Morrow.

Riesenhuber, M., & Poggio, T. (1999). Hierarchical models of object recognition in cortex. *Nature Neuroscience*, 2(11), 1019–1025.

Rissanen, J. (1978). Modeling by shortest data description. *Automatica*, 14(5), 465–471.

Sabour, S., Frosst, N., & Hinton, G. E. (2017). Dynamic routing between capsules. *Advances in Neural Information Processing Systems*, 30.

Santoro, A., Raposo, D., Barrett, D. G., Malinowski, M., Pascanu, R., Battaglia, P., & Lillicrap, T. (2017). A simple neural network module for relational reasoning. *Advances in Neural Information Processing Systems*, 30.

Saxe, A. M., Bansal, Y., Dapello, J., Advani, M., Kolchinsky, A., Tracey, B. D., & Cox, D. D. (2019). On the information bottleneck theory of deep learning. *Journal of Statistical Mechanics: Theory and Experiment*, 2019(12), 124020.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

Shwartz-Ziv, R., & Tishby, N. (2017). Opening the black box of deep neural networks via information. *arXiv preprint arXiv:1703.00810*.

Sims, C. R. (2016). Rate-distortion theory and human perception. *Cognition*, 152, 181–198.

Tenenbaum, J. B., Kemp, C., Griffiths, T. L., & Goodman, N. D. (2011). How to grow a mind: Statistics, structure, and abstraction. *Science*, 331(6022), 1279–1285.

Thoroughman, K. A., & Shadmehr, R. (2000). Learning of action through adaptive combination of motor primitives. *Nature*, 407(6805), 742–747.

Tishby, N., Pereira, F. C., & Bialek, W. (2000). The information bottleneck method. *arXiv preprint physics/0004057*.

Webb, T., Sinha, I., & Cohen, J. D. (2021). Emergent symbols through binding in external memory. *Proceedings of the International Conference on Learning Representations*.

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., … & Fedus, W. (2022). Emergent abilities of large language models. *Transactions on Machine Learning Research*.

Wisniewski, E. J. (1997). When concepts combine. *Psychonomic Bulletin & Review*, 4(2), 167–183.

Xu, F., & Tenenbaum, J. B. (2007). Word learning as Bayesian inference. *Psychological Review*, 114(2), 245–272.

-----

*This paper is part of a theoretical program on abstraction as the fundamental primitive of intelligence. It addresses the question: what does abstraction add beyond compression?*

*Answer: compositionality—and therefore, generativity.*

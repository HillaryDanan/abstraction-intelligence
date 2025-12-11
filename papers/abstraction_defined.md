# The Computational Structure of Abstraction

## Defining the Operation That Distinguishes Intelligence from Reactivity

-----

**Abstract**

What precisely is abstraction? Despite its centrality to theories of intelligence, the term remains underspecified—sometimes conflated with compression, categorization, or attention itself. This paper offers a precise operational definition: **abstraction is the formation of compositional representations**—representations that combine via systematic rules to generate novel meaningful structures. This single criterion distinguishes abstraction from attention (which selects but does not compose) and from compression (which reduces but does not generate). We identify enabling conditions (stabilization, attentional selection) and implementation requirements (token formation, combinatorial syntax) that systems must satisfy to achieve compositional capacity, while arguing that the criterion itself—not these supporting operations—defines abstraction. This definition generates falsifiable predictions about dissociations, developmental sequences, and architectural requirements for compositional generalization. We review evidence from cognitive neuroscience, developmental psychology, and machine learning, noting where empirical support is strong and where the framework remains hypothetical.

-----

## 1. Introduction

The capacity to form and manipulate abstract representations is widely regarded as central to intelligence (Halford et al., 1998; Penn et al., 2008; Gentner, 1983). Yet the term “abstraction” is used inconsistently across literatures—sometimes denoting categorization, sometimes compression, sometimes the formation of concepts, sometimes analogical mapping. This ambiguity impedes both theoretical progress and empirical testing.

We propose a precise definition: **abstraction is the capacity to form compositional representations**. A representation is compositional when it combines with other representations via systematic rules to yield novel structures with determinable meaning (Fodor & Pylyshyn, 1988; Szabó, 2012).

This is a *single criterion*, not a list of components. A system abstracts if and only if it forms representations that compose. Everything else—how it achieves this, what neural or computational machinery it employs—constitutes enabling conditions or implementation requirements, not the definition itself.

The central claim is not that abstraction is important—this is uncontroversial—but that abstraction *is* compositional representation. A system that performs attention without compositionality reacts; a system that achieves compositionality reasons.

### 1.1 Scope and Claims

This paper advances both established findings and theoretical proposals. We distinguish these carefully:

**Established (empirical support from multiple independent studies):**

- Compositionality is central to human language and thought (Fodor & Pylyshyn, 1988; Pinker, 1994)
- Systematicity—understanding novel combinations of familiar elements—is a signature of compositional structure (Fodor & Pylyshyn, 1988; Hadley, 1994)
- Compositional generalization in neural networks depends on architectural structure (Lake & Baroni, 2018; Kim & Linzen, 2020)
- Attention and categorization are dissociable processes (Posner & Petersen, 1990; Warrington & Shallice, 1984)
- Prefrontal cortex encodes abstract rules and categories (Freedman et al., 2001; Wallis et al., 2001)

**Proposed (theoretical framework requiring further testing):**

- The single-criterion definition of abstraction as compositional representation capacity
- The distinction between enabling conditions and implementation requirements
- The claim that attention is necessary but not sufficient for abstraction
- Specific predictions about dissociation patterns

-----

## 2. The Single Criterion: Compositional Representation

### 2.1 Definition

**Abstraction is the formation of compositional representations.**

A representation is compositional when:

1. It consists of parts (constituents) that are themselves meaningful
1. The meaning of the whole is determined by the meanings of the parts and their mode of combination
1. The same parts can recombine to form different wholes with different meanings

This definition derives from the principle of compositionality in semantics (Frege, 1892; Montague, 1970) and its application to mental representation (Fodor, 1975; Fodor & Pylyshyn, 1988).

**Example:** The representation RED SQUARE consists of RED and SQUARE combined. These can recombine: RED CIRCLE, BLUE SQUARE. Understanding “the cat chased the dog” requires representing CAT, DOG, and CHASED in roles (AGENT, PATIENT, ACTION) that can recombine: “the dog chased the cat” uses the same constituents in different roles.

**The test:** A system abstracts if it exhibits *systematicity*—the capacity to understand or produce novel combinations of familiar elements (Fodor & Pylyshyn, 1988). If a system can process “John loves Mary” but not “Mary loves John” given only exposure to the constituents, it lacks compositional structure and therefore does not abstract in the relevant sense.

### 2.2 Why One Criterion, Not Four Components?

Previous versions of this framework proposed four components: stabilization, discretization, binding, and structural decoupling. Critical analysis revealed problems with this decomposition:

**Problem 1: Mixed levels.** Stabilization (temporal persistence) is an enabling condition for many cognitive operations, not a distinctive feature of abstraction. Working memory supports perception, motor planning, and navigation—none of which require abstraction.

**Problem 2: Theoretical commitment.** Discretization presupposes that compositional representations must be symbolic in the classical sense. But connectionist systems may achieve compositionality through distributed representations without discrete symbols (Smolensky, 1990; although see Marcus, 2001, for counterarguments). Whether discreteness is required is an empirical question, not a definitional matter.

**Problem 3: Potential redundancy.** Binding and structural decoupling may not be separable operations. Tensor product binding (Smolensky, 1990) achieves both simultaneously—it binds fillers to roles. The claim that these are distinct requires empirical evidence of dissociation that is currently lacking.

**Problem 4: No derivation.** Why these four specifically? The original decomposition lacked principled justification for why this particular set, rather than some alternative, captures the structure of abstraction.

**Resolution:** Compositionality itself is the criterion. The “components” become either enabling conditions (what must be in place for compositionality to occur) or implementation requirements (what computational mechanisms achieve compositionality in specific systems). This is more parsimonious and avoids the problems above.

### 2.3 Relation to Classical Accounts

This definition is not novel—it recovers the core insight of classical cognitive science:

- **Language of Thought (Fodor, 1975):** Mental representations have compositional structure analogous to sentences.
- **Systematicity Argument (Fodor & Pylyshyn, 1988):** The systematicity of thought implies compositional structure; this is what connectionist systems must explain.
- **Compositional Semantics (Montague, 1970; Partee, 1984):** Linguistic meaning is compositionally determined.

What the present framework adds is:

1. Explicit identification of compositionality as the *criterion* for abstraction across domains
1. Distinction between the criterion and its implementation
1. Application to artificial systems with specific architectural predictions
1. Falsifiable predictions about dissociations and development

-----

## 3. Enabling Conditions

Enabling conditions are necessary for abstraction but do not constitute it. Their presence does not indicate abstraction; their absence prevents it.

### 3.1 Temporal Stabilization

**Definition:** The maintenance of representations beyond the duration of eliciting stimuli.

Compositional operations take time. Combining RED with SQUARE requires that both be simultaneously available. Without stabilization, representations decay before combination can occur.

**Empirical grounding:** Working memory maintains approximately four items in an active state (Cowan, 2001). Delay-period activity in prefrontal and parietal cortices maintains information across temporal gaps (Curtis & D’Esposito, 2003; Freedman et al., 2001).

**Why enabling, not defining:** Stabilization supports *any* complex processing—perception, motor planning, navigation, decision-making. A system with excellent stabilization but no compositional operations would not abstract. Conversely, a hypothetical system with very brief but sufficient stabilization that achieved composition would abstract.

### 3.2 Attentional Selection

**Definition:** The selective enhancement of some information over other information for processing.

Compositional operations require that relevant constituents be available for combination. Attention selects which representations enter the compositional process.

**Empirical grounding:** Attention modulates neural gain (Desimone & Duncan, 1995; Reynolds & Chelazzi, 2004). Feature integration requires focused attention (Treisman & Gelade, 1980).

**Why enabling, not defining:** Attention can occur without composition. Orienting to a stimulus, tracking a moving object, and filtering distractors are attentional operations that need not involve abstraction. A reflex arc involves selection (the stimulus that triggers response) without composition.

### 3.3 The Distinction Matters

A system might have:

- Attention without stabilization → cannot abstract (information decays before processing)
- Stabilization without attention → cannot abstract (no selection of constituents)
- Attention and stabilization without compositional operations → cannot abstract (enabling conditions met, criterion not met)
- Attention, stabilization, and compositional operations → abstracts

The enabling conditions are necessary but not sufficient. The criterion—compositional representation—is what makes the difference.

-----

## 4. Implementation Requirements

Implementation requirements are what systems must achieve to satisfy the compositionality criterion. These are *how* questions, not *what* questions.

### 4.1 Token Formation

To compose representations, a system needs representational units that can enter into combinations. These are “tokens” in the sense of reidentifiable particulars that can occupy different structural positions.

**The theoretical question:** Must tokens be discrete symbols, or can continuous/distributed representations function as tokens?

**Classical view (Fodor & Pylyshyn, 1988; Marcus, 2001):** Tokens must be discrete, context-independent symbols with determinate identity conditions.

**Alternative view (Smolensky, 1990; van Gelder, 1990):** Distributed representations can achieve functional compositionality without classical symbols.

**Empirical status:** This remains contested. The present framework is *neutral* on whether tokens must be discrete—what matters is whether the system achieves systematicity. If distributed representations support systematic recombination, they implement compositionality; if they do not, they fail regardless of whether they are “symbolic.”

**Neural evidence:** Prefrontal neurons encode categories independently of specific features (Freedman et al., 2001), and encode abstract rules that apply across stimuli (Wallis et al., 2001). Whether these are “discrete symbols” or “attractor states in a continuous dynamical system” (Amit, 1989) is interpretive.

### 4.2 Combinatorial Syntax

To compose representations meaningfully, a system needs rules or operations that combine tokens while preserving or generating meaning. This is the “syntax” of thought.

**What combinatorial syntax requires:**

- Roles that can be filled by different fillers (AGENT, PATIENT, etc.)
- Operations that preserve constituency (combining A and B yields [A B], not a new unstructured element)
- Systematic relationships between combinations and their meanings

**Empirical grounding:** The systematicity of language demonstrates combinatorial syntax in human cognition—understanding “John loves Mary” correlates perfectly with understanding “Mary loves John” across competent speakers (Fodor & Pylyshyn, 1988). Failures of systematicity in neural networks indicate lack of appropriate combinatorial structure (Lake & Baroni, 2018).

**Neural evidence:** Prefrontal cortex distinguishes roles from fillers—the same region encodes “agent” across different agents (Frankland & Greene, 2020). This suggests neural implementation of role-filler separation.

### 4.3 Relation to Previous “Components”

The previous four-component model maps onto this framework:

|Previous Component   |Status in Revised Framework                                                               |
|---------------------|------------------------------------------------------------------------------------------|
|Stabilization        |Enabling condition                                                                        |
|Discretization       |Contested implementation requirement (token formation may or may not require discreteness)|
|Binding              |Aspect of token formation (creating unified representations from features)                |
|Structural decoupling|Aspect of combinatorial syntax (role-filler independence)                                 |

This mapping shows that the previous components were not parallel categories but a mix of enabling conditions, implementation options, and aspects of the core criterion.

-----

## 5. Abstraction Is Not Attention

The distinction between attention and abstraction is fundamental.

### 5.1 Attention Selects; Abstraction Composes

Attention is selection: modulating which information is processed. Abstraction is composition: combining representations via systematic rules.

A reflex arc involves selection (the stimulus that controls behavior) without composition (no intermediate representations that recombine). Attention can be directed to single features, locations, or objects without forming compositional structures.

**The transition:** A system crosses from attention to abstraction when selected information enters into compositional operations—when representations are formed that can combine with other representations systematically.

### 5.2 Evidence for Dissociation

**Attentional deficits with intact abstraction:** Patients with hemispatial neglect cannot attend to contralesional space but retain abstract reasoning capacity for attended stimuli (Driver & Mattingley, 1998).

**Abstractive deficits with intact attention:** Category-specific semantic deficits show preserved attention with impaired categorical representation (Warrington & Shallice, 1984; Caramazza & Shelton, 1998). Frontal lesions impair abstract rule use while sparing attentional orienting (Stuss & Knight, 2002).

**Developmental dissociation:** Infants orient attention from birth but compositional reasoning develops over years (Johnson, 1990; Halford et al., 1998).

**Architectural dissociation:** Neural networks implement attention mechanisms (Vaswani et al., 2017) without achieving systematic compositional generalization (Lake & Baroni, 2018).

-----

## 6. Abstraction Is Not Compression

Compression and abstraction are often conflated because both produce more compact representations. But they differ fundamentally.

### 6.1 Compression Reduces; Abstraction Generates

Compression minimizes description length while preserving reconstruction capacity (Shannon, 1948). The output is a code—evaluated by fidelity and efficiency.

Abstraction produces representations that combine to generate novel structures. The output is compositional—evaluated by systematicity and generalization.

**Formal distinction:** Compression is measured by reconstruction error relative to encoding cost. Compositionality is measured by generalization to novel combinations. These can dissociate: excellent compression without compositional generalization (Locatello et al., 2019), or compositional structure without minimal encoding (Lake & Baroni, 2018).

**The JPEG test:** A compressed JPEG does not compose meaningfully with another JPEG. Concatenation produces garbage, not novel meaningful structure. Concepts compose: RED + SQUARE → RED SQUARE, a novel meaningful structure.

### 6.2 When Does Compression Yield Abstraction?

**Hypothesis:** Compression yields abstraction only when architectural constraints enforce compositional structure—factorized encoding with compositional output (see companion paper “Abstraction Beyond Compression”).

Deep autoencoders achieve excellent compression while learning representations that do not support compositional generalization (Locatello et al., 2019). Disentangled representation learning attempts both but requires specific inductive biases—compositionality does not emerge automatically from compression objectives (Higgins et al., 2017).

-----

## 7. Neural Substrates

If abstraction is compositional representation, its neural substrate should be where compositional structure is implemented.

### 7.1 Prefrontal Cortex

PFC is consistently implicated in compositional cognition:

**Category encoding:** PFC neurons encode learned categories independently of specific visual features (Freedman et al., 2001; Freedman & Assad, 2006).

**Rule encoding:** PFC neurons encode abstract rules that apply across stimulus dimensions (Wallis et al., 2001; Bunge et al., 2003).

**Relational encoding:** PFC represents relations between stimuli (Christoff et al., 2001).

**Role-filler separation:** PFC activity distinguishes roles from fillers (Frankland & Greene, 2020).

### 7.2 Network Interactions

Compositional representation likely emerges from PFC interaction with posterior cortices:

**Top-down modulation:** PFC biases sensory processing toward task-relevant features (Miller & Cohen, 2001).

**Working memory networks:** PFC-parietal circuits maintain information for compositional operations (Curtis & D’Esposito, 2003).

**Relational binding:** Hippocampus may contribute to binding elements into relational structures (Eichenbaum, 2000).

### 7.3 Developmental and Evolutionary Considerations

PFC is phylogenetically recent and develops slowly (Diamond, 2002). This is consistent with compositional capacity being a derived ability that builds on but exceeds basic attentional mechanisms.

Comparative evidence suggests that systematic compositionality is rare phylogenetically—present in humans and perhaps partially in great apes, limited or absent in other species (Penn et al., 2008; although see Gentner et al., 2006, for evidence of relational reasoning in baboons).

-----

## 8. Abstraction in Artificial Systems

The single-criterion definition generates clear predictions for AI.

### 8.1 The Test

Does the system exhibit systematicity? Can it generalize to novel combinations of familiar elements?

If a model learns “the cat sat on the mat” and “the dog ran in the park,” can it process “the cat ran in the park” without specific training? If yes, compositional. If no, not compositional—regardless of how impressive its performance on trained combinations.

### 8.2 Current Large Language Models

**Evidence for partial compositionality:** LLMs show some compositional generalization, analogical reasoning, and novel conceptual combination (Webb et al., 2023).

**Evidence for limitations:** LLMs fail systematically on tasks requiring strict compositional generalization, particularly with novel role-filler combinations (Lake & Baroni, 2018; Kim & Linzen, 2020). Performance degrades with relational complexity (Dziri et al., 2023).

**Interpretation:** LLMs may achieve partial or “soft” compositionality—systematic for some combinations, not others. Whether this constitutes genuine abstraction or sophisticated approximation is empirically underdetermined. The framework predicts that failures should cluster around tasks requiring novel role-filler combinations rather than novel feature combinations.

### 8.3 Architectural Predictions

**Prediction:** Architectures that enforce compositional structure should outperform standard architectures on systematicity tests.

- Factorized representations with compositional output structure should improve generalization (see companion paper)
- Explicit role-filler binding mechanisms should improve systematicity (Webb et al., 2020)
- Architectures without such structure should show systematicity failures regardless of scale

-----

## 9. Falsifiable Predictions

### 9.1 Dissociation Predictions

**Prediction 1:** Attentional and abstractive deficits should dissociate.

- Patients with attentional deficits should show preserved compositionality for attended stimuli
- Patients with compositional deficits should show preserved attention to elements they cannot compose

**Prediction 2:** Enabling conditions and compositionality should dissociate.

- Intact stabilization without compositionality: patients who maintain items but cannot combine them systematically
- Intact attention without compositionality: systems that select but do not compose

### 9.2 Developmental Predictions

**Prediction 3:** Compositionality should develop after enabling conditions are in place.

- Infants with mature attention and stabilization should still show compositionality limitations
- Compositionality should emerge gradually through childhood, correlated with PFC maturation (Diamond, 2002; Halford et al., 1998)

### 9.3 Architectural Predictions

**Prediction 4:** In artificial systems, attention mechanisms are insufficient for compositionality.

- Adding attention to a non-compositional architecture should not produce systematicity
- Systematicity requires compositional structure in representation and processing

**Prediction 5:** Compression is insufficient for compositionality.

- High-quality autoencoders without compositional constraints should fail systematicity tests
- Compositionality requires architectural enforcement, not emergent from compression

### 9.4 Threshold Prediction

**Prediction 6:** There should be a qualitative distinction between systems that achieve compositionality and those that approximate it.

- Systems with compositional structure should show flat generalization across novel combinations
- Systems without should show degradation with distance from training distribution

This prediction is harder to test because “distance from training” is difficult to quantify, but in principle distinguishes genuine compositionality from sophisticated interpolation.

-----

## 10. Limitations and Open Questions

### 10.1 The Graded Compositionality Problem

Human compositionality is not perfectly systematic. We understand some novel combinations better than others; there are prototype effects, context effects, and productivity limits. Does this mean human abstraction is “partial”?

**Possible resolution:** The criterion is whether a system has compositional *structure*, not whether it achieves perfect systematicity in all cases. Noise, resource limits, and interference can degrade performance without eliminating underlying compositional capacity—just as grammatical competence can coexist with performance errors.

**Open question:** How do we distinguish “compositional system with noise” from “non-compositional system with good interpolation”? This operationalization problem is not fully resolved.

### 10.2 The Implementation Neutrality Problem

We claimed the criterion is neutral on implementation—discrete vs. distributed, symbolic vs. subsymbolic. But can distributed representations really achieve full systematicity?

**The Marcus (2001) challenge:** Neural networks trained on examples fail to generalize to novel combinations in ways that suggest they lack genuine variables.

**The Smolensky (1990) response:** Tensor product representations can implement compositional structure in distributed form.

**Empirical status:** Whether any current artificial system achieves human-like systematicity is contested. The question remains open.

### 10.3 The Circularity Concern

If abstraction is defined as compositional representation, and we test abstraction by testing compositionality, have we explained anything?

**Response:** The definition is not circular—it is *clarifying*. It tells us what to look for (systematicity), what the criterion is (compositional structure), and what the enabling conditions and implementation requirements are. This generates testable predictions and rules out systems that fail the criterion.

What the definition does *not* explain is why compositionality is adaptive. The functional story—compositionality solves combinatorial explosion, enabling finite systems to handle infinite possibility spaces—provides this (see README discussion).

-----

## 11. Conclusion

We have proposed that **abstraction is the formation of compositional representations**. This single criterion:

1. **Defines the phenomenon:** Abstraction is compositionality—the capacity to combine representations systematically to generate novel meaningful structures.
1. **Distinguishes abstraction from attention:** Attention selects; abstraction composes. Selection is necessary but not sufficient.
1. **Distinguishes abstraction from compression:** Compression reduces; abstraction generates. Compact codes need not be compositional.
1. **Identifies enabling conditions:** Stabilization and attentional selection are necessary for compositional operations but do not constitute abstraction.
1. **Identifies implementation requirements:** Token formation and combinatorial syntax are what systems must achieve, though how they achieve it (discrete vs. distributed, symbolic vs. subsymbolic) remains an empirical question.
1. **Generates falsifiable predictions:** About dissociations, development, and architectural requirements.

The framework is offered not as established fact but as a theoretical proposal warranting empirical investigation. If compositionality is the criterion for abstraction, this clarifies what makes intelligence more than reactivity, and what artificial systems require to achieve genuine abstract thought.

-----

## Box 1: The Single Criterion

|Question            |Answer                                                |
|--------------------|------------------------------------------------------|
|What is abstraction?|Formation of compositional representations            |
|How do we test it?  |Systematicity—generalization to novel combinations    |
|What enables it?    |Stabilization, attentional selection                  |
|What implements it? |Token formation, combinatorial syntax                 |
|What is it not?     |Attention (which selects), compression (which reduces)|

-----

## Box 2: Enabling Conditions vs. Implementation Requirements

|Type                       |Examples                             |Relation to Abstraction                                                   |
|---------------------------|-------------------------------------|--------------------------------------------------------------------------|
|Enabling conditions        |Stabilization, attention             |Necessary but not sufficient; their presence does not indicate abstraction|
|Implementation requirements|Token formation, combinatorial syntax|How systems achieve compositionality; may vary across implementations     |
|The criterion              |Compositional representation         |The defining feature; what makes abstraction abstraction                  |

-----

## Box 3: The Abstraction Test

A system abstracts if and only if it forms **compositional representations**:

- Representations with **meaningful parts**
- Parts that combine via **systematic rules**
- Same parts **recombine** into different wholes
- Test: **Systematicity**—novel combinations of familiar elements

**Examples of passing:**

- Understanding “Mary loves John” given “John loves Mary”
- Representing RED CIRCLE given RED, CIRCLE, and BLUE SQUARE

**Examples of failing:**

- Memorizing “John loves Mary” without generalizing
- Interpolating between trained examples without systematic recombination

-----

## References

Amit, D. J. (1989). *Modeling brain function: The world of attractor neural networks*. Cambridge University Press.

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

Fodor, J. A. (1975). *The language of thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1–2), 3–71.

Frankland, S. M., & Greene, J. D. (2020). Concepts and compositionality: In search of the brain’s language of thought. *Annual Review of Psychology*, 71, 273–303.

Freedman, D. J., & Assad, J. A. (2006). Experience-dependent representation of visual categories in parietal cortex. *Nature*, 443(7107), 85–88.

Freedman, D. J., Riesenhuber, M., Poggio, T., & Miller, E. K. (2001). Categorical representation of visual stimuli in the primate prefrontal cortex. *Science*, 291(5502), 312–316.

Frege, G. (1892). Über Sinn und Bedeutung. *Zeitschrift für Philosophie und philosophische Kritik*, 100, 25–50.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.

Gentner, T. Q., Fenn, K. M., Margoliash, D., & Nusbaum, H. C. (2006). Recursive syntactic pattern learning by songbirds. *Nature*, 440(7088), 1204–1207.

Hadley, R. F. (1994). Systematicity in connectionist language learning. *Mind & Language*, 9(3), 247–272.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803–831.

Higgins, I., Matthey, L., Pal, A., Burgess, C., Glorot, X., Botvinick, M., … & Lerchner, A. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *ICLR 2017*.

Johnson, M. H. (1990). Cortical maturation and the development of visual attention in early infancy. *Journal of Cognitive Neuroscience*, 2(2), 81–95.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge based on semantic interpretation. *EMNLP 2020*.

Lake, B., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *ICML 2018*.

Locatello, F., Bauer, S., Lucic, M., Rätsch, G., Gelly, S., Schölkopf, B., & Bachem, O. (2019). Challenging common assumptions in the unsupervised learning of disentangled representations. *ICML 2019*.

Marcus, G. F. (2001). *The algebraic mind: Integrating connectionism and cognitive science*. MIT Press.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167–202.

Montague, R. (1970). Universal grammar. *Theoria*, 36(3), 373–398.

Partee, B. (1984). Compositionality. In F. Landman & F. Veltman (Eds.), *Varieties of formal semantics* (pp. 281–311). Foris.

Penn, D. C., Holyoak, K. J., & Povinelli, D. J. (2008). Darwin’s mistake: Explaining the discontinuity between human and nonhuman minds. *Behavioral and Brain Sciences*, 31(2), 109–130.

Pinker, S. (1994). *The language instinct*. William Morrow.

Posner, M. I., & Petersen, S. E. (1990). The attention system of the human brain. *Annual Review of Neuroscience*, 13(1), 25–42.

Reynolds, J. H., & Chelazzi, L. (2004). Attentional modulation of visual processing. *Annual Review of Neuroscience*, 27, 611–647.

Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. *Artificial Intelligence*, 46(1–2), 159–216.

Stuss, D. T., & Knight, R. T. (Eds.). (2002). *Principles of frontal lobe function*. Oxford University Press.

Szabó, Z. G. (2012). The case for compositionality. In M. Werning, W. Hinzen, & E. Machery (Eds.), *The Oxford handbook of compositionality* (pp. 64–80). Oxford University Press.

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136.

van Gelder, T. (1990). Compositionality: A connectionist variation on a classical theme. *Cognitive Science*, 14(3), 355–384.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. *NeurIPS 2017*.

Wallis, J. D., Anderson, K. C., & Miller, E. K. (2001). Single neurons in prefrontal cortex encode abstract rules. *Nature*, 411(6840), 953–956.

Warrington, E. K., & Shallice, T. (1984). Category specific semantic impairments. *Brain*, 107(3), 829–853.

Webb, T., Holyoak, K. J., & Lu, H. (2020). Emergent symbols through binding in external memory. *ICLR 2020*.

Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical reasoning in large language models. *Nature Human Behaviour*, 7, 1526–1541.

-----

*Acknowledgments:* This paper develops ideas from the Abstraction Primitive Hypothesis framework. Previous versions proposed a four-component decomposition; critical analysis revealed that a single criterion—compositional representation—is more parsimonious and avoids conflating enabling conditions with defining features. We distinguish established findings from theoretical proposals throughout and welcome empirical testing of all claims.

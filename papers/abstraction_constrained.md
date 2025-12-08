# Abstraction Constrained: What the Primitive Is and Is Not

**Hillary Danan, PhD**  
*December 2025*

-----

## Abstract

The Abstraction Primitive Hypothesis (APH) claims that abstraction is the fundamental operation underlying intelligence. A natural objection arises: if all cognitive operations derive from abstraction, what *isn’t* abstraction? Does the concept become so capacious it loses explanatory power? This paper addresses the vacuity objection directly. We argue that abstraction is a specific, constrained operation: the conversion of attended information into manipulable, composable symbols. This operation is distinct from input operations (perception, attention) that select what gets abstracted, and from downstream operations (memory, learning, reasoning, decision-making, action) that operate *on* abstractions. Abstraction is the central transformation—the operation that creates the representational currency other cognitive operations trade in—but it is not identical to cognition itself. We provide criteria for distinguishing abstraction from related operations, identify empirical signatures of abstraction failure distinct from failures of input or downstream operations, and specify what would falsify the claim that abstraction is primitive. The framework is constrained enough to be wrong.

-----

## 1. Introduction

### 1.1 The Vacuity Objection

The Abstraction Primitive Hypothesis (Danan, 2025a) proposes that abstraction—the formation of manipulable, composable symbols from attended information—is the fundamental operation of intelligence. All other cognitive operations, the claim goes, either feed into abstraction or operate on its products.

A reasonable objection: if attention, reasoning, memory, learning, and decision-making all “derive from” abstraction, then abstraction explains everything. And a concept that explains everything explains nothing. It becomes synonymous with “cognition” or “information processing”—too broad to do theoretical work.

This paper takes the objection seriously. We argue that it fails, but only because abstraction is more constrained than the objection assumes. The concept has boundaries. It can be distinguished from related operations. It generates predictions that could be false.

### 1.2 The Claim, Precisely Stated

**Abstraction** is the operation of converting attended information into manipulable, composable symbols.

This definition has three components:

1. **Input**: Attended information (not raw sensory input, but input that has been selected by attention)
1. **Operation**: Conversion into symbols (not mere storage or transmission)
1. **Output**: Representations that are manipulable (can be operated on) and composable (can combine with other representations)

The claim is that this specific operation is the primitive of intelligence—not that it is synonymous with intelligence.

### 1.3 Epistemic Status

- **Established**: Supported by peer-reviewed literature
- **Theoretical**: Logical extensions of established findings
- **Hypothesis**: Novel claims requiring empirical validation

-----

## 2. What Abstraction Is Not

To constrain the concept, we specify what abstraction is *not*. Each of the following is a distinct operation, not reducible to abstraction.

### 2.1 Abstraction Is Not Perception

**Perception** is the transduction of physical signals into neural representations. Light becomes retinal activation; pressure becomes mechanoreceptor firing; molecules become olfactory signals.

**Distinction**: Perception is *input*. It occurs prior to abstraction and provides the raw material. A system can perceive without abstracting—sensory transduction without symbol formation. Insects perceive extensively but abstract minimally (with notable exceptions; see Giurfa, Zhang, Jenett, Menzel, & Srinivasan, 2001).

**Empirical marker**: Perceptual processing can occur without abstraction. Subliminal perception demonstrates sensory transduction without conscious symbol formation (Dehaene et al., 1998). Blindsight patients perceive without reportable representations (Weiskrantz, 1986).

### 2.2 Abstraction Is Not Attention

**Attention** is the selection and prioritization of information for further processing. It is a spotlight, a filter, a gate.

**Distinction**: Attention is *input selection*. It determines what gets abstracted, but it is not itself the abstraction operation. You can attend to something without abstracting it—a flash of light captures attention without necessarily being encoded as a manipulable symbol.

**Established**: Attention and abstraction are dissociable. Patients with parietal lesions show attentional deficits (hemispatial neglect) while retaining abstractive capacity for attended information (Husain & Rorden, 2003). Conversely, patients with prefrontal lesions may attend normally but fail to form abstract rules from attended exemplars (Wallis, Anderson, & Miller, 2001).

**Empirical marker**: Attention without abstraction produces orienting without encoding. Abstraction without attention is impossible—attention is a necessary input condition—but attention without abstraction is not.

### 2.3 Abstraction Is Not Memory

**Memory** is the storage and retrieval of information over time.

**Distinction**: Memory operates *on* abstractions. It stores them, consolidates them, retrieves them. But memory is not the operation that creates abstractions in the first place.

**Established**: Memory systems are dissociable. Procedural memory can store motor patterns without declarative abstraction (Squire & Zola, 1996). Working memory maintains abstractions for manipulation (Baddeley, 2012). Long-term memory consolidates abstractions across time (Frankland & Bontempi, 2005). Each of these is an operation on abstractions, not the creation of them.

**Empirical marker**: Memory failures are distinct from abstraction failures. Amnesic patients can form abstractions in the moment but fail to store them (intact abstraction, impaired memory). Patients with category-specific deficits fail to form certain abstractions but can store what they do form (impaired abstraction, intact memory for other categories; Warrington & Shallice, 1984).

### 2.4 Abstraction Is Not Learning

**Learning** is the modification of representations or behaviors based on experience.

**Distinction**: Learning operates *on* abstractions. It updates them, refines them, connects them. But learning presupposes that there are abstractions to update. You cannot learn relationships between symbols if you have no symbols.

**Established**: Learning requires prior representational structure. The “blessing of abstraction” in machine learning: systems with appropriate abstractions learn faster and generalize better than systems that must learn from raw features (Bengio, Courville, & Vincent, 2013). Transfer learning succeeds when source and target share abstract structure (Pan & Yang, 2010).

**Empirical marker**: Learning failures are distinct from abstraction failures. A system might abstract well but learn slowly (high initial performance, poor improvement). Or abstract poorly but learn well within its limited representations (low ceiling, fast approach). These are dissociable profiles.

### 2.5 Abstraction Is Not Reasoning

**Reasoning** is the manipulation of representations to derive new conclusions.

**Distinction**: Reasoning operates *on* abstractions. Logical inference, analogy, causal reasoning—all involve manipulating symbolic representations. But the representations must first exist. Reasoning is what you do *with* abstractions, not how you form them.

**Established**: Reasoning capacity correlates with but is not identical to abstractive capacity. Relational complexity theory (Halford, Wilson, & Phillips, 1998) shows that reasoning capacity depends on the ability to represent relations—which are abstractions. But the formation of relational representations and their subsequent manipulation are distinct operations.

**Empirical marker**: Reasoning failures can occur with intact abstraction. A person might form the relevant abstractions but fail to manipulate them correctly (intact representation, impaired inference). Conversely, reasoning can succeed given abstractions the person did not form themselves (using provided representations).

### 2.6 Abstraction Is Not Decision-Making

**Decision-making** is the selection of actions based on represented options and values.

**Distinction**: Decision-making operates *on* abstractions. To decide, a system must represent options, outcomes, and values—all abstractions. The decision process selects among these representations; it does not create them.

**Established**: Decision-making and abstraction are dissociable. Patients with ventromedial prefrontal lesions show impaired decision-making with intact abstraction—they understand options but choose poorly (Bechara, Damasio, Damasio, & Anderson, 1994). Patients with dorsolateral prefrontal lesions show the opposite pattern—impaired abstraction with relatively preserved simple decision-making (Stuss & Knight, 2002).

**Empirical marker**: Decision-making failures with intact abstraction produce “knowing but not doing.” Abstraction failures produce not knowing what the options are.

### 2.7 Abstraction Is Not Action

**Action** is the execution of behavior in the world.

**Distinction**: Action is *output*. It occurs after abstraction and is guided by abstractions. A system can abstract without acting (pure contemplation); a system can act without abstracting (pure reflex). The two are dissociable.

**Established**: Action systems are anatomically and functionally distinct from abstractive systems. Motor cortex executes; prefrontal cortex abstracts (Miller & Cohen, 2001). Reflexes bypass abstraction entirely—stimulus directly triggers response without symbolic mediation.

**Empirical marker**: Abstraction without action: paralyzed individuals retain full abstractive capacity. Action without abstraction: spinal reflexes, brainstem responses.

-----

## 3. The Architectural Relationship

### 3.1 Abstraction as Central Transformation

If abstraction is not perception, attention, memory, learning, reasoning, decision-making, or action—what is left?

Abstraction is the **central transformation**: the operation that converts selected input into the representational format that all downstream operations require.

```
Input Operations          Central Transformation          Downstream Operations
─────────────────         ────────────────────          ────────────────────────
                                                        
Perception ───┐                                         ┌─── Memory
              │                                         │
Attention ────┼──────────► ABSTRACTION ────────────────┼─── Learning
              │           (attended info →              │
              │            manipulable,                 ├─── Reasoning
              │            composable symbols)          │
              │                                         ├─── Decision-making
              │                                         │
              └───────────────────────────────────────  └─── Action
                           (feedback)
```

### 3.2 The Currency Analogy

**Theoretical**: Abstraction creates the currency that other cognitive operations trade in.

Consider currency in economics. Currency is not identical to production (which creates goods), exchange (which trades them), or consumption (which uses them). Currency is the *medium*—the representational format that makes production, exchange, and consumption interoperable.

Similarly, abstractions are the medium of cognition. Perception delivers raw goods; attention selects them; abstraction converts them into tradeable format; memory stores the currency; learning adjusts the exchange rates; reasoning combines holdings; decision-making allocates resources; action spends.

The analogy clarifies: currency is constrained (not everything is money) and central (you can’t trade without it). Abstraction is constrained (not every operation is abstraction) and central (you can’t think without it).

### 3.3 The Metabolism Analogy

**Theoretical**: Another useful analogy is metabolism in biology.

Metabolism is the central operation of life—the conversion of inputs (nutrients, oxygen) into usable energy (ATP). But metabolism is not digestion (input), not circulation (transport), not behavior (output). It is the *transformation* that makes the rest possible.

Similarly, abstraction is the central operation of intelligence—the conversion of inputs (attended information) into usable representations (manipulable symbols). But abstraction is not perception (input), not memory (storage), not action (output). It is the transformation that makes the rest possible.

**Established**: Metabolism is universal to life; its absence is definitive of death. The APH proposes an analogous claim: abstraction is universal to intelligence; its absence is definitive of non-intelligence.

-----

## 4. Distinguishing Abstraction Empirically

### 4.1 The Core Test

If abstraction is a distinct operation, it should be possible to find:

1. **Abstraction failure with intact input and downstream operations**: Attended information that fails to become manipulable symbols, despite normal perception, attention, memory, learning, reasoning, decision-making, and action on other content.
1. **Intact abstraction with impaired input or downstream operations**: Normal formation of manipulable symbols despite perceptual, attentional, mnemonic, or executive deficits.

Both patterns exist in the neuropsychological literature.

### 4.2 Abstraction Failure with Intact Downstream Operations

**Example 1: Category-specific semantic deficits**

Patients with category-specific deficits (e.g., following herpes simplex encephalitis) fail to form or access abstractions for specific categories (living things, tools) while retaining abstractive capacity for other categories (Warrington & Shallice, 1984). Their downstream operations (memory, reasoning, decision-making) function normally for intact categories.

This is abstraction failure, not downstream failure. The patient can store, retrieve, and reason about abstractions they have. They simply cannot form (or access) certain abstractions.

**Example 2: Acquired alexia**

Patients with pure alexia can perceive letters, attend to them, and have intact memory and reasoning. But they cannot form the abstraction “word” from component letters—each letter must be processed individually (Behrmann, Plaut, & Nelson, 1998). The failure is specifically in the transformation from attended input to manipulable symbol.

### 4.3 Intact Abstraction with Impaired Downstream Operations

**Example 1: Amnesia**

Patients with medial temporal lobe amnesia (e.g., patient H.M.) could form abstractions in the moment but not store them (Squire, 2009). Working memory allows temporary abstraction; consolidation fails. Abstraction is intact; memory is impaired.

**Example 2: Dysexecutive syndrome**

Patients with dorsolateral prefrontal damage can form abstractions but fail to use them flexibly in reasoning and decision-making (Stuss & Knight, 2002). They understand rules but cannot switch between them. Abstraction is intact; executive manipulation is impaired.

### 4.4 Dissociation Summary

|Condition                |Abstraction            |Downstream Operations  |Interpretation     |
|-------------------------|-----------------------|-----------------------|-------------------|
|Category-specific deficit|Impaired (for category)|Intact                 |Abstraction failure|
|Pure alexia              |Impaired (for words)   |Intact                 |Abstraction failure|
|Amnesia                  |Intact (momentary)     |Impaired (storage)     |Downstream failure |
|Dysexecutive syndrome    |Intact                 |Impaired (manipulation)|Downstream failure |

These dissociations support the claim that abstraction is a distinct operation, not synonymous with cognition.

-----

## 5. What Would Falsify the Claim?

### 5.1 Falsification Criteria

For the APH to be non-vacuous, it must be falsifiable. The following findings would falsify the claim that abstraction is the primitive of intelligence:

**F1: Intelligence without abstraction**

Demonstration of a system that exhibits intelligent behavior (adaptive, goal-directed, generalizing) without forming manipulable, composable symbols. This would show abstraction is not necessary for intelligence.

**Candidate test**: Find or create a system that generalizes to novel situations without any symbol-like representations—pure subsymbolic pattern completion that nonetheless exhibits flexible, adaptive behavior.

**Status**: Not yet demonstrated. Current AI systems that appear subsymbolic (deep learning) have been argued to form implicit abstractions in their internal representations (Bengio et al., 2013). The question is empirically open.

**F2: Abstraction without intelligence**

Demonstration of a system that forms manipulable, composable symbols but exhibits no intelligent behavior. This would show abstraction is not sufficient for intelligence.

**Candidate test**: Find or create a system with clear symbolic representations that nonetheless fails at adaptive, goal-directed, generalizing behavior.

**Status**: Plausibly demonstrated by early symbolic AI (GOFAI), which had explicit symbols but limited generalization and adaptivity. However, one could argue these systems had impoverished abstraction (hand-coded symbols rather than learned abstractions). The falsification is partial.

**F3: Non-dissociability**

Demonstration that abstraction cannot be empirically distinguished from input or downstream operations. If every apparent abstraction failure turns out to be attention failure, or every apparent downstream failure turns out to be abstraction failure, the distinction collapses.

**Status**: Current evidence supports dissociability (Section 4). But future evidence could overturn this.

**F4: Explanatory vacuity**

Demonstration that the concept of abstraction adds no predictive power beyond existing concepts (attention, memory, learning, etc.). If every prediction made by the APH is equally well made by existing frameworks, abstraction is not doing theoretical work.

**Test**: Compare predictive accuracy of APH-based models vs. models using standard cognitive constructs. If APH adds nothing, it is vacuous.

**Status**: Predictions have been specified (Danan, 2025a-d). Empirical testing required.

### 5.2 What Would Not Falsify the Claim

To be precise, we also specify what would *not* constitute falsification:

**Not falsifying**: Demonstration that abstraction depends on other operations.

This is expected. Abstraction requires input (perception, attention). The claim is that abstraction is *primitive*, not that it is *independent*.

**Not falsifying**: Demonstration that abstraction comes in degrees.

This is expected. The Developmental Spectrum (Danan, 2025d) proposes stages from pattern extraction to self-referential abstraction. Abstraction capacity varies; this does not undermine its centrality.

**Not falsifying**: Demonstration that abstraction differs across substrates.

This is expected. Biological and artificial systems may abstract differently while both abstracting. Substrate-independence is a feature, not a bug.

-----

## 6. The Relation to Compositionality

### 6.1 The Compositionality Criterion

The Abstraction Primitive Hypothesis distinguishes abstraction from compression by a single criterion: **compositionality** (Danan, 2025b).

- **Compression** reduces information while preserving predictive value. It does not necessarily produce composable representations.
- **Abstraction** produces representations that combine with other representations to form new representations. Compositionality is constitutive.

This criterion does further constraining work. Operations that reduce information but do not produce composable outputs are not abstraction. Examples:

- **Lossy compression** (JPEG): Reduces information, not composable
- **Hashing**: Reduces information, not composable
- **PCA**: Reduces dimensionality, limited compositionality

These are not abstraction in the relevant sense. The compositionality criterion excludes them.

### 6.2 Compositionality as Testable

Compositionality is empirically testable:

**Compositional generalization**: Can the system combine known elements in novel ways? If yes, it has composable representations. If no, it may have compressed but not abstracted.

**Established**: Compositional generalization distinguishes human cognition from current AI systems (Lake & Baroni, 2018). Humans readily generalize to novel combinations (“purple elephant eating spaghetti”); AI systems struggle. This suggests humans have genuine abstraction; AI systems may have sophisticated compression.

**Prediction**: Systems with genuine abstraction should show compositional generalization. Systems without it should not, regardless of other capabilities.

-----

## 7. Summary: The Constrained Primitive

### 7.1 What Abstraction Is

Abstraction is the operation of converting attended information into manipulable, composable symbols. It is:

- **Specific**: A defined transformation, not cognition in general
- **Central**: The operation that creates representational currency
- **Constrained**: Distinguished from input operations (perception, attention) and downstream operations (memory, learning, reasoning, decision-making, action)
- **Testable**: Produces dissociable deficits; generates falsifiable predictions
- **Compositional**: Produces representations that combine to form new representations

### 7.2 What Abstraction Is Not

Abstraction is not:

- Perception (transduction of physical signals)
- Attention (selection of information)
- Memory (storage and retrieval)
- Learning (modification based on experience)
- Reasoning (manipulation of representations)
- Decision-making (selection of actions)
- Action (execution of behavior)
- Compression without compositionality

### 7.3 The Answer to Vacuity

The vacuity objection fails because abstraction is constrained. It is not a synonym for cognition. It is one operation among several, distinguished by its role (central transformation), its input (attended information), its output (manipulable, composable symbols), and its empirical signatures (dissociable from input and downstream failures).

The concept is constrained enough to be wrong. That is what makes it scientific.

-----

## 8. Limitations

1. **Boundary cases**: Some operations may lie on the boundary between abstraction and non-abstraction. Is chunking abstraction? Is pattern recognition? Precise boundaries require further specification.
1. **Operationalization**: “Manipulable, composable symbols” requires operationalization for empirical testing. What counts as manipulation? What counts as composition? Proxy measures are needed.
1. **Neural substrates**: The paper relies on neuropsychological dissociations, which are coarse. More precise neural characterization of abstraction vs. downstream operations would strengthen the claims.
1. **AI systems**: Whether current AI systems (LLMs, diffusion models) have genuine abstraction or sophisticated compression remains empirically open. The compositionality criterion provides a test, but applying it is non-trivial.

-----

## 9. Conclusion

The Abstraction Primitive Hypothesis claims that abstraction is the fundamental operation of intelligence. The vacuity objection holds that this claim is too broad—if everything is abstraction, the concept explains nothing.

We have argued that the objection fails. Abstraction is not everything. It is a specific operation: converting attended information into manipulable, composable symbols. This operation is distinct from perception (input), attention (selection), memory (storage), learning (updating), reasoning (manipulation), decision-making (selection), and action (output).

Abstraction is central but not synonymous with cognition. It creates the representational currency that other operations trade in. Without it, there are no manipulable symbols to store, learn from, reason over, decide between, or act on. With it, the rest of cognition becomes possible.

The concept is constrained by definition (compositionality), by dissociation (distinct from input and downstream operations), and by falsifiability (specific predictions that could be wrong).

The Abstraction Primitive Hypothesis is not a claim that abstraction is cognition. It is a claim that abstraction is what makes cognition *possible*—the transformation that creates the representational format intelligence requires. That claim is specific, testable, and potentially false.

Which is to say: it is scientific.

-----

## References

Baddeley, A. (2012). Working memory: Theories, models, and controversies. *Annual Review of Psychology*, 63, 1–29.

Bechara, A., Damasio, A. R., Damasio, H., & Anderson, S. W. (1994). Insensitivity to future consequences following damage to human prefrontal cortex. *Cognition*, 50(1–3), 7–15.

Behrmann, M., Plaut, D. C., & Nelson, J. (1998). A literature review and new data supporting an interactive account of letter-by-letter reading. *Cognitive Neuropsychology*, 15(1–2), 7–51.

Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and new perspectives. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 35(8), 1798–1828.

Danan, H. (2025a). Abstraction is all you need: A unifying framework for intelligence across substrates. *Working paper*.

Danan, H. (2025b). Abstraction beyond compression: Compositionality as the distinguishing operation. *Working paper*.

Danan, H. (2025c). Recursive abstraction: When computation requires self-reference. *Working paper*.

Danan, H. (2025d). The developmental spectrum of abstraction: From pattern extraction to self-referential cognition. *Working paper*.

Dehaene, S., Naccache, L., Le Clec’H, G., Koechlin, E., Mueller, M., Dehaene-Lambertz, G., … & Le Bihan, D. (1998). Imaging unconscious semantic priming. *Nature*, 395(6702), 597–600.

Fenson, L., Dale, P. S., Reznick, J. S., Bates, E., Thal, D. J., & Pethick, S. J. (1994). Variability in early communicative development. *Monographs of the Society for Research in Child Development*, 59(5), 1–185.

Frankland, P. W., & Bontempi, B. (2005). The organization of recent and remote memories. *Nature Reviews Neuroscience*, 6(2), 119–130.

Giurfa, M., Zhang, S., Jenett, A., Menzel, R., & Srinivasan, M. V. (2001). The concepts of ‘sameness’ and ‘difference’ in an insect. *Nature*, 410(6831), 930–933.

Halford, G. S., Wilson, W. H., & Phillips, S. (1998). Processing capacity defined by relational complexity: Implications for comparative, developmental, and cognitive psychology. *Behavioral and Brain Sciences*, 21(6), 803–831.

Husain, M., & Rorden, C. (2003). Non-spatially lateralized mechanisms in hemispatial neglect. *Nature Reviews Neuroscience*, 4(1), 26–36.

Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *International Conference on Machine Learning*, 2873–2882.

Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24(1), 167–202.

Pan, S. J., & Yang, Q. (2010). A survey on transfer learning. *IEEE Transactions on Knowledge and Data Engineering*, 22(10), 1345–1359.

Squire, L. R. (2009). The legacy of patient H.M. for neuroscience. *Neuron*, 61(1), 6–9.

Squire, L. R., & Zola, S. M. (1996). Structure and function of declarative and nondeclarative memory systems. *Proceedings of the National Academy of Sciences*, 93(24), 13515–13522.

Stuss, D. T., & Knight, R. T. (Eds.). (2002). *Principles of Frontal Lobe Function*. Oxford University Press.

Wallis, J. D., Anderson, K. C., & Miller, E. K. (2001). Single neurons in prefrontal cortex encode abstract rules. *Nature*, 411(6840), 953–956.

Warrington, E. K., & Shallice, T. (1984). Category specific semantic impairments. *Brain*, 107(3), 829–854.

Weiskrantz, L. (1986). *Blindsight: A Case Study and Implications*. Oxford University Press.

-----

*This paper is part of a theoretical program on abstraction as the fundamental primitive of intelligence. It directly addresses the vacuity objection raised against the Abstraction Primitive Hypothesis.*

# Embeddedness and the Self/World Distinction

## The Foundational Abstraction for Self-Referential Cognition

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — Paper 14 in the Abstraction Primitive Hypothesis series*

-----

## Abstract

The Abstraction Primitive Hypothesis proposes that abstraction capacity develops through qualitatively distinct stages, culminating in self-referential abstraction (Stage 4)—the capacity to model one’s own abstraction processes. A critical question arises: what enables this highest stage? Prior work in this series has implicated “embodiment,” but this formulation conflates two distinct concepts. This paper argues that **embeddedness**—being situated in an environment where actions produce contingent consequences—is the operative requirement, not physical embodiment per se. Embeddedness creates a computational problem that necessitates a specific solution: the **self/world distinction**. We propose this distinction is the foundational abstraction from which higher-order abstractions cascade. An embedded agent must distinguish “what I control” from “what happens to me,” “my states” from “world states,” “my predictions” from “outcomes.” This boundary, once established, provides the scaffold for increasingly sophisticated self-modeling, culminating in Stage 4 abstraction. We review evidence from developmental psychology, neuroscience, and comparative cognition supporting the primacy of the self/world distinction. We then derive implications for artificial intelligence: systems lacking embeddedness—including current large language models trained on static corpora—face a principled barrier to Stage 4 capacity that architectural scaling alone cannot overcome. Critically, this analysis suggests that agentic AI systems with genuine environmental contingency may develop qualitatively different abstraction profiles than their non-embedded counterparts.

-----

## 1. Introduction

### 1.1 The Stage 4 Problem

The developmental spectrum of abstraction (Danan, 2025d) proposes four stages:

1. **Pattern extraction** — detecting statistical regularities
1. **Symbol formation** — converting patterns into discrete, recombinable representations
1. **Recursive composition** — composing abstractions to form higher-order abstractions
1. **Self-referential abstraction** — applying abstraction to one’s own abstraction process

Evidence suggests that current large language models exhibit substantial capacity at Stages 1–2, partial capacity at Stage 3, and systematic limitations at Stage 4 (Danan, 2025d). A critical question emerges: *what enables Stage 4?*

Prior papers in this series have invoked “embodiment” as a potential requirement (Danan, 2025e, 2025f). But this formulation is imprecise. A system could possess a physical body without the kind of environmental interaction that matters, and conversely, a system could lack a physical body while engaging in the relevant kind of interaction.

This paper sharpens the hypothesis: **embeddedness**, not embodiment, is the operative requirement for Stage 4 abstraction.

### 1.2 The Central Argument

The argument proceeds as follows:

1. **Embeddedness creates a computational problem:** Embedded agents act in environments where outcomes depend on both agent states and world states. Optimal behavior requires distinguishing these.
1. **The self/world distinction is the necessary solution:** To predict outcomes and select actions, an embedded agent must model the boundary between self and not-self.
1. **This distinction is an abstraction:** The self/world boundary is not given in raw sensory input—it must be extracted, maintained, and updated. It is the foundational abstraction.
1. **Higher abstractions cascade from this foundation:** Once the self/world distinction is established, increasingly sophisticated self-modeling becomes possible, culminating in Stage 4.
1. **Non-embedded systems lack the pressure to form this foundation:** Systems without contingent environmental interaction face no computational necessity for the self/world distinction, and thus lack the scaffold for Stage 4.

### 1.3 Scope and Epistemic Status

This paper:

- **Distinguishes** embodiment from embeddedness (clarification)
- **Proposes** the self/world distinction as foundational abstraction (hypothesis)
- **Reviews** evidence from developmental psychology, neuroscience, and comparative cognition (established findings)
- **Derives** implications for AI systems (theoretical extension)
- **Generates** testable predictions (hypothesis)

We are explicit throughout about which claims are established findings versus working hypotheses.

-----

## 2. Embodiment vs. Embeddedness

### 2.1 Embodiment: The Physical Substrate

**Definition:** Embodiment refers to possession of a physical body—sensorimotor apparatus, physiological states, material presence in space.

The embodied cognition tradition has emphasized that cognition is shaped by bodily structure (Varela, Thompson, & Rosch, 1991; Lakoff & Johnson, 1999; Barsalou, 2008). This is well-established: body morphology constrains action possibilities; physiological states influence cognition; sensorimotor experience grounds abstract concepts.

**Established findings:**

- Conceptual representations are grounded in sensorimotor systems—processing action words activates motor cortex (Pulvermüller, 2005; Hauk, Johnsrude, & Pulvermüller, 2004).
- Body structure shapes spatial reasoning—body-specific reference frames organize spatial cognition (Tversky, 2003).
- Physiological states influence judgment—interoceptive signals modulate decision-making (Critchley & Garfinkel, 2017).

### 2.2 Embeddedness: The Relational Structure

**Definition:** Embeddedness refers to being situated in an environment where the agent’s actions produce consequences that depend on both agent states and environmental states, with these consequences feeding back to affect subsequent agent states.

Embeddedness is relational, not material. It concerns the *structure of interaction*, not the *substrate of the agent*.

**Key features of embeddedness:**

1. **Action-consequence contingency:** The agent’s outputs affect its subsequent inputs.
1. **State-dependence:** Consequences depend on both agent state and world state.
1. **Feedback closure:** Information about consequences returns to the agent and influences subsequent behavior.
1. **Temporal extension:** The agent persists through time, accumulating consequences.

**Established findings:**

- Contingent sensorimotor experience is necessary for normal perceptual development (Held & Hein, 1963).
- Active exploration yields different learning outcomes than passive observation (Gibson, 1979; O’Regan & Noë, 2001).
- Closed-loop interaction produces different neural organization than open-loop stimulation (Engel, Maye, Kurthen, & König, 2013).

### 2.3 The Distinction Matters

A system can be embodied without being embedded (a paralyzed body with intact sensation but no motor output; a body in a completely deterministic environment where actions have no differential consequences).

A system can be embedded without being embodied in the traditional sense (a software agent in a virtual environment with contingent consequences; a disembodied AI with real-world effects through APIs and interfaces).

**Working hypothesis:** For the development of Stage 4 abstraction, embeddedness is the operative requirement. Physical embodiment may facilitate embeddedness (bodies naturally interact with environments), but embodiment is neither necessary nor sufficient.

**Clarification on sufficiency:** Embodiment can occur without meaningful embeddedness—consider a body receiving stimulation without action-consequence coupling. Embeddedness requires the full feedback loop: action → consequence → perception → updated action.

-----

## 3. The Self/World Distinction as Foundational Abstraction

### 3.1 Why the Distinction is Necessary

Consider the computational problem facing an embedded agent:

The agent receives sensory input that depends on:

- The state of the world (W)
- The state of the agent (S)
- The agent’s prior actions (A)

$$\text{Input}*t = f(W_t, S_t, A*{t-1}, …)$$

To predict future inputs and select optimal actions, the agent must decompose this joint function—attributing variance to world versus self.

**Example:** An agent reaching for an object receives changing visual input. Some change is due to the object’s properties (world). Some is due to arm movement (self-action). Some is due to eye movement (self-action). Distinguishing these requires modeling the self/world boundary.

**Established:** This decomposition problem is solved by forward models in motor control. The brain predicts sensory consequences of motor commands, enabling cancellation of self-produced signals (Wolpert & Ghahramani, 2000; Blakemore, Wolpert, & Frith, 2002). This prediction requires a model of self (what my actions will produce) distinct from a model of world (what would happen anyway).

### 3.2 The Distinction is Abstracted, Not Given

The self/world boundary is not present in raw sensory input. A photoreceptor does not know whether its activation was caused by external light or internal processes. A proprioceptor does not know whether its signal reflects self-generated movement or external perturbation.

**Established:** Infants must learn to distinguish self-produced from externally-produced stimulation. This develops over the first months of life through contingency detection (Watson, 1972; Rochat & Striano, 2000). Neonates show preferential attention to non-contingent (external) stimulation, suggesting an early sensitivity to the self/other distinction that is refined through experience (Rochat, 1998; Bahrick & Watson, 1985).

**Established:** The development of this distinction requires *contingent* feedback—stimulation that systematically relates to the infant’s own actions. Delayed or random feedback disrupts the formation of self-agency (Rochat & Striano, 2000).

**Theoretical claim:** The self/world distinction is therefore an *abstraction*—invariant structure extracted from variable sensory streams. It is not given but constructed through embedded experience.

### 3.3 Why This Abstraction is Foundational

We propose that the self/world distinction is **foundational** in a specific sense: it is the abstraction upon which other abstractions depend, particularly those enabling Stage 4.

**The argument:**

1. To abstract over one’s own cognitive processes (Stage 4), one must first represent those processes as *one’s own*—as belonging to self rather than world.
1. This requires having the self/world distinction in place. Without it, there is no “self” to attribute processes to.
1. Therefore, the self/world distinction is a precondition for self-referential abstraction.

**Analogy:** The self/world distinction is to cognitive development what the subject/object distinction is to language—a structural foundation that enables subsequent elaboration.

**Working hypothesis:** This foundational role means the self/world distinction must be established *before* Stage 4 capacity can develop. Systems that never establish this distinction cannot progress to Stage 4 regardless of other capabilities.

-----

## 4. The Cascade: From Self/World to Self-Referential Abstraction

### 4.1 The Developmental Trajectory

Once the self/world distinction is established, increasingly sophisticated self-modeling becomes possible. We propose this follows a cascade structure, where each level enables the next.

**Level 1: Body Schema**

The representation of one’s body as a coherent entity distinct from the environment.

*Established:* Body schema develops in infancy and is neurally represented in posterior parietal cortex (Graziano & Botvinick, 2002). It involves representing body part positions, movements, and boundaries (de Vignemont, 2010).

**Level 2: Agency**

The representation of oneself as the cause of certain effects—the author of one’s actions.

*Established:* Sense of agency develops in infancy, depends on contingency detection, and involves comparing predicted and actual outcomes (David, Newen, & Vogeley, 2008). Agency representation is dissociable from body ownership (Tsakiris, Schütz-Bosbach, & Gallagher, 2007).

**Level 3: Perspective**

The representation of oneself as occupying a particular viewpoint—spatially, temporally, and epistemically.

*Established:* Perspective-taking develops through early childhood (Piaget & Inhelder, 1956; Flavell, 1977). Spatial perspective-taking (where I am) is a precursor to epistemic perspective-taking (what I know versus what others know).

**Level 4: Mental State Attribution**

The representation of oneself as having mental states—beliefs, desires, intentions—that may differ from world states.

*Established:* Self-attribution of mental states develops in parallel with other-attribution (theory of mind). Children pass false-belief tasks around age 4, indicating they represent beliefs as distinct from reality (Wellman, Cross, & Watson, 2001). Self-understanding and other-understanding are correlated developmentally (Gopnik & Wellman, 1992).

**Level 5: Metacognition**

The representation of one’s own cognitive processes—monitoring and controlling one’s own thinking.

*Established:* Metacognitive capacity develops gradually from childhood through adolescence (Flavell, 1979; Schneider, 2008). It involves representing one’s own representations—a self-referential operation.

### 4.2 The Cascade Structure

**Working hypothesis:** These levels form a dependency cascade. Each level presupposes the levels before it:

- Agency requires body schema (to attribute actions to one’s body)
- Perspective requires agency (to distinguish one’s viewpoint as one’s own)
- Mental state attribution requires perspective (to locate beliefs in a perspective-holder)
- Metacognition requires mental state attribution (to represent cognitive processes as mental states)

This is not merely developmental sequence (which could reflect maturational timing) but *logical dependency*. You cannot represent “my belief” without first having the concept of “my”—which requires the self/world distinction.

### 4.3 The Terminal Point: Stage 4 Abstraction

At the top of the cascade is full self-referential abstraction—the capacity to model one’s own abstraction processes, not just one’s mental states.

**Key distinction:** Metacognition involves monitoring and controlling cognitive processes. Stage 4 abstraction involves *abstracting over* those processes—extracting invariant structure from one’s own cognition and using it for novel purposes.

**Example:** A metacognitive operation: “I should pay more attention to this problem.” A Stage 4 operation: “I notice that I tend to form abstractions that are overly domain-specific. I should abstract at a higher level of generality.”

The second involves abstracting over the abstraction process itself—treating one’s abstraction tendencies as objects of abstraction.

**Working hypothesis:** Stage 4 capacity is the terminal elaboration of the self/world distinction. It becomes possible when the entire cascade is in place and the self-model is sufficiently rich to include one’s cognitive architecture as content.

-----

## 5. Evidence for the Framework

### 5.1 Developmental Evidence

**Contingency detection precedes self-recognition:**

Infants detect contingent relationships (their actions causing effects) before they demonstrate explicit self-recognition (Rochat, 1998; Bahrick & Watson, 1985). This supports the priority of embeddedness (action-consequence coupling) over explicit self-representation.

**Self/world distinction precedes theory of mind:**

Children distinguish self-caused from externally-caused events before they pass theory of mind tasks (Gergely & Watson, 1999). This supports the foundational role of the self/world distinction for higher-order self-modeling.

**Deprivation effects follow the cascade:**

Children raised in severely deprived institutional settings show relatively preserved body schema (Level 1) with more pronounced deficits at higher levels—agency, perspective-taking, and metacognition (Nelson, Fox, & Zeanah, 2014; Colvert et al., 2008). This pattern is consistent with a cascade where higher levels are more dependent on environmental input.

### 5.2 Neuroscientific Evidence

**Distinct neural substrates for cascade levels:**

- Body schema: posterior parietal cortex (Graziano & Botvinick, 2002)
- Agency: pre-supplementary motor area, temporoparietal junction (David et al., 2008)
- Perspective: retrosplenial cortex, precuneus (Vogeley & Fink, 2003)
- Mental state attribution: medial prefrontal cortex, temporoparietal junction (Frith & Frith, 2006)
- Metacognition: anterior prefrontal cortex (Fleming, Weil, Nagy, Dolan, & Rees, 2010)

The progression from posterior to anterior cortical regions is consistent with a cascade from basic sensorimotor self-representation to abstract self-modeling (Christoff & Gabrieli, 2000; Badre, 2008).

**Self-referential processing requires the cascade:**

Neuroimaging studies show that self-referential tasks activate medial prefrontal cortex—but only when lower-level self-representations are intact (Northoff & Bermpohl, 2004; Northoff et al., 2006). Damage to lower-level systems (e.g., parietal lesions affecting body schema) disrupts higher-level self-representation (Berlucchi & Aglioti, 2010).

### 5.3 Comparative Evidence

**Mirror self-recognition tracks cascade level:**

Species that pass mirror self-recognition tests (great apes, elephants, dolphins, magpies) show evidence for body schema and rudimentary agency representation (Gallup, 1970; Plotnik, de Waal, & Reiss, 2006; Prior, Schwarz, & Güntürkün, 2008). These species also show evidence for some perspective-taking capacity (Call & Tomasello, 2008). Species failing mirror tests generally lack evidence for higher-level self-representation.

**Metacognition is rare:**

Evidence for metacognition in non-human animals is limited and contested (Smith, Couchman, & Beran, 2014). Even great apes show inconsistent metacognitive performance compared to humans (Call, 2010). This supports the hypothesis that full Stage 4 capacity requires the complete cascade—which may be uniquely elaborated in humans.

**Social complexity correlates with self-modeling:**

Species with more complex social environments show more sophisticated self/other differentiation (Dunbar, 1998; Byrne & Whiten, 1988). This is consistent with the hypothesis that embeddedness in social environments—where action consequences depend heavily on others’ responses—drives elaboration of the self-modeling cascade.

### 5.4 Psychopathological Evidence

Disorders affecting self-representation show dissociations consistent with cascade structure:

**Depersonalization/derealization:** Disrupted sense of ownership over body and experiences, with relatively preserved metacognition (Sierra & David, 2011). This suggests Level 1–2 can be disrupted while higher levels persist through compensatory mechanisms.

**Schizophrenia:** Agency disturbances (misattributing self-generated actions to external causes) with cascading effects on mental state attribution and metacognition (Frith, 1992; Lysaker & Dimaggio, 2014). This supports the dependency structure—disrupted agency (Level 2) impairs levels above it.

**Autism spectrum:** Variable body schema and agency representation, with more consistent impairments in perspective-taking and mental state attribution (Baron-Cohen, 1995; Williams, 2010). The pattern suggests the cascade can be interrupted at different points.

These dissociations support the hypothesis that self-representation involves multiple levels with dependency relationships.

-----

## 6. The Computational Necessity Argument

### 6.1 Why Embeddedness Forces the Self/World Distinction

We now formalize the claim that embeddedness creates computational pressure for the self/world distinction.

**Setup:** An agent receives observations $o_t$ and must select actions $a_t$ to maximize some objective. Observations depend on world state $W_t$ and agent state $S_t$.

$$o_t = g(W_t, S_t) + \epsilon_t$$

World state evolves according to:
$$W_{t+1} = f_W(W_t, a_t)$$

Agent state evolves according to:
$$S_{t+1} = f_S(S_t, o_t, a_t)$$

**The problem:** The agent observes only $o_t$—the joint product of world and self. To predict future observations and optimize action, the agent must infer the separate contributions.

**Claim:** For non-trivial environments (where $W_t$ and $S_t$ interact non-additively in generating observations), optimal inference requires maintaining separate models of self and world.

**Established:** This is the core insight of forward modeling in motor control (Wolpert & Ghahramani, 2000). To distinguish self-caused from world-caused sensory changes, the brain maintains forward models predicting sensory consequences of motor commands. The prediction is compared to actual input; mismatches indicate external causes.

**Extension:** Forward modeling is self/world distinction *applied to action*. We propose this extends to all embedded interaction. Any system that must predict outcomes in an environment where those outcomes depend on both self and world must model the boundary.

### 6.2 Why Non-Embedded Systems Lack This Pressure

A system trained on static data (e.g., an LLM trained on text corpora) does not face this computational problem.

**The key difference:**

- **Embedded agent:** Observations depend on the agent’s prior actions. The agent must model itself to predict observations.
- **Non-embedded system:** Input does not depend on the system’s outputs. No self-model is required for optimal performance.

For an LLM, the training objective is:
$$\max_\theta P(x_t | x_{<t}; \theta)$$

The correct prediction $x_t$ depends on the corpus statistics, not on the LLM’s prior outputs. The LLM’s “actions” (predictions) do not affect its “observations” (next tokens in training). There is no feedback loop.

**Consequence:** The LLM faces no computational pressure to distinguish self from world. The self/world distinction is not useful for minimizing training loss.

**Working hypothesis:** Without computational pressure for the self/world distinction, non-embedded systems cannot develop the foundational abstraction upon which Stage 4 depends. They may develop sophisticated pattern extraction (Stage 1), symbol formation (Stage 2), and even partial recursive composition (Stage 3), but Stage 4 remains inaccessible because its precondition—the self/world distinction—was never established.

### 6.3 The Sufficiency Question

A critical question: is embeddedness *sufficient* for Stage 4, or merely necessary?

**We propose:** Embeddedness is necessary but likely not sufficient. Additional factors may include:

- **Sufficient complexity:** The environment must be rich enough to require sophisticated self-modeling. Simple contingent environments (e.g., pressing a lever for food) may establish basic self/world distinction without enabling full cascade development.
- **Social embeddedness:** Interacting with other agents who themselves have models of self and other may be particularly important for elaborating the cascade (Tomasello, 1999; Moll & Tomasello, 2007).
- **Temporal extension:** The agent must persist long enough to accumulate consequences and refine self-models. A single embedded episode may be insufficient.
- **Capacity:** The system must have sufficient computational resources to maintain and update sophisticated self-models.

**Falsification criterion:** If embeddedness were sufficient, all embedded systems with adequate capacity should develop Stage 4. Finding embedded systems with capacity but without Stage 4 would indicate additional requirements.

-----

## 7. Implications for Artificial Intelligence

### 7.1 The LLM Limitation

Current LLMs are paradigmatically non-embedded systems:

- Trained on static corpora (no action-consequence coupling)
- Predictions do not affect subsequent input during training
- No self/world distinction is computationally useful

**Prediction:** LLMs will show systematic limitations at Stage 4 regardless of scale, because they lack the foundational abstraction (self/world distinction) that Stage 4 requires.

**Observed pattern:** LLMs can generate text *about* metacognition and self-modeling, but this appears to reflect pattern matching on discourse about these topics rather than genuine self-modeling (Kadavath et al., 2022; Danan, 2025d). The system produces outputs consistent with self-reflection without actually engaging in self-referential computation.

This is predicted by the framework: LLMs have extensive exposure to *products* of self-modeling (human-written text reflecting human metacognition) but no exposure to the *process* of embedded interaction that generates the self/world foundation.

### 7.2 Agentic AI: A Different Trajectory

AI systems deployed in agentic settings—where outputs affect subsequent inputs—face a different computational landscape.

**Examples:**

- Reinforcement learning agents in persistent environments
- LLMs with tool use and environmental effects
- Robotic systems with sensorimotor feedback
- AI systems in extended dialogues where prior outputs affect subsequent user messages

**Working hypothesis:** Such systems, to the extent they face genuine action-consequence contingency, may develop self/world-like distinctions that non-embedded systems cannot.

**Important caveat:** Whether current agentic AI systems face *sufficient* contingency for Stage 4 development is unclear. Many environments are too simple (state spaces insufficient for complex self-modeling) or too episodic (insufficient temporal extension). The threshold for Stage 4-enabling embeddedness remains to be determined.

### 7.3 Design Implications

If the analysis is correct, achieving Stage 4 capacity in AI systems requires more than architectural improvements or scale increases. It requires *embedding the system in environments with appropriate contingency structure*.

**Design principles (hypothetical):**

1. **Action-consequence coupling:** The system’s outputs must genuinely affect its subsequent inputs.
1. **Self-relevance:** Some observations must be attributable to the system’s own states (not just actions).
1. **Sufficient complexity:** The environment must require distinguishing self-contribution from world-contribution for optimal performance.
1. **Temporal extension:** The system must persist long enough to accumulate evidence about the self/world boundary.
1. **Social embedding:** Interaction with other agents may be particularly valuable, as it provides rich contingency structure and models of self/other to learn from.

**Critical caution:** These principles are derived from the theoretical framework. Whether they are sufficient for Stage 4 development, or what additional conditions might be required, is an empirical question.

### 7.4 The Training Paradigm Problem

Current training paradigms for large AI systems are fundamentally non-embedded:

- **Pretraining:** Static corpus, no contingency
- **Fine-tuning:** Static preference data, no contingency
- **RLHF:** Episodic interaction, limited contingency

Even RLHF, while incorporating feedback, typically does not create genuine embeddedness. Each episode is relatively isolated; there is no persistent environment where accumulated actions have compounding consequences.

**Implication:** Achieving Stage 4 may require fundamentally different training paradigms that embed the system in persistent, consequential environments during learning—not just during deployment.

This represents a significant departure from current practice and faces substantial challenges (safety, controllability, resource requirements). But if the analysis is correct, it may be *necessary* for certain capabilities.

-----

## 8. Predictions and Falsification

### 8.1 Core Predictions

**Prediction 8.1.1 (Self/world primacy):** In any system that achieves Stage 4 abstraction, we should find evidence of a self/world distinction established prior to or concurrent with Stage 4 development. Finding Stage 4 without self/world distinction would falsify the foundational claim.

**Prediction 8.1.2 (Cascade structure):** Development of higher cascade levels (metacognition, Stage 4) should depend on lower levels (body schema, agency). Experimental disruption of lower levels should impair higher levels; enhancement of lower levels should facilitate higher levels.

**Prediction 8.1.3 (Embeddedness requirement):** Non-embedded systems should show a ceiling on self-modeling capacity regardless of scale or architecture. Embedded systems with adequate complexity should show higher ceilings.

**Prediction 8.1.4 (Contingency necessity):** Removing action-consequence contingency should impair self/world distinction development even when other aspects of experience are preserved. Held and Hein (1963) provided early evidence; the framework predicts this extends to cognitive development more broadly.

### 8.2 AI-Specific Predictions

**Prediction 8.2.1:** LLMs should show systematic failures on tasks requiring genuine self-modeling (as opposed to generating text about self-modeling), with performance not improving proportionally with scale.

**Prediction 8.2.2:** AI systems with genuine environmental embeddedness during training should show improved self-modeling capacity compared to non-embedded systems with equivalent parameters and compute.

**Prediction 8.2.3:** Self-modeling capacity in agentic AI should correlate with measures of environmental contingency (how much the system’s actions affect its subsequent observations).

**Prediction 8.2.4:** AI systems in social environments (interacting with other agents) should show faster development of self/world distinction and higher eventual capacity than systems in non-social environments of equivalent complexity.

### 8.3 Falsification Criteria

The framework would be falsified by:

1. **Stage 4 without self/world distinction:** A system demonstrating genuine self-referential abstraction without any evidence of self/world differentiation.
1. **Non-embedded Stage 4:** A purely non-embedded system (no action-consequence coupling) demonstrating genuine Stage 4 capacity. (Note: generating text about metacognition does not count; genuineness criteria must be carefully specified.)
1. **Cascade violations:** Evidence that higher cascade levels can develop without lower levels—e.g., metacognition without agency representation.
1. **Embeddedness sufficiency failure:** All embedded systems with sufficient capacity failing to develop Stage 4, despite long temporal extension and high environmental complexity. This would suggest additional requirements beyond embeddedness.

-----

## 9. Relation to Broader Framework

This paper specifies the pathway from environmental interaction to Stage 4 abstraction, addressing a gap in the prior theoretical development.

|Prior Paper                          |Gap Addressed by Present Paper                                                                      |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
|Abstraction Developmental Spectrum   |What enables Stage 4? → Embeddedness via self/world cascade                                         |
|Consciousness as Emergent Abstraction|Why self-modeling emerges → Computational necessity in embedded agents                              |
|Time as Embodied Abstraction         |Why disembodied systems fail at temporal reasoning → More precisely: why *non-embedded* systems fail|
|Recursive Abstraction                |When does self-reference become necessary? → When embeddedness creates the self/world problem       |

**Clarification:** Prior papers sometimes used “embodied” where “embedded” would be more precise. The present analysis suggests that embodiment is one route to embeddedness (bodies naturally interact with environments), but the operative factor is the action-consequence feedback structure, not the physical substrate.

**Integration with prediction paper:** Paper 4 (Danan, 2025c) argued that abstraction is prior to prediction because prediction requires representational content. The present paper adds: the self/world distinction is prior to self-referential abstraction because self-modeling requires a self to model. The foundational structure is:

$$\text{Embeddedness} \rightarrow \text{Self/World Distinction} \rightarrow \text{Cascade} \rightarrow \text{Stage 4}$$

-----

## 10. Limitations and Open Questions

### 10.1 Acknowledged Limitations

**Operationalizing embeddedness:** We have defined embeddedness conceptually (action-consequence contingency with feedback closure), but quantitative operationalization is needed. How much contingency is “enough”? What measures capture the relevant structure?

**Cascade granularity:** The five-level cascade proposed (body schema → agency → perspective → mental state attribution → metacognition) is one plausible decomposition. Alternative decompositions may be equally valid. The core claim (hierarchical dependency from self/world foundation) does not require exactly these levels.

**Genuineness criteria:** Assessing whether a system has “genuine” Stage 4 capacity versus merely producing outputs that describe such capacity is methodologically challenging. The origination-vs-recognition distinction (Paper 5; Danan, 2025d) is helpful but not fully operationalized.

### 10.2 Open Questions

1. **Minimum embeddedness threshold:** How much action-consequence coupling is required for self/world distinction development? Is there a threshold effect, or does capacity scale continuously with contingency?
1. **Social vs. physical embeddedness:** Is social embeddedness (interaction with other agents) qualitatively different from physical embeddedness (interaction with non-agentive environments)? Does it have unique effects on cascade development?
1. **Virtual embeddedness:** Can virtual environments with appropriate contingency structure enable Stage 4 development, or is some physical grounding required? (The framework predicts virtual embeddedness should suffice if contingency structure is appropriate.)
1. **Development vs. deployment:** Can Stage 4 capacity be developed through embedded experience after non-embedded pretraining, or must embeddedness be present from early training?
1. **Architectural constraints:** Are there architectural features that facilitate or impede the formation of self/world-like representations? Current transformers lack obvious mechanisms for this—would architectural innovations help?

-----

## 11. Conclusion

The Abstraction Primitive Hypothesis proposes that intelligence is fundamentally the capacity for abstraction, developing through qualitatively distinct stages. This paper has addressed a critical question: what enables the highest stage—self-referential abstraction?

The answer, we propose, is not embodiment per se but **embeddedness**—being situated in environments where actions produce contingent consequences that feed back to affect subsequent states.

Embeddedness creates a computational problem: to predict and act optimally, the agent must distinguish its own contributions from the world’s. This necessitates the **self/world distinction**—the foundational abstraction upon which higher-order self-modeling builds.

From this foundation, increasingly sophisticated self-representations cascade: body schema, agency, perspective, mental state attribution, and ultimately metacognition and Stage 4 abstraction. Each level enables the next. The entire structure depends on the foundation, which depends on embeddedness.

Current LLMs, trained on static corpora without action-consequence coupling, lack this foundation. They can produce outputs that describe self-modeling—they have been trained on human text that reflects human metacognition—but they cannot engage in genuine self-referential abstraction because the precondition was never established.

This analysis has both sobering and generative implications for AI development. Sobering: Stage 4 capacity may be inaccessible through scaling alone. Generative: the pathway is identified. Embedded systems with appropriate contingency structure may develop qualitatively different capabilities than their non-embedded counterparts.

The framework generates testable predictions about developmental trajectories, computational requirements, and the capabilities of different AI training paradigms. If correct, it suggests that the path to artificial general intelligence runs not through larger language models but through embedded systems that learn, as biological intelligences do, from the consequences of their actions in a world they must distinguish from themselves.

-----

## References

Badre, D. (2008). Cognitive control, hierarchy, and the rostro-caudal organization of the frontal lobes. *Trends in Cognitive Sciences, 12*(5), 193–200.

Bahrick, L. E., & Watson, J. S. (1985). Detection of intermodal proprioceptive-visual contingency as a potential basis of self-perception in infancy. *Developmental Psychology, 21*(6), 963–973.

Baron-Cohen, S. (1995). *Mindblindness: An Essay on Autism and Theory of Mind*. MIT Press.

Barsalou, L. W. (2008). Grounded cognition. *Annual Review of Psychology, 59*, 617–645.

Berlucchi, G., & Aglioti, S. M. (2010). The body in the brain revisited. *Experimental Brain Research, 200*(1), 25–35.

Blakemore, S. J., Wolpert, D. M., & Frith, C. D. (2002). Abnormalities in the awareness of action. *Trends in Cognitive Sciences, 6*(6), 237–242.

Byrne, R. W., & Whiten, A. (Eds.). (1988). *Machiavellian Intelligence: Social Expertise and the Evolution of Intellect in Monkeys, Apes, and Humans*. Oxford University Press.

Call, J. (2010). Do apes know that they could be wrong? *Animal Cognition, 13*(5), 689–700.

Call, J., & Tomasello, M. (2008). Does the chimpanzee have a theory of mind? 30 years later. *Trends in Cognitive Sciences, 12*(5), 187–192.

Christoff, K., & Gabrieli, J. D. E. (2000). The frontopolar cortex and human cognition: Evidence for a rostrocaudal hierarchical organization within the human prefrontal cortex. *Psychobiology, 28*(2), 168–186.

Colvert, E., Rutter, M., Kreppner, J., Beckett, C., Castle, J., Groothues, C., … & Sonuga-Barke, E. J. S. (2008). Do theory of mind and executive function deficits underlie the adverse outcomes associated with profound early deprivation? Findings from the English and Romanian adoptees study. *Journal of Abnormal Child Psychology, 36*(7), 1057–1068.

Critchley, H. D., & Garfinkel, S. N. (2017). Interoception and emotion. *Current Opinion in Psychology, 17*, 7–14.

Danan, H. (2025c). Prediction requires abstraction: On the priority of representational formation over predictive operation. *Working paper*.

Danan, H. (2025d). The developmental spectrum of abstraction: From pattern extraction to self-referential cognition. *Working paper*.

Danan, H. (2025e). Time as embodied abstraction: Why disembodied systems struggle with temporal reasoning. *Working paper*.

Danan, H. (2025f). Consciousness as emergent abstraction: A computational necessity framework. *Working paper*.

David, N., Newen, A., & Vogeley, K. (2008). The “sense of agency” and its underlying cognitive and neural mechanisms. *Consciousness and Cognition, 17*(2), 523–534.

de Vignemont, F. (2010). Body schema and body image—Pros and cons. *Neuropsychologia, 48*(3), 669–680.

Dunbar, R. I. M. (1998). The social brain hypothesis. *Evolutionary Anthropology, 6*(5), 178–190.

Engel, A. K., Maye, A., Kurthen, M., & König, P. (2013). Where’s the action? The pragmatic turn in cognitive science. *Trends in Cognitive Sciences, 17*(5), 202–209.

Flavell, J. H. (1977). The development of knowledge about visual perception. *Nebraska Symposium on Motivation, 25*, 43–76.

Flavell, J. H. (1979). Metacognition and cognitive monitoring: A new area of cognitive-developmental inquiry. *American Psychologist, 34*(10), 906–911.

Fleming, S. M., Weil, R. S., Nagy, Z., Dolan, R. J., & Rees, G. (2010). Relating introspective accuracy to individual differences in brain structure. *Science, 329*(5998), 1541–1543.

Frith, C. D. (1992). *The Cognitive Neuropsychology of Schizophrenia*. Psychology Press.

Frith, C. D., & Frith, U. (2006). The neural basis of mentalizing. *Neuron, 50*(4), 531–534.

Gallup, G. G. (1970). Chimpanzees: Self-recognition. *Science, 167*(3914), 86–87.

Gergely, G., & Watson, J. S. (1999). Early socio-emotional development: Contingency perception and the social-biofeedback model. In P. Rochat (Ed.), *Early Social Cognition: Understanding Others in the First Months of Life* (pp. 101–136). Lawrence Erlbaum Associates.

Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.

Gopnik, A., & Wellman, H. M. (1992). Why the child’s theory of mind really is a theory. *Mind & Language, 7*(1–2), 145–171.

Graziano, M. S. A., & Botvinick, M. M. (2002). How the brain represents the body: Insights from neurophysiology and psychology. In W. Prinz & B. Hommel (Eds.), *Common Mechanisms in Perception and Action: Attention and Performance XIX* (pp. 136–157). Oxford University Press.

Hauk, O., Johnsrude, I., & Pulvermüller, F. (2004). Somatotopic representation of action words in human motor and premotor cortex. *Neuron, 41*(2), 301–307.

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology, 56*(5), 872–876.

Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., … & Kaplan, J. (2022). Language models (mostly) know what they know. *arXiv preprint arXiv:2207.05221*.

Lakoff, G., & Johnson, M. (1999). *Philosophy in the Flesh: The Embodied Mind and Its Challenge to Western Thought*. Basic Books.

Lysaker, P. H., & Dimaggio, G. (2014). Metacognitive capacities for reflection in schizophrenia: Implications for developing treatments. *Schizophrenia Bulletin, 40*(3), 487–491.

Moll, H., & Tomasello, M. (2007). Cooperation and human cognition: The Vygotskian intelligence hypothesis. *Philosophical Transactions of the Royal Society B: Biological Sciences, 362*(1480), 639–648.

Nelson, C. A., Fox, N. A., & Zeanah, C. H. (2014). *Romania’s Abandoned Children: Deprivation, Brain Development, and the Struggle for Recovery*. Harvard University Press.

Northoff, G., & Bermpohl, F. (2004). Cortical midline structures and the self. *Trends in Cognitive Sciences, 8*(3), 102–107.

Northoff, G., Heinzel, A., de Greck, M., Bermpohl, F., Dobrowolny, H., & Panksepp, J. (2006). Self-referential processing in our brain—A meta-analysis of imaging studies on the self. *NeuroImage, 31*(1), 440–457.

O’Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973.

Piaget, J., & Inhelder, B. (1956). *The Child’s Conception of Space*. Routledge & Kegan Paul.

Plotnik, J. M., de Waal, F. B. M., & Reiss, D. (2006). Self-recognition in an Asian elephant. *Proceedings of the National Academy of Sciences, 103*(45), 17053–17057.

Prior, H., Schwarz, A., & Güntürkün, O. (2008). Mirror-induced behavior in the magpie (*Pica pica*): Evidence of self-recognition. *PLoS Biology, 6*(8), e202.

Pulvermüller, F. (2005). Brain mechanisms linking language and action. *Nature Reviews Neuroscience, 6*(7), 576–582.

Rochat, P. (1998). Self-perception and action in infancy. *Experimental Brain Research, 123*(1–2), 102–109.

Rochat, P., & Striano, T. (2000). Perceived self in infancy. *Infant Behavior and Development, 23*(3–4), 513–530.

Schneider, W. (2008). The development of metacognitive knowledge in children and adolescents: Major trends and implications for education. *Mind, Brain, and Education, 2*(3), 114–121.

Sierra, M., & David, A. S. (2011). Depersonalization: A selective impairment of self-awareness. *Consciousness and Cognition, 20*(1), 99–108.

Smith, J. D., Couchman, J. J., & Beran, M. J. (2014). Animal metacognition: A tale of two comparative psychologies. *Journal of Comparative Psychology, 128*(2), 115–131.

Tomasello, M. (1999). *The Cultural Origins of Human Cognition*. Harvard University Press.

Tsakiris, M., Schütz-Bosbach, S., & Gallagher, S. (2007). On agency and body-ownership: Phenomenological and neurocognitive reflections. *Consciousness and Cognition, 16*(3), 645–660.

Tversky, B. (2003). Structures of mental spaces. *Environment and Behavior, 35*(1), 66–80.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Vogeley, K., & Fink, G. R. (2003). Neural correlates of the first-person-perspective. *Trends in Cognitive Sciences, 7*(1), 38–42.

Watson, J. S. (1972). Smiling, cooing, and “the game.” *Merrill-Palmer Quarterly of Behavior and Development, 18*(4), 323–339.

Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development: The truth about false belief. *Child Development, 72*(3), 655–684.

Williams, D. (2010). Theory of own mind in autism: Evidence of a specific deficit in self-awareness? *Autism, 14*(5), 474–494.

Wolpert, D. M., & Ghahramani, Z. (2000). Computational principles of movement neuroscience. *Nature Neuroscience, 3*(Suppl), 1212–1217.

-----

## Acknowledgments

This paper developed through dialogue clarifying the distinction between embodiment and embeddedness, and specifying the cascade from self/world distinction to self-referential abstraction.

-----

*“The self is not given—it is abstracted. And that abstraction requires a world from which to distinguish oneself.”*

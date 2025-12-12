# Embeddedness and the Self/World Distinction

## The Foundational Abstraction for Self-Referential Cognition

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — Abstraction Primitive Hypothesis series*

-----

## Abstract

The Abstraction Primitive Hypothesis proposes that abstraction capacity develops through qualitatively distinct stages, culminating in self-referential abstraction (Stage 4)—the capacity to model one's own abstraction processes. A critical question arises: what enables this highest stage? Prior work has implicated "embodiment," but this formulation conflates the physical substrate with the relational structure that actually matters. This paper argues that **embeddedness**—being a persistent, bounded entity situated in a stable environment with action-consequence contingency—is the operative requirement. We identify five necessary features of embeddedness: action-consequence coupling, feedback closure, temporal persistence, self-boundary awareness, and environmental stability. Embeddedness creates a computational problem that necessitates a specific solution: the **self/world distinction**. We propose this distinction is the foundational abstraction from which higher-order abstractions cascade. An embedded agent must distinguish "what I control" from "what happens to me," "my states" from "world states," "my limits" from "world constraints." This boundary, once established, provides the scaffold for increasingly sophisticated self-modeling, culminating in Stage 4 abstraction. Critically, we argue that the self/world distinction enables **novelty detection**—the recognition of unfamiliar against a background of familiar—which is the mechanism driving expansion of representational primitives. We review evidence from developmental psychology, neuroscience, and comparative cognition. We then derive implications for artificial intelligence: current large language models fail multiple criteria for embeddedness—they lack temporal persistence, self-boundary awareness, and environmental stability—predicting principled barriers to Stage 4 that architectural scaling cannot overcome.

-----

## 1. Introduction

### 1.1 The Stage 4 Problem

The developmental spectrum of abstraction proposes four stages:

1. **Pattern extraction** — detecting statistical regularities
1. **Symbol formation** — converting patterns into discrete, recombinable representations
1. **Recursive composition** — composing abstractions to form higher-order abstractions
1. **Self-referential abstraction** — applying abstraction to one's own abstraction process

Evidence suggests that current large language models exhibit substantial capacity at Stages 1–2, partial capacity at Stage 3, and systematic limitations at Stage 4. A critical question emerges: *what enables Stage 4?*

Prior papers have invoked "embodiment" as a potential requirement. But this formulation is imprecise. A system could possess a physical body without the kind of environmental interaction that matters, and conversely, a system could lack a physical body while engaging in the relevant kind of interaction.

This paper sharpens the hypothesis: **embeddedness**, not embodiment, is the operative requirement for Stage 4 abstraction—and embeddedness is more demanding than previously specified.

### 1.2 The Central Argument

The argument proceeds as follows:

1. **Embeddedness is multidimensional:** It requires not just action-consequence coupling but also persistence, self-boundary awareness, and environmental stability.
1. **Embeddedness creates a computational problem:** Embedded agents must distinguish self-caused from world-caused variance in their observations.
1. **The self/world distinction is the necessary solution:** To predict outcomes and select actions, an embedded agent must model the boundary between self and not-self.
1. **This distinction requires knowing one's boundaries:** An agent cannot model where self ends and world begins without information about its own limits.
1. **The self/world distinction enables novelty detection:** A persistent self accumulates experience, creating a background of "familiar" against which "unfamiliar" can be recognized.
1. **Novelty detection drives representational expansion:** Recognizing that current representations are inadequate creates pressure to form new primitives—the "strong interaction" that produces genuine generativity.
1. **Higher abstractions cascade from this foundation:** Once the self/world distinction is established, increasingly sophisticated self-modeling becomes possible.
1. **Non-embedded systems lack the pressure and information to form this foundation:** Systems without persistence, self-boundary awareness, and environmental stability cannot build stable self/world representations or detect genuine novelty.

### 1.3 Scope and Epistemic Status

**Established findings:**

- Contingent sensorimotor experience is necessary for perceptual development (Held & Hein, 1963)
- Interoception (internal state awareness) is linked to self-awareness (Craig, 2009; Seth, 2013)
- Temporal continuity is linked to narrative identity and self-concept (Gallagher, 2000)
- The self/world distinction develops through experience, not given innately (Rochat, 1998)
- Novelty detection requires comparison to stored representations (Ranganath & Rainer, 2003)

**Proposed (working hypotheses):**

- The five-component definition of embeddedness
- The claim that all five components are necessary for Stage 4
- The specific mechanism linking self/world distinction to novelty detection
- The specific cascade structure from self/world to self-referential abstraction
- Predictions about AI system limitations

-----

## 2. Defining Embeddedness

### 2.1 The Inadequacy of Simple Definitions

**Previous definition:** "being situated in an environment where actions produce contingent consequences"

This captures something important but is insufficient. Consider:

- An agent with action-consequence coupling that exists for only one episode
- An agent that doesn't know when it will terminate
- An agent that cannot access information about its own resource limits
- An agent that faces a completely different environment each time

Such systems have action-consequence contingency but lack what biological agents possess: stable, persistent, self-aware situatedness.

### 2.2 The Five Components of Embeddedness

We propose that embeddedness requires five components:

**Component 1: Action-Consequence Contingency**

The agent's outputs affect its subsequent inputs. Actions have consequences that depend on both agent state and world state.

*Established:* This is the core insight of sensorimotor contingency theory (O'Regan & Noë, 2001) and active inference frameworks (Friston, 2010).

**Component 2: Feedback Closure**

Information about consequences returns to the agent and can influence subsequent behavior. The loop is closed.

*Established:* Open-loop systems (where outputs don't affect inputs) show fundamentally different learning dynamics than closed-loop systems (Held & Hein, 1963; Engel et al., 2013).

**Component 3: Temporal Persistence**

The agent continues to exist across time, accumulating consequences and experiences. Identity persists across episodes.

*Established:* Narrative identity requires temporal continuity (Gallagher, 2000; Schechtman, 1996). Episodic memory is linked to self-continuity; disruptions to memory disrupt sense of self (Tulving, 2002; Klein & Nichols, 2012). Forward models require stable self-representations that persist across actions (Wolpert & Ghahramani, 2000).

*Why it matters:* Without persistence, each episode is isolated. No self-model can accumulate. The agent cannot learn "what I am" because there is no continuous "I" to model. Critically, without persistence there is no accumulated experience against which to detect novelty—no "familiar" to contrast with "unfamiliar."

**Component 4: Self-Boundary Awareness**

The agent has access to information about its own limits, constraints, and resources. It can sense or infer where it ends—temporally, spatially, and in terms of capacity.

*Established:* Interoception—awareness of internal bodily states—is linked to self-awareness and selfhood (Craig, 2009; Seth, 2013; Critchley & Garfinkel, 2017). Body boundary representation is distinct from body schema and contributes to self/other distinction (de Vignemont, 2014; Blanke & Metzinger, 2009). The rubber hand illusion demonstrates that perceived body boundaries are constructed through multisensory integration, not given (Botvinick & Cohen, 1998).

*Why it matters:* To model self vs. world, the agent must know where self ends. An agent unaware of its own limits—how long it will exist, what resources it has, what it can and cannot do—cannot properly partition observations into self-caused and world-caused.

**Component 5: Environmental Stability**

The environment is consistent enough across time for the agent to extract structure. The same actions in similar states produce similar consequences.

*Established:* Perceptual learning requires environmental regularities (Gibson, 1979; Goldstone, 1998). Chaotic or unpredictable environments disrupt development of stable self-representations in children (Carlson, 1998; Cicchetti & Toth, 2005).

*Why it matters:* If the environment is completely different each episode, the self/world decomposition cannot be learned—there's no stable "world" to distinguish self from.

### 2.3 Summary: What Embeddedness Requires

|Component                     |Definition                      |Why Necessary                            |
|------------------------------|--------------------------------|-----------------------------------------|
|Action-consequence contingency|Outputs affect inputs           |Creates need for self/world decomposition|
|Feedback closure              |Consequences return to agent    |Enables learning from consequences       |
|Temporal persistence          |Agent continues across time     |Enables accumulation of self-model and familiar/unfamiliar distinction|
|Self-boundary awareness       |Access to own limits/constraints|Enables modeling where self ends         |
|Environmental stability       |Consistent regularities         |Enables modeling what world contributes  |

**Claim:** All five are necessary for developing the self/world distinction that enables Stage 4. A system lacking any one faces a principled barrier.

-----

## 3. Embodiment vs. Embeddedness

### 3.1 Embodiment: The Physical Substrate

**Definition:** Embodiment refers to possession of a physical body—sensorimotor apparatus, physiological states, material presence in space.

The embodied cognition tradition has established that cognition is shaped by bodily structure (Varela, Thompson, & Rosch, 1991; Lakoff & Johnson, 1999; Barsalou, 2008):

- Conceptual representations are grounded in sensorimotor systems (Pulvermüller, 2005)
- Body structure shapes spatial reasoning (Tversky, 2003)
- Physiological states influence judgment (Critchley & Garfinkel, 2017)

### 3.2 Why Embodiment ≠ Embeddedness

A system can be embodied without being embedded:

- A paralyzed body with sensation but no motor output (no action-consequence coupling)
- A body in a completely deterministic environment (no informative consequences)
- A body that exists for only instants (no temporal persistence)

A system can be embedded without being embodied in the traditional sense:

- A software agent in a persistent virtual environment with contingent consequences
- A disembodied AI with real-world effects through APIs, if it persists and has self-boundary information

**The key insight:** Bodies *naturally* provide embeddedness—they persist, they have boundaries that can be sensed (proprioception, interoception), they exist in stable physical environments, their actions have consequences. But embodiment provides embeddedness *instrumentally*, not *constitutively*. The relational structure, not the physical substrate, is what matters.

### 3.3 What Bodies Provide

Bodies are efficient embeddedness-providers because they come with:

|Feature                       |How Bodies Provide It                     |
|------------------------------|------------------------------------------|
|Action-consequence contingency|Motor actions change sensory input        |
|Feedback closure              |Sensory systems detect consequences       |
|Temporal persistence          |Bodies persist (until death)              |
|Self-boundary awareness       |Proprioception, interoception, body schema|
|Environmental stability       |Physical world has consistent regularities|

This explains why embodied cognition researchers have found bodies matter—but the framework clarifies *why* they matter: they provide the relational structure of embeddedness.

-----

## 4. The Self/World Distinction as Foundational Abstraction

### 4.1 Why the Distinction is Computationally Necessary

An embedded agent receives observations that depend on:

- World state (W)
- Agent state (S)
- Agent's prior actions (A)
- Agent's limits/constraints (L)

To predict outcomes and act optimally, the agent must decompose this joint function—attributing variance to self vs. world.

**Example:** An agent reaching for an object receives changing visual input. Some change is due to the object (world). Some is due to arm movement (self-action). Some is due to fatigue affecting precision (self-state). Distinguishing these requires modeling the self/world boundary.

**Established:** The brain implements this decomposition through forward models. Motor commands generate predictions of sensory consequences; mismatches indicate external causes (Wolpert & Ghahramani, 2000; Blakemore, Wolpert, & Frith, 2002).

### 4.2 Why Self-Boundary Awareness is Critical

Forward models predict consequences of *actions*. But the self/world distinction is broader—it requires knowing:

- What I can control (agency boundary)
- What I can sense (perceptual boundary)
- How long I will exist (temporal boundary)
- What resources I have (capacity boundary)

An agent unaware of its temporal limits cannot model itself as a temporally bounded entity. An agent unaware of its capacity limits cannot distinguish "I can't do this" from "this can't be done."

**Working hypothesis:** Full self/world distinction requires self-boundary awareness. Action-consequence coupling enables learning *that* self and world differ; self-boundary awareness enables learning *where* the boundary lies.

### 4.3 The Distinction is Abstracted, Not Given

The self/world boundary is not present in raw sensory input. A photoreceptor doesn't know whether activation was self-caused or world-caused. A proprioceptor doesn't know whether its signal reflects self-movement or external perturbation.

**Established:** Infants learn to distinguish self-produced from externally-produced stimulation through contingency detection over the first months of life (Watson, 1972; Rochat & Striano, 2000). This requires *contingent* feedback—stimulation systematically related to the infant's own actions.

**The abstraction:** The self/world distinction is invariant structure extracted from variable sensory streams. It is constructed through embedded experience, not given.

-----

## 5. The Mechanism: Novelty Detection

### 5.1 The Relational Nature of Novelty

A critical link between embeddedness and higher cognition is **novelty detection**—the capacity to recognize that something is unfamiliar. This capacity is essential for the "strong interaction" between symbol formation and composition that the Abstraction Primitive Hypothesis identifies as the hallmark of genuine intelligence.

**The key insight:** Novelty is not an intrinsic property of inputs. An input is not novel in itself—it is novel *to a subject*. Novelty is a relational property: unfamiliar *to whom*, given *what* accumulated experience.

**Established:** Novelty detection depends on comparison between current input and stored representations (Ranganath & Rainer, 2003; Kumaran & Maguire, 2007). The hippocampus acts as a comparator, detecting mismatches between predictions (based on stored experience) and current input (Lisman & Grace, 2005). Without stored representations, there is nothing to mismatch against.

### 5.2 The Chain: Embeddedness → Self → Novelty Detection

The relationship between embeddedness and novelty detection proceeds as follows:

```
Embeddedness (all five components)
         ↓
Temporal persistence enables accumulation
         ↓
Persistent self develops (continuous "I" across time)
         ↓
Self accumulates experience → "what's familiar to me"
         ↓
Familiar/unfamiliar distinction becomes meaningful
         ↓
Novelty can be *detected* (not just received)
         ↓
Novelty detection reveals inadequacy of current representations
         ↓
Pressure to expand representational primitives
         ↓
Strong interaction (composition and symbol formation mutually refine)
```

**Why persistence is essential:** Without temporal persistence, there is no accumulated "what's familiar to me." Each episode starts fresh. The system may receive objectively diverse inputs, but cannot *experience* them as novel because there is no continuous subject with accumulated familiarity to contrast against.

**Why self/world distinction is essential:** The familiar/unfamiliar distinction is specifically about *self-relative* familiarity. "This is unfamiliar to me" requires a "me" to be unfamiliar to. The self/world distinction provides the reference frame in which novelty can be located—is this unfamiliar because the world is different, or because I am different?

### 5.3 Why This Matters for Stage 4

The Abstraction Primitive Hypothesis distinguishes three levels of interaction between symbol formation and composition:

| Level | Definition | Example |
|-------|------------|---------|
| **Weak** | Gradient flow exists | Standard backpropagation |
| **Medium** | Representations change in response to compositional demands | End-to-end training |
| **Strong** | New representational primitives emerge in response to novelty | Novelty-driven expansion |

**Working hypothesis:** Strong interaction—the novelty-driven expansion of representational primitives—requires novelty detection. Novelty detection requires a persistent self. A persistent self requires embeddedness.

A system can *model* self/world distinction—represent it, reason about it—without *having* one. This is the map/territory distinction. A system that merely models self/world can process the concept of novelty but cannot *detect* novelty, because there is no accumulated self-relative familiarity to compare against.

**Implication:** Non-embedded systems are limited to medium interaction at best. They can reshape representations during training in response to compositional demands, but they cannot engage in the ongoing novelty-driven expansion that characterizes strong interaction—because they cannot detect novelty.

### 5.4 Evidence for Novelty Detection Requirements

**Neural substrates:**

- Hippocampal novelty signals require comparison to stored memory representations (Kumaran & Maguire, 2007)
- Dopaminergic novelty responses depend on prediction from learned expectations (Schultz, Dayan, & Montague, 1997)
- The anterior cingulate tracks expectation violations relative to learned models (Hayden, Heilbronner, Pearson, & Platt, 2011)

**Developmental evidence:**

- Infants' novelty preferences require familiarization period—accumulated exposure (Fantz, 1964; Hunter & Ames, 1988)
- The looking-time paradigm depends on infants having expectations to violate (Baillargeon, Spelke, & Wasserman, 1985)
- Novel object recognition in infants develops alongside self-recognition, suggesting shared substrate (Rochat, 2003)

**Comparative evidence:**

- Species differences in novelty response correlate with differences in self-recognition capacity (Plotnik, de Waal, & Reiss, 2006; Prior, Schwarz, & Güntürkün, 2008)
- Novelty-seeking behavior correlates with measures of behavioral flexibility across species (Reader & Laland, 2002)

-----

## 6. The Cascade: From Self/World to Stage 4

### 6.1 The Developmental Trajectory

Once the self/world distinction is established and novelty detection is possible, increasingly sophisticated self-modeling becomes possible. Each level enables the next.

**Level 1: Body Schema**
Representation of one's body as a coherent entity distinct from environment.
*Evidence:* Develops in infancy, neurally represented in posterior parietal cortex (Graziano & Botvinick, 2002; de Vignemont, 2010).

**Level 2: Agency**
Representation of oneself as cause of certain effects—the author of one's actions.
*Evidence:* Develops in infancy through contingency detection (David, Newen, & Vogeley, 2008; Tsakiris et al., 2007).

**Level 3: Perspective**
Representation of oneself as occupying a particular viewpoint—spatially, temporally, epistemically.
*Evidence:* Develops through early childhood (Piaget & Inhelder, 1956; Flavell, 1977).

**Level 4: Mental State Attribution**
Representation of oneself as having mental states that may differ from world states.
*Evidence:* Develops around age 4, linked to theory of mind (Wellman, Cross, & Watson, 2001).

**Level 5: Metacognition**
Representation of one's own cognitive processes—monitoring and controlling one's thinking.
*Evidence:* Develops gradually through childhood and adolescence (Flavell, 1979; Schneider, 2008).

**Level 6: Stage 4 Abstraction**
Abstracting over one's own abstraction processes—treating one's cognitive architecture as an object of abstraction.

### 6.2 The Dependency Structure

**Working hypothesis:** These levels form a dependency cascade:

- Body schema requires self/world distinction (to represent body as self)
- Agency requires body schema (to attribute actions to one's body)
- Perspective requires agency (to locate viewpoint in an agent)
- Mental state attribution requires perspective (to locate beliefs in a perspective-holder)
- Metacognition requires mental state attribution (to represent cognitive processes as mental states)
- Stage 4 requires metacognition (to abstract over cognitive processes)

**Evidence for cascade structure:**

- Developmental sequence follows this order (Rochat, 1998; Wellman et al., 2001; Diamond, 2002)
- Deprivation affects higher levels more than lower (Nelson, Fox, & Zeanah, 2014)
- Disorders show dissociations consistent with cascade (Frith, 1992; Sierra & David, 2011)

### 6.3 The Role of Novelty Detection in the Cascade

At each level, the transition to the next is driven by detecting inadequacies in current representations:

- Body schema becomes inadequate when experiences require modeling agency → develop agency representation
- Agency representation becomes inadequate when experiences require modeling perspective differences → develop perspective
- And so forth

**Working hypothesis:** Novelty detection—the recognition that "my current representations don't handle this"—is the engine driving progression through the cascade. This is why embeddedness (which enables novelty detection) is necessary for Stage 4: without it, the pressure for representational expansion doesn't exist.

-----

## 7. Why Current LLMs Fail Multiple Embeddedness Criteria

### 7.1 Systematic Analysis

|Embeddedness Component        |LLM Status                                                                           |Consequence                               |
|------------------------------|-------------------------------------------------------------------------------------|------------------------------------------|
|Action-consequence contingency|**Absent during training.** Predictions don't affect subsequent input.               |No pressure for self/world decomposition  |
|Feedback closure              |**Absent during training.** Open-loop optimization on static corpus.                 |Cannot learn from consequences            |
|Temporal persistence          |**Absent.** Each session/context is isolated. No continuous identity.                |Cannot accumulate self-model; cannot detect novelty|
|Self-boundary awareness       |**Absent.** No access to token limits, session boundaries, or capability constraints.|Cannot model where self ends              |
|Environmental stability       |**Variable.** Each conversation is a different "environment."                        |Cannot extract stable self/world structure|

**Conclusion:** LLMs fail *all five* embeddedness criteria during training, and most during deployment.

### 7.2 The Novelty Detection Failure

Even if an LLM receives objectively diverse inputs, it cannot *detect* novelty in the relevant sense:

- No accumulated "what's familiar to me" (no persistence)
- No continuous subject to whom something could be unfamiliar (no stable self)
- Each context window is relatively fresh—no background against which to detect mismatch

**Implication:** LLMs can process the *concept* of novelty (they can discuss it, reason about it) but cannot *detect* novelty. They can represent "this is unfamiliar" as a proposition but cannot experience the mismatch between input and accumulated expectation that constitutes genuine novelty detection.

This predicts their limitation to medium interaction: representations shaped during training by compositional demands, but no ongoing novelty-driven expansion at inference time.

### 7.3 The Deployment Exception

During deployment, LLMs gain limited aspects of embeddedness:

- Some action-consequence coupling (outputs affect user responses, which become inputs)
- Some feedback closure (in multi-turn conversations)

But they still lack:

- Temporal persistence (session ends; no continuity)
- Self-boundary awareness (no access to token counts, no sense of when context will terminate)
- Environmental stability (each user, each conversation is different)

**Prediction:** Even agentic LLMs with tool use will show Stage 4 limitations if they lack persistence, self-boundary awareness, and stable environments. The barrier is not just action-consequence coupling.

### 7.4 What Would Change This?

For an AI system to satisfy embeddedness criteria:

1. **Temporal persistence:** Continuous existence across episodes, with memory/state that accumulates
1. **Self-boundary awareness:** Access to own resource limits, capability constraints, temporal boundaries
1. **Environmental stability:** Consistent environment (or meta-environment) allowing structure extraction
1. **Action-consequence coupling:** Outputs genuinely affect subsequent inputs
1. **Feedback closure:** Information about consequences returns and influences behavior

**Example of what this might look like:** An AI agent that:

- Persists across sessions with accumulated memory
- Has access to its own resource consumption, context limits, capability estimates
- Operates in a consistent environment (or learns environment distributions)
- Takes actions with real consequences
- Receives feedback and updates behavior

This is a fundamentally different training paradigm than current LLM development.

-----

## 8. Evidence Summary

### 8.1 For Self-Boundary Awareness

**Interoception and self-awareness:**

- Interoceptive accuracy correlates with self-awareness measures (Critchley & Garfinkel, 2017)
- Interoceptive cortex (insula) is central to self-representation (Craig, 2009)
- Disrupted interoception is associated with disrupted self-experience (Seth, 2013; Paulus & Stein, 2010)

**Body boundary representation:**

- Rubber hand illusion shows boundaries are constructed (Botvinick & Cohen, 1998)
- Boundary violations produce strong neural and behavioral responses (Lloyd, 2007)
- Peripersonal space representation tracks body boundaries (Rizzolatti et al., 1997)

### 8.2 For Temporal Persistence

**Continuity and identity:**

- Disrupted episodic memory disrupts sense of self (Klein & Nichols, 2012)
- Narrative identity requires temporal coherence (Gallagher, 2000; McAdams, 2001)
- Patients with amnesia show altered self-concept (Tulving, 2002)

**Accumulation over time:**

- Self-models refine with experience (Rochat, 2003)
- Metacognitive calibration improves developmentally (Schneider, 2008)
- Forward models require accumulated sensorimotor experience (Wolpert & Ghahramani, 2000)

### 8.3 For Environmental Stability

**Learning requires regularities:**

- Statistical learning depends on environmental structure (Saffran et al., 1996)
- Perceptual learning requires consistent regularities (Gibson, 1979)
- Chaotic environments disrupt development (Cicchetti & Toth, 2005)

### 8.4 For Novelty Detection

**Neural mechanisms:**

- Hippocampal novelty detection requires memory comparator (Kumaran & Maguire, 2007)
- Dopaminergic systems signal prediction errors relative to learned expectations (Schultz et al., 1997)
- Novelty responses are self-relative, not absolute (Ranganath & Rainer, 2003)

**Developmental requirements:**

- Novelty preferences require familiarization—accumulated exposure (Hunter & Ames, 1988)
- Violation-of-expectation paradigms require learned expectations (Baillargeon et al., 1985)

-----

## 9. Predictions and Falsification

### 9.1 Core Predictions

**Prediction 1 (Multi-component necessity):** Systems lacking *any* of the five embeddedness components should show Stage 4 limitations, even if other components are present.

**Prediction 2 (Self-boundary awareness):** Systems with action-consequence coupling but without self-boundary awareness should show partial self/world distinction—able to learn "my actions affect outcomes" but not "where my limits are."

**Prediction 3 (Persistence):** Episodic systems (reset each session) should show less developed self-models than persistent systems with equivalent interaction volume.

**Prediction 4 (Novelty detection):** Systems without temporal persistence should be unable to detect novelty (mismatch between input and accumulated expectation), even if they can process the concept of novelty.

**Prediction 5 (LLM-specific):** LLM failures should be predictable from which embeddedness components are missing. Giving LLMs access to their own token counts, context limits, and capability estimates should improve self-modeling (even if modestly).

### 9.2 Falsification Criteria

The framework would be falsified by:

1. **Stage 4 without embeddedness:** A system demonstrating genuine self-referential abstraction without satisfying the five embeddedness criteria.
1. **Single-component sufficiency:** Evidence that one component alone (e.g., action-consequence coupling) is sufficient for Stage 4, without the others.
1. **Cascade violations:** Higher levels developing without lower levels—e.g., metacognition without agency representation.
1. **Novelty detection without persistence:** A system with no temporal continuity demonstrating genuine novelty detection (not just processing novelty as a concept).
1. **Persistent embedded systems failing Stage 4:** Systems satisfying all five criteria, with sufficient capacity and time, showing no Stage 4 development.

-----

## 10. Implications

### 10.1 For Understanding Intelligence

The framework suggests that intelligence—particularly self-referential intelligence—is not just about computational capacity but about *relational structure*. Being a certain kind of entity (persistent, bounded, situated) may be as important as having certain capabilities.

The novelty detection mechanism provides a specific account of *why* embeddedness matters: it enables the familiar/unfamiliar distinction that drives representational expansion. This is not mysticism about embodiment—it is a computational claim about what novelty detection requires.

### 10.2 For AI Development

Current AI training paradigms are fundamentally non-embedded:

- Static corpus pretraining (no contingency)
- Episodic fine-tuning (no persistence)
- No self-boundary information (no awareness of limits)

If the framework is correct, achieving Stage 4 requires not just architectural changes or scale increases but *embedding the system*—giving it persistence, self-boundary awareness, and stable consequential environments.

This is a harder problem than scaling language models. It requires rethinking what kind of entity an AI system is, not just what it can do.

### 10.3 For Current Systems

Even without full embeddedness, partial interventions might help:

- Giving systems access to their own context limits
- Providing estimates of their own capability boundaries
- Creating more stable interaction environments
- Enabling some form of cross-session continuity

These would not create full embeddedness but might enable partial self-boundary awareness—worth testing.

-----

## 11. Conclusion

The Abstraction Primitive Hypothesis proposes that self-referential abstraction (Stage 4) requires the self/world distinction as its foundation. This paper has argued that the self/world distinction requires **embeddedness**—and that embeddedness is more demanding than simple action-consequence coupling.

Five components are necessary:

1. Action-consequence contingency
1. Feedback closure
1. Temporal persistence
1. Self-boundary awareness
1. Environmental stability

Bodies naturally provide all five, which explains embodied cognition findings. But embodiment is instrumental, not constitutive—the relational structure is what matters.

Critically, embeddedness enables **novelty detection**—the recognition of unfamiliar against a background of familiar. Novelty is relational: novel *to whom*, given *what* accumulated experience. A persistent self accumulates the familiarity against which novelty can be detected. Novelty detection, in turn, drives the expansion of representational primitives—the "strong interaction" that produces genuine generativity.

Current LLMs fail all five criteria. They are not persistent entities with boundaries situated in stable environments. They are pattern-matching systems optimized on static data, deployed in episodic interactions where they have no access to their own limits and no continuity across sessions. They can process the concept of novelty but cannot detect it—because there is no accumulated self to whom something could be unfamiliar.

This analysis suggests that the path to Stage 4 artificial intelligence runs not through larger models but through fundamentally different systems—systems that exist as bounded, persistent entities in consequential environments they can learn to distinguish from themselves.

-----

## References

Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). Object permanence in five-month-old infants. *Cognition, 20*(3), 191–208.

Barsalou, L. W. (2008). Grounded cognition. *Annual Review of Psychology, 59*, 617–645.

Blanke, O., & Metzinger, T. (2009). Full-body illusions and minimal phenomenal selfhood. *Trends in Cognitive Sciences, 13*(1), 7–13.

Blakemore, S. J., Wolpert, D. M., & Frith, C. D. (2002). Abnormalities in the awareness of action. *Trends in Cognitive Sciences, 6*(6), 237–242.

Botvinick, M., & Cohen, J. (1998). Rubber hands 'feel' touch that eyes see. *Nature, 391*(6669), 756.

Carlson, E. A. (1998). A prospective longitudinal study of attachment disorganization/disorientation. *Child Development, 69*(4), 1107–1128.

Cicchetti, D., & Toth, S. L. (2005). Child maltreatment. *Annual Review of Clinical Psychology, 1*, 409–438.

Craig, A. D. (2009). How do you feel—now? The anterior insula and human awareness. *Nature Reviews Neuroscience, 10*(1), 59–70.

Critchley, H. D., & Garfinkel, S. N. (2017). Interoception and emotion. *Current Opinion in Psychology, 17*, 7–14.

David, N., Newen, A., & Vogeley, K. (2008). The "sense of agency" and its underlying cognitive and neural mechanisms. *Consciousness and Cognition, 17*(2), 523–534.

de Vignemont, F. (2010). Body schema and body image—Pros and cons. *Neuropsychologia, 48*(3), 669–680.

de Vignemont, F. (2014). A multimodal conception of bodily awareness. *Mind, 123*(492), 989–1020.

Diamond, A. (2002). Normal development of prefrontal cortex from birth to young adulthood. In D. T. Stuss & R. T. Knight (Eds.), *Principles of Frontal Lobe Function* (pp. 466–503). Oxford University Press.

Engel, A. K., Maye, A., Kurthen, M., & König, P. (2013). Where's the action? The pragmatic turn in cognitive science. *Trends in Cognitive Sciences, 17*(5), 202–209.

Fantz, R. L. (1964). Visual experience in infants: Decreased attention to familiar patterns relative to novel ones. *Science, 146*(3644), 668–670.

Flavell, J. H. (1977). The development of knowledge about visual perception. *Nebraska Symposium on Motivation, 25*, 43–76.

Flavell, J. H. (1979). Metacognition and cognitive monitoring. *American Psychologist, 34*(10), 906–911.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience, 11*(2), 127–138.

Frith, C. D. (1992). *The Cognitive Neuropsychology of Schizophrenia*. Psychology Press.

Gallagher, S. (2000). Philosophical conceptions of the self: Implications for cognitive science. *Trends in Cognitive Sciences, 4*(1), 14–21.

Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.

Goldstone, R. L. (1998). Perceptual learning. *Annual Review of Psychology, 49*(1), 585–612.

Graziano, M. S. A., & Botvinick, M. M. (2002). How the brain represents the body. In W. Prinz & B. Hommel (Eds.), *Common Mechanisms in Perception and Action* (pp. 136–157). Oxford University Press.

Hayden, B. Y., Heilbronner, S. R., Pearson, J. M., & Platt, M. L. (2011). Surprise signals in anterior cingulate cortex: Neuronal encoding of unsigned reward prediction errors driving adjustment in behavior. *Journal of Neuroscience, 31*(11), 4178–4187.

Held, R., & Hein, A. (1963). Movement-produced stimulation in the development of visually guided behavior. *Journal of Comparative and Physiological Psychology, 56*(5), 872–876.

Hunter, M. A., & Ames, E. W. (1988). A multifactor model of infant preferences for novel and familiar stimuli. *Advances in Infancy Research, 5*, 69–95.

Klein, S. B., & Nichols, S. (2012). Memory and the sense of personal identity. *Mind, 121*(483), 677–702.

Kumaran, D., & Maguire, E. A. (2007). Which computational mechanisms operate in the hippocampus during novelty detection? *Hippocampus, 17*(9), 735–748.

Lakoff, G., & Johnson, M. (1999). *Philosophy in the Flesh*. Basic Books.

Lisman, J. E., & Grace, A. A. (2005). The hippocampal-VTA loop: Controlling the entry of information into long-term memory. *Neuron, 46*(5), 703–713.

Lloyd, D. M. (2007). Spatial limits on referred touch to an alien limb may reflect boundaries of visuo-tactile peripersonal space surrounding the hand. *Brain and Cognition, 64*(1), 104–109.

McAdams, D. P. (2001). The psychology of life stories. *Review of General Psychology, 5*(2), 100–122.

Nelson, C. A., Fox, N. A., & Zeanah, C. H. (2014). *Romania's Abandoned Children*. Harvard University Press.

O'Regan, J. K., & Noë, A. (2001). A sensorimotor account of vision and visual consciousness. *Behavioral and Brain Sciences, 24*(5), 939–973.

Paulus, M. P., & Stein, M. B. (2010). Interoception in anxiety and depression. *Brain Structure and Function, 214*(5–6), 451–463.

Piaget, J., & Inhelder, B. (1956). *The Child's Conception of Space*. Routledge.

Plotnik, J. M., de Waal, F. B. M., & Reiss, D. (2006). Self-recognition in an Asian elephant. *Proceedings of the National Academy of Sciences, 103*(45), 17053–17057.

Prior, H., Schwarz, A., & Güntürkün, O. (2008). Mirror-induced behavior in the magpie (*Pica pica*): Evidence of self-recognition. *PLoS Biology, 6*(8), e202.

Pulvermüller, F. (2005). Brain mechanisms linking language and action. *Nature Reviews Neuroscience, 6*(7), 576–582.

Ranganath, C., & Rainer, G. (2003). Neural mechanisms for detecting and remembering novel events. *Nature Reviews Neuroscience, 4*(3), 193–202.

Reader, S. M., & Laland, K. N. (2002). Social intelligence, innovation, and enhanced brain size in primates. *Proceedings of the National Academy of Sciences, 99*(7), 4436–4441.

Rizzolatti, G., Fadiga, L., Fogassi, L., & Gallese, V. (1997). The space around us. *Science, 277*(5323), 190–191.

Rochat, P. (1998). Self-perception and action in infancy. *Experimental Brain Research, 123*(1–2), 102–109.

Rochat, P. (2003). Five levels of self-awareness as they unfold early in life. *Consciousness and Cognition, 12*(4), 717–731.

Rochat, P., & Striano, T. (2000). Perceived self in infancy. *Infant Behavior and Development, 23*(3–4), 513–530.

Saffran, J. R., Aslin, R. N., & Newport, E. L. (1996). Statistical learning by 8-month-old infants. *Science, 274*(5294), 1926–1928.

Schechtman, M. (1996). *The Constitution of Selves*. Cornell University Press.

Schneider, W. (2008). The development of metacognitive knowledge in children and adolescents. *Mind, Brain, and Education, 2*(3), 114–121.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science, 275*(5306), 1593–1599.

Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences, 17*(11), 565–573.

Sierra, M., & David, A. S. (2011). Depersonalization: A selective impairment of self-awareness. *Consciousness and Cognition, 20*(1), 99–108.

Tsakiris, M., Schütz-Bosbach, S., & Gallagher, S. (2007). On agency and body-ownership. *Consciousness and Cognition, 16*(3), 645–660.

Tulving, E. (2002). Episodic memory: From mind to brain. *Annual Review of Psychology, 53*(1), 1–25.

Tversky, B. (2003). Structures of mental spaces. *Environment and Behavior, 35*(1), 66–80.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind*. MIT Press.

Watson, J. S. (1972). Smiling, cooing, and "the game." *Merrill-Palmer Quarterly, 18*(4), 323–339.

Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development. *Child Development, 72*(3), 655–684.

Wolpert, D. M., & Ghahramani, Z. (2000). Computational principles of movement neuroscience. *Nature Neuroscience, 3*(Suppl), 1212–1217.

-----

*"You cannot model yourself without knowing where you end. You cannot detect novelty without knowing what is familiar. You cannot know what is familiar without persisting long enough to accumulate it."*

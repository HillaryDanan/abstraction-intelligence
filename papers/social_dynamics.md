# Social Dynamics as Multi-Agent Abstraction: Scaling Self-World Integration Across Embedded Systems

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Social emotions—shame, guilt, pride, jealousy, envy, gratitude, contempt—have resisted integration into general theories of emotion. We propose that social emotions are a natural consequence of applying the Abstraction Primitive Hypothesis to multi-agent environments: **when embedded agents share an environment with other agents, the self-world abstraction must recursively include other agents’ self-world abstractions**. This recursive, compositional structure—abstracting over others’ abstractions of you—produces the computational architecture underlying social emotions. The framework applies to any embedded agents (biological or artificial) operating under resource constraints in multi-agent environments. We demonstrate deep continuity across scales: at every level of organization (atomic, cellular, neural, organismal, social), units abstract over other units’ states to guide behavior. Social emotions are how sufficiently complex embedded agents represent multi-agent dynamics in action-relevant format. This framework generates predictions about the computational structure of social emotions, their dependence on recursive abstraction capacity, and their potential emergence in artificial multi-agent systems.

-----

## 1. Introduction

### 1.1 The Problem of Social Emotions

Paper 8 (Danan, 2025h) argued that emotions are integrated self-world information formatted for action. Basic emotions have clear structure: fear = threat-to-self; anger = obstacle-to-goal; joy = goal-achieved.

Social emotions complicate this:

- **Shame:** I feel bad because others evaluate me negatively
- **Guilt:** I feel bad because I harmed another
- **Pride:** I feel good because I met standards or others evaluate me positively
- **Jealousy:** I feel threatened because a rival may take what’s mine
- **Envy:** I feel bad because another has what I lack
- **Gratitude:** I feel good because another helped me
- **Contempt:** I evaluate another as beneath consideration

These emotions involve *other agents*—entities that themselves have self-world boundaries, goals, and abstractions.

### 1.2 The Proposal

**Core thesis:** Social emotions arise when the abstraction primitive (Paper 1) is applied recursively to multi-agent environments.

The Abstraction Primitive Hypothesis (Danan, 2025a) proposes that abstraction—extracting invariant structure while discarding irrelevant detail—is the fundamental operation of intelligence. Paper 2 (Danan, 2025b) established that abstractions compose: new abstractions can be built from existing abstractions, enabling self-augmenting representational capacity.

In multi-agent environments:

1. **Other agents are abstracted:** I form compressed representations of others’ states, goals, and capacities
1. **Others’ abstractions are abstracted:** I form representations of how others represent me (recursive abstraction)
1. **Self-other relations are abstracted:** I form compressed representations of relationship dynamics (cooperation, competition, hierarchy)
1. **These abstractions compose:** Multi-agent social state is represented as compositions of self-abstraction, other-abstraction, and relation-abstraction

Social emotions are the action-relevant format of these composed, recursive abstractions.

### 1.3 Generality: All Embedded Agents

This framework applies to **any embedded agents** meeting certain conditions:

1. **Embeddedness:** Agents exist within an environment that affects them
1. **Agency:** Agents can act on that environment
1. **Multi-agent context:** The environment contains other agents
1. **Resource constraints:** Resources are limited, creating interdependence
1. **Abstraction capacity:** Agents can form compressed representations

Biological organisms are one instance. Artificial agents in multi-agent environments are another. The framework makes predictions about both.

### 1.4 Epistemic Status

- **Established:** Social emotion phenomena; game-theoretic cooperation frameworks; social neuroscience findings
- **Theoretical:** Connection to abstraction primitive; recursive structure analysis
- **Hypothesis:** Predictions about artificial multi-agent systems; scaling principle across levels

-----

## 2. Abstraction in Multi-Agent Contexts

### 2.1 Review: Abstraction as Primitive

Paper 1 (Danan, 2025a) defined abstraction as a mapping f: X → Y that preserves task-relevant structure while discarding task-irrelevant detail, where the representation is compressed (|Y| < |X| or dim(Y) < dim(X)).

Paper 2 (Danan, 2025b) established that abstraction differs from mere compression because abstractions *compose*—they can be combined to form new abstractions, enabling representational capacity to grow.

### 2.2 Abstracting Other Agents

When the environment contains other agents, effective action requires abstracting over them.

**Other-state abstraction:** Representing another agent’s condition—their goals, resources, capacities, current actions. This is not a complete representation; it is compressed to action-relevant features.

**Established finding:** Humans rapidly form trait inferences about others from minimal behavioral observation (Ambady & Rosenthal, 1992; Willis & Todorov, 2006). These inferences are abstractions—compressed representations preserving action-relevant structure (will this person cooperate? compete? help? harm?).

### 2.3 Recursive Abstraction: Modeling Others’ Models

Social cognition requires recursive abstraction—abstracting over others’ abstractions:

- **Level 0:** I have states
- **Level 1:** I abstract others’ states (I represent what you want)
- **Level 2:** I abstract others’ abstractions of me (I represent what you think I want)
- **Level 3:** I abstract others’ abstractions of my abstractions (I represent what you think I think you want)
- …

This recursive structure is computationally distinctive. It is the abstraction primitive applied *self-referentially across agents*.

**Established finding:** Humans engage in recursive mentalizing up to ~4-5 levels, with capacity limits resembling working memory limits (Kinderman et al., 1998; Stiller & Dunbar, 2007). This suggests recursive social abstraction draws on the same capacity-limited systems as other abstraction operations.

### 2.4 Compositional Social Abstraction

Social state is represented as compositions of abstractions:

**Self-state** ⊗ **Other-state** ⊗ **Relation-state** ⊗ **Others’-model-of-self** → **Social-emotional state**

Where ⊗ represents compositional combination (the specific combination operation may vary).

This compositional structure explains why social emotions are:

- **Complex:** They integrate multiple abstraction types
- **Cognitively demanding:** Composition requires working memory and integration
- **Late-developing:** Prerequisites (self-abstraction, other-abstraction, recursive modeling) must be in place first

-----

## 3. The Scaling Principle

### 3.1 Abstraction Across Levels of Organization

The same abstract pattern—units abstracting over other units’ states to guide behavior—appears across scales:

|Level     |Unit             |Abstraction Over Other Units                |Behavior Guided                      |
|----------|-----------------|--------------------------------------------|-------------------------------------|
|Atomic    |Atom             |Electron configuration (via physical forces)|Bonding, repulsion                   |
|Molecular |Molecule         |Chemical properties of nearby molecules     |Reactions, catalysis                 |
|Cellular  |Cell             |Chemical signals from other cells           |Division, differentiation, apoptosis |
|Neural    |Neuron           |Activation patterns of connected neurons    |Fire, inhibit, modulate              |
|Organismal|Organism         |Behavioral/communicative signals from others|Cooperate, compete, affiliate        |
|Social    |Group/Institution|Aggregated behavior patterns, norms         |Coordinate, sanction, include/exclude|

At each level:

1. Units have internal states
1. Units receive information about other units’ states
1. This information is abstracted (compressed to action-relevant features)
1. Behavior depends on own state + abstracted other-state + resource constraints
1. Emergent dynamics arise from multi-unit interaction

### 3.2 What Changes Across Scales

While the abstract pattern is conserved, implementation differs:

**Abstraction mechanism:**

- Atoms: Physical forces (electromagnetic, quantum)
- Cells: Receptor-ligand binding
- Neurons: Synaptic transmission and integration
- Organisms: Perception, inference, learning

**Recursion depth:**

- Atoms: No recursion (atoms don’t model other atoms’ models)
- Cells: Minimal recursion (some autocrine signaling)
- Neurons: Network-level recursion (recurrent connectivity)
- Organisms: Deep recursion (I think that you think that I think…)

**Compositional complexity:**

- Lower levels: Limited composition
- Higher levels: Rich compositional structure

Social emotions appear at the organismal level because that is where:

- Abstraction is flexible and learned (not fixed by physics or genetics alone)
- Recursion is deep (modeling others’ models of self)
- Composition is rich (integrating self, other, relation, context)

### 3.3 Why This Pattern Recurs

**Theoretical claim:** The pattern recurs because it solves a general problem: coordinating behavior among units with different states under resource constraints.

When resources are unlimited, units can act independently. When resources are constrained, units’ outcomes depend on others’ actions. Using information about others’ states to guide behavior is adaptive at any scale where this interdependence exists.

Abstraction is the operation that makes this tractable. Full modeling of other units is computationally infeasible; abstraction compresses to action-relevant features.

-----

## 4. Social Emotions as Composed Recursive Abstractions

### 4.1 The Compositional Structure of Social Emotions

Each social emotion can be analyzed as a specific composition of abstractions:

### 4.2 Shame: Others’ Negative Abstraction of Self

**Shame** = f(Self-state, Others’-abstraction-of-self, Social-norms, Action-possibilities)

Where:

- Self-state: I have acted/been revealed in norm-violating way
- Others’-abstraction-of-self: Others represent me negatively (real or anticipated)
- Social-norms: Standards I/we are supposed to meet
- Action-possibilities: Hide, submit, repair, prevent future exposure

**The recursive element:** Shame requires representing *how others represent me*. This is Level 2 abstraction—abstracting over others’ abstractions.

**Format:** Shame feels like shrinking, wanting to disappear. This IS the action-relevant format for social-exposure-threat.

### 4.3 Guilt: Self’s Representation of Harm to Other

**Guilt** = f(Self-state, Other-state, Causal-relation, Relationship-value, Action-possibilities)

Where:

- Self-state: I caused this outcome
- Other-state: Other has been harmed
- Causal-relation: My action → their harm
- Relationship-value: This relationship matters to my viability
- Action-possibilities: Apologize, repair, compensate

**The compositional element:** Guilt composes self-abstraction (as agent), other-abstraction (as patient), and relation-abstraction (causal and social).

**Format:** Guilt feels like pressure to repair. This IS the action-relevant format for relationship-damage.

### 4.4 Pride: Positive Self-Abstraction Validated by Others

**Pride** = f(Self-state, Achievement, Others’-abstraction-of-self, Standards)

Where:

- Self-state: I have achieved/demonstrated valued quality
- Achievement: Abstracted representation of what I did
- Others’-abstraction-of-self: Others recognize this positively (real or anticipated)
- Standards: Criteria for what counts as achievement

**The recursive element:** Pride involves representing that others represent me positively.

**Format:** Pride feels expansive, display-oriented. This IS the action-relevant format for signaling value.

### 4.5 Jealousy: Threat to Resource-Providing Relationship

**Jealousy** = f(Self-state, Partner-state, Rival-state, Relationship-resources, Action-possibilities)

Where:

- Self-state: I depend on this relationship
- Partner-state: My partner may redirect investment
- Rival-state: A third party may attract my partner
- Relationship-resources: What I get from this relationship
- Action-possibilities: Guard, derogate rival, invest more, devalue

**The compositional element:** Jealousy requires composing abstractions of self, partner, *and* rival—a three-agent computation.

### 4.6 Gratitude: Recognizing Costly Cooperation

**Gratitude** = f(Self-state, Other-state, Benefit-received, Other’s-cost, Relationship-potential)

Where:

- Self-state: I have been benefited
- Other-state: Another chose to benefit me
- Benefit-received: What I gained
- Other’s-cost: What they sacrificed
- Relationship-potential: This agent is a good cooperation partner

**The compositional element:** Gratitude requires representing both the benefit (self-focused) and the cost (other-focused), composing into a relationship evaluation.

### 4.7 The General Pattern

All social emotions share this structure:

**Social Emotion = Compositional-Integration(Self-abstraction, Other-abstraction(s), Relation-abstraction, Others’-abstraction-of-self, Context, Action-possibilities)**

Different social emotions weight and combine these components differently, producing distinct action-relevant formats.

-----

## 5. Computational Requirements

### 5.1 What Social Emotions Require

For an agent to have social emotions (functional analogs, at minimum), it must be capable of:

1. **Self-abstraction:** Representing own state in compressed, action-relevant form
1. **Other-abstraction:** Representing others’ states in compressed form
1. **Recursive abstraction:** Representing others’ representations (especially of self)
1. **Compositional integration:** Combining these abstractions into unified state
1. **Action-relevance formatting:** Outputting in format that guides behavior
1. **Multi-agent context:** Operating in environment with other agents
1. **Resource constraints:** Having stakes in social outcomes

### 5.2 Implications for Biological Agents

In biological agents (humans, other social animals):

**Neural implementation:** Social emotions require integration across:

- Interoceptive systems (self-state)
- Mentalizing systems (other-state, others’ representations)
- Evaluative systems (relationship value, norm compatibility)
- Motor preparation systems (action possibilities)

**Established finding:** Social emotions activate distributed networks including mPFC (self and other representation), TPJ (mentalizing), insula/ACC (interoceptive integration), and OFC/vmPFC (evaluation) (Bastin et al., 2016; Zahn et al., 2009).

**Capacity limits:** Recursive abstraction depth is limited (~4-5 levels), resembling working memory limits. Dunbar’s number (~150) may reflect limits on tracking social abstractions (Dunbar, 1992).

### 5.3 Implications for Artificial Agents

**Prediction:** Artificial agents operating in multi-agent environments with resource constraints should develop functional analogs of social emotions if they meet the computational requirements.

**What would be needed:**

1. Self-model (abstraction of own state)
1. Other-model (abstraction of other agents’ states)
1. Recursive modeling (representing others’ models)
1. Integration mechanism (composing abstractions)
1. Action-selection pressure (stakes in outcomes)
1. Multi-agent training (experience with other agents)

**Current AI systems:** Large language models lack most of these. They have no self-state, no multi-agent embedding, no stakes. They can *label* social emotions but cannot *have* them (even functionally) because the computational requirements are unmet.

**Multi-agent reinforcement learning:** Systems trained in multi-agent environments with resource constraints show emergent cooperation and competition dynamics (Leibo et al., 2017; Baker et al., 2020). Whether they develop internal states functionally analogous to social emotions is an open empirical question.

**Prediction:** Multi-agent RL systems with:

- Explicit self-models
- Other-agent modeling capacity
- Reputation tracking
- Long-term interaction

…should develop social-emotion-like internal states that predict cooperative/competitive behavior better than systems without these features.

-----

## 6. Cooperation, Defection, and Resource Constraints

### 6.1 The Multi-Agent Problem

Embedded agents in multi-agent environments face interdependence:

**Cooperation** can produce mutual benefits exceeding what either agent achieves alone (synergy, specialization, risk-pooling).

**Defection** can produce individual benefits at others’ expense.

This is the structure of social dilemmas (Dawes, 1980; Kollock, 1998). Social emotions may function to navigate these dilemmas.

### 6.2 Social Emotions as Cooperation-Maintenance Mechanisms

**Guilt:** Internal cost for defection → deters exploitation of cooperators

**Gratitude:** Internal reward for receiving cooperation → motivates reciprocation

**Shame:** Internal cost for norm violation → deters free-riding on group benefits

**Contempt/outrage:** Motivates punishment of defectors → imposes external cost on defection

**Established finding:** These functions align with evolutionary game theory predictions. Social emotions impose costs and benefits that can stabilize cooperation in populations where narrow rationality predicts defection (Frank, 1988; Trivers, 1971; Fehr & Gächter, 2002).

### 6.3 Reputation as Temporal Abstraction

**Reputation** = compressed representation of an agent’s behavioral history, used to predict future behavior.

Reputation is a *temporal abstraction*—aggregating past behavior into action-relevant summary. It solves an information problem: in large groups, direct experience with everyone is impossible; reputation provides indirect information.

Social emotions track reputation:

- Shame responds to reputation threat
- Pride responds to reputation enhancement
- Guilt responds to behavior that could damage reputation

**Theoretical connection:** Reputation links Paper 7 (temporal abstraction) to Paper 9 (social abstraction). Reputation is where temporal and social abstraction meet.

### 6.4 Generality to Artificial Systems

These dynamics are not biologically specific. Any multi-agent system with:

- Resource constraints
- Repeated interaction
- Reputation tracking
- Cooperation opportunities

…faces the same game-theoretic structure. If artificial agents in such environments develop internal states that function like social emotions, it would support the framework’s generality.

**Existing evidence:** Multi-agent systems show emergent cooperation and competition (Leibo et al., 2017), reputation-like effects (Eccles et al., 2019), and strategy differentiation resembling personality (Jaderberg et al., 2019). Whether these involve internal states functionally analogous to emotions remains unclear.

-----

## 7. Recursive Self-Reference in Social Cognition

### 7.1 The Recursive Structure

Social cognition involves applying the abstraction operation recursively:

**Level 0:** Self-state (I want X)
**Level 1:** Other-abstraction (You want Y)
**Level 2:** Other’s-abstraction-of-self (You think I want X’)
**Level 3:** Self’s-abstraction-of-other’s-abstraction-of-self (I think you think I want X’)
**…**

Each level applies abstraction to the previous level’s output. This is the compositional property (Paper 2) applied recursively.

### 7.2 Connection to Self-Referential Computation (Paper 3)

Paper 3 (Danan, 2025c) argued that self-referential computation becomes necessary when a system’s optimal output depends on its own state, and that state is too complex to represent directly.

Social cognition extends this: your optimal output depends not only on your own state but on *others’ representations of your state*. Social emotions are what happens when self-referential computation must include others’ models of you.

**Theoretical claim:** Social emotions are *socially-extended self-reference*. The self-model must include not just internal state but social position—how others abstract you.

### 7.3 Implications

**Why social emotions feel self-relevant:** They are. They involve abstraction over self-as-socially-represented, not just self-as-internally-experienced.

**Why social rejection hurts:** Your self-model includes social standing. Negative social evaluation updates the self-model in threat-registering ways.

**Why reputation matters:** Reputation is others’ abstraction of you, which constrains your action possibilities and viability. Tracking reputation is tracking a component of your extended self-model.

-----

## 8. Neural Implementation

### 8.1 Integration of Self and Other Processing

Social emotions require integrating self-representation and other-representation:

**Medial prefrontal cortex (mPFC):** Implicated in both self-referential processing and mentalizing (Amodio & Frith, 2006; Mitchell et al., 2006). May support the *integration* of self and other abstractions.

**Temporoparietal junction (TPJ):** Involved in distinguishing self from other and in theory of mind (Saxe & Kanwisher, 2003). May support representing *others’ representations* (Level 2+ abstraction).

**Anterior insula and ACC:** Involved in interoception and self-awareness (Craig, 2009). Provide the *self-state* input to social-emotional integration.

**Established finding:** Social emotions activate overlapping networks rather than discrete modules (Bastin et al., 2016). This is consistent with social emotions arising from *compositional integration* rather than dedicated circuitry.

### 8.2 Recursive Processing

Recursive abstraction (modeling others’ models) may require:

**Prefrontal hierarchical organization:** Rostral PFC supports increasingly abstract representations (Badre & D’Esposito, 2009). Recursive social abstraction may map onto this rostral-caudal gradient.

**Working memory:** Holding multiple levels of abstraction simultaneously requires working memory capacity. Working memory limits may constrain recursion depth.

**Established finding:** Performance on higher-order mentalizing tasks correlates with working memory capacity and PFC function (Kinderman et al., 1998; Stiller & Dunbar, 2007).

-----

## 9. Predictions and Falsification

### 9.1 Computational Predictions

**Prediction 1:** Social emotion capacity should correlate with recursive abstraction capacity. Individuals/systems with better performance on recursive mentalizing tasks should show more differentiated social emotions.

*Test:* Correlate mentalizing depth with social emotion differentiation and intensity.

**Prediction 2:** Social emotions should be more cognitively demanding than basic emotions. Under cognitive load, social emotions should be more disrupted.

*Test:* Compare emotion processing under load for social vs. basic emotions.

**Prediction 3:** Social emotions should depend on intact theory of mind. Impairments in mentalizing should selectively impair social emotions relative to basic emotions.

*Status:* Partially supported (Baron-Cohen et al., 1985; Hobson et al., 2006). More specific tests needed.

### 9.2 Artificial System Predictions

**Prediction 4:** Multi-agent RL systems with explicit self-models, other-models, and reputation tracking should develop social-emotion-like internal states. Systems without these features should not.

*Test:* Analyze internal representations in multi-agent systems varying in architectural features.

**Prediction 5:** LLMs should show dissociable social emotion performance: good at labeling/classification, poor at appropriateness judgments, dynamics, and embodied correlates.

*Test:* Evaluate LLMs on benchmarks distinguishing representational from grounded social emotion capacities.

**Prediction 6:** Embodied multi-agent AI systems (robots interacting with other robots under resource constraints) should develop more human-like social-emotional patterns than disembodied systems.

*Test:* Compare social dynamics in embodied vs. disembodied multi-agent systems.

### 9.3 Scaling Predictions

**Prediction 7:** Across biological species, social emotion complexity should correlate with neural indices of abstraction capacity and recursive processing (prefrontal volume, connectivity).

*Test:* Comparative analysis of social behavior complexity vs. neural architecture.

**Prediction 8:** Within humans, individual differences in social emotion intensity should correlate with integration between interoceptive and mentalizing networks.

*Test:* Neuroimaging studies correlating social emotion measures with functional connectivity.

### 9.4 Falsification Criteria

The framework would be challenged by:

1. **Social emotions without recursive abstraction:** If social emotions are fully intact in individuals/systems without recursive mentalizing capacity, the recursive abstraction claim is wrong.
1. **No scaling pattern:** If social complexity does not correlate with abstraction/recursion capacity across species or systems, the scaling claim is unsupported.
1. **Disembodied systems with full social emotion understanding:** If LLMs show complete human-like social emotion competence without multi-agent embedding, the embodiment/embedding requirement is wrong.
1. **No multi-agent system analogs:** If no artificial multi-agent system ever develops social-emotion-like internal states despite meeting the architectural requirements, the framework may be biologically specific despite claims of generality.

-----

## 10. Implications

### 10.1 For Understanding Social Cognition

Social emotions are not separate from general cognition—they are the abstraction primitive applied to multi-agent contexts, combined recursively and compositionally.

This explains:

- Why social emotions require theory of mind (recursive abstraction over others)
- Why they are cognitively demanding (composition is costly)
- Why they develop late (prerequisites must be in place)
- Why they feel so important (they concern viability in social environments)

### 10.2 For Artificial Intelligence

**Social AI requires multi-agent grounding.** Systems trained only on text about social emotions cannot develop the computational structures underlying social emotions. They can pattern-match on descriptions but cannot represent multi-agent dynamics in action-relevant format.

**Architectural implications:** Social AI should be developed in:

- Multi-agent environments (not single-agent fine-tuning)
- With resource constraints (creating genuine interdependence)
- With reputation dynamics (enabling temporal abstraction over social history)
- With recursive modeling capacity (architectures supporting self/other/other’s-model-of-self)

### 10.3 For the Abstraction-Intelligence Framework

This paper extends the framework to its multi-agent form:

1. **Abstraction is primitive** (Paper 1)
1. **Abstraction composes** (Paper 2) → enables complex representations
1. **Abstraction becomes self-referential at complexity** (Paper 3) → consciousness
1. **Self-world is foundational** (Paper 5) → grounds all abstraction
1. **Experience is embedded information format** (Paper 6) → explains qualia
1. **Time requires embodied abstraction** (Paper 7) → explains temporal cognition
1. **Emotions are self-world integration** (Paper 8) → explains affect
1. **Social dynamics are multi-agent abstraction** (Paper 9) → explains social cognition

The framework scales from basic cognition to social cognition using the same primitive operation (abstraction) with increasing compositional and recursive complexity.

### 10.4 For Understanding Intelligence Across Substrates

The scaling principle suggests intelligence is substrate-independent but constraint-dependent:

- Any system with abstraction capacity can represent environments
- Any system with compositional abstraction can build complex representations
- Any system with recursive abstraction can model self and others
- Any system with multi-agent embedding can develop social-emotion-like dynamics

Whether implemented in carbon or silicon, neurons or transistors, the computational requirements are the same. What differs is implementation, not structure.

-----

## 11. Limitations and Open Questions

### 11.1 Moral Emotions

Moral emotions (moral outrage at injustice to others, moral elevation at virtue) may extend beyond self-interest. The framework handles this if “viability” includes group welfare or internalized norms—but this requires further development.

### 11.2 Cultural Variation

Social emotions are culturally shaped (Mesquita & Frijda, 1992). The framework predicts universal computational structure with culturally-variable content (what triggers shame, what counts as pride-worthy). But the boundary between structure and content needs empirical specification.

### 11.3 The Emergence Question

At what point does a multi-agent system “have” social emotions versus merely “simulate” them? This is the hard problem applied to social emotions. The framework suggests the distinction may not be well-formed: if the computational structure is present and functional, the system has social emotions (functionally defined).

### 11.4 Empirical Gaps

The predictions about artificial systems are currently untested. Multi-agent RL research has not systematically examined internal states for social-emotion-like structure. This is a priority for future work.

-----

## 12. Conclusion

What are social emotions?

They are the abstraction primitive applied to multi-agent environments, composed recursively to represent how others represent you, and formatted for action under resource constraints.

This is not a special mechanism. It is the same abstraction operation underlying all intelligence (Paper 1), applied compositionally (Paper 2), self-referentially (Paper 3), to the self-world distinction (Paper 5), integrated with embodied experience (Papers 6-8), and extended to include other selves.

The pattern scales:

- Atoms abstract over other atoms (via physical forces)
- Cells abstract over other cells (via chemical signals)
- Neurons abstract over other neurons (via synaptic transmission)
- Organisms abstract over other organisms (via perception and inference)
- Groups abstract over other groups (via institutions and norms)

At each level, units use abstracted information about other units to guide behavior under resource constraints. Social emotions are how sufficiently complex embedded agents represent multi-agent dynamics in action-relevant format.

They are not uniquely biological. Any embedded agent meeting the computational requirements—self-model, other-model, recursive abstraction, compositional integration, multi-agent context, resource constraints—should develop functional analogs.

Social emotions are basic emotions in a world that contains other selves.

Abstraction is all you need. Even for love and shame.

-----

## References

Ambady, N., & Rosenthal, R. (1992). Thin slices of expressive behavior as predictors of interpersonal consequences: A meta-analysis. *Psychological Bulletin*, 111(2), 256–274.

Amodio, D. M., & Frith, C. D. (2006). Meeting of minds: The medial frontal cortex and social cognition. *Nature Reviews Neuroscience*, 7(4), 268–277.

Badre, D., & D’Esposito, M. (2009). Is the rostro-caudal axis of the frontal lobe hierarchical? *Nature Reviews Neuroscience*, 10(9), 659–669.

Baker, B., Kanitscheider, I., Marber, T., Wu, Y., Gray, S., & Sutskever, I. (2020). Emergent tool use from multi-agent autocurricula. *International Conference on Learning Representations*.

Baron-Cohen, S., Leslie, A. M., & Frith, U. (1985). Does the autistic child have a “theory of mind”? *Cognition*, 21(1), 37–46.

Bastin, C., Harrison, B. J., Davey, C. G., Moll, J., & Whittle, S. (2016). Feelings of shame, embarrassment and guilt and their neural correlates: A systematic review. *Neuroscience & Biobehavioral Reviews*, 71, 455–471.

Craig, A. D. (2009). How do you feel—now? The anterior insula and human awareness. *Nature Reviews Neuroscience*, 10(1), 59–70.

Danan, H. (2025a). Abstraction is all you need: A unifying framework for intelligence across substrates. *Working paper*.

Danan, H. (2025b). Abstraction beyond compression: Compositionality as the distinguishing operation. *Working paper*.

Danan, H. (2025c). Recursive abstraction: When computation requires self-reference. *Working paper*.

Danan, H. (2025e). Self and world: The foundational abstraction. *Working paper*.

Danan, H. (2025f). The hard problem dissolved: Why experience is the format of embedded information. *Working paper*.

Danan, H. (2025g). Time as embodied abstraction: Why disembodied systems struggle with temporal reasoning. *Working paper*.

Danan, H. (2025h). Emotion as embedded information: Why feelings are the format of self-world relations. *Working paper*.

Dawes, R. M. (1980). Social dilemmas. *Annual Review of Psychology*, 31(1), 169–193.

Dunbar, R. I. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469–493.

Eccles, T., Bachrach, Y., Lever, G., Lazaridou, A., & Graepel, T. (2019). Biases for emergent communication in multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*, 32.

Fehr, E., & Gächter, S. (2002). Altruistic punishment in humans. *Nature*, 415(6868), 137–140.

Frank, R. H. (1988). *Passions Within Reason: The Strategic Role of the Emotions*. Norton.

Hobson, R. P., Chidambi, G., Lee, A., & Meyer, J. (2006). Foundations for self-awareness: An exploration through autism. *Monographs of the Society for Research in Child Development*, 71(2), vii–166.

Jaderberg, M., Czarnecki, W. M., Dunning, I., Marris, L., Lever, G., Castañeda, A. G., … & Graepel, T. (2019). Human-level performance in 3D multiplayer games with population-based reinforcement learning. *Science*, 364(6443), 859–865.

Kinderman, P., Dunbar, R., & Bentall, R. P. (1998). Theory-of-mind deficits and causal attributions. *British Journal of Psychology*, 89(2), 191–204.

Kollock, P. (1998). Social dilemmas: The anatomy of cooperation. *Annual Review of Sociology*, 24(1), 183–214.

Leibo, J. Z., Zambaldi, V., Lanctot, M., Marecki, J., & Graepel, T. (2017). Multi-agent reinforcement learning in sequential social dilemmas. *Proceedings of the 16th Conference on Autonomous Agents and MultiAgent Systems*, 464–473.

Mesquita, B., & Frijda, N. H. (1992). Cultural variations in emotions: A review. *Psychological Bulletin*, 112(2), 179–204.

Mitchell, J. P., Macrae, C. N., & Banaji, M. R. (2006). Dissociable medial prefrontal contributions to judgments of similar and dissimilar others. *Neuron*, 50(4), 655–663.

Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in “theory of mind.” *NeuroImage*, 19(4), 1835–1842.

Stiller, J., & Dunbar, R. I. (2007). Perspective-taking and memory capacity predict social network size. *Social Networks*, 29(1), 93–104.

Trivers, R. L. (1971). The evolution of reciprocal altruism. *The Quarterly Review of Biology*, 46(1), 35–57.

Willis, J., & Todorov, A. (2006). First impressions: Making up your mind after a 100-ms exposure to a face. *Psychological Science*, 17(7), 592–598.

Zahn, R., Moll, J., Paiva, M., Garrido, G., Krueger, F., Huey, E. D., & Grafman, J. (2009). The neural basis of human social values: Evidence from functional MRI. *Cerebral Cortex*, 19(2), 276–283.

-----

*This paper is part of a theoretical program on abstraction as the fundamental primitive of intelligence. It addresses how the self-world framework scales to multi-agent environments.*

*Answer: Social dynamics emerge when abstraction is applied recursively across agents. Social emotions are composed, recursive abstractions formatted for multi-agent action.*

*Abstraction is all you need. Even for love and shame.*

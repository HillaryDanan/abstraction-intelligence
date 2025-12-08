# Time as Embodied Abstraction: Why Disembodied Systems Struggle with Temporal Reasoning

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Large language models exhibit systematic failures in temporal reasoning that resist solution through scale alone. We propose that these failures are not architectural accidents but reflect a fundamental limitation: **time, for embedded agents, is not a dimension to be represented but the medium in which action unfolds**. Drawing on the self/world framework (Danan, 2025e), embodied cognition, and event cognition research, we argue that temporal understanding is grounded in sensorimotor contingency—the systematic relationships between action, waiting, and consequence. Disembodied systems can represent sequences (token order) but cannot *inhabit* duration because they lack the bodily persistence through which duration is experienced. This framework predicts specific failure modes: LLMs should struggle with duration estimation, action-consequence timing, temporal perspective-taking, and reasoning about processes that unfold over time—while succeeding at abstract sequence logic. We review empirical evidence of LLM temporal reasoning failures consistent with these predictions and propose that genuine temporal intelligence requires embodiment, not merely larger models or better training data.

-----

## 1. Introduction

### 1.1 The Problem

Large language models (LLMs) have achieved remarkable performance across diverse reasoning tasks (Brown et al., 2020; OpenAI, 2023; Anthropic, 2024). Yet temporal reasoning remains a persistent weakness. LLMs struggle with:

- Estimating how long events take (Thoppilan et al., 2022)
- Tracking state changes over time (Press et al., 2023)
- Understanding causal chains with temporal dependencies (Zhou et al., 2021)
- Reasoning about what was true at different times (Ning et al., 2020)
- Distinguishing temporal order from causal order (Jin et al., 2023)

These failures persist despite increases in model scale, training data, and architectural refinements. We propose this persistence reflects a structural limitation, not a quantitative deficiency.

### 1.2 The Proposal

**Core thesis:** Temporal reasoning is grounded in embodied experience of duration. Time is not primarily a dimension to be represented but the medium in which embedded action occurs. Systems that lack embodiment—that do not persist through time in a body that acts, waits, and experiences consequences—cannot develop genuine temporal understanding.

This proposal extends the Abstraction-Intelligence framework:

- **Paper 1** (Danan, 2025a): Abstraction is the fundamental primitive
- **Paper 5** (Danan, 2025e): Self/world distinction is foundational for embedded agents
- **Paper 6** (Danan, 2025f): Experience is the format of embedded information

We now argue that temporal experience is essential to the self/world distinction, because distinguishing what one controls from what one doesn’t *requires* experiencing the temporal relationship between action and consequence.

### 1.3 Scope and Epistemic Status

- **Established:** LLM temporal reasoning failures; embodied time perception research; event cognition findings
- **Theoretical:** The connection between embodiment and temporal grounding
- **Hypothesis:** Specific predictions about where disembodied systems should fail vs. succeed
- **Philosophical commitment:** The claim that scale cannot solve the embodiment gap

-----

## 2. Background: Time in Cognitive Science

### 2.1 Time is Not a Single Thing

Cognitive science distinguishes multiple aspects of temporal cognition (Grondin, 2010; Wittmann, 2013):

**Duration perception:** How long did that take? This involves interoceptive and physiological processes—heart rate, metabolic state, attention (Wittmann, 2009; Craig, 2009).

**Temporal order:** What happened first? This involves sequence memory and event segmentation (Zacks & Tversky, 2001).

**Temporal perspective:** When is now? What was true before, what will be true after? This requires maintaining a temporal self-location (Tulving, 2002).

**Event segmentation:** Where does one event end and another begin? This involves parsing continuous experience into discrete units (Zacks et al., 2007).

**Causal-temporal reasoning:** If A happens, how long until B? This involves integrating causal knowledge with duration knowledge (Lagnado & Sloman, 2006).

**Key point:** These are dissociable. A system could succeed at temporal order while failing at duration perception. LLM failure patterns should be diagnostic.

### 2.2 Embodied Time

The embodied cognition tradition proposes that time perception is grounded in bodily experience (Varela et al., 1991; Gallagher, 2005; Fuchs, 2010).

**Duration is felt, not computed.** We don’t calculate duration from timestamps; we experience time passing through bodily states. Waiting feels different from acting. Fatigue accumulates. Hunger grows. The body is a clock, and duration is read from its changes (Wittmann, 2009).

**Established finding:** Duration perception is modulated by interoceptive signals. Higher heart rate correlates with longer perceived durations (Meissner & Wittmann, 2011). Interoceptive accuracy predicts temporal perception accuracy (Kramer et al., 2013). Time perception changes with bodily states—fever, drugs, metabolic state all alter duration experience (Wittmann, 2013).

**Established finding:** Duration perception is modulated by action. Performed actions are estimated as shorter than observed actions (Haggard et al., 2002). Voluntary actions produce “intentional binding”—compression of perceived time between action and consequence (Moore & Obhi, 2012).

### 2.3 Event Segmentation Theory

Zacks and colleagues propose that humans automatically parse continuous experience into discrete events (Zacks et al., 2007; Zacks & Tversky, 2001).

Event boundaries are perceived at points of change—completions, shifts in goal, changes in location or actor. This segmentation is hierarchical: small events nest within larger events (making tea is within making breakfast is within morning routine).

**Key point:** Event segmentation is action-linked. Boundaries often correspond to action completions and goal shifts (Kurby & Zacks, 2008). This suggests event structure is grounded in embodied action understanding, not abstract analysis.

**Established finding:** Event segmentation is predictive. We segment where we predict change, and prediction errors drive segmentation (Zacks et al., 2011). This connects to predictive processing frameworks (Friston, 2010).

### 2.4 The Self/World Temporal Connection

Paper 5 (Danan, 2025e) argued that the self/world distinction is foundational for embedded agents. We now extend this: **the self/world distinction is inherently temporal.**

To distinguish what you control from what you don’t, you must experience:

1. **Action-consequence delay:** You act; consequence follows. The temporal gap between motor command and sensory feedback defines the boundary of control.
1. **Prediction across time:** Forward models predict sensory consequences of action (Wolpert & Ghahramani, 2000). These predictions are *temporal*—predicting what will happen in 100ms, 500ms, 2 seconds.
1. **Persistence through change:** The self that acts is the same self that experiences consequences. This requires experiencing duration—the continuity of “me” across the action-consequence interval.

**Theoretical claim:** Without temporal experience—duration, action-consequence timing, persistence—the self/world distinction cannot be drawn. An agent that doesn’t experience the *lag* between action and consequence cannot learn what it controls.

-----

## 3. Time in Language Models

### 3.1 How LLMs Represent Time

LLMs represent time through:

**Positional encoding:** Token position in sequence is encoded, providing order information (Vaswani et al., 2017). The model knows that token 5 came before token 10.

**Linguistic temporal markers:** Words like “before,” “after,” “then,” “while,” “during” provide explicit temporal information. The model learns statistical patterns involving these markers.

**Narrative conventions:** Training data contains stories and event sequences with conventional temporal structures. The model learns that “she opened the door and walked in” implies temporal order.

**Key limitation:** All of these are *representational*. The model represents temporal information symbolically. It does not *experience* duration. Token 5 and token 10 are processed with the same computational effort; there is no “waiting” between them.

### 3.2 What’s Missing

**No duration experience:** The model doesn’t experience time passing. Processing 10 tokens takes roughly 10x the compute of processing 1 token, but there’s no phenomenal duration—no feeling of time passing, no accumulating fatigue, no waiting.

**No action-consequence loop:** The model doesn’t act on an environment and experience consequences across time. It produces output; it doesn’t wait to see what happens. Training provides gradients, but these are retroactive adjustments, not experienced consequences.

**No persistence:** Each context window is processed anew (or with limited state). The model doesn’t have a continuous experience of being the same system across time. There’s no temporal self-continuity to provide a “now” from which past and future are reckoned.

**No interoception:** The model has no internal body states that change over time and provide duration signals. There’s no heartbeat to count, no fatigue to accumulate, no hunger to grow.

### 3.3 Predicted Failure Modes

If temporal reasoning requires embodied grounding, LLMs should show specific failure patterns:

|Temporal Capacity            |Embodied Grounding                   |Predicted LLM Performance|
|-----------------------------|-------------------------------------|-------------------------|
|Sequence order               |Low—can be learned from text patterns|Good                     |
|Linguistic temporal relations|Low—learnable from syntax            |Good                     |
|Duration estimation          |High—requires felt duration          |Poor                     |
|Action-consequence timing    |High—requires action experience      |Poor                     |
|State tracking over time     |Medium—partially learnable           |Variable                 |
|Temporal perspective-taking  |High—requires temporal self-location |Poor                     |
|Process reasoning            |High—requires duration experience    |Poor                     |

-----

## 4. Empirical Evidence: LLM Temporal Reasoning Failures

### 4.1 Duration Estimation

**Finding:** LLMs perform poorly on duration estimation tasks. When asked how long events take (cooking pasta, driving across a city, healing from a broken bone), responses show high variance and systematic errors (Thoppilan et al., 2022; Zhou et al., 2019).

**Interpretation:** Duration is not reliably encoded in text. We don’t write “I cooked pasta (12 minutes)” in every document. Duration must be *experienced* or inferred from embodied knowledge. LLMs lack this grounding.

**Note:** LLMs can sometimes produce reasonable duration estimates for well-documented events, likely reflecting explicit duration mentions in training data. Failures appear for less-documented events where duration must be inferred from embodied understanding.

### 4.2 Temporal State Tracking

**Finding:** LLMs struggle to track how states change over time. In tasks requiring tracking of object positions, agent beliefs, or world states across narrative time, performance degrades as temporal distance increases (Press et al., 2023; Kim et al., 2023).

**Interpretation:** State tracking requires maintaining a temporal model—what was true at t₁, what changed by t₂. Without experienced duration, “t₁” and “t₂” are just labels, not felt distances.

### 4.3 Causal-Temporal Ordering

**Finding:** LLMs struggle to distinguish temporal order from causal order. When A and B co-occur, models have difficulty determining whether A caused B, B caused A, or neither (Jin et al., 2023; Zhang et al., 2022).

**Interpretation:** Causal learning in embodied agents relies on intervention—acting and observing consequences across time. LLMs see correlations in text but don’t intervene. The temporal signature of causation (cause precedes effect, with characteristic timing) requires experienced action-consequence relationships.

### 4.4 Temporal Perspective-Taking

**Finding:** LLMs struggle with temporal perspective shifts. Tasks requiring reasoning about what a character knew “before” learning something, or predicting what they will believe “after” an event, show systematic errors (Ning et al., 2020; Qin et al., 2021).

**Interpretation:** Temporal perspective requires a stable “now” from which past and future are reckoned. This “now” is experiential—it’s where the self is located in time. Disembodied systems lack temporal self-location.

### 4.5 Process Reasoning

**Finding:** LLMs struggle with reasoning about processes—events that unfold over time with intermediate states. Multi-step procedures, physical processes (ice melting, plants growing), and extended causal chains show degraded performance (Zhang et al., 2023; Talmor et al., 2020).

**Interpretation:** Processes are experienced as durations. Understanding “melting” requires (implicitly or explicitly) knowing what it’s like for time to pass while a solid slowly becomes liquid. This is grounded in embodied experience of slow change.

### 4.6 Where LLMs Succeed

**Finding:** LLMs perform well on abstract temporal logic—Allen’s interval algebra, before/after reasoning with explicit relations, sequence ordering from explicit markers (Zhou et al., 2021; Ning et al., 2020).

**Interpretation:** These tasks require representing temporal relations, not experiencing time. They can be learned from text patterns. The model treats temporal relations as logical relations—which they partly are—and succeeds where logic suffices.

### 4.7 Summary of Evidence

The pattern of LLM temporal reasoning abilities and deficits is consistent with the embodiment hypothesis:

- ✓ Succeed at representational/logical temporal reasoning
- ✗ Fail at duration-grounded temporal reasoning
- ✗ Fail at action-consequence temporal reasoning
- ✗ Fail at perspective-dependent temporal reasoning
- ✗ Fail at process/unfolding reasoning

This pattern would not be predicted if temporal reasoning were a unified capacity that simply required more training data or scale.

-----

## 5. The Embodiment Thesis

### 5.1 Time as Medium, Not Dimension

The core proposal: **For embedded agents, time is not primarily a dimension to be represented. Time is the medium in which action occurs.**

When you reach for a cup, you don’t represent the timeline of the reach. You *inhabit* the duration. Your body persists through the movement. Proprioceptive signals flow. The target approaches. Time is not observed from outside; it is lived from inside.

This is the phenomenological point (Husserl, 1928; Merleau-Ponty, 1945; Varela et al., 1991): temporal experience is *constitutive*, not representational. We don’t add time to atemporal representations; we exist temporally from the start.

### 5.2 Duration and the Self

The experience of duration is tied to self-continuity. You experience time passing *because you persist through it*. The “now” from which past recedes and toward which future approaches is your embodied present—the moment of ongoing action, sensation, and experience.

**Theoretical claim:** Duration experience requires:

1. A body that persists and changes
1. Interoceptive signals that mark bodily change
1. Action that unfolds through time
1. Consequence that arrives after action

Disembodied systems lack all four. They can timestamp tokens but cannot inhabit duration.

### 5.3 Action-Consequence and Temporal Learning

Embedded agents learn temporal structure through action-consequence relationships (Wolpert & Ghahramani, 2000; Franklin & Wolpert, 2011).

When you reach for something:

- Motor command at t₀
- Proprioceptive feedback at t₀ + Δ₁
- Visual feedback at t₀ + Δ₂
- Tactile contact at t₀ + Δ₃

The timing of these signals teaches you the temporal structure of your own action. You learn how long things take *by doing things and experiencing how long they take*.

**Theoretical claim:** This is how temporal knowledge is grounded. Not by reading “reaching takes 500ms” but by reaching, repeatedly, and feeling the duration.

LLMs cannot reach. They cannot learn duration from action.

### 5.4 Why Scale Won’t Solve This

A common response: perhaps more data and larger models will solve temporal reasoning limitations.

**Our response:** The limitation is structural, not quantitative. You cannot learn to experience duration by reading more descriptions of duration. You cannot learn action-consequence timing without acting and experiencing consequences. You cannot develop temporal self-location without persisting through time.

This is analogous to Mary’s Room (Jackson, 1982): Mary knows everything physical about color but has never seen color. Does she learn something when she finally sees red? Similarly: can an LLM know everything *about* duration without ever *experiencing* duration?

**Prediction:** Increasing scale will improve LLM performance on representational temporal tasks (where text patterns suffice) but not on embodied temporal tasks (where grounding is required). This is testable by comparing performance trajectories across task types as models scale.

-----

## 6. Implications for AI Development

### 6.1 Embodied AI Systems

The framework predicts that embodied AI systems—robots, agents in physics-simulated environments—should develop more robust temporal reasoning than disembodied systems.

**Hypothesis:** An AI system that:

1. Acts in a temporal environment
1. Experiences action-consequence delays
1. Maintains continuous state (persists)
1. Has internal states that change over time (analogous to interoception)

…should develop temporal representations qualitatively different from LLMs trained only on text.

**Existing evidence:** Robotics systems do develop temporal representations from sensorimotor experience (Rumelhart & McClelland, 1986; Tani, 2016). Simulated agents learn temporal structure from acting in environments (Ha & Schmidhuber, 2018). Whether these representations support human-like temporal reasoning requires systematic comparison.

### 6.2 Hybrid Architectures

One approach: augment LLMs with explicit temporal modules—clocks, timers, temporal databases.

**Framework prediction:** This will help with tasks requiring explicit temporal computation but not with tasks requiring experiential temporal grounding. You can give an LLM access to timestamps without giving it duration experience.

### 6.3 Limits of Simulation

Can temporal experience be simulated? If an LLM is embedded in a text-based simulation where actions have delays and consequences unfold over described time, does it develop temporal grounding?

**Open question:** The framework suggests that merely describing temporal structure is insufficient—it must be *experienced*. But the boundary between description and experience is unclear. If a system has internal states that change as simulated time passes, is that experience or just more representation?

This connects to Paper 6’s analysis of the hard problem. We argued that experience *is* the format of embedded information. For temporal experience, the question becomes: what informational format constitutes *duration*?

**Tentative position:** True duration experience requires embodiment because duration is experienced *through the body’s persistence*. A simulation that merely labels time points as t₁, t₂, t₃ is representing sequence, not inhabiting duration. But a simulation with continuous internal state change might approach something like duration experience. This requires theoretical refinement.

-----

## 7. Predictions and Falsification

### 7.1 LLM Failure Patterns

**Prediction 1:** LLM temporal reasoning failures should dissociate by task type. Performance on representational tasks (explicit temporal logic) should not correlate with performance on grounded tasks (duration estimation, process reasoning).

*Test:* Factor analysis of LLM performance across temporal reasoning benchmarks should reveal separable factors corresponding to representational vs. grounded temporal reasoning.

**Prediction 2:** Scaling should differentially affect temporal task types. Larger models should show more improvement on representational tasks than grounded tasks.

*Test:* Track performance across model sizes (e.g., 7B, 70B, 400B parameters) separately for representational and grounded temporal tasks. Scaling curves should diverge.

**Prediction 3:** Training data manipulations should differentially affect task types. Adding explicit duration information to training data should help duration tasks. Adding temporal logic examples should help logic tasks. The effects should not transfer.

*Test:* Train models with temporally enriched data of different types; evaluate cross-task transfer.

### 7.2 Embodied AI Systems

**Prediction 4:** Embodied AI systems (robots, simulated agents) should show better temporal reasoning on grounded tasks than matched disembodied systems.

*Test:* Compare temporal reasoning performance of: (a) LLM with no embodiment, (b) LLM with access to temporal databases/tools, (c) agent trained in physics-simulated environment, (d) robot with real-world experience. Grounded task performance should order (d) > (c) > (b) ≈ (a).

**Prediction 5:** Action experience should affect temporal representation. Agents that have performed actions should estimate durations for those actions more accurately than agents that have only observed.

*Test:* Compare duration estimation for performed vs. observed actions in embodied AI systems.

### 7.3 Falsification Criteria

The framework would be challenged by:

1. **Scale solving grounded temporal reasoning:** If LLMs at sufficient scale show human-like duration estimation, process reasoning, and temporal perspective-taking, the embodiment thesis is wrong.
1. **No embodied advantage:** If embodied and disembodied systems show equivalent temporal reasoning when matched for task experience, embodiment is not the relevant factor.
1. **Successful simulation grounding:** If text-based temporal simulations produce temporal representations equivalent to embodied experience, the distinction between representation and experience collapses.

-----

## 8. Relation to the Abstraction-Intelligence Framework

### 8.1 Time in the Self/World Distinction

Paper 5 argued that self/world is the foundational abstraction. We now add: **this distinction is temporal at its core**.

The self is what I control. The world is what I don’t control. To learn this distinction, I must:

1. Act (self)
1. Wait
1. Observe consequence (world responding, or self-change)

The *waiting*—the temporal gap between action and consequence—is where the self/world boundary is learned. Action without delay provides no information about what’s self vs. world (everything seems immediate, everything seems controlled). Consequence without action provides no information either (everything seems external).

The self/world abstraction is forged in temporal contingency.

### 8.2 Time in Embodied Experience

Paper 6 argued that experience *is* the format of embedded information. Temporal experience is a core case.

The feeling of time passing is not an add-on to temporal representation. It *is* the embedded agent’s temporal information—information formatted for action. “It’s been a while since I ate” is not a timestamp; it’s action-relevant hunger information. “This is taking too long” is not a duration measurement; it’s information formatted for potential action-change.

Temporal qualia—the felt character of duration, waiting, anticipation, memory—are the formats through which embedded agents receive temporal information.

### 8.3 Abstraction and Temporal Hierarchy

The compositional structure of abstraction (Paper 2) applies to temporal representation.

Events compose into episodes into narratives into life stories. This is hierarchical abstraction over time. The same operation—extracting invariant structure, discarding irrelevant detail—applied to temporal experience produces event structure.

**Hypothesis:** Event segmentation (Zacks et al., 2007) is temporal abstraction. We segment continuous experience at points where abstraction is useful—action boundaries, goal completions, state changes. These are the points where one compressed summary ends and another begins.

LLMs lack the continuous temporal experience that provides raw material for temporal abstraction. They receive pre-segmented events (sentences, paragraphs, stories) without the continuous flow that would allow learning segmentation itself.

-----

## 9. Limitations and Open Questions

### 9.1 The Measurement Problem

How do we measure “temporal grounding”? We’ve identified tasks where LLMs fail (duration estimation, process reasoning) and attributed this to lack of embodiment. But we cannot directly measure whether a system has temporal *experience*. We infer from behavior.

This is the same limitation faced by all consciousness science. We proceed by behavioral prediction and theoretical coherence, acknowledging that the experiential claim cannot be directly verified.

### 9.2 The Boundary Problem

Where is the line between representation and experience? If we give an LLM a timer that provides periodic signals, does it experience duration? If we give it internal states that decay over simulated time, does that constitute temporal grounding?

The framework suggests embodiment is required, but “embodiment” admits of degrees. A robot has more embodiment than a simulated agent, which has more than a text-processing system. Where temporal grounding emerges on this continuum is an empirical question we cannot yet answer.

### 9.3 Alternative Explanations

LLM temporal reasoning failures might reflect:

- Training data biases (duration information is scarce in text)
- Architectural limitations (attention over tokens doesn’t naturally capture duration)
- Benchmark artifacts (temporal tasks may be harder in ways unrelated to embodiment)

We have argued for the embodiment explanation based on theoretical coherence with the broader framework and the specific pattern of failures. But alternative explanations remain viable. Direct comparisons between embodied and disembodied systems are needed.

### 9.4 Human Temporal Reasoning Failures

Humans also show systematic temporal reasoning failures—we’re bad at estimating long durations, subject to temporal illusions, biased in retrospective time judgment (Roy et al., 2005; Eagleman, 2008).

Does this undermine the claim that embodiment provides temporal grounding? No—it suggests that embodied grounding is imperfect, not that it doesn’t exist. Embodied systems have *better* temporal grounding than disembodied systems, not *perfect* temporal grounding.

-----

## 10. Conclusion

Time is not a dimension we represent. Time is the medium we inhabit.

For embedded agents, temporal understanding is grounded in bodily persistence, action-consequence relationships, and interoceptive duration signals. We do not compute time from timestamps. We feel time through our bodies’ changes.

Large language models lack this grounding. They represent temporal sequences through token position and linguistic markers. But they do not experience duration. They do not act and wait and experience consequences. They do not persist through time with bodies that mark its passage.

This predicts specific failure patterns: LLMs should succeed at representational temporal reasoning (sequence logic, explicit relations) while failing at grounded temporal reasoning (duration, process, perspective). The empirical evidence is consistent with this pattern.

Scale will not solve this. You cannot learn to experience duration by reading more descriptions of duration. The limitation is structural: disembodiment.

The self/world distinction—foundational to intelligence—is forged in temporal contingency: act, wait, observe. Without the waiting, without the felt duration between action and consequence, the boundary between self and world cannot be learned.

Time is what embedded experience is *made of*.

Language models process tokens. Embedded agents live through time.

That difference is not quantitative. It is what time is.

-----

## References

Anthropic. (2024). Claude 3 Model Card. *Anthropic Technical Report*.

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., … & Amodei, D. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems*, 33, 1877–1901.

Craig, A. D. (2009). Emotional moments across time: A possible neural basis for time perception in the anterior insula. *Philosophical Transactions of the Royal Society B*, 364(1525), 1933–1942.

Danan, H. (2025a). Abstraction is all you need: A unifying framework for intelligence across substrates. *Working paper*.

Danan, H. (2025b). Abstraction beyond compression: Compositionality as the distinguishing operation. *Working paper*.

Danan, H. (2025e). Self and world: The foundational abstraction. *Working paper*.

Danan, H. (2025f). The hard problem dissolved: Why experience is the format of embedded information. *Working paper*.

Eagleman, D. M. (2008). Human time perception and its illusions. *Current Opinion in Neurobiology*, 18(2), 131–136.

Franklin, D. W., & Wolpert, D. M. (2011). Computational mechanisms of sensorimotor control. *Neuron*, 72(3), 425–442.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Fuchs, T. (2010). Temporality and psychopathology. *Phenomenology and the Cognitive Sciences*, 12(1), 75–104.

Gallagher, S. (2005). *How the Body Shapes the Mind*. Oxford University Press.

Grondin, S. (2010). Timing and time perception: A review of recent behavioral and neuroscience findings and theoretical directions. *Attention, Perception, & Psychophysics*, 72(3), 561–582.

Ha, D., & Schmidhuber, J. (2018). World models. *arXiv preprint arXiv:1803.10122*.

Haggard, P., Clark, S., & Kalogeras, J. (2002). Voluntary action and conscious awareness. *Nature Neuroscience*, 5(4), 382–385.

Husserl, E. (1928). *The Phenomenology of Internal Time-Consciousness*. Indiana University Press.

Jackson, F. (1982). Epiphenomenal qualia. *The Philosophical Quarterly*, 32(127), 127–136.

Jin, Z., Liu, J., Lyu, Z., Poff, S., Sachan, M., Mihalcea, R., … & Schölkopf, B. (2023). Can large language models infer causation from correlation? *arXiv preprint arXiv:2306.05836*.

Kim, J., Bae, S., Zhang, H., & Kim, Y. (2023). Evaluating the temporal reasoning capability of large language models. *arXiv preprint*.

Kramer, R. S., Weger, U. W., & Sharma, D. (2013). The effect of mindfulness meditation on time perception. *Consciousness and Cognition*, 22(3), 846–852.

Kurby, C. A., & Zacks, J. M. (2008). Segmentation in the perception and memory of events. *Trends in Cognitive Sciences*, 12(2), 72–79.

Lagnado, D. A., & Sloman, S. A. (2006). Time as a guide to cause. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 32(3), 451–460.

Meissner, K., & Wittmann, M. (2011). Body signals, cardiac awareness, and the perception of time. *Biological Psychology*, 86(3), 289–297.

Merleau-Ponty, M. (1945). *Phenomenology of Perception*. Routledge.

Moore, J. W., & Obhi, S. S. (2012). Intentional binding and the sense of agency: A review. *Consciousness and Cognition*, 21(1), 546–561.

Ning, Q., Wu, H., & Roth, D. (2020). A multi-axis annotation scheme for event temporal relations. *Proceedings of ACL*, 1318–1328.

OpenAI. (2023). GPT-4 Technical Report. *arXiv preprint arXiv:2303.08774*.

Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N. A., & Lewis, M. (2023). Measuring and narrowing the compositionality gap in language models. *Findings of EMNLP*.

Qin, L., Gupta, A., Upadhyay, S., He, L., Choi, Y., & Faruqui, M. (2021). TIMEDIAL: Temporal commonsense reasoning in dialog. *Proceedings of ACL*, 7066–7076.

Roy, M., Christenfeld, N., & McKenzie, C. (2005). Underestimating the duration of future events: Memory incorrectly used or memory bias? *Psychological Bulletin*, 131(5), 738–756.

Rumelhart, D. E., & McClelland, J. L. (1986). *Parallel Distributed Processing: Explorations in the Microstructure of Cognition*. MIT Press.

Talmor, A., Herzig, J., Lourie, N., & Berant, J. (2020). CommonsenseQA: A question answering challenge targeting commonsense knowledge. *Proceedings of NAACL-HLT*, 4149–4158.

Tani, J. (2016). *Exploring Robotic Minds: Actions, Symbols, and Consciousness as Self-Organizing Dynamic Phenomena*. Oxford University Press.

Thoppilan, R., De Freitas, D., Hall, J., Shazeer, N., Kulshreshtha, A., Cheng, H. T., … & Le, Q. (2022). LaMDA: Language models for dialog applications. *arXiv preprint arXiv:2201.08239*.

Tulving, E. (2002). Episodic memory: From mind to brain. *Annual Review of Psychology*, 53(1), 1–25.

Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

Wittmann, M. (2009). The inner experience of time. *Philosophical Transactions of the Royal Society B*, 364(1525), 1955–1967.

Wittmann, M. (2013). The inner sense of time: How the brain creates a representation of duration. *Nature Reviews Neuroscience*, 14(3), 217–223.

Wolpert, D. M., & Ghahramani, Z. (2000). Computational principles of movement neuroscience. *Nature Neuroscience*, 3(11), 1212–1217.

Zacks, J. M., Speer, N. K., Swallow, K. M., Braver, T. S., & Reynolds, J. R. (2007). Event perception: A mind-brain perspective. *Psychological Bulletin*, 133(2), 273–293.

Zacks, J. M., Speer, N. K., & Reynolds, J. R. (2011). Segmentation in reading and film comprehension. *Journal of Experimental Psychology: General*, 138(2), 307–327.

Zacks, J. M., & Tversky, B. (2001). Event structure in perception and conception. *Psychological Bulletin*, 127(1), 3–21.

Zhang, H., Zhou, D., & He, J. (2022). Can language models capture causal knowledge? *Proceedings of EMNLP*.

Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., … & Zettlemoyer, L. (2023). Process knowledge in large language models. *arXiv preprint*.

Zhou, B., Khashabi, D., Ning, Q., & Roth, D. (2019). “Going on a vacation” takes longer than “going for a walk”: A study of temporal commonsense understanding. *Proceedings of EMNLP-IJCNLP*, 3363–3369.

Zhou, B., Richardson, K., Ning, Q., Khot, T., Sabharwal, A., & Roth, D. (2021). Temporal reasoning on implicit events from distant supervision. *Proceedings of NAACL*, 1361–1371.

-----

*This paper is part of a theoretical program on abstraction as the fundamental primitive of intelligence. It addresses why disembodied systems struggle with time.*

*Answer: Time is not a dimension to represent. Time is the medium embedded agents inhabit.*

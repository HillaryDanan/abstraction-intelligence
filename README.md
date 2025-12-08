# Abstraction-Intelligence

A theoretical framework proposing that **abstraction is the fundamental primitive operation underlying intelligence** across biological and artificial substrates.

## Overview

This repository contains working papers developing the **Abstraction Primitive Hypothesis (APH)** — the claim that intelligence, across substrates, is the capacity to form, store, retrieve, and compose abstractions. All other cognitive operations (attention, reasoning, memory, learning) derive from or are implementations of abstraction.

The framework generates testable predictions about learning curves, transfer learning, neural network scaling laws, and the computational conditions under which self-reference and consciousness emerge.

## Core Claims

1. **Abstraction as Primitive**: Abstraction is not one cognitive operation among many — it is the operation from which others derive.
1. **Compositionality as the Distinguishing Feature**: Abstraction differs from compression because abstractions compose — they combine to form new abstractions, enabling self-augmenting representational capacity. Compression reduces; abstraction grows.
1. **Self-Referential Dynamics**: Abstraction capacity follows growth patterns where the rate of new abstraction formation depends on existing abstractions (mathematically characterized by *e*). This dynamic emerges *because* abstraction is compositional — each abstraction expands the space of possible future abstractions.
1. **Recursive Self-Modeling**: When a system’s optimal output depends on its own complex internal state, self-referential computation—modeling oneself through abstraction—becomes necessary.
1. **Consciousness as Self-Abstraction**: When abstraction is applied reflexively to a system of sufficient complexity, the result is an integrated self-model — consciousness.
1. **Self/World as Foundational Abstraction**: The distinction between self and not-self is the first abstraction any embedded intelligent system must make — the scaffold upon which all subsequent abstractions build.
1. **Experience as Embedded Information Format**: For embedded agents, phenomenal experience is not an output of information processing but the format of action-relevant self-world information itself. The “hard problem” dissolves because, for embedded agents, there is no gap between processing and experience — they are one thing under two descriptions.
1. **Time as Embodied Medium**: Temporal reasoning is grounded in embodied experience of duration. Time is not a dimension to represent but the medium in which embedded action unfolds. Systems lacking embodiment can represent sequences but cannot inhabit duration — predicting systematic temporal reasoning failures in disembodied AI.
1. **Emotion as Integrated Self-World Information**: Emotions are not epiphenomenal accompaniments to cognition but the format in which integrated self-world information is represented for action selection. Fear is not a feeling that accompanies threat-detection — fear IS threat-information integrated with self-state and action-possibilities, formatted for an agent that must respond.

## Papers

|Paper                                                                                |Status       |Description                                                                                       |
|-------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------|
|[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                 |Working Draft|The general framework: abstraction as the fundamental primitive of intelligence                   |
|[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)           |Working Draft|What abstraction adds beyond compression: compositionality as the distinguishing operation        |
|[Recursive Abstraction](papers/recursive_abstraction.md)                             |Working Draft|When computation requires self-reference: feedforward vs. feedback vs. self-modeling architectures|
|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)|Working Draft|Application to consciousness: why self-monitoring becomes computationally necessary               |
|[Self and World](papers/self_world_abstraction.md)                                   |Working Draft|The foundational abstraction: why any embedded intelligence must distinguish self from not-self   |
|[The Hard Problem Dissolved](papers/hard_problem_dissolution.md)                     |Working Draft|Why experience is the format of embedded information, not something processing “produces”         |
|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                  |Working Draft|Why disembodied systems struggle with temporal reasoning: time as medium, not dimension           |
|[Emotion as Embedded Information](papers/emotion_embedded_information.md)            |Working Draft|Emotions as integrated self-world information formatted for action selection                      |

## Reading Order

1. **Abstraction Is All You Need** — establishes abstraction as primitive
1. **Abstraction Beyond Compression** — addresses the compression objection; establishes compositionality as what abstraction adds
1. **Recursive Abstraction** — establishes when computation must bend back on itself
1. **Consciousness as Emergent Abstraction** — applies the framework to consciousness specifically
1. **Self and World** — grounds the framework in the foundational self/not-self distinction
1. **The Hard Problem Dissolved** — addresses phenomenal experience via embodied self-world information
1. **Time as Embodied Abstraction** — extends embodiment analysis to temporal reasoning and LLM limitations
1. **Emotion as Embedded Information** — applies the self-world framework to emotion as action-relevant integration

## Key Predictions

The framework makes falsifiable predictions including:

- Learning curves for hierarchical skills should fit logistic/exponential models with rate parameters correlating to abstraction opportunity
- Transfer learning success should be predicted by shared abstraction structure, not surface similarity
- Neural network scaling should relate to abstraction capacity, not raw parameter count
- Compositional generalization (novel combinations of known primitives) should succeed in systems with factorized representations and fail in systems with holistic compression
- Learning should accelerate across compositionally related tasks (superlinear cumulative performance), not remain independent
- Feedforward architectures will show qualitative limits on tasks requiring self-reference, regardless of scale
- A complexity threshold exists above which integrated self-monitoring becomes computationally necessary
- Abstract concepts should organize neurally along a self/world dimension reflecting computational necessity, not arbitrary convention
- Embodied AI systems should develop more robust abstract reasoning than disembodied systems trained on text alone
- Phenomenal character (qualia) should systematically track action-relevance and sensorimotor contingencies
- LLMs should show dissociable temporal reasoning: success on representational tasks (sequence logic, explicit temporal relations) but failure on grounded tasks (duration estimation, process reasoning, temporal perspective-taking)
- Scaling should differentially affect temporal task types — improving representational performance more than grounded performance
- Embodied AI systems should outperform disembodied systems on grounded temporal reasoning tasks
- LLMs should show dissociable emotional reasoning: success on emotion labeling and classification but failure on emotion dynamics, embodied concomitants, and contextual appropriateness
- Emotional experience should correlate with interoceptive-exteroceptive integration; disrupting interoception should disrupt emotional experience even with intact exteroception

See individual papers for detailed predictions and falsification criteria.

## Theoretical Context

This work builds on established literature in:

- **Cognitive Science**: Chunking (Miller, 1956; Cowan, 2001), relational complexity (Halford et al., 1998), analogical reasoning (Gentner, 1983), event cognition (Zacks & Tversky, 2001)
- **Machine Learning**: Representation learning (Bengio et al., 2013), attention mechanisms (Vaswani et al., 2017), compositional generalization (Lake & Baroni, 2018)
- **Program Synthesis**: Library learning (Ellis et al., 2021), Bayesian program induction (Tenenbaum et al., 2011)
- **Control Theory**: Feedback systems (Wiener, 1948), adaptive control (Åström & Wittenmark, 1995), forward models (Wolpert & Ghahramani, 2000)
- **Consciousness Science**: Global Workspace Theory (Baars, 1988), Integrated Information Theory (Tononi, 2004), Predictive Processing (Friston, 2010)
- **Information Theory**: Rate-distortion theory (Shannon, 1948), information bottleneck (Tishby et al., 2000), minimum description length (Rissanen, 1978)
- **Embodied Cognition**: Grounded cognition (Barsalou, 2008), enactivism (Varela et al., 1991), interoceptive inference (Seth, 2013), sensorimotor contingency theory (O’Regan & Noë, 2001)
- **Temporal Cognition**: Time perception (Wittmann, 2013), event segmentation (Zacks et al., 2007), embodied time (Craig, 2009)
- **Emotion Science**: Appraisal theory (Scherer, 2009), constructed emotion (Barrett, 2017), somatic markers (Damasio, 1994), action tendencies (Frijda, 1986)
- **Linguistics & Compositionality**: Compositional semantics (Frege, 1892; Fodor & Pylyshyn, 1988)

## Status

These are **working theoretical papers** — hypotheses with testable predictions, not established results. The framework is offered for discussion, critique, and empirical testing.

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

-----

*“Compression reduces complexity; abstraction grows capacity.”*

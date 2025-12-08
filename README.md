# Abstraction-Intelligence

A theoretical framework proposing that **abstraction is the fundamental primitive operation underlying intelligence** across biological and artificial substrates.

## Overview

This repository contains working papers developing the **Abstraction Primitive Hypothesis (APH)** — the claim that intelligence, across substrates, is the capacity to form, store, retrieve, and compose abstractions. All other cognitive operations (attention, reasoning, memory, learning) derive from or are implementations of abstraction.

The framework generates testable predictions about learning curves, transfer learning, neural network scaling laws, and the computational conditions under which self-reference, consciousness, emotion, and social cognition emerge.

## Core Claims

1. **Abstraction as Primitive**: Abstraction is not one cognitive operation among many — it is the operation from which others derive.
1. **Compositionality as the Distinguishing Feature**: Abstraction differs from compression because abstractions compose — they combine to form new abstractions, enabling self-augmenting representational capacity. Compression reduces; abstraction grows.
1. **Self-Referential Dynamics**: Abstraction capacity follows growth patterns where the rate of new abstraction formation depends on existing abstractions (mathematically characterized by *e*). This dynamic emerges *because* abstraction is compositional — each abstraction expands the space of possible future abstractions.
1. **Developmental Spectrum**: Abstraction capacity is not binary but develops through qualitatively distinct stages — pattern extraction, symbol formation, recursive composition, and self-referential abstraction — each enabling operations impossible at prior stages.
1. **Disembodied Abstraction**: Systems lacking embodiment can achieve substantial capacity at early abstraction stages while showing systematic limitations at later stages, particularly self-referential abstraction. Current LLMs exhibit this profile.
1. **Recursive Self-Modeling**: When a system’s optimal output depends on its own complex internal state, self-referential computation—modeling oneself through abstraction—becomes necessary.
1. **Consciousness as Self-Abstraction**: When abstraction is applied reflexively to a system of sufficient complexity, the result is an integrated self-model — consciousness.
1. **Self/World as Foundational Abstraction**: The distinction between self and not-self is the first abstraction any embedded intelligent system must make — the scaffold upon which all subsequent abstractions build.
1. **Experience as Embedded Information Format**: For embedded agents, phenomenal experience is not an output of information processing but the format of action-relevant self-world information itself. The “hard problem” dissolves because, for embedded agents, there is no gap between processing and experience — they are one thing under two descriptions.
1. **Time as Embodied Medium**: Temporal reasoning is grounded in embodied experience of duration. Time is not a dimension to represent but the medium in which embedded action unfolds. Systems lacking embodiment can represent sequences but cannot inhabit duration — predicting systematic temporal reasoning failures in disembodied AI.
1. **Emotion as Self-World Integration**: Emotions are integrated self-world information formatted for action selection. They are not outputs of cognition but the format in which action-relevant cognition occurs for embedded agents. Valence tracks predicted viability impact.
1. **Social Dynamics as Multi-Agent Abstraction**: When environments contain multiple agents, the abstraction primitive is applied recursively — abstracting over others’ abstractions of self. Social emotions are composed, recursive abstractions formatted for multi-agent coordination under resource constraints. This pattern scales across levels of organization.

## Papers

|Paper                                                                                    |Status       |Description                                                                                           |
|-----------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------|
|[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                     |Working Draft|The general framework: abstraction as the fundamental primitive of intelligence                       |
|[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)               |Working Draft|What abstraction adds beyond compression: compositionality as the distinguishing operation            |
|[Recursive Abstraction](papers/recursive_abstraction.md)                                 |Working Draft|When computation requires self-reference: feedforward vs. feedback vs. self-modeling architectures    |
|[The Developmental Spectrum of Abstraction](papers/abstraction_developmental_spectrum.md)|Working Draft|From pattern extraction to self-referential cognition: abstraction capacity as staged development     |
|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)    |Working Draft|Application to consciousness: why self-monitoring becomes computationally necessary                   |
|[Self and World](papers/self_world_abstraction.md)                                       |Working Draft|The foundational abstraction: why any embedded intelligence must distinguish self from not-self       |
|[The Hard Problem Dissolved](papers/hard_problem_dissolution.md)                         |Working Draft|Why experience is the format of embedded information, not something processing “produces”             |
|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                      |Working Draft|Why disembodied systems struggle with temporal reasoning: time as medium, not dimension               |
|[Emotion as Embedded Information](papers/emotion_embedded_information.md)                |Working Draft|Emotions as integrated self-world information formatted for action selection                          |
|[Social Dynamics](papers/social_dynamics.md)                                             |Working Draft|Multi-agent abstraction: recursive, compositional abstraction across agents under resource constraints|

## Reading Order

1. **Abstraction Is All You Need** — establishes abstraction as primitive
1. **Abstraction Beyond Compression** — addresses the compression objection; establishes compositionality as what abstraction adds
1. **Recursive Abstraction** — establishes when computation must bend back on itself
1. **The Developmental Spectrum of Abstraction** — establishes that abstraction capacity develops through qualitatively distinct stages; locates LLMs on this spectrum
1. **Consciousness as Emergent Abstraction** — applies the framework to consciousness specifically; builds on stage 4 (self-referential abstraction)
1. **Self and World** — grounds the framework in the foundational self/not-self distinction
1. **The Hard Problem Dissolved** — addresses phenomenal experience via embodied self-world information
1. **Time as Embodied Abstraction** — extends embodiment analysis to temporal reasoning and LLM limitations
1. **Emotion as Embedded Information** — applies self-world integration to emotion; synthesizes major emotion theories
1. **Social Dynamics** — scales the framework to multi-agent environments; shows recursive abstraction structure of social cognition

## Key Predictions

The framework makes falsifiable predictions including:

**Abstraction and Learning**

- Learning curves for hierarchical skills should fit logistic/exponential models with rate parameters correlating to abstraction opportunity
- Transfer learning success should be predicted by shared abstraction structure, not surface similarity
- Neural network scaling should relate to abstraction capacity, not raw parameter count
- Compositional generalization (novel combinations of known primitives) should succeed in systems with factorized representations and fail in systems with holistic compression
- Learning should accelerate across compositionally related tasks (superlinear cumulative performance), not remain independent

**Developmental Spectrum**

- Stage progression should be sequential: no system should exhibit capacity at stage N without capacity at stage N-1
- Stage-specific tasks should cluster: performance within stages should correlate more strongly than performance across stages
- Stage transitions should be marked by qualitative changes in failure modes, not just worse performance

**LLM-Specific**

- LLM performance should degrade systematically with increased hierarchical depth (nesting, relational complexity) in ways human performance does not
- LLM confidence should be poorly calibrated on tasks requiring genuine self-modeling compared to pattern extraction tasks
- Scaling (parameters, data, compute) should improve stage 1–2 performance more than stage 3–4 performance
- Chain-of-thought prompting should improve stage 3 tasks more than stage 4 tasks

**Architecture and Self-Reference**

- Feedforward architectures will show qualitative limits on tasks requiring self-reference, regardless of scale
- A complexity threshold exists above which integrated self-monitoring becomes computationally necessary

**Embodiment and Grounding**

- Embodied AI systems should develop more robust abstract reasoning than disembodied systems trained on text alone
- Embodied systems should outperform disembodied systems on grounded temporal reasoning tasks
- Abstract concepts should organize neurally along a self/world dimension reflecting computational necessity, not arbitrary convention
- Phenomenal character (qualia) should systematically track action-relevance and sensorimotor contingencies

**Temporal Reasoning**

- LLMs should show dissociable temporal reasoning: success on representational tasks (sequence logic, explicit temporal relations) but failure on grounded tasks (duration estimation, process reasoning, temporal perspective-taking)
- Scaling should differentially affect temporal task types — improving representational performance more than grounded performance

**Emotion and Social Cognition**

- Emotional phenomenology should systematically track action-relevance: pain phenomenology should track action-type, color phenomenology should track ecological relevance, emotional experience should track interoceptive predictions
- Social emotion capacity should correlate with recursive abstraction (mentalizing) capacity
- Multi-agent AI systems with self-models, other-models, reputation tracking, and resource constraints should develop social-emotion-like internal states; systems without these features should not

See individual papers for detailed predictions and falsification criteria.

## Theoretical Context

This work builds on established literature in:

- **Cognitive Science**: Chunking (Miller, 1956; Cowan, 2001), relational complexity (Halford et al., 1998), analogical reasoning (Gentner, 1983), event cognition (Zacks & Tversky, 2001)
- **Developmental Psychology**: Stage theories (Piaget, 1954), metacognitive development (Flavell, 1979; Schneider, 2008), relational complexity trajectories (Halford et al., 1998)
- **Comparative Cognition**: Cross-species abstraction capacity (Giurfa et al., 2001; Seed & Byrne, 2010), mirror self-recognition (Gallup, 1970)
- **Machine Learning**: Representation learning (Bengio et al., 2013), attention mechanisms (Vaswani et al., 2017), compositional generalization (Lake & Baroni, 2018), multi-agent reinforcement learning (Leibo et al., 2017)
- **Program Synthesis**: Library learning (Ellis et al., 2021), Bayesian program induction (Tenenbaum et al., 2011)
- **Control Theory**: Feedback systems (Wiener, 1948), adaptive control (Åström & Wittenmark, 1995), forward models (Wolpert & Ghahramani, 2000)
- **Consciousness Science**: Global Workspace Theory (Baars, 1988), Integrated Information Theory (Tononi, 2004), Predictive Processing (Friston, 2010)
- **Information Theory**: Rate-distortion theory (Shannon, 1948), information bottleneck (Tishby et al., 2000), minimum description length (Rissanen, 1978)
- **Embodied Cognition**: Grounded cognition (Barsalou, 2008), enactivism (Varela et al., 1991), interoceptive inference (Seth, 2013), sensorimotor contingency theory (O’Regan & Noë, 2001)
- **Temporal Cognition**: Time perception (Wittmann, 2013), event segmentation (Zacks et al., 2007), embodied time (Craig, 2009)
- **Emotion Science**: Appraisal theory (Scherer, 2009), constructed emotion (Barrett, 2017), embodied emotion (Damasio, 1994)
- **Social Cognition**: Theory of mind (Frith & Frith, 2006), recursive mentalizing (Stiller & Dunbar, 2007), social emotions (Tracy & Robins, 2007)
- **Evolutionary Game Theory**: Cooperation dynamics (Trivers, 1971; Fehr & Gächter, 2002), emotions as commitment devices (Frank, 1988)
- **Linguistics & Compositionality**: Compositional semantics (Frege, 1892; Fodor & Pylyshyn, 1988)

## Status

These are **working theoretical papers** — hypotheses with testable predictions, not established results. The framework is offered for discussion, critique, and empirical testing.

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

-----

*“Abstraction is all you need.”*

# Abstraction-Intelligence

A theoretical framework proposing that **abstraction is the fundamental primitive operation underlying intelligence** across biological and artificial substrates.

## Overview

This repository contains working papers developing the **Abstraction Primitive Hypothesis (APH)** — the claim that intelligence, across substrates, is the capacity to form, store, retrieve, and compose abstractions. All other cognitive operations (attention, reasoning, memory, learning) derive from or are implementations of abstraction.

The framework generates testable predictions about learning curves, transfer learning, neural network scaling laws, and the computational conditions under which self-reference, consciousness, emotion, and social cognition emerge.

## Core Claims

1. **Abstraction as Primitive**: Abstraction is not one cognitive operation among many — it is the operation from which others derive.
1. **Compositionality as the Distinguishing Feature**: Abstraction differs from compression because abstractions compose — they combine to form new abstractions, enabling self-augmenting representational capacity. Compression reduces; abstraction grows. Compositionality admits degrees and can be measured via compositional generalization rate, systematicity, transfer efficiency, compositional depth, and reuse frequency.
1. **Abstraction as the Minimal Sufficient Operation**: Abstraction is the specific operation of converting attended information into manipulable, composable symbols. Attention selects; abstraction transforms selection into composable currency. A reflex arc attends but does not abstract. Intelligence begins precisely where composition begins — this is the minimal sufficient operation that distinguishes a sensor from a spotlight. Abstraction is distinct from input operations (perception, attention) and downstream operations (memory, learning, reasoning, decision-making, action). It creates the representational currency that other cognitive operations trade in — constrained enough to be falsifiable, central enough to be foundational.
1. **Abstraction as Prior to Prediction**: Prediction presupposes representational content — to predict X will occur requires a representation of X, a representation of futurity, and the compositional capacity to combine them. Abstraction creates the representational currency that prediction operates on. Prediction is the selection pressure; abstraction is what is selected over.
1. **Architectural Conditions for Abstraction**: Compression yields abstraction when end-to-end compositional structure is present: factorized input encoding, compositional output structure, sufficient compression ratio (>5×), and balanced factor cardinalities (<2.5× asymmetry). Without this alignment, compression produces factorized representations that cannot be used compositionally — the interaction between input and output structure dominates main effects (empirically confirmed: interaction = 0.720 vs. main effects ~0.36; Cohen’s d = 11.95).
1. **Self-Referential Dynamics and *e***: Abstraction capacity follows growth patterns where the rate of new abstraction formation depends on existing abstractions. The “state” in this state-dependent dynamic is the system’s own abstraction capacity — for sufficiently developed systems, its self-model. If abstraction is the universal primitive of intelligence, *e* emerges not as an incidental feature of common growth processes but as a mathematical signature of what intelligence fundamentally is. This is not metaphor but mathematical necessity, arising from three independent sources: the compositionality of abstraction (dA/dt ∝ A), information theory (optimal self-modeling uses natural logarithms and exponential family distributions), and the general mathematics of state-dependent change. The connection holds even under sublinear compositionality.
1. **Developmental Spectrum**: Abstraction capacity is not binary but develops through qualitatively distinct stages — pattern extraction, symbol formation, recursive composition, and self-referential abstraction — each enabling operations impossible at prior stages.
1. **Embeddedness as Precondition for Stage 4**: Embeddedness — being situated in an environment where actions produce contingent consequences that feed back to affect subsequent states — is the operative requirement for Stage 4 abstraction, not physical embodiment per se. Embeddedness creates computational pressure for the self/world distinction: to predict and act optimally, an embedded agent must decompose observations into self-caused versus world-caused components. This pressure is absent in non-embedded systems. The self/world distinction is thus the foundational abstraction from which higher-order self-modeling cascades.
1. **Non-Embedded Abstraction**: Systems lacking embeddedness (action-consequence contingency with feedback closure) can achieve substantial capacity at early abstraction stages while showing systematic limitations at later stages, particularly self-referential abstraction. Current LLMs, trained on static corpora without action-consequence coupling, exhibit this profile — not because they lack bodies, but because they lack the embedded interaction that forces self/world differentiation.
1. **Recursive Self-Modeling**: When a system’s optimal output depends on its own complex internal state, self-referential computation—modeling oneself through abstraction—becomes necessary.
1. **Consciousness as Self-Abstraction**: When abstraction is applied reflexively to a system of sufficient complexity, the result is an integrated self-model — consciousness.
1. **Self/World as Foundational Abstraction**: The distinction between self and not-self is the first abstraction any embedded intelligent system must make — the scaffold upon which all subsequent abstractions build. This distinction is not given in raw sensory input but must be extracted through embedded experience.
1. **The Self-Modeling Cascade**: From the self/world foundation, increasingly sophisticated self-representations cascade: body schema → agency → perspective → mental state attribution → metacognition → Stage 4 abstraction. Each level presupposes the levels below it. Disrupting lower levels impairs higher levels; the entire structure depends on the foundation, which depends on embeddedness.
1. **Experience as Embedded Information Format**: For embedded agents, phenomenal experience is not an output of information processing but the format of action-relevant self-world information itself. The “hard problem” dissolves because, for embedded agents, there is no gap between processing and experience — they are one thing under two descriptions.
1. **Time as Embedded Medium**: Temporal reasoning is grounded in embedded experience of duration. Time is not a dimension to represent but the medium in which embedded action unfolds. Systems lacking embeddedness can represent sequences but cannot inhabit duration — predicting systematic temporal reasoning failures in non-embedded AI.
1. **Emotion as Self-World Integration**: Emotions are integrated self-world information formatted for action selection. They are not outputs of cognition but the format in which action-relevant cognition occurs for embedded agents. Valence tracks predicted viability impact.
1. **Social Dynamics as Multi-Agent Abstraction**: When environments contain multiple agents, the abstraction primitive is applied recursively — abstracting over others’ abstractions of self. Social emotions are composed, recursive abstractions formatted for multi-agent coordination under resource constraints. This pattern scales across levels of organization.
1. **Architectural Implications for AI**: Current LLMs are compression engines, not abstraction engines. Progress beyond current limitations requires not merely architectural improvements or scale increases, but embedding systems in environments with appropriate contingency structure — action-consequence coupling, self-relevance, sufficient complexity, temporal extension, and potentially social embedding.

## Papers

|Paper                                                                                    |Status       |Description                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[Abstraction Is All You Need](papers/abstraction_is_all_you_need.md)                     |Working Draft|The general framework: abstraction as the fundamental primitive of intelligence                                                                                                                                                                 |
|[Abstraction Beyond Compression](papers/abstraction_beyond_compression.md)               |Working Draft|What abstraction adds beyond compression: compositionality as the distinguishing operation; metrics for measuring compositionality; architectural conditions for abstraction                                                                    |
|[Abstraction Constrained](papers/abstraction_constrained.md)                             |Working Draft|What abstraction is and is not: addressing the vacuity objection by distinguishing abstraction from input and downstream operations                                                                                                             |
|[Prediction Requires Abstraction](papers/prediction_requires_abstraction.md)             |Working Draft|On the priority of representational formation over predictive operation: why prediction presupposes abstraction                                                                                                                                 |
|[Recursive Abstraction](papers/recursive_abstraction.md)                                 |Working Draft|When computation requires self-reference: feedforward vs. feedback vs. self-modeling architectures; the mathematics of *e* (with information-theoretic grounding, robustness under sublinear compositionality, and oscillatory dynamics via *π*)|
|[The Developmental Spectrum of Abstraction](papers/abstraction_developmental_spectrum.md)|Working Draft|From pattern extraction to self-referential cognition: abstraction capacity as staged development                                                                                                                                               |
|[Embeddedness and the Self/World Distinction](papers/embedded_abstraction.md)            |Working Draft|Why embeddedness (not embodiment) enables Stage 4: computational pressure for self/world distinction; the cascade from foundational abstraction to self-referential cognition                                                                   |
|[Self and World](papers/self_world_abstraction.md)                                       |Working Draft|The foundational abstraction: why any embedded intelligence must distinguish self from not-self                                                                                                                                                 |
|[Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md)    |Working Draft|Application to consciousness: why self-monitoring becomes computationally necessary                                                                                                                                                             |
|[The Hard Problem Dissolved](papers/hard_problem_dissolution.md)                         |Working Draft|Why experience is the format of embedded information, not something processing “produces”                                                                                                                                                       |
|[Time as Embodied Abstraction](papers/time_embodied_abstraction.md)                      |Working Draft|Why non-embedded systems struggle with temporal reasoning: time as medium, not dimension                                                                                                                                                        |
|[Emotion as Embedded Information](papers/emotion_embedded_information.md)                |Working Draft|Emotions as integrated self-world information formatted for action selection                                                                                                                                                                    |
|[Social Dynamics](papers/social_dynamics.md)                                             |Working Draft|Multi-agent abstraction: recursive, compositional abstraction across agents under resource constraints                                                                                                                                          |
|[Beyond Large Language Models](papers/beyond_llms.md)                                    |Working Draft|Architectural principles for post-LLM AI: why current systems compress rather than abstract, and what abstraction-promoting architectures require                                                                                               |

## Reading Order

1. **Abstraction Is All You Need** — establishes abstraction as primitive
1. **Abstraction Beyond Compression** — addresses the compression objection; establishes compositionality as what abstraction adds; develops metrics for measuring compositionality; identifies architectural conditions under which compression yields abstraction
1. **Abstraction Constrained** — addresses the vacuity objection; establishes what abstraction is and is not; distinguishes from input operations (perception, attention) and downstream operations (memory, learning, reasoning, decision-making, action)
1. **Prediction Requires Abstraction** — addresses the predictive processing alternative; establishes that prediction presupposes representational content that abstraction provides
1. **Recursive Abstraction** — establishes when computation must bend back on itself; formalizes the mathematical role of *e* in self-referential dynamics via compositionality and information theory; demonstrates robustness under varying compositionality assumptions; extends to oscillatory dynamics governed by *π*
1. **The Developmental Spectrum of Abstraction** — establishes that abstraction capacity develops through qualitatively distinct stages; locates LLMs on this spectrum; poses the question: what enables Stage 4?
1. **Embeddedness and the Self/World Distinction** — answers the Stage 4 question: embeddedness (not embodiment) creates computational pressure for self/world distinction; establishes the cascade from foundational abstraction to self-referential cognition; explains why non-embedded systems face principled barriers to Stage 4
1. **Self and World** — elaborates the foundational self/not-self distinction; grounds the framework in the primary abstraction any embedded intelligence must make
1. **Consciousness as Emergent Abstraction** — applies the framework to consciousness specifically; builds on the self/world foundation and Stage 4 abstraction
1. **The Hard Problem Dissolved** — addresses phenomenal experience via embedded self-world information
1. **Time as Embodied Abstraction** — extends embeddedness analysis to temporal reasoning; explains systematic temporal reasoning failures in non-embedded AI
1. **Emotion as Embedded Information** — applies self-world integration to emotion; synthesizes major emotion theories
1. **Social Dynamics** — scales the framework to multi-agent environments; shows recursive abstraction structure of social cognition
1. **Beyond Large Language Models** — applies the complete framework to AI architecture; derives engineering principles from APH; generates testable predictions for post-transformer systems

-----

## Empirical Research Program

This theoretical framework is accompanied by an empirical research program testing its predictions. The repositories below probe specific aspects of the Abstraction Primitive Hypothesis through experiments, analysis tools, and working implementations.

### Temporal Reasoning & Embeddedness

*Testing: Time as Embedded Abstraction, Non-Embedded Abstraction limitations*

|Repository                                                                      |Description                                                                                         |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
|[TIDE](https://github.com/HillaryDanan/TIDE)                                    |Temporal-Internal Dimensional Encoding: cognitive architecture patterns from neurodiversity insights|
|[TIDE-resonance](https://github.com/HillaryDanan/TIDE-resonance)                |Empirical explorations of cognitive-sensory resonance patterns; AI metacognitive reflection studies |
|[TIDE-analysis](https://github.com/HillaryDanan/TIDE-analysis)                  |Automated analysis pipeline for AI Perception Study data                                            |
|[temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm)|Testing temporal integration capacity in LLMs                                                       |
|[temporal-myopia-llm](https://github.com/HillaryDanan/temporal-myopia-llm)      |Testing addiction-like patterns via temporal reasoning limitations                                  |
|[llm-time-decay](https://github.com/HillaryDanan/llm-time-decay)                |Comparing temporal coherence degradation across LLM architectures                                   |
|[curved-cognition](https://github.com/HillaryDanan/curved-cognition)            |Testing recursive temporal reasoning; geometric constraints in transformers                         |
|[embodied-cognition](https://github.com/HillaryDanan/embodied-cognition)        |Testing physics intuitions and embedded concepts in LLMs                                            |

### Self/World Boundary & Consciousness

*Testing: Self/World as Foundational Abstraction, Consciousness as Self-Abstraction, Embeddedness Requirements*

|Repository                                                                                      |Description                                                                            |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
|[BIND](https://github.com/HillaryDanan/BIND)                                                    |Boundary Information Neural Dynamics: consciousness emergence at information boundaries|
|[computational-emergence-theory](https://github.com/HillaryDanan/computational-emergence-theory)|Multi-scale intelligence framework examining emergent patterns across substrates       |
|[claude-emergence-patterns](https://github.com/HillaryDanan/claude-emergence-patterns)          |Empirical analysis of emergence patterns in Claude AI conversations                    |
|[comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms)|Testing cognitive signatures and self-modeling capacity across LLM architectures       |
|[hexagonal-consciousness-suite](https://github.com/HillaryDanan/hexagonal-consciousness-suite)  |Hexagonal architecture for consciousness modeling                                      |

### Developmental Spectrum & Abstraction Stages

*Testing: Stage progression, Pattern extraction vs. symbol formation vs. recursive composition*

|Repository                                                                                        |Description                                                                                         |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
|[reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum)                        |Testing pattern matching vs. genuine rule induction in LLMs                                         |
|[concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector)          |Detecting when systems fall back to concrete features; stage regression analysis                    |
|[benign-violations](https://github.com/HillaryDanan/benign-violations)                            |Testing humor generation as embedded prediction error resolution                                    |
|[paradox-induced-oscillations](https://github.com/HillaryDanan/paradox-induced-oscillations)      |Testing dissociative patterns and representational instability in LLMs; *e*-*π* oscillatory dynamics|
|[computational-self-construction](https://github.com/HillaryDanan/computational-self-construction)|Testing self-construction and self-model building in LLMs                                           |

### Recursive & Self-Referential Dynamics

*Testing: Recursive Abstraction, self-modeling necessity, e-governed dynamics*

|Repository                                                                                      |Description                                                                        |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
|[recursive-reality](https://github.com/HillaryDanan/recursive-reality)                          |Testing reality perception and self-reference through physical vs. constructed data|
|[ouroboros-learning](https://github.com/HillaryDanan/ouroboros-learning)                        |Self-referential learning dynamics                                                 |
|[reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence)|Multi-agent reciprocal mirroring and emergence patterns                            |

### Architecture & Representation

*Testing: Compositionality, geometric constraints, information primitives*

|Repository                                                                                    |Description                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|[emergent-factorization](https://github.com/HillaryDanan/emergent-factorization)              |**End-to-end compositionality principle**: testing that compositional generalization requires factorized input AND compositional output (confirmed: d = 11.95)|
|[compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction)        |Minimal test of holistic vs. factorized architecture for compositional generalization (confirmed: d = 12.65)                                                  |
|[information-atoms](https://github.com/HillaryDanan/information-atoms)                        |Theoretical exploration of unified information atoms for multimodal AI                                                                                        |
|[causal-attention-geometry](https://github.com/HillaryDanan/causal-attention-geometry)        |Testing causal reasoning and geometric pattern effects in transformers                                                                                        |
|[multi-geometric-attention](https://github.com/HillaryDanan/multi-geometric-attention)        |Working theory for multi-geometric attention in transformer architecture                                                                                      |
|[relativistic-interpretability](https://github.com/HillaryDanan/relativistic-interpretability)|Geometric framework for understanding neural network reasoning through multiple reference frames                                                              |
|[spectral-representations](https://github.com/HillaryDanan/spectral-representations)          |Exploring wave-based representations in computation and cognition                                                                                             |
|[hexagonal-vision-research](https://github.com/HillaryDanan/hexagonal-vision-research)        |Hexagonal patterns in visual processing                                                                                                                       |
|[computational-substrates](https://github.com/HillaryDanan/computational-substrates)          |Conceptualizing computation and intelligence based on substrate and architecture                                                                              |

### Social & Multi-Agent Dynamics

*Testing: Social Dynamics as Multi-Agent Abstraction, recursive mentalizing*

|Repository                                                                                |Description                                                              |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
|[game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite)        |Trust and cooperation dynamics; recursive modeling in multi-agent systems|
|[trust-calibration-framework](https://github.com/HillaryDanan/trust-calibration-framework)|Framework for trust and verification in AI-human interaction             |

### Language, Memory & Cognition

*Testing: Abstraction in linguistic processing, compositional structure*

|Repository                                                                                                |Description                                                       |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
|[linguistic-dynamics-theory](https://github.com/HillaryDanan/linguistic-dynamics-theory)                  |Language as control parameter in cognitive-behavioral trajectories|
|[linguistic-memory-framework](https://github.com/HillaryDanan/linguistic-memory-framework)                |Testing memory patterns based on linguistic framing in LLMs       |
|[cross-linguistic-attention-dynamics](https://github.com/HillaryDanan/cross-linguistic-attention-dynamics)|Testing cross-linguistic attention patterns in transformers       |
|[retroactive-causality](https://github.com/HillaryDanan/retroactive-causality)                            |Testing garden path effects and reanalysis in language models     |
|[nonlinear-dialogue-dynamics](https://github.com/HillaryDanan/nonlinear-dialogue-dynamics)                |Testing nonlinear conversational patterns in LLMs                 |
|[llm-habituation-patterns](https://github.com/HillaryDanan/llm-habituation-patterns)                      |Testing habituation and adaptation patterns in LLMs               |

### Physical Grounding & Embeddedness

*Testing: Embedded information format, grounded abstraction*

|Repository                                                                                        |Description                                                          |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
|[physical-grounding-llm](https://github.com/HillaryDanan/physical-grounding-llm)                  |Testing LLM interpretability with physical sensor data               |
|[TERRA-embodied-interpretability](https://github.com/HillaryDanan/TERRA-embodied-interpretability)|Grounded/embedded concepts from physical data in LLM interpretability|

### Analysis Tools & Infrastructure

*Frameworks for empirical testing across the research program*

|Repository                                                                                    |Description                                                               |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
|[pattern-analyzer](https://github.com/HillaryDanan/pattern-analyzer)                          |AI Cognitive Pattern Analysis Framework: empirical detection suite        |
|[cognitive-architectures-ai](https://github.com/HillaryDanan/cognitive-architectures-ai)      |Neurodiversity-inspired cognitive architectures for AI systems            |
|[TIDE-dissertation-integration](https://github.com/HillaryDanan/TIDE-dissertation-integration)|Integration hub connecting PhD dissertation findings to AI implementations|

-----

## Key Predictions

The framework makes falsifiable predictions including:

**Abstraction and Learning**

- Learning curves for hierarchical skills should fit logistic/exponential models with rate parameters correlating to abstraction opportunity
- Transfer learning success should be predicted by shared abstraction structure, not surface similarity
- Neural network scaling should relate to abstraction capacity, not raw parameter count
- Compositional generalization (novel combinations of known primitives) should succeed in systems with factorized representations and fail in systems with holistic compression
- Learning should accelerate across compositionally related tasks (superlinear cumulative performance), not remain independent

**Abstraction Dissociability**

- Abstraction failures should be dissociable from input failures (perception, attention) and downstream failures (memory, reasoning, decision-making)
- Category-specific abstraction deficits should occur with intact downstream operations
- Downstream deficits (e.g., amnesia, dysexecutive syndrome) should occur with intact momentary abstraction
- Systems with genuine abstraction should show compositional generalization; systems with sophisticated compression should not

**Abstraction vs. Prediction**

- Abstraction deficits should impair prediction more than prediction deficits impair abstraction
- Compositional generalization should be dissociable from prediction accuracy (systems can predict well without composing well)
- Abstract representation should emerge in systems not trained for prediction (via clustering, compression, analogy)
- Abstraction stage should constrain prediction sophistication — no system should make predictions requiring stage N representations without stage N abstraction capacity

**Compositionality Metrics**

- Compositional Generalization Rate (CGR), Systematicity Index (SI), Transfer Efficiency Ratio (TER), Compositional Depth (CD), and Reuse Frequency (RF) should correlate with each other and predict downstream intelligence-relevant outcomes
- Aggregate Compositionality Score should predict generalization, transfer, and abstraction stage better than simple compression metrics (reconstruction error, encoding length)

**Architectural Conditions** ✓ *Core predictions empirically confirmed*

- ✓ Neural networks with explicit factorization pressure should show higher compositional generalization than holistic architectures *(confirmed: d = 12.65)*
- ✓ Compositional generalization requires end-to-end compositional structure — factorized input AND compositional output *(confirmed: interaction = 0.720, d = 11.95)*
- ✓ Factorized representations alone are insufficient; output structure is equally critical *(confirmed: 93% factor decodability with 0% generalization under non-compositional output)*
- ✓ Compositional generalization scales with compression ratio *(confirmed: 20% → 100% as ratio increases from 2× to 16×)*
- ✓ Factor asymmetry degrades generalization with quantifiable boundary *(confirmed: ratio <2.5 required)*
- ✓ Transformer architectures outperform MLPs; RNNs underperform *(confirmed: Transformer 92%, MLP 80%, RNN 41%)*
- Architectures with compositional bottlenecks (neural module networks, structured attention) should show higher systematicity than fully distributed architectures
- Multi-task training should improve transfer efficiency more than single-task training when tasks share compositional structure
- Adding explicit compositional bottlenecks to LLMs should improve systematicity even at equivalent scale

**Developmental Spectrum**

- Stage progression should be sequential: no system should exhibit capacity at stage N without capacity at stage N-1
- Stage-specific tasks should cluster: performance within stages should correlate more strongly than performance across stages
- Stage transitions should be marked by qualitative changes in failure modes, not just worse performance

**LLM-Specific**

- LLM performance should degrade systematically with increased hierarchical depth (nesting, relational complexity) in ways human performance does not
- LLM confidence should be poorly calibrated on tasks requiring genuine self-modeling compared to pattern extraction tasks
- Scaling (parameters, data, compute) should improve stage 1–2 performance more than stage 3–4 performance
- Chain-of-thought prompting should improve stage 3 tasks more than stage 4 tasks
- LLMs should show mixed compositional generalization — succeeding on some novel compositions, failing on others — reflecting partial but incomplete compositional abstraction

**Embeddedness and Self/World Distinction**

- Non-embedded systems should show a ceiling on self-modeling capacity regardless of scale or architecture
- Removing action-consequence contingency should impair self/world distinction development even when other aspects of experience are preserved
- AI systems with genuine environmental embeddedness during training should show improved self-modeling capacity compared to non-embedded systems with equivalent parameters and compute
- Self-modeling capacity in agentic AI should correlate with measures of environmental contingency
- Development of higher cascade levels (metacognition, Stage 4) should depend on lower levels (body schema, agency); disruption of lower levels should impair higher levels
- In any system that achieves Stage 4 abstraction, evidence of self/world distinction should be present; Stage 4 without self/world distinction would falsify the foundational claim

**Architecture and Self-Reference (*e*-Governed Dynamics)**

- Feedforward architectures will show qualitative limits on tasks requiring self-reference, regardless of scale
- A complexity threshold exists above which integrated self-monitoring becomes computationally necessary
- Self-referential learning curves should follow *e*-governed (exponential/logistic) dynamics, not power laws — discriminable via asymptote tests, log-linear vs. log-log plotting, and characteristic time constant ratios (63.2%, 86.5%, 95% of asymptote at τ, 2τ, 3τ)
- Neural systems implementing self-reference should exhibit characteristic time constants related to *e*, with cross-system invariance: time constant ratios should equal inverse processing speed ratios
- Measured compositionality (Paper 2 metrics) should correlate with the dynamical exponent β — higher compositionality yields dynamics closer to pure exponential
- Self-referential systems with feedback delays should exhibit oscillatory dynamics governed by *π* (damped oscillations, limit cycles), with the *e*-*π* signature (exponential envelope, sinusoidal oscillation) as evidence of delayed self-reference

**Embeddedness and Grounding**

- Embedded AI systems should develop more robust abstract reasoning than non-embedded systems trained on text alone
- Embedded systems should outperform non-embedded systems on grounded temporal reasoning tasks
- Abstract concepts should organize neurally along a self/world dimension reflecting computational necessity, not arbitrary convention
- Phenomenal character (qualia) should systematically track action-relevance and sensorimotor contingencies
- AI systems in social environments (interacting with other agents) should show faster development of self/world distinction than systems in non-social environments of equivalent complexity

**Temporal Reasoning**

- LLMs should show dissociable temporal reasoning: success on representational tasks (sequence logic, explicit temporal relations) but failure on grounded tasks (duration estimation, process reasoning, temporal perspective-taking)
- Scaling should differentially affect temporal task types — improving representational performance more than grounded performance

**Emotion and Social Cognition**

- Emotional phenomenology should systematically track action-relevance: pain phenomenology should track action-type, color phenomenology should track ecological relevance, emotional experience should track interoceptive predictions
- Social emotion capacity should correlate with recursive abstraction (mentalizing) capacity
- Multi-agent AI systems with self-models, other-models, reputation tracking, and resource constraints should develop social-emotion-like internal states; systems without these features should not

**Post-LLM Architecture**

- Architectures with explicit factorization pressure should show improved compositional generalization compared to standard transformers at equivalent scale
- Architectures with compositional bottlenecks should show improved systematicity, with magnitude of improvement increasing with compositional complexity
- Multi-task training across compositionally related tasks should produce superlinear cumulative performance gains
- Scaling standard transformers should improve Stage 1–2 performance more than Stage 3–4 performance
- Systems trained with embedded grounding should outperform text-only systems on temporal reasoning tasks involving duration, process dynamics, and temporal perspective-taking
- Systems with learned self-models should show improved metacognitive calibration compared to systems without explicit self-models
- Achieving Stage 4 capacity may require fundamentally different training paradigms that embed systems in persistent, consequential environments during learning — not just during deployment

See individual papers for detailed predictions and falsification criteria.

-----

## Theoretical Context

This work builds on established literature in:

- **Cognitive Science**: Chunking (Miller, 1956; Cowan, 2001), relational complexity (Halford et al., 1998), analogical reasoning (Gentner, 1983), event cognition (Zacks & Tversky, 2001)
- **Developmental Psychology**: Stage theories (Piaget, 1954), metacognitive development (Flavell, 1979; Schneider, 2008), relational complexity trajectories (Halford et al., 1998), contingency detection (Watson, 1972; Rochat & Striano, 2000)
- **Comparative Cognition**: Cross-species abstraction capacity (Giurfa et al., 2001; Seed & Byrne, 2010), mirror self-recognition (Gallup, 1970), metacognition in animals (Smith, Couchman, & Beran, 2014)
- **Neuropsychology**: Category-specific deficits (Warrington & Shallice, 1984), dissociations between abstraction and memory (Squire, 2009), prefrontal function (Stuss & Knight, 2002), self-referential processing (Northoff & Bermpohl, 2004)
- **Machine Learning**: Representation learning (Bengio et al., 2013), attention mechanisms (Vaswani et al., 2017), compositional generalization (Lake & Baroni, 2018), disentangled representations (Higgins et al., 2017), multi-agent reinforcement learning (Leibo et al., 2017)
- **Program Synthesis**: Library learning (Ellis et al., 2021), Bayesian program induction (Tenenbaum et al., 2011)
- **Control Theory**: Feedback systems (Wiener, 1948), adaptive control (Åström & Wittenmark, 1995), forward models (Wolpert & Ghahramani, 2000)
- **Dynamical Systems**: Nonlinear dynamics and oscillations (Strogatz, 2015), delay differential equations (Glass & Mackey, 1988)
- **Consciousness Science**: Global Workspace Theory (Baars, 1988), Integrated Information Theory (Tononi, 2004), Predictive Processing (Friston, 2010; Clark, 2013)
- **Information Theory**: Rate-distortion theory (Shannon, 1948), information bottleneck (Tishby et al., 2000), minimum description length (Rissanen, 1978), maximum entropy (Jaynes, 1957)
- **Embodied & Embedded Cognition**: Grounded cognition (Barsalou, 2008), enactivism (Varela et al., 1991), interoceptive inference (Seth, 2013), sensorimotor contingency theory (O’Regan & Noë, 2001), active perception (Held & Hein, 1963; Gibson, 1979)
- **Temporal Cognition**: Time perception (Wittmann, 2013), event segmentation (Zacks et al., 2007), embodied time (Craig, 2009)
- **Emotion Science**: Appraisal theory (Scherer, 2009), constructed emotion (Barrett, 2017), embodied emotion (Damasio, 1994)
- **Social Cognition**: Theory of mind (Frith & Frith, 2006), recursive mentalizing (Stiller & Dunbar, 2007), social emotions (Tracy & Robins, 2007)
- **Evolutionary Game Theory**: Cooperation dynamics (Trivers, 1971; Fehr & Gächter, 2002), emotions as commitment devices (Frank, 1988)
- **Linguistics & Compositionality**: Compositional semantics (Frege, 1892; Fodor & Pylyshyn, 1988)

-----

## Status

These are **working theoretical papers** — hypotheses with testable predictions, not established results. The framework is offered for discussion, critique, and empirical testing.

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

-----

*“Abstraction is all you need.”*

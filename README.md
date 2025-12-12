# Abstraction-Intelligence

**What makes something intelligent?**

This repository develops the **Abstraction Primitive Hypothesis (APH)**: intelligence emerges from recursive interaction between symbol formation and compositional structure.

## Framework Overview

| Component | Status |
|-----------|--------|
| Composition type hierarchy (3a→3b→3c→3d) | **Core contribution** — testable predictions about dissociations |
| Recursive interaction framing | **Core idea** — composition and symbol formation must inform each other |
| Embeddedness claims | **Exploratory** — interesting direction, not required for main claims |

---

## The Core Idea

### Abstraction as Recursive Interaction

**Abstraction is the recursive process of forming and composing symbols.**

This isn't a checklist (symbols ✓, composition ✓, therefore intelligent). It's a claim about computational architecture: symbol formation and composition must *inform each other iteratively*.

1. Extract stable representations from continuous input (symbol formation)
2. Combine them systematically (composition)
3. Composition reveals structure not visible in individual symbols
4. That structure feeds back to refine symbol formation
5. Refined symbols enable more sophisticated composition
6. **Return to step 2 → iterate**

**The computational structure:**

```
         ┌─────────────────────────────────────┐
         │                                     │
         ▼                                     │
    [Raw Input] → [Symbol Formation] → [Symbols] → [Composition] → [Composed Structures]
                         ▲                                              │
                         │                                              │
                         └──── [Compositional demands/failures] ────────┘
```

This feedback loop is what produces expanding representational capacity—not composition alone, not symbol formation alone, but their mutual refinement.

### Why Interaction Matters

| System | Forms Symbols? | Composes? | Interaction? | Result |
|--------|----------------|-----------|--------------|--------|
| Calculator | ✗ (provided) | ✓ | N/A | Not intelligent |
| Edge detectors | ✓ | ✗ | ✗ | Not intelligent |
| CNN classifier | ✓ | Limited | Medium | Limited |
| Word2vec | Partial | 3a only | Minimal | Marginal |
| LLM | ✓ | ✓ (3a-3b, limited 3c-3d) | Medium | Capable but bounded |
| Human cognition | ✓ | ✓ (3a–3d) | Strong (ongoing) | Intelligent |

---

## The Composition Type Hierarchy

**Not all composition is the same.** This is the framework's core empirical contribution.

| Type | Structure | Example | Computational Requirement |
|------|-----------|---------|--------------------------|
| **3a: Concatenative** | A + B → AB | "blue" + "bird" → "bluebird" | Sequencing |
| **3b: Role-filler binding** | R(x) + S(y) → R(x)S(y) | AGENT(dog) + ACTION(chased) + PATIENT(cat) | Slots separable from content |
| **3c: Recursive embedding** | A contains [B contains C] | "The dog [that chased the cat [that caught the mouse]]" | Composed units become compositional primitives |
| **3d: Analogical mapping** | Structure(A) → Structure(B) | atom:nucleus :: solar system:sun | Abstract structure transfers across domains |

**Proposed ordering:** 3a → 3b → 3c → 3d

Each level requires capacities the previous doesn't:
- Role-filler requires separating structure from content
- Recursive embedding requires treating composed wholes as primitives
- Analogical mapping requires abstracting structure entirely

### Predictions

**Composition type dissociations:**
- Systems should show 3a-3b success with 3c-3d failure (not uniform degradation)
- Bees: waggle dance is role-filler binding (DISTANCE × DIRECTION); predict success on novel combinations, failure on recursive embedding
- LLMs: accuracy should degrade faster with recursive depth than with role-filler novelty

**The key distinction:**
- 3a–3b: Finite combinatorial space (could be captured by sufficiently large lookup)
- 3c–3d: Unbounded combinatorial space (requires genuinely generative mechanisms)

---

## The Symbol Identification Problem

If symbols are defined by entering compositional relationships, the framework is circular. Solution: **define symbols by formation, not downstream behavior.**

A symbol is a representational unit the system *extracted from continuous input*:

| Criterion | Measurement |
|-----------|-------------|
| **Discreteness** | Clustering in activation space | 
| **Stability** | Same cluster activates for similar inputs across time |
| **Context-independence** | Representation activates regardless of what else is present |

---

## Interaction Levels

| Level | Definition | Example |
|-------|------------|---------|
| **Weak** | Gradient flow exists | Standard backpropagation |
| **Medium** | Representations change in response to compositional demands | End-to-end training |
| **Strong** | New representational primitives emerge in response to novelty | Novelty-driven expansion |

APH's distinctive claim: *strong interaction*—novelty-driven expansion—is what produces genuine generativity.

---

## Embeddedness (Exploratory)

Strong interaction may require encountering genuine novelty, which may require a stable self against which to measure. If so, embeddedness (persistence, self/world distinction, action-consequence loops) enables what non-embedded systems can't achieve.

---

## Falsifiable Predictions

| Prediction | Testability | Falsification |
|------------|-------------|---------------|
| Composition types dissociate (3a-3b vs. 3c-3d) | **High** | No differences found across systems |
| Hierarchy ordering holds | **High** | Dissociations exist but ordering wrong |
| Recursive depth degrades faster than role-filler novelty | **High** | Identical degradation curves |
| Bees: role-filler success, recursive failure | **High** | Bees succeed at recursive embedding |

---

## Papers

**Core framework (1–9):** The interaction criterion, composition types, embeddedness requirements.

| # | Paper | Description |
|---|-------|-------------|
| 1 | [Abstraction Is All You Need](papers/abstraction_is_all_you_need.md) | The general framework |
| 2 | [The Computational Structure of Abstraction](papers/abstraction_defined.md) | Symbol formation + compositional structure |
| 3 | [Abstraction Beyond Compression](papers/abstraction_beyond_compression.md) | Compositionality as distinguishing operation |
| 4 | [Abstraction Constrained](papers/abstraction_constrained.md) | What abstraction is not |
| 5 | [Prediction Requires Abstraction](papers/prediction_requires_abstraction.md) | Why prediction presupposes representation |
| 6 | [Recursive Abstraction](papers/recursive_abstraction.md) | Self-reference and the mathematics of *e* |
| 7 | [The Developmental Spectrum](papers/abstraction_developmental_spectrum.md) | Levels of formation-composition interaction |
| 8 | [Embeddedness and Self/World](papers/embedded_abstraction.md) | Five components of embeddedness |
| 9 | [Self and World](papers/self_world_abstraction.md) | The foundational abstraction |

**Adjacent explorations (10–14):** Consciousness, time, emotion, social cognition.

| # | Paper | Description |
|---|-------|-------------|
| 10 | [Consciousness as Emergent Abstraction](papers/consciousness_emergent_abstraction.md) | Self-monitoring as computational necessity |
| 11 | [The Hard Problem Reframed](papers/hard_problem_reframed.md) | Experience as embedded information format |
| 12 | [Time as Embodied Abstraction](papers/time_embodied_abstraction.md) | Temporal reasoning and embeddedness |
| 13 | [Emotion as Embedded Information](papers/emotion_embedded_information.md) | Emotions as action-formatted information |
| 14 | [Social Dynamics](papers/social_dynamics.md) | Multi-agent recursive abstraction |

**Applications (15):**

| # | Paper | Description |
|---|-------|-------------|
| 15 | [Beyond Large Language Models](papers/beyond_llms.md) | Architectural implications for AI |

**Recommended reading order:** 1 → 2 → 3 → 7 → 8 → 9 → 15 (core path) or continue through all for full picture.

---

## Empirical Research Program

The framework connects to a broader research program spanning 48 repositories. Organized by how they relate to APH:

### 🧠 Core Framework & Composition

Testing the central claims about abstraction, composition types, and symbol formation.

| Repository | Description |
|------------|-------------|
| [abstraction-intelligence](https://github.com/HillaryDanan/abstraction-intelligence) | The APH framework (this repo) |
| [composition-type-dissociation](https://github.com/HillaryDanan/composition-type-dissociation) | Empirical tests of 3a→3b→3c→3d dissociations |
| [compositional-abstraction](https://github.com/HillaryDanan/compositional-abstraction) | Experiments on compositional abstraction in different systems |
| [emergent-factorization](https://github.com/HillaryDanan/emergent-factorization) | Testing emergent factorization properties |
| [reasoning-in-vacuum](https://github.com/HillaryDanan/reasoning-in-vacuum) | Pattern matching vs. genuine reasoning in LLMs |

### 🔄 Recursive Interaction & Self-Reference

Testing the recursive interaction claim—does composition inform symbol formation?

| Repository | Description |
|------------|-------------|
| [self-referential-dynamics](https://github.com/HillaryDanan/self-referential-dynamics) | *e*-governed dynamics in intelligent systems |
| [computational-self-construction](https://github.com/HillaryDanan/computational-self-construction) | Self-construction patterns in LLMs |
| [ouroboros-learning](https://github.com/HillaryDanan/ouroboros-learning) | Self-referential learning dynamics |
| [recursive-reality](https://github.com/HillaryDanan/recursive-reality) | Reality perception and recursive effects |

### ⏱️ Temporal Dynamics

Time as a dimension of abstraction—how temporal structure relates to composition.

| Repository | Description |
|------------|-------------|
| [TIDE](https://github.com/HillaryDanan/TIDE) | Temporal-Internal Dimensional Encoding framework |
| [TIDE-resonance](https://github.com/HillaryDanan/TIDE-resonance) | Cognitive-sensory resonance patterns |
| [TIDE-analysis](https://github.com/HillaryDanan/TIDE-analysis) | Empirical analysis pipeline |
| [TIDE-dissertation-integration](https://github.com/HillaryDanan/TIDE-dissertation-integration) | Integration with Levinson (2021) dissertation |
| [temporal-coherence-llm](https://github.com/HillaryDanan/temporal-coherence-llm) | Temporal integration in LLMs |
| [temporal-myopia-llm](https://github.com/HillaryDanan/temporal-myopia-llm) | Temporal reasoning and myopia patterns |
| [llm-time-decay](https://github.com/HillaryDanan/llm-time-decay) | Temporal coherence decay across models |
| [curved-cognition](https://github.com/HillaryDanan/curved-cognition) | Curved biological patterns in cognition |

### 🌍 Embodiment & Grounding

Testing embeddedness claims—does physical grounding enable something non-embedded systems can't achieve?

| Repository | Description |
|------------|-------------|
| [embodied-cognition](https://github.com/HillaryDanan/embodied-cognition) | Embodied concepts in LLMs |
| [physical-grounding-llm](https://github.com/HillaryDanan/physical-grounding-llm) | Physical sensor data in LLM interpretability |
| [TERRA-embodied-interpretability](https://github.com/HillaryDanan/TERRA-embodied-interpretability) | Grounding/embodied concepts from physical data |

### 🪞 Consciousness & Self/World

The foundational abstraction—self/world distinction and consciousness.

| Repository | Description |
|------------|-------------|
| [BIND](https://github.com/HillaryDanan/BIND) | Boundary Information Neural Dynamics framework |
| [comparative-consciousness-llms](https://github.com/HillaryDanan/comparative-consciousness-llms) | Cognitive signatures across LLMs |
| [hexagonal-consciousness-suite](https://github.com/HillaryDanan/hexagonal-consciousness-suite) | Hexagonal architecture for consciousness modeling |
| [computational-emergence-theory](https://github.com/HillaryDanan/computational-emergence-theory) | Multi-scale intelligence and emergence |

### 👥 Social Dynamics & Multi-Agent

Multi-agent recursive abstraction—how interaction drives abstraction.

| Repository | Description |
|------------|-------------|
| [reciprocal-mirroring-emergence](https://github.com/HillaryDanan/reciprocal-mirroring-emergence) | Multi-agent mirroring and emergence |
| [game-theory-trust-suite](https://github.com/HillaryDanan/game-theory-trust-suite) | Cooperation dynamics and trust |
| [trust-calibration-framework](https://github.com/HillaryDanan/trust-calibration-framework) | Trust and verification in AI-Human interaction |

### 🗣️ Language & Linguistics

Language as a window into compositional structure.

| Repository | Description |
|------------|-------------|
| [linguistic-dynamics-theory](https://github.com/HillaryDanan/linguistic-dynamics-theory) | Language as control parameter in cognition |
| [linguistic-memory-framework](https://github.com/HillaryDanan/linguistic-memory-framework) | Memory patterns based on linguistic framing |
| [cross-linguistic-attention-dynamics](https://github.com/HillaryDanan/cross-linguistic-attention-dynamics) | Cross-linguistic attention patterns |
| [benign-violations](https://github.com/HillaryDanan/benign-violations) | Humor generation and violation structures |

### 🔬 Attention & Geometry

Geometric structure in attention and composition.

| Repository | Description |
|------------|-------------|
| [causal-attention-geometry](https://github.com/HillaryDanan/causal-attention-geometry) | Causal reasoning and geometric patterns |
| [multi-geometric-attention](https://github.com/HillaryDanan/multi-geometric-attention) | Multi-geometric attention in transformers |
| [relativistic-interpretability](https://github.com/HillaryDanan/relativistic-interpretability) | Geometric framework for neural network reasoning |
| [spectral-representations](https://github.com/HillaryDanan/spectral-representations) | Wave-based representations in cognition |

### 🧪 LLM Empirical Testing

Direct empirical tests of LLM capabilities and limitations.

| Repository | Description |
|------------|-------------|
| [llm-habituation-patterns](https://github.com/HillaryDanan/llm-habituation-patterns) | Habituation patterns in LLMs |
| [nonlinear-dialogue-dynamics](https://github.com/HillaryDanan/nonlinear-dialogue-dynamics) | Nonlinear conversational patterns |
| [paradox-induced-oscillations](https://github.com/HillaryDanan/paradox-induced-oscillations) | Dissociative patterns analogous to human neural networks |
| [retroactive-causality](https://github.com/HillaryDanan/retroactive-causality) | Garden path effects in language models |
| [claude-emergence-patterns](https://github.com/HillaryDanan/claude-emergence-patterns) | Emergence patterns in Claude conversations |

### 🔧 Representation & Architecture

Alternative representational schemes and architectures.

| Repository | Description |
|------------|-------------|
| [information-atoms](https://github.com/HillaryDanan/information-atoms) | Unified information atoms for multimodal AI |
| [hexagonal-vision-research](https://github.com/HillaryDanan/hexagonal-vision-research) | Hexagonal patterns in visual processing |
| [computational-substrates](https://github.com/HillaryDanan/computational-substrates) | Computation and intelligence across substrates |
| [cognitive-architectures-ai](https://github.com/HillaryDanan/cognitive-architectures-ai) | Neurodiversity-inspired cognitive architectures |

### 📊 Analysis Tools

Frameworks for analyzing AI cognitive patterns.

| Repository | Description |
|------------|-------------|
| [pattern-analyzer](https://github.com/HillaryDanan/pattern-analyzer) | Cognitive pattern analysis framework |
| [concrete-overflow-detector](https://github.com/HillaryDanan/concrete-overflow-detector) | Linguistic analysis for AI reasoning patterns |

---

## References

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Chomsky, N. (1957). *Syntactic Structures*. Mouton.

Fodor, J. A. (1975). *The Language of Thought*. Harvard University Press.

Fodor, J. A., & Pylyshyn, Z. W. (1988). Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2), 3-71.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Hauser, M. D., Chomsky, N., & Fitch, W. T. (2002). The faculty of language: What is it, who has it, and how did it evolve? *Science*, 298(5598), 1569-1579.

Higgins, I., et al. (2017). β-VAE: Learning basic visual concepts with a constrained variational framework. *ICLR 2017*.

Kim, N., & Linzen, T. (2020). COGS: A compositional generalization challenge. *EMNLP 2020*.

Kriegeskorte, N., Mur, M., & Bandettini, P. A. (2008). Representational similarity analysis. *Frontiers in Systems Neuroscience*, 2, 4.

Lake, B., & Baroni, M. (2018). Generalization without systematicity. *ICML 2018*.

Menzel, R., et al. (2011). A common frame of reference for learned and communicated vectors in honeybee navigation. *Current Biology*, 21(8), 645-650.

---

## Author

**Hillary Danan, PhD**  
Cognitive Neuroscience

## License

MIT

---

*"Abstraction is all your need ;)"*

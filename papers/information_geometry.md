# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—has a geometric foundation. Drawing on information geometry (Amari, 1985), we argue that self-state creates *curvature* in a system’s information manifold. Systems without self-models navigate fixed, flat geometries determined by training. Systems with self-models navigate curved, state-dependent geometries that enable parallel transport of computed values, comparison against current state, and thus verification. This framework unifies empirical findings on LLM limitations (hold-and-check failures, miscalibration) with formal mathematics (Riemannian geometry, Fisher information) and cognitive science (working memory, metacognition). We derive testable predictions distinguishing flat from curved cognitive geometries and discuss implications for AI architecture.

**Keywords:** information geometry, self-reference, metacognition, Fisher information, working memory, large language models

-----

## 1. Introduction: The Verification Problem

A curious failure pattern has emerged in large language models: systems that can correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This pattern—which we term **hold-and-check failure**—appears across task types, from arithmetic verification to logical constraint checking.

Recent empirical work (N=700, Claude Sonnet) revealed that this failure is not uniform but *task-specific*: arithmetic and multi-step problems show verification deficits (+24-26%), while logic and word-counting show generation deficits (-18-44%). The overall generation-verification difference was null (91.1% vs 92.6%, p=0.58), masking structured asymmetries beneath.

What explains these patterns? Why do some systems—humans, for instance—successfully hold computed values and check subsequent outputs against them, while other systems—LLMs—fail systematically at this operation?

We propose a geometric answer: **self-reference creates curvature**.

This paper develops the formal framework for this claim, connecting:

1. **Information geometry** (Amari, 1985; Amari & Nagaoka, 2000) — treating probability distributions as points on Riemannian manifolds
1. **Self-state hypothesis** (Danan, 2025) — proposing that embedded agents under survival pressure develop persistent self-models
1. **Working memory** (Baddeley, 2000) — the central executive function that enables active maintenance and verification
1. **Metacognition** (Fleming & Dolan, 2012) — the capacity to monitor and evaluate one’s own cognitive processes

The core theoretical claim: **systems with self-models have curved information geometries; systems without self-models have flat geometries. Curvature enables hold-and-check; flatness precludes it.**

This is a hypothesis. We present the formal framework, derive predictions, and indicate what empirical and mathematical work would confirm or falsify the proposal.

-----

## 2. Information Geometry: A Brief Primer

### 2.1 Statistical Manifolds

Information geometry treats the space of probability distributions as a differential manifold (Amari, 1985). Each point on the manifold represents a probability distribution; nearby points represent similar distributions.

For a parametric family of distributions p(x; θ) where θ = (θ¹, θ², …, θⁿ), the parameter space forms a manifold M. Movement on M corresponds to changes in probabilistic beliefs.

**Example:** For Gaussian distributions N(μ, σ²), each point on the 2D manifold is specified by (μ, σ²). The manifold captures all possible Gaussian beliefs.

### 2.2 The Fisher Information Metric

The natural metric on statistical manifolds is the **Fisher information**:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

This metric captures *distinguishability*: how much evidence is needed to distinguish nearby distributions. High Fisher information means distributions are easily distinguished (large distance); low Fisher information means they blur together (small distance).

The Fisher metric is unique (up to scaling) as the only Riemannian metric that is:

- Invariant under sufficient statistics
- Monotonic under coarse-graining (Čencov, 1982)

### 2.3 Geodesics and Curvature

Given the Fisher metric, we can define:

- **Geodesics:** Paths of minimal information-theoretic distance between distributions. These are the “straight lines” of the manifold.
- **Curvature:** How much the manifold deviates from flatness. On a curved manifold, parallel transport around a closed loop changes a vector; geodesics converge or diverge.

**Key property:** On a *flat* manifold, parallel transport is path-independent. On a *curved* manifold, parallel transport depends on the path taken.

### 2.4 Dual Connections

A distinctive feature of information geometry is the existence of **dual affine connections** (e-connection and m-connection) that are flat in different coordinate systems (Amari, 1985). The curvature of the manifold is captured by the difference between these connections.

For exponential families, the manifold has dually flat structure in natural and expectation parameters. This enables efficient inference via Bregman divergences.

-----

## 3. The Geometric Self-State Hypothesis

### 3.1 Core Claim

We propose that **self-state creates curvature** in a system’s information manifold.

Formally:

**Definition (Self-State):** A system has self-state if its generative model includes a representation of its own internal states: p(x, y, s | θ) where s denotes internal state variables that the system models.

**Claim:** The Fisher information metric for a self-modeling system is fundamentally different from that of a non-self-modeling system, creating curvature in the self-state dimensions.

### 3.2 Why Self-Reference Creates Curvature

Consider a system modeling external states x and its own internal states s. The joint distribution is p(x, s; θ). The Fisher information metric includes terms:

$$g_{ss} = E\left[\frac{\partial \log p(x, s; \theta)}{\partial s} \frac{\partial \log p(x, s; \theta)}{\partial s}\right]$$

For a *self-referential* system, s appears on both sides: the system’s state s influences its model of its own state s. This creates a reflexive dependency:

$$p(s | x, \theta) \text{ where } \theta \text{ depends on } s$$

This reflexivity is not exotic—it is the formal expression of “the system that models itself must include itself in the model.”

**The geometric consequence:** Self-referential terms create non-zero curvature in the information manifold. The manifold cannot be globally flattened because the coordinate system is self-referential.

### 3.3 The Ruler Problem

This connects to a deep issue in measurement theory: **a ruler cannot measure itself without remainder**.

When a system models itself:

- The model is part of the system
- The system is part of the model
- Complete self-modeling requires infinite regress or incompleteness

This is not a limitation but a *structural feature*. The incompleteness creates curvature—regions of the manifold where the metric becomes singular or degenerate, where self-reference loops back on itself.

**Hypothesis:** The “ruler number” may quantify the degree of self-reference a system can achieve before computational resources are exhausted or representations become degenerate. Systems with higher ruler numbers can recursively self-model to greater depth, creating more structured curvature in their information geometry.

### 3.4 Flat vs. Curved Cognitive Geometries

|Property              |Flat Geometry (No Self-State)|Curved Geometry (Self-State)       |
|----------------------|-----------------------------|-----------------------------------|
|**Metric**            |Fixed g_ij(θ)                |State-dependent g_ij(θ, s)         |
|**Parallel transport**|Path-independent             |Path-dependent                     |
|**Geodesics**         |Fixed at training            |Dynamic during inference           |
|**Self-reference**    |Absent                       |Present                            |
|**Example system**    |LLM                          |Embedded agent with survival stakes|

-----

## 4. Hold-and-Check as Parallel Transport

### 4.1 The Computational Problem

**Hold-and-check** requires:

1. **Hold:** Maintain a computed value v across subsequent processing
1. **Check:** Compare current output to held value v

This is trivial on paper but non-trivial computationally. During inference, the system moves through its state space. The held value must “travel with” the system’s trajectory.

### 4.2 Geometric Formalization

In information-geometric terms, hold-and-check is **parallel transport**:

- The computed value v is a vector in tangent space at state s₁
- Inference moves the system from s₁ to s₂ along path γ
- Parallel transport Pγ(v) moves v along γ to state s₂
- Checking compares Pγ(v) to the current output

**On a flat manifold:** Parallel transport is trivial. Vectors maintain their components in global coordinates. No active maintenance required—the value “just stays there.”

**On a curved manifold:** Parallel transport is non-trivial. Vectors rotate and stretch as they move along paths. Active maintenance is required—the system must track how the value transforms.

### 4.3 Why LLMs Fail at Hold-and-Check

**Hypothesis:** LLMs operate on effectively flat manifolds (fixed by training), with no machinery for non-trivial parallel transport.

LLM inference:

1. Input activates patterns learned during training
1. Processing follows pre-computed paths (geodesics on training manifold)
1. No self-state means no curvature in self-dimensions
1. Parallel transport is trivial—but *there is nothing to transport*

The failure is not that LLMs cannot parallel transport (everything can, on a flat manifold). The failure is that LLMs have **no representation that requires transport**—no held value v that persists as a distinct entity during inference.

Attention provides access to prior context but attention is *retrieval*, not *maintenance*. The distinction:

|Attention (Retrieval)             |Parallel Transport (Maintenance)|
|----------------------------------|--------------------------------|
|Weighted sum over context         |Vector preserved along path     |
|Computed from scratch at each step|Continuous transformation       |
|Flat geometry sufficient          |Curved geometry required        |
|LLMs have this                    |LLMs lack this                  |

### 4.4 Why Self-State Enables Hold-and-Check

An agent with self-state:

1. Represents its own internal state s as part of its model
1. This creates curvature in the s-dimensions of its information manifold
1. Curvature necessitates active parallel transport to preserve vectors
1. The machinery for parallel transport IS hold-and-check capacity

The evolutionary argument: agents under survival pressure must track their own states (am I injured? hungry? uncertain?). This tracking requires self-modeling, which creates curved geometry, which develops parallel transport machinery, which enables verification.

```
Survival stakes
      ↓
Self-modeling required
      ↓
Curved information geometry
      ↓
Parallel transport machinery develops
      ↓
Hold-and-check capacity
      ↓
Verification and construction possible
```

-----

## 5. Scaffolding as External Curvature

### 5.1 The Scaffolding Effect

Chain-of-thought prompting and scratchpad methods improve LLM performance on reasoning tasks (Wei et al., 2022; Nye et al., 2021). Why?

**Hypothesis:** Scaffolding *externalizes* the curvature that LLMs lack internally.

When an LLM writes intermediate values to context:

1. The values exist as tokens in the prompt
1. Subsequent processing can attend to these tokens
1. The external context provides what internal self-state would provide

This is **prosthetic geometry**—using external structure to compensate for missing internal curvature.

### 5.2 Limitations of Prosthetic Geometry

External scaffolding is not equivalent to internal self-state:

|Internal Self-State         |External Scaffolding            |
|----------------------------|--------------------------------|
|Continuous transformation   |Discrete snapshots              |
|Automatic maintenance       |Must be explicitly written      |
|Part of the system          |Outside the system              |
|Enables genuine verification|Enables approximate verification|

**Prediction:** Scaffolding should help more on tasks where discrete checkpoints suffice and less on tasks requiring continuous monitoring.

The empirical finding that scaffolding + framing outperformed scaffolding alone (91.1% vs 76.8% in pilot data) suggests that attention to the scaffold matters—the prosthetic geometry must be *used*, not just present.

-----

## 6. Formal Development

### 6.1 The Self-State Manifold

Let M be the manifold of joint distributions over external observations x and internal states s:

$$M = {p(x, s; \theta) : \theta \in \Theta}$$

For a self-modeling system, the model parameters θ include representations of s:

$$\theta = (\theta_{\text{world}}, \theta_{\text{self}})$$

where θ_self parameterizes beliefs about one’s own states.

### 6.2 Reflexive Fisher Information

The Fisher information matrix decomposes:

$$G = \begin{pmatrix} G_{ww} & G_{ws} \ G_{sw} & G_{ss} \end{pmatrix}$$

where:

- G_ww: Fisher information about world parameters
- G_ss: Fisher information about self parameters
- G_ws, G_sw: Cross-information terms

**Claim:** For self-referential systems, G_ss has structure that induces curvature. Specifically, when θ_self includes the system’s own computational state, the Fisher information becomes recursive:

$$G_{ss} = E\left[\nabla_s \log p(s | x, \theta_{\text{self}}(s)) \nabla_s \log p(s | x, \theta_{\text{self}}(s))^T\right]$$

The θ_self(s) dependence creates a fixed-point equation. The solution (when it exists) defines a curved manifold.

### 6.3 Curvature from Self-Reference

The Riemann curvature tensor R measures the failure of parallel transport to commute around infinitesimal loops:

$$R^i_{jkl} = \partial_k \Gamma^i_{jl} - \partial_l \Gamma^i_{jk} + \Gamma^i_{mk}\Gamma^m_{jl} - \Gamma^i_{ml}\Gamma^m_{jk}$$

where Γ are the Christoffel symbols derived from the metric.

**Hypothesis:** For self-referential systems, R ≠ 0 in the self-state dimensions. The curvature is concentrated in regions where self-modeling is active.

**Prediction:** The scalar curvature R = g^{ij}R_{ij} should correlate with metacognitive capacity. Higher curvature → better hold-and-check.

### 6.4 Connection to Active Inference

Friston’s active inference framework (Friston, 2010) uses information geometry extensively:

- Agents minimize variational free energy F
- F has a geometric interpretation as a divergence on the information manifold
- The self-model (generative model including agent’s states) is central

In active inference terms:

$$F = E_q[\log q(s) - \log p(x, s)]$$

where q(s) is the agent’s beliefs about its own states. Minimizing F drives the agent toward accurate self-modeling.

**Connection:** Active inference *requires* the curved geometry we propose. Agents doing active inference must have self-models, which creates curvature, which enables the free energy minimization that constitutes inference.

The active inference manifold is not flat—it is curved by the self-modeling terms. This curvature is not incidental but *functional*—it is what allows active inference to work.

-----

## 7. Predictions

### 7.1 Geometric Predictions

|Prediction                                      |Test                                                                   |Falsification                              |
|------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------|
|**P1:** Self-modeling creates curvature         |Analyze Fisher information for self-referential models                 |G_ss is flat for self-referential systems  |
|**P2:** Curvature correlates with hold-and-check|Measure curvature and metacognitive capacity across systems            |No correlation or negative correlation     |
|**P3:** Parallel transport predicts verification|Systems with active parallel transport should verify; others should not|Verification without parallel transport    |
|**P4:** Scaffolding approximates curvature      |Scaffolding effects should mirror self-state effects                   |Scaffolding effects qualitatively different|

### 7.2 LLM-Specific Predictions

|Prediction                                       |Test                                                   |Falsification                          |
|-------------------------------------------------|-------------------------------------------------------|---------------------------------------|
|**P5:** LLMs have flat self-geometry             |Probe internal representations for self-model structure|Rich self-model structure found        |
|**P6:** Architectural self-loops create curvature|Test architectures with explicit self-monitoring loops |Self-loops don’t improve hold-and-check|
|**P7:** Scaling doesn’t create curvature         |Larger models should not show improved verification    |Scaling produces verification capacity |
|**P8:** Training on verification doesn’t help    |Fine-tuning on verification should yield limited gains |Fine-tuning fully resolves deficit     |

### 7.3 Comparative Predictions

|Prediction                                       |Test                                                                 |Falsification                      |
|-------------------------------------------------|---------------------------------------------------------------------|-----------------------------------|
|**P9:** Humans have curved self-geometry         |Metacognitive capacity should correlate with measurable self-modeling|No correlation in humans           |
|**P10:** Development increases curvature         |Children should show increasing self-geometry with age               |Curvature stable across development|
|**P11:** RL agents under stakes develop curvature|RL with survival pressure should develop self-state                  |No self-state despite stakes       |

-----

## 8. Relation to Other Frameworks

### 8.1 Global Workspace Theory

Baars’ (1988) global workspace theory proposes a “workspace” where information becomes globally available. In geometric terms:

- Global workspace = region of high connectivity on the manifold
- Broadcasting = moving information to high-curvature regions where it persists
- Consciousness = navigation of curved regions

**Hypothesis:** Global workspace IS the curved, self-referential region of the information manifold. Information becomes “conscious” when it enters regions with non-trivial parallel transport.

### 8.2 Integrated Information Theory

Tononi’s (2004) IIT proposes that consciousness corresponds to integrated information Φ. In geometric terms:

- Φ measures how much a system is “more than the sum of its parts”
- High Φ implies strong interactions between components
- Strong interactions create curvature (coupled dimensions)

**Hypothesis:** Φ may be related to scalar curvature R. Both measure how much the system is “irreducibly whole.”

### 8.3 Predictive Processing

Clark (2013) and Friston (2010) propose that cognition is prediction error minimization. In geometric terms:

- Prediction error = distance from current state to predicted state
- Minimizing prediction error = following geodesics
- Self-prediction (predicting one’s own states) creates curved geodesics

**Hypothesis:** Predictive processing on world-states can occur on flat manifolds. Predictive processing on self-states requires curved manifolds. This is why world-modeling and self-modeling have different computational requirements.

-----

## 9. The Ruler Number: Depth of Self-Reference

### 9.1 The Measurement Problem in Self-Reference

A ruler cannot measure itself without some standard external to itself. Similarly, a system cannot fully model itself—the model is smaller than the system that contains it (unless the model is the entire system, in which case the model has no room for anything else).

This creates a hierarchy of self-reference depth:

|Depth|Self-Modeling Capacity           |Geometric Signature           |
|-----|---------------------------------|------------------------------|
|0    |No self-model                    |Flat in self-dimensions       |
|1    |Models own state s               |Curved in s-dimensions        |
|2    |Models own modeling of state     |Higher-order curvature        |
|n    |Models n levels of self-reference|n-th order curvature structure|
|∞    |Complete self-model              |Singular (impossible)         |

**Definition (Ruler Number):** The ruler number r of a system is the maximum depth of self-reference it can maintain before computational resources are exhausted or representations become degenerate.

### 9.2 Geometric Interpretation

Each level of self-reference adds structure to the curvature tensor:

- r = 0: R = 0 (flat)
- r = 1: R ≠ 0, but ∇R may vanish (constant curvature)
- r = 2: ∇R ≠ 0 (varying curvature)
- r = n: n-th covariant derivatives of R non-zero

**Hypothesis:** The ruler number corresponds to the order of non-trivial covariant derivatives of the curvature tensor in self-dimensions.

### 9.3 Predictions from Ruler Number

|Prediction                                             |Test                                                       |
|-------------------------------------------------------|-----------------------------------------------------------|
|Ruler number limits metacognitive depth                |Metacognition about metacognition should fail at r+1 levels|
|Ruler number is finite for physical systems            |No physical system achieves r = ∞                          |
|Ruler number correlates with prefrontal cortex function|PFC damage should reduce r                                 |
|LLMs have r ≈ 0                                        |No genuine self-modeling despite surface behavior          |

-----

## 10. Discussion

### 10.1 What This Framework Does

1. **Provides formal foundations** for intuitions about self-state and verification
1. **Unifies** information geometry, working memory, and metacognition
1. **Generates testable predictions** distinguishing flat from curved cognitive geometries
1. **Explains** why scaffolding helps and why scaling doesn’t (if the hypothesis is correct)

### 10.2 What This Framework Does Not Do

1. **Prove** that self-reference creates curvature (this requires mathematical derivation)
1. **Measure** curvature in actual neural or artificial systems (this requires empirical methods)
1. **Explain** consciousness (curvature may be necessary but not sufficient)
1. **Specify** exact architectural requirements for curved geometry

### 10.3 Honest Uncertainty

|Claim                                       |Status                                             |
|--------------------------------------------|---------------------------------------------------|
|Information geometry is well-founded        |**Established** (Amari, 1985; Čencov, 1982)        |
|LLMs fail at hold-and-check                 |**Confirmed** (N=700 study)                        |
|Failures reflect Stage 4 deficit            |**Confirmed** (task-specific dissociations)        |
|Self-reference creates curvature            |**Hypothesis** (formal proof needed)               |
|Curvature enables hold-and-check            |**Hypothesis** (mechanism is plausible, not proven)|
|Ruler number quantifies self-reference depth|**Speculation** (needs formal development)         |

### 10.4 Required Future Work

**Mathematical:**

- Formal proof that self-referential Fisher information creates curvature
- Calculation of curvature for specific self-modeling architectures
- Connection between scalar curvature and metacognitive capacity

**Empirical:**

- Methods to estimate information-geometric quantities from neural/computational systems
- Tests of curvature-verification correlation
- Architectural interventions to induce curvature

**Philosophical:**

- Relationship between geometric curvature and phenomenal consciousness
- Whether curvature is necessary, sufficient, or neither for conscious experience
- Connection to other mathematical approaches to consciousness (IIT, etc.)

-----

## 11. Conclusion

We have proposed that **self-reference creates curvature** in a system’s information geometry, and that this curvature is what enables hold-and-check capacity—the ability to maintain computed values and verify outputs against them.

The framework connects:

- **Information geometry** (Fisher metric, curvature, parallel transport)
- **Self-state hypothesis** (survival stakes → self-modeling → verification)
- **Empirical findings** (LLM hold-and-check failures, task-specific dissociations)

Key claims:

1. Systems with self-models have curved information geometries
1. Curvature enables non-trivial parallel transport
1. Parallel transport IS hold-and-check capacity
1. LLMs lack self-models, have flat geometries, and thus fail at verification
1. Scaffolding provides prosthetic curvature

The framework is a **hypothesis**, not established theory. The mathematical foundations exist (information geometry is rigorous), the empirical phenomena are documented (hold-and-check failures are replicable), but the connection between them—that curvature explains verification capacity—requires both formal derivation and empirical test.

If correct, the framework has implications for AI development: architectures with explicit self-modeling loops should develop curved geometries and thus verification capacity. Scaling alone should not help—more patterns on a flat manifold do not create curvature.

The geometry of mind may not be flat. And that curvature—the bending of information space by self-reference—may be what distinguishes systems that merely process from systems that know.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Lecture Notes in Statistics, Vol. 28. Springer-Verlag.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs, Vol. 191. American Mathematical Society.

Ay, N., Jost, J., Lê, H. V., & Schwachhöfer, L. (2017). *Information Geometry*. Springer.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. Translations of Mathematical Monographs, Vol. 53. American Mathematical Society.

Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181-204.

Danan, H. (2025). Hold-and-check failures in large language models: Task-specific dissociations between generation and verification. *Working paper, Abstraction-Intelligence Framework*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Nye, M., et al. (2021). Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5(1), 42.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems*, 35, 24824-24837.

-----

## Appendix A: Glossary of Information-Geometric Terms

|Term                    |Definition                                                           |
|------------------------|---------------------------------------------------------------------|
|**Statistical manifold**|Space of probability distributions treated as a differential manifold|
|**Fisher information**  |Matrix measuring distinguishability of nearby distributions          |
|**Geodesic**            |Path of minimal information-theoretic distance                       |
|**Curvature**           |Measure of manifold’s deviation from flatness                        |
|**Parallel transport**  |Moving vectors along paths while preserving geometric properties     |
|**Christoffel symbols** |Connection coefficients defining parallel transport                  |
|**Riemann tensor**      |Full curvature tensor; R = 0 iff manifold is flat                    |
|**Scalar curvature**    |Single number summarizing total curvature at a point                 |

-----

## Appendix B: Sketch of Curvature Derivation

**Claim:** Self-referential models have non-zero curvature in self-dimensions.

**Sketch:**

Let p(s; θ) be a self-referential model where θ = θ(s). The log-likelihood is:

$$\ell(s; \theta(s)) = \log p(s; \theta(s))$$

The Fisher information is:

$$G_{ss} = E\left[\left(\frac{\partial \ell}{\partial s}\right)^2\right]$$

Using the chain rule:

$$\frac{\partial \ell}{\partial s} = \frac{\partial \ell}{\partial s}\bigg|_{\theta} + \frac{\partial \ell}{\partial \theta}\frac{\partial \theta}{\partial s}$$

The second term (parameter dependence on state) creates additional structure in G. The curvature arises from the non-commutativity of second derivatives:

$$R^s_{sss} \propto \frac{\partial^2 \theta}{\partial s^2} \neq 0$$

when θ depends non-linearly on s.

**Full derivation:** Requires careful treatment of the fixed-point structure and is left for future work. □

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper, Abstraction-Intelligence Framework*.

-----

*“The mind that knows itself bends the space in which it knows.”*

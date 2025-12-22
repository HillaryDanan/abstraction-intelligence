# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—has a geometric foundation. Drawing on information geometry (Amari, 1985), we argue that self-state creates *curvature* in a system’s information manifold. Systems without self-models navigate fixed, flat geometries determined by training. Systems with self-models navigate curved, state-dependent geometries that enable parallel transport of computed values, comparison against current state, and thus verification.

We show that this geometric framework converges with dynamical analyses of self-reference: the curvature induced by self-modeling is mathematically equivalent to state-dependent dynamics governed by Euler’s number *e*. This is not coincidence—*e* is intrinsic to information geometry through the Fisher metric, KL divergence, and exponential family distributions. The same constant that governs learning curves in self-referential systems also defines the natural structure of belief space.

When self-referential systems exhibit feedback delays, oscillatory dynamics emerge governed by *π*, unified with *e* through Euler’s identity. The co-occurrence of *e*-governed envelopes and *π*-governed oscillations provides a distinctive signature of self-referential computation.

The framework unifies empirical findings on LLM limitations (hold-and-check failures, miscalibration) with formal mathematics (Riemannian geometry, Fisher information, dynamical systems) and cognitive science (working memory, metacognition). We derive testable predictions distinguishing flat from curved cognitive geometries and discuss implications for AI architecture.

**Keywords:** information geometry, self-reference, Euler’s number, metacognition, Fisher information, working memory, large language models

-----

## 1. Introduction: The Verification Problem

A curious failure pattern has emerged in large language models: systems that can correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This pattern—which we term **hold-and-check failure**—appears across task types, from arithmetic verification to logical constraint checking.

Recent empirical work (N=700, Claude Sonnet) revealed that this failure is not uniform but *task-specific*: arithmetic and multi-step problems show verification deficits (+24-26%), while logic and word-counting show generation deficits (-18-44%). The overall generation-verification difference was null (91.1% vs 92.6%, p=0.58), masking structured asymmetries beneath.

What explains these patterns? Why do some systems—humans, for instance—successfully hold computed values and check subsequent outputs against them, while other systems—LLMs—fail systematically at this operation?

We propose a geometric answer: **self-reference creates curvature**.

This paper develops the formal framework for this claim, connecting:

1. **Information geometry** (Amari, 1985; Amari & Nagaoka, 2000) — treating probability distributions as points on Riemannian manifolds
1. **Dynamical systems** (Danan, 2025b) — self-referential computation governed by Euler’s number *e*
1. **Self-state hypothesis** (Danan, 2025a) — embedded agents under survival pressure develop persistent self-models
1. **Working memory** (Baddeley, 2000) — the central executive function that enables active maintenance and verification
1. **Metacognition** (Fleming & Dolan, 2012) — the capacity to monitor and evaluate one’s own cognitive processes

The core theoretical claim: **systems with self-models have curved information geometries; systems without self-models have flat geometries. Curvature enables hold-and-check; flatness precludes it. The curvature is governed by *e*—the same constant that appears in optimal self-modeling under uncertainty.**

This is a hypothesis. We present the formal framework, derive predictions, and indicate what empirical and mathematical work would confirm or falsify the proposal.

-----

## 2. Information Geometry: A Brief Primer

### 2.1 Statistical Manifolds

Information geometry treats the space of probability distributions as a differential manifold (Amari, 1985). Each point on the manifold represents a probability distribution; nearby points represent similar distributions.

For a parametric family of distributions p(x; θ) where θ = (θ¹, θ², …, θⁿ), the parameter space forms a manifold M. Movement on M corresponds to changes in probabilistic beliefs.

### 2.2 The Fisher Information Metric

The natural metric on statistical manifolds is the **Fisher information**:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Critical observation:** The Fisher metric is defined in terms of *natural logarithms*—logarithms base *e*. This is not an arbitrary choice. The natural log is the unique logarithm that makes information-theoretic calculus tractable:

- Entropy in nats: $H = -\sum p \ln p$
- KL divergence: $D_{KL} = \sum p \ln(p/q)$
- Maximum entropy distributions: $p(x) \propto e^{\theta \cdot T(x)}$

**Established:** The Fisher metric is unique (up to scaling) as the only Riemannian metric that is invariant under sufficient statistics and monotonic under coarse-graining (Čencov, 1982). This uniqueness theorem means *e* is not optional—it is intrinsic to the geometry of belief space.

### 2.3 Geodesics and Curvature

Given the Fisher metric, we can define:

- **Geodesics:** Paths of minimal information-theoretic distance between distributions
- **Curvature:** How much the manifold deviates from flatness
- **Exponential map:** The function that traces geodesics from a point

**Key property:** On a *flat* manifold, parallel transport is path-independent. On a *curved* manifold, parallel transport depends on the path taken.

### 2.4 The Exponential Map and *e*

In Riemannian geometry, geodesics are traced by the **exponential map**:

$$\exp_p: T_pM \to M$$

which takes a tangent vector v at point p and returns the endpoint of the geodesic starting at p with initial velocity v, after unit time.

The name “exponential map” is not metaphorical—for Lie groups with their natural metrics, this map is literally the matrix exponential $e^{tX}$. In general Riemannian geometry, the exponential map satisfies analogous properties that justify the name.

**Implication:** Movement on curved manifolds—including the information manifold—is fundamentally described by exponential structure. The constant *e* is woven into the fabric of how beliefs change.

-----

## 3. The Geometric Self-State Hypothesis

### 3.1 Core Claim

We propose that **self-state creates curvature** in a system’s information manifold.

**Definition (Self-State):** A system has self-state if its generative model includes a representation of its own internal states: p(x, y, s | θ) where s denotes internal state variables that the system models.

**Claim:** The Fisher information metric for a self-modeling system is fundamentally different from that of a non-self-modeling system, creating curvature in the self-state dimensions.

### 3.2 Why Self-Reference Creates Curvature

Consider a system modeling external states x and its own internal states s. The joint distribution is p(x, s; θ). The Fisher information metric includes terms:

$$g_{ss} = E\left[\frac{\partial \log p(x, s; \theta)}{\partial s} \frac{\partial \log p(x, s; \theta)}{\partial s}\right]$$

For a *self-referential* system, s appears on both sides: the system’s state s influences its model of its own state s. This creates a reflexive dependency:

$$p(s | x, \theta) \text{ where } \theta \text{ depends on } s$$

**The geometric consequence:** Self-referential terms create non-zero curvature. The manifold cannot be globally flattened because the coordinate system is self-referential.

### 3.3 The Ruler Problem

This connects to a deep issue in measurement theory: **a ruler cannot measure itself without remainder**.

When a system models itself:

- The model is part of the system
- The system is part of the model
- Complete self-modeling requires infinite regress or incompleteness

This is not a limitation but a *structural feature*. The incompleteness creates curvature—regions of the manifold where self-reference loops back on itself.

### 3.4 Flat vs. Curved Cognitive Geometries

|Property              |Flat Geometry (No Self-State)|Curved Geometry (Self-State)       |
|----------------------|-----------------------------|-----------------------------------|
|**Metric**            |Fixed g_ij(θ)                |State-dependent g_ij(θ, s)         |
|**Parallel transport**|Path-independent             |Path-dependent                     |
|**Geodesics**         |Fixed at training            |Dynamic during inference           |
|**Self-reference**    |Absent                       |Present                            |
|**Dynamics**          |Not state-dependent          |*e*-governed                       |
|**Example system**    |LLM                          |Embedded agent with survival stakes|

-----

## 4. The Convergence: Why Curvature Implies *e*-Governed Dynamics

### 4.1 The Central Insight

The geometric framework (curvature from self-reference) and the dynamical framework (self-reference produces *e*-governed dynamics) are **not independent claims**. They are two perspectives on the same mathematical structure.

**The bridge:** Curvature means the metric depends on position. Position-dependent metric → state-dependent dynamics → *e*-governed evolution.

### 4.2 From Curvature to Dynamics

On a curved manifold, how you move depends on where you are. The geodesic equations are:

$$\frac{d^2\gamma^k}{dt^2} + \Gamma^k_{ij}\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt} = 0$$

where Γ are the Christoffel symbols derived from the metric. When the metric varies with position (curvature ≠ 0), these equations produce state-dependent dynamics.

For self-modeling systems updating beliefs about their own state, the natural dynamics on the information manifold follow:

$$\frac{dS}{dt} = -\nabla_S D_{KL}(q(s) | p(s|x))$$

This is gradient flow on the KL divergence—the system moves to minimize the discrepancy between its self-model q(s) and the true posterior p(s|x).

**Key observation:** KL divergence is defined in terms of natural logarithms. Gradient flow on KL divergence produces exponential approach to equilibrium:

$$D_{KL}(t) = D_{KL}(0) \cdot e^{-kt}$$

The *e* is not imported from outside—it emerges from the intrinsic structure of information geometry.

### 4.3 The Compositionality Connection

The Abstraction Primitive Hypothesis (Danan, 2025a) proposes that abstractions compose—each abstraction can combine with others to form new abstractions. If A(t) denotes abstraction capacity:

$$\frac{dA}{dt} = k \cdot A^\beta$$

where β reflects effective compositionality (β = 1 for linear compositionality, 0 < β < 1 for sublinear).

**For β = 1:** $A(t) = A_0 e^{kt}$ — pure exponential growth

**For 0 < β < 1:** Sublinear dynamics, but *e* remains in the mathematical structure through:

- Equilibrium approach (logistic dynamics involve $e^{-kt}$)
- Information-theoretic quantities (still defined via natural logs)
- Bayesian updating (log-likelihoods)

**Robustness:** The *e* connection holds even when compositionality is sublinear, because it derives from information theory independently of the growth exponent.

### 4.4 Why *e* Specifically?

*e* is the unique positive number satisfying:

$$\frac{d}{dx}e^x = e^x$$

For self-referential systems—where the state and its rate of change are intrinsically coupled—this property is constitutive, not incidental. Self-reference means the system’s state affects its own evolution. The mathematics of such coupling *is* the mathematics of *e*.

|Source                |Why *e* Appears                                          |
|----------------------|---------------------------------------------------------|
|**Compositionality**  |Rate of new abstractions depends on existing abstractions|
|**Information theory**|Entropy, divergence, mutual information use natural logs |
|**Maximum entropy**   |Optimal distributions are exponential families           |
|**Fisher metric**     |Defined via log-likelihood derivatives                   |
|**Geodesic flow**     |Exponential map traces paths on manifold                 |
|**Bayesian updating** |Log-likelihood ratios govern belief revision             |

These are not six separate arguments for *e*—they are six faces of one mathematical structure.

-----

## 5. Hold-and-Check as Parallel Transport

### 5.1 The Computational Problem

**Hold-and-check** requires:

1. **Hold:** Maintain a computed value v across subsequent processing
1. **Check:** Compare current output to held value v

### 5.2 Geometric Formalization

In information-geometric terms, hold-and-check is **parallel transport**:

- The computed value v is a vector in tangent space at state s₁
- Inference moves the system from s₁ to s₂ along path γ
- Parallel transport Pγ(v) moves v along γ to state s₂
- Checking compares Pγ(v) to the current output

**On a flat manifold:** Parallel transport is trivial. Vectors maintain their components in global coordinates.

**On a curved manifold:** Parallel transport is non-trivial. Vectors rotate and stretch as they move along paths. Active maintenance is required.

### 5.3 Why LLMs Fail at Hold-and-Check

**Hypothesis:** LLMs operate on effectively flat manifolds with no machinery for non-trivial parallel transport.

The failure is not that LLMs cannot parallel transport (on a flat manifold, it’s trivial). The failure is that LLMs have **no representation that requires transport**—no held value v that persists as a distinct entity during inference.

|Attention (Retrieval)             |Parallel Transport (Maintenance)|
|----------------------------------|--------------------------------|
|Weighted sum over context         |Vector preserved along path     |
|Computed from scratch at each step|Continuous transformation       |
|Flat geometry sufficient          |Curved geometry required        |
|LLMs have this                    |LLMs lack this                  |

### 5.4 Why Self-State Enables Hold-and-Check

An agent with self-state:

1. Represents its own internal state s as part of its model
1. This creates curvature in the s-dimensions
1. Curvature necessitates active parallel transport
1. The machinery for parallel transport IS hold-and-check capacity

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

## 6. Oscillatory Dynamics: When *π* Joins *e*

### 6.1 Beyond Monotonic Growth

Self-referential systems often exhibit oscillations, not just monotonic growth or decay. This section extends the framework to oscillatory regimes.

### 6.2 The Source of Oscillation: Feedback Delays

**Established:** Oscillations arise in feedback systems when there are delays between action and effect (Strogatz, 2015). Self-referential systems are natural candidates—the self-model is constructed with finite processing time and applied with some lag.

### 6.3 The *e*-*π* Connection

When oscillations enter, *π* joins *e*. The damped oscillator solution is:

$$S(t) = Ae^{-\gamma t}\cos(\omega t + \phi)$$

where:

- *e* governs the **envelope** (damping rate γ)
- *π* governs the **oscillation** (frequency ω = 2π/T)

### 6.4 Euler’s Identity: The Deep Unity

The relationship between *e* and *π* is captured by **Euler’s formula**:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

and **Euler’s identity**:

$$e^{i\pi} + 1 = 0$$

**Interpretation:** An oscillation is the real part of a complex exponential:

$$\cos(\omega t) = \text{Re}(e^{i\omega t})$$

The appearance of both *e* and *π* in self-referential oscillatory systems reflects mathematical unity. State-dependent growth (*e*) and periodic structure (*π*) are aspects of a single object—the complex exponential.

### 6.5 Geometric Interpretation of Oscillation

In information-geometric terms, oscillatory dynamics may correspond to:

**Hypothesis:** Geodesics on certain curved manifolds can spiral or oscillate rather than converge monotonically. When the curvature tensor has appropriate structure, approach to equilibrium involves rotation in the tangent space—producing oscillatory approach to fixed points.

**Formal condition:** Oscillation occurs when the connection has non-trivial holonomy—parallel transport around a closed loop produces rotation. This holonomy introduces *π* into the dynamics.

### 6.6 Conditions for Oscillation

For a delayed self-referential system:

$$\frac{dS}{dt} = -k[S(t) - S^*] + g[S(t-\delta) - S(t)]$$

oscillations occur when:

$$\delta \cdot g > \frac{\pi}{2k}$$

Note that *π* appears in the stability criterion—the threshold for oscillation involves the relationship between delay, gain, and the fundamental oscillatory constant.

-----

## 7. The Ruler Number: Depth of Self-Reference

### 7.1 The Measurement Problem

A ruler cannot measure itself without remainder. Similarly, a system cannot fully model itself—the model is smaller than the system containing it.

This creates a hierarchy:

|Depth|Self-Modeling Capacity|Geometric Signature            |
|-----|----------------------|-------------------------------|
|0    |No self-model         |Flat (R = 0)                   |
|1    |Models own state s    |Curved (R ≠ 0)                 |
|2    |Models own modeling   |Higher-order curvature (∇R ≠ 0)|
|n    |n levels deep         |n-th order structure           |
|∞    |Complete self-model   |Singular (impossible)          |

**Definition (Ruler Number):** The ruler number r is the maximum depth of self-reference before resources exhaust or representations degenerate.

### 7.2 Geometric Interpretation

Each level of self-reference adds structure to the curvature tensor:

- r = 0: R = 0 (flat)
- r = 1: R ≠ 0 (constant curvature)
- r = 2: ∇R ≠ 0 (varying curvature)
- r = n: n-th covariant derivatives non-zero

**Hypothesis:** The ruler number corresponds to the order of non-trivial derivatives of curvature in self-dimensions.

### 7.3 Connection to Dynamical Exponent

The ruler number may relate to the effective compositionality exponent β:

- Higher r → more recursive abstraction capacity → higher effective β
- Lower r → shallower self-reference → β closer to 0

This connects the geometric (curvature order) and dynamical (growth exponent) perspectives.

-----

## 8. Predictions

### 8.1 Geometric-Dynamical Predictions

|Prediction                              |Test                                                  |Falsification                   |
|----------------------------------------|------------------------------------------------------|--------------------------------|
|Self-reference creates curvature        |Analyze Fisher information for self-referential models|G_ss flat despite self-reference|
|Curvature correlates with hold-and-check|Measure both across systems                           |No correlation                  |
|Self-referential dynamics follow *e*    |Fit learning curves for metacognitive tasks           |Power law fits better           |
|Delays produce *e*-*π* oscillations     |Track self-model updating with measurable delay       |No oscillation despite delay    |

### 8.2 LLM-Specific Predictions

|Prediction                               |Test                                   |Falsification                         |
|-----------------------------------------|---------------------------------------|--------------------------------------|
|LLMs have flat self-geometry             |Probe for self-model structure         |Rich self-models found                |
|Architectural self-loops create curvature|Test architectures with self-monitoring|Self-loops don’t help verification    |
|Scaling doesn’t create curvature         |Larger models tested on verification   |Scaling produces verification capacity|

### 8.3 Experimental Designs for Discriminating *e*-Governed Dynamics

**The Asymptote Test:** Power laws don’t asymptote; logistics do. Observe until stabilization.

**The Log-Log vs. Log-Linear Test:** Power laws are linear on log-log plots; exponentials on log-linear plots. Compare R².

**The Characteristic Time Test:** For *e*-governed dynamics:

- Time to 63.2% = τ (one time constant)
- Time to 86.5% = 2τ
- Time to 95.0% ≈ 3τ

Power laws show no such fixed ratios.

**The Intervention Test:** After interruption, decay from any point should follow $e^{-\lambda t}$ for *e*-governed systems.

### 8.4 Oscillation Predictions

|Prediction                                                         |Test                                             |
|-------------------------------------------------------------------|-------------------------------------------------|
|Self-referential systems with delays show oscillatory equilibration|Track meta-cognitive calibration for overshooting|
|Damping/frequency ratio predictable from delay and gain            |Measure independently, test relationship         |
|Paradoxical inputs induce oscillatory instability                  |Present paradoxes, analyze response patterns     |

-----

## 9. Relation to Other Frameworks

### 9.1 Active Inference

Friston’s (2010) active inference uses information geometry extensively:

- Agents minimize variational free energy F
- F has geometric interpretation as divergence on information manifold
- Self-model (generative model including agent’s states) is central

**Connection:** Active inference *requires* curved geometry. Agents doing active inference have self-models → curvature → *e*-governed dynamics. The frameworks are compatible and mutually reinforcing.

### 9.2 Global Workspace Theory

Baars’ (1988) global workspace proposes a “workspace” for global information availability.

**Hypothesis:** Global workspace IS the curved, self-referential region of the information manifold. Information becomes “conscious” when it enters regions with non-trivial parallel transport.

### 9.3 Integrated Information Theory

Tononi’s (2004) IIT proposes consciousness corresponds to integrated information Φ.

**Hypothesis:** Φ may relate to scalar curvature R. Both measure irreducible wholeness of a system.

-----

## 10. Discussion

### 10.1 What This Framework Does

1. **Unifies** geometric (curvature) and dynamical (*e*-governed) perspectives on self-reference
1. **Explains** why *e* appears in information geometry (it’s intrinsic, not imported)
1. **Connects** hold-and-check failures to lack of parallel transport machinery
1. **Generates** testable predictions distinguishing flat from curved cognitive geometries
1. **Extends** to oscillatory dynamics via *π* and Euler’s identity

### 10.2 Honest Uncertainty

|Claim                                        |Status                                                         |
|---------------------------------------------|---------------------------------------------------------------|
|Information geometry is well-founded         |**Established** (Amari, 1985; Čencov, 1982)                    |
|*e* is intrinsic to information geometry     |**Established** (Fisher metric, KL divergence use natural logs)|
|LLMs fail at hold-and-check                  |**Confirmed** (N=700 study)                                    |
|Self-reference creates curvature             |**Hypothesis** (formal proof needed)                           |
|Curvature → *e*-governed dynamics            |**Theoretical** (follows from structure but needs derivation)  |
|Curvature enables hold-and-check             |**Hypothesis** (mechanism plausible, not proven)               |
|Oscillation involves *π* via Euler’s identity|**Hypothesis** (needs formal development)                      |
|Ruler number quantifies self-reference depth |**Speculation** (interesting direction)                        |

### 10.3 Required Future Work

**Mathematical:**

- Formal proof that self-referential Fisher information creates non-zero curvature
- Derivation of *e*-governed dynamics from geodesic flow on self-state manifold
- Characterization of conditions for oscillatory vs. monotonic dynamics

**Empirical:**

- Methods to estimate curvature from neural/computational systems
- Experimental discrimination of *e*-governed from power-law dynamics
- Tests of curvature-verification correlation

-----

## 11. Conclusion

We have proposed that **self-reference creates curvature** in information geometry, and that this curvature both enables hold-and-check capacity and produces *e*-governed dynamics.

The convergence is not coincidental:

- Information geometry is built on natural logarithms (base *e*)
- Self-reference creates state-dependent metric → curvature
- State-dependent dynamics → *e*-governed evolution
- Delayed self-reference → oscillation → *π* enters via Euler’s formula

The geometric and dynamical perspectives are two faces of one mathematical structure. The same *e* that defines the Fisher metric also governs learning curves in self-referential systems. The same curvature that enables parallel transport also produces the state-dependence that yields exponential dynamics.

If correct, the framework has implications for AI development: architectures with explicit self-modeling should develop curved geometries, *e*-governed dynamics, and verification capacity. Scaling alone should not help—more patterns on a flat manifold do not create curvature.

The geometry of mind may not be flat. And that curvature—governed by *e*, occasionally oscillating with *π*, unified by Euler’s identity—may be what distinguishes systems that merely process from systems that know.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Springer.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Baddeley, A. (2000). The episodic buffer. *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS.

Danan, H. (2025a). The self-state hypothesis. *Working paper, Abstraction-Intelligence Framework*.

Danan, H. (2025b). Recursive abstraction: When computation requires self-reference. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Phil. Trans. R. Soc. B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos* (2nd ed.). Westview Press.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5(1), 42.

-----

## Appendix: The Mathematical Unity of *e* and *π* in Self-Reference

Euler’s identity $e^{i\pi} + 1 = 0$ connects five fundamental constants. For self-referential systems:

|Constant|Role in Self-Reference                                      |
|--------|------------------------------------------------------------|
|*e*     |Governs state-dependent dynamics; intrinsic to Fisher metric|
|*π*     |Governs oscillation when feedback has delay                 |
|*i*     |Complex structure enabling rotation in tangent space        |
|1       |Unit of change; baseline for ratios                         |
|0       |Equilibrium; target of self-modeling                        |

The formula $e^{i\theta} = \cos\theta + i\sin\theta$ unifies exponential growth (*e*) with oscillation (*π*). In self-referential systems with delays, both aspects manifest: *e* in the envelope, *π* in the frequency.

This is why Euler’s identity is sometimes called “the most beautiful equation”—it unifies the mathematics of growth with the mathematics of cycles. For self-referential systems navigating curved information manifolds with processing delays, both mathematics apply.

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper, Abstraction-Intelligence Framework*.

-----

*“The mind that knows itself bends the space in which it knows—and that bending is governed by e.”*

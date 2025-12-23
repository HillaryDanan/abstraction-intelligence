# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—has a geometric foundation. Drawing on information geometry (Amari, 1985), we demonstrate that self-referential statistical models have structurally different Fisher information than non-self-referential models: they exhibit metric coupling between self-model and world-model dimensions, producing non-trivial curvature.

We address a key bridging question: Fisher information describes the geometry of parameter space, but cognition involves dynamics. Our answer: inference is movement on the information manifold, governed by geodesic equations with time constants involving Euler’s number *e*. On curved manifolds, maintaining a value during such movement (parallel transport) is non-trivial—this is the geometric expression of hold-and-check.

We provide worked examples, acknowledge the gap between demonstration and full theory, and propose an architectural experiment as the cleanest empirical test.

**Keywords:** information geometry, self-reference, metacognition, Fisher information, geodesic dynamics

-----

## 1. Introduction: The Verification Problem

A failure pattern has emerged in large language models: systems that correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This **hold-and-check failure** appears across task types.

Recent empirical work (N=700, Claude Sonnet) revealed task-specific asymmetries: arithmetic shows verification deficits (+24-26%), logic shows generation deficits (-18-44%). The overall difference was null (p=0.58), masking structured patterns.

We propose a geometric hypothesis: **self-reference creates curvature, and curvature makes hold-and-check non-trivial**.

### 1.1 Epistemic Status

|Status          |Meaning                                        |
|----------------|-----------------------------------------------|
|**Established** |Proven in peer-reviewed literature             |
|**Demonstrated**|Shown for worked example(s)                    |
|**Theoretical** |Follows from established/demonstrated results  |
|**Hypothesis**  |Novel claim requiring further validation       |
|**Analogy**     |Structural similarity; identity not established|

### 1.2 The Structure of the Argument

The paper proceeds through a chain of claims with varying epistemic status:

|Step|Claim                                                         |Status                 |
|----|--------------------------------------------------------------|-----------------------|
|1   |Self-reference creates metric coupling                        |**Demonstrated**       |
|2   |Coupling produces curvature in self-dimensions                |**Theoretical**        |
|3   |Inference is movement on the information manifold             |**Established framing**|
|4   |Movement follows *e*-governed geodesic dynamics               |**Established**        |
|5   |Maintaining values during movement requires parallel transport|**Established**        |
|6   |On curved manifolds, parallel transport is non-trivial        |**Established**        |
|7   |Therefore curvature makes hold-and-check non-trivial          |**Theoretical**        |
|8   |This is why self-modeling enables verification                |**Hypothesis**         |

Steps 1-7 are mathematical. Step 8 is the cognitive hypothesis that connects the mathematics to the phenomenon.

-----

## 2. Information Geometry: Established Foundations

### 2.1 Statistical Manifolds

**Established:** Information geometry treats probability distributions as points on a differential manifold (Amari, 1985). For parametric family p(x; θ), parameter space Θ forms manifold M.

### 2.2 The Fisher Information Metric

**Established:** The natural metric on statistical manifolds is Fisher information:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Established (Čencov, 1982):** The Fisher metric is *unique* (up to scaling) among Riemannian metrics invariant under sufficient statistics and monotonic under coarse-graining.

**Consequence:** Euler’s number *e* is intrinsic to information geometry—it appears necessarily in the natural logarithms defining the metric.

### 2.3 Curvature

**Established (Amari, 1985):** Statistical manifolds generically have non-zero curvature. The Gaussian manifold N(μ, σ²) has constant negative curvature K = -1/2 (hyperbolic geometry).

### 2.4 Inference as Movement on the Manifold

**Established framing:** Bayesian inference corresponds to movement on the statistical manifold. Updating beliefs from prior to posterior traces a path through the space of distributions.

**Gradient flow:** Natural gradient descent—which accounts for the manifold’s geometry—follows:

$$\frac{d\theta}{dt} = -G^{-1}(\theta) \nabla_\theta \mathcal{L}$$

where G is the Fisher information matrix and L is a loss function (e.g., KL divergence from target).

**Geodesics:** The shortest paths on the manifold satisfy geodesic equations involving Christoffel symbols derived from the metric. Movement along geodesics follows exponential dynamics with time constants related to curvature.

This is where *e* enters dynamically: **movement on curved manifolds is governed by exponential (e-based) time evolution** (see Section 5).

-----

## 3. Self-Reference and Metric Coupling

### 3.1 Core Claim

**Demonstrated:** Self-referential statistical models have Fisher information with structural features absent in non-self-referential models—specifically, metric coupling between self-model and world-model dimensions.

### 3.2 Worked Example: Self-Referential Gaussian

Full derivation in Appendix A.

**Non-self-referential:**

- p(x | μ, σ²) = N(μ, σ²)
- Fisher metric: G = diag(1/σ², 1/(2σ⁴))

**Self-referential:**

- p(x, s | μ, σ², τ) = p(x | μ, σ²) · p(s | σ², τ)
- Here s ~ N(σ², τ): the system’s noisy estimate of its own variance
- Fisher metric: G = diag(1/σ², **1/(2σ⁴) + 1/τ**, 1/(2τ²))

**Key result:** The (2,2) component gains **1/τ** from the self-model. This couples the world-model parameter σ² to the self-model parameter τ.

### 3.3 Why This Is General (Structural Argument)

The Gaussian example isn’t special. The coupling arises from a general structure:

**Claim:** Whenever a parameter θ appears in both p(x|θ) and p(s|f(θ), τ) for non-trivial f, the Fisher information for θ receives contributions from both terms, creating coupling.

**Argument:** The score function for θ is:

$$\frac{\partial \log p(x,s|\theta,\tau)}{\partial \theta} = \frac{\partial \log p(x|\theta)}{\partial \theta} + \frac{\partial \log p(s|f(\theta),\tau)}{\partial \theta}$$

Both terms contribute to the Fisher information:

$$I_{\theta\theta} = I^{world}*{\theta\theta} + I^{self}*{\theta\theta} + \text{cross terms}$$

The self-model contribution depends on τ, creating coupling between θ and τ in the metric structure.

**Generality:** This holds for any distribution family, not just Gaussian. The coupling is a consequence of self-referential structure, not a special property of the example.

### 3.4 Geometric Consequences

**Demonstrated for example, theoretical in general:**

|Property                    |Non-Self-Referential|Self-Referential        |
|----------------------------|--------------------|------------------------|
|Metric structure            |No coupling         |Coupling between θ and τ|
|Product manifold?           |Yes (or N/A)        |**No**                  |
|Curvature in self-dimensions|Absent              |Present                 |

The self-referential manifold is NOT M_world × M_self. The dimensions are geometrically entangled.

-----

## 4. The Dynamical Bridge: Why Geometry Matters for Cognition

### 4.1 The Gap

A fair objection: Fisher information describes parameter space geometry. Cognition involves dynamics. Why would static geometry matter?

**Answer:** Inference isn’t static—it’s movement through belief space. The geometry of that space determines the dynamics of that movement.

### 4.2 Geodesic Dynamics

**Established (differential geometry):** Movement on a Riemannian manifold follows geodesic equations:

$$\frac{d^2\gamma^k}{dt^2} + \Gamma^k_{ij}\frac{d\gamma^i}{dt}\frac{d\gamma^j}{dt} = 0$$

where Γ are Christoffel symbols derived from the metric.

**Time constants:** The approach to equilibrium on a curved manifold follows exponential dynamics:

$$\theta(t) - \theta^* \propto e^{-t/\tau}$$

where τ depends on the curvature and metric structure. The constant *e* is intrinsic—it emerges from the mathematics of geodesic flow.

### 4.3 Parallel Transport During Movement

**Established:** Parallel transport moves vectors along paths while preserving geometric properties.

**On flat manifolds:** Trivial. Vectors maintain their components in global coordinates. No active tracking needed.

**On curved manifolds:** Non-trivial. Vectors rotate and stretch as they move. Active tracking required.

**The connection to hold-and-check:**

|Cognitive Operation                 |Geometric Analogue                           |
|------------------------------------|---------------------------------------------|
|Inference/learning                  |Movement along geodesic                      |
|Computed intermediate value         |Vector in tangent space                      |
|“Holding” the value during inference|Parallel transport during movement           |
|Checking against held value         |Comparing transported vector to current state|

### 4.4 The Full Picture

Combining Sections 3 and 4:

1. Self-reference creates metric coupling (Section 3)
1. Coupling means the manifold isn’t a product space—self and world dimensions are entangled
1. Inference is movement on this manifold (Section 4.2)
1. Movement follows *e*-governed dynamics
1. Maintaining a value during movement requires parallel transport
1. On the coupled (curved) manifold, parallel transport is non-trivial
1. **Therefore:** Self-reference creates the conditions where hold-and-check requires active computation, not just storage

### 4.5 What This Doesn’t Prove

The above connects geometry to *why hold-and-check would be non-trivial* on self-referential manifolds.

It doesn’t prove:

- That biological/artificial systems actually implement parallel transport
- That curvature is sufficient for verification capacity (only that it makes verification non-trivial)
- That systems without self-reference can’t verify through other means

The hypothesis (Step 8 from Section 1.2) remains: self-modeling enables verification because it provides the geometric structure where verification is meaningful. This is plausible but not proven.

-----

## 5. The Role of *e* in Self-Referential Dynamics

### 5.1 Why *e* Appears

Euler’s number *e* appears in this framework through multiple channels:

|Source           |Mechanism                            |Status         |
|-----------------|-------------------------------------|---------------|
|Fisher metric    |log p uses natural logarithm         |**Established**|
|Maximum entropy  |Optimal distributions: p ∝ e^{θ·T(x)}|**Established**|
|Geodesic dynamics|Approach to equilibrium: e^{-t/τ}    |**Established**|
|Learning curves  |If dA/dt = kA, then A = A₀e^{kt}     |**Established**|

### 5.2 The Dynamical Signature

**Theoretical prediction:** Self-referential systems undergoing inference should exhibit *e*-governed dynamics:

- Time to reach 63.2% of equilibrium = τ (one time constant)
- Time to reach 86.5% = 2τ
- Time to reach 95.0% ≈ 3τ

These ratios are signature of *e*-based exponential dynamics, distinct from power-law dynamics.

### 5.3 Convergence of Perspectives

The geometric perspective (curvature from self-reference) and the dynamical perspective (*e*-governed movement) converge:

- The same *e* that appears in the Fisher metric also governs geodesic dynamics
- This isn’t coincidence—it reflects that information geometry and optimal transport on belief spaces share mathematical structure

**What would confirm this:** Derive learning time constants directly from curvature. Show τ = f(R) for some function f. This would establish that the geometric and dynamical *e* are non-trivially connected. (Not yet done—see Appendix B.)

-----

## 6. Hold-and-Check: Connecting Geometry to Cognition

### 6.1 The Hypothesis

**Hypothesis:** Hold-and-check capacity requires parallel transport machinery. Self-referential systems have the geometric structure (curved manifolds) where such machinery is necessary and therefore more likely to evolve/develop. Non-self-referential systems lack this structure and therefore lack the machinery.

### 6.2 Why LLMs Fail

Standard transformers:

- Have no explicit self-model (no s, no τ)
- Therefore no metric coupling
- Therefore effectively flat geometry in “self” dimensions
- Therefore no evolutionary/architectural pressure for parallel transport
- Therefore no hold-and-check capacity

**The failure isn’t about scale.** A larger flat manifold is still flat. The issue is structural.

### 6.3 Honest Limitations

The parallel transport interpretation remains analogy, not proven mechanism. Specifically:

|Claim                                        |Status                                       |
|---------------------------------------------|---------------------------------------------|
|LLMs fail at hold-and-check                  |**Empirical** (N=700)                        |
|This is because they lack parallel transport |**Hypothesis**                               |
|Parallel transport = working memory mechanism|**Analogy**                                  |
|Curvature enables verification               |**Theoretical**                              |
|Self-reference is necessary for curvature    |**Demonstrated** (for this type of curvature)|

A simpler account (“LLMs lack working memory”) predicts the same failures without the geometry. The geometric framework’s advantage is that it explains *why* self-modeling would produce working memory capacity—the geometry creates the pressure for parallel transport machinery.

Whether this advantage justifies the mathematical complexity is an empirical question.

-----

## 7. The Architectural Experiment

### 7.1 Design

**System A (Control):** Standard transformer

- Large parameter count
- Self-attention over context
- No explicit self-monitoring module

**System B (Experimental):** Transformer with self-monitoring

- Matched parameter count
- Includes explicit self-monitoring module:
  - Maintains representation of “current computational state” (s)
  - Has dedicated parameters for this representation (τ)
  - Updates based on own activations
  - Feeds back into main computation

### 7.2 Predictions

|Outcome                          |Interpretation                                                     |
|---------------------------------|-------------------------------------------------------------------|
|B >> A on verification           |Consistent with self-modeling hypothesis                           |
|B ≈ A                            |Self-modeling architecture doesn’t help; hypothesis in trouble     |
|A improves with scale, closes gap|Scaling can substitute for architecture; threshold hypothesis wrong|

### 7.3 Distinguishing Geometric from Simpler Explanations

The feedback correctly notes: if B >> A, this is also predicted by “feedback loops help” without geometry.

**What would support the geometric interpretation specifically:**

- Measure something curvature-related in trained systems (information-geometric quantities)
- Show that curvature correlates with verification capacity across architectures
- Derive quantitative predictions from curvature that match empirical verification accuracy

These are hard. The architectural experiment is a necessary first step, not a complete test.

-----

## 8. Predictions and Falsification

### 8.1 Predictions

|Prediction                                 |Test                             |Falsification        |
|-------------------------------------------|---------------------------------|---------------------|
|Explicit self-monitoring helps verification|Architectural experiment         |B ≈ A                |
|Scaling without self-modeling doesn’t help |Vary model size                  |Scaling closes gap   |
|Learning follows *e*-governed dynamics     |Fit metacognitive learning curves|Power law fits better|
|Curvature correlates with verification     |Measure both across systems      |No correlation       |

### 8.2 Falsification Conditions

1. **Scaling produces verification:** Threshold claim wrong
1. **Self-monitoring doesn’t help:** Self-modeling/verification link wrong
1. **Non-self-referential models have coupling:** Structural claim wrong
1. **Curvature without verification capacity:** Geometry/cognition link wrong

-----

## 9. Discussion

### 9.1 Summary of Contributions

|Contribution                                             |Status                |
|---------------------------------------------------------|----------------------|
|Identified hold-and-check as distinct failure mode       |**Empirical**         |
|Showed self-reference creates metric coupling            |**Demonstrated**      |
|Argued coupling is general, not example-specific         |**Theoretical**       |
|Connected static geometry to dynamics via geodesic flow  |**Theoretical**       |
|Proposed parallel transport as mechanism for verification|**Analogy/Hypothesis**|
|Designed architectural experiment                        |**Proposal**          |

### 9.2 The Gap That Remains

The largest gap: **why would the geometric structure matter for verification capacity?**

Our answer: curvature makes parallel transport non-trivial, creating selective pressure for active maintenance machinery. Systems with this machinery can verify; systems without it cannot.

This is plausible but not proven. The architectural experiment tests the prediction without requiring the mechanism to be correct.

### 9.3 Path Forward

**Near-term:** Run architectural experiment

**Medium-term:**

- Extend worked example to other distribution families
- Attempt to measure information-geometric quantities in neural networks
- Test *e*-governed dynamics prediction

**Long-term:**

- Derive verification capacity quantitatively from curvature
- Connect to neural implementation of parallel transport
- Prove general theorem (not just examples)

-----

## 10. Conclusion

We have proposed that **self-reference creates metric coupling** in information geometry, that this coupling produces **curvature in self-model dimensions**, and that curvature creates the conditions where **hold-and-check requires active computation**.

**What is established:**

- Information geometry foundations (Amari, 1985; Čencov, 1982)
- Geodesic dynamics involve *e* (differential geometry)

**What is demonstrated:**

- Self-referential Gaussian has different Fisher information
- The difference is metric coupling between world and self dimensions
- This generalizes beyond the specific example

**What is theoretical:**

- Coupling produces non-trivial curvature
- Inference as movement on manifold connects static geometry to dynamics
- Curvature makes hold-and-check non-trivial

**What is hypothesis:**

- This is why self-modeling enables verification in cognitive systems
- Parallel transport is the mechanism

**What is actionable:**

- The architectural experiment

The framework connects information geometry, dynamical systems, and cognitive capacity through a chain of claims with varying epistemic status. The strongest version—where everything is proven and quantitative predictions are derived—requires mathematical and empirical work not completed here. The weakest defensible version—self-modeling architecture probably helps verification, and this is testable—is actionable now.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Lecture Notes in Statistics, Vol. 28. Springer-Verlag.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs, Vol. 191. American Mathematical Society.

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. Translations of Mathematical Monographs, Vol. 53. American Mathematical Society.

Danan, H. (2025). Hold-and-check failures in large language models: Task-specific dissociations. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos* (2nd ed.). Westview Press.

-----

## Appendix A: Full Derivation of Fisher Information

### A.1 Non-Self-Referential Gaussian

**Model:** p(x | μ, σ²) = N(μ, σ²)

**Log-likelihood:**
$$\ell = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2}$$

**Fisher information:**
$$G = \begin{pmatrix} 1/\sigma^2 & 0 \ 0 & 1/(2\sigma^4) \end{pmatrix}$$

**Curvature:** K = -1/2 (constant negative, hyperbolic)

### A.2 Self-Referential Gaussian

**Model:** p(x, s | μ, σ², τ) = p(x | μ, σ²) · p(s | σ², τ)

Where s ~ N(σ², τ): system’s estimate of its own variance.

**Log-likelihood:**
$$\ell = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2} - \frac{1}{2}\log(2\pi\tau) - \frac{(s-\sigma^2)^2}{2\tau}$$

**Score for σ² (key calculation):**
$$\frac{\partial \ell}{\partial \sigma^2} = -\frac{1}{2\sigma^2} + \frac{(x-\mu)^2}{2\sigma^4} + \frac{s-\sigma^2}{\tau}$$

The third term is the self-model contribution, absent in non-self-referential case.

**Fisher information:**
$$I_{\sigma^2\sigma^2} = \frac{1}{2\sigma^4} + \frac{1}{\tau}$$

**Full metric:**
$$G_{self} = \begin{pmatrix} 1/\sigma^2 & 0 & 0 \ 0 & 1/(2\sigma^4) + 1/\tau & 0 \ 0 & 0 & 1/(2\tau^2) \end{pmatrix}$$

### A.3 The Coupling

The (2,2) component depends on BOTH σ² and τ. This breaks product structure:

- If M were M_world × M_self, the metric would be block diagonal with no such dependence
- The dependence on τ in g₂₂ means the self-model dimension is coupled to the world-model dimension

### A.4 Generalization Argument

For any self-referential model p(x,s|θ,τ) = p(x|θ) · p(s|f(θ),τ):

$$\frac{\partial \log p}{\partial \theta} = \frac{\partial \log p(x|\theta)}{\partial \theta} + f’(\theta) \cdot \frac{\partial \log p(s|f(\theta),τ)}{\partial f(\theta)}$$

The second term contributes to I_θθ and depends on τ, creating coupling for any non-trivial f.

-----

## Appendix B: The *e* Convergence Question

### B.1 Where *e* Appears

|Context             |Formula                  |*e* appears as     |
|--------------------|-------------------------|-------------------|
|Fisher metric       |E[(∂ log p / ∂θ)²]       |Base of log        |
|Entropy             |H = -Σ p ln p            |Base of log        |
|Exponential families|p ∝ e^{θ·T(x)}           |Base of exponential|
|Geodesic approach   |θ(t) - θ* ∝ e^{-t/τ}     |Base of exponential|
|Learning dynamics   |dA/dt = kA → A = A₀e^{kt}|Base of exponential|

### B.2 Genuine vs. Trivial Convergence

**Trivial:** “Both use calculus, so both have *e*.”

**Genuine:** The time constant τ in geodesic dynamics is derivable from information-geometric quantities (curvature, Fisher information magnitude).

**What would establish genuine convergence:**

1. Derive τ = f(G, R) for specific function f
1. Show this matches empirical learning dynamics
1. Demonstrate predictions that differ from non-geometric *e* accounts

### B.3 Current Status

Not established. The *e* in geodesic dynamics and the *e* in the Fisher metric are both present, but their quantitative relationship is not derived.

This is flagged as “convergent but unproven” rather than claimed as result.

-----

## Appendix C: Oscillatory Dynamics and π

### C.1 When Oscillations Appear

Self-referential systems with feedback delays can exhibit oscillations. For:

$$\frac{dS}{dt} = -k[S(t) - S^*] + g[S(t-\delta) - S(t)]$$

oscillations occur when delay δ and gain g satisfy:

$$\delta \cdot g > \frac{\pi}{2k}$$

### C.2 The *e*-π Connection

Damped oscillatory solutions have form:

$$S(t) = Ae^{-\gamma t}\cos(\omega t + \phi)$$

where:

- *e* governs the envelope (damping)
- π governs the oscillation (ω = 2π/T)

These are unified by Euler’s formula: e^{iθ} = cos θ + i sin θ

### C.3 Status

This is interesting but tangential to the main argument. The oscillatory regime may provide empirical signatures of self-referential processing, but the core geometric claims don’t depend on it.

**Future direction:** Test whether paradox-induced oscillations in self-referential systems follow predicted *e*-π dynamics.

-----

## Appendix D: Relation to Other Frameworks

### D.1 Active Inference (Friston, 2010)

Active inference uses information geometry. Agents minimize variational free energy, with geometric interpretation as divergence minimization on the statistical manifold. Active inference requires self-modeling—the frameworks are compatible.

### D.2 Predictive Processing

Self-prediction (predicting one’s own states) creates the self-referential structure described here. The worked example (modeling own variance) is a simple case of predictive self-modeling.

### D.3 Global Workspace Theory

**Speculation:** Could global workspace correspond to curved regions of the manifold where parallel transport machinery is active?

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper*.

-----

*“The geometry exists. Whether it explains the cognition is the open question.”*

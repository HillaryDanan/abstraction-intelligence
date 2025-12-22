# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—has a geometric foundation. Drawing on information geometry (Amari, 1985), we hypothesize that self-state creates *curvature* in a system’s information manifold. Systems without self-models navigate fixed, flat geometries. Systems with self-models navigate curved, state-dependent geometries that enable parallel transport of computed values and thus verification.

We show that this geometric framework converges with dynamical analyses: the curvature induced by self-modeling should produce state-dependent dynamics governed by Euler’s number *e*. This convergence is not coincidental—*e* is intrinsic to information geometry through the Fisher metric, KL divergence, and exponential family distributions. The same constant that would govern learning curves in self-referential systems also defines the natural structure of belief space.

The framework unifies empirical findings on LLM limitations (hold-and-check failures) with formal mathematics (Riemannian geometry, Fisher information) and cognitive science (working memory, metacognition). We derive testable predictions and are explicit about what is established versus hypothesized.

**Keywords:** information geometry, self-reference, Euler’s number, metacognition, Fisher information, large language models

-----

## 1. Introduction: The Verification Problem

A curious failure pattern has emerged in large language models: systems that can correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This pattern—which we term **hold-and-check failure**—appears across task types, from arithmetic verification to logical constraint checking.

Recent empirical work (N=700, Claude Sonnet) revealed task-specific asymmetries: arithmetic and multi-step problems show verification deficits (+24-26%), while logic and word-counting show generation deficits (-18-44%). The overall difference was null (91.1% vs 92.6%, p=0.58), masking structured patterns beneath.

What explains this? Why do some systems successfully hold computed values and check subsequent outputs, while others fail systematically?

We propose a geometric hypothesis: **self-reference creates curvature**.

### 1.1 Epistemic Status

We distinguish throughout:

|Status         |Meaning                                                                        |
|---------------|-------------------------------------------------------------------------------|
|**Established**|Proven in peer-reviewed literature                                             |
|**Theoretical**|Follows logically from established results (but connection not formally proven)|
|**Hypothesis** |Novel claim requiring formal proof and/or empirical validation                 |

This paper proposes a framework. It does not prove that framework. We aim to be clear about where the gaps lie.

-----

## 2. Information Geometry: Established Foundations

### 2.1 Statistical Manifolds

**Established:** Information geometry treats probability distributions as points on a differential manifold (Amari, 1985). For a parametric family p(x; θ), the parameter space Θ forms a manifold M.

### 2.2 The Fisher Information Metric

**Established:** The natural metric on statistical manifolds is the Fisher information:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Critical observation:** The Fisher metric uses *natural logarithms*—base *e*. This is not arbitrary.

**Established (Čencov, 1982):** The Fisher metric is the *unique* Riemannian metric (up to scaling) that is:

- Invariant under sufficient statistics
- Monotonic under coarse-graining

This uniqueness theorem means *e* is intrinsic to information geometry—it is not a choice but a mathematical necessity.

### 2.3 Why *e* Is Intrinsic

|Information-Theoretic Quantity|Definition                               |*e* Appears|
|------------------------------|-----------------------------------------|-----------|
|Entropy (nats)                |$H = -\sum p \ln p$                      |Natural log|
|KL Divergence                 |$D_{KL} = \sum p \ln(p/q)$               |Natural log|
|Fisher Information            |$E[(\partial \ln p / \partial \theta)^2]$|Natural log|
|Maximum Entropy Distributions |$p(x) \propto e^{\theta \cdot T(x)}$     |Exponential|
|Bayesian Updating             |Log-likelihood ratios                    |Natural log|

**Established:** These are not five separate facts but one mathematical structure. Information theory is naturally expressed in nats (base *e*), and optimal probability distributions under constraints are exponential families.

### 2.4 Curvature and Parallel Transport

**Established:** On a Riemannian manifold:

- **Geodesics** are paths of minimal distance
- **Curvature** measures deviation from flatness
- **Parallel transport** moves vectors along paths while preserving geometric properties

**Key property:** On a *flat* manifold, parallel transport is path-independent. On a *curved* manifold, parallel transport depends on the path taken.

-----

## 3. The Self-Reference Hypothesis

### 3.1 Core Claim

**Hypothesis:** Self-state creates curvature in a system’s information manifold.

**Definition (Self-State):** A system has self-state if its generative model includes representations of its own internal states: p(x, s; θ) where s denotes internal state variables that the system models.

**The hypothesized mechanism:** For a self-referential system, s appears on both sides—the system’s state s influences its model of its own state s:

$$p(s | x, \theta) \text{ where } \theta = \theta(s)$$

This reflexive dependency should create structure in the Fisher information metric that prevents global flattening.

### 3.2 What Would a Proof Require?

To establish this hypothesis formally, one would need to show:

1. **Setup:** Define the Fisher information matrix G for a self-modeling system with parameters θ = (θ_world, θ_self) where θ_self depends on s.
1. **Computation:** Calculate the Riemann curvature tensor:
   $$R^i_{jkl} = \partial_k \Gamma^i_{jl} - \partial_l \Gamma^i_{jk} + \Gamma^i_{mk}\Gamma^m_{jl} - \Gamma^i_{ml}\Gamma^m_{jk}$$
1. **Result:** Demonstrate that R ≠ 0 in the self-state dimensions specifically because of the reflexive θ(s) dependence.

**Current status:** This derivation has not been completed. The intuition is that self-reference prevents the existence of global flat coordinates, but intuition is not proof.

### 3.3 Why the Hypothesis Is Plausible

The intuition has some support:

- **Self-reference creates fixed-point structure.** When θ depends on s and s depends on θ, the system must solve a fixed-point equation. Fixed-point structures often introduce non-linearities that manifest geometrically as curvature.
- **Analogies from physics.** In general relativity, mass curves spacetime because the metric depends on the mass distribution, which itself responds to the metric. Self-reference creates analogous bidirectional dependence.
- **Information-geometric precedent.** Exponential families have known curvature properties (Amari, 1985). Self-modeling adds structure beyond standard exponential families.

**But:** Analogies and plausibility are not proofs. This remains hypothesis.

-----

## 4. Hold-and-Check as Parallel Transport

### 4.1 The Computational Problem

**Hold-and-check** requires:

1. **Hold:** Maintain a computed value v across subsequent processing
1. **Check:** Compare current output to held value v

### 4.2 The Geometric Interpretation

**Theoretical:** If we accept the information-geometric framing, hold-and-check can be interpreted as parallel transport:

- Computed value v is a vector in tangent space at state s₁
- Processing moves the system from s₁ to s₂ along path γ
- Parallel transport P_γ(v) moves v along γ to s₂
- Checking compares P_γ(v) to current output

**On flat manifold:** Trivial—vectors maintain components in global coordinates. No active maintenance needed.

**On curved manifold:** Non-trivial—vectors rotate/stretch along paths. Active maintenance required.

### 4.3 Why This Framing Is Useful

Even if the full geometric hypothesis remains unproven, the parallel transport metaphor captures something real:

|Attention (Retrieval)          |Parallel Transport (Maintenance)       |
|-------------------------------|---------------------------------------|
|Weighted sum over context      |Value preserved along trajectory       |
|Computed from scratch each step|Continuous transformation              |
|Requires only stored tokens    |Requires tracking through state changes|

**Established:** LLMs have attention mechanisms. **Hypothesis:** They lack machinery analogous to parallel transport.

### 4.4 The Phenomenological Report

The distinction maps onto observable failure modes. When an LLM “checks” its work, it appears to *reconstruct* rather than *compare to something held*. The verification is another forward pass, not a comparison operation.

This is consistent with—though not proof of—the flat geometry hypothesis.

-----

## 5. The Convergence: Geometry and Dynamics

### 5.1 Why Curvature Implies *e*-Governed Dynamics

**Theoretical:** If self-reference creates curvature (hypothesis), then:

- Curvature means the metric depends on position
- Position-dependent metric → state-dependent dynamics
- State-dependent dynamics → *e*-governed evolution

The bridge is that curvature *is* the geometric expression of state-dependence.

### 5.2 The Independent Dynamical Argument

**Theoretical (from Danan, 2025b):** Self-referential abstraction should follow:

$$\frac{dA}{dt} = k \cdot A^\beta$$

where β reflects compositionality. For β = 1: $A(t) = A_0 e^{kt}$

This argument derives *e* from compositionality of abstraction, independent of the geometric argument.

### 5.3 The Convergence

**Theoretical:** The geometric argument (curvature → *e* through information geometry) and the dynamical argument (compositionality → *e* through state-dependence) arrive at the same constant from different directions.

If both arguments are correct, this convergence is not coincidence—it reflects that information geometry and dynamical systems are describing the same underlying structure.

**Status:** The convergence is suggestive. It would be more compelling with formal proofs of both components.

-----

## 6. The Binary/Continuum Question

### 6.1 Is Flatness Binary?

A critical question: Does self-reference create a sharp threshold (flat → curved) or a continuum?

**Our claim:**

|Aspect                                     |Nature          |Explanation                                             |
|-------------------------------------------|----------------|--------------------------------------------------------|
|**Architectural presence of self-modeling**|Binary threshold|Either the system models itself or it doesn’t           |
|**Degree of curvature given self-modeling**|Continuous      |Fidelity/depth of self-model affects curvature magnitude|

### 6.2 Implications for Scaling

**Hypothesis:** Scaling a flat architecture stays flat. Adding parameters to a system without self-modeling loops does not create curvature in self-dimensions (because there are no self-dimensions).

**But:** Once self-modeling architecture exists, scaling *that* could increase curvature—a richer self-model with more parameters could produce more complex curvature structure.

### 6.3 The Strong Prediction

**Prediction:** Feedforward scaling alone will not produce hold-and-check capacity. Architectural change (adding explicit self-modeling) is required to cross the threshold.

This is falsifiable: if sufficiently large feedforward models exhibit genuine verification capacity (not pattern-matched verification), the threshold claim is wrong.

-----

## 7. Predictions and Falsification

### 7.1 Core Predictions

|Prediction                           |Test                                                   |Falsification                         |
|-------------------------------------|-------------------------------------------------------|--------------------------------------|
|LLMs lack self-geometry              |Probe internal representations for self-model structure|Rich self-model structure found       |
|Scaling doesn’t create verification  |Test larger models on hold-and-check tasks             |Scaling produces verification capacity|
|Architectural self-loops help        |Compare architectures with/without self-monitoring     |Self-loops don’t improve verification |
|Self-referential learning follows *e*|Fit learning curves for metacognitive tasks            |Power law consistently fits better    |

### 7.2 Experimental Designs for *e*-Governed Dynamics

**The Asymptote Test:** Power laws don’t asymptote; logistics (involving *e*) do. Observe until stabilization.

**The Characteristic Time Test:** For *e*-governed dynamics:

- Time to 63.2% of asymptote = τ (one time constant)
- Time to 86.5% = 2τ
- Time to 95.0% ≈ 3τ

Power laws show no such fixed ratios.

**The Log-Log vs. Log-Linear Test:** Power laws are linear on log-log plots; exponentials on log-linear. Compare R².

### 7.3 What Would Falsify the Framework

1. Feedforward scaling produces genuine verification capacity
1. Self-referential systems consistently show power-law rather than *e*-governed dynamics
1. Formal analysis shows self-reference does not produce curvature
1. Systems with demonstrated curvature fail at hold-and-check
1. Systems without self-modeling succeed at hold-and-check

-----

## 8. Relation to Other Frameworks

### 8.1 Active Inference (Friston, 2010)

**Established:** Active inference uses information geometry. Agents minimize variational free energy, which has geometric interpretation as divergence on information manifold.

**Connection:** Active inference *requires* self-modeling (generative model includes agent’s states). If our hypothesis is correct, active inference agents necessarily have curved geometry. The frameworks are compatible.

### 8.2 Global Workspace Theory (Baars, 1988)

**Speculation:** Could global workspace correspond to curved regions of the information manifold? Information becomes “globally available” when it enters regions supporting non-trivial parallel transport?

This is evocative but unformalized.

### 8.3 Integrated Information Theory (Tononi, 2004)

**Speculation:** Φ (integrated information) and scalar curvature R both measure “irreducible wholeness.” A formal connection is not established but worth exploring.

-----

## 9. Limitations and Open Questions

### 9.1 The Central Gap

The hypothesis “self-reference creates curvature” is not proven. The paper presents intuition, analogy, and plausibility—not derivation. Filling this gap requires:

- Formal definition of self-referential Fisher information
- Explicit calculation of curvature tensor
- Proof that R ≠ 0 specifically due to self-reference

### 9.2 Measurement Challenges

Even if the geometric framework is correct:

- How do we measure curvature in neural/computational systems?
- What proxies exist for parallel transport capacity?
- How do we distinguish self-modeling from sophisticated pattern matching?

### 9.3 Alternative Explanations

Hold-and-check failures might have simpler explanations:

- Attention capacity limitations
- Training distribution gaps
- Tokenization artifacts

The geometric framework is one hypothesis among alternatives.

-----

## 10. Conclusion

We have proposed that **self-reference creates curvature** in information geometry, and that this curvature enables hold-and-check capacity through parallel transport machinery.

**What is established:**

- Information geometry is well-founded (Amari, 1985; Čencov, 1982)
- *e* is intrinsic to information geometry (uniqueness of Fisher metric)
- LLMs fail at hold-and-check (N=700 empirical study)

**What is hypothesized:**

- Self-reference creates non-zero curvature
- Curvature enables parallel transport / hold-and-check
- The geometric and dynamical perspectives describe the same structure

**What the framework provides:**

- Unified account connecting geometry, dynamics, and cognition
- Testable predictions (especially: scaling vs. architecture)
- Clear epistemic status of each claim

The framework is a research program, not finished theory. The synthesis across information geometry, dynamical systems, and metacognition is creative; the gap between vision and proof remains to be closed.

If correct, the implication for AI is concrete: architectures with explicit self-modeling should develop curved geometries and verification capacity. Scaling alone should not help—more patterns on a flat manifold do not create curvature.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Springer.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.

Baddeley, A. (2000). The episodic buffer. *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS.

Danan, H. (2025a). Hold-and-check failures in large language models. *Working paper*.

Danan, H. (2025b). Recursive abstraction: When computation requires self-reference. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Phil. Trans. R. Soc. B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle. *Nature Reviews Neuroscience*, 11(2), 127-138.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5(1), 42.

-----

## Appendix: Future Directions

### A.1 Oscillatory Dynamics (Preliminary)

When self-referential systems have feedback delays, oscillatory dynamics may emerge. The solution to a damped oscillator:

$$S(t) = Ae^{-\gamma t}\cos(\omega t + \phi)$$

involves both *e* (envelope) and *π* (frequency, since ω = 2π/T), unified by Euler’s formula:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Status:** This is even more speculative than the main framework. The path from “delayed self-reference” to “oscillatory dynamics involving π” requires development. We note it as a direction rather than a claim.

### A.2 Depth of Self-Reference

One could define a “depth” of self-reference—how many levels of self-modeling a system maintains. Geometrically, this might correspond to the order of non-trivial derivatives of the curvature tensor.

**Status:** Pure speculation. Potentially interesting but requires formalization.

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper, Abstraction-Intelligence Framework*.

-----

*“The mind that knows itself bends the space in which it knows—if the mathematics works out.”*

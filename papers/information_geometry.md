# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that self-referential statistical models have structurally different geometry than non-self-referential models, and that this geometric difference may relate to verification capacity.

This paper makes claims at three distinct levels, which we separate explicitly:

1. **Mathematical (demonstrated):** Self-referential models exhibit metric coupling in their Fisher information—the geometry of self-dimensions is entangled with world-dimensions. We demonstrate this for two distribution families (Gaussian, Bernoulli).
1. **Geometric (theoretical):** This coupling produces non-trivial curvature, making parallel transport path-dependent. This follows from standard differential geometry given the demonstrated metric structure.
1. **Cognitive (hypothesis):** This geometric structure explains why self-modeling systems can verify their computations while non-self-modeling systems cannot. This is genuinely speculative.

The architectural experiment we propose tests the cognitive hypothesis without requiring the geometric mechanism to be correct.

**Keywords:** information geometry, self-reference, metacognition, Fisher information

-----

## 1. Introduction

### 1.1 The Phenomenon

Large language models exhibit a specific failure pattern: they correctly compute intermediate values but fail to verify conclusions against those values (Danan, 2025). We call this **hold-and-check failure**.

Preliminary data (N=700, Claude Sonnet) shows task-specific asymmetries: arithmetic shows verification deficits, logic shows generation deficits. The empirical foundation is thin—this requires replication across models and larger samples before strong conclusions.

### 1.2 The Three-Level Structure

This paper’s claims have very different epistemic status:

|Level              |Claim                                                                      |Status                         |What Would Falsify                              |
|-------------------|---------------------------------------------------------------------------|-------------------------------|------------------------------------------------|
|**1. Mathematical**|Self-reference creates metric coupling                                     |Demonstrated (2 examples)      |Finding self-referential models without coupling|
|**2. Geometric**   |Coupling produces curvature; curvature makes parallel transport non-trivial|Theoretical (follows from math)|Mathematical error in the derivation            |
|**3. Cognitive**   |This explains verification capacity                                        |Hypothesis                     |Architectural experiment showing no effect      |

**The key gap:** Level 1→2 is mathematics. Level 2→3 is a leap. The paper is honest that Level 3 is genuinely speculative.

### 1.3 Why Bother With the Geometry?

A simpler account: “LLMs lack working memory, so they can’t verify.”

This predicts the same failures. What does the geometric framework add?

**Claimed advantage:** It explains *why* self-modeling might produce working memory capacity—the geometry creates conditions where active maintenance is necessary.

**Honest assessment:** This is “naming the phenomenon geometrically” unless we can show the geometric structure causally produces the cognitive capacity. We cannot currently show this. The architectural experiment tests the prediction without resolving the mechanism.

-----

## 2. Level 1: The Mathematical Claim (Demonstrated)

### 2.1 Core Result

**Claim:** Self-referential statistical models have Fisher information with metric coupling between self-model and world-model parameters.

**Method:** We demonstrate this for two distribution families.

### 2.2 Example 1: Self-Referential Gaussian

**Non-self-referential:**

- Model: p(x | μ, σ²) = N(μ, σ²)
- Fisher metric: G = diag(1/σ², 1/(2σ⁴))

**Self-referential:**

- Model: p(x, s | μ, σ², τ) = N(x | μ, σ²) × N(s | σ², τ)
- Here s represents the system’s estimate of its own variance
- Fisher metric: G = diag(1/σ², **1/(2σ⁴) + 1/τ**, 1/(2τ²))

**The coupling:** g₂₂ = 1/(2σ⁴) + 1/τ depends on both world-model (σ²) and self-model (τ) parameters.

Full derivation in Appendix A.

### 2.3 Example 2: Self-Referential Bernoulli

To show this isn’t a Gaussian artifact:

**Non-self-referential:**

- Model: p(x | θ) = Bernoulli(θ)
- Fisher information: I_θθ = 1/(θ(1-θ))

**Self-referential:**

- Model: p(x, s | θ, τ) = Bernoulli(x | θ) × N(s | θ, τ)
- Here s represents the system’s noisy estimate of its own success probability
- Score for θ: ∂ℓ/∂θ = x/θ - (1-x)/(1-θ) + (s-θ)/τ

**Fisher information:**

$$I_{\theta\theta} = \frac{1}{\theta(1-\theta)} + \frac{1}{\tau}$$

**The coupling:** Same structure—the self-model contributes 1/τ to the world-model parameter’s Fisher information.

Full derivation in Appendix A.

### 2.4 The Structural Pattern

Both examples show the same structure:

|Component|Non-Self-Referential|Self-Referential    |
|---------|--------------------|--------------------|
|I_θθ     |I^world_θθ          |I^world_θθ + **1/τ**|
|Coupling |None                |θ coupled to τ      |

**Why this generalizes:** For any model p(x, s | θ, τ) = p(x | θ) × p(s | f(θ), τ):

$$\frac{\partial \log p}{\partial \theta} = \frac{\partial \log p(x|\theta)}{\partial \theta} + f’(\theta) \cdot \frac{\partial \log p(s|f(\theta), \tau)}{\partial f(\theta)}$$

Both terms contribute to Fisher information. The self-model term depends on τ, creating coupling.

**Limitation:** Two examples and a structural argument aren’t a proof. A general theorem would require specifying exactly which self-referential structures produce coupling.

-----

## 3. Level 2: The Geometric Claim (Theoretical)

### 3.1 From Coupling to Curvature

**Established (differential geometry):** When the metric tensor g_ij depends on multiple coordinates in a coupled way, the manifold is not a product space. Non-product structure generically produces non-zero Riemann curvature.

**Applied to our case:** The self-referential Fisher metric has g₂₂ depending on both σ² (or θ) and τ. The manifold is not M_world × M_self. The self-dimension is geometrically entangled with the world-dimension.

### 3.2 From Curvature to Parallel Transport

**Established (differential geometry):** On curved manifolds, parallel transport is path-dependent. Moving a vector from A to B along different paths yields different results.

**Applied to our case:** If the self-model dimensions have non-trivial curvature, then maintaining a vector (representing a held value) while moving through belief space requires tracking how that vector transforms along the path.

### 3.3 The Dynamical Picture

**Established framing:** Inference corresponds to movement on the statistical manifold—updating beliefs traces paths through the space of distributions.

**Combining:** If inference is movement, and the manifold is curved, then maintaining held values during inference is non-trivial parallel transport.

### 3.4 What Level 2 Establishes

Given the metric coupling (Level 1), standard differential geometry implies:

- The manifold has non-trivial curvature in self-dimensions
- Parallel transport in these dimensions is path-dependent
- Any “held value” must be actively tracked during belief updates

This is mathematics, not hypothesis. **But:** It says nothing about whether cognitive systems implement anything like parallel transport, or whether this geometric structure causally produces verification capacity.

-----

## 4. Level 3: The Cognitive Hypothesis (Speculative)

### 4.1 The Claimed Connection

**Hypothesis:** Self-referential systems develop the geometric structure (Level 2) that makes hold-and-check non-trivial. This creates selective pressure for active maintenance machinery. Systems with this machinery can verify; systems without it cannot.

### 4.2 Why This Is a Leap

Level 2 says: *if* you’re doing parallel transport on a curved manifold, it’s non-trivial.

Level 3 claims: cognitive systems *are* doing parallel transport, and the curvature *causes* them to develop the capacity.

**The gaps:**

1. Do biological/artificial systems actually implement parallel transport?
1. Does geometric necessity translate to architectural development?
1. Is there really selective pressure from curvature to develop maintenance machinery?

**Honest answer:** We don’t know. The paper gestures at “evolutionary pressure” but doesn’t spell out the mechanism.

### 4.3 The Alternative

A simpler account: “Verification requires working memory. Self-monitoring architectures have working memory. Therefore self-monitoring helps verification.”

This predicts the same outcome without invoking geometry. The geometric framework’s claimed advantage—explaining *why* self-modeling produces working memory—remains undemonstrated.

### 4.4 What Would Support Level 3

1. **Architectural experiment:** If explicit self-monitoring helps verification regardless of scale, that’s consistent with (but doesn’t prove) the hypothesis
1. **Quantitative predictions:** If curvature magnitude predicts verification accuracy, that would support the geometric mechanism
1. **Neural evidence:** If working memory involves something isomorphic to parallel transport, that would support the literal interpretation

Currently we have none of these. The architectural experiment is proposed but not run.

-----

## 5. The Architectural Experiment

### 5.1 Design

**System A (Control):** Standard transformer, large scale, no explicit self-monitoring

**System B (Experimental):** Matched parameters, includes self-monitoring module:

- Maintains “current computational state” representation
- Has dedicated parameters for this representation
- Updates based on own activations
- Feeds back into computation

### 5.2 What This Tests

|Outcome               |Interpretation                             |
|----------------------|-------------------------------------------|
|B >> A on verification|Consistent with Level 3 hypothesis         |
|B ≈ A                 |Self-monitoring doesn’t help; Level 3 wrong|
|A improves with scale |Scaling substitutes for architecture       |

### 5.3 What This Doesn’t Test

If B >> A, this supports “self-monitoring helps” without confirming the *geometric* mechanism. The result would also be predicted by:

- “Feedback loops help”
- “Explicit state helps”
- “Working memory helps”

The geometric interpretation would require additional evidence (curvature measurements, quantitative predictions).

### 5.4 Why Run It Anyway

The experiment tests the actionable prediction: does self-monitoring architecture help verification? This matters regardless of whether the geometric explanation is correct.

-----

## 6. On the Role of *e*

### 6.1 Where *e* Appears

Euler’s number appears in information geometry through:

- Fisher metric (log likelihood uses natural log)
- Maximum entropy distributions (exponential families)
- Geodesic dynamics (exponential approach to equilibrium)

### 6.2 What This Means

**Minimal claim:** *e* is intrinsic to information geometry. This is established (Čencov, 1982).

**Stronger claim:** The *e* in geodesic dynamics connects to learning time constants in self-referential systems.

**Honest assessment:** The stronger claim is “both frameworks involve calculus” territory. We have not derived quantitative relationships between geometric quantities and learning dynamics. The connection is suggestive, not demonstrated.

### 6.3 Testable Prediction

Self-referential learning should follow *e*-governed dynamics (exponential, not power-law):

- Time to 63.2% = τ
- Time to 86.5% = 2τ
- Time to 95.0% ≈ 3τ

This is testable but not yet tested. If confirmed, it would support (but not prove) the geometric interpretation.

-----

## 7. Limitations

### 7.1 Empirical Foundation

The hold-and-check failure pattern comes from one study (N=700, Claude Sonnet). This requires:

- Replication across models
- Larger samples
- Clearer methodology documentation
- Effect size robustness analysis

The theoretical framework is built on preliminary data.

### 7.2 Mathematical Generality

Two worked examples demonstrate the mechanism *can* exist. They don’t prove it *always* exists for self-referential structures. A general theorem is needed.

### 7.3 The Cognitive Leap

Level 3 is genuinely speculative. The paper is honest about this, but the honest assessment is: we have an interesting mathematical observation and a plausible-but-undemonstrated connection to cognition.

### 7.4 Simpler Explanations

The geometric framework may be adding complexity without explanatory power. Whether it “earns its keep” depends on whether it generates unique predictions. Currently it doesn’t—the predictions it makes are also made by simpler accounts.

-----

## 8. What This Paper Contributes

### 8.1 Definite Contributions

1. **Mathematical observation:** Self-referential models have metric coupling. Demonstrated for two distribution families.
1. **Geometric consequence:** This coupling implies non-trivial curvature. Follows from established mathematics.
1. **Experimental design:** A clean test of whether self-monitoring architecture helps verification.
1. **Epistemic clarity:** Explicit about what’s established vs. hypothesized.

### 8.2 Claimed But Undemonstrated

1. The coupling generalizes to all self-referential structures
1. Curvature explains verification capacity
1. Parallel transport is the mechanism
1. *e*-governed dynamics connect to geometric structure

### 8.3 The Honest Summary

We have found something mathematically interesting: self-reference changes metric structure in a specific way. Whether this explains why self-modeling systems can verify their computations is an open question. The architectural experiment would tell us something about the prediction. The geometric mechanism would require additional evidence.

-----

## 9. Conclusion

**Level 1 (Mathematical):** Self-referential models have Fisher information with metric coupling between self and world dimensions. *Demonstrated for Gaussian and Bernoulli; structural argument for generality.*

**Level 2 (Geometric):** This coupling produces curvature making parallel transport non-trivial. *Theoretical; follows from differential geometry.*

**Level 3 (Cognitive):** This explains why self-modeling enables verification. *Hypothesis; genuinely speculative; testable via architectural experiment.*

The mathematical observation is solid. The cognitive connection is a leap. The experiment would test the prediction without requiring the mechanism.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Springer.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS.

Baddeley, A. (2000). The episodic buffer. *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS.

Danan, H. (2025). Hold-and-check failures in large language models. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Phil. Trans. R. Soc. B*, 367(1594), 1338-1349.

-----

## Appendix A: Full Derivations

### A.1 Gaussian Example

**Non-self-referential:** p(x | μ, σ²) = N(μ, σ²)

Log-likelihood: ℓ = -½log(2πσ²) - (x-μ)²/(2σ²)

Scores:

- ∂ℓ/∂μ = (x-μ)/σ²
- ∂ℓ/∂σ² = -1/(2σ²) + (x-μ)²/(2σ⁴)

Fisher information:

- I_μμ = 1/σ²
- I_σ²σ² = 1/(2σ⁴)

**Self-referential:** p(x, s | μ, σ², τ) = N(x | μ, σ²) × N(s | σ², τ)

Additional log-likelihood term: -½log(2πτ) - (s-σ²)²/(2τ)

Modified score for σ²:
∂ℓ/∂σ² = -1/(2σ²) + (x-μ)²/(2σ⁴) + **(s-σ²)/τ**

Fisher information:

- I_σ²σ² = 1/(2σ⁴) + **1/τ**

The **1/τ** term is the self-model contribution, creating coupling.

### A.2 Bernoulli Example

**Non-self-referential:** p(x | θ) = θ^x (1-θ)^(1-x)

Log-likelihood: ℓ = x log θ + (1-x) log(1-θ)

Score: ∂ℓ/∂θ = x/θ - (1-x)/(1-θ)

Fisher information: I_θθ = 1/(θ(1-θ))

**Self-referential:** p(x, s | θ, τ) = Bernoulli(x | θ) × N(s | θ, τ)

The system maintains a noisy estimate s of its success probability θ.

Additional log-likelihood: -½log(2πτ) - (s-θ)²/(2τ)

Modified score:
∂ℓ/∂θ = x/θ - (1-x)/(1-θ) + **(s-θ)/τ**

Fisher information:

- I_θθ = 1/(θ(1-θ)) + **1/τ**

Same coupling structure as Gaussian case.

### A.3 Curvature Implications

For both examples, the Fisher information for the world-model parameter gains a term 1/τ that depends on the self-model precision.

This means:

- The metric is not block-diagonal
- The manifold is not a product space
- Christoffel symbols mix world and self coordinates
- Riemann curvature is non-trivial in directions involving both

Full curvature calculation (Christoffel symbols → Riemann tensor) is tedious but mechanical. The key point: non-trivial coupling → non-trivial curvature.

-----

## Appendix B: The *e* Question

### B.1 Established

*e* appears in:

- Fisher metric (natural log)
- Exponential families (p ∝ e^{θ·T(x)})
- Geodesic dynamics (exponential time evolution)

### B.2 Unestablished

Whether the *e* in geodesic dynamics quantitatively connects to learning dynamics in self-referential systems.

**What would establish this:**

- Derive time constants τ from geometric quantities
- Show τ = f(curvature, Fisher info)
- Verify empirically

**Current status:** Not done. The *e* connection is noted, not demonstrated.

-----

## Appendix C: Oscillatory Dynamics (Brief)

When self-referential systems have feedback delays, oscillations can emerge:

$$S(t) = Ae^{-\gamma t}\cos(\omega t + \phi)$$

*e* governs damping; *π* governs frequency.

This is interesting but tangential to the main argument. See Appendix C of Danan (2025b) for development.

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper*.

-----

*“The mathematics is demonstrated. The connection to cognition is hypothesized. The experiment would test the prediction.”*

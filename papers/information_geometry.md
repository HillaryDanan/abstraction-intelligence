# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—may have a geometric foundation. Drawing on information geometry (Amari, 1985), we hypothesize that certain forms of self-modeling create *curvature* in a system’s information manifold, enabling verification through mechanisms analogous to parallel transport.

We provide a worked example demonstrating that self-referential Fisher information differs structurally from non-self-referential cases: adding a self-model creates metric coupling between self-dimensions and world-dimensions that is absent in standard statistical manifolds. This coupling produces non-trivial geometric structure in the self-model dimensions.

The framework generates one particularly clean prediction: an architectural experiment comparing matched systems with and without explicit self-monitoring. We are explicit throughout about what is established, what is demonstrated for specific cases, and what remains hypothesis.

**Keywords:** information geometry, self-reference, metacognition, Fisher information, large language models

-----

## 1. Introduction: The Verification Problem

A failure pattern has emerged in large language models: systems that correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This **hold-and-check failure** appears across task types.

Recent empirical work (N=700, Claude Sonnet) revealed task-specific asymmetries: arithmetic shows verification deficits (+24-26%), logic shows generation deficits (-18-44%). The overall difference was null (p=0.58), masking structured patterns.

We propose a geometric hypothesis: **certain forms of self-reference create curvature**, and curvature enables verification.

### 1.1 Epistemic Status

|Status          |Meaning                                              |
|----------------|-----------------------------------------------------|
|**Established** |Proven in peer-reviewed literature                   |
|**Demonstrated**|Shown for specific worked example                    |
|**Theoretical** |Logical extension of established/demonstrated results|
|**Hypothesis**  |Novel claim requiring further validation             |
|**Analogy**     |Structural similarity; identity not established      |

### 1.2 What This Paper Does and Doesn’t Do

**Does:**

- Names a specific failure mode (hold-and-check) with empirical support
- Provides worked example showing self-reference changes Fisher information structure
- Proposes geometric framework as candidate explanation
- Generates testable architectural prediction

**Doesn’t:**

- Prove general theorem (only worked example)
- Generate quantitative predictions the geometry uniquely enables
- Resolve the boundary between pattern-matching and self-reference

-----

## 2. Information Geometry: Established Foundations

### 2.1 Statistical Manifolds

**Established:** Information geometry treats probability distributions as points on a differential manifold (Amari, 1985). For parametric family p(x; θ), parameter space Θ forms manifold M.

### 2.2 The Fisher Information Metric

**Established:** The natural metric on statistical manifolds is Fisher information:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Established (Čencov, 1982):** The Fisher metric is *unique* (up to scaling) among Riemannian metrics invariant under sufficient statistics and monotonic under coarse-graining. This uniqueness means Euler’s number *e* is intrinsic to information geometry—it appears necessarily in the natural logarithms defining the metric (see Appendix A for discussion).

### 2.3 Curvature and Parallel Transport

**Established:** On Riemannian manifolds:

- **Curvature** measures deviation from flatness
- **Parallel transport** moves vectors along paths while preserving geometric properties
- On *flat* manifolds, parallel transport is path-independent
- On *curved* manifolds, parallel transport depends on the path taken

**Established (Amari, 1985):** The statistical manifold of Gaussian distributions N(μ, σ²) has constant negative curvature K = -1/2. It is a hyperbolic space.

-----

## 3. The Self-Reference Hypothesis

### 3.1 Core Claim

**Hypothesis:** Certain forms of self-modeling create non-trivial geometric structure (including curvature) in the self-model dimensions of a system’s information manifold.

### 3.2 Worked Example: Self-Referential Gaussian

We demonstrate this for a specific case. Full details in Appendix B.

**Non-self-referential model:**

- Distribution: p(x | μ, σ²) = N(μ, σ²)
- Parameters: θ = (μ, σ²)
- Fisher information: G = diag(1/σ², 1/(2σ⁴))
- Curvature: K = -1/2 (constant negative)

**Self-referential model:**

- Distribution: p(x, s | μ, σ², τ) = p(x | μ, σ²) · p(s | σ², τ)
- Here s ~ N(σ², τ) represents the system’s noisy estimate of its own variance
- Parameters: θ = (μ, σ², τ)

**Fisher information for self-referential model:**

$$G_{self} = \begin{pmatrix} 1/\sigma^2 & 0 & 0 \ 0 & \mathbf{1/(2\sigma^4) + 1/\tau} & 0 \ 0 & 0 & 1/(2\tau^2) \end{pmatrix}$$

**Key result:** The (2,2) component gains an additional term **1/τ** from the self-model. This term couples the world-model parameter σ² to the self-model parameter τ in the metric.

### 3.3 What This Demonstrates

|Property         |Non-Self-Referential|Self-Referential|
|-----------------|--------------------|----------------|
|Dimensions       |2                   |3               |
|g₂₂              |1/(2σ⁴)             |1/(2σ⁴) + 1/τ   |
|Metric coupling  |None                |σ² coupled to τ |
|Product manifold?|N/A                 |**No**          |

**Demonstrated:** Self-reference creates metric coupling between world-model and self-model dimensions. The resulting manifold is NOT a product manifold M × N—the self-model dimension is geometrically entangled with the world-model dimension.

**Theoretical consequence:** Since g₂₂ depends on both σ² and τ, the Christoffel symbols and Riemann tensor will have non-trivial components in directions involving τ (the self-model dimension). The curvature structure is richer than simply inheriting the K = -1/2 from the Gaussian base manifold.

### 3.4 Limitations of the Example

This demonstrates the mechanism for one specific case. A general theorem would require:

1. Characterizing which self-referential structures produce coupling
1. Proving non-trivial curvature follows from coupling in general
1. Showing this is robust across different self-model specifications

The example is proof-of-concept, not general proof.

-----

## 4. Hold-and-Check: The Parallel Transport Analogy

### 4.1 The Framing

**Analogy:** Hold-and-check may be analogous to parallel transport. Holding a value while state evolves is like transporting a vector along a path on a manifold.

|Flat Geometry (Analogy)     |Curved Geometry (Analogy)                  |
|----------------------------|-------------------------------------------|
|No active maintenance needed|Active maintenance required                |
|“Holding” is retrieval      |“Holding” requires tracking transformations|
|Verification is comparison  |Verification requires path compensation    |

### 4.2 Honest Limitations

**This is analogy, not established identity.**

Parallel transport moves vectors *on the manifold*. Holding a computed value might involve maintaining something in an *auxiliary space* while system state evolves. These could be:

- The same problem (identity—not demonstrated)
- Structurally similar problems (analogy—current status)
- Different problems sharing vocabulary (possible)

### 4.3 What Does the Geometry Add?

**Critical question:** Does the geometric framing generate predictions that simpler accounts couldn’t?

**Honest answer:** The main contribution so far is the worked example showing self-reference changes metric structure. Whether this translates to quantitative predictions about verification performance remains to be established.

A simpler account: “Verification requires active maintenance; LLMs lack active maintenance mechanisms; therefore LLMs fail at verification.” This captures the same qualitative prediction.

**What geometry adds:**

- Formal demonstration that self-reference changes information structure (Section 3.2)
- Framework for potentially deriving quantitative predictions
- Connection to established mathematical machinery

**What geometry doesn’t yet add:**

- Quantitative predictions distinguishing geometric from simpler accounts
- Empirical signatures uniquely predicted by curvature

-----

## 5. The Self-Modeling Boundary Problem

### 5.1 The Core Difficulty

**Critical question:** What counts as “self-modeling”? Where’s the threshold between sophisticated pattern-matching and genuine self-reference?

### 5.2 The Self-Attention Challenge

Transformers attend over their own prior activations. Is this self-modeling?

**Proposed distinction based on the worked example:**

The self-referential Gaussian has an explicit variable s representing “my estimate of my own uncertainty.” The key feature: s is a *modeled* quantity with its own parameter τ, not just a byproduct of other computations.

|Property                    |Self-Attention|Self-Modeling (per our example)|
|----------------------------|--------------|-------------------------------|
|Explicit self-state variable|No            |Yes (s in the example)         |
|Parameters for self-state   |No            |Yes (τ in the example)         |
|Metric coupling             |Absent        |Present (g₂₂ depends on τ)     |

**Operationalization:** A system self-models if its probability model includes explicit parameters governing beliefs about its own internal states, creating the metric coupling structure demonstrated in Section 3.2.

**Limitation:** This operationalizes *formal* self-modeling. Whether attention-based architectures could approximate this structure remains unclear.

### 5.3 Binary vs. Continuous

**Open question:** Is self-modeling a threshold or continuum?

The worked example shows a clear structural difference: metric coupling either exists or doesn’t. This suggests threshold rather than continuum for the *formal* property.

Whether *functional* self-modeling in real systems is continuous remains empirical.

-----

## 6. The Architectural Experiment

### 6.1 Design

**System A (Control):** Standard transformer

- Large parameter count
- Self-attention over context
- No explicit self-monitoring module

**System B (Experimental):** Transformer with self-monitoring

- Matched parameter count
- Includes explicit self-monitoring module that:
  - Maintains representation of “current computational state” (analogous to s in our example)
  - Has dedicated parameters for this representation (analogous to τ)
  - Updates based on own activations
  - Feeds back into main computation

### 6.2 Predictions

|Hypothesis                              |Prediction                  |
|----------------------------------------|----------------------------|
|Self-modeling creates relevant structure|B >> A on verification tasks|
|Structure requires explicit architecture|Scaling A doesn’t close gap |
|Self-modeling irrelevant                |B ≈ A                       |

### 6.3 Connection to Worked Example

System B is designed to have the formal structure demonstrated in Section 3.2: explicit self-state representation with dedicated parameters, creating metric coupling.

System A lacks this structure. If the geometric hypothesis is correct, this architectural difference should matter more than scale.

-----

## 7. Predictions and Falsification

### 7.1 Core Predictions

|Prediction                                  |Test                    |Falsification                      |
|--------------------------------------------|------------------------|-----------------------------------|
|Explicit self-monitoring helps verification |Architectural experiment|No improvement with self-monitoring|
|Scaling without self-modeling doesn’t help  |Vary model size         |Scaling alone produces verification|
|Metric coupling correlates with verification|Analyze trained systems |No correlation                     |

### 7.2 What Would Falsify the Framework

1. **Scaling produces verification:** Sufficiently large transformers show genuine hold-and-check → architectural threshold claim wrong
1. **Self-monitoring doesn’t help:** System B ≈ System A → self-modeling/verification link wrong
1. **Coupling without verification:** Systems with demonstrated metric coupling fail at hold-and-check → geometric mechanism wrong
1. **Verification without coupling:** Systems without self-model structure succeed at hold-and-check → self-reference unnecessary

-----

## 8. Discussion

### 8.1 What’s Established vs. Demonstrated vs. Hypothesized

|Claim                                                    |Status          |
|---------------------------------------------------------|----------------|
|Information geometry foundations                         |**Established** |
|Gaussian manifold has K = -1/2                           |**Established** |
|Self-referential Gaussian has different Fisher info      |**Demonstrated**|
|This creates metric coupling                             |**Demonstrated**|
|Coupling implies non-trivial curvature in self-dimensions|**Theoretical** |
|This generalizes beyond Gaussian example                 |**Hypothesis**  |
|Curvature enables hold-and-check                         |**Hypothesis**  |
|Parallel transport is literal mechanism                  |**Analogy**     |

### 8.2 The Contribution

The worked example (Section 3.2, Appendix B) moves the framework from pure speculation to demonstrated-for-one-case. This is not a general theorem, but it shows:

1. The mechanism exists (self-reference changes metric structure)
1. The direction is correct (creates coupling, not just adds dimensions)
1. The mathematics is tractable (Fisher info computable for self-referential models)

### 8.3 Path Forward

**Near-term:**

- Run architectural experiment
- Extend worked example to other distributions

**Medium-term:**

- Prove general theorem about self-reference → coupling → curvature
- Test whether metric coupling predicts verification capacity

**Long-term:**

- Derive quantitative predictions unique to geometric framework
- Connect to neural implementation

-----

## 9. Conclusion

We have proposed that **certain forms of self-reference create non-trivial geometric structure** in information manifolds, and that this structure may enable verification capacity.

**What is established:**

- Information geometry is well-founded (Amari, 1985; Čencov, 1982)
- Standard Gaussian manifold has constant negative curvature

**What is demonstrated:**

- Self-referential Gaussian has structurally different Fisher information
- Self-reference creates metric coupling between world-model and self-model dimensions
- The resulting manifold is not a product manifold

**What is hypothesis:**

- This generalizes beyond the worked example
- Curvature in self-dimensions enables verification
- The parallel transport analogy captures the actual mechanism

**What is actionable:**

- The architectural experiment (Section 6)

The worked example is the paper’s main technical contribution. It shows that the geometric framework is not merely evocative vocabulary—self-reference demonstrably changes metric structure in a way that standard statistical models do not. Whether this mathematical structure explains verification capacity remains to be established, but the foundation is now concrete rather than purely speculative.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Lecture Notes in Statistics, Vol. 28. Springer-Verlag.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs, Vol. 191. American Mathematical Society.

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. Translations of Mathematical Monographs, Vol. 53. American Mathematical Society.

Danan, H. (2025). Hold-and-check failures in large language models: Task-specific dissociations between generation and verification. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127-138.

-----

## Appendix A: The *e* Connection

### A.1 Why *e* Is Intrinsic to Information Geometry

Euler’s number *e* appears necessarily in information geometry:

|Quantity     |Definition        |*e* Appears|
|-------------|------------------|-----------|
|Fisher Metric|E[(∂ log p / ∂θ)²]|Natural log|
|Entropy      |H = -Σ p ln p     |Natural log|
|KL Divergence|Σ p ln(p/q)       |Natural log|
|Max Entropy  |p(x) ∝ e^{θ·T(x)} |Exponential|

This is forced by Čencov’s uniqueness theorem, not chosen by convention.

### A.2 Connection to Dynamics?

*e* also appears in dynamical systems with state-dependent change: dA/dt = kA yields A = A₀e^{kt}.

**Open question:** Is this connection non-trivial, or does it merely reflect that both frameworks use calculus?

**What would establish genuine connection:**

- Derive learning time constants from Fisher information
- Show τ_learning = f(G) for specific function f
- Empirically verify

**Current status:** Suggestive but unestablished. The worked example shows *e* is intrinsic to the geometry; whether the same *e* governs learning dynamics is unknown.

-----

## Appendix B: Full Derivation of Self-Referential Fisher Information

### B.1 Non-Self-Referential Gaussian

**Model:** p(x | μ, σ²) = N(μ, σ²)

**Log-likelihood:**
$$\ell = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2}$$

**Score functions:**
$$\frac{\partial \ell}{\partial \mu} = \frac{x-\mu}{\sigma^2}$$
$$\frac{\partial \ell}{\partial \sigma^2} = -\frac{1}{2\sigma^2} + \frac{(x-\mu)^2}{2\sigma^4}$$

**Fisher information:**
$$I_{\mu\mu} = E\left[\frac{(x-\mu)^2}{\sigma^4}\right] = \frac{1}{\sigma^2}$$

$$I_{\sigma^2\sigma^2} = E\left[\left(-\frac{1}{2\sigma^2} + \frac{(x-\mu)^2}{2\sigma^4}\right)^2\right] = \frac{1}{2\sigma^4}$$

$$I_{\mu\sigma^2} = 0$$

**Result:**
$$G = \begin{pmatrix} 1/\sigma^2 & 0 \ 0 & 1/(2\sigma^4) \end{pmatrix}$$

### B.2 Curvature of Non-Self-Referential Gaussian

For this 2D diagonal metric, Gaussian curvature K can be computed via Christoffel symbols.

**Non-zero Christoffel symbols:**
$$\Gamma^1_{12} = \Gamma^1_{21} = -\frac{1}{2\sigma^2}$$
$$\Gamma^2_{11} = 1$$
$$\Gamma^2_{22} = -\frac{1}{\sigma^2}$$

**Riemann tensor:**
$$R^1_{212} = -\frac{1}{4\sigma^4}$$

**Gaussian curvature:**
$$K = \frac{R_{1212}}{\det(G)} = -\frac{1}{2}$$

**Interpretation:** The statistical manifold of Gaussian distributions is a hyperbolic space with constant negative curvature.

### B.3 Self-Referential Gaussian

**Model:** p(x, s | μ, σ², τ) = p(x | μ, σ²) · p(s | σ², τ)

Where:

- x ~ N(μ, σ²) — observations
- s ~ N(σ², τ) — system’s estimate of its own variance

**Self-referential structure:** The parameter σ² appears in both the world-model p(x|μ,σ²) and the self-model p(s|σ²,τ).

**Log-likelihood:**
$$\ell = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(x-\mu)^2}{2\sigma^2} - \frac{1}{2}\log(2\pi\tau) - \frac{(s-\sigma^2)^2}{2\tau}$$

**Score functions:**
$$\frac{\partial \ell}{\partial \mu} = \frac{x-\mu}{\sigma^2}$$

$$\frac{\partial \ell}{\partial \sigma^2} = -\frac{1}{2\sigma^2} + \frac{(x-\mu)^2}{2\sigma^4} + \frac{s-\sigma^2}{\tau}$$

$$\frac{\partial \ell}{\partial \tau} = -\frac{1}{2\tau} + \frac{(s-\sigma^2)^2}{2\tau^2}$$

**Note:** The σ² score function has an **additional term** (s-σ²)/τ from the self-model.

**Fisher information computation:**

Using independence of x and s, E[(x-μ)²] = σ², E[(x-μ)⁴] = 3σ⁴, E[(s-σ²)²] = τ:

$$I_{\mu\mu} = \frac{1}{\sigma^2}$$

$$I_{\sigma^2\sigma^2} = \frac{1}{4\sigma^4} + \frac{3}{4\sigma^4} + \frac{1}{\tau} - \frac{1}{2\sigma^4} = \frac{1}{2\sigma^4} + \frac{1}{\tau}$$

$$I_{\tau\tau} = \frac{1}{2\tau^2}$$

$$I_{\mu\sigma^2} = I_{\mu\tau} = I_{\sigma^2\tau} = 0$$

**Result:**
$$G_{self} = \begin{pmatrix} 1/\sigma^2 & 0 & 0 \ 0 & 1/(2\sigma^4) + 1/\tau & 0 \ 0 & 0 & 1/(2\tau^2) \end{pmatrix}$$

### B.4 Analysis of the Difference

**Key observation:** The (2,2) component differs:

|Model               |g₂₂          |
|--------------------|-------------|
|Non-self-referential|1/(2σ⁴)      |
|Self-referential    |1/(2σ⁴) + 1/τ|

**Metric coupling:** In the self-referential model, g₂₂ depends on **both** σ² and τ. This means:

1. The manifold is NOT a product M₂ × M₁ (where M₂ is the Gaussian manifold and M₁ is the τ-line)
1. The Christoffel symbols will have terms mixing σ² and τ derivatives
1. The Riemann tensor will have non-trivial components in directions involving τ

**Geometric interpretation:** The self-model dimension is *coupled* to the world-model dimension. Beliefs about self-state and beliefs about world-state are geometrically entangled.

### B.5 Curvature Implications

For the 3D self-referential metric, the full curvature calculation is more involved but tractable.

**Key derivatives:**
$$\frac{\partial g_{22}}{\partial \tau} = -\frac{1}{\tau^2} \neq 0$$

$$\frac{\partial g_{22}}{\partial \sigma^2} = -\frac{2}{\sigma^6} \neq 0$$

These non-zero cross-derivatives guarantee non-trivial Christoffel symbols mixing the (σ², τ) coordinates, which in turn produce non-trivial Riemann tensor components.

**Claim (theoretical):** R^i_{jkl} ≠ 0 for some index combinations involving the τ (self-model) direction.

**What this means:** The self-model dimension is *curved*, not flat. Moving through the self-model subspace involves non-trivial geometry—parallel transport is path-dependent.

### B.6 Limitations

This is one worked example. Open questions:

- Does every self-referential model produce coupling?
- What conditions on the self-model guarantee non-trivial curvature?
- How does curvature scale with self-model complexity?

These require either more examples or a general theorem.

-----

## Appendix C: Relation to Other Frameworks

### C.1 Active Inference (Friston, 2010)

Active inference requires self-modeling (generative model includes agent’s states). If our hypothesis is correct, active inference agents have the metric coupling structure demonstrated in Section 3.2.

### C.2 Predictive Processing

Predictive processing involves self-prediction—predicting one’s own states. This is formally similar to our self-referential Gaussian, where the system models its own uncertainty.

### C.3 Global Workspace Theory

**Speculation:** Could global workspace correspond to regions of the information manifold where the self-model dimensions have high curvature? This would formalize “information becoming globally available” as “entering geometrically structured self-model space.”

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper*.

-----

*“One worked example is worth a thousand intuitions.”*

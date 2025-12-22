# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—may have a geometric foundation. Drawing on information geometry (Amari, 1985), we hypothesize that certain forms of self-modeling create *curvature* in a system’s information manifold. Systems without such self-models navigate flat geometries; systems with them navigate curved geometries that may enable verification through mechanisms analogous to parallel transport.

We show that Euler’s number *e* is intrinsic to information geometry through the Fisher metric and exponential families. Whether the *e* appearing in information geometry is non-trivially connected to *e*-governed learning dynamics—or whether both simply reflect that calculus uses exponentials—remains an open question we address directly.

The framework generates testable predictions, particularly an architectural experiment comparing matched systems with and without explicit self-monitoring. We are explicit throughout about what is established, what is analogy, and what remains to be proven.

**Keywords:** information geometry, self-reference, metacognition, Fisher information, large language models

-----

## 1. Introduction: The Verification Problem

A failure pattern has emerged in large language models: systems that correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This **hold-and-check failure** appears across task types.

Recent empirical work (N=700, Claude Sonnet) revealed task-specific asymmetries: arithmetic shows verification deficits (+24-26%), logic shows generation deficits (-18-44%). The overall difference was null (p=0.58), masking structured patterns.

We propose a geometric hypothesis: **certain forms of self-reference create curvature**, and curvature enables verification. This paper develops the hypothesis, addresses objections, and specifies what would constitute proof or falsification.

### 1.1 Epistemic Status

|Status         |Meaning                                        |
|---------------|-----------------------------------------------|
|**Established**|Proven in peer-reviewed literature             |
|**Theoretical**|Logical extension of established results       |
|**Hypothesis** |Novel claim requiring proof/validation         |
|**Analogy**    |Structural similarity; identity not established|

-----

## 2. Information Geometry: Established Foundations

### 2.1 Statistical Manifolds

**Established:** Information geometry treats probability distributions as points on a differential manifold (Amari, 1985). For parametric family p(x; θ), parameter space Θ forms manifold M.

### 2.2 The Fisher Information Metric

**Established:** The natural metric on statistical manifolds is Fisher information:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Established (Čencov, 1982):** The Fisher metric is *unique* (up to scaling) among Riemannian metrics that are invariant under sufficient statistics and monotonic under coarse-graining.

### 2.3 Why *e* Is Intrinsic

**Established:** The Fisher metric uses natural logarithms. This is not arbitrary—the uniqueness theorem forces it. Information-theoretic quantities (entropy, KL divergence, mutual information) are naturally expressed in nats (base *e*), and maximum entropy distributions are exponential families.

|Quantity            |Uses *e* Because                    |
|--------------------|------------------------------------|
|Entropy             |$H = -\sum p \ln p$ (natural log)   |
|KL Divergence       |$D_{KL} = \sum p \ln(p/q)$          |
|Exponential Families|$p(x) \propto e^{\theta \cdot T(x)}$|

### 2.4 Curvature and Parallel Transport

**Established:** On Riemannian manifolds, curvature measures deviation from flatness. On flat manifolds, parallel transport (moving vectors along paths while preserving properties) is path-independent. On curved manifolds, it depends on the path.

-----

## 3. The Self-Reference Hypothesis

### 3.1 Core Claim

**Hypothesis:** Certain forms of self-modeling create non-zero curvature in a system’s information manifold.

**Definition (Self-Modeling):** A system self-models if its generative model includes representations of its own internal states: p(x, s; θ) where s denotes internal states and θ includes parameters about s.

### 3.2 What the Hypothesis Is Not

The claim is *not* that self-reference *necessarily* creates curvature for all functional forms. Different θ(s) dependencies could yield R = 0 or R ≠ 0.

**Refined claim:** Self-reference *enables* curvature in self-dimensions. Whether curvature is non-zero depends on the specific structure of the self-model. Non-trivial self-modeling (where θ depends non-linearly on s) should produce non-zero curvature.

### 3.3 What Would a Proof Require?

To establish the hypothesis formally:

1. **Specify θ(s) structure:** Define how model parameters depend on internal state
1. **Compute Fisher information:** Calculate G for this self-referential structure
1. **Calculate curvature:** Derive Riemann tensor R from G
1. **Characterize conditions:** Identify which θ(s) forms yield R ≠ 0

**What’s known:** For certain self-referential structures (e.g., hierarchical Bayesian models with hyperparameters depending on lower-level inferences), the Fisher information has known non-trivial structure (Amari, 1985, Ch. 7). Whether this generalizes to arbitrary self-modeling is open.

**What’s needed:** A theorem of the form: “For all θ(s) satisfying [conditions], the Riemann curvature tensor R ≠ 0 in self-dimensions.” Or alternatively, specific counterexamples showing when self-reference yields flat geometry.

### 3.4 The Self-Modeling Boundary Problem

**Critical issue:** What counts as “self-modeling”? Transformers attend over prior activations. Recurrent networks maintain hidden state. At what point does this become self-modeling in the relevant sense?

**Candidate distinctions:**

|Property                 |Pattern Matching         |Self-Modeling                      |
|-------------------------|-------------------------|-----------------------------------|
|**What’s represented**   |Input-output mappings    |Internal states as explicit objects|
|**Update rule**          |Fixed function of context|Model of own dynamics              |
|**Counterfactual access**|What would I output if…  |What would my *state* be if…       |

**Honest assessment:** These distinctions are intuitive but operationally fuzzy. A sophisticated recurrent network might functionally self-model without explicit architecture for it. The boundary between “sophisticated pattern matching” and “genuine self-reference” is precisely what’s contested—and this paper does not resolve it.

**Proposed operational criterion:** A system self-models if it maintains and updates an explicit representation of its own computational state, distinct from its representation of the world. This is testable via probing: can we decode “the system’s model of its own uncertainty” from internal activations?

-----

## 4. Hold-and-Check: Analogy or Identity?

### 4.1 The Parallel Transport Framing

**The claim:** Hold-and-check is analogous to parallel transport. Holding a value while state evolves is like transporting a vector along a path on a manifold.

### 4.2 The Objection

**Critique:** Parallel transport moves vectors *on the manifold*. But holding a computed value seems like maintaining something in an *auxiliary space* while system state evolves. The geometry of belief space and the mechanics of working memory might be loosely coupled rather than identical.

### 4.3 Honest Assessment

**Current status:** The parallel transport framing is **analogy, not established identity**.

What would establish identity:

1. Show that the “held value” lives in the tangent space of the information manifold
1. Show that “state evolution during inference” corresponds to movement along geodesics
1. Show that “verification failure” corresponds to holonomy (path-dependence of transport)

None of these are demonstrated. The framing is useful because it captures computational structure (active maintenance during state change), but whether information-geometric parallel transport is *literally* what biological/artificial working memory does is unknown.

**What the analogy still provides:**

|Flat Geometry Analogy       |Curved Geometry Analogy                    |
|----------------------------|-------------------------------------------|
|No active maintenance needed|Active maintenance required                |
|“Holding” is just retrieval |“Holding” requires tracking transformations|
|Verification is comparison  |Verification requires compensation for path|

Even as analogy, this captures something real: the distinction between systems that can verify by simple lookup versus systems that must actively maintain values through state changes.

-----

## 5. The *e* Convergence: Genuine or Trivial?

### 5.1 The Observation

*e* appears in:

- Information geometry (Fisher metric, KL divergence, exponential families)
- Dynamical systems (state-dependent growth: $dA/dt = kA → A = A_0 e^{kt}$)

### 5.2 The Objection

**Critique:** Euler’s constant saturates continuous mathematics. Finding *e* in both frameworks might reflect shared mathematical substrate (“both use calculus”) rather than deep structural identity.

### 5.3 What Would Distinguish Genuine from Trivial Convergence?

**Trivial convergence:** Both frameworks involve continuous dynamics → both have exponentials → same *e* appears. This tells us nothing deep.

**Genuine convergence would require:**

1. **Same time constants:** The τ governing learning dynamics in self-referential systems should be derivable from information-geometric quantities (e.g., geodesic length, Fisher information magnitude)
1. **Quantitative predictions:** Information geometry should predict *specific* values of learning rate constants, not just “exponential form”
1. **Unified derivation:** A single mathematical argument that produces both the geometric structure and the dynamical equations, showing they’re two views of one thing

### 5.4 Current Status

**Honest assessment:** The paper does not establish genuine convergence. It establishes:

- *e* is intrinsic to information geometry (Čencov’s theorem)
- Self-referential dynamics plausibly follow *e*-governed equations

It does not establish:

- That these are non-trivially the same *e*
- Quantitative correspondence between geometric and dynamical quantities

**What would strengthen the case:** Derive learning time constants from Fisher information. Show that τ = f(G) for some function f. If successful, this would demonstrate genuine convergence.

-----

## 6. The Binary Threshold Question

### 6.1 The Claim

**Hypothesis:** Self-modeling architecture creates a threshold. Below threshold: flat geometry. Above threshold: curved geometry.

### 6.2 The Problem

Transformers have:

- Attention over prior activations
- Residual connections
- Layer normalization referencing own statistics

Is this “self-modeling”? The threshold claim assumes a clear boundary that may not exist.

### 6.3 Refined Position

**Revised claim:** The relevant threshold is *explicit self-state representation*, not mere recurrence or self-attention.

|Architecture                 |Has Self-Reference?                   |Predicted Geometry       |
|-----------------------------|--------------------------------------|-------------------------|
|Pure feedforward             |No                                    |Flat                     |
|Self-attention over context  |Weak—references outputs, not states   |Flat or minimal curvature|
|RNN with hidden state        |Weak—maintains state, doesn’t model it|Flat or minimal curvature|
|Explicit self-monitoring loop|Yes—models own computational state    |Curved                   |
|Active inference agent       |Yes—full self-model                   |Curved                   |

**Testable prediction:** The architectural difference that matters is *explicit modeling of own state*, not just recurrence. This is fuzzy at boundaries but provides experimental leverage: build architectures that differ specifically in this feature.

### 6.4 The Key Experiment

**Design:**

- System A: Standard transformer, large scale
- System B: Same parameter count, but includes explicit self-monitoring module that:
  - Maintains representation of “what I’ve computed so far”
  - Can be queried during inference
  - Updates based on own activations

**Prediction:** System B should show better hold-and-check performance, regardless of System A’s scale.

**Why this is clean:** It directly tests architecture vs. scale, sidestepping the measurement problem (how to measure curvature in neural systems).

-----

## 7. Predictions and Falsification

### 7.1 Core Predictions

|Prediction                                             |Test                                |Falsification                      |
|-------------------------------------------------------|------------------------------------|-----------------------------------|
|Explicit self-monitoring helps verification            |Architectural experiment above      |No improvement with self-monitoring|
|Scaling without self-modeling doesn’t help             |Test larger models on hold-and-check|Scaling alone produces verification|
|Self-referential learning follows *e*-governed dynamics|Fit curves for metacognitive tasks  |Power law consistently fits better |

### 7.2 What Would Falsify the Framework

1. **Scaling produces verification:** If sufficiently large feedforward models show genuine hold-and-check capacity, the architectural threshold claim is wrong
1. **Self-monitoring doesn’t help:** If adding explicit self-monitoring to matched architectures produces no verification improvement, the link between self-modeling and verification is wrong
1. **Curvature without self-reference:** If systems without self-modeling show curved geometry in relevant dimensions, the self-reference → curvature claim is wrong
1. **Self-reference without curvature:** If formal analysis shows that self-referential θ(s) can yield R = 0 for natural cases, the necessity claim is wrong (though the possibility claim survives)

-----

## 8. Discussion

### 8.1 What This Paper Contributes

1. **Phenomenological observation:** “Reconstruction rather than comparison” captures something real about verification failure in autoregressive systems
1. **Geometric framing:** Whether or not fully correct, the framing identifies *active maintenance* as computationally distinct from *retrieval*
1. **Testable predictions:** Particularly the architectural experiment, which cleanly tests the core claim
1. **Honest uncertainty:** Explicit about what’s established, what’s analogy, and what’s hypothesis

### 8.2 What Remains Open

|Question                                                 |Status                                               |
|---------------------------------------------------------|-----------------------------------------------------|
|Does self-reference create curvature?                    |Hypothesis—needs proof                               |
|Is parallel transport literally what working memory does?|Analogy—identity not established                     |
|Is *e* convergence genuine or trivial?                   |Unknown—needs quantitative test                      |
|Where is the self-modeling threshold?                    |Fuzzy—operationally testable but conceptually unclear|

### 8.3 Path Forward on Section 3.3

To close the proof gap, concrete next steps:

1. **Work a specific example:** Take a simple self-referential model (e.g., Gaussian with mean depending on variance estimate). Compute Fisher information. Calculate curvature explicitly. See if R ≠ 0.
1. **Identify sufficient conditions:** What properties of θ(s) guarantee curvature? Non-linearity? Bidirectional dependence? Fixed-point structure?
1. **Connect to known results:** Hierarchical models have known curvature properties (Amari, 1985). Can self-reference be shown to induce hierarchical structure that imports those properties?

This is real mathematical work. It hasn’t been done. The paper is honest about that gap.

-----

## 9. Conclusion

We have proposed that **certain forms of self-reference may create curvature** in information geometry, and that this curvature may enable verification capacity through mechanisms **analogous to** parallel transport.

**What is established:**

- Information geometry is well-founded
- *e* is intrinsic to Fisher metric (Čencov’s theorem)
- LLMs fail at hold-and-check (N=700 empirical study)

**What is analogy:**

- Parallel transport as model for working memory (structural similarity, not proven identity)

**What is hypothesis:**

- Self-reference creates curvature
- Curvature enables verification
- Geometric and dynamical *e* are non-trivially connected

**What the framework provides:**

- Testable architectural prediction (self-monitoring vs. scale)
- Clear epistemic status of each claim
- Identification of what formal work would resolve the open questions

The framework is a research program, not finished theory. The strongest version—where everything is proven identical rather than analogous—would require mathematical work this paper identifies but does not complete.

The weakest defensible version: self-modeling and verification are connected; the connection might be geometric; testing whether explicit self-monitoring architecture improves verification is the cleanest experiment. That version is actionable even if the geometric interpretation remains speculative.

-----

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics*. Springer.

Amari, S., & Nagaoka, H. (2000). *Methods of Information Geometry*. AMS.

Baddeley, A. (2000). The episodic buffer. *Trends in Cognitive Sciences*, 4(11), 417-423.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS.

Danan, H. (2025). Hold-and-check failures in large language models. *Working paper*.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Phil. Trans. R. Soc. B*, 367(1594), 1338-1349.

Friston, K. (2010). The free-energy principle. *Nature Reviews Neuroscience*, 11(2), 127-138.

-----

## Appendix: Concrete Example for Section 3.3

**Example system:** Self-referential Gaussian

Let a system estimate the mean μ of incoming data, with uncertainty σ². Suppose the system’s *learning rate* depends on its current uncertainty estimate:

$$\theta = \alpha(\sigma^2)$$

where α is learning rate and σ² is the system’s estimate of its own uncertainty.

**Self-referential structure:** The system’s parameters (θ) depend on its state estimate (σ²), which itself is updated using those parameters.

**To compute curvature:**

1. The Fisher information for Gaussian with mean μ, variance σ² has known form:
   $$G = \begin{pmatrix} 1/\sigma^2 & 0 \ 0 & 1/(2\sigma^4) \end{pmatrix}$$
1. With θ = α(σ²), the effective parameter space has additional structure
1. Curvature calculation requires working through Christoffel symbols and Riemann tensor for this specific case

**Status:** This is sketched, not completed. The point is that such calculations are tractable for specific examples, even if general theorems are hard.

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper*.

-----

*“The strongest claims require the strongest proofs. This paper offers the claims; the proofs remain to be constructed.”*

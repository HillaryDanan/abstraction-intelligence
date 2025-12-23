# The Geometry of Self-Reference: Information-Theoretic Foundations for Self-State and Metacognitive Capacity

**Hillary Danan, PhD**  
Cognitive Neuroscience

*Working Draft — December 2025*

-----

## Abstract

Why can some systems verify their own computations while others cannot? We propose that the capacity for self-monitoring—what we term “hold-and-check”—may have a geometric foundation. Drawing on information geometry (Amari, 1985), we hypothesize that certain forms of self-modeling create *curvature* in a system’s information manifold, enabling verification through mechanisms analogous to parallel transport.

The framework generates one particularly clean prediction: an architectural experiment comparing matched systems with and without explicit self-monitoring. We are explicit throughout about what is established (information geometry foundations), what is analogy (parallel transport as model for working memory), and what remains hypothesis (self-reference creating curvature). The geometric framing is currently more suggestive than explanatory—it provides language for qualitative distinctions but does not yet generate quantitative predictions that simpler accounts couldn’t. We address this limitation directly.

**Keywords:** information geometry, self-reference, metacognition, Fisher information, large language models

-----

## 1. Introduction: The Verification Problem

A failure pattern has emerged in large language models: systems that correctly compute intermediate values yet reach conclusions inconsistent with those values (Danan, 2025). The computation succeeds; the verification fails. This **hold-and-check failure** appears across task types.

Recent empirical work (N=700, Claude Sonnet) revealed task-specific asymmetries: arithmetic shows verification deficits (+24-26%), logic shows generation deficits (-18-44%). The overall difference was null (p=0.58), masking structured patterns.

We propose a geometric hypothesis: **certain forms of self-reference create curvature**, and curvature enables verification. This paper develops the hypothesis honestly—including where it currently falls short.

### 1.1 Epistemic Status

|Status         |Meaning                                        |
|---------------|-----------------------------------------------|
|**Established**|Proven in peer-reviewed literature             |
|**Theoretical**|Logical extension of established results       |
|**Hypothesis** |Novel claim requiring proof/validation         |
|**Analogy**    |Structural similarity; identity not established|

### 1.2 What This Paper Does and Doesn’t Do

**Does:**

- Names a specific failure mode (hold-and-check) with empirical support
- Proposes a geometric framework as candidate explanation
- Generates a testable architectural prediction
- Is explicit about uncertainty at each step

**Doesn’t:**

- Prove the geometric claims
- Generate quantitative predictions the geometry uniquely enables
- Resolve the boundary between pattern-matching and self-reference

-----

## 2. Information Geometry: Established Foundations

### 2.1 Statistical Manifolds

**Established:** Information geometry treats probability distributions as points on a differential manifold (Amari, 1985). For parametric family p(x; θ), parameter space Θ forms manifold M.

### 2.2 The Fisher Information Metric

**Established:** The natural metric on statistical manifolds is Fisher information:

$$g_{ij}(\theta) = E\left[\frac{\partial \log p(x; \theta)}{\partial \theta^i} \frac{\partial \log p(x; \theta)}{\partial \theta^j}\right]$$

**Established (Čencov, 1982):** The Fisher metric is *unique* (up to scaling) among Riemannian metrics invariant under sufficient statistics and monotonic under coarse-graining. This uniqueness means Euler’s number *e* is intrinsic to information geometry—it appears necessarily in the natural logarithms defining the metric (see Appendix A for discussion of whether this connects non-trivially to dynamical systems).

### 2.3 Curvature and Parallel Transport

**Established:** On Riemannian manifolds:

- **Curvature** measures deviation from flatness
- **Parallel transport** moves vectors along paths while preserving geometric properties
- On *flat* manifolds, parallel transport is path-independent
- On *curved* manifolds, parallel transport depends on the path taken

-----

## 3. The Self-Reference Hypothesis

### 3.1 Core Claim

**Hypothesis:** Certain forms of self-modeling create non-zero curvature in a system’s information manifold.

**Definition (Self-Modeling):** A system self-models if its generative model includes representations of its own internal states: p(x, s; θ) where s denotes internal states and θ includes parameters about s.

### 3.2 What the Hypothesis Is Not

The claim is *not* that self-reference *necessarily* creates curvature for all functional forms. Different dependencies between parameters θ and states s could yield zero or non-zero curvature.

**Refined claim:** Self-reference *enables* curvature in self-dimensions. Non-trivial self-modeling (where θ depends non-linearly on s) should produce non-zero curvature. This requires formal proof we have not completed.

### 3.3 What Would a Proof Require?

1. **Specify θ(s) structure:** Define how model parameters depend on internal state
1. **Compute Fisher information:** Calculate G for this self-referential structure
1. **Calculate curvature:** Derive Riemann tensor R from G
1. **Characterize conditions:** Identify which θ(s) forms yield R ≠ 0

**Current status:** This derivation has not been completed. Appendix B sketches a specific example (self-referential Gaussian) that could be worked through.

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
- Different problems sharing vocabulary (concerning possibility)

What would establish identity:

1. Show the “held value” lives in tangent space of the information manifold
1. Show “state evolution during inference” corresponds to geodesic movement
1. Show “verification failure” corresponds to holonomy (path-dependence)

None demonstrated. The analogy is useful for capturing qualitative structure; it is not a proven mechanism.

### 4.3 What Does the Geometry Add?

**Critical question:** Does the geometric framing generate predictions that simpler accounts couldn’t?

**Honest answer:** Not yet, at least not quantitatively.

A simpler account: “Verification requires active maintenance; LLMs lack active maintenance mechanisms; therefore LLMs fail at verification.” This captures the same qualitative prediction without Riemannian geometry.

**What geometry could add (but doesn’t yet):**

- Quantitative predictions about *degree* of verification failure from curvature magnitude
- Predictions about *which* tasks fail from geometric properties of the relevant belief spaces
- Unification with other phenomena that have known geometric structure

**Current status:** The geometric framing is evocative and may eventually prove explanatory. Currently it provides language for qualitative distinctions rather than quantitative predictions. This is a limitation.

-----

## 5. The Self-Modeling Boundary Problem

### 5.1 The Core Difficulty

**Critical question:** What counts as “self-modeling”? Where’s the threshold between sophisticated pattern-matching and genuine self-reference?

This is not a minor technical issue. The entire framework depends on this distinction being real and detectable.

### 5.2 The Self-Attention Challenge

Transformers attend over their own prior activations. Is this self-modeling?

**The attempted distinction:**

|Property        |Self-Attention                         |Self-Modeling (Hypothesized)    |
|----------------|---------------------------------------|--------------------------------|
|What’s accessed |Prior outputs/activations              |Model of own computational state|
|Representation  |Implicit in weights/activations        |Explicit state representation   |
|Update mechanism|Fixed attention computation            |Model of own dynamics           |
|Counterfactual  |“What would I output if input changed?”|“What would my *state* be if…?” |

**Honest assessment:** This distinction is intuitive but operationally fuzzy.

The problem: self-attention over activations *is* a form of referencing one’s own computational history. Calling it “not self-modeling” because it doesn’t involve an “explicit” state representation begs the question of what “explicit” means.

### 5.3 Proposed Operationalization

**Testable criterion:** A system self-models if we can decode, from its internal activations, a representation of its own uncertainty/confidence that:

1. Is distinct from its object-level representations
1. Tracks actual performance calibration
1. Can be intervened on to affect behavior

**Probe experiment:** Train a classifier to predict “will this system’s output be correct?” from internal activations. If successful, the system maintains something like self-model. If not, it doesn’t.

**Limitation:** This operationalizes *functional* self-modeling. Whether functional self-modeling is sufficient for the geometric claims remains unclear.

### 5.4 Binary vs. Continuous: An Open Question

The framework as presented assumes a threshold: no self-modeling → flat; self-modeling → curved.

**Alternative possibility:** Self-modeling is continuous, and so is curvature. There’s no threshold, just gradations.

**Implications:**

- If threshold: architectural change required for verification capacity
- If continuous: scaling might gradually increase curvature and verification

**Current position:** We frame this as binary for testability, but acknowledge this is an assumption. The architectural experiment (Section 6) can help distinguish: if *any* amount of self-attention produces *some* verification capacity scaling with model size, the continuous picture is supported. If verification capacity is absent without explicit self-monitoring regardless of scale, the threshold picture is supported.

-----

## 6. The Architectural Experiment

### 6.1 Design

This is the paper’s most concrete contribution: a clean experimental test.

**System A (Control):** Standard transformer

- Large parameter count
- Self-attention over context
- No explicit self-monitoring module

**System B (Experimental):** Transformer with self-monitoring

- Matched parameter count
- Includes explicit self-monitoring module that:
  - Maintains representation of “current computational state”
  - Updates based on own activations
  - Can be queried during inference
  - Feeds back into main computation

### 6.2 Predictions

|Hypothesis                                   |Prediction                                           |
|---------------------------------------------|-----------------------------------------------------|
|Self-modeling threshold (geometric framework)|B >> A on verification tasks, regardless of A’s scale|
|Continuous self-modeling                     |B > A, but scaling A helps too                       |
|Self-modeling irrelevant                     |B ≈ A                                                |

### 6.3 Why This Test Is Clean

1. **Controls for scale:** Matched parameters isolates architecture
1. **Operationalizes self-modeling:** The module is explicit and defined
1. **Measurable outcome:** Verification accuracy on hold-and-check tasks
1. **Falsifiable:** If B ≈ A, the framework is in trouble

### 6.4 What This Test Doesn’t Resolve

Even if B >> A, this supports “self-monitoring architecture helps verification” without confirming the *geometric* interpretation specifically. The result would be consistent with simpler accounts (“explicit maintenance helps”) without requiring curvature.

The geometric framework would require additional tests:

- Does verification capacity correlate with measurable curvature?
- Do systems with different curvature profiles show different verification patterns?

These are harder to operationalize. The architectural experiment is a necessary first step.

-----

## 7. Predictions and Falsification

### 7.1 Core Predictions

|Prediction                                 |Test                                            |Falsification                      |
|-------------------------------------------|------------------------------------------------|-----------------------------------|
|Explicit self-monitoring helps verification|Architectural experiment (Section 6)            |No improvement with self-monitoring|
|Scaling without self-modeling doesn’t help |Verification performance vs. model size         |Scaling alone produces verification|
|Self-modeling threshold exists             |Probe for discontinuity in verification capacity|Continuous improvement with scale  |

### 7.2 What Would Falsify the Framework

1. **Scaling produces verification:** Sufficiently large transformers show genuine hold-and-check → threshold claim wrong
1. **Self-monitoring doesn’t help:** Adding explicit self-monitoring produces no verification improvement → self-modeling/verification link wrong
1. **Continuous curvature without self-reference:** Formal analysis shows standard transformers have non-trivial curvature → self-reference/curvature link wrong
1. **Curvature without verification:** Systems with demonstrated curvature fail at hold-and-check → curvature/verification link wrong

-----

## 8. Discussion

### 8.1 The Strongest Claim

“LLMs fail at hold-and-check because they lack mechanisms for active maintenance during state change.”

This is supported by:

- Empirical documentation of hold-and-check failures (N=700)
- The observation that verification requires something distinct from retrieval
- The architectural prediction (testable)

### 8.2 The Weakest Claim

“The mechanism is specifically information-geometric curvature enabling parallel transport.”

This is:

- Not proven mathematically
- Not generating unique quantitative predictions
- Possibly just evocative vocabulary for a simpler phenomenon

### 8.3 What’s Worth Preserving

Even if the geometric interpretation is wrong, the paper contributes:

1. **Naming the failure mode:** “Hold-and-check failure” isolates something real
1. **The architectural prediction:** Self-monitoring vs. scale is testable
1. **Epistemic honesty:** Explicit about what’s established vs. hypothesized

### 8.4 Path Forward

**Near-term:** Run the architectural experiment. If self-monitoring helps, continue; if not, abandon.

**Medium-term:** If self-monitoring helps, probe whether the geometric interpretation adds anything. Can we measure curvature? Does it predict verification capacity beyond simpler variables?

**Long-term:** If geometric interpretation proves out, formalize. Prove the self-reference → curvature theorem. Derive quantitative predictions.

-----

## 9. Conclusion

We have proposed that **certain forms of self-reference may create curvature** in information geometry, and that this curvature may enable verification through mechanisms **analogous to** parallel transport.

**What is established:**

- Information geometry is well-founded (Amari, 1985; Čencov, 1982)
- LLMs fail at hold-and-check (N=700 empirical study)

**What is analogy:**

- Parallel transport as model for working memory

**What is hypothesis:**

- Self-reference creates curvature
- Curvature enables verification

**What is honest limitation:**

- The geometry doesn’t yet generate unique quantitative predictions
- The self-modeling boundary is fuzzy
- Binary vs. continuous is assumed, not demonstrated

**What is actionable:**

- The architectural experiment (Section 6)

The framework is a research program announcement. The strongest version—where curvature is proven, predictions are quantitative, and the geometry does unique explanatory work—would require mathematical and empirical progress this paper identifies but does not complete.

The weakest defensible version: self-monitoring architecture probably helps verification; this is testable; the geometric interpretation may or may not prove useful. That version is actionable now.

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

## Appendix A: The *e* Convergence Question

### A.1 The Observation

Euler’s number *e* appears in:

- **Information geometry:** Fisher metric uses natural logs; maximum entropy distributions are exponential families
- **Dynamical systems:** State-dependent growth ($dA/dt = kA$) yields $A = A_0 e^{kt}$

If self-referential systems have curved information geometry *and* exhibit state-dependent learning dynamics, both would involve *e*.

### A.2 The Problem

**Objection:** *e* saturates continuous mathematics. Finding it in both frameworks might reflect shared mathematical substrate (“both use calculus”) rather than deep structural identity.

**What would distinguish genuine from trivial convergence:**

- **Trivial:** Both frameworks involve continuous dynamics → both have exponentials → same *e* appears
- **Genuine:** The *same* time constants, derived from *same* structure—not just “both have exponentials”

### A.3 What Would Be Required

To establish genuine convergence:

1. Derive learning time constants τ from information-geometric quantities (Fisher information magnitude, geodesic length)
1. Show τ = f(G) for specific function f
1. Empirically verify this relationship

### A.4 Current Status

This has not been done. The connection remains suggestive but unestablished. We flag it as potentially interesting rather than claiming it as result.

-----

## Appendix B: Sketch Toward Proof of Self-Reference → Curvature

### B.1 Example System: Self-Referential Gaussian

Consider a system estimating mean μ of incoming data, with learning rate depending on uncertainty estimate:

$$\theta = \alpha(\sigma^2)$$

where α is learning rate, σ² is the system’s estimate of its own uncertainty.

**Self-referential structure:** Parameters θ depend on state estimate σ², which is updated using those parameters.

### B.2 Known Results

For Gaussian with mean μ, variance σ², Fisher information is:

$$G = \begin{pmatrix} 1/\sigma^2 & 0 \ 0 & 1/(2\sigma^4) \end{pmatrix}$$

This has known curvature properties (Amari, 1985, Ch. 3).

### B.3 The Extension

With θ = α(σ²), the effective parameter space has additional structure. Computing curvature requires:

1. Defining the augmented parameter space
1. Computing Fisher information for the self-referential model
1. Deriving Christoffel symbols
1. Computing Riemann tensor

### B.4 Status

This is outlined, not completed. The point: such calculations are tractable for specific examples. A general theorem (“self-reference implies curvature under conditions C”) would require either:

- Working many examples to find pattern
- Direct proof from structure of self-referential Fisher information

Either is substantive mathematical work beyond this paper’s scope.

-----

## Appendix C: Relation to Other Frameworks

### C.1 Active Inference (Friston, 2010)

**Established:** Active inference uses information geometry. Agents minimize variational free energy with geometric interpretation as divergence on information manifold.

**Connection:** Active inference requires self-modeling. If our hypothesis is correct, active inference agents have curved geometry. Frameworks are compatible.

### C.2 Global Workspace Theory (Baars, 1988)

**Speculation:** Could global workspace correspond to curved regions where parallel transport is non-trivial? Unformalized.

### C.3 Integrated Information Theory (Tononi, 2004)

**Speculation:** Φ and scalar curvature R both measure “irreducible wholeness.” Connection unexplored.

-----

**Citation:** Danan, H. (2025). The geometry of self-reference: Information-theoretic foundations for self-state and metacognitive capacity. *Working paper*.

-----

*“The strongest claims require the strongest proofs. This paper offers claims, identifies what proofs would require, and proposes experiments for the parts that don’t require proof—just data.”*

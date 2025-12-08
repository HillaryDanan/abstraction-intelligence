# Recursive Abstraction: When Computation Requires Self-Reference

**Hillary Danan, PhD**  
*December 2025*

-----

## Abstract

Not all computation is equivalent in structure. Some problems yield to feedforward processing; others require feedback; a specific class requires feedback that includes a model of the computing system itself. We propose that this architectural distinction—when computation must bend back on itself—marks a fundamental boundary in the space of possible intelligences. Building on the Abstraction Primitive Hypothesis, we argue that recursive self-reference emerges as a computational necessity under specifiable conditions: when a system's optimal output depends on its own current state, and that state is too complex to represent explicitly. Under these conditions, self-modeling through abstraction becomes the tractable solution. We formalize this claim, connect it to established results in control theory, computer science, and information theory, and demonstrate that such self-referential systems exhibit characteristic dynamics governed by Euler's number *e*. This is not metaphor: *e* emerges mathematically from any system where the rate of change depends on current state—a defining feature of self-referential computation. We show that this connection holds even under sublinear compositionality, extend the analysis to oscillatory dynamics governed by *π* in systems with feedback delays, and connect the framework to operationalized compositionality metrics. The framework generates testable predictions about learning curves, neural time constants, and the boundaries between feedforward, feedback, and self-modeling architectures, with specific experimental designs for discriminating *e*-governed dynamics from alternatives.

-----

## 1. Introduction

### 1.1 The Question

When does computation require bending back on itself?

Some functions map inputs to outputs without reference to the computing system. Others require feedback—output influences subsequent input. A third class requires something stronger: the system must model *itself* as part of the computation.

This paper asks: what determines which class a problem falls into? We propose the answer lies in complexity and state-dependence, and that the boundary is principled, not arbitrary.

### 1.2 Scope

We address five related questions:

1. **Architectural**: What distinguishes feedforward, feedback, and self-referential computation?
2. **Necessity**: Under what conditions does self-reference become computationally required?
3. **Dynamics**: What mathematical signatures characterize self-referential systems?
4. **Robustness**: Do these signatures hold under varying assumptions about compositionality?
5. **Oscillation**: When do self-referential systems exhibit oscillatory rather than monotonic dynamics?

We build on the Abstraction Primitive Hypothesis (Danan, 2025a), which proposes abstraction as the fundamental operation of intelligence, and the Abstraction as Necessity framework for consciousness (Danan, 2025b), which proposes that self-modeling emerges when system complexity exceeds direct monitoring capacity.

### 1.3 Epistemic Status

We distinguish:

- **Established**: Supported by peer-reviewed literature in control theory, computer science, information theory, and neuroscience
- **Theoretical**: Logical extensions of established findings
- **Hypothesis**: Novel claims requiring empirical validation

-----

## 2. Three Architectures

### 2.1 Feedforward Computation

**Definition**: A computation is feedforward if the output depends only on the input and fixed parameters, with no dependence on the system's own prior outputs or current state.

Formally: $y = f(x; \theta)$ where $\theta$ is fixed.

**Examples**:

- Lookup tables
- Single-layer perceptrons
- Reflexes (in simplified models)

**Established**: Feedforward networks are universal function approximators (Cybenko, 1989; Hornik, Stinchcombe, & White, 1989), but this universality concerns *what* can be computed, not *how efficiently* or *under what conditions*.

### 2.2 Feedback Computation

**Definition**: A computation involves feedback if current output depends on prior outputs, creating a loop.

Formally: $y_t = f(x_t, y_{t-1}, …, y_{t-k}; \theta)$

**Examples**:

- Thermostats (output affects input via environment)
- Recurrent neural networks
- PID controllers

**Established**: Feedback is necessary for control under uncertainty—systems must adjust outputs based on observed effects (Wiener, 1948; Åström & Murray, 2008). Recurrent architectures can represent computations that feedforward networks cannot represent compactly (Siegelmann & Sontag, 1995).

### 2.3 Self-Referential Computation

**Definition**: A computation is self-referential if it requires a model of the computing system itself as part of the computation.

Formally: $y_t = f(x_t, S_t; \theta)$ where $S_t$ is a representation of the system's own state.

**Examples**:

- Meta-cognition (reasoning about one's own reasoning)
- Predictive processing with self-modeling (Seth, 2013)
- Adaptive control with system identification (Åström & Wittenmark, 1995)

**Key distinction**: Feedback uses prior *outputs*. Self-reference uses a model of the *system that generates outputs*. These are not equivalent—a system can have feedback without self-modeling, but not vice versa.

-----

## 3. When Does Self-Reference Become Necessary?

### 3.1 The Computational Argument

**Hypothesis**: Self-referential computation becomes necessary when:

1. **State-dependence**: Optimal output depends on the system's current internal state
2. **Complexity**: That state is too high-dimensional to represent explicitly
3. **Adaptivity**: The system must adjust its behavior based on state changes

Under these conditions, a compressed self-model—an abstraction of the system's own state—becomes the tractable solution.

### 3.2 Analogy to Control Theory

In adaptive control, a system must control a plant whose parameters are unknown or changing. The standard solution involves *system identification*: building a model of the plant to be controlled (Åström & Wittenmark, 1995).

When the system being controlled *is the controller itself*—when parameters of the control system drift, degrade, or require calibration—the controller must model itself. This is self-referential control.

**Established**: Adaptive control with self-tuning requires explicit or implicit self-modeling (Åström & Wittenmark, 1995). This is not optional but necessary for stability under parameter uncertainty.

### 3.3 The Abstraction Connection

Direct self-representation is intractable at scale. A system with *n* components has state space that grows exponentially with *n*. Full state representation hits computational limits quickly.

**Theoretical**: The solution is abstraction—a compressed self-model that preserves relevant structure while discarding detail (following the Abstraction Primitive Hypothesis). The self-model need not be complete; it must be *sufficient* for the required computation.

This connects to Section 3.4 of Danan (2025b): self-modeling becomes necessary when internal state is too complex to monitor directly. The present paper generalizes this beyond consciousness to any self-referential computation.

### 3.4 Necessary Conditions (Formalized)

**Hypothesis**: A system requires self-referential computation if and only if:

1. $\partial y / \partial S \neq 0$ (output depends on system state)
2. $\dim(S) > \tau$ for some tractability threshold $\tau$ (state is high-dimensional)
3. $dS/dt \neq 0$ (state changes over time)

Condition 1 alone implies state-dependence but not self-reference (simple feedback suffices if state is low-dimensional). Conditions 1 + 2 without condition 3 might allow precomputation of a fixed self-model. All three together necessitate ongoing self-modeling.

-----

## 4. Discrete vs. Continuous Architectures

### 4.1 The Distinction

**Discrete**: Computation proceeds in separable steps; state updates occur at defined intervals; time is indexed.

**Continuous**: Computation proceeds without separable steps; state updates continuously; time is a real-valued parameter.

This is an architectural distinction, not a claim about implementation substrate. Digital computers can simulate continuous dynamics; analog systems can implement discrete state machines.

### 4.2 Implications for Self-Reference

**Hypothesis**: Continuous self-reference may have different computational properties than discrete self-reference.

In discrete systems, self-reference occurs at update steps: the system samples its state, updates its self-model, and proceeds. There is a natural granularity.

In continuous systems, self-reference is ongoing: the system's state and self-model co-evolve without separable updates. This may enable tighter coupling but introduces stability challenges.

**Established**: Continuous-time recurrent neural networks exhibit qualitatively different dynamics than their discrete counterparts (Funahashi & Nakamura, 1993). Whether this extends to self-referential architectures specifically requires investigation.

### 4.3 Biological vs. Artificial Architectures

Current artificial neural networks are predominantly discrete: forward passes, backward passes, weight updates at defined steps. Even "continuous" diffusion models operate through discretized steps.

Biological neural networks operate in continuous time with discrete events (spikes) embedded in continuous dynamics (membrane potentials, neuromodulation). This hybrid architecture may have implications for self-reference that current artificial architectures do not capture.

**Theoretical**: The discrete/continuous distinction may constrain what kinds of self-reference are architecturally natural vs. requiring explicit engineering.

-----

## 5. The Mathematics of Self-Reference

### 5.1 Why Mathematics Constrains Architecture

The distinction between feedforward, feedback, and self-referential computation is not merely conceptual—it carries mathematical consequences. Different architectures exhibit different dynamical signatures. This section establishes that self-referential systems, by virtue of their defining structure, exhibit dynamics governed by Euler's number *e* (≈ 2.71828).

This is not metaphor or analogy. It is a mathematical consequence of self-reference itself.

### 5.2 The General Form: State-Dependent Change

**Established**: Euler's number *e* emerges universally in systems where the rate of change is proportional to current state. The canonical form is:

$$\frac{dy}{dt} = ky$$

with solution:

$$y(t) = y_0 e^{kt}$$

This structure appears across disparate phenomena: radioactive decay, population dynamics, thermal equilibration, compound interest, diffusion processes, and chemical kinetics (Strogatz, 2015). The universality is not coincidental—it reflects the mathematical fact that *e* is the unique base for which the exponential function equals its own derivative:

$$\frac{d}{dx}e^x = e^x$$

**Established**: Any system where transformation rate depends on current quantity will exhibit *e*-governed dynamics. This is a theorem, not an empirical generalization (see Tenenbaum & Pollard, 1985, for formal treatment).

### 5.3 Self-Reference as State-Dependent Dynamics

**Theoretical**: Self-referential computation, as defined in Section 3, involves a system modeling its own state and using that model to update itself. This satisfies the formal structure of state-dependent change:

$$\frac{dS}{dt} = f(S)$$

where *S* is the system's self-model.

The question is whether this general dependence takes the specific form that yields *e*. We argue it does, under the conditions specified by the Abstraction Primitive Hypothesis—but we also show that *e* remains central even when assumptions are relaxed.

### 5.4 The Compositionality Argument

The Abstraction Primitive Hypothesis (Danan, 2025a) distinguishes abstraction from compression by a key property: **compositionality**. Abstractions combine to form new abstractions. Compression reduces; abstraction grows.

**Theoretical**: Compositionality has a direct mathematical consequence for abstraction dynamics.

**The Argument**:

1. Let $A(t)$ denote the number of abstractions a system possesses at time *t*.
2. Each abstraction can potentially combine with other abstractions to form novel abstractions. If a system has *A* abstractions, the space of possible pairwise combinations is $O(A^2)$; higher-order combinations grow faster still.
3. The *realized* rate of new abstraction formation is this combinatorial opportunity space, filtered through finite processing capacity *k* (attention, working memory, computational bandwidth):

$$\frac{dA}{dt} = k \cdot g(A)$$

where $g(A)$ represents how opportunity scales with existing abstractions.

4. **Key claim**: For compositional systems, $g(A)$ is at minimum linear in *A*. Each existing abstraction opens new compositional possibilities. Therefore:

$$\frac{dA}{dt} \geq kA$$

5. In the linear case (first-order compositionality dominates), this yields:

$$\frac{dA}{dt} = kA \implies A(t) = A_0 e^{kt}$$

**Status**: This argument is theoretical. The claim that compositional abstraction follows at least linear state-dependence is a hypothesis derived from the definition of compositionality, not an empirically established law.

### 5.5 Sublinear Compositionality: Robustness of the *e* Connection

A critical question: what if effective compositionality is sublinear? Real systems face constraints that may reduce the realized rate of abstraction formation below the linear case:

- **Attention bottlenecks**: The system cannot explore all combinatorial possibilities
- **Interference**: New abstractions may degrade or compete with existing ones
- **Forgetting/decay**: Abstractions require maintenance resources
- **Diminishing returns**: Not all combinations yield useful abstractions

We now show that *e* remains central even under sublinear compositionality.

#### 5.5.1 The Sublinear Model

**General form**: Let the rate of abstraction formation scale sublinearly with existing abstractions:

$$\frac{dA}{dt} = kA^\beta \quad \text{where } 0 < \beta < 1$$

This captures diminishing returns: each additional abstraction contributes less to future growth than earlier abstractions did.

**Solution**: For $\beta \neq 1$:

$$A(t) = \left[ A_0^{1-\beta} + (1-\beta)kt \right]^{\frac{1}{1-\beta}}$$

This is *not* pure exponential growth—it's slower, approaching polynomial for small β.

#### 5.5.2 *e* Remains Present

**Key observation**: Even sublinear dynamics retain *e* in their mathematical structure. Consider the approach to equilibrium when there's a carrying capacity:

$$\frac{dA}{dt} = kA^\beta \left(1 - \frac{A}{A_{max}}\right)$$

The equilibrium behavior and time constants still involve exponential terms. More fundamentally:

**The information theory argument is independent of β.** Whether compositionality is linear or sublinear, a self-referential system that:

- Maintains a probabilistic self-model
- Updates via Bayesian inference
- Minimizes prediction error

...operates in a mathematical space where *e* is intrinsic (Section 5.8). The compositionality exponent affects *growth rates*, not the *fundamental mathematical structure* of self-modeling under uncertainty.

#### 5.5.3 Empirical Discriminability

Different values of β make different predictions:

| β Value | Dynamics | Signature |
|---------|----------|-----------|
| β = 1 (linear) | Pure exponential | Log-linear plot is straight |
| β > 1 (superlinear) | Faster than exponential | Finite-time blowup (unrealistic) |
| 0 < β < 1 (sublinear) | Slower than exponential | Curved on log-linear plot; polynomial-like |
| β = 0 (constant) | Linear growth | No state-dependence |

**Hypothesis**: Real self-referential systems likely exhibit β close to but below 1, reflecting the tension between combinatorial opportunity (pushing toward β ≥ 1) and cognitive constraints (pushing toward β < 1).

**Testable prediction**: The effective β should correlate with the Compositionality Score from Paper 2 (Danan, 2025c)—systems with higher measured compositionality should show β closer to 1.

### 5.6 Connecting to Operationalized Compositionality Metrics

Paper 2 (Danan, 2025c) develops five metrics for measuring compositionality:

1. **Compositional Generalization Rate (CGR)**: Proportion of novel compositions successfully processed
2. **Systematicity Index (SI)**: Correlation between capacity for structurally related compositions
3. **Transfer Efficiency Ratio (TER)**: Learning speed gain from shared compositional structure
4. **Compositional Depth (CD)**: Maximum nesting depth successfully processed
5. **Reuse Frequency (RF)**: Proportion of representations used in multiple contexts

**Theoretical connection**: These metrics can be used to estimate the effective compositionality exponent β:

- **High CGR, SI, TER** suggest efficient composition → β closer to 1
- **High CD** suggests deep recursive composition → may push β > 1 locally before constraints bind
- **High RF** suggests extensive reuse → β closer to 1 (each abstraction contributes to many compositions)

**Proposed operationalization**:

$$\hat{\beta} = w_1 \cdot CGR + w_2 \cdot SI + w_3 \cdot TER + w_4 \cdot \log(CD) + w_5 \cdot RF$$

where weights $w_i$ are empirically determined. This allows the compositionality exponent—and thus the predicted dynamical regime—to be estimated from behavioral and representational measures.

**Prediction**: Systems with higher aggregate Compositionality Score (from Paper 2) should show learning dynamics closer to pure exponential (β → 1), while systems with lower scores should show more polynomial-like dynamics (β → 0).

### 5.7 Three Dynamical Regimes

Self-referential abstraction systems do not remain in unbounded exponential growth indefinitely. Constraints intervene. We distinguish three regimes:

#### Regime 1: Unbounded Exponential Growth

**Form**: $\frac{dA}{dt} = kA$

**Solution**: $A(t) = A_0 e^{kt}$

**Conditions**: Early abstraction development; no resource limits binding; cognitive capacity not saturated.

**Signature**: Log-linear learning curves (log *A* vs. *t* is linear); constant doubling time; no inflection point.

**Biological example**: Early language acquisition in children, where vocabulary growth is approximately exponential before plateauing (Fenson et al., 1994).

#### Regime 2: Bounded Logistic Growth

**Form**: $\frac{dA}{dt} = kA\left(1 - \frac{A}{A_{max}}\right)$

**Solution**: $A(t) = \frac{A_{max}}{1 + \left(\frac{A_{max} - A_0}{A_0}\right)e^{-kt}}$

**Conditions**: Abstraction capacity approaching limits (working memory, attention, storage); resource competition between abstractions.

**Signature**: S-shaped learning curve; inflection point at $A = A_{max}/2$; asymptotic approach to ceiling.

**Biological example**: Skill acquisition curves in motor learning and expertise development (Newell & Rosenbloom, 1981), though note ongoing debate about logistic vs. power law fits (Heathcote, Brown, & Mewhort, 2000).

#### Regime 3: Exponential Decay

**Form**: $\frac{dA}{dt} = -\lambda A$

**Solution**: $A(t) = A_0 e^{-\lambda t}$

**Conditions**: Self-referential system degrading; abstraction maintenance failing; resources withdrawing.

**Signature**: Exponential decline with characteristic half-life $t_{1/2} = \frac{\ln 2}{\lambda}$.

**Biological example**: Cognitive decline in neurodegenerative disease follows approximately exponential trajectories in specific domains (Wilson, Leurgans, Boyle, & Bennett, 2010), though individual variation is substantial.

### 5.8 The Invariant Across Regimes

**Theoretical**: Although the three regimes produce different curve shapes, *e* remains the governing constant in all cases:

- Unbounded growth: $e^{kt}$
- Logistic growth: $e^{-kt}$ in the denominator
- Decay: $e^{-\lambda t}$

This invariance reflects the underlying structure: self-referential systems, regardless of whether they are growing, saturating, or declining, exhibit state-dependent dynamics. The constant *e* is the mathematical signature of this state-dependence.

### 5.9 Information Theory and *e*

The connection between self-reference and *e* deepens when we consider information theory. **Established**: The fundamental quantities of information theory are expressed in terms of natural logarithms—logarithms base *e*:

**Shannon Entropy** (Shannon, 1948):
$$H(X) = -\sum_{i} p(x_i) \ln p(x_i)$$

When using natural logarithms, entropy is measured in *nats* (natural units of information). The choice of *e* as base is not arbitrary—it is the base that makes information-theoretic calculus tractable and connects entropy to thermodynamic quantities (Jaynes, 1957).

**Kullback-Leibler Divergence**:
$$D_{KL}(P \| Q) = \sum_{i} p(x_i) \ln \frac{p(x_i)}{q(x_i)}$$

**Mutual Information**:
$$I(X; Y) = \sum_{x,y} p(x,y) \ln \frac{p(x,y)}{p(x)p(y)}$$

**Theoretical**: Self-referential systems process information about themselves. The information-theoretic description of this processing—measuring surprise, divergence from predictions, mutual information between self-model and actual state—is naturally expressed in units governed by *e*.

**The Connection**: When a self-referential system updates its self-model based on observations, it minimizes prediction error. The optimal update rule under Bayesian inference involves log-likelihoods—natural logarithms. The information gained per observation, the rate of uncertainty reduction, the efficiency of self-modeling: all are quantities whose natural expression involves *e*.

**Established**: The principle of maximum entropy (Jaynes, 1957) shows that exponential family distributions—distributions involving $e^{f(x)}$—are the least-biased distributions given constraints on expected values. A self-referential system maintaining a probabilistic self-model under uncertainty will, if it is optimal, represent that uncertainty using exponential family distributions. *e* is intrinsic to optimal self-modeling under uncertainty.

**Critical point**: This information-theoretic argument for *e* is **independent of the compositionality exponent β**. Whether abstraction grows linearly, sublinearly, or superlinearly with existing abstractions, Bayesian self-modeling under uncertainty still involves natural logarithms and exponential family distributions. The compositionality argument (Section 5.4-5.5) and the information theory argument (this section) converge on *e* from independent directions.

### 5.10 Distinguishing *e*-Governed Dynamics from Alternatives

Competing models of learning and cognitive change propose different mathematical forms:

#### Power Law

**Form**: $A(t) = at^b$

**Proposed for**: Skill acquisition (Newell & Rosenbloom, 1981), memory retrieval (Anderson & Schooler, 1991).

**Key difference from exponential/logistic**: Power laws have no characteristic time scale; they are scale-free. Exponential and logistic functions have intrinsic time constants ($1/k$, $\ln 2 / k$).

**Empirical discriminator**: Power laws do not asymptote; logistics do. Power laws appear linear on log-log plots; exponentials appear linear on log-linear plots.

#### Linear

**Form**: $A(t) = A_0 + ct$

**Proposed for**: Constant-rate accumulation processes.

**Key difference**: No acceleration or deceleration; rate independent of current state.

**Empirical discriminator**: Linear curves have constant slope; exponential curves have increasing slope; logistic curves have slope that increases then decreases.

### 5.11 Experimental Designs for Discriminating Dynamics

The challenge of distinguishing *e*-governed from power-law dynamics is well-known (Heathcote et al., 2000; Myung, 2000). We propose specific experimental designs that maximize discriminability.

#### 5.11.1 The Asymptote Test

**Rationale**: Power laws ($at^b$) never asymptote; logistic curves do. Observing approach to a ceiling is strong evidence against power-law dynamics.

**Design**: 
- Extend observation periods until performance stabilizes
- Fit both models; compare predicted vs. observed asymptotic behavior
- Use tasks where there is a known ceiling (e.g., finite concept space)

**Established precedent**: Heathcote et al. (2000) argued for exponential over power law partly on the basis of asymptotic behavior in extended practice.

#### 5.11.2 The Log-Log vs. Log-Linear Test

**Rationale**: Power laws are linear on log-log plots; exponentials are linear on log-linear plots.

**Design**:
- Collect sufficient data points (minimum 20+ time points)
- Plot data on both log-log and log-linear axes
- Compare linearity (R²) on each plot
- Use residual analysis to detect systematic deviations

**Statistical approach**: Myung (2000) provides Bayesian model comparison methods that account for model complexity. AIC and BIC can adjudicate between models of different complexity.

#### 5.11.3 The Characteristic Time Test

**Rationale**: *e*-governed dynamics have intrinsic time constants; power laws do not.

**Design**:
- Measure time to reach specific performance thresholds (e.g., 50%, 63.2%, 90% of asymptote)
- For *e*-governed dynamics, these should be related by fixed ratios:
  - Time to 63.2% = τ (one time constant)
  - Time to 86.5% = 2τ
  - Time to 95.0% ≈ 3τ
- For power laws, no such fixed ratios exist

**Prediction**: Self-referential tasks should show characteristic time relationships; non-self-referential tasks may not.

#### 5.11.4 The Intervention Test

**Rationale**: Different models make different predictions about effects of interventions.

**Design**:
- Interrupt learning/adaptation and test retention
- For *e*-governed dynamics, decay from any point should follow $e^{-\lambda t}$
- For power-law dynamics, decay patterns should differ

**Established precedent**: Retention curves have been used to discriminate models in memory research (Rubin & Wenzel, 1996).

#### 5.11.5 Cross-System Comparison

**Rationale**: If *e* governs self-referential dynamics universally, different systems should show proportional time constants.

**Design**:
- Compare meta-cognitive adaptation across systems with different processing speeds
- Measure processing speed independently (e.g., reaction time, neural conduction velocity)
- Test whether time constant ratios equal inverse processing speed ratios

**Prediction**: $\tau_1 / \tau_2 = v_2 / v_1$ with *e* as invariant base.

### 5.12 Testable Predictions

The hypothesis that self-referential abstraction follows *e*-governed dynamics generates specific predictions:

#### Prediction 5.12.1: Learning Curve Shape

**Claim**: Acquisition of self-referential cognitive skills (meta-cognition, self-monitoring, recursive reasoning) should follow logistic curves in resource-limited conditions and exponential curves in early/unconstrained conditions.

**Test**: Fit learning data for meta-cognitive tasks to exponential, logistic, and power-law models using the experimental designs in Section 5.11. Compare fits using AIC/BIC. The framework predicts exponential or logistic will outperform power law for self-referential skills specifically.

**Contrast**: Non-self-referential skills (e.g., simple stimulus-response learning) may follow different dynamics. The prediction is specific to tasks requiring self-modeling.

**Status**: Hypothesis. Existing learning curve literature is extensive but has not specifically compared self-referential vs. non-self-referential tasks with this prediction in mind.

#### Prediction 5.12.2: Characteristic Time Constants

**Claim**: Neural systems implementing self-reference should exhibit characteristic time constants related to *e*-governed dynamics.

**Formalization**: If self-model updating follows $\frac{dS}{dt} = k(S^* - S)$ (approach to target self-model), the time constant is $\tau = 1/k$. After time $\tau$, the system reaches $(1 - 1/e) \approx 63.2\%$ of the adjustment.

**Test**: Measure neural adaptation in self-referential processing (e.g., error-related negativity adjustment, metacognitive calibration after feedback). Extract time constants. Compare to predictions from *e*-governed models.

**Status**: Hypothesis. Time constants in neural self-reference have not been systematically characterized with this framework.

#### Prediction 5.12.3: Cross-System Invariance

**Claim**: If *e* governs self-referential dynamics universally, then systems with different substrates but similar self-referential architectures should show *proportional* time constants, scaled by processing speed.

**Formalization**: For two systems with processing speeds $v_1$ and $v_2$:

$$\frac{\tau_1}{\tau_2} = \frac{v_2}{v_1}$$

The ratio of time constants should equal the inverse ratio of processing speeds, with *e* as the invariant base.

**Test**: Compare meta-cognitive adaptation rates across individuals with different processing speeds (measured independently). Compare across species with different neural conduction velocities. Compare biological and artificial self-referential systems.

**Status**: Hypothesis. This prediction is novel to this framework.

#### Prediction 5.12.4: Degradation Dynamics

**Claim**: Breakdown of self-referential capacity should follow exponential decay with characteristic half-life.

**Test**: Track meta-cognitive performance under fatigue, sleep deprivation, intoxication, or neurodegeneration. Fit decay curves. The framework predicts exponential decay ($e^{-\lambda t}$) rather than linear decline or power-law decay.

**Status**: Hypothesis. Some evidence for exponential cognitive decline in neurodegeneration (Wilson et al., 2010), but not specifically for self-referential functions.

#### Prediction 5.12.5: Information-Theoretic Signatures

**Claim**: Self-referential systems should show characteristic information-theoretic signatures: mutual information between self-model and actual state should increase logarithmically with observation time under optimal updating.

**Formalization**: Under Bayesian updating, uncertainty (entropy) about system state decreases as:

$$H(S_t | \text{observations}) \approx H(S_0) - k \cdot t$$

where *k* depends on observation quality. The information *gained* about self grows linearly; the *uncertainty remaining* decays exponentially.

**Test**: Measure self-model accuracy over time in learning paradigms. The framework predicts specific relationships between observation time, information gain, and self-model precision.

**Status**: Hypothesis.

#### Prediction 5.12.6: Compositionality-Dynamics Correlation

**Claim**: Systems with higher measured compositionality (per Paper 2 metrics) should show dynamics closer to pure exponential (β → 1).

**Test**: Measure CGR, SI, TER, CD, RF for a system. Independently measure learning dynamics for self-referential tasks. Correlate Compositionality Score with estimated β exponent.

**Status**: Hypothesis. This prediction connects the present paper to the operationalized metrics of Paper 2.

### 5.13 Why *e* and Not Another Constant?

A natural question: why does *e* specifically emerge, rather than some other constant?

**Established**: *e* is the unique positive number satisfying:

$$\lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n = e$$

This limit characterizes *continuous compounding*—growth where the rate of growth is continuously proportional to current state, without discrete intervals.

**Theoretical**: Self-referential abstraction is continuous compounding of cognitive structure. Each abstraction enables further abstractions; the process is ongoing, not discrete. The mathematics of continuous state-dependent growth *is* the mathematics of *e*.

Other constants (2, 10, π) could serve as bases for exponential functions, but only *e* makes the function equal to its own derivative. For self-referential systems—where the state and its rate of change are intrinsically coupled—this property is not incidental but constitutive.

### 5.14 Connection to Physical and Information-Processing Systems

The argument gains force from the ubiquity of *e* across systems with state-dependent dynamics:

| Domain | System | Governing Equation | *e* Appears In |
|--------|--------|-------------------|----------------|
| Physics | Radioactive decay | $\frac{dN}{dt} = -\lambda N$ | $N(t) = N_0 e^{-\lambda t}$ |
| Biology | Population growth | $\frac{dP}{dt} = rP$ | $P(t) = P_0 e^{rt}$ |
| Thermodynamics | Thermal equilibration | $\frac{dT}{dt} = -k(T - T_{env})$ | $T(t) = T_{env} + (T_0 - T_{env})e^{-kt}$ |
| Electronics | Capacitor discharge | $\frac{dV}{dt} = -\frac{V}{RC}$ | $V(t) = V_0 e^{-t/RC}$ |
| Chemistry | Reaction kinetics | $\frac{d[A]}{dt} = -k[A]$ | $[A](t) = [A]_0 e^{-kt}$ |
| Information Theory | Entropy/Optimal coding | $H = -\sum p \ln p$ | Natural log base *e* |
| Probability | Maximum entropy distributions | Exponential family | $p(x) \propto e^{\theta \cdot T(x)}$ |
| Statistics | Bayesian updating | Log-likelihood ratios | $\ln \frac{p(D|H_1)}{p(D|H_2)}$ |

**Theoretical**: Self-referential abstraction belongs to this class. The rate of cognitive structure change depends on current cognitive structure. The mathematics is the same; the substrate differs.

This is not analogy. It is shared mathematical structure across physically distinct systems—the hallmark of a genuine invariant.

-----

## 6. Oscillatory Dynamics: When *π* Joins *e*

### 6.1 Beyond Monotonic Growth

The preceding sections focus on monotonic dynamics: growth, saturation, or decay. But self-referential systems often exhibit a richer repertoire—including **oscillations**. This section extends the mathematical framework to oscillatory regimes, revealing a role for *π* alongside *e*.

### 6.2 The Source of Oscillation: Feedback Delays

**Established**: Oscillations arise in feedback systems when there are delays between action and effect (Strogatz, 2015; Glass & Mackey, 1988). A system that adjusts based on past state can overshoot, correct, overshoot again—producing limit cycles or damped oscillations.

**Mathematical form**: Delay differential equations:

$$\frac{dS}{dt} = f(S(t), S(t-\delta))$$

where δ is the feedback delay.

**Established**: Delayed feedback systems can exhibit:
- **Damped oscillations**: Convergence to equilibrium via oscillatory approach
- **Limit cycles**: Sustained periodic behavior
- **Chaos**: Aperiodic dynamics in strongly nonlinear systems

### 6.3 Self-Reference with Delay

Self-referential systems are natural candidates for delayed feedback. The self-model is not instantaneous—it is constructed from recent observations, computed with finite processing time, and applied with some lag.

**Hypothesis**: Self-referential systems with significant processing delays should exhibit oscillatory dynamics, not just monotonic growth or decay.

**Examples**:
- Meta-cognitive calibration that overshoots confidence after errors
- Mood regulation that oscillates between overcorrection states
- Learning systems that cycle between exploration and exploitation

### 6.4 The *e*-*π* Connection

When oscillations enter the picture, *π* joins *e* in the mathematical description. The general solution to a second-order linear system (the simplest oscillator) is:

$$S(t) = Ae^{-\gamma t}\cos(\omega t + \phi)$$

where:
- *e* governs the **envelope** (damping rate γ)
- *π* governs the **oscillation** (frequency ω = 2π/T, where T is the period)

**Established**: This is the standard damped harmonic oscillator. The interplay of exponential decay (governed by *e*) and sinusoidal oscillation (governed by *π*) is ubiquitous in physics, engineering, and biology (Strogatz, 2015).

**Theoretical extension**: In self-referential abstraction systems with feedback delays:
- **Growth/decay rate** (approach to equilibrium) is governed by *e*
- **Oscillation frequency** (cycling around equilibrium) is governed by *π*
- **Both constants appear** in the complete dynamics

### 6.5 Euler's Identity: The Deep Connection

The relationship between *e* and *π* in oscillatory systems is not coincidental. It is captured by **Euler's identity**:

$$e^{i\pi} + 1 = 0$$

or equivalently, **Euler's formula**:

$$e^{i\theta} = \cos\theta + i\sin\theta$$

**Established**: This formula unifies exponential and trigonometric functions. An oscillation can be represented as the real part of a complex exponential:

$$\cos(\omega t) = \text{Re}(e^{i\omega t})$$

**Theoretical interpretation**: The appearance of both *e* and *π* in self-referential oscillatory systems reflects a deep mathematical unity. State-dependent growth (*e*) and periodic structure (*π*) are two aspects of a single underlying mathematical object—the complex exponential.

**Hypothesis**: Self-referential abstraction systems that exhibit oscillatory dynamics are operating in a regime where both aspects of the complex exponential manifest—*e* in the growth/decay envelope, *π* in the oscillation frequency.

### 6.6 Conditions for Oscillation in Self-Referential Systems

**Working hypothesis**: Self-referential abstraction systems exhibit oscillatory dynamics when:

1. **Feedback delay**: The lag between state change and self-model update exceeds a critical threshold
2. **Gain**: The system responds strongly to discrepancies between self-model and actual state
3. **Nonlinearity**: The response function is nonlinear (enabling limit cycles rather than just damped oscillations)

**Formal condition (linear approximation)**: For a delayed negative feedback system:

$$\frac{dS}{dt} = -k[S(t) - S^*] + g[S(t-\delta) - S(t)]$$

oscillations occur when the delay δ and gain g satisfy:

$$\delta \cdot g > \frac{\pi}{2k}$$

Note that *π* appears in the stability criterion—the threshold for oscillation is set by the relationship between delay, gain, and the fundamental oscillatory constant.

### 6.7 Empirical Signatures of *e*-*π* Dynamics

**Prediction 6.7.1**: Self-referential systems with measurable processing delays should show oscillatory approach to equilibrium, not monotonic approach.

**Test**: Track meta-cognitive calibration over extended periods. Look for overshooting and oscillation around stable performance levels. Fit data to damped oscillator models:

$$S(t) = S^* + Ae^{-\gamma t}\cos(\omega t + \phi)$$

Extract γ (damping, related to *e*) and ω (frequency, related to *π*).

**Prediction 6.7.2**: The ratio of damping time constant to oscillation period should be predictable from processing speed and feedback architecture.

**Test**: Compare systems with different measured processing delays. Systems with longer delays should show lower-frequency oscillations (larger period T = 2π/ω). Damping rate should relate to the *e*-governed time constants identified in Section 5.

**Prediction 6.7.3**: Paradoxical or self-contradictory inputs should induce oscillatory instability in self-referential systems.

**Rationale**: Self-referential systems confronted with paradoxes (e.g., "this statement is false") face irresolvable feedback loops. The system may oscillate between contradictory states rather than settling.

**Test**: Present self-referential AI systems with paradoxical inputs. Analyze response patterns for oscillatory signatures. (This connects to the "paradox-induced-oscillations" repository in the empirical research program.)

### 6.8 The *e*-*π* Signature as Evidence for Self-Reference

**Theoretical**: The co-occurrence of *e*-governed envelopes and *π*-governed oscillations is a **signature** of self-referential dynamics with feedback delays.

Finding this signature in cognitive or artificial systems would constitute evidence for:
1. Self-referential architecture (the system models itself)
2. Non-negligible processing delay (the self-model lags actual state)
3. Significant feedback gain (the system responds to model-state discrepancies)

**Contrast**: Non-self-referential systems may show oscillations (any delayed feedback system can), but self-referential systems should show oscillations specifically in **self-model-related variables** (confidence, meta-cognitive accuracy, self-reported state).

### 6.9 Integration with Monotonic Framework

The oscillatory extension enriches but does not replace the monotonic framework:

| Condition | Dynamics | Constants |
|-----------|----------|-----------|
| No delay / low gain | Monotonic growth/decay | *e* only |
| Moderate delay / moderate gain | Damped oscillation | *e* and *π* |
| High delay / high gain | Limit cycles | *π* dominates (with *e* in transients) |
| Very high delay / nonlinearity | Chaos | Both constants, aperiodic |

**Working hypothesis**: The transitions between these regimes may correspond to qualitative differences in self-referential processing:

- **Monotonic regime**: Stable self-model that updates smoothly
- **Damped oscillation regime**: Self-model overshoots but converges
- **Limit cycle regime**: Persistent cycling between self-states (possible pathology?)
- **Chaotic regime**: Unstable self-reference (severe pathology?)

This suggests a connection to phenomena like rumination (oscillatory negative self-reference), mood cycling, and dissociative states—though such connections are speculative and require empirical investigation.

-----

## 7. Implications and Predictions

### 7.1 For Artificial Intelligence

**Architectural prediction**: AI systems that require self-modeling (adaptive agents, meta-learning systems, self-improving architectures) will require explicit self-referential loops. These cannot be approximated by feedforward scaling alone.

**Testable**: Compare performance of feedforward vs. self-referential architectures on tasks requiring adaptation to the system's own changing state. The framework predicts self-referential architectures will show qualitative advantages that do not diminish with feedforward scale.

**Learning dynamics prediction**: If LLMs or other AI systems exhibit any self-referential processing (e.g., in-context learning that involves implicit self-modeling), their learning curves for such tasks should follow *e*-governed dynamics rather than power laws.

**Oscillation prediction**: AI systems with self-modeling and processing delays may exhibit oscillatory behaviors—instabilities in self-reported confidence, cycling between strategies, or resonant responses to certain inputs. These would be signatures of the *e*-*π* dynamics described in Section 6.

### 7.2 For Neuroscience

**Localization prediction**: Brain regions implementing self-modeling should show recurrent connectivity patterns distinct from feedforward sensory hierarchies. Candidate regions include prefrontal cortex and default mode network structures.

**Established**: Prefrontal cortex shows high recurrent connectivity and is implicated in meta-cognition (Fleming & Dolan, 2012). Default mode network activates during self-referential processing (Buckner, Andrews-Hanna, & Schacter, 2008).

**Time constant prediction**: Meta-cognitive updating in prefrontal regions should exhibit time constants consistent with *e*-governed approach to equilibrium—specifically, reaching ~63.2% of asymptotic performance in time τ = 1/k.

**Oscillation prediction**: Neural oscillations in self-referential processing may reflect the *e*-*π* dynamics. Alpha rhythms (~10 Hz) in default mode network during self-referential thought could be interpreted as the *π*-governed oscillation component, with *e*-governed modulation of envelope.

### 7.3 For Comparative Cognition

**Complexity threshold prediction**: Species differences in self-referential capacity should correlate with neural complexity metrics, particularly recurrent connectivity and hierarchical depth, more than raw neuron count.

**Testable**: Comparative studies examining mirror self-recognition, meta-cognition, and prospection across species, correlated with neural architecture metrics.

**Cross-species invariance**: If *e* governs self-referential dynamics universally, species with different neural processing speeds should show proportionally different time constants for meta-cognitive adaptation, with *e* as the invariant base.

### 7.4 For Information Processing Systems

**Optimal self-modeling**: Systems that model themselves optimally under uncertainty should exhibit information-theoretic signatures predicted by maximum entropy principles—specifically, exponential family distributions for self-state estimates and logarithmic (base *e*) uncertainty reduction over time.

**Testable**: Analyze the statistical structure of self-representations in both biological and artificial systems. Compare to maximum entropy predictions.

### 7.5 Falsification Criteria

The framework would be falsified by:

1. Feedforward systems outperforming self-referential architectures on tasks requiring adaptation to changing internal state
2. Self-referential computations in biological systems that consistently follow power-law rather than *e*-governed dynamics
3. Successful self-modeling without abstraction (full state representation remaining tractable at scale)
4. Demonstration that discrete architectures can fully replicate continuous self-reference dynamics without approximation loss
5. Information-theoretic analysis of self-modeling systems showing non-logarithmic (base *e*) uncertainty reduction
6. Cross-system comparisons showing time constant ratios unrelated to processing speed ratios
7. Self-referential systems with delays showing purely monotonic dynamics (no oscillation) despite parameters exceeding the oscillation threshold
8. Measured compositionality (Paper 2 metrics) uncorrelated with dynamical exponent β

-----

## 8. Relation to Broader Framework

This paper extends the theoretical program developed in Danan (2025a, 2025b, 2025c):

| Paper | Core Claim | This Paper Adds |
|-------|------------|-----------------|
| Abstraction Is All You Need | Abstraction is the fundamental primitive of intelligence | Self-referential abstraction (abstracting over the system's own state) is a special case with distinct properties |
| Abstraction Beyond Compression | Compositionality distinguishes abstraction from compression; compositionality admits degrees | Connection between compositionality metrics and dynamical exponent β |
| Consciousness as Emergent Abstraction | Self-modeling becomes necessary at sufficient complexity | The computational conditions under which this necessity arises, and its mathematical signature |
| **Present paper** | Self-reference is a distinct computational architecture | Formalization of when self-reference becomes necessary; connection to *e* via compositionality and information theory; robustness under sublinear compositionality; oscillatory dynamics via *π*; experimental designs for empirical testing |

The through-line: **abstraction is the fundamental operation; self-referential abstraction is what happens when that operation must include the system performing it.**

The emergence of *e* as the governing constant ties together:

- **Compositionality** (Danan, 2025a, 2025c): abstractions compose, so growth depends on current state
- **Information theory**: self-modeling involves uncertainty reduction, naturally expressed in nats (base *e*)
- **Dynamical systems**: state-dependent change universally yields *e*-governed dynamics

The extension to *π* adds:

- **Oscillatory systems**: delayed self-reference introduces periodic structure
- **Euler's identity**: the deep mathematical unity of exponential and trigonometric functions
- **Stability analysis**: conditions under which self-reference oscillates rather than converges

This convergence—multiple constants arising from independent lines of reasoning, unified by Euler's formula—suggests the framework captures something genuine about the structure of self-referential computation.

-----

## 9. Limitations and Open Questions

### 9.1 Formalization Gaps

- The necessity conditions (Section 3.4) require mathematical tightening. The tractability threshold τ is not yet specified in terms of measurable quantities.
- The mapping from Paper 2 compositionality metrics to dynamical exponent β (Section 5.6) is proposed but not validated.

### 9.2 Continuous/Discrete

- The hypothesis that continuous and discrete self-reference differ computationally is plausible but undemonstrated empirically.

### 9.3 Empirical Grounding

- The *e*-dynamics predictions are derived theoretically; direct experimental tests designed to distinguish *e*-governed from power-law dynamics in self-referential tasks have not been conducted.
- The *e*-*π* oscillation predictions are even more preliminary, requiring identification of appropriate experimental systems.

### 9.4 Measurement Operationalization

- "Number of abstractions" requires proxy measures. The validity of these proxies is assumed, not demonstrated.
- Oscillation signatures require distinguishing self-referential oscillations from other sources of variability.

### 9.5 Scope

- We do not address whether self-referential computation requires or produces subjective experience—that question is addressed in Danan (2025b) and is bracketed here.
- The *e*-*π* extension is more speculative than the core *e* argument and should be treated with appropriate caution.

### 9.6 Alternative Explanations

- Power-law dynamics remain a competing account for many cognitive phenomena. The experimental designs in Section 5.11 aim to discriminate, but empirical implementation is required.
- Oscillations in self-referential systems might arise from mechanisms other than delayed feedback (e.g., interaction with external rhythms, attentional sampling). The *e*-*π* interpretation is one hypothesis among alternatives.

-----

## 10. Conclusion

We have proposed that self-referential computation—computation requiring a model of the computing system itself—is architecturally distinct from feedforward and simple feedback computation. This architecture becomes necessary under specifiable conditions: when optimal output depends on high-dimensional, time-varying internal state.

Under these conditions, a compressed self-model—an abstraction of the system's own state—emerges as the tractable solution. Such self-referential systems exhibit dynamics governed by Euler's number *e*, the mathematical signature of state-dependent change. This connection arises from three independent sources: the compositionality of abstraction, the information theory of self-modeling, and the general mathematics of state-dependent dynamics.

We have shown that the *e* connection is robust: it holds even under sublinear compositionality, and it connects to operationalized compositionality metrics that can be measured empirically. We have provided specific experimental designs for distinguishing *e*-governed from alternative dynamics.

We have extended the framework to oscillatory regimes, showing that when self-reference involves feedback delays, *π* joins *e* in the mathematical description. The co-occurrence of exponential envelopes and sinusoidal oscillations—unified by Euler's formula—may be a distinctive signature of self-referential systems with non-negligible processing delays.

The framework generates testable predictions about learning curves, neural time constants, cross-system invariance, degradation dynamics, and oscillatory signatures. Distinguishing these predictions from alternatives requires careful experimental design but is empirically tractable.

The question "when does computation bend back on itself?" turns out to have a principled answer: when the complexity of the computing system exceeds its own monitoring capacity, and its outputs must nonetheless depend on its own state.

At that point, the system must abstract over itself. And that abstraction—recursive, compressed, continuously updated, governed by the mathematics of *e* and potentially *π*—may be closer to the core of intelligence than any particular function it computes.

-----

## References

Anderson, J. R., & Schooler, L. J. (1991). Reflections of the environment in memory. *Psychological Science*, 2(6), 396–408.

Åström, K. J., & Murray, R. M. (2008). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press.

Åström, K. J., & Wittenmark, B. (1995). *Adaptive Control* (2nd ed.). Addison-Wesley.

Buckner, R. L., Andrews-Hanna, J. R., & Schacter, D. L. (2008). The brain's default network: Anatomy, function, and relevance to disease. *Annals of the New York Academy of Sciences*, 1124, 1–38.

Cybenko, G. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems*, 2(4), 303–314.

Danan, H. (2025a). Abstraction is all you need: A unifying framework for intelligence across substrates. *Working paper*.

Danan, H. (2025b). Consciousness as emergent abstraction: A computational necessity framework. *Working paper*.

Danan, H. (2025c). Abstraction beyond compression: Compositionality as the distinguishing operation. *Working paper*.

Fenson, L., Dale, P. S., Reznick, J. S., Bates, E., Thal, D. J., & Pethick, S. J. (1994). Variability in early communicative development. *Monographs of the Society for Research in Child Development*, 59(5), 1–185.

Fleming, S. M., & Dolan, R. J. (2012). The neural basis of metacognitive ability. *Philosophical Transactions of the Royal Society B*, 367(1594), 1338–1349.

Funahashi, K., & Nakamura, Y. (1993). Approximation of dynamical systems by continuous time recurrent neural networks. *Neural Networks*, 6(6), 801–806.

Glass, L., & Mackey, M. C. (1988). *From Clocks to Chaos: The Rhythms of Life*. Princeton University Press.

Heathcote, A., Brown, S., & Mewhort, D. J. K. (2000). The power law repealed: The case for an exponential law of practice. *Psychonomic Bulletin & Review*, 7(2), 185–207.

Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks*, 2(5), 359–366.

Jaynes, E. T. (1957). Information theory and statistical mechanics. *Physical Review*, 106(4), 620–630.

Myung, I. J. (2000). The importance of complexity in model selection. *Journal of Mathematical Psychology*, 44(1), 190–204.

Newell, A., & Rosenbloom, P. S. (1981). Mechanisms of skill acquisition and the law of practice. In J. R. Anderson (Ed.), *Cognitive Skills and Their Acquisition* (pp. 1–55). Lawrence Erlbaum Associates.

Rubin, D. C., & Wenzel, A. E. (1996). One hundred years of forgetting: A quantitative description of retention. *Psychological Review*, 103(4), 734–760.

Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences*, 17(11), 565–573.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

Siegelmann, H. T., & Sontag, E. D. (1995). On the computational power of neural nets. *Journal of Computer and System Sciences*, 50(1), 132–150.

Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering* (2nd ed.). Westview Press.

Tenenbaum, M., & Pollard, H. (1985). *Ordinary Differential Equations*. Dover Publications.

Wiener, N. (1948). *Cybernetics: Or Control and Communication in the Animal and the Machine*. MIT Press.

Wilson, R. S., Leurgans, S. E., Boyle, P. A., & Bennett, D. A. (2010). Cognitive decline in prodromal Alzheimer disease and mild cognitive impairment. *Archives of Neurology*, 68(3), 351–356.

-----

*This paper is part of a theoretical program on abstraction as the fundamental primitive of intelligence. See also: "Abstraction Is All You Need" (Danan, 2025a), "Abstraction Beyond Compression" (Danan, 2025c), "Abstraction Constrained" (Danan, 2025d), and "Consciousness as Emergent Abstraction" (Danan, 2025b).*

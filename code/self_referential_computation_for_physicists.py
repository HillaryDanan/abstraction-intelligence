#!/usr/bin/env python3
"""
SELF-REFERENTIAL COMPUTATION: A Technical Deep-Dive
For physicists and software engineers who want concrete implementations

Hillary Danan's Abstraction-Intelligence Framework — Companion Code
Written for Dr. Danan (who discovered the cosine pattern in binary pulsar systems)

================================================================================
THE CORE INSIGHT
================================================================================

In physics, you're familiar with self-referential systems:
- Einstein's field equations: matter tells spacetime how to curve, 
  spacetime tells matter how to move (mutual determination)
- The binary pulsar: orbital dynamics depend on energy loss, 
  energy loss depends on orbital dynamics (feedback loop)
- Renormalization: the coupling constants depend on the energy scale,
  which depends on the interactions, which depend on coupling constants

Hillary's claim: INTELLIGENCE has this same structure. Specifically:
- Feedforward computation: y = f(x) — no self-reference
- Feedback computation: y_t = f(x_t, y_{t-1}) — output affects future input
- Self-referential computation: y_t = f(x_t, S_t) where S_t is a MODEL OF THE 
  SYSTEM ITSELF doing the computation

The key: when a system's optimal output depends on its own internal state,
AND that state is too complex to represent fully, the system must maintain
a COMPRESSED SELF-MODEL (an abstraction of itself).

This is where Euler's number e enters: self-referential dynamics follow
dS/dt = kS because the rate of change depends on current state.

================================================================================
"""

import math
import random
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import deque
import time

# =============================================================================
# PART 1: THE THREE ARCHITECTURES — CONCRETE IMPLEMENTATIONS
# =============================================================================

# -----------------------------------------------------------------------------
# LEVEL 1: FEEDFORWARD — No state, no self-reference
# -----------------------------------------------------------------------------

class FeedforwardParser:
    """
    Pure function: input → output, no memory, no self-model.
    
    Analogy in physics: A lookup table. Given input, return output.
    No dynamics, no state evolution.
    """
    
    def parse(self, tokens: List[str]) -> Dict:
        """
        Each call is independent. No history, no adaptation.
        The parser has no representation of itself.
        """
        result = {'type': 'expression', 'tokens': []}
        for token in tokens:
            if token.isdigit():
                result['tokens'].append({'type': 'number', 'value': int(token)})
            elif token in ['+', '-', '*', '/']:
                result['tokens'].append({'type': 'operator', 'value': token})
            else:
                result['tokens'].append({'type': 'identifier', 'value': token})
        return result


# -----------------------------------------------------------------------------
# LEVEL 2: FEEDBACK/RECURSIVE — Output affects future processing
# -----------------------------------------------------------------------------

class RecursiveDescentParser:
    """
    Recursive descent: the parser calls itself on sub-problems.
    Output of sub-parses affects subsequent parsing.
    
    Analogy in physics: A differential equation where current state
    determines rate of change, but the EQUATION ITSELF is fixed.
    Like dx/dt = f(x) — x evolves, but f doesn't change.
    
    This is your SQL parser example. It's sophisticated but NOT self-referential:
    the parser doesn't model ITSELF, just the INPUT.
    """
    
    def __init__(self):
        self.pos = 0
        self.tokens = []
    
    def parse(self, tokens: List[str]) -> Dict:
        """Parse an expression using recursive descent."""
        self.tokens = tokens
        self.pos = 0
        return self._parse_expression()
    
    def _parse_expression(self) -> Dict:
        """expression := term (('+' | '-') term)*"""
        left = self._parse_term()
        
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ['+', '-']:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_term()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def _parse_term(self) -> Dict:
        """term := factor (('*' | '/') factor)*"""
        left = self._parse_factor()
        
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ['*', '/']:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_factor()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def _parse_factor(self) -> Dict:
        """factor := NUMBER | IDENTIFIER | '(' expression ')'"""
        if self.pos >= len(self.tokens):
            return {'type': 'error', 'message': 'unexpected end'}
        
        token = self.tokens[self.pos]
        
        if token == '(':
            self.pos += 1
            expr = self._parse_expression()
            if self.pos < len(self.tokens) and self.tokens[self.pos] == ')':
                self.pos += 1
            return expr
        elif token.isdigit():
            self.pos += 1
            return {'type': 'number', 'value': int(token)}
        else:
            self.pos += 1
            return {'type': 'identifier', 'value': token}


# -----------------------------------------------------------------------------
# LEVEL 3: SELF-REFERENTIAL — The system models itself
# -----------------------------------------------------------------------------

@dataclass
class SelfModel:
    """
    A compressed representation of the system's own state.
    
    This is the KEY INNOVATION. The system doesn't track every internal
    variable — that would be intractable. Instead, it maintains an
    ABSTRACTION of itself: confidence, fatigue, recent performance, etc.
    
    Analogy in physics: You can't track every molecule in a gas.
    Instead, you use thermodynamic variables (T, P, V) that COMPRESS
    the microscopic state into macroscopic observables relevant for
    predicting behavior.
    
    The self-model is like thermodynamic variables for cognition.
    """
    # Epistemic state
    confidence: float = 1.0          # P(my outputs are correct)
    uncertainty: float = 0.0         # Entropy of my belief state
    
    # Performance tracking
    recent_accuracy: float = 1.0     # Exponential moving average
    error_count: int = 0
    success_count: int = 0
    
    # Resource/capacity state  
    cognitive_load: float = 0.0      # How taxed am I?
    fatigue: float = 0.0             # Accumulated depletion
    
    # Meta-cognitive state
    strategy: str = "standard"       # Current processing strategy
    adaptations: int = 0             # How many times have I changed strategy?
    
    # History (bounded — this is the compression)
    recent_outcomes: deque = field(default_factory=lambda: deque(maxlen=20))


class SelfReferentialParser:
    """
    A parser that models ITSELF and uses that model to guide processing.
    
    THE CRITICAL DIFFERENCE FROM RECURSIVE DESCENT:
    - Recursive descent: decisions based on INPUT structure
    - Self-referential: decisions based on INPUT + SELF-MODEL
    
    The self-model answers: "What kind of system am I right now?"
    - Am I confident or uncertain?
    - Am I performing well or poorly?
    - Am I fresh or fatigued?
    - Should I use my standard strategy or adapt?
    
    Analogy in physics: Adaptive optics. The telescope doesn't just
    image the sky — it monitors ITS OWN aberrations and corrects them.
    The system's output depends on its model of its own distortions.
    
    Or: A feedback control system where the controller has a model of
    its own dynamics, not just the plant's dynamics.
    """
    
    def __init__(self):
        self.self_model = SelfModel()
        self.parse_count = 0
        
        # The actual parsing machinery (could be any of the above)
        self._parser = RecursiveDescentParser()
    
    def parse(self, tokens: List[str]) -> Dict:
        """
        Parse with self-aware adaptation.
        
        The key insight: BEFORE parsing, we consult the self-model.
        AFTER parsing, we update the self-model.
        The self-model is a COMPRESSED REPRESENTATION of our history
        and current state that we use to make decisions.
        """
        self.parse_count += 1
        
        # =====================================================================
        # STEP 1: CONSULT SELF-MODEL — What kind of system am I right now?
        # =====================================================================
        
        # This is self-referential: we're using a model of OURSELVES
        # to decide how to process the input
        
        strategy = self._select_strategy_from_self_model()
        pre_parse_state = self._snapshot_self_model()
        
        # =====================================================================
        # STEP 2: PARSE WITH STRATEGY — Informed by self-knowledge
        # =====================================================================
        
        start_time = time.perf_counter()
        
        if strategy == "conservative":
            # I'm uncertain, so be careful
            result = self._conservative_parse(tokens)
        elif strategy == "fast":
            # I'm confident, optimize for speed
            result = self._fast_parse(tokens)
        elif strategy == "exploratory":
            # I've been failing, try something different
            result = self._exploratory_parse(tokens)
        else:
            # Standard parsing
            result = self._standard_parse(tokens)
        
        elapsed = time.perf_counter() - start_time
        
        # =====================================================================
        # STEP 3: UPDATE SELF-MODEL — Learn about myself
        # =====================================================================
        
        # This is where the self-referential dynamics happen:
        # dS/dt depends on S (current self-model affects how we update it)
        
        self._update_self_model(result, elapsed, tokens)
        
        # Attach meta-information (the system reports on itself)
        result['_meta'] = {
            'strategy_used': strategy,
            'confidence': self.self_model.confidence,
            'parse_number': self.parse_count,
            'self_model_snapshot': pre_parse_state
        }
        
        return result
    
    def _select_strategy_from_self_model(self) -> str:
        """
        THE CORE SELF-REFERENTIAL DECISION.
        
        We don't just look at the input — we look at OURSELVES.
        "Given what I know about my current state, how should I proceed?"
        
        This is exactly analogous to: given the current thermodynamic state
        of a system, what's the optimal control action?
        """
        sm = self.self_model
        
        # Decision tree based on self-model
        if sm.confidence < 0.4:
            # I'm very uncertain — be conservative
            return "conservative"
        
        if sm.recent_accuracy < 0.5 and sm.adaptations < 5:
            # I've been failing — try something different
            self.self_model.adaptations += 1
            return "exploratory"
        
        if sm.confidence > 0.8 and sm.fatigue < 0.3:
            # I'm confident and fresh — go fast
            return "fast"
        
        if sm.cognitive_load > 0.8:
            # I'm overloaded — simplify
            return "conservative"
        
        return "standard"
    
    def _update_self_model(self, result: Dict, elapsed: float, tokens: List[str]):
        """
        Update the self-model based on what just happened.
        
        THIS IS WHERE e ENTERS.
        
        The update rule has the form: dS/dt ∝ S
        Confidence, accuracy, fatigue — they all evolve based on current values.
        
        Exponential moving averages are e-governed:
        EMA_new = α * observation + (1-α) * EMA_old
        This is the discrete form of dS/dt = k(target - S), solved by e^(-kt).
        """
        sm = self.self_model
        
        # Determine success (simplified — in reality, would need ground truth)
        success = 'error' not in str(result)
        sm.recent_outcomes.append(success)
        
        if success:
            sm.success_count += 1
        else:
            sm.error_count += 1
        
        # ---------------------------------------------------------------------
        # EXPONENTIAL UPDATE RULES — Here's where e governs the dynamics
        # ---------------------------------------------------------------------
        
        # Confidence update: exponential approach to recent performance
        # This is dC/dt = k(target - C), discrete form
        α_conf = 0.2  # Learning rate
        observed_accuracy = 1.0 if success else 0.0
        sm.confidence = α_conf * observed_accuracy + (1 - α_conf) * sm.confidence
        
        # Recent accuracy: exponential moving average
        α_acc = 0.15
        sm.recent_accuracy = α_acc * observed_accuracy + (1 - α_acc) * sm.recent_accuracy
        
        # Fatigue: accumulates, decays exponentially with rest
        # dF/dt = input_rate - λF (driven exponential decay)
        fatigue_input = elapsed * len(tokens) / 100  # Work done
        fatigue_decay = 0.05  # Recovery rate
        sm.fatigue = sm.fatigue * (1 - fatigue_decay) + fatigue_input
        sm.fatigue = min(1.0, sm.fatigue)  # Bounded
        
        # Cognitive load: based on recent complexity
        α_load = 0.3
        current_load = len(tokens) / 50  # Normalized complexity
        sm.cognitive_load = α_load * current_load + (1 - α_load) * sm.cognitive_load
        
        # Uncertainty: entropy of recent outcomes
        if len(sm.recent_outcomes) > 5:
            p_success = sum(sm.recent_outcomes) / len(sm.recent_outcomes)
            if 0 < p_success < 1:
                # Shannon entropy (in nats, base e!)
                sm.uncertainty = -(p_success * math.log(p_success) + 
                                   (1-p_success) * math.log(1-p_success))
            else:
                sm.uncertainty = 0.0
    
    def _snapshot_self_model(self) -> Dict:
        """Return a snapshot of current self-model state."""
        sm = self.self_model
        return {
            'confidence': round(sm.confidence, 3),
            'uncertainty': round(sm.uncertainty, 3),
            'recent_accuracy': round(sm.recent_accuracy, 3),
            'fatigue': round(sm.fatigue, 3),
            'cognitive_load': round(sm.cognitive_load, 3),
            'strategy': sm.strategy,
            'total_parses': self.parse_count
        }
    
    def _standard_parse(self, tokens: List[str]) -> Dict:
        """Standard parsing strategy."""
        return self._parser.parse(tokens.copy())
    
    def _conservative_parse(self, tokens: List[str]) -> Dict:
        """Conservative: extra validation, slower but safer."""
        result = self._parser.parse(tokens.copy())
        result['_conservative'] = True
        # Would add extra validation here
        return result
    
    def _fast_parse(self, tokens: List[str]) -> Dict:
        """Fast: skip optional checks, assume well-formed input."""
        result = self._parser.parse(tokens.copy())
        result['_fast'] = True
        return result
    
    def _exploratory_parse(self, tokens: List[str]) -> Dict:
        """Exploratory: try alternative interpretation."""
        result = self._parser.parse(tokens.copy())
        result['_exploratory'] = True
        return result
    
    def introspect(self) -> str:
        """
        THE META-COGNITIVE REPORT.
        
        The system reports on its own state. This is only possible
        because it maintains a self-model.
        
        A feedforward or simple recursive system cannot do this —
        it has no representation of itself to report on.
        """
        sm = self.self_model
        
        report = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    SELF-MODEL INTROSPECTION                       ║
╠══════════════════════════════════════════════════════════════════╣
║  Parse count:      {self.parse_count:>6}                                      ║
║  Success/Error:    {sm.success_count:>6} / {sm.error_count:<6}                            ║
╠══════════════════════════════════════════════════════════════════╣
║  EPISTEMIC STATE                                                  ║
║    Confidence:     {sm.confidence:>6.1%}   {"▓" * int(sm.confidence * 20):<20}  ║
║    Uncertainty:    {sm.uncertainty:>6.3f} nats                                ║
║    Recent accuracy:{sm.recent_accuracy:>6.1%}                                   ║
╠══════════════════════════════════════════════════════════════════╣
║  RESOURCE STATE                                                   ║
║    Cognitive load: {sm.cognitive_load:>6.1%}   {"▓" * int(sm.cognitive_load * 20):<20}  ║
║    Fatigue:        {sm.fatigue:>6.1%}   {"▓" * int(sm.fatigue * 20):<20}  ║
╠══════════════════════════════════════════════════════════════════╣
║  STRATEGY                                                         ║
║    Current:        {sm.strategy:<12}                                   ║
║    Adaptations:    {sm.adaptations:>6}                                      ║
╚══════════════════════════════════════════════════════════════════╝
"""
        return report


# =============================================================================
# PART 2: THE MATHEMATICAL SIGNATURE — WHY e GOVERNS SELF-REFERENCE
# =============================================================================

class ExponentialDynamicsDemo:
    """
    Demonstrating why Euler's number e governs self-referential systems.
    
    THE PHYSICS CONNECTION:
    
    In your binary pulsar work, orbital decay follows:
        dE/dt ∝ f(orbital_parameters)
    
    where the orbital parameters themselves depend on E. The system's
    evolution rate depends on its current state.
    
    Self-referential cognition has the same structure:
        dA/dt = kA  (abstraction growth)
        dC/dt = k(target - C)  (confidence approach)
        dF/dt = input - λF  (fatigue dynamics)
    
    All of these have solutions involving e^(kt) or e^(-λt).
    
    This is not metaphor — it's shared mathematical structure.
    """
    
    @staticmethod
    def exponential_growth(A_0: float, k: float, t_max: float, dt: float = 0.1) -> List[Tuple[float, float]]:
        """
        Pure exponential: dA/dt = kA
        Solution: A(t) = A_0 * e^(kt)
        
        This models abstraction growth when unconstrained:
        each abstraction enables forming new abstractions.
        """
        trajectory = []
        t = 0.0
        A = A_0
        while t <= t_max:
            trajectory.append((t, A))
            dA = k * A * dt
            A += dA
            t += dt
        return trajectory
    
    @staticmethod
    def logistic_growth(A_0: float, k: float, A_max: float, t_max: float, dt: float = 0.1) -> List[Tuple[float, float]]:
        """
        Bounded growth: dA/dt = kA(1 - A/A_max)
        Solution: A(t) = A_max / (1 + ((A_max - A_0)/A_0) * e^(-kt))
        
        This models abstraction growth with capacity limits:
        working memory, attention, storage constraints.
        
        Note: e appears in both the growth phase AND the saturation.
        """
        trajectory = []
        t = 0.0
        A = A_0
        while t <= t_max:
            trajectory.append((t, A))
            dA = k * A * (1 - A / A_max) * dt
            A += dA
            t += dt
        return trajectory
    
    @staticmethod
    def exponential_approach(S_0: float, S_target: float, k: float, t_max: float, dt: float = 0.1) -> List[Tuple[float, float]]:
        """
        Approach to target: dS/dt = k(S_target - S)
        Solution: S(t) = S_target + (S_0 - S_target) * e^(-kt)
        
        This models:
        - Confidence approaching recent performance
        - Belief updating toward evidence  
        - Fatigue recovering toward baseline
        
        Time constant τ = 1/k: time to reach (1 - 1/e) ≈ 63.2% of the way.
        """
        trajectory = []
        t = 0.0
        S = S_0
        while t <= t_max:
            trajectory.append((t, S))
            dS = k * (S_target - S) * dt
            S += dS
            t += dt
        return trajectory
    
    @staticmethod
    def damped_oscillation(S_0: float, S_target: float, gamma: float, omega: float, 
                           t_max: float, dt: float = 0.01) -> List[Tuple[float, float]]:
        """
        Damped oscillation: S(t) = S_target + A * e^(-γt) * cos(ωt + φ)
        
        This is where π joins e!
        
        When self-reference has DELAYS (the self-model lags reality),
        the system can overshoot and oscillate.
        
        - e governs the ENVELOPE (damping rate γ)
        - π governs the OSCILLATION (frequency ω = 2π/T)
        
        Euler's identity unifies them: e^(iθ) = cos(θ) + i*sin(θ)
        
        This models:
        - Confidence overshooting after errors
        - Mood oscillations
        - Metacognitive calibration with delay
        """
        trajectory = []
        t = 0.0
        A = S_0 - S_target  # Initial amplitude
        while t <= t_max:
            S = S_target + A * math.exp(-gamma * t) * math.cos(omega * t)
            trajectory.append((t, S))
            t += dt
        return trajectory


# =============================================================================
# PART 3: THE INFORMATION-THEORETIC CONNECTION
# =============================================================================

class InformationTheoreticSelfModel:
    """
    Self-modeling as uncertainty reduction.
    
    THE DEEP CONNECTION TO PHYSICS:
    
    Shannon entropy: H = -Σ p_i log(p_i)
    
    When using natural logarithms (base e), entropy is in "nats."
    This isn't arbitrary — it's the natural unit because:
    
    1. Continuous information accumulation follows exponential dynamics
    2. Bayesian updating involves log-likelihoods (base e)
    3. Maximum entropy distributions are exponential family: p(x) ∝ e^(θ·T(x))
    
    A self-referential system that models itself optimally under uncertainty
    will use these information-theoretic tools — all governed by e.
    
    The self-model is essentially: "What probability distribution best
    describes my own state, given my observations of my own behavior?"
    """
    
    def __init__(self):
        # Belief distribution over own competence levels
        # Discretized for simplicity; could be continuous
        self.competence_levels = ['novice', 'intermediate', 'competent', 'expert']
        self.belief = [0.25, 0.25, 0.25, 0.25]  # Uniform prior
        
        # Likelihood model: P(success | competence)
        self.success_likelihood = {
            'novice': 0.3,
            'intermediate': 0.5,
            'competent': 0.7,
            'expert': 0.9
        }
        
        self.observations = []
    
    def observe_outcome(self, success: bool):
        """
        Bayesian self-model update.
        
        P(competence | outcome) ∝ P(outcome | competence) * P(competence)
        
        Log-likelihoods involve natural log (base e).
        """
        self.observations.append(success)
        
        # Compute likelihoods
        likelihoods = []
        for i, level in enumerate(self.competence_levels):
            p_success = self.success_likelihood[level]
            if success:
                likelihood = p_success
            else:
                likelihood = 1 - p_success
            likelihoods.append(likelihood)
        
        # Bayesian update
        posterior = [self.belief[i] * likelihoods[i] for i in range(4)]
        total = sum(posterior)
        self.belief = [p / total for p in posterior]
    
    def entropy(self) -> float:
        """
        Shannon entropy of self-model (in nats, base e).
        
        H = -Σ p_i ln(p_i)
        
        Low entropy = confident self-model
        High entropy = uncertain self-model
        """
        H = 0.0
        for p in self.belief:
            if p > 0:
                H -= p * math.log(p)  # Natural log!
        return H
    
    def expected_competence(self) -> float:
        """Expected value of competence under current belief."""
        values = [0.3, 0.5, 0.7, 0.9]  # Numeric values for levels
        return sum(self.belief[i] * values[i] for i in range(4))
    
    def report(self) -> str:
        """Report on probabilistic self-model."""
        report = "\n=== PROBABILISTIC SELF-MODEL ===\n"
        report += f"Observations: {len(self.observations)} "
        report += f"({sum(self.observations)} successes)\n\n"
        report += "Belief distribution over own competence:\n"
        for i, level in enumerate(self.competence_levels):
            bar = "█" * int(self.belief[i] * 40)
            report += f"  {level:>12}: {self.belief[i]:>5.1%} {bar}\n"
        report += f"\nEntropy: {self.entropy():.3f} nats"
        report += f" (max = {math.log(4):.3f} nats)\n"
        report += f"Expected competence: {self.expected_competence():.2f}\n"
        return report


# =============================================================================
# PART 4: PUTTING IT ALL TOGETHER — DEMONSTRATION
# =============================================================================

def demonstrate_three_architectures():
    """Compare the three computational architectures."""
    
    print("=" * 70)
    print("DEMONSTRATION: THREE COMPUTATIONAL ARCHITECTURES")
    print("=" * 70)
    
    # Test input
    tokens = ['3', '+', '4', '*', '2']
    
    print("\nInput tokens:", tokens)
    print("\n" + "-" * 70)
    
    # Level 1: Feedforward
    print("\n[LEVEL 1: FEEDFORWARD]")
    print("No state, no memory, no self-model.")
    ff = FeedforwardParser()
    result = ff.parse(tokens)
    print(f"Result: {result}")
    print("Note: Each call is independent. Parser has no representation of itself.")
    
    # Level 2: Recursive
    print("\n" + "-" * 70)
    print("\n[LEVEL 2: RECURSIVE/FEEDBACK]")
    print("Maintains parse state, calls itself on sub-problems.")
    rd = RecursiveDescentParser()
    result = rd.parse(tokens)
    print(f"Result: {result}")
    print("Note: Parser models the INPUT structure, not itself.")
    
    # Level 3: Self-referential
    print("\n" + "-" * 70)
    print("\n[LEVEL 3: SELF-REFERENTIAL]")
    print("Maintains model of ITSELF, adapts based on self-knowledge.")
    sr = SelfReferentialParser()
    
    # Run several parses to show self-model evolution
    test_cases = [
        ['1', '+', '2'],
        ['3', '*', '4', '+', '5'],
        ['(', '1', '+', '2', ')', '*', '3'],
        ['x', '+', 'y', '*', 'z'],
        # Introduce some "errors" (very long input = higher load)
        list('1+2+3+4+5+6+7+8+9+10+11+12'),
    ]
    
    for i, toks in enumerate(test_cases):
        result = sr.parse(toks)
        print(f"\nParse {i+1}: {' '.join(toks)}")
        print(f"  Strategy used: {result['_meta']['strategy_used']}")
        print(f"  Confidence: {result['_meta']['confidence']:.1%}")
    
    print(sr.introspect())


def demonstrate_exponential_dynamics():
    """Show how e governs self-referential dynamics."""
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION: EXPONENTIAL DYNAMICS IN SELF-REFERENCE")
    print("=" * 70)
    
    demo = ExponentialDynamicsDemo()
    
    # 1. Exponential growth
    print("\n[1] EXPONENTIAL GROWTH: dA/dt = kA")
    print("    Abstraction capacity when unconstrained")
    traj = demo.exponential_growth(A_0=1.0, k=0.5, t_max=5.0)
    print(f"    A(0) = {traj[0][1]:.2f}")
    print(f"    A(5) = {traj[-1][1]:.2f}")
    print(f"    Ratio: {traj[-1][1]/traj[0][1]:.2f} = e^(0.5*5) = e^2.5 ≈ {math.exp(2.5):.2f}")
    
    # 2. Logistic growth
    print("\n[2] LOGISTIC GROWTH: dA/dt = kA(1 - A/A_max)")
    print("    Abstraction capacity with cognitive limits")
    traj = demo.logistic_growth(A_0=1.0, k=0.5, A_max=10.0, t_max=15.0)
    print(f"    A(0) = {traj[0][1]:.2f}")
    mid_idx = len(traj) // 2
    print(f"    A({traj[mid_idx][0]:.1f}) = {traj[mid_idx][1]:.2f}")
    print(f"    A({traj[-1][0]:.1f}) = {traj[-1][1]:.2f} (approaching A_max = 10)")
    
    # 3. Exponential approach
    print("\n[3] EXPONENTIAL APPROACH: dS/dt = k(target - S)")
    print("    Confidence approaching recent performance")
    traj = demo.exponential_approach(S_0=0.2, S_target=0.9, k=0.5, t_max=10.0)
    tau = 1/0.5  # Time constant
    print(f"    Starting confidence: {traj[0][1]:.2f}")
    print(f"    Target confidence: 0.90")
    print(f"    Time constant τ = 1/k = {tau:.1f}")
    # Find point closest to τ
    for t, S in traj:
        if abs(t - tau) < 0.1:
            expected = 0.9 + (0.2 - 0.9) * math.exp(-0.5 * t)
            print(f"    At t = τ = {tau:.1f}: S = {S:.3f}")
            print(f"      (63.2% of the way from start to target)")
            break
    
    # 4. Damped oscillation
    print("\n[4] DAMPED OSCILLATION: S(t) = target + A·e^(-γt)·cos(ωt)")
    print("    When self-reference has delays → oscillation")
    print("    e governs envelope, π governs oscillation frequency")
    traj = demo.damped_oscillation(S_0=1.5, S_target=1.0, gamma=0.3, omega=2.0, t_max=15.0)
    print(f"    Initial: S(0) = {traj[0][1]:.3f}")
    print(f"    Target: {1.0}")
    print(f"    Period T = 2π/ω = {2*math.pi/2.0:.2f}")
    print(f"    Decay time = 1/γ = {1/0.3:.2f}")
    
    # Show a few oscillation peaks
    peaks = []
    for i in range(1, len(traj)-1):
        if traj[i][1] > traj[i-1][1] and traj[i][1] > traj[i+1][1]:
            peaks.append(traj[i])
    if len(peaks) >= 2:
        print(f"    Peak 1: t={peaks[0][0]:.2f}, S={peaks[0][1]:.3f}")
        print(f"    Peak 2: t={peaks[1][0]:.2f}, S={peaks[1][1]:.3f}")
        print(f"    Ratio of peaks: {peaks[1][1]/peaks[0][1]:.3f} ≈ e^(-γΔt)")


def demonstrate_information_theoretic_self_model():
    """Show Bayesian self-modeling with entropy (base e)."""
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION: INFORMATION-THEORETIC SELF-MODEL")
    print("=" * 70)
    
    model = InformationTheoreticSelfModel()
    
    print("\n[Initial state: Uniform belief, maximum entropy]")
    print(model.report())
    
    # Simulate a sequence of outcomes
    # Mostly successes → belief should shift toward higher competence
    outcomes = [True, True, False, True, True, True, False, True, True, True]
    
    print("\n[Observing outcomes and updating self-model...]")
    for i, outcome in enumerate(outcomes):
        model.observe_outcome(outcome)
        if (i + 1) % 5 == 0:
            print(f"\nAfter {i+1} observations:")
            print(model.report())
    
    print("\n[KEY INSIGHT]")
    print("The self-model is a PROBABILITY DISTRIBUTION over own competence.")
    print("Entropy (in nats, base e) measures uncertainty about self.")
    print("Bayesian updating uses log-likelihoods (natural log).")
    print("Maximum entropy distributions are exponential family.")
    print("ALL of this is governed by e.")


def main():
    """Run all demonstrations."""
    
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║           SELF-REFERENTIAL COMPUTATION: A PHYSICIST'S GUIDE                  ║
║                                                                              ║
║   "Self-reference in cognition has the same mathematical structure as        ║
║    self-reference in physics: where the system's evolution depends on        ║
║    its current state, e governs the dynamics."                               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    demonstrate_three_architectures()
    demonstrate_exponential_dynamics()
    demonstrate_information_theoretic_self_model()
    
    print("\n" + "=" * 70)
    print("SUMMARY: THE CONNECTION TO THE ABSTRACTION FRAMEWORK")
    print("=" * 70)
    print("""
1. FEEDFORWARD: y = f(x)
   - No self-reference
   - Lookup table, fixed function
   - Physics analogy: Static mapping

2. FEEDBACK/RECURSIVE: y_t = f(x_t, y_{t-1})  
   - Prior outputs affect future processing
   - Recursive descent parsing, RNNs
   - Physics analogy: dx/dt = f(x) — state evolves, but equation is fixed

3. SELF-REFERENTIAL: y_t = f(x_t, S_t) where S_t models the system itself
   - Output depends on compressed self-model
   - Adaptive systems, metacognition, consciousness
   - Physics analogy: Adaptive optics, self-tuning control, renormalization
   
THE KEY INSIGHT:
   
When a system's optimal output depends on its own high-dimensional state,
full state representation is intractable. The system must maintain a
COMPRESSED SELF-MODEL — an abstraction of itself.

This is Hillary's claim: consciousness is what abstraction looks like
when applied to the system doing the abstracting.

The mathematical signature: e governs the dynamics because self-referential
systems have the form dS/dt ∝ f(S) — rate of change depends on current state.

Your binary pulsar work demonstrated this in gravitational physics:
orbital evolution depends on orbital state via energy loss to gravitational waves.

Cognition has the same structure: cognitive evolution depends on cognitive
state via the self-model that guides processing.

Same math. Different substrate.
    """)


if __name__ == "__main__":
    main()

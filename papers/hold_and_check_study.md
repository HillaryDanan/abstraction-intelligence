# Hold-and-Check Failures in Large Language Models: Task-Specific Dissociations Between Generation and Verification

**Draft Manuscript**

---

## Abstract

We tested whether large language models (LLMs) show systematic differences between generation tasks (produce an answer) and verification tasks (check if presented work is correct). Contrary to our initial hypothesis that verification would be uniformly harder than generation, we found **task-specific dissociations**: arithmetic and multi-step problems showed verification deficits (24-26 percentage points), while logic and word-counting showed generation deficits (18-44 percentage points). The overall difference was null (91.1% vs. 92.6%, p=0.58). We propose that both failure modes reflect a common underlying deficit: the inability to **hold and check**—whether holding a computed value to check presented work (verification failure) or holding constraints to check generated output before committing (generation failure). This reframing unifies apparently opposite patterns under a single architectural hypothesis: LLMs lack the active maintenance mechanisms required for self-monitoring during inference.

**Keywords:** large language models, verification, generation, working memory, self-monitoring, active maintenance

---

## Introduction

### The Puzzle of LLM Failures

Large language models exhibit inconsistent performance patterns that resist simple characterization. They solve complex problems yet fail unpredictably on seemingly simple tasks (Wei et al., 2022; Bubeck et al., 2023). Previous frameworks have sought to predict failures based on formal properties—compositional complexity (Lake & Baroni, 2018), reasoning depth (Dziri et al., 2023), or training distribution novelty. These approaches have yielded inconsistent results.

### The Generation-Verification Hypothesis

We proposed a different approach: comparing performance on matched problems presented either as generation tasks ("compute X") or verification tasks ("is this computation of X correct?"). The hypothesis was motivated by an observed failure pattern: LLMs often compute intermediate values correctly but reach incorrect conclusions—suggesting intact generation but impaired verification.

**Initial hypothesis:** Verification accuracy < Generation accuracy, because verification requires holding computed values for comparison, which autoregressive architectures may not support.

**Initial evidence (Experiment 1, N=60):** Overall verification (83.3%) was lower than generation (96.7%), with a striking arithmetic-specific effect (50% vs. 100%). This appeared to support the hypothesis.

### The Present Study

Experiment 2 tested this hypothesis at larger scale (N=700) across 7 problem types and 3 difficulty levels, with proper statistical analysis. The results were more complex—and more informative—than the initial hypothesis predicted.

---

## Methods

### Participants

Claude Sonnet (claude-sonnet-4-20250514; Anthropic, 2024). Single-model design enables controlled comparison but limits generalizability.

### Design

2 (Condition: generation vs. verification) × 7 (Problem Type) × 3 (Difficulty) mixed design.

**Problem types:**
- *Easy:* Arithmetic, sequence completion, word/letter counting
- *Medium:* Syllogistic logic, multi-step word problems, numerical comparison
- *Hard:* Graph degree counting

**N = 700 trials** (50 per type × 2 conditions × 7 types)

### Materials

**Generation trials:** Present problem, request answer.
- Example (arithmetic): "Calculate (25 + 17) × 4. Give the final answer."
- Example (logic): "All dogs are mammals. Fido is a dog. Is Fido a mammal? Answer YES or NO."

**Verification trials:** Present problem with solution (50% contain subtle errors), request CORRECT/ERROR judgment.
- Example (arithmetic): "Check this: 25+17=42, 42×4=168. Answer: 168. Is this CORRECT or ERROR?"
- Example (logic): "Check this reasoning: All dogs are mammals. Fido is a mammal. Therefore Fido is a dog. Is this CORRECT or ERROR?"

**Error types in verification trials:**
- Off-by-one arithmetic errors
- Wrong operation applied (addition vs. subtraction)
- Logical fallacies (affirming the consequent)
- Incorrect counts

### Procedure

Single API call per trial. Binary scoring (correct/incorrect). Trials randomized.

### Statistical Analysis

- Chi-square test for overall difference
- Fisher's exact test (confirmatory)
- Cohen's h for effect size
- Odds ratio with 95% CI
- Task-specific breakdown

---

## Results

### Overall: Null Effect

| Condition | Accuracy | n |
|-----------|----------|---|
| Generation | 91.1% | 319/350 |
| Verification | 92.6% | 324/350 |
| **Difference** | **-1.4%** | |

**Statistical tests:**
- χ²(1) = 0.48, p = 0.49
- Fisher's exact p = 0.58
- Cohen's h = -0.05 (negligible)
- OR = 0.83, 95% CI [0.48, 1.42]

**Conclusion:** The overall hypothesis (verification < generation) is **not supported**.

### Task-Specific Dissociations

| Problem Type | Generation | Verification | Δ | Direction |
|--------------|------------|--------------|---|-----------|
| Arithmetic | 100% | 76% | +24% | **Ver harder** |
| Multistep | 100% | 74% | +26% | **Ver harder** |
| Logic | 56% | 100% | -44% | **Gen harder** |
| Word count | 82% | 100% | -18% | **Gen harder** |
| Comparison | 100% | 100% | 0% | No difference |
| Sequence | 100% | 100% | 0% | No difference |
| Graph | 100% | 98% | +2% | No difference |

**Key finding:** The null overall effect masks two opposite task-specific patterns:
1. **Verification deficit** on arithmetic/multistep (+25% average)
2. **Generation deficit** on logic/word_count (-31% average)

### By Difficulty

| Difficulty | Generation | Verification | Δ |
|------------|------------|--------------|---|
| Easy | 94% | 92% | +2% |
| Medium | 85% | 91% | -6% |
| Hard | 100% | 98% | +2% |

Difficulty level does not predict which condition is harder.

---

## Discussion

### The Simple Hypothesis is Falsified

The hypothesis that verification is uniformly harder than generation is **not supported**. Overall accuracy is equivalent (91.1% vs. 92.6%, p=0.58).

### Two Distinct Failure Modes

The task-specific dissociations suggest **two distinct failure modes**:

**Failure Mode 1: Hold-and-Compare (Verification Deficit)**
- Affected tasks: Arithmetic, multi-step word problems
- Pattern: Perfect generation (100%), impaired verification (74-76%)
- Interpretation: The model can compute correctly but cannot hold the computed value while evaluating presented work

**Failure Mode 2: Pattern-Override (Generation Deficit)**
- Affected tasks: Logic (56%), word counting (82%)
- Pattern: Impaired generation, perfect verification (100%)
- Interpretation: The model pattern-matches a plausible-but-wrong answer during generation, but can recognize correct reasoning when presented

### A Unifying Framework: Hold-and-Check

Both failure modes may reflect a common underlying deficit: **the inability to hold and check**.

| Failure Mode | What Must Be Held | What Must Be Checked | Result |
|--------------|-------------------|---------------------|--------|
| Verification deficit | Computed intermediate value | Whether presented work matches | Correct computation, wrong judgment |
| Generation deficit | Constraint/rule | Whether generated output satisfies constraint | Pattern-matched output without constraint checking |

**The unifying claim:** LLMs lack **active maintenance**—the ability to hold information in a state where it can be continuously checked against ongoing processing.

This connects to Baddeley's (2000) distinction between storage (which attention can provide) and the central executive (which performs monitoring and verification). LLMs may have storage-like capabilities through attention but lack executive-like active maintenance.

### Why Task Type Determines Direction

**Arithmetic/multistep verification requires holding computed values:**
- Generation: Forward computation (pattern-matchable from training on math)
- Verification: Must compute answer AND compare to presented work
- The comparison step requires holding—which fails

**Logic/word-count generation requires constraint checking:**
- Logic generation: Must resist the "affirming the consequent" fallacy pattern
- Word-count generation: Must actually count, not estimate
- Verification: Correct reasoning is presented; just evaluate it
- Generation fails because output isn't checked against constraints before emission

**Sequence/comparison/graph show no asymmetry:**
- Both generation and verification are pattern-matchable for these tasks
- No holding-and-checking required beyond what attention provides

### Relation to Self-State Hypothesis

These findings are consistent with the broader self-state hypothesis (Danan, 2024): LLMs lack persistent self-state that would enable them to monitor "what I just computed" or "what constraints apply."

The causal chain:
```
Absent self-state
        ↓
No active maintenance mechanism
        ↓
Cannot hold-and-check during inference
        ↓
Task-specific failures depending on whether holding or checking is the bottleneck
```

**Verification tasks** make the holding requirement explicit (must hold computed value).
**Generation tasks** make the checking requirement implicit (should check output against constraints, but nothing forces this).

When the task structure demands explicit holding (verification on arithmetic), we see verification deficits.
When the task allows pattern-matching that bypasses checking (generation on logic), we see generation deficits.

### Implications

**For understanding LLM failures:**

The simple dichotomy "LLMs are good/bad at X" misses the structure. The same model shows opposite patterns on different tasks, depending on whether the bottleneck is holding or checking.

**For intervention design:**

- **Scaffolding** (chain-of-thought, scratchpads) should help when holding is the bottleneck—externalizing intermediate values into context
- **Explicit constraint prompting** should help when checking is the bottleneck—forcing the model to verify output against stated constraints
- These interventions should show task-specific benefits matching the task-specific deficits

**For architectural development:**

If the bottleneck is active maintenance, architectural interventions should target this specifically:
- Explicit working memory modules
- Recurrent verification loops
- Output-checking before emission

### Limitations

1. **Single model:** Results may not generalize across architectures
2. **Task selection:** The 7 tasks are not exhaustive; other tasks may show different patterns
3. **Binary scoring:** Loses information about partial success
4. **Prompt sensitivity:** Results may depend on specific prompt wording
5. **Mechanism remains inferential:** We observe the dissociation but cannot directly measure "active maintenance"

### Future Directions

1. **Cross-model replication:** Test GPT-4, Gemini, Llama to assess generality
2. **Intervention studies:** Test scaffolding on verification-deficit tasks vs. constraint-prompting on generation-deficit tasks
3. **Fine-grained error analysis:** What specific errors occur in each failure mode?
4. **Human comparison:** Do humans show similar task-specific patterns, or is this LLM-specific?
5. **Architectural interventions:** Test whether explicit working memory modules reduce both failure modes

---

## Conclusion

The hypothesis that LLMs show uniform verification deficits is falsified. Instead, we find task-specific dissociations: verification deficits on arithmetic/multi-step tasks (+25%), generation deficits on logic/word-count tasks (-31%), and no difference on others.

We propose that both failure modes reflect a common deficit in **hold-and-check** capacity—the ability to maintain information in a state where it can be continuously compared against ongoing processing. Verification tasks expose holding failures; generation tasks expose checking failures.

This framework:
- Unifies apparently opposite findings under a single architectural hypothesis
- Generates specific predictions for interventions (scaffolding for holding, constraint-prompting for checking)
- Connects to established cognitive science (Baddeley's central executive)
- Provides a more nuanced understanding than "LLMs are bad at reasoning"

The data show that LLMs are not uniformly impaired. They are specifically impaired when tasks require active maintenance—and the direction of impairment depends on whether the task makes holding or checking the bottleneck.

---

## References

Baddeley, A. (2000). The episodic buffer: A new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417-423.

Baddeley, A. D., & Hitch, G. (1974). Working memory. In G. H. Bower (Ed.), *The psychology of learning and motivation* (Vol. 8, pp. 47-89). Academic Press.

Bubeck, S., et al. (2023). Sparks of artificial general intelligence: Early experiments with GPT-4. *arXiv preprint arXiv:2303.12712*.

Danan, H. (2024). The self-state hypothesis: From stakes to verification. *Abstraction-Intelligence Framework*. https://github.com/HillaryDanan/abstraction-intelligence

Dziri, N., et al. (2023). Faith and fate: Limits of transformers on compositionality. *arXiv preprint arXiv:2305.18654*.

Lake, B., & Baroni, M. (2018). Generalization without systematicity. *ICML*.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*, 35.

---

## Supplementary Materials

### S1. Prior Experiments

**Compositional hierarchy experiments:** Initial attempts to predict LLM failures based on formal complexity (3a-3b vs. 3c-3d) yielded inconsistent results:
- Pilot (N=304): d=0.71, p<0.0001
- Extended replication (N=356): d=0.00, p=1.0

This replication failure motivated the shift to the generation-verification framework.

**Experiment 1 (N=60):** Found overall verification deficit (83.3% vs. 96.7%), concentrated in arithmetic (50% vs. 100%). Experiment 2 was designed to replicate and extend.

### S2. Full Task Descriptions

[Task prompts and samples available in supplementary code]

### S3. Raw Data

Results file: `verification_v2_20251222_084038.json`

### S4. Statistical Power

With N=350 per condition:
- 80% power to detect h ≥ 0.21 (small effect)
- The observed h = -0.05 is well below detectable range
- Task-specific effects (h ≈ 0.5-0.9) are adequately powered

---

## Author Contributions

Experimental design, implementation, and analysis conducted through iterative dialogue between human researcher (H.D.) and AI system (Claude). The AI contributed code and analysis while acknowledging its own limitations, including bugs in prior experimental code that were diagnosed and corrected. This collaborative process itself illustrates the hold-and-check deficit: the AI generated experimental designs but required human verification to catch errors.

## Competing Interests

The AI system tested is developed by Anthropic. Findings include both supportive evidence (task-specific deficits) and null results (overall hypothesis falsified), reported transparently.

---

*End of manuscript*

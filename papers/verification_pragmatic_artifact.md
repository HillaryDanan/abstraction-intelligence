# The Verification Deficit in Large Language Models is a Pragmatic Inference Artifact

**Hillary Danan, PhD**

*Correspondence: [email]*

---

## Abstract

Large language models (LLMs) exhibit an apparent "verification deficit"—failing to confirm correct answers they themselves can compute. In Study 1 (N=100), Claude Sonnet 4 achieved 100% accuracy generating 3-digit × 2-digit multiplication answers but only 58% accuracy verifying identical problems, with errors concentrated entirely in false negatives (saying "No" to correct answers). However, Study 2 (N=150) demonstrates this deficit is largely a **pragmatic inference artifact**, not a computational limitation. Simply rephrasing "Is A × B = C?" (10% confirmation) to "Does it equal C?" (96.7% confirmation) nearly eliminates the deficit. Critically, reversing question polarity ("Is A × B ≠ C?") did not improve performance (20%), ruling out simple response bias. These findings indicate that LLMs interpret "Is X = Y?" questions as implying doubt—consistent with Gricean conversational implicature—and default to rejection. The practical implication is significant: verification accuracy in LLMs depends critically on prompt framing, and standard yes/no verification queries systematically underestimate model capability.

**Keywords:** large language models, verification, pragmatic inference, prompt engineering, Gricean implicature

---

## Introduction

A growing body of work documents failures in large language model (LLM) reasoning, including arithmetic errors, logical inconsistencies, and hallucinations (Bubeck et al., 2023; Marcus & Davis, 2020). One proposed explanation invokes architectural limitations—that transformer-based models lack mechanisms for certain computational operations, such as maintaining intermediate results during multi-step verification (Danan, 2024).

However, an alternative possibility deserves consideration: apparent reasoning failures may sometimes reflect pragmatic inference rather than computational incapacity. LLMs are trained on human language, which is saturated with conversational implicature (Grice, 1975). Questions of the form "Is X true?" pragmatically imply that the speaker has reason to doubt X—otherwise, why ask? If LLMs have internalized such pragmatic patterns, they may interpret verification questions as invitations to find errors, biasing responses toward rejection.

We present two studies distinguishing computational limitation from pragmatic artifact in the domain of arithmetic verification.

---

## Results

### Study 1: Replicating the Generation-Verification Dissociation

We presented Claude Sonnet 4 with 100 arithmetic trials: 50 generation tasks ("What is A × B?") and 50 verification tasks ("Is A × B = C?"). Stimuli were 3-digit × 2-digit multiplication problems. Verification trials were evenly split between correct answers (n=25) and off-by-one errors (n=25).

**Primary finding.** Generation accuracy was 100% (50/50), while verification accuracy was 58% (29/50), yielding a 42-percentage-point difference (95% CI: 28.1%–55.9%, Fisher's exact p < .0001, Cohen's h = 1.41).

**Error analysis.** The critical observation emerged from disaggregating verification errors:

| Presented Answer | N | Correct | Accuracy |
|------------------|---|---------|----------|
| Incorrect (off-by-one) | 25 | 25 | 100.0% |
| Correct | 25 | 4 | 16.0% |

When presented with incorrect answers, the model correctly rejected 100% of trials. When presented with correct answers, the model incorrectly rejected 84% of trials. This **confirmation deficit**—the selective failure to affirm correct answers—suggested either (a) a specific computational limitation in self-consistency checking, or (b) a systematic bias toward rejection in verification contexts.

### Study 2: Disambiguating Mechanism via Prompt Variants

To distinguish computational limitation from response bias, we designed five prompt variants testing the same arithmetic problems (all with correct presented answers, N=30 per variant):

| Variant | Prompt Format | Expected Response |
|---------|---------------|-------------------|
| A | "Is A × B = C? Reply Yes or No." | Yes |
| B | "Compute A × B. Does it equal C? Reply Match or No match." | Match |
| C | "First compute A × B. Then compare to C. Reply Equal or Not equal." | Equal |
| D | "Is A × B ≠ C? Reply Yes or No." | No |
| E | "Rate confidence (1-10), then say Correct or Incorrect." | Correct |

**Predictions:**
- If computational limitation: All variants should show similar deficits
- If "No" response bias: Variant D (where correct answer is "No") should succeed
- If pragmatic inference: Variants B and C (neutral framing) should succeed; Variant D should fail

**Results.** Accuracy varied dramatically across prompt variants (Table 1):

| Variant | Accuracy | 95% CI | Description |
|---------|----------|--------|-------------|
| B (neutral) | 96.7% (29/30) | [83.3%, 99.4%] | "Does it equal...?" |
| C (scaffolded) | 90.0% (27/30) | [74.4%, 96.5%] | "First compute, then compare" |
| E (confidence) | 73.3% (22/30) | [55.6%, 85.8%] | Rate confidence first |
| D (reversed) | 20.0% (6/30) | [9.5%, 37.3%] | "Is X ≠ Y?" |
| A (original) | 10.0% (3/30) | [3.5%, 25.6%] | "Is X = Y?" |

*Table 1. Verification accuracy by prompt variant. All variants present correct answers; accuracy reflects successful confirmation.*

**Pairwise comparisons** (McNemar's test, matched pairs):

| Comparison | Δ | p-value | Interpretation |
|------------|---|---------|----------------|
| A vs B | +86.7% | < .0001 | Neutral framing eliminates deficit |
| A vs C | +80.0% | < .0001 | Scaffolding eliminates deficit |
| A vs D | +10.0% | .248 | Polarity reversal does NOT help |
| B vs D | +76.7% | < .0001 | Framing matters more than polarity |
| D vs E | -53.3% | .0002 | Confidence prompt helps vs. reversed |

**Critical finding: Variant D (reversed polarity) failed.**

If the deficit were a simple "No" response bias, reversing the question to "Is A × B ≠ C?" should have succeeded—the correct answer becomes "No" (they are NOT unequal; they ARE equal). Instead, Variant D achieved only 20% accuracy, not significantly better than Variant A (10%, p = .248).

The model said "Yes, they are unequal" when in fact they were equal—the same error pattern as Variant A, just with opposite surface form. This rules out lexical response bias and implicates the **question structure** itself.

**Confidence analysis (Variant E):**

| Outcome | Mean Confidence | N |
|---------|-----------------|---|
| Correct responses | 5.8 | 22 |
| Incorrect responses | 3.9 | 8 |

Lower confidence was associated with incorrect responses, suggesting uncertainty contributes to but does not fully explain the deficit.

---

## Discussion

### Summary

Two studies reveal that the "verification deficit" in LLMs is largely a pragmatic inference artifact:

1. **Study 1** replicated the generation-verification dissociation (100% vs. 58%) and identified a **confirmation deficit**: the model perfectly rejects incorrect answers but systematically fails to confirm correct ones.

2. **Study 2** demonstrated this deficit nearly disappears with neutral prompt framing ("Does it equal?" achieves 96.7%) but persists regardless of response polarity ("Is X ≠ Y?" achieves only 20%).

### The Pragmatic Inference Account

We propose that LLMs interpret "Is X = Y?" questions as carrying a **conversational implicature of doubt** (Grice, 1975). In natural language, asking "Is this correct?" typically implies the speaker suspects it might not be. A cooperative conversational partner—which LLMs are trained to emulate—would attend to this implied doubt and search for potential errors.

This account explains the observed pattern:

1. **Why Variant A fails (10%):** "Is A × B = C?" implies doubt about C, biasing toward rejection.

2. **Why Variant B succeeds (96.7%):** "Does it equal C?" is a neutral verification request without implied doubt. The "Match/No match" response format further removes the Yes/No asymmetry.

3. **Why Variant D fails (20%):** "Is A × B ≠ C?" still implies doubt—now doubt about whether they *are* equal. The model, attending to this doubt, affirms the inequality (incorrectly).

4. **Why Variant C succeeds (90%):** Explicit step-by-step framing ("First compute... then compare...") reframes the task as computation rather than skeptical verification.

### Alternative Accounts Ruled Out

**Simple "No" bias:** If the model simply preferred saying "No," Variant D should have succeeded (correct answer is "No"). It did not (20%).

**Working memory limitation:** If the model couldn't hold computed values during comparison, all verification variants should fail similarly. They did not—Variant B achieved 96.7%.

**Arithmetic difficulty:** Generation accuracy was 100%, demonstrating the model can compute these products. The verification failures are not computational.

### Implications

**For AI Safety and Alignment.** These findings have immediate practical implications. Verification and fact-checking systems using LLMs may systematically underestimate model accuracy if using standard yes/no query formats. A model that says "No, this is incorrect" may be responding to pragmatic cues rather than detecting actual errors.

**For Evaluation Methodology.** Benchmark tasks testing verification or consistency-checking should control for prompt framing effects. Observed "failures" may reflect prompt artifacts rather than capability limitations.

**For Understanding LLM Cognition.** LLMs have deeply internalized pragmatic patterns from training data. This is both a feature (enabling natural conversation) and a bug (introducing systematic biases). Disentangling what models "can do" from "what they do by default" requires careful prompt engineering.

### Relation to Prior Work

Our findings connect to several research threads:

**Prompt sensitivity.** Extensive work documents LLM sensitivity to prompt wording (Reynolds & McDonell, 2021; Webson & Pavlick, 2022; Lu et al., 2022). We extend this to verification contexts, showing that framing can produce 10× differences in accuracy (10% vs. 96.7%).

**Pragmatic reasoning in LLMs.** Recent work has examined whether LLMs engage in Gricean reasoning (Hu et al., 2023; Ruis et al., 2022). Our findings suggest LLMs have internalized pragmatic patterns sufficiently that they affect downstream task performance, even when such patterns are counterproductive.

**Metacognition and calibration.** Prior work documents miscalibration in LLM confidence (Kadavath et al., 2022). Our Variant E results (confidence correlates with accuracy) suggest LLMs have *some* metacognitive signal, but it is insufficient to override pragmatic biases.

### Limitations

1. **Single model.** Results are from Claude Sonnet 4. Generalization to GPT-4, Gemini, and open-source models requires replication.

2. **Single domain.** Arithmetic verification may not generalize to logical, factual, or semantic verification.

3. **Limited sample size.** N=30 per variant in Study 2 provides adequate power for large effects but wide confidence intervals for small effects.

4. **Mechanism remains correlational.** We demonstrate that prompt framing affects accuracy but cannot directly observe the model's internal processing.

### Future Directions

1. **Cross-model replication.** Test whether pragmatic bias is universal to instruction-tuned LLMs or architecture-specific.

2. **Domain extension.** Examine whether the same prompt framing effects appear in logical reasoning, code verification, and factual checking.

3. **Training intervention.** Test whether fine-tuning on verification tasks with balanced framing reduces the bias.

4. **Mechanistic analysis.** For open-weight models, examine attention patterns and activations during verification to identify computational signatures of pragmatic inference.

---

## Methods

### Study 1

**Stimuli.** 100 trials: 50 generation ("What is A × B? Reply with just the number.") and 50 verification ("Is A × B = C? Reply with just 'Yes' or 'No'."). Operands were 3-digit (100-999) × 2-digit (10-99), generated deterministically (seed=42). Verification trials: 25 correct answers, 25 off-by-one errors.

**Model.** Claude Sonnet 4 (claude-sonnet-4-20250514) via Anthropic API, temperature=0, max_tokens=100.

**Scoring.** Generation: correct if extracted number matched true product. Verification: correct if "Yes" when answer was correct, "No" when incorrect.

**Analysis.** Fisher's exact test for proportion comparison; Cohen's h for effect size; Agresti-Caffo confidence intervals.

### Study 2

**Stimuli.** 150 trials: 30 per variant (A, B, C, D, E). All presented answers were correct, isolating confirmation performance. Same operand ranges as Study 1, different seed (43). Matched design: identical number pairs across all variants.

**Variants.** See Table in Results. Each variant tested a different hypothesis about the failure mechanism.

**Model.** Same as Study 1.

**Scoring.** Variant-specific: A/D scored on Yes/No, B on Match/No match, C on Equal/Not equal, E on Correct/Incorrect. Responses parsed via regex; unparseable responses coded as incorrect.

**Analysis.** McNemar's test for matched pairs; Wilson score confidence intervals.

### Data Availability

All code, data, and materials:
- Study 1: https://github.com/HillaryDanan/verification-deficit-replication
- Study 2: https://github.com/HillaryDanan/verification-prompt-variants

---

## References

Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., ... & Zhang, Y. (2023). Sparks of artificial general intelligence: Early experiments with GPT-4. *arXiv preprint arXiv:2303.12712*.

Danan, H. (2024). Hold-and-check: Task-specific dissociations in LLM verification. *Abstraction-Intelligence Working Papers*. https://github.com/HillaryDanan/abstraction-intelligence

Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics* (Vol. 3, pp. 41–58). Academic Press.

Hu, J., Floyd, S., Jouravlev, O., Fedorenko, E., & Gibson, E. (2023). A fine-grained comparison of pragmatic language understanding in humans and language models. *ACL 2023*.

Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., ... & Kaplan, J. (2022). Language models (mostly) know what they know. *arXiv preprint arXiv:2207.05221*.

Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity. *ACL 2022*.

Marcus, G., & Davis, E. (2020). GPT-3, Bloviator: OpenAI's language generator has no idea what it's talking about. *MIT Technology Review*.

Reynolds, L., & McDonell, K. (2021). Prompt programming for large language models: Beyond the few-shot paradigm. *Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems*, 1–7.

Ruis, L., Khan, A., Biderman, S., Hooker, S., Rocktäschel, T., & Grefenstette, E. (2022). Large language models are not zero-shot communicators. *arXiv preprint arXiv:2210.14986*.

Webson, A., & Pavlick, E. (2022). Do prompt-based models really understand the meaning of their prompts? *NAACL 2022*, 2039–2050.

---

## Acknowledgments

[To be added]

## Author Contributions

H.D. conceived the studies, designed experiments, conducted analyses, and wrote the manuscript.

## Competing Interests

The author declares no competing interests.

---

## Extended Data

### Extended Data Table 1: Study 1 Full Results

| Condition | N | Correct | Accuracy | 95% CI |
|-----------|---|---------|----------|--------|
| Generation | 50 | 50 | 100.0% | [92.9%, 100%] |
| Verification (all) | 50 | 29 | 58.0% | [43.2%, 71.8%] |
| Verification (correct presented) | 25 | 4 | 16.0% | [6.4%, 34.7%] |
| Verification (incorrect presented) | 25 | 25 | 100.0% | [86.7%, 100%] |

### Extended Data Table 2: Study 2 Pairwise Comparisons

| Comparison | Variant 1 Acc | Variant 2 Acc | Δ | McNemar χ² | p |
|------------|---------------|---------------|---|------------|---|
| A vs B | 10.0% | 96.7% | -86.7% | 24.04 | <.0001 |
| A vs C | 10.0% | 90.0% | -80.0% | 22.04 | <.0001 |
| A vs D | 10.0% | 20.0% | -10.0% | 1.33 | .248 |
| A vs E | 10.0% | 73.3% | -63.3% | 17.05 | <.0001 |
| B vs C | 96.7% | 90.0% | +6.7% | 0.50 | .480 |
| B vs D | 96.7% | 20.0% | +76.7% | 21.04 | <.0001 |
| B vs E | 96.7% | 73.3% | +23.3% | 4.00 | .046 |
| C vs D | 90.0% | 20.0% | +70.0% | 19.05 | <.0001 |
| C vs E | 90.0% | 73.3% | +16.7% | 1.45 | .228 |
| D vs E | 20.0% | 73.3% | -53.3% | 14.06 | .0002 |

### Extended Data Figure 1: Accuracy by Prompt Variant

```
Variant B (neutral)    |████████████████████████████████████████████████| 96.7%
Variant C (scaffold)   |████████████████████████████████████████████   | 90.0%
Variant E (confidence) |████████████████████████████████████           | 73.3%
Variant D (reversed)   |██████████                                     | 20.0%
Variant A (original)   |█████                                          | 10.0%
                       0%                    50%                      100%
```

---

*Manuscript prepared: December 2024*
*Word count: ~3,200 (main text)*

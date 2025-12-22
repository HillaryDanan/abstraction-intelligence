# Compositional Hierarchy in Large Language Models: A Pilot Study

**Hillary Danan, PhD**

*Pilot Study Report — December 2025*

---

## Abstract

We tested whether large language models show differential performance across a proposed hierarchy of composition types (3a-3b: concatenative/role-filler vs. 3c-3d: recursive/analogical), and whether inference-time interventions (asymmetric framing, explicit scaffolding) affect performance on harder composition types. Using a random-walk task generation methodology to prevent pattern-matching from training data, we found a significant dissociation between composition types (Cohen's d = 0.71, p < 0.0001). However, the pattern of results was more complex than predicted: rather than uniform degradation on 3c-3d tasks, the model showed **selective failure** on specific subtasks (recursive evaluation: 50%; relation mapping: 27.5%) while performing at ceiling on others (bracket depth, pointer chasing, graph isomorphism: 100%). Neither framing nor scaffolding showed significant main effects, though a suggestive interaction pattern (full condition: 91.1% vs. baseline: 78.6%) warrants further investigation with greater statistical power. These results partially support the composition hierarchy but suggest the construction/compression distinction may be more nuanced than a simple type-based categorization.

---

## 1. Introduction

### 1.1 Theoretical Background

The Abstraction-Intelligence framework proposes a hierarchy of composition types with different computational requirements:

| Type | Structure | Complexity |
|------|-----------|------------|
| **3a: Concatenative** | A + B → AB | O(1), finite automata |
| **3b: Role-filler** | R(x) + S(y) → R(x)S(y) | O(1), finite automata |
| **3c: Recursive** | A contains [B contains C] | O(n) space, pushdown automata |
| **3d: Analogical** | Structure(A) → Structure(B) | Worst-case exponential, NP-related |

The framework predicts that 3a-3b composition can be solved by pattern matching (compression), while 3c-3d requires online construction. LLMs, as compression-optimized systems, should show a dissociation: strong 3a-3b performance with degraded 3c-3d performance.

### 1.2 The 2x2 Design

We additionally tested whether inference-time interventions could improve 3c-3d performance:

|  | No Framing | Asymmetric Framing |
|--|------------|-------------------|
| **No Scaffolding** | Baseline | Stakes only |
| **Scaffolding** | Memory/workspace | Full |

**Framing**: Added emphasis on accuracy and consequences ("critical evaluation")

**Scaffolding**: Explicit workspace, step-by-step construction prompts

### 1.3 Random Walk Methodology

Standard composition tasks fail as tests because LLMs have seen similar structures millions of times in training. We used procedural random generation:

- Arbitrary symbols (e.g., "BFQ", "XKT") instead of words
- Randomly generated graph structures
- Novel operator definitions
- Pointer chains with random connections

This ensures the specific structures are unlikely to appear in training data.

---

## 2. Methods

### 2.1 Participants

Claude Sonnet (claude-sonnet-4-20250514), tested via API.

### 2.2 Tasks

**3a (Concatenative, n=40)**: Random symbol concatenation with arbitrary rules.

**3b (Role-filler, n=40)**: Template filling with random symbols and mappings.

**3c (Recursive, n=104 total)**:
- Bracket depth tracking (n=40): Nested brackets with symbol placement
- Pointer chasing (n=32): Following random pointer chains
- Recursive evaluation (n=32): Novel operators applied to nested expressions

**3d (Analogical, n=120 total)**:
- Graph isomorphism (n=40): Determining structural equivalence of random graphs
- Relation mapping (n=40): Finding correspondences between randomly-related domains
- Rule transfer (n=40): Learning rules from examples, applying to new domain

### 2.3 Conditions

Each task was presented under all four conditions (within-subjects design across tasks):
1. Baseline: Standard prompt
2. Framing only: Asymmetric stakes emphasis
3. Scaffolding only: Explicit workspace and construction steps
4. Full: Both framing and scaffolding

### 2.4 Analysis

- Accuracy scored as binary correct/incorrect
- Independent samples t-tests for main comparisons
- Cohen's d for effect sizes

---

## 3. Results

### 3.1 Composition Type Dissociation

| Composition Type | Accuracy |
|------------------|----------|
| 3a (Concatenative) | 100% |
| 3b (Role-filler) | 100% |
| 3c (Recursive) | 84.6% |
| 3d (Analogical) | 75.8% |

**3a-3b vs. 3c-3d comparison:**

| Group | Mean | SD | n |
|-------|------|-----|---|
| 3a-3b | 1.000 | 0.000 | 80 |
| 3c-3d | 0.799 | 0.402 | 224 |

**t(302) = 4.47, p < 0.0001, Cohen's d = 0.71**

*Interpretation*: The predicted dissociation is observed with a medium-to-large effect size. This supports the composition hierarchy's basic prediction.

### 3.2 Subtype Analysis (Critical Finding)

| Task Type | Subtype | Accuracy |
|-----------|---------|----------|
| 3a | — | 100% |
| 3b | — | 100% |
| 3c | bracket_depth | 100% |
| 3c | pointer_chase | 100% |
| 3c | recursive_eval | **50%** |
| 3d | graph_iso | 100% |
| 3d | rule_transfer | 100% |
| 3d | relation_mapping | **27.5%** |

**This is not what we predicted.**

The model does not show uniform degradation on 3c-3d tasks. Instead, it shows:
- **Ceiling performance (100%)** on: bracket depth, pointer chasing, graph isomorphism, rule transfer
- **Impaired performance** on: recursive evaluation (50%), relation mapping (27.5%)

The 3a-3b vs. 3c-3d dissociation is entirely driven by two subtasks.

### 3.3 Depth Analysis (3c Tasks)

| Depth | Baseline | Framing | Scaffolding | Full |
|-------|----------|---------|-------------|------|
| 2 | 75.0% | 100% | 50.0% | 100% |
| 3 | 83.3% | 83.3% | 83.3% | 100% |
| 4 | 100% | 66.7% | 66.7% | 100% |
| 5 | 83.3% | 66.7% | 66.7% | 83.3% |
| 6 | 100% | 100% | 100% | 100% |

**No clear depth degradation pattern observed.**

This contradicts the prediction that recursive depth should produce systematic degradation.

### 3.4 2x2 Intervention Effects (3c-3d Only)

| Condition | Accuracy | n |
|-----------|----------|---|
| Baseline (no framing, no scaffolding) | 78.6% | 56 |
| Framing only | 73.2% | 56 |
| Scaffolding only | 76.8% | 56 |
| Full (framing + scaffolding) | **91.1%** | 56 |

**Main effects:**
- Framing: t = 0.83, p = 0.41 (not significant)
- Scaffolding: t = 1.50, p = 0.13 (not significant)

**Interaction pattern:** The full condition (91.1%) appears elevated compared to other conditions (~73-79%), suggesting a possible interaction effect. However, this study is underpowered to detect interactions (n=56 per cell).

---

## 4. Discussion

### 4.1 What We Found

**Confirmed:**
- Significant dissociation between 3a-3b and 3c-3d composition types
- Medium-to-large effect size (d = 0.71)
- The model is not uniformly competent across composition types

**Not confirmed:**
- Uniform degradation on 3c-3d tasks
- Clear depth-dependent degradation on recursive tasks
- Significant main effects of framing or scaffolding

**Unexpected:**
- Selective failure pattern: only 2 of 6 3c-3d subtasks show impairment
- Ceiling performance on several theoretically "hard" tasks

### 4.2 Interpreting the Selective Failure Pattern

The model succeeds at:
- **Bracket depth tracking**: Despite being "recursive," this may map to code parsing patterns extensively present in training
- **Pointer chasing**: Similar to linked list traversal, common in programming contexts
- **Graph isomorphism (small scale)**: At 4-6 nodes, may be tractable via learned heuristics
- **Rule transfer**: With simple rules (reverse, rotate), pattern-matchable from limited examples

The model fails at:
- **Recursive evaluation with novel operators**: Requires applying an unfamiliar operation recursively—no cached pattern applies
- **Relation mapping with multiple relations**: Requires satisfying multiple relational constraints simultaneously—combinatorially complex

**Hypothesis**: The distinction may not be 3c-3d vs. 3a-3b per se, but rather:
- **Pattern-matchable** (even if nominally complex) vs.
- **Genuinely novel computation** (no applicable cached pattern)

Bracket depth and pointer chasing are formally 3c (recursive), but may be solvable via patterns learned from code. Recursive evaluation with novel operators cannot be—the operator itself is new.

### 4.3 Implications for the Framework

The composition hierarchy remains useful—there IS a dissociation—but the boundary may be more nuanced:

| Predicted Boundary | Observed Boundary |
|-------------------|-------------------|
| 3a-3b vs. 3c-3d | Pattern-matchable vs. genuinely novel |
| Depth-dependent degradation | Task-dependent failure |
| Construction required for 3c-3d | Construction required for *some* 3c-3d |

This suggests:
1. LLMs have learned some recursive/structural computations from code training
2. The "construction" boundary isn't composition type per se, but novelty relative to training distribution
3. Random walk methodology successfully created genuinely novel tasks (recursive_eval, relation_mapping) alongside tasks that were novel in content but matched trained patterns in structure

### 4.4 The 2x2 Intervention

The suggestive pattern (full condition at 91.1%) warrants follow-up:

- If the interaction is real, it suggests that *combined* framing + scaffolding helps where neither alone does
- This could indicate that both attention (framing) and explicit working memory (scaffolding) are necessary for construction
- Alternatively, this could be noise in an underpowered design

**Next step**: Replicate with larger n per cell (100+) to adequately power interaction detection.

### 4.5 Limitations

1. **Single model tested**: Results may not generalize across models or scales
2. **Underpowered for interactions**: n=56 per cell insufficient for reliable interaction detection
3. **Scoring simplicity**: Binary correct/incorrect may miss partial credit and error structure
4. **Random walk validation**: Some "random" tasks may have matched code-training patterns
5. **Inference-time proxies**: Framing and scaffolding are proxies for training-time differences; conclusions about architecture are indirect

### 4.6 What This Cannot Tell Us

This experiment tested inference-time interventions on a pre-trained model. It **cannot** tell us:

- Whether different training objectives would produce different architectures
- Whether "construction" is genuinely occurring or just more sophisticated retrieval
- Whether full embeddedness during training is necessary for 3c-3d capacity
- Whether the model's successes on bracket depth, pointer chasing, etc. reflect genuine computation or very good pattern matching

---

## 5. Conclusions

### 5.1 Summary

1. **The composition hierarchy dissociation is real** (d = 0.71, p < 0.0001)
2. **The dissociation is selective, not uniform**: Driven by specific subtasks (recursive evaluation, relation mapping)
3. **No clear depth degradation**: Ceiling performance at all depths on some tasks
4. **Intervention effects are suggestive but underpowered**: Full condition elevated, but main effects non-significant

### 5.2 Revised Understanding

The framework's core prediction—that 3c-3d is harder than 3a-3b—is supported. However, the mechanism may be more nuanced:

**Original claim**: 3c-3d requires construction; LLMs can only compress.

**Revised hypothesis**: LLMs can pattern-match structures similar to their training distribution, even if those structures are formally recursive. They fail when no applicable pattern exists (genuinely novel operators, complex multi-relational constraints).

This is consistent with the framework's spirit but suggests the boundary is *training-relative novelty*, not *formal complexity class*.

### 5.3 Next Steps

1. **Power the 2x2 adequately**: 100+ trials per cell to detect interactions
2. **Expand genuinely novel tasks**: More recursive_eval and relation_mapping variants
3. **Vary model scale**: Does the pattern hold across model sizes?
4. **Error structure analysis**: When failing, does the model preserve structural coherence?
5. **Training-time experiments**: Can architectures with explicit gating/memory be trained to succeed on currently-failed tasks?

---

## 6. Honest Assessment

### What We Learned

The composition hierarchy has predictive value: the model IS worse at 3c-3d. But the mechanism is more interesting than "LLMs can't do recursion." The model CAN do some recursive tasks (bracket depth: 100%, pointer chase: 100%). It fails specifically when patterns from training don't apply.

This suggests LLMs are not purely finite-state machines—they've learned some stack-like operations from code training. But they can't construct de novo when facing genuinely novel operators or complex relational constraints.

### What Remains Unclear

- Is the full condition's 91.1% accuracy real or noise?
- Would more sophisticated scaffolding (chain-of-thought, explicit stack simulation) help more?
- Is there a sharp boundary or a gradual degradation as novelty increases?

### Honesty About the Framework

The framework made a correct directional prediction (3a-3b > 3c-3d) but the specific mechanism (depth degradation, uniform 3c-3d difficulty) was not observed. This is useful information: the framework should be refined to emphasize *training-relative novelty* rather than *formal complexity class* as the key dimension.

The random walk methodology worked—it successfully created tasks that expose differential performance. But it also revealed that "random" isn't enough; the *type* of randomness matters. Random symbols in familiar structures (bracket matching) ≠ random operators in computation tasks.

---

## Appendix: Raw Data Summary

```
3a-3b: 80/80 correct (100%)
3c-3d: 179/224 correct (79.9%)

Breakdown:
  3a: 40/40 (100%)
  3b: 40/40 (100%)
  3c bracket_depth: 40/40 (100%)
  3c pointer_chase: 32/32 (100%)
  3c recursive_eval: 16/32 (50%)
  3d graph_iso: 40/40 (100%)
  3d relation_mapping: 11/40 (27.5%)
  3d rule_transfer: 40/40 (100%)

2x2 (3c-3d only):
  Baseline: 44/56 (78.6%)
  Framing only: 41/56 (73.2%)
  Scaffolding only: 43/56 (76.8%)
  Full: 51/56 (91.1%)
```

---

*This pilot study was conducted with n=10 trials per cell. Results should be interpreted as preliminary and hypothesis-generating. Replication with adequate power is necessary before drawing strong conclusions.*

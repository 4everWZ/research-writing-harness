# Usage Examples

## Initialize only

```text
Use research-writing-harness.
Create docs/fire_mamba_ir as a flat paper workspace.
Do not search literature.
Do not write paper content.
```

## Literature search only

```text
Use research-writing-harness literature mode.
Search high-quality deep learning papers related to frequency-domain attention and wavelet-based downsampling.
Update only paper_index.md, references.bib, and reading notes.
Do not write introduction or related work.
Rank sources by evidence quality, not venue alone.
```

## Idea refinement

```text
Use research-writing-harness idea refinement mode.
Current idea: [paste idea].
Use indexed papers to suggest refinements.
Do not modify code.
Do not optimize for novelty alone.
Write only to idea_log.md.
```

## Repo to method section

```text
Use research-writing-harness repo-to-paper mode.
Convert the implemented module into method.md.
Inspect code/config first.
Do not invent tensor shapes.
Do not write results.
Do not claim novelty.
Update claims.md for nontrivial claims.
```

## Results placeholders only

```text
Use research-writing-harness.
Create results_tables.md placeholders for my main comparison and ablation study.
Do not fill values.
Use TODO for all missing metrics.
```

## Citation audit

```text
Use research-writing-harness citation-audit mode.
Check whether related_work.md citations support the claims.
Update claims.md with unsupported or partially supported claims.
Do not rewrite the whole section unless necessary.
```

## Paper handoff

```text
Use research-writing-harness.
Prepare paper handoff because the method direction changed.
Classify this as Tier A/B/C and update handoff.md only if needed.
```

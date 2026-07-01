# Round 1 Editorial Synthesis

Decision: **Minor revision**
Manuscript: draft v1
Reviewers: methodology, domain/rubric and devil's advocate

## Editorial assessment

The report is coherent, reproducible and closely aligned with the assignment
rubric. No P0 issue was identified. One shared P1 issue requires correction:
the description of the test set overstates single-use isolation and does not
fully explain that notebook code uses the sorted test table to choose the model
for downstream diagnostics. This does not invalidate the selected HGB result
because the family and tuned configuration were already favoured by
cross-validation, but the chronology and limitation must be explicit.

## Revision roadmap

| ID | Priority | Source | Required revision | Verification |
|---|---|---|---|---|
| R1 | P1 | M1, A1 | Replace “used once/untouched” language with an exact account of the reserved test set, prespecified final comparisons and test-ranked diagnostic helper. | Methods and Validation preserve CV-led selection and disclose repeated test reporting. |
| R2 | P2 | M2 | Add Matplotlib and seaborn versions to Methods. | Package versions match experiment provenance. |
| R3 | P2 | M3 | Add a standalone note to Table 7. | Abbreviations, bolding and unavailable cells are explained. |
| R4 | P2 | D1 | Add a standalone note to Related Works Table 2. | Abbreviations and non-comparability are explained. |
| R5 | P2 | D2, D3, A2-A4 | Preserve current provenance, perfect-cleanliness, causal, same-dataset and disclosure warnings. | Re-review confirms no warning was diluted. |
| R6 | P3 | Editorial | Remove Markdown trailing whitespace and excess EOF blank lines. | `git diff --check` passes. |

The revision is bounded and does not require new experiments, new sources or a
change to the research question or conclusion.

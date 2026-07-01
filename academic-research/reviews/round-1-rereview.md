# Round 1 Re-Review

Mode: `re-review`

Revised manuscript: draft v2, as recorded in
`academic-research/manuscript-manifest.yaml`

Decision: **Accept as a verified modular draft with warnings**

## Finding verification

| ID | Original requirement | Verification evidence | Result |
|---|---|---|---|
| R1 | Correct single-use test language and explain selection chronology | Methods now enumerates the prespecified reserved-test uses and rejects a strict single-look description. Validation states that CV favoured tuned HGB before the test-ranked helper selected the diagnostic model, and notes the external-evaluation limitation. | Resolved |
| R2 | Name plotting package versions | Methods reports Matplotlib 3.10.9 and seaborn 0.13.2, matching experiment provenance. | Resolved |
| R3 | Make Table 7 standalone | The note defines CV, HGB, MAE, RMSE and SD and explains bolding and unavailable tuned cells. | Resolved |
| R4 | Add the Related Works table boundary | The Table 2 note defines AI, GenAI and VLE and prohibits direct numerical benchmarking against GPA-change regression. | Resolved |
| R5 | Preserve evidence warnings | Dataset provenance, perfect cleanliness, causal boundaries, structured-review label, unavailable same-dataset comparison and disclosure placeholders remain explicit. | Resolved |
| R6 | Remove whitespace defects | The trailing-whitespace scan and `git diff --check` report no content errors. | Resolved |

## Residual assessment

No P0 or P1 finding remains. No additional substantive revision round is
required. Three warnings remain by design:

1. Dataset collection, consent, geography and real-versus-synthetic status are
   undocumented.
2. The literature search encountered OpenAlex, Semantic Scholar and Kaggle API
   degradation and is not claimed as a full PRISMA review.
3. Names of direct helpers and institution-required AI-disclosure wording
   require author confirmation during final Typst assembly.

These warnings define the evidence boundary but do not invalidate the modular
draft.

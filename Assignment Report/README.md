# Modular AML Assignment Report

This directory contains the reviewable Markdown draft for later Typst assembly.
Notebook 05 is the sole reported implementation. Typst conversion, cover pages,
pagination and rendered PDF inspection are intentionally deferred.

## Merge order and status

| Order | File | Words | Status |
|---:|---|---:|---|
| 1 | `sections/00_title_and_abstract.md` | 296 | Pre-review audit passed; full review pending |
| 2 | `sections/01_introduction_aim_objectives.md` | 758 | Pre-review audit passed; full review pending |
| 3 | `sections/02_related_works.md` | 1,829 | Pre-review audit passed; full review pending |
| 4 | `sections/03_methods.md` | 697 | Pre-review audit passed; full review pending |
| 5 | `sections/04_dataset_preparation.md` | 627 | Pre-review audit passed; full review pending |
| 6 | `sections/05_model_implementation.md` | 926 | Pre-review audit passed; full review pending |
| 7 | `sections/06_model_validation.md` | 648 | Pre-review audit passed; full review pending |
| 8 | `sections/07_analysis_and_recommendations.md` | 1,071 | Pre-review audit passed; full review pending |
| 9 | `sections/08_conclusion.md` | 373 | Pre-review audit passed; full review pending |
| 10 | `sections/09_references.md` | Excluded | Citation-reference audit passed; full review pending |
| 11 | `sections/10_acknowledgements.md` | 69 | Drafted with explicit placeholders |

Total counted words excluding references: **7,294**. Counts use a
Unicode-aware word-token expression and include headings and table text.

## Canonical metadata and assets

- `references.bib` is the canonical bibliographic metadata file.
- `sections/09_references.md` is the reviewable APA 7 presentation list.
- `assets/fig01_gpa_change_eda.png` presents target and descriptive EDA.
- `assets/fig02_model_test_rmse_and_actual_vs_predicted.png` presents model
  RMSE and actual-versus-predicted values.
- `assets/fig03_residual_diagnostics.png` presents residual diagnostics.
- `assets/fig04_permutation_importance.png` presents feature importance.

The figures were exported from an unchanged deterministic rerun of
`Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb`. Raw
metrics and eight result tables matched the saved notebook exactly.

## Evidence and writing controls

- British English and APA 7 author-date citations.
- Predictive association only; no causal or population-level inference.
- Cross-validation provides model-selection evidence; the test set provides
  final confirmation.
- Tables and figures have standalone captions and are discussed in prose.
- Phrasebank candidates are recorded in
  `../academic-research/phrasebank-usage-log.md` and are not evidence.

## Unresolved placeholders and later work

1. Confirm names and contributions of any people who provided direct
   assistance.
2. Insert the institution-required AI-assistance disclosure wording.
3. Merge the Markdown modules into the final Typst template.
4. Apply APU cover, declaration, pagination, font and spacing requirements.
5. Render and inspect the final PDF before claiming `submission-ready`.

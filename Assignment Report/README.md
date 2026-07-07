# Modular AML Assignment Report

This directory contains the reviewable Markdown source, modular Typst assembly,
and rendered PDF for the assignment report. Notebook 05 is the sole reported
implementation.

The current rendered deliverable is `AML_Assignment_Report.pdf`. It includes
the APU assignment cover, declaration, title page, abstract, table of contents,
lists of figures and tables, the complete report body, references and
acknowledgements.

## Merge order and status

| Order | File | Words | Status |
|---:|---|---:|---|
| 1 | `sections/00_title_and_abstract.md` | 296 | Verified modular draft |
| 2 | `sections/01_introduction_aim_objectives.md` | 758 | Verified modular draft |
| 3 | `sections/02_related_works.md` | 1,861 | Verified modular draft |
| 4 | `sections/03_methods.md` | 726 | Verified modular draft |
| 5 | `sections/04_dataset_preparation.md` | 627 | Verified modular draft |
| 6 | `sections/05_model_implementation.md` | 926 | Verified modular draft |
| 7 | `sections/06_model_validation.md` | 676 | Verified modular draft |
| 8 | `sections/07_analysis_and_recommendations.md` | 1,071 | Verified modular draft |
| 9 | `sections/08_conclusion.md` | 373 | Verified modular draft |
| 10 | `sections/09_references.md` | Excluded | Verified and reconciled |
| 11 | `sections/10_acknowledgements.md` | 80 | Verified; limited to documented contributors and tools |

The counted total is **7,394 words excluding references**. The
acknowledgements were revised to remove speculative placeholders and add the
documented AI-assistance disclosure.

## Typst assembly

| Path | Purpose |
|---|---|
| `typst/main.typ` | Canonical merge entry point and pagination control |
| `typst/metadata.typ` | Student and assignment cover metadata |
| `typst/template.typ` | A4 layout, Times New Roman typography, 1.5 line spacing, headers, tables and APA hanging indents |
| `typst/front-matter/` | Cover, declaration, title and abstract modules |
| `typst/sections/` | Ordered Typst body modules generated from the reviewed Markdown sections |
| `typst/back-matter/` | References and acknowledgements modules |
| `AML_Assignment_Report.pdf` | Compiled and visually inspected report |

Compile from the workspace root with:

```powershell
typst compile --root "Assignment Report" `
  "Assignment Report\typst\main.typ" `
  "Assignment Report\AML_Assignment_Report.pdf"
```

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

## Remaining student completion fields

Before submission, replace the three explicit values in
`typst/metadata.typ`:

1. `student-name`
2. `student-id`
3. `declaration-date`

The assembly is verified, but it remains `not submission-ready` until those
fields are completed and the student performs the final submission review.

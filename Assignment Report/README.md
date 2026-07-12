# Modular AML Assignment Report

This directory contains the reviewable Markdown source, modular Typst assembly,
and rendered PDF for the assignment report. Notebook 06 is the sole reported
implementation; notebook 05 is its byte-preserved modelling baseline.

The current rendered deliverable is `AML_Assignment_Report.pdf`. It includes
the APU assignment cover, declaration, title page, abstract, table of contents,
lists of figures and tables, the complete report body, references and
acknowledgements.

## Merge order and status

| Order | File | Words | Status |
|---:|---|---:|---|
| 1 | `sections/00_title_and_abstract.md` | 303 | Verified revision-round-2 draft |
| 2 | `sections/01_introduction_aim_objectives.md` | 758 | Verified modular draft |
| 3 | `sections/02_related_works.md` | 2,002 | Verified revision-round-2 draft |
| 4 | `sections/03_methods.md` | 771 | Verified revision-round-2 draft |
| 5 | `sections/04_dataset_preparation.md` | 763 | Verified revision-round-2 draft |
| 6 | `sections/05_model_implementation.md` | 996 | Verified revision-round-2 draft |
| 7 | `sections/06_model_validation.md` | 773 | Verified revision-round-2 draft |
| 8 | `sections/07_analysis_and_recommendations.md` | 1,148 | Verified revision-round-2 draft |
| 9 | `sections/08_conclusion.md` | 406 | Verified revision-round-2 draft |
| 10 | `sections/09_references.md` | Excluded | Verified and reconciled |
| 11 | `sections/10_acknowledgements.md` | 80 | Verified; limited to documented contributors and tools |

The counted total is **8,000 words excluding references**. The
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
- Figures 1--6 present data quality, full-field distributions, correlations,
  target imbalance and focused EDA.
- Figures 7--10 present model comparison, residuals, direction-specific error
  and permutation importance.

Figures were exported from executed
`Final Assignment/notebooks/06_comprehensive_gpa_change_regression.ipynb`.
Core metrics match byte-preserved notebook 05 exactly.

`AML_Assignment_Report_Merged.md` is generated from canonical section files for
single-file review. Rebuild it with
`academic-research/build_merged_report.py`; it does not replace the modules.

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

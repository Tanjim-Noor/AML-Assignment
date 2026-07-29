# AML Submission Documents

The current submission candidates are:

- `AML_Assignment_Report_Final.md`: canonical reviewable source.
- `AML_Assignment_Report_Final_Readable_Figures.docx`: formatted submission
  document with readability-first figure plates.

They supersede `AML_Assignment_Report_Submission_Source.md` and the earlier
Word revisions. The older DOCX files are retained under
`_backup/docx-2026-07-29/` as recoverable revision inputs; only the current
submission DOCX remains in the main report folder. The modular Markdown, Typst
and PDF files remain historical assembly artefacts.

Notebook 06 is the comprehensive implementation supporting the final
documents. Notebook 05 remains the byte-preserved modelling baseline.

## Final-document status

The final documents were rewritten around the prediction problem rather than
the production process. Visible filenames, notebook references, raw variable
identifiers and assessment-oriented commentary were removed from the main
narrative. The revised structure explains:

- the problem, research question, aim and measurable objectives;
- why continuous GPA change is treated as a regression target;
- what each benchmark, linear, ensemble and neural model does;
- why randomised hyperparameter search is appropriate;
- why the best neural result did not justify replacing gradient boosting;
- how cross-validation, the reserved test set and deterministic bootstrap
  intervals support model selection and uncertainty assessment; and
- where provenance, outcome-direction error and non-causal interpretation
  limit use of the findings.

The DOCX uses A4 pages, Times New Roman throughout, black headings, 1.5-line
body spacing, accessible table headers and alternative text for figures. It
uses equal one-inch margins, inline centred figures and no external-file
relationships or automatic field-update request. Dense exploratory and
validation graphics use dedicated, full-width plates with reader-facing panel
titles and alternative text. It was rendered to 52 pages and visually
inspected page by page. The main sections occupy 45 numbered
pages: Introduction 1--3, Related Works 4--8, Methods 9--12, Dataset
Preparation 13--23, Model Implementation 24--28, Model Validation 29--36,
Analysis and Recommendations 37--41, Conclusion 41--42, References 43--45
and Acknowledgements 45.

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
  target imbalance and focused EDA. Figures 2 and 3 are split into five
  readable plates while retaining their main numbers.
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

## Submission boundary

The final pair is technically verified and aligned to the marking scheme.
Distinction remains a marker judgement, and the student should still perform
the final authorship, declaration and upload checks before submitting.

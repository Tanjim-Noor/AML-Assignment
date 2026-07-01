# Pre-Review Integrity Audit: Draft v1

Date: 2026-07-01  
Manuscript manifest: `academic-research/manuscript-manifest.yaml`
(`ce2d8065fbf5006dfc9adf9745dec531322ae829dcc66bb78cb7419ef5c00388`)  
Overall result: **PASS-WITH-WARNINGS**

| Check | Result | Evidence and residual warning |
|---|---|---|
| Required section set | PASS | Eleven ordered Markdown modules, canonical BibTeX and four figure assets exist. |
| Word budget | PASS | Deterministic count is 7,294 words excluding references; every prose module is within its approved range. |
| Quantitative claims | PASS | Headline metrics, feature-set results, residual tolerances and importances were checked against notebook 05 and its exact deterministic rerun. |
| Data and methods consistency | PASS | Dataset size, source-column count, feature groups, exclusions, split, folds, preprocessing, model settings and tuning space match the notebook. |
| Citation-reference reconciliation | PASS | Seventeen author-year families appear in prose, the APA list and the 17-record BibTeX file; all 15 scholarly core sources retain verified DOI metadata. |
| Source-to-claim support | PASS-WITH-WARNINGS | Claims follow the approved source matrix. Some publisher verification was limited to official abstract/results material, and no same-dataset benchmark was accessible. |
| Causal and population boundary | PASS | Causal-language search was manually reviewed; every occurrence either describes prior study design or explicitly rejects causal inference from this dataset. |
| Tables and figures | PASS | Tables are numbered 1-8, figures 1-4, links resolve, captions are standalone, and every visual is discussed in surrounding prose. |
| Phrasebank use | PASS | A small set of adapted rhetorical phrases is logged; no phrase supplies evidence or changes claim strength. |
| Originality and quotation | PASS-WITH-WARNINGS | The draft contains no direct quotations or copied source passages. No external similarity service was used; such tools would be weak screening evidence rather than proof. |
| Ethics and provenance | PASS-WITH-WARNINGS | The dataset is public and CC0, but collection, consent, ethics, geography and real-versus-synthetic status are undocumented and remain prominent limitations. |
| Disclosure and acknowledgements | PASS-WITH-WARNINGS | Assistance names and institution-required AI-disclosure wording remain explicit placeholders for final assembly. |
| Final formatting | PASS-WITH-WARNINGS | Markdown is reviewable; Typst assembly, APU administrative pages and rendered PDF inspection are outside this phase. |

No P0 critical finding was identified. The warnings do not invalidate the
modular draft, but they prevent a `submission-ready` status.

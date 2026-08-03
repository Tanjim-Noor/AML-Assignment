# Rubric–Evidence Matrix

| Criterion | Weight | Distinction requirement | Planned report location | Primary evidence | Acceptance check |
|---|---:|---|---|---|---|
| Title and Abstract | 5% | Suitable title and complete, coherent abstract | Final document: title and Abstract | Executed results and final synthesis | Self-contained problem, design, model families, neural comparison, metrics, uncertainty, principal finding and limitation |
| Introduction, Aim and Objectives | 10% | Outstanding problem formulation and aligned objectives | Final document: Introduction, Aim and Objectives | Brief, marking scheme and predictive design | Accessible problem, exact research question, one aim, six measurable objectives and bounded non-causal scope |
| Related Works | 25% | Wide and deep systematic review using multiple searches and databases | Final document: Related Works, pp. 4–8 | Approved multi-database corpus plus primary model papers | Reproducible search method, thematic synthesis, critical comparison, research gap and architecture basis within the six-page maximum |
| Methods | 5% | Highly appropriate methods with clear justification | Final document: Methods, pp. 9–12 | Executed notebook and methodological sources | Regression choice, data split, fold-local preprocessing, model progression, metrics, random search and bootstrap justified |
| Dataset Preparation | 5% | Complete and fully reported preparation | Final document: Dataset Preparation, pp. 13–23 | Executed schema, integrity and EDA outputs | Full data-quality account, no manufactured defects, reader-facing variables and explicit leakage controls |
| Model Implementation | 20% | Appropriate algorithms, built models and clearly explained outputs | Final document: Model Implementation, pp. 24–28 | Executed classical and neural experiments | Mean baseline, Linear, Ridge, random forest, histogram gradient boosting, MLP, FT-Transformer and TabM explained; tuning space and selected configuration justified |
| Model Validation | 10% | Appropriate validation with significant interpretation | Final document: Model Validation, pp. 29–36 | Five-fold CV, reserved test metrics and 2,000 bootstrap resamples | Selection chronology, fold variability, test performance, 95% intervals, residuals, direction errors and neural material-win gate |
| Analysis and Recommendations | 15% | Outstanding critical analysis, discussion and recommendations | Final document: Analysis and Recommendations, pp. 37–41 | Executed results and approved literature | Direct answer, literature comparison, model trade-offs, uncertainty, provenance limits, unequal direction error and proportionate recommendations |
| Interactive Prediction Demonstration | Supplementary | Reader-facing model showcase with clear evidence boundaries | Final document: Interactive Prediction Demonstration, pp. 42–45 | Executed matched-pipeline demonstration and live screenshots | Three modes, leakage-safe inputs, reproducible worked example, full-page landscape figures, accessible output and explicit non-causal warning |
| Conclusion | 5% | Addresses all objectives with strong implications | Final document: Conclusion, p. 46 | Completed final synthesis | Objective-by-objective resolution, implications, limitations and defensible future work |
| References | Mandatory | Relevant publications, dataset and APA consistency | Final document: References, pp. 47–49; `references.bib` | Approved corpus and primary architecture papers | In-text citations resolve and APA presentation is consistent |
| Acknowledgements | Mandatory | Factual acknowledgement of assistance and resources | Final document: Acknowledgements, p. 49 | Documented resources and assistance | Concise factual disclosure with no speculative contributor claims |

## Cross-cutting distinction checks

1. At least three models are compared under one validation protocol.
2. Hyperparameter tuning occurs inside development data only.
3. Cross-validation, not the test set, drives model selection.
4. Every figure and table is discussed in surrounding prose.
5. Results are compared critically with prior work rather than listed.
6. Dataset provenance and perfect cleanliness are treated as central limitations.
7. Prediction and feature importance are never converted into causal claims.
8. Neural models are compared empirically and retained only if improvement clears a predefined materiality threshold.
9. Final test estimates include deterministic bootstrap uncertainty and a paired model-comparison interval.
10. The DOCX passes page-by-page visual, font, accessibility and main-body artefact scans.
11. The interactive comparison changes only the supplied feature set and never labels the resulting prediction difference as a causal effect.

# Rubric–Evidence Matrix

| Criterion | Weight | Distinction requirement | Planned report location | Primary evidence | Acceptance check |
|---|---:|---|---|---|---|
| Title and Abstract | 5% | Suitable title and complete, coherent abstract | `00_title_and_abstract.md` | All final section findings | One paragraph; problem, context, preprocessing, models, metrics, findings and limitation |
| Introduction, Aim and Objectives | 10% | Outstanding problem formulation and aligned objectives | `01_introduction_aim_objectives.md` | Assignment brief; notebook problem statement | Accessible problem, exact research question, one aim, six measurable objectives and bounded scope |
| Related Works | 25% | Wide and deep systematic review using multiple searches and databases | `02_related_works.md` | Approved external corpus | At least three databases, reproducible logs, 12–15 core sources, thematic synthesis and comparison table |
| Methods | 5% | Highly appropriate methods with clear justification | `03_methods.md` | Notebook cells 0–15 | Design, data, target, split, fold-local preprocessing, models, metrics and tuning justified |
| Dataset Preparation | 5% | Complete and fully reported preparation | `04_dataset_preparation.md` | Notebook cells 3–9; dataset README | Complete schema/integrity/EDA account; no invented missingness; explicit leakage controls |
| Model Implementation | 20% | Appropriate algorithms, built models and clearly explained outputs | `05_model_implementation.md` | Notebook cells 11–17 | Baseline plus four regressors, pipeline, parameters, tuning space and selected configuration |
| Model Validation | 10% | Appropriate validation with significant interpretation | `06_model_validation.md` | Notebook cells 11–23 | CV means/variability, untouched test metrics, residuals, error tolerances and selection hierarchy |
| Analysis and Recommendations | 15% | Outstanding critical analysis, discussion and recommendations | `07_analysis_and_recommendations.md` | Notebook results; approved literature corpus | Answer research question, compare literature, explain anomalies, delimit inference and give responsible recommendations |
| Conclusion | 5% | Addresses all objectives with strong implications | `08_conclusion.md` | Completed report | Objective-by-objective evaluation, self-assessment, implications, limitations and future work |
| References | Mandatory | Relevant publications, dataset and APA consistency | `09_references.md`; `references.bib` | Approved corpus | Every in-text citation resolves; every listed source is intentionally cited |
| Acknowledgements | Mandatory | Factual acknowledgement of assistance and resources | `10_acknowledgements.md` | Author-confirmed facts | No invented names or assistance; unresolved disclosure wording remains explicit |

## Cross-cutting distinction checks

1. At least three models are compared under one validation protocol.
2. Hyperparameter tuning occurs inside development data only.
3. Cross-validation, not the test set, drives model selection.
4. Every figure and table is discussed in surrounding prose.
5. Results are compared critically with prior work rather than listed.
6. Dataset provenance and perfect cleanliness are treated as central limitations.
7. Prediction and feature importance are never converted into causal claims.

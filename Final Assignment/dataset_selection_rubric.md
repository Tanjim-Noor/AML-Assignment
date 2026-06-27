# Dataset Selection Rubric and Final Dataset Decision

Last updated: 2026-06-27

Requirement sources:

- `Assignment Requirements/CT046-3-M-AML_Assignment Question.md`
- `Assignment Requirements/CT046-3-M-AML_Assignment Marking Scheme and Minimum Document Requirements.md`

## Final Decision

Select **Impact of AI on Students** as the primary final assignment dataset after it passed the modelling, leakage, validation, notebook-execution, and literature-feasibility migration gate.

Archived predecessor: **Global Urban Air Quality & Pollution Time-Series**.

Additional backup: **AI Workforce Displacement 2020-2026**.

Frozen problem statement:

> Predict semester GPA change and evaluate whether generative-AI usage variables add predictive value beyond previous GPA and general study context, while controlling outcome leakage and avoiding causal claims.

Recommended report direction:

- Primary task: predict derived `GPA_Change`, not raw post-semester GPA.
- Primary comparison: context-only features versus context plus AI-usage features.
- Required model comparison: linear regression, Ridge, random forest, and histogram gradient boosting against a mean baseline.
- Alternative tasks: burnout classification, skill-retention regression, and GPA-decline classification remain available in the advanced notebooks.
- Optional extension: predictor-only student-behaviour clustering remains in the advanced variants, not the essential final notebook.

## Rubric Derived From The Assessment

| Criterion | Weight | Highest-distinction dataset evidence |
| --- | ---: | --- |
| Assignment fit | 20 | Reasonably large, mixed categorical and numeric variables, more than 12 variables, meaningful preprocessing, and a non-trivial problem. |
| Problem and related-works strength | 20 | Clear educational problem, recent literature, comparable methods, and defensible aim/objectives. |
| ML implementation depth | 25 | At least three tuned models, feature engineering, interpretation, classification, regression, and unsupervised learning. |
| Validation strength | 20 | Untouched test data, cross-validation, leakage control, imbalance handling, uncertainty, and subgroup analysis. |
| Analysis and recommendation potential | 15 | Critical discussion, anomalies, uncertainty, limitations, model comparisons, and carefully bounded recommendations. |

Hard demotion rules:

- Fewer than 12 variables or a very small row count.
- A deterministic, definition-adjacent, or outcome-leaking target.
- Weak same-domain literature.
- Unsupported real-world or causal claims from synthetic or undocumented data.
- Manufactured missingness or corruption presented as genuine preprocessing.

## Updated Candidate Matrix

| Rank | Dataset | Assignment fit /20 | Related works /20 | ML depth /25 | Validation /20 | Analysis /15 | Total /100 | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Impact of AI on Students | 15 | 19 | 24 | 18 | 13 | **89** | Select with explicit provenance and cleanliness limitations. |
| 2 | Global Urban Air Quality & Pollution Time-Series | 16 | 19 | 20 | 15 | 13 | Archive current implementation; retain as a backup dataset. |
| 3 | AI Workforce Displacement 2020-2026 | 17 | 16 | 21 | 15 | 11 | Retain as an additional backup. |
| 4 | LLM Hallucination | 5 | 18 | 13 | 7 | 12 | Lab/appendix only. |
| 5 | Student AI Tools vs Exam Scores | 3 | 8 | 9 | 5 | 6 | Lab practice only. |

### Why The Student-Impact Dataset Is Now Primary

- It has exactly 50,000 rows and 16 original variables, matching the assignment size guidance.
- It mixes numeric, categorical, ordinal, and Boolean fields.
- Leakage-controlled targets are challenging without being unusable.
- It supports multiclass and imbalanced binary classification, two defensible regressions, clustering, tuning, uncertainty analysis, and subgroup validation.
- The AI-in-education topic supports a current and sufficiently broad related-work section.
- The current air-quality hazard target is too closely dictated by pollutant/AQI values, while the forecasting variants can also become overly easy through temporal persistence.

### Important Limitations

- The student-impact CSV has no missing values, duplicates, or inconsistent categories. This is weaker than the assignment preference for a dataset that is not perfectly clean.
- The Kaggle page does not document collection methods, population, geography, sampling, observation dates, ethics, or real-versus-synthetic status.
- No result may be described as a causal effect of AI use, institutional policy, dependency, anxiety, or study time.
- Raw `Post_Semester_GPA` prediction is not a primary task because `Pre_Semester_GPA` alone dominates performance.

## Migration Gate Evidence

The gate used a fixed 20% untouched test split and shuffled five-fold cross-validation on the 80% training partition. All preprocessing was fitted inside each training fold.

| Task | Dummy baseline | Strongest five-fold result | Fold standard deviation | Untouched-test result | Gate |
| --- | ---: | ---: | ---: | ---: | --- |
| Burnout multiclass classification | Macro-F1 0.198 | Histogram gradient boosting macro-F1 0.535 | 0.004 | 0.533 | Pass |
| Skill-retention regression | R-squared approximately 0.000 | Histogram gradient boosting R-squared 0.216 | 0.007 | 0.222 | Pass |
| GPA-change regression | R-squared approximately 0.000 | Histogram gradient boosting R-squared 0.408 | 0.008 | Tuned test R-squared 0.4185 | Pass |
| GPA-decline classification | Macro-F1 0.467 | Random forest macro-F1 0.655 | 0.009 | 0.669 | Pass |

Additional checks:

- Three or more real models materially beat the dummy baseline for each selected direction.
- Excluding exam anxiety from the primary burnout feature set did not collapse performance.
- All 13 lab notebooks and four final notebooks parsed and completed controlled smoke execution.
- Static checks found no external result writes, saved outputs, or execution counts.
- Lab 13 was rejected because the data has no temporal sequence.

## Literature Feasibility

The topic can support the required 10–15 recent references. The final review should combine systematic reviews/meta-analyses, empirical student studies, wellbeing/dependency research, and modelling-method references.

Seed sources:

| Source | Use in report |
| --- | --- |
| [Official Kaggle dataset page](https://www.kaggle.com/datasets/laveshjadon/ai-impact-on-students) | Dataset access, stated variables, targets, licence, and provenance limitations. |
| [An, Koh, and Liu: systematic review of student GenAI use and learning outcomes](https://doi.org/10.14742/ajet.10561) | Usage patterns, actual and perceived learning outcomes, and research gaps. |
| [Badger, López, and Nissen: impact of GenAI chatbots on student learning](https://doi.org/10.46328/ijte.5111) | Motivation, engagement, self-regulation, comprehension, and performance. |
| [Fan et al.: three-level meta-analysis of higher-education learning outcomes](https://doi.org/10.3389/fpsyg.2026.1758670) | Quantitative synthesis and moderators of GenAI learning effects. |
| [Effect of GenAI on university-student learning outcomes](https://www.sciencedirect.com/science/article/pii/S1747938X25000740) | Recent systematic-review and meta-analysis evidence. |
| [ChatGPT impact on student learning outcomes](https://www.nature.com/articles/s41599-026-07019-z) | Experimental-study synthesis and learning-outcome comparisons. |
| [ChatGPT effects on performance, perception, and higher-order thinking](https://www.nature.com/articles/s41599-025-04787-y) | Meta-analysis covering academic and cognitive outcomes. |
| [AI in higher education: systematic literature review](https://doi.org/10.3389/feduc.2024.1391485) | Wider institutional, academic-integrity, and educational context. |
| [Longitudinal study of ChatGPT adoption behaviour](https://doi.org/10.3389/frai.2023.1324398) | Student usage change, trust, and the value of longitudinal evidence. |
| [ChatGPT satisfaction and continued-use intention](https://doi.org/10.3389/feduc.2024.1354929) | Adoption, perceived usefulness, and continued-use factors. |
| [Academic stress and GenAI dependency](https://doi.org/10.1016/j.iheduc.2026.101094) | Dependency, stress-coping theory, engagement, and limitations awareness. |
| [Technostress, GenAI, and digital classroom burnout](https://doi.org/10.1038/s41598-026-47683-4) | Wellbeing context and a contrasting alternative student outcome. |

The literature should be reviewed systematically rather than treated as a citation list. Same-dataset Kaggle notebooks may be discussed as implementation comparisons, but they do not replace peer-reviewed related work.

## Final Modelling Acceptance Criteria

- Preserve the raw CSV and documented SHA-256.
- Drop `Student_ID` from all models.
- Use an untouched 20% test split and five-fold validation for the full report run.
- Compare at least three real models against a dummy baseline.
- Fit preprocessing, resampling, feature selection, and tuning inside training folds.
- Use macro/class-level metrics for classification and MAE, RMSE, and R-squared for regression.
- Include bootstrap confidence intervals and subgroup error analysis.
- Keep outcome fields out of one another's predictor sets.
- Use exam anxiety only as a labelled burnout ablation.
- Fit K-means on predictor-only features.
- Explain perfect cleanliness and undocumented provenance.
- Avoid causal and population-level claims.
- Keep all final results inline in standalone notebooks.

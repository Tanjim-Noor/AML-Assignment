# Impact of AI on Students

Metadata and local schema notes for `ai_student_impact_dataset.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official Kaggle page | https://www.kaggle.com/datasets/laveshjadon/ai-impact-on-students |
| Kaggle title | Impact of Ai on Students |
| Creator | Nagi sisiro (`laveshjadon`) |
| License | CC0-1.0 / Public Domain |
| Version | 1 |
| Last updated on Kaggle | 2026-05-10 |
| Kaggle usability rating | 1.0 |
| Kaggle activity at review time | 67,809 views, 17,563 downloads, 408 votes, 43 notebooks |
| Local review date | 2026-06-27 |

## What The Dataset Is

This is a cross-sectional tabular dataset describing 50,000 student records. It combines academic background, generative-AI usage, conventional study behaviour, institutional AI policy, exam anxiety, academic outcomes, skill retention, and assessed burnout risk.

The Kaggle page presents `Post_Semester_GPA`, `Skill_Retention_Score`, and `Burnout_Risk_Level` as candidate targets. It does not document a collection instrument, institution, country, sampling design, observation dates, ethics process, or whether the rows are observed, simulated, or synthetic. The dataset must therefore be treated as a Kaggle-provided modelling dataset with undocumented provenance, not as verified survey evidence about a real student population.

## Local File Inventory

| File | Rows | Columns | Size | Missing values | Duplicate rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| `ai_student_impact_dataset.csv` | 50,000 | 16 | 5,892,478 bytes | 0 | 0 |

SHA-256:

`4D911088C4B12D60A450A9ACAE6B606F4119EBBB48679518E427A4FC00778472`

## Coverage

| Field | Local values |
| --- | --- |
| Student identifiers | 100001 to 150000; all unique |
| Major categories | STEM, Business, Humanities, Medical, Arts |
| Years of study | Freshman, Sophomore, Junior, Senior, Graduate |
| AI use cases | Debugging/Troubleshooting, Copywriting/Drafting, Ideation, Summarizing_Reading, Direct_Answer_Generation |
| Prompt skill levels | Beginner, Intermediate, Advanced |
| Institutional policies | Allowed_With_Citation, Actively_Encouraged, Strict_Ban |
| Burnout classes | Low, Medium, High |

Burnout-risk distribution:

| `Burnout_Risk_Level` | Rows | Share |
| --- | ---: | ---: |
| Low | 16,369 | 32.74% |
| Medium | 21,144 | 42.29% |
| High | 12,487 | 24.97% |

Derived GPA-change distribution:

| Measure | Value |
| --- | ---: |
| Mean change | +0.203 |
| Median change | +0.204 |
| Minimum change | -0.924 |
| Maximum change | +1.008 |
| Students with lower post-semester GPA | 12.38% |
| Students with higher post-semester GPA | 87.52% |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `Student_ID` | Integer identifier | 0 | 50,000 | 100001 to 150000 | Drop from every model; it has no defensible predictive meaning. |
| `Major_Category` | Categorical text | 0 | 5 | STEM, Business, Humanities, Medical, Arts | Encode as nominal categorical data. |
| `Year_of_Study` | Categorical text | 0 | 5 | Freshman to Graduate | Ordered in meaning, but one-hot encoding avoids imposing equal spacing. |
| `Pre_Semester_GPA` | Numeric | 0 | 2,389 | 1.183 to 3.998 | Strong baseline predictor of post-semester GPA and useful for GPA-change modelling. |
| `Weekly_GenAI_Hours` | Numeric | 0 | 3,566 | 0.00 to 40.00 | Right-skewed AI-usage measure; inspect extreme values. |
| `Primary_Use_Case` | Categorical text | 0 | 5 | Five use cases | Encode as nominal categorical data. |
| `Prompt_Engineering_Skill` | Categorical text | 0 | 3 | Beginner, Intermediate, Advanced | Can be ordinal- or one-hot-encoded depending on the model. |
| `Tool_Diversity` | Integer | 0 | 5 | 1 to 5 | Small bounded count. |
| `Paid_Subscription` | Boolean | 0 | 2 | True, False | Convert consistently to Boolean or binary form. |
| `Traditional_Study_Hours` | Numeric | 0 | 2,516 | 1.00 to 35.86 | Continuous study-behaviour feature. |
| `Perceived_AI_Dependency` | Integer ordinal | 0 | 10 | 1 to 10 | Self-rated dependency measure. |
| `Institutional_Policy` | Categorical text | 0 | 3 | Allowed_With_Citation, Actively_Encouraged, Strict_Ban | Institutional context; do not interpret group differences causally. |
| `Anxiety_Level_During_Exams` | Integer ordinal | 0 | 10 | 1 to 10 | Contemporaneous wellbeing feature; exclude from the primary early-risk burnout feature set and add only as an ablation. |
| `Post_Semester_GPA` | Numeric outcome | 0 | 2,269 | 1.00 to 4.00 | Do not use as an input when predicting GPA change, decline, retention, or burnout. |
| `Skill_Retention_Score` | Numeric outcome | 0 | 5,872 | 10.78 to 100.00 | Recommended non-trivial regression target. |
| `Burnout_Risk_Level` | Categorical outcome | 0 | 3 | Low, Medium, High | Recommended multiclass classification target. |

## Data Quality Notes

- The file is unusually clean: there are no missing values, duplicated rows, invalid identifiers, or inconsistent category spellings.
- This cleanliness conflicts with the assignment preference for a dataset that is not perfectly clean. Preprocessing must therefore demonstrate legitimate work such as identifier removal, schema and boundary validation, categorical encoding, scaling, skew/outlier analysis, target construction, imbalance handling, and leakage control. Do not manufacture missing values or corruptions.
- There is no timestamp or repeated-student structure. Random cross-sectional splits and repeated shuffled cross-validation are appropriate; chronological forecasting and univariate time-series analysis are not.
- `Pre_Semester_GPA` explains much of `Post_Semester_GPA`. A leakage-controlled random-forest baseline reached approximately 0.90 test R-squared, so raw post-GPA prediction is too easy to be the primary final task.
- `Burnout_Risk_Level` is described as an assessed risk based on study and wellbeing indicators. Use a primary early-risk feature set that excludes anxiety and all post-semester outcomes, then report anxiety only as a sensitivity/ablation feature.
- The dataset supports association and prediction, not causal claims. Model results cannot establish that AI usage caused changes in GPA, retention, anxiety, dependency, or burnout.

## Machine Learning Fit

Recommended directions:

- Multiclass classification: predict `Burnout_Risk_Level` from pre-semester, AI-usage, study-behaviour, and institutional features.
- Regression: predict `Skill_Retention_Score`.
- Regression: derive `GPA_Change = Post_Semester_GPA - Pre_Semester_GPA` and predict the magnitude of change.
- Binary classification: derive `GPA_Declined = GPA_Change < 0` and handle the minority decline class explicitly.
- Unsupervised learning: cluster students using predictor-only behavioural profiles, then interpret clusters using outcomes after fitting.

Leakage-safe defaults:

- Always remove `Student_ID`.
- Exclude `Post_Semester_GPA`, `Skill_Retention_Score`, and `Burnout_Risk_Level` from one another's predictor sets.
- Never include `Post_Semester_GPA` when modelling derived GPA change or decline.
- Use `Anxiety_Level_During_Exams` only in a documented burnout ablation, not the primary early-risk model.
- Fit encoders, scalers, imputers, resampling, and feature selection only on training folds.

Initial local feasibility baselines:

| Task | Leakage-controlled result | Interpretation |
| --- | --- | --- |
| Burnout multiclass classification | Macro-F1 about 0.52 vs 0.20 dummy | Non-trivial but not suspiciously easy. |
| Skill-retention regression | Test R-squared about 0.19 | Difficult target with room for comparison and critical analysis. |
| GPA-change regression | Test R-squared about 0.39 | Moderate target suitable for regression experiments. |
| GPA-decline classification | Macro-F1 about 0.64; decline share 12.38% | Useful imbalanced binary-classification variant. |

## Assignment Suitability

The dataset matches the 20k-to-50k row guideline, has more than 12 variables, mixes categorical and numeric data, supports classification, regression, clustering, imbalance handling, model tuning, and subgroup analysis, and has a strong contemporary AI-in-education literature base.

Its main weaknesses are perfect cleanliness and undocumented provenance. It is suitable as a conditional final dataset only when the report:

- makes those limitations prominent,
- avoids causal or population-level claims,
- uses leakage-controlled feature sets,
- demonstrates meaningful validation rather than reporting accuracy alone,
- and frames recommendations as modelling implications that require confirmation with real longitudinal or survey data.

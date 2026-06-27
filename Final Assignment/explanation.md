# Essential GPA-Change Regression Notebook: Explanation and Results Analysis

Notebook:

`Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb`

This document explains what every notebook section does, why it is needed for the assignment, and what the executed results mean.

## What The Notebook Investigates

The notebook predicts:

```text
GPA_Change = Post_Semester_GPA - Pre_Semester_GPA
```

A positive value means GPA increased. A negative value means GPA decreased.

The research question is:

> Do AI-usage variables add useful predictive information about GPA change beyond previous GPA and general study context?

This wording is important. The dataset can show whether AI-related variables help predict GPA change. It cannot prove that AI usage caused the change because there is no credible non-AI control group, random assignment, or documented data-collection process.

## Why Regression Was Selected

GPA change is a continuous number, so regression preserves more information than classification.

For example:

- a change of `+0.02` and `+0.80` would both become “improved” in classification;
- regression keeps the difference between these outcomes;
- regression allows errors to be measured directly in GPA points;
- the target is more closely aligned with academic change than predicting raw post-semester GPA.

Raw post-semester GPA was not selected because it is already highly predictable from pre-semester GPA. That would produce an impressive score without answering whether AI variables add useful information.

## Notebook Sections

| Section | Responsibility | Why it is useful |
| --- | --- | --- |
| Problem statement | Defines GPA change and the research question. | Prevents the analysis from drifting into unsupported causal claims. |
| Aim and objectives | Lists the work the notebook must complete. | Connects the implementation to the assignment objectives and conclusion. |
| Setup and data loading | Imports packages and loads the raw CSV. | Makes the notebook reproducible and self-contained. |
| Dataset understanding and EDA | Checks rows, missing values, duplicates, target distribution, prompt skill, and AI-hours patterns. | Demonstrates dataset preparation and identifies patterns that may explain model behaviour. |
| Data preparation and leakage control | Defines context and AI feature groups and removes identifiers/outcome columns. | Prevents the models from receiving invalid or target-derived information. |
| Train/test split | Reserves 20% of the rows as untouched test data. | Provides a fair final check on unseen records. |
| AI predictive-value comparison | Fits the same model with context-only, AI-only, and combined features. | Directly tests whether AI variables add predictive information. |
| Model comparison | Compares a baseline and four regression models with five-fold cross-validation. | Satisfies the requirement to compare at least three models consistently. |
| Hyperparameter tuning | Searches for a stronger gradient-boosting configuration. | Demonstrates model optimisation using training folds only. |
| Final test evaluation | Calculates MAE, RMSE, and R² on the untouched test set. | Shows how the models generalise beyond the training data. |
| Residual analysis | Examines the difference between actual and predicted GPA changes. | Reveals bias, typical error size, and unexplained variation. |
| Feature importance | Measures the performance loss caused by shuffling each feature. | Identifies which fields were most useful for prediction. |
| Results analysis | Automatically converts the computed metrics into plain-language findings. | Ensures the discussion refers to actual results rather than generic statements. |
| Recommendations and limitations | States responsible uses and weaknesses of the evidence. | Supports the assignment’s analysis and recommendations marks. |
| Conclusion | Returns to the aim and gives the defensible final claim. | Demonstrates whether the objectives were achieved. |

## Dataset Findings

The notebook loaded:

| Check | Result |
| --- | ---: |
| Rows | 50,000 |
| Original columns | 16 |
| Missing cells | 0 |
| Duplicate rows | 0 |
| Unique student IDs | 50,000 |
| Students with increased GPA | 43,759 |
| Students with decreased GPA | 6,192 |

The mean GPA change was `+0.2032`, with a standard deviation of `0.1872`.

The changes ranged from `-0.924` to `+1.008`. The dataset therefore contains both improvement and decline, although improvement is much more common.

### Initial AI-Related Patterns

Mean GPA change by prompt-engineering skill:

| Prompt skill | Mean GPA change |
| --- | ---: |
| Advanced | +0.2481 |
| Intermediate | +0.1869 |
| Beginner | +0.1852 |

Mean GPA change by weekly AI-hours quartile:

| AI-hours group | Mean GPA change |
| --- | ---: |
| Lowest | +0.1881 |
| Low-Medium | +0.2055 |
| High-Medium | +0.2287 |
| Highest | +0.1905 |

The pattern is not a simple “more AI hours means higher GPA” relationship. The high-medium group had the largest mean increase, while the highest-use group had a smaller increase. This supports using nonlinear models and cautions against simplistic recommendations.

These group means are descriptive associations. They do not control for other student differences and cannot establish an AI effect.

## Do AI Variables Add Predictive Value?

The same histogram gradient boosting method was tested with three feature sets.

| Feature set | CV R² | Test MAE | Test RMSE | Test R² |
| --- | ---: | ---: | ---: | ---: |
| Context only | 0.2378 | 0.1239 | 0.1618 | 0.2382 |
| AI variables only | 0.1708 | 0.1347 | 0.1689 | 0.1703 |
| Context and AI variables | 0.4084 | 0.1114 | 0.1415 | 0.4170 |

The combined feature set increased test R² by:

```text
0.4170 - 0.2382 = 0.1788
```

This is a meaningful predictive improvement.

The correct interpretation is:

> AI-related variables contain additional information that helps predict GPA change after general context is included.

The incorrect interpretation is:

> AI usage caused 17.88% more GPA improvement.

R² differences are changes in predictive explanatory performance, not causal-effect percentages.

AI variables alone reached only `0.1703` test R². They are not sufficient by themselves. The best predictions require both student context and AI-related information.

## Five-Fold Model Comparison

| Model | CV MAE | CV RMSE | CV R² | R² standard deviation |
| --- | ---: | ---: | ---: | ---: |
| Histogram gradient boosting | 0.1130 | 0.1443 | 0.4080 | 0.0085 |
| Random forest | 0.1149 | 0.1473 | 0.3833 | 0.0122 |
| Ridge regression | 0.1261 | 0.1608 | 0.2657 | 0.0104 |
| Linear regression | 0.1261 | 0.1608 | 0.2657 | 0.0104 |
| Mean baseline | 0.1459 | 0.1876 | -0.0003 | 0.0004 |

### Interpretation

- All four real models outperformed the mean baseline.
- Histogram gradient boosting produced the best average cross-validation result.
- Random forest was the second-best model.
- Linear and Ridge regression produced almost identical results.
- The nonlinear tree ensembles performed better than the linear models, indicating that the relationships are not fully explained by one straight-line effect per feature.
- The best model’s R² standard deviation was only `0.0085`, showing stable performance across the five folds.

## Hyperparameter Tuning

The best gradient-boosting configuration was:

| Parameter | Selected value |
| --- | ---: |
| Minimum samples per leaf | 10 |
| Maximum leaf nodes | 15 |
| Boosting iterations | 180 |
| Learning rate | 0.05 |
| L2 regularisation | 0.1 |

Its best five-fold cross-validation RMSE was `0.1441`.

The small learning rate and moderate number of leaf nodes produce gradual, controlled learning rather than a highly complex tree structure. L2 regularisation adds protection against overfitting.

## Final Test Results

| Model | Test MAE | Test RMSE | Test R² |
| --- | ---: | ---: | ---: |
| Tuned histogram gradient boosting | **0.1112** | **0.1414** | **0.4185** |
| Histogram gradient boosting | 0.1114 | 0.1416 | 0.4166 |
| Random forest | 0.1142 | 0.1448 | 0.3896 |
| Linear regression | 0.1242 | 0.1583 | 0.2712 |
| Ridge regression | 0.1242 | 0.1583 | 0.2712 |
| Mean baseline | 0.1444 | 0.1854 | -0.0003 |

### Winning Model

The tuned histogram gradient boosting model was the strongest final model.

- MAE `0.1112` means its prediction differed from the actual GPA change by approximately 0.11 GPA points on average.
- RMSE `0.1414` penalises larger mistakes more strongly.
- R² `0.4185` means the model accounted for approximately 41.85% of the variation in GPA change within the test data.

The untuned model reached R² `0.4166`. Tuning improved R² by only `0.0019`. The gain is real but small, so the report should not exaggerate the value of tuning.

The selected model reduced RMSE from the baseline’s `0.1854` to `0.1414`, a reduction of approximately 23.7%.

## Cross-Validation Versus Test Performance

The best untuned cross-validation R² was `0.4080`, while the tuned model’s test R² was `0.4185`.

The difference is approximately `+0.0105`. Test performance is close to the cross-validation estimate, providing no strong evidence of severe overfitting.

The test result being slightly higher does not mean the model improved after seeing test data. It reflects ordinary sampling variation between the cross-validation folds and test partition.

## Residual and Error Analysis

| Error measure | Result |
| --- | ---: |
| Mean residual | +0.0019 |
| Residual standard deviation | 0.1414 |
| Median absolute error | 0.0922 |
| Predictions within 0.10 GPA points | 53.57% |
| Predictions within 0.20 GPA points | 84.34% |

The mean residual is close to zero, so the model does not consistently overpredict or underpredict GPA change overall.

Approximately half the predictions are within 0.10 GPA points, and more than four-fifths are within 0.20 points. This is useful predictive performance, but the unexplained errors remain large enough that the model should not be used for individual academic decisions.

## Feature Importance

The most useful predictors were:

| Rank | Feature | Permutation importance |
| ---: | --- | ---: |
| 1 | `Traditional_Study_Hours` | 0.0328 |
| 2 | `Primary_Use_Case` | 0.0267 |
| 3 | `Weekly_GenAI_Hours` | 0.0174 |
| 4 | `Year_of_Study` | 0.0136 |
| 5 | `Prompt_Engineering_Skill` | 0.0122 |
| 6 | `Pre_Semester_GPA` | 0.0108 |

Three of the six strongest features are directly AI-related:

- primary AI use case;
- weekly AI hours;
- prompt-engineering skill.

This supports the conclusion that AI variables add predictive information. It does not show that changing these variables would cause GPA to change.

Traditional study hours was the strongest feature. The result suggests that conventional study behaviour remains important even in an AI-focused dataset.

## Overall Findings

1. GPA change is moderately predictable.
2. Nonlinear ensemble models clearly outperform linear regression.
3. The tuned histogram gradient boosting model is the best model, but tuning only slightly improves the untuned version.
4. Context-only and AI-only models are both incomplete.
5. Combining context and AI features produces the strongest results.
6. AI-use case, AI hours, and prompt skill contribute useful predictive information.
7. Traditional study hours remains the single strongest predictor.
8. The model generalises consistently across cross-validation and test data.
9. Considerable variation remains unexplained, so individual predictions should be treated cautiously.
10. No causal conclusion about AI’s effect on GPA is justified.

## Defensible Final Claim

Use this wording:

> The addition of AI-usage variables improved the prediction of semester GPA change beyond previous GPA and general study-context variables. The combined model achieved test R² of 0.4170, compared with 0.2382 for the context-only model. The tuned histogram gradient boosting model produced the strongest final result with MAE 0.1112, RMSE 0.1414, and R² 0.4185. These findings indicate predictive associations within the supplied dataset and do not establish that AI usage caused GPA changes.

Do not use this wording:

> The model proves that AI improves students’ GPA.

## How This Supports The Assignment Report

| Report section | Notebook evidence to use |
| --- | --- |
| Methods | Regression problem, feature groups, preprocessing pipeline, split, models, metrics, and tuning design. |
| Dataset Preparation | Integrity checks, target creation, EDA, identifier removal, categorical encoding, scaling, and leakage prevention. |
| Model Implementation | Linear regression, Ridge, random forest, histogram gradient boosting, and the tuned model. |
| Model Validation | Five-fold results, fold variability, untouched-test metrics, actual-versus-predicted plot, and residual diagnostics. |
| Analysis and Recommendations | AI incremental-value comparison, model ranking, tuning gain, feature importance, error interpretation, limitations, and future-data recommendations. |
| Conclusion | The defensible final claim and explicit statement that association is not causation. |

## Key Terms

| Term | Plain-language meaning |
| --- | --- |
| Target | The value the model attempts to predict; here it is GPA change. |
| Feature | An input column used to make a prediction. |
| Regression | Predicting a numeric value. |
| Baseline | A simple reference prediction that real models should beat. |
| Train set | Data used to fit models. |
| Test set | Unseen data reserved for final evaluation. |
| Cross-validation | Repeating training and validation across several partitions to estimate stability. |
| MAE | Average absolute prediction error in GPA points. |
| RMSE | Error metric that penalises larger mistakes more strongly. |
| R² | Proportion of target variation accounted for by the model; higher is better. |
| Hyperparameter | A model setting selected before training, such as learning rate. |
| Residual | Actual GPA change minus predicted GPA change. |
| Leakage | Giving the model information that would not legitimately be available when predicting. |
| Feature importance | How useful a feature was for prediction, not proof of causal influence. |
| Overfitting | Learning training-specific patterns that do not generalise to unseen data. |

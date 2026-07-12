# Predicting Semester GPA Change Using Student Context and Generative AI Usage: A Leakage-Controlled Machine Learning Study

## Abstract

Generative-AI tools are used in higher education, but evidence
about their relationship with academic performance remains mixed and
context-dependent. This study investigated whether recorded AI-use variables
improved out-of-sample prediction of semester GPA change beyond previous GPA
and general study context, and which regression model provided the strongest
validated performance. The Kaggle *Impact of Ai on Students* dataset contained
50,000 records and 16 source columns. Every field was audited for completeness,
validity and distribution; no valid observations were changed.
GPA change was defined as post-semester
minus pre-semester GPA. `Student_ID`, post-semester GPA and two other
post-outcome fields were excluded to prevent meaningless identification and
outcome leakage. Numeric and categorical variables were processed through
fold-fitted imputation, standardisation and one-hot encoding. A mean baseline,
Linear Regression, Ridge Regression, Random Forest and Histogram Gradient
Boosting (HGB) were compared using an 80/20 development-test split and shuffled
five-fold cross-validation; HGB was subsequently tuned within the development
data. The combined context-and-AI model achieved test $R^2=0.4170$, compared
with 0.2382 for context only and 0.1703 for AI variables only. Untuned HGB
produced the strongest model-comparison CV RMSE of 0.1443, while tuning reduced
the best CV RMSE to 0.1441. On the reserved test set, tuned HGB achieved MAE
0.1112, RMSE 0.1414 and $R^2=0.4185$; 84.34% of predictions were within 0.20
GPA points. Traditional study hours, primary AI use case and weekly GenAI hours
were the three largest permutation importances. These findings indicate that
AI-related fields supplied additional predictive information when combined
with student context and that nonlinear ensembles represented the recorded
relationships better than linear models. However, undocumented dataset
provenance and much higher error for GPA decreases prohibit causal or
individual-decision conclusions.

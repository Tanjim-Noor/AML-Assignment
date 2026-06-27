# Impact of AI on Students Lab Applications

Source dataset: `Datasets/Impact of AI on Students/ai_student_impact_dataset.csv`

These notebooks apply the class learning materials to the student-impact dataset without editing the raw CSV. The dataset has undocumented collection and real-versus-synthetic provenance, so all interpretations are predictive or associative rather than causal.

## Lab 01 - Data Loading

`Lab 01 - Data Loading/lab_01_data_loading.ipynb` applies the Lab 1 workflow: locate and load the CSV, inspect records, shape, columns, data types, missing values, duplicates, and identifier uniqueness.

## Lab 02 - Data Understanding

`Lab 02 - Data Understanding/lab_02_data_understanding.ipynb` applies numeric and categorical summaries, target distributions, correlations, grouped comparisons, and dataset-appropriate visualisations.

## Lab 03 - Data Preprocessing

`Lab 03 - Data Preprocessing/lab_03_data_preprocessing.ipynb` validates expected value boundaries, removes `Student_ID`, creates GPA-change targets, defines leakage-safe feature sets, encodes categorical fields, scales numeric fields, and performs a stratified split.

## Lab 04 - Naive Bayes

`Lab 04 - Naive Bayes/lab_04_naive_bayes.ipynb` compares a dummy classifier with Gaussian Naive Bayes for multiclass `Burnout_Risk_Level` prediction using macro-F1, balanced accuracy, multiclass ROC-AUC, class-level metrics, and a normalised confusion matrix.

## Lab 05 - Decision Tree

`Lab 05 - Decision Tree/lab_05_decision_tree.ipynb` applies decision-tree classification to burnout risk and decision-tree regression to skill retention, comparing controlled depths to expose overfitting.

## Lab 06 - Linear Regression

`Lab 06 - Linear Regression/lab_06_linear_regression.ipynb` compares linear regression, Ridge, Lasso, and Elastic Net for skill retention and GPA change, then adds a controlled polynomial Ridge experiment.

## Lab 07 - Cross Validation

`Lab 07 - Cross Validation/lab_07_cross_validation.ipynb` uses repeated shuffled five-fold validation for regression and repeated stratified five-fold validation for classification. Chronological validation is intentionally not used because the dataset has no timestamp or repeated-student sequence.

## Lab 07 - Logistic Regression

`Lab 07 - Logistic Regression/lab_07_logistic_regression.ipynb` applies class-weighted multiclass logistic regression to burnout risk and inspects class-specific coefficients.

## Lab 08 - SVM

`Lab 08 - SVM/lab_08_svm.ipynb` compares a full-data linear SVM with a reproducible 12,000-row RBF SVM experiment after scaling and encoding.

## Lab 09 - Neural Network

`Lab 09 - Neural Network/lab_09_neural_network.ipynb` applies early-stopping scikit-learn MLP models to burnout classification and skill-retention regression.

## Lab 10 - RF

`Lab 10 - RF/lab_10_random_forest.ipynb` applies random-forest classification and regression with class weighting, controlled leaf sizes, and transformed feature-importance inspection.

## Lab 11 - Ensemble Models

`Lab 11 - Ensemble Models/lab_11_ensemble_models.ipynb` compares logistic regression, a decision tree, random forest, histogram gradient boosting, and a soft-voting ensemble for burnout classification.

## Lab 12 - K Means Clustering

`Lab 12 - K Means Clustering/lab_12_k_means_clustering.ipynb` selects a cluster count using silhouette score, fits predictor-only student-behaviour profiles, and interprets outcomes only after fitting.

## Lab 13 Applicability Decision

Lab 13 univariate time-series analysis is not implemented for this dataset. Each row is a different student, and there is no timestamp, ordered observation index, repeated-student history, or defensible temporal frequency. Treating `Student_ID` as time would be invalid.

## Shared Modelling Rules

- Drop `Student_ID` from every model.
- Never use post-semester outcomes to predict one another.
- Never use `Post_Semester_GPA` to predict derived GPA change or GPA decline.
- Exclude exam anxiety from the primary early-risk burnout feature set; add it only as an explicit ablation.
- Fit preprocessing only on training folds.
- Use macro and class-level metrics for burnout and GPA-decline classification.
- Do not manufacture missing values or claim that model associations are causal effects.

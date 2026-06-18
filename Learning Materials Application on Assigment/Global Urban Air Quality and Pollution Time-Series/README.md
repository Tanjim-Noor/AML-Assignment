# Global Urban Air Quality and Pollution Time-Series Lab Applications

Source dataset: `Datasets/Global Urban Air Quality & Pollution Time-Series/global_urban_smog_pm25_hourly.csv`

## Lab 01 - Data Loading

`Lab 01 - Data Loading/lab_01_data_loading.ipynb` applies the Lab 1 workflow: package/import note, pandas CSV loading, display settings, dataframe display, `head()`, `tail()`, shape, columns, and dtypes.

## Lab 02 - Data Understanding

`Lab 02 - Data Understanding/lab_02_data_understanding.ipynb` applies the Lab 2 workflow: row inspection, category counts, and dataset-appropriate visualizations based on the Iris examples.

## Lab 03 - Data Preprocessing

`Lab 03 - Data Preprocessing/lab_03_data_preprocessing.ipynb` applies timestamp parsing, missing-value checks, city-aware `PM10_ug_m3` imputation, time feature engineering, categorical encoding, scaling, and chronological splitting.

## Lab 04 - Naive Bayes

`Lab 04 - Naive Bayes/lab_04_naive_bayes.ipynb` builds a no-`European_AQI` Gaussian Naive Bayes baseline for `Hazardous_Event` classification with confusion matrix, classification report, and threshold tuning.

## Lab 05 - Decision Tree

`Lab 05 - Decision Tree/lab_05_decision_tree.ipynb` applies decision-tree classification for `Hazardous_Event` and decision-tree regression for `PM2_5_ug_m3`, including feature-importance and tree-structure inspection.

## Lab 06 - Linear Regression

`Lab 06 - Linear Regression/lab_06_linear_regression.ipynb` predicts `PM2_5_ug_m3` using linear regression, Ridge, Lasso, Elastic Net, and a controlled polynomial Ridge baseline.

## Lab 07 - Cross Validation

`Lab 07 - Cross Validation/lab_07_cross_validation.ipynb` compares shuffled K-fold validation with `TimeSeriesSplit` so the final workflow can justify chronological validation.

## Lab 07 - Logistic Regression

`Lab 07 - Logistic Regression/lab_07_logistic_regression.ipynb` trains a class-weighted no-`European_AQI` logistic regression model for `Hazardous_Event`, with coefficient inspection and threshold tuning.

## Lab 08 - SVM

`Lab 08 - SVM/lab_08_svm.ipynb` applies scaled SVM classification with a practical linear SVM baseline and a smaller RBF SVM comparison.

## Lab 09 - Neural Network

`Lab 09 - Neural Network/lab_09_neural_network.ipynb` applies lightweight scikit-learn MLP classifier and regressor models with early stopping.

## Lab 10 - RF

`Lab 10 - RF/lab_10_random_forest.ipynb` applies random-forest classification and regression, including feature-importance review.

## Lab 11 - Ensemble Models

`Lab 11 - Ensemble Models/lab_11_ensemble_models.ipynb` compares logistic regression, decision tree, random forest, histogram gradient boosting, and a soft voting ensemble for hazardous-event classification.

## Lab 12 - K Means Clustering

`Lab 12 - K Means Clustering/lab_12_k_means_clustering.ipynb` builds unsupervised pollution-profile clusters and interprets them after fitting using AQI and hazardous-event rates.

## Lab 13 - Univariate Time Series Analysis

`Lab 13 - Univariate Time Series Analysis/lab_13_univariate_time_series_analysis.ipynb` creates a single-city hourly `PM2_5_ug_m3` series, studies rolling and seasonal patterns, and compares lag-based forecasting models against a persistence baseline.

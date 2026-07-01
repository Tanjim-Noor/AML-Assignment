# Model Implementation

## Common pipeline

Every candidate used the same train-test indices, five cross-validation folds
and preprocessing architecture. This controlled comparison isolates differences
in the estimators rather than allowing each model to benefit from a different
data treatment. Numeric columns were median-imputed and standardised.
Categorical and Boolean columns were most-frequent-imputed and one-hot encoded.
The dense encoded matrix was then supplied to the estimator. Because the
preprocessor and estimator formed one `Pipeline`, fitting within a
cross-validation fold could not learn category levels, medians, modes or scale
parameters from its validation partition.

The mean baseline was essential even though it was not a learning model. It
predicted the development-set mean GPA change for every record and established
the minimum performance that a useful regression model should exceed. Its
expected $R^2$ is around zero on unseen data; a negative value means that even
the fixed mean would perform better.

## Candidate regressors

Ordinary least-squares Linear Regression provided an interpretable additive
benchmark. It assumes that the encoded predictors contribute through linear
combinations and therefore cannot directly represent thresholds or
interactions. Ridge Regression used the same functional form with an L2 penalty
and `alpha=1.0`. It tests whether shrinking correlated or weak coefficients
improves generalisation.

Random Forest represented bagged nonlinear trees. The implementation used 180
trees, a minimum of three samples per leaf and 80% of available features at
each split (`max_features=0.8`). Setting `n_jobs=1` within the estimator avoided
nested model-level parallelism, while the cross-validation operation could run
folds in parallel. A fixed random state made bootstrap sampling and feature
selection reproducible. Tree ensembles were suitable because the exploratory
patterns suggested possible thresholds and interactions, and comparable
educational-data-mining studies have found tree-based methods competitive with
linear and other classifiers (Yağcı, 2022). That prior classification result
was methodological context, not a numerical benchmark for this regression.

Histogram Gradient Boosting built trees sequentially, with each iteration
reducing residual error from the preceding ensemble. Histogram binning makes
the method efficient for 50,000 rows. The untuned comparison used 180 boosting
iterations, learning rate 0.07 and 31 maximum leaf nodes. Its capacity to learn
non-additive structure was relevant to the non-monotonic AI-hours pattern and
the ceiling-shaped relation between previous GPA and GPA change.

**Table 5. Candidate model specification**

| Model | Key implementation settings | Analytical role |
|---|---|---|
| Mean baseline | `strategy="mean"` | Minimum predictive reference |
| Linear Regression | scikit-learn defaults | Unregularised additive benchmark |
| Ridge Regression | `alpha=1.0` | Regularised additive benchmark |
| Random Forest | 180 trees; minimum leaf 3; 80% features; seed 42 | Bagged nonlinear ensemble |
| HGB | 180 iterations; rate 0.07; 31 leaves; seed 42 | Boosted nonlinear ensemble |

## Feature-set ablation

Before the broad model comparison, the same HGB procedure was applied to three
feature sets. The context-only model used five academic and study-context
variables. The AI-only model used seven AI behaviour, skill and institutional
variables. The combined model used all 12. For this ablation, HGB used 150
iterations, learning rate 0.08 and 31 maximum leaf nodes. Holding the estimator
and data partition constant meant that the difference between context-only and
combined performance could be interpreted as incremental predictive
information from the AI feature group within this dataset.

This is not the same as a treatment comparison. Some AI variables may encode
unobserved differences in courses, students or institutional settings, and the
dataset contains no random assignment or credible non-user control group.
Accordingly, the ablation quantifies prediction, not an AI-induced GPA change.

## Hyperparameter optimisation

HGB achieved the lowest mean cross-validated RMSE in the untuned comparison and
was therefore the only family passed to optimisation. Restricting tuning to the
development data preserved the test set for confirmation. A randomised search
evaluated ten sampled combinations from the space in Table 6. RMSE was the
search objective because it expresses error in GPA points while assigning
greater cost to large mistakes.

**Table 6. HGB randomised-search space and selected configuration**

| Hyperparameter | Candidate values | Selected |
|---|---|---:|
| Learning rate | 0.03, 0.05, 0.08, 0.10 | 0.05 |
| Maximum leaf nodes | 15, 31, 63 | 15 |
| Minimum samples per leaf | 10, 20, 40 | 10 |
| L2 regularisation | 0.0, 0.1, 1.0 | 0.1 |
| Maximum iterations | 120, 180, 240 | 180 |

The selected configuration combined a smaller learning rate with 180
iterations, fewer maximum leaves and modest L2 regularisation. This represents
gradual learning with constrained tree complexity. Explicitly reporting such
controls is important because ensemble performance depends on tuning choices,
and broad algorithm labels conceal materially different model capacities
(Probst et al., 2019).

The best search score was a five-fold RMSE of 0.1441, compared with 0.1443 for
the strongest untuned HGB comparison. The improvement was therefore only
0.0002 GPA points at the displayed precision. The optimisation still
demonstrated a valid tuning procedure, but its small gain indicates that the
initial HGB settings were already close to the useful region of the tested
space.

## Final fitting and interpretation outputs

After search completion, the best pipeline was refitted on all 40,000
development rows. The same procedure was used to fit the untuned models so that
all candidates could be evaluated on the reserved 10,000-row test set.
Predictions from the tuned HGB were retained for residual analysis.

Permutation importance was calculated on the test data with RMSE scoring, five
repetitions and random state 42. Each source feature was shuffled while the
fitted pipeline remained fixed; the mean deterioration in score described how
much the model relied on that feature. This method can capture contribution in
a nonlinear pipeline but remains sensitive to correlated predictors and the
specific fitted model. It was used for interpretation, not for asserting that a
feature produced the outcome.

# Conclusion

The following conclusions can be drawn from this predictive study. AI-use
variables improved held-out prediction of semester GPA change when they were
combined with previous GPA and general study context. The combined HGB
feature-set model achieved test $R^2=0.4170$, compared with 0.2382 for context
only and 0.1703 for AI variables only. Among the candidate algorithms,
Histogram Gradient Boosting produced the strongest cross-validated performance,
and its tuned version achieved test MAE 0.1112, RMSE 0.1414 and
$R^2=0.4185$. These values answer the research question within the supplied
dataset; they do not show that AI use caused any student's GPA to change.

All six objectives were met. Every field was profiled for type, completeness,
cardinality, range, distribution and category frequency without altering the
raw data. The 50,000 rows, 16 source columns, absence of missing values,
duplicates and invalid ranges were reported. GPA change was constructed as a
continuous target, while context, AI-only and combined feature groups enabled a
direct ablation. Identifier and post-outcome fields were removed, and
preprocessing was fitted within model pipelines. A baseline and four regressors
were compared using identical five-fold validation. The strongest nonlinear
family was tuned using development folds, then confirmed on a reserved test
set. Finally, residuals, prediction tolerances and permutation importance were
interpreted alongside the literature.

What worked best was the controlled comparison: nonlinear ensembles improved
on the linear models, and cross-validation and test rankings were consistent.
The feature-set experiment also answered a substantive question rather than
merely selecting an algorithm. What worked less well was extensive tuning; the
HGB improvement was small, indicating that the initial settings were already
adequate. The final model also left most outcome variation unexplained and
compressed extreme predictions. Direction-specific testing exposed this
limitation: MAE was 0.1979 for GPA decreases versus 0.0993 for increases, with
declines systematically predicted towards the positive centre.

The main limitation is evidential rather than computational. Dataset
collection, sampling, geography, ethics and real-versus-synthetic status are
undocumented, and perfect cleanliness reduces confidence that the file reflects
unprocessed field data. Future work should collect longitudinal, provenance-rich
records; include course, assessment and instructor context; define a credible
comparison group; and validate the model externally. A controlled design would
be required before making intervention claims. The practical implication is
therefore cautious: purposeful AI-use variables deserve inclusion in future
student-success research, but neither usage hours nor feature importance should
be converted into prescriptive advice without stronger evidence.

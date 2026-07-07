#import "../template.typ": *

= Model Validation

== Cross-validation and model selection

Table 7 reports the five-fold development results used for model selection. All four trained regressors clearly outperformed the mean baseline. Histogram Gradient Boosting (HGB) had the lowest mean RMSE (0.1443), lowest MAE (0.1130) and highest $R^2$ (0.4080). Random Forest ranked second, while Linear and Ridge Regression were effectively identical. The HGB fold-to-fold $R^2$ standard deviation was 0.0085, compared with 0.0122 for Random Forest, indicating that the winning untuned model was also comparatively stable across the five partitions. The tuned search reduced mean CV RMSE slightly further to 0.1441.

#figure(
  {
    compact-table(size: 8pt)[
      #table(
        columns: 8,
        align: left + top,
        inset: (x: 4pt, y: 3pt),
        stroke: 0.45pt + rule-grey,
        fill: (x, y) => if y == 0 { pale-grey },
        table.header(
          [Model],
          [CV MAE],
          [CV RMSE],
          [CV $R^2$],
          [SD of CV $R^2$],
          [Test MAE],
          [Test RMSE],
          [Test $R^2$],
        ),
        [Tuned HGB],
        [-],
        [#strong[0.1441]],
        [-],
        [-],
        [#strong[0.1112]],
        [#strong[0.1414]],
        [#strong[0.4185]],
        [HGB],
        [#strong[0.1130]],
        [0.1443],
        [#strong[0.4080]],
        [#strong[0.0085]],
        [0.1114],
        [0.1416],
        [0.4166],
        [Random Forest],
        [0.1149],
        [0.1473],
        [0.3833],
        [0.0122],
        [0.1142],
        [0.1448],
        [0.3896],
        [Ridge Regression],
        [0.1261],
        [0.1608],
        [0.2657],
        [0.0104],
        [0.1242],
        [0.1583],
        [0.2712],
        [Linear Regression],
        [0.1261],
        [0.1608],
        [0.2657],
        [0.0104],
        [0.1242],
        [0.1583],
        [0.2712],
        [Mean baseline],
        [0.1459],
        [0.1876],
        [-0.0003],
        [0.0004],
        [0.1444],
        [0.1854],
        [-0.0003],
      )
    ]
  },
  caption: [Five-fold cross-validation and reserved-test performance],
  kind: table,
)

#emph[Note.]​ CV = cross-validation; HGB = Histogram Gradient Boosting; MAE = mean absolute error; RMSE = root mean squared error; SD = standard deviation. Bold values mark the strongest available result within their comparison. Em dashes indicate tuned CV statistics that the notebook did not retain.

The fold standard deviations describe stability, not formal significance. Because the notebook retained neither paired fold differences nor confidence intervals, statistical superiority is not claimed. Selection rests on average ranking under identical folds and reserved-test confirmation, not the lowest test error alone.

== Test confirmation

The reserved test results retained the development ranking. As Figure 2 shows, tuned and untuned HGB had the lowest RMSE, followed by Random Forest, the two linear models and the baseline. The tuned HGB achieved MAE 0.1112, RMSE 0.1414 and $R^2=0.4185$. Relative to the baseline RMSE of 0.1854, its RMSE was approximately 23.7% lower. The improvement over untuned HGB was only 0.0002 RMSE and 0.0019 $R^2$, so validation supports HGB strongly but the specific benefit of tuning only weakly. Its test $R^2$ was only 0.0105 above the best untuned cross-validation mean, which is consistent with ordinary partition variation and provides no strong indication of severe overfitting.

#figure(
  image("../../assets/fig02_model_test_rmse_and_actual_vs_predicted.png", width: 100%),
  caption: [Reserved-test RMSE by model and actual versus predicted GPA change for the selected tuned HGB model. The dashed diagonal represents perfect predictions.],
)

== Residual behaviour

Figure 3 shows residuals defined as actual minus predicted GPA change. Their mean was 0.0019 and their standard deviation was 0.1414. The near-zero mean indicates little overall directional bias, but the scatter demonstrates substantial unexplained record-level variation. Predictions also compressed extreme outcomes towards the centre, a common limitation when a model is optimised for average error and extreme cases are sparse.

The median absolute error was 0.0922. Of the 10,000 test predictions, 53.57% were within 0.10 GPA points of the observed change and 84.34% were within 0.20. These tolerances make the error scale more interpretable than $R^2$ alone. However, the remaining error and moderate $R^2$ prevent the model from being treated as a high-confidence decision rule for individual students.

#figure(
  image("../../assets/fig03_residual_diagnostics.png", width: 100%),
  caption: [Residuals against predicted GPA change and the residual distribution for tuned HGB.],
)

The execution was reproduced without editing the canonical notebook. The raw analysis summary and eight displayed result tables matched the saved run exactly. Cleanup-only ZMQ and joblib warnings were recorded, but they did not alter any metric, ranking or figure.

Although CV had already favoured tuned HGB, notebook code sorted the test table to choose the model used in diagnostic plots. No refitting followed, but using one partition for several confirmatory summaries may be more optimistic than an external evaluation.

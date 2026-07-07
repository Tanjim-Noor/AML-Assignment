#import "../template.typ": *

= Methods

== Research design

This study used a cross-sectional predictive modelling design. Its unit of analysis was one student record in the supplied tabular dataset, and its outcome was the change between pre-semester and post-semester grade point average (GPA). In this report, #emph[GPA change]​ refers to:

$ "GPA Change"_i = "Post-Semester GPA"_i - "Pre-Semester GPA"_i $

Positive values denote an increase and negative values denote a decrease. A regression design was selected because the target is continuous. This preserves the magnitude of change that would be lost by reducing the outcome to “improved” or “declined”. The design addresses prediction and comparison; it does not estimate an effect of AI use.

== Data and feature groups

The source was the #emph[Impact of Ai on Students]​ dataset downloaded from Kaggle (Nagi sisiro, 2026). It contained 50,000 records and 16 source columns. The target was derived after loading the data. Twelve predictors were divided into two conceptually distinct groups. The context group contained #raw("Pre_Semester_GPA"), #raw("Major_Category"), #raw("Year_of_Study"), #raw("Traditional_Study_Hours") and #raw("Anxiety_Level_During_Exams"). The AI group contained #raw("Weekly_GenAI_Hours"), #raw("Primary_Use_Case"), #raw("Prompt_Engineering_Skill"), #raw("Tool_Diversity"), #raw("Paid_Subscription"), #raw("Perceived_AI_Dependency") and #raw("Institutional_Policy"). Comparing context-only, AI-only and combined models made the research question directly testable.

Four fields were excluded from all predictors. #raw("Student_ID") was an identifier without a defensible substantive meaning. #raw("Post_Semester_GPA") was used to construct the target and would reveal its outcome. #raw("Skill_Retention_Score") and #raw("Burnout_Risk_Level") were separate post-semester outcomes. Their removal was a deliberate leakage control rather than optional feature selection.

== Experimental procedure

The analysis was implemented in Python 3.13.11 with pandas 3.0.3, NumPy 2.4.6 and scikit-learn 1.9.0 (Pedregosa et al., 2011). Matplotlib 3.10.9 and seaborn 0.13.2 generated the figures. A fixed random state of 42 was used. A single random 80/20 split produced 40,000 development records and a reserved test set of 10,000 records. All model selection was performed within the development data using shuffled five-fold cross-validation with the same folds for every model. This consistent protocol was important because student-performance prediction studies often differ in targets, data and evaluation choices, making disciplined within-study comparison more informative than isolated scores (Alyahyan & Düştegör, 2020; Hellas et al., 2018).

Preprocessing and estimation were joined in scikit-learn pipelines. Numeric features passed through median imputation and standardisation; categorical and Boolean features passed through most-frequent imputation and one-hot encoding with unknown categories ignored. Although the observed file had no missing values, these steps made the workflow robust to missing or unseen values. Crucially, transformer parameters were fitted within each training fold, not on the complete dataset.

The candidate set comprised a mean dummy baseline, ordinary least-squares Linear Regression, Ridge Regression, Random Forest and Histogram Gradient Boosting (HGB). Mean absolute error (MAE) reported typical absolute error in GPA points. Root mean squared error (RMSE) penalised larger errors more heavily and was the primary selection metric. The coefficient of determination ($R^2$) described the proportion of test-set variation accounted for by the predictions relative to the mean baseline. Lower MAE and RMSE and higher $R^2$ indicate better performance.

HGB was selected for optimisation only after it achieved the lowest untuned cross-validated RMSE. #raw("RandomizedSearchCV") evaluated ten parameter combinations over learning rate, leaf count, minimum leaf size, L2 regularisation and number of boosting iterations. Search, scoring and refitting remained inside the development data. Test outputs were treated as confirmatory: the same reserved partition supported the prespecified feature-set comparison, candidate-model confirmation, residual summaries and permutation importance. It did not alter the search space or trigger model refitting, but these multiple reporting uses mean that it was not a strict single-look test benchmark.

No ethics approval is claimed for the secondary analysis because the dataset was obtained as a public CC0 modelling file and contains only a unique numeric identifier without documented personal meaning. Nevertheless, the source provides no account of consent or ethical review. This absence is an evidence limitation and prevents treating public availability as proof of ethical provenance.

#figure(
  {
    compact-table(size: 9pt)[
      #table(
        columns: (1.1fr, 1fr, 1.55fr),
        align: left + top,
        inset: (x: 4pt, y: 3pt),
        stroke: 0.45pt + rule-grey,
        fill: (x, y) => if y == 0 { pale-grey },
        table.header(
          [Stage],
          [Data used],
          [Purpose],
        ),
        [Integrity checks and target construction],
        [All raw records],
        [Verify schema and define the continuous outcome],
        [Development-test split],
        [All eligible records],
        [Reserve 20% for final confirmation],
        [Five-fold comparison],
        [Development data only],
        [Select the strongest model family],
        [Randomised tuning],
        [Development folds only],
        [Optimise the selected HGB family],
        [Final evaluation],
        [Reserved test set],
        [Confirm generalisation and inspect errors],
        [Permutation importance],
        [Reserved test set],
        [Describe model-specific predictive contribution],
      )
    ]
  },
  caption: [Experimental workflow and evidence role],
  kind: table,
)

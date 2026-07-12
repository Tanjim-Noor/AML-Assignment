# Dataset Preparation

## Data understanding, audit and target construction

The raw CSV was loaded without modification. It contained 50,000 rows and 16
source columns: eight numeric or ordinal measures, six categorical fields, one
Boolean field and one integer identifier. The fields covered academic
background, study behaviour, generative-AI use, institutional policy, exam
anxiety and post-semester outcomes (Nagi sisiro, 2026).

Every field was profiled for data type, non-null count, missing count,
cardinality and, where applicable, numeric range. The audit found 50,000 unique
student identifiers, no missing cells, no duplicated rows and no duplicated
identifiers. Both GPA fields were within 0--4; weekly AI and traditional-study
hours were within feasible weekly limits; and diversity, dependency, anxiety
and retention measures stayed within their documented scale limits. Complete
category-frequency tables exposed every observed level and no inconsistent
spellings. Figure 5 summarises the quality checks and field types.

![Figure 1. Data-quality results and original field-type composition. Zero counts for missing cells, duplicate rows, duplicate identifiers and invalid-range rows document why no corrective cleaning was applied.](../assets/fig01_data_quality_and_schema.png)

Numeric exploration reported descriptive statistics, distributions and IQR
outlier flags for every measured field (Figure 6). Flags prompted inspection,
not automatic deletion. Figure 7 reports every categorical and Boolean
frequency before encoding.

![Figure 2. Distributions of all original numeric and ordinal measures except the unique student identifier.](../assets/fig02_numeric_distributions.png)

![Figure 3. Frequency distributions for every categorical and Boolean source field.](../assets/fig03_categorical_distributions.png)

`GPA_Change` was derived as post-semester minus pre-semester GPA, increasing
the in-memory working table to 17 columns without changing the raw file. The
target mean was 0.2032 GPA points, its standard deviation was 0.1872 and its
median was 0.2040, with values from -0.924 to 1.008. Figure 8 presents numeric
correlations and the bounded relationship between previous GPA and GPA change.
These correlations support exploration of predictive structure but do not
establish causation.

![Figure 4. Numeric correlation matrix and sampled relationship between previous GPA and GPA change. Post-semester outcomes are excluded from the predictor-focused matrix.](../assets/fig04_correlation_and_target_relationships.png)

There were 43,759 positive changes (87.52%), 6,192 negative changes (12.38%)
and 49 unchanged records (0.10%). Figure 9 makes this asymmetry explicit. It is
not conventional class imbalance because the model predicts a continuous
quantity rather than an increase/decrease class. Resampling by sign would
change the observed target distribution and regression estimand. All records
were therefore retained, while direction-specific test errors were added to
detect performance differences hidden by aggregate metrics.

![Figure 5. Counts and continuous distributions of GPA decreases, unchanged values and increases. The continuous target was retained without balancing.](../assets/fig05_gpa_direction_imbalance.png)

Figure 1 shows an approximately unimodal target, a GPA-ceiling relationship,
prompt-skill differences and non-monotonic AI-hours quartiles. These unadjusted
patterns support nonlinear modelling but do not identify causal effects.

![Figure 6. Distribution of GPA change and descriptive relationships with previous GPA, prompt-engineering skill and weekly generative-AI hours. Error bars show 95% confidence intervals for group means.](../assets/fig06_gpa_change_eda.png)

## Preparation and leakage control

Table 4 records every preparation decision. `Student_ID` was excluded because
record identity has no transferable meaning. `Post_Semester_GPA` was used only
to construct the target; retaining it as a predictor would reveal the answer.
`Skill_Retention_Score` and `Burnout_Risk_Level` were excluded as separate
post-semester outcomes unavailable at the intended prediction point.
`AI_Hours_Quartile` and `GPA_Direction` were diagnostic fields only; models
retained continuous hours and continuous GPA change.

**Table 4. Dataset preparation decisions**

| Action | Fields or rule | Rationale |
|---|---|---|
| Construct target | Post-GPA minus pre-GPA | Preserve magnitude and direction of academic change |
| Remove identifier | `Student_ID` | Avoid arbitrary record identity |
| Remove target source | `Post_Semester_GPA` | Prevent direct outcome leakage |
| Remove other outcomes | `Skill_Retention_Score`, `Burnout_Risk_Level` | Preserve a predictor-only feature set |
| Audit validity | Missingness, duplicates, ranges, categories, IQR flags | Demonstrate cleaning decisions from evidence |
| Encode categories | Fold-fitted one-hot encoding; ignore unknown levels | Represent nominal values without artificial ordering |
| Prepare numeric fields | Fold-fitted median imputation and standardisation | Provide robustness and linear-model comparability |
| Retain clean observations | No deletion, fabrication or forced transformation | Preserve valid supplied data |
| Retain target distribution | No balancing by GPA-change sign | Preserve the continuous regression estimand |
| Add direction diagnostic | `GPA_Direction`, evaluation only | Detect unequal errors hidden by overall averages |

Encoders, imputers and scaling remained inside model pipelines, so every fold
learned transformations from training data only. No imputation was activated,
but the pipeline defines future missing-value handling without manufacturing
present defects.

Complete cleaning was demonstrated through audits, validity rules and the
decision log; it does not require changing valid data. Kaggle does not document
collection, sampling, ethics or whether records are observed or synthetic.
Perfect cleanliness is therefore a provenance warning, not proof of quality.

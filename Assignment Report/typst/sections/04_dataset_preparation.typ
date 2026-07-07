#import "../template.typ": *

= Dataset Preparation

== Dataset audit and target construction

The raw CSV was loaded without modification. It contained 50,000 rows and 16 columns: eight numeric or ordinal measures, six categorical fields, one Boolean field and one integer identifier. The source covered academic background, study behaviour, generative-AI use, institutional policy, exam anxiety and post-semester outcomes (Nagi sisiro, 2026). Initial checks found 50,000 unique student identifiers, no missing cells and no duplicated source rows. Category spellings and numeric boundaries were also internally consistent. The derived #raw("GPA_Change") column increased the working table to 17 columns but was not written back to the raw file.

The target had a mean of 0.2032 GPA points and a standard deviation of 0.1872. Its median was 0.2040, with values from -0.924 to 1.008. There were 43,759 positive changes and 6,192 negative changes; the remaining 49 records were exactly zero. Consequently, the regression target covered both improvement and decline but was centred above zero. No class-balancing method was applied because the model predicted a continuous value rather than a categorical increase/decline label. Resampling the sign of change would have altered the observed regression distribution without answering the stated question.

As shown in Figure 1, GPA change was approximately unimodal, while its relation to previous GPA had a bounded shape partly imposed by the 4.0 maximum for post-semester GPA. Mean change also differed descriptively by prompt skill: 0.2481 for advanced, 0.1869 for intermediate and 0.1852 for beginner records. The weekly AI-hours quartiles were non-monotonic. Mean change rose from 0.1881 in the lowest quartile to 0.2055 and 0.2287 in the two middle groups, then fell to 0.1905 in the highest-use group. These unadjusted patterns supported testing nonlinear models but did not identify causal effects.

#figure(
  image("../../assets/fig01_gpa_change_eda.png", width: 100%),
  caption: [Distribution of GPA change and descriptive relationships with previous GPA, prompt-engineering skill and weekly generative-AI hours. Error bars in the lower-right panel show 95% confidence intervals for the group means.],
)

== Preparation and leakage control

Table 4 distinguishes each preparation action from its modelling purpose. #raw("Student_ID") was removed because uniqueness does not make an identifier informative. #raw("Post_Semester_GPA") was excluded because the target was calculated from it; including it would allow the model to reconstruct the answer. #raw("Skill_Retention_Score") and #raw("Burnout_Risk_Level") were excluded because they were separate post-semester outcomes and could convey information unavailable at the intended prediction point. The temporary AI-hours quartile was used for EDA only; the models retained the original continuous hours field.

#figure(
  {
    compact-table(size: 9pt)[
      #table(
        columns: (1fr, 1.4fr, 1.9fr),
        align: left + top,
        inset: (x: 4pt, y: 3pt),
        stroke: 0.45pt + rule-grey,
        fill: (x, y) => if y == 0 { pale-grey },
        table.header(
          [Action],
          [Fields or rule],
          [Rationale],
        ),
        [Construct target],
        [Post-GPA minus pre-GPA],
        [Preserve the magnitude and direction of academic change],
        [Remove identifier],
        [#raw("Student_ID")],
        [Avoid learning arbitrary record identity],
        [Remove target source],
        [#raw("Post_Semester_GPA")],
        [Prevent direct outcome leakage],
        [Remove other outcomes],
        [#raw("Skill_Retention_Score"), #raw("Burnout_Risk_Level")],
        [Preserve a predictor-only feature set],
        [Encode categories],
        [One-hot encoding; ignore unknown levels],
        [Represent nominal values without artificial ordering],
        [Scale numeric fields],
        [Standardisation fitted within folds],
        [Place numeric inputs on a consistent scale for linear models],
        [Retain clean observations],
        [No rows deleted or values fabricated],
        [Reflect the supplied data faithfully],
      )
    ]
  },
  caption: [Dataset preparation decisions],
  kind: table,
)

The categorical encoders, imputers and scaler were placed inside each model pipeline. Therefore, fold validation learned preprocessing statistics only from the corresponding training partition. This avoids the optimistic bias that can arise when transformation parameters are estimated before cross-validation.

The principal limitation of this preparation is the file's perfect cleanliness. The assignment brief prefers data that require substantive cleaning, yet this dataset contained no missing or duplicate records. Inventing defects would have weakened integrity, so none were introduced. More importantly, Kaggle does not document the collection instrument, sampling frame, institution, geography, observation dates, ethics process or whether records are observed or synthetic. Perfect cleanliness therefore remains a provenance warning rather than evidence of exceptional measurement quality.

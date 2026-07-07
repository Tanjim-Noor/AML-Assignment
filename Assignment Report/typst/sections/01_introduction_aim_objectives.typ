#import "../template.typ": *

= Introduction, Aim and Objectives

== Problem context

Generative artificial intelligence (GenAI) tools can produce explanations, drafts, summaries, code and feedback in response to natural-language prompts. Their rapid adoption has moved educational AI beyond systems selected by an institution: students can now decide whether, why and how intensively to use such tools. Earlier higher-education research already treated profiling and prediction as major AI applications (Zawacki-Richter et al., 2019), while more recent reviews identify prediction, assessment, tutoring and AI assistance across the field (Crompton & Burke, 2023). GenAI adds a difficult question to this landscape: do recorded differences in student use help explain or predict academic outcomes after conventional study context is considered?

Academic performance is often represented by grade point average (GPA). Raw post-semester GPA, however, is strongly related to previous GPA and can make a model appear successful without explaining academic change. In this report, #emph[GPA change]​ refers to post-semester GPA minus pre-semester GPA. A positive number indicates improvement and a negative number indicates decline. Predicting this continuous difference retains both direction and magnitude, whereas a binary “improved/not improved” label would treat a change of 0.02 as equivalent to a change of 0.80.

The educational literature does not justify assuming that greater AI exposure will improve performance. Early reviews describe opportunities for tutoring, feedback and independent study but also identify inaccuracy, over-reliance and academic-integrity risks (Kasneci et al., 2023; Lo, 2023). Empirical results also depend on how use and performance are measured. It is therefore more defensible to ask whether AI-related fields contain #emph[predictive information]​ than whether AI use #emph[caused]​ GPA change.

== Dataset and analytical problem

The analysis used the Kaggle #emph[Impact of Ai on Students]​ dataset (Nagi sisiro, 2026). It contains 50,000 student records and 16 source columns covering major, year of study, previous GPA, conventional study hours, exam anxiety, weekly GenAI hours, use case, prompt skill, tool diversity, subscription, perceived dependency, institutional policy and post-semester outcomes. The file is large, mixed-type and suitable for comparing regression algorithms.

Its strengths are accompanied by substantial limitations. Kaggle does not document the institution, country, sampling design, collection instrument, observation period, ethics procedure or whether the records are observed or synthetic. The file also has no missing values or duplicate rows, despite the assignment's preference for an imperfect dataset. These conditions make it appropriate for demonstrating a rigorous machine-learning workflow, but not for estimating population prevalence or recommending that students change AI use to alter GPA.

The modelling problem was designed around leakage control. The derived #raw("GPA_Change") target could be reconstructed if #raw("Post_Semester_GPA") were retained as a predictor, so that field was excluded. #raw("Student_ID") and the separate post-semester outcomes #raw("Skill_Retention_Score") and #raw("Burnout_Risk_Level") were also removed. Context variables and AI variables were compared separately and together, then five candidate regressors were evaluated using a common development-test split and five-fold cross-validation.

== Research question

#report-quote[To what extent do AI-usage variables improve out-of-sample prediction of semester GPA change beyond previous GPA and general study context, and which regression model provides the strongest validated performance?]

This wording sets two boundaries. “Out-of-sample” requires evaluation on rows not used to fit the corresponding model. “Prediction” limits the conclusion to associations within the supplied data.

== Aim

The primary aim of this study was to build and critically evaluate leakage-controlled regression models for semester GPA change, with particular attention to the incremental predictive value of AI-usage variables.

== Objectives

+ Examine the dataset's structure, integrity and GPA-change distribution without modifying the raw CSV or manufacturing data-quality problems.
+ Construct a defensible continuous GPA-change target and define separate context, AI-only and combined predictor groups.
+ Prevent identifier and post-outcome leakage through explicit feature exclusions and fold-local preprocessing.
+ Compare a mean baseline, Linear Regression, Ridge Regression, Random Forest and Histogram Gradient Boosting using consistent five-fold cross-validation.
+ Tune the strongest nonlinear model using development data only and confirm performance on a reserved 20% test set.
+ Interpret residuals, error tolerances and permutation importance against the literature, then make recommendations proportionate to the evidence.

== Scope and contribution

The report covers one regression notebook and excludes the supplementary deep-learning experiments from the reported implementation. Its technical contribution is a reproducible comparison of linear and nonlinear models, an explicit context-versus-AI feature ablation, and a validation hierarchy that uses cross-validation for selection and the test set for confirmation. Its critical contribution is equally important: it connects model results to a structured 15-source literature review while distinguishing predictive association from causal explanation. The following sections first synthesise the evidence base, then describe preparation, implementation and validation before analysing the findings and their practical limits.

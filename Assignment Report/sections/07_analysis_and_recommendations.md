# Analysis and Recommendations

## Answer to the research question

The clearest finding to emerge from the analysis is that AI-use variables added
out-of-sample predictive information when combined with previous GPA and
general study context. As Table 8 shows, the context-only HGB model achieved
test $R^2=0.2382$, while AI variables alone achieved 0.1703. Combining the two
groups raised test $R^2$ to 0.4170 and reduced RMSE from 0.1618 to 0.1415
relative to context alone. The $R^2$ increment was 0.1788. This is a change in
predictive performance, not a percentage increase in GPA and not an estimate
of an AI effect.

**Table 8. HGB feature-set comparison**

| Feature set | CV MAE | CV RMSE | CV $R^2$ | Test MAE | Test RMSE | Test $R^2$ |
|---|---:|---:|---:|---:|---:|---:|
| Context only | 0.1254 | 0.1638 | 0.2378 | 0.1239 | 0.1618 | 0.2382 |
| AI variables only | 0.1356 | 0.1708 | 0.1708 | 0.1347 | 0.1689 | 0.1703 |
| Context and AI variables | **0.1129** | **0.1443** | **0.4084** | **0.1114** | **0.1415** | **0.4170** |

AI variables were therefore informative but insufficient by themselves. The
strongest prediction required academic context and AI-related behaviour
together. This result is consistent with the wider literature's emphasis on
context and quality of use. AI literacy includes understanding, application,
evaluation and ethics rather than exposure alone (Ng et al., 2021), while
effective prompting also depends on domain knowledge and critical checking
(Lee & Palmer, 2025). The result should not be interpreted as validating the
dataset's self-described skill measure; it only shows that the recorded AI
fields helped this model discriminate between outcomes.

## Why nonlinear models performed better

HGB and Random Forest outperformed Linear and Ridge Regression under the same
folds and preprocessing. The tuned HGB test RMSE was 0.1414, compared with
0.1448 for Random Forest and 0.1583 for both linear models. This suggests that
one additive coefficient per encoded feature did not capture all useful
structure. Two descriptive findings support that interpretation. First, mean
GPA change rose through the high-medium AI-hours quartile and then fell in the
highest quartile. Second, the maximum feasible increase narrows as previous GPA
approaches 4.0. Tree ensembles can represent thresholds and interactions
without imposing a single straight-line relationship.

This pattern aligns cautiously with educational-data-mining evidence in which
tree-based and other nonlinear models have performed competitively (Yağcı,
2022). It does not show that HGB is universally preferable: Waheed et al.
(2020), for example, reported a deep model as strongest for a different
classification task using virtual-learning data. Model ranking is conditional
on the outcome, features, sample and validation protocol.

The optimisation result is also instructive. Randomised search improved HGB
cross-validated RMSE from 0.1443 to 0.1441 and test $R^2$ from 0.4166 to 0.4185
relative to the untuned HGB. The gain was genuine within the recorded run but
small. Tuning therefore refined an already suitable model rather than
transforming performance. This supports explicit optimisation while cautioning
against presenting search as inherently valuable irrespective of its measured
benefit.

## Predictive importance and anomalies

Figure 4 shows that `Traditional_Study_Hours` had the largest permutation
importance (0.0328 increase in RMSE-based loss when shuffled), followed by
`Primary_Use_Case` (0.0267), `Weekly_GenAI_Hours` (0.0174),
`Year_of_Study` (0.0136), `Prompt_Engineering_Skill` (0.0122) and
`Pre_Semester_GPA` (0.0108). Institutional policy and paid subscription made
small contributions, while tool diversity, perceived dependency, exam anxiety
and major category were near zero in this fitted model.

![Figure 10. Test-set permutation importance for the selected tuned HGB model. Values show the mean deterioration in RMSE-based score after shuffling each source feature across five repetitions.](../assets/fig10_permutation_importance.png)

Traditional study hours ranking above any AI field is substantively important:
AI behaviour did not replace conventional study context. At the same time,
purpose of use ranking above weekly hours supports the argument that how a tool
is used may be more informative than exposure quantity. The non-monotonic
quartile pattern further rejects the simplistic recommendation that more hours
should improve GPA.

These importance values do not isolate independent effects. Correlated features
can substitute for one another when shuffled, and a variable may be useful
because it proxies an unobserved factor. The near-zero importance of perceived
dependency, for instance, does not establish that dependency is educationally
irrelevant. It means only that shuffling this field did not materially worsen
this model's test score after the other recorded predictors were available.

## Relationship to prior evidence

Taken together, the results fit the literature's mixed rather than
deterministic account of GenAI. Sun and Zhou (2024) found positive average
effects in structured interventions, whereas Abbas et al. (2024) reported
adverse associations in observational survey data. Molerov et al. (2026) found
faster task completion and more examinations passed among users, but no better
task accuracy or grades. The current model neither confirms nor refutes those
effects because it uses different measures and has no intervention or credible
control group. Its contribution is narrower: use-related fields improved
prediction within the supplied records, and the form of the association was
not simply monotonic.

The final $R^2$ of 0.4185 left most test variation unexplained. Missing course,
assessment, instructor and socioeconomic context plus extreme-outcome
compression require caution.

Direction-specific validation revealed the clearest practical bias risk. Test
MAE for GPA decreases (0.1979) was nearly twice that for increases (0.0993),
and the mean residual of -0.1916 shows that declines were systematically
predicted as less severe. This behaviour is consistent with the 87.52% positive
target share and central prediction compression. The result does not justify
changing the observed distribution, but it prevents the near-zero overall mean
residual from being presented as evidence of equal performance.

## Recommendations

First, the tuned HGB should be retained as the assignment's predictive
benchmark because it led both cross-validation and test evaluation. It should
not be deployed as an intervention rule or used to label individual students
as likely to benefit from AI. At most, its outputs could support hypothesis
generation after independent validation. Any later deployment study must set
direction-specific acceptance thresholds and examine errors across documented
demographic and institutional groups that are absent from this file.

Second, future data collection should document the institution, sampling frame,
time period, consent, collection instrument and real-versus-synthetic status.
Verified behavioural logs should be distinguished from self-report. Course,
assessment and instructor variables should be added because they offer
plausible explanations for the unexplained variance.

Third, future analysis should predefine a genuine low-use or non-use comparison
and follow students longitudinally if the objective changes from prediction to
effect estimation. External validation on a separately collected cohort is
more valuable than increasingly extensive tuning of the present file.

Finally, educational recommendations should emphasise purposeful and critical
use rather than maximising AI hours. Teaching should combine prompt practice
with subject knowledge, output verification and ethical judgement, consistent
with AI-literacy research (Laupichler et al., 2022; Lee & Palmer, 2025).
Whether such support improves GPA requires controlled evaluation; it cannot be
inferred from the present feature importances.

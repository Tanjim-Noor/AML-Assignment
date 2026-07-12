# Related Works

## Review method

A structured multi-database search was conducted on 1 July 2026 to identify
work relevant to generative-AI use, academic outcomes, AI literacy and
student-performance prediction in higher education. Four query families
combined: (1) generative AI or ChatGPT with academic performance; (2) AI-use
behaviour, prompt engineering or AI literacy with student outcomes; (3) machine
learning with GPA or academic-performance prediction; and (4) the exact Kaggle
dataset title, filename and creator. Searches were run through ERIC and
Crossref, supplemented by public Semantic Scholar result pages and publisher or
DOI records. OpenAlex was attempted but its anonymous API required an API key or
returned a rate-limit response; this was recorded as unavailable rather than
interpreted as no evidence.

English publications from 2016 to 2026 were prioritised, with emphasis on work
published after 2022 for generative AI. Eligible records included empirical
higher-education studies, relevant reviews and methodological sources that
could support model design or validation. Promotional material, unverifiable
records, school-only studies, perception studies without a relevant outcome and
duplicates were excluded. Records were deduplicated by DOI and normalised
title. The review inspected 50 discovery records, verified 15 domain records
by DOI, title, author and year, and retained them as the problem-focused core.
Ten primary software or methodological publications were then verified to
document tools, algorithms, tuning, validation and interpretation used in the
implementation.
The exact-dataset search located the Kaggle metadata but no inspectable
peer-reviewed benchmark. The review is therefore reproducible and systematic
in its search logic, but it is not presented as a complete PRISMA systematic
review.

**Table 1. Search coverage and screening outcome**

| Source | Search role | Records inspected | Core records retained |
|---|---|---:|---:|
| ERIC | All four query families | 17 | 10 before cross-database deduplication |
| Crossref | Broad discovery and targeted DOI verification | 20 broad results plus 15 DOI checks | 15 verified DOI records |
| Semantic Scholar | Supplementary public-result discovery | 13 | 3 before deduplication |
| OpenAlex | Planned discovery source | 0 | 0; access unavailable |
| Kaggle | Exact dataset and notebook search | Dataset metadata only | Dataset source; no comparative study |

Counts overlap because studies appeared through several routes. Degraded API
access was recorded rather than interpreted as negative evidence, and no
Kaggle notebook was admitted without inspectable methods and results.

Quality appraisal covered design, sample, outcome, validation, leakage,
self-reporting and causal overreach. It prevented pooled effects,
classification accuracy and observational associations from being transferred
uncritically to this regression.

## AI in higher education

A considerable body of literature has examined artificial intelligence in
higher education, although the focus has changed quickly. Zawacki-Richter et
al. (2019) reviewed 146 studies published between 2007 and 2018 and grouped
applications into profiling and prediction, assessment and evaluation,
adaptive systems and personalisation, and intelligent tutoring. Their review
also identified limited involvement of educators and limited attention to
pedagogical and ethical questions. Crompton and Burke (2023) subsequently
reviewed 138 studies from 2016 to 2022 and found prominent uses in prediction,
assessment, AI assistance, tutoring and learning management. Together, these
reviews establish student prediction as a longstanding application, but they
largely precede widespread student access to generative AI.

The release of general-purpose conversational systems expanded the research
problem from institutional analytics to student-controlled use. Lo's (2023)
rapid review identified opportunities for tutoring, feedback and independent
study alongside risks involving accuracy, academic integrity and over-reliance.
Kasneci et al. (2023) similarly argued that large language models could support
personalisation and feedback, but stressed reliability, bias, assessment and
dependency. These sources justify examining AI use as a multidimensional
context rather than assuming that use is uniformly beneficial or harmful.
However, both reflect an early evidence base in which conceptual discussion was
more developed than direct measurement of academic outcomes.

## Mixed evidence on academic outcomes

Empirical findings do not support a simple relationship between “more AI” and
better performance. Sun and Zhou's (2024) meta-analysis synthesised 65
independent studies from 28 articles and reported a medium positive pooled
effect on academic achievement ($g=0.533$). The effect varied across learning
activities, content and samples, and the intervention designs differed from
uncontrolled everyday use. The pooled result therefore supports the potential
value of structured GenAI-assisted learning, not a universal benefit from usage
hours.

By contrast, Abbas et al. (2024) developed a usage scale and analysed a
three-wave survey of 494 university students in Pakistan. Greater reported use
was associated with procrastination, memory loss and lower reported academic
performance. Temporal separation strengthened the measurement design relative
to a one-time survey, but self-reporting, contextual specificity and
observational modelling still prevent a causal conclusion. Molerov et al.
(2026) provide a further qualification using a German higher-education panel
and verified chatbot-use information. Chatbot users completed reasoning tasks
faster but not more accurately; frequent users passed more examinations but did
not obtain better grades. The authors explicitly treated self-selection and
partial cross-sectional comparison as limits.

The generalisability of this evidence is restricted by differing populations,
tasks, exposure definitions and outcome measures. Positive findings are more
common in structured learning interventions, whereas naturally occurring use
may reflect workload, procrastination, prior skill or course demands. These
differences are not contradictions that can be resolved by counting studies.
They indicate that purpose, quality and context of use need to be represented
alongside quantity.

## AI literacy and prompt skill

AI literacy provides one framework for representing use quality. Ng et al.
(2021) synthesised 30 articles and organised AI literacy around understanding,
application, evaluation and creation, together with ethical awareness. This
definition is broader than operational knowledge of a chatbot. Laupichler et
al. (2022) reached a compatible conclusion after screening 902 records and
including 30 studies in higher and adult education. They found that definitions,
curricula and assessment instruments remained immature, limiting consistent
measurement.

Prompt engineering is one component within this broader capability. Lee and
Palmer's (2025) systematic review of 33 articles found that prompting can be
learnt, but effective practice also requires domain knowledge, critical
evaluation and iterative refinement. The participant base and success criteria
in the literature were limited and heterogeneous. Consequently, a categorical
`Prompt_Engineering_Skill` field can be a plausible predictor, but it should
not be treated as a validated measure of comprehensive AI literacy. The present
dataset also includes purpose of use, weekly hours, tool diversity, paid access,
dependency and institutional policy, allowing a more contextual representation
than hours alone.

## Predicting academic performance

Student-performance prediction is methodologically diverse. Alyahyan and
Düştegör (2020) argued that a useful study begins with a precise outcome and
aligns feature selection, preprocessing, algorithm choice and evaluation with
that outcome. Hellas et al. (2018), reviewing 357 studies, found growth in both
predictors and algorithms but recurring weaknesses in reporting, validation
and replication. These findings support the present focus on change in GPA
rather than raw post-semester GPA, because the former asks a more specific
question and reduces the dominance of previous attainment.

Primary studies show that behavioural and contextual data can support
prediction, although published scores are not directly comparable. Waheed et
al. (2020) used demographics, assessments and virtual-learning-environment
clickstream data to predict performance and reported that deep neural models
outperformed their alternatives. Yağcı (2022) compared six algorithms for
final-examination classification among 1,854 university students and found
Random Forest, neural network and support vector machine among the strongest,
with approximately 70–75% accuracy. Both studies concern classification,
different institutions and different inputs. Their accuracy cannot be compared
with RMSE or $R^2$ for GPA-change regression.

Model labels also conceal consequential implementation choices. Probst et al.
(2019) showed that Random Forest behaviour depends on parameters such as
feature sampling, leaf size and tree count, supporting explicit configuration
and tuning reports. More generally, preprocessing and model selection must be
confined to development folds to prevent leakage. This study therefore compares
all candidates on identical folds, reports variation across folds, tunes only
the development data and reserves a test partition for confirmation.

## Methodological and software foundations

The implementation also depends on literature beyond the educational problem
domain. pandas supplied labelled data structures (McKinney, 2010), NumPy
provided numerical arrays (Harris et al., 2020), and scikit-learn supplied the
common estimator, pipeline and evaluation interfaces (Pedregosa et al., 2011).
Matplotlib and seaborn supported reproducible exploratory and statistical
graphics (Hunter, 2007; Waskom, 2021). These sources document tools used to
produce the work; they are cited in Methods rather than treated as evidence
about student outcomes.

Algorithm choice also had literature foundations. Ordinary and Ridge
Regression supplied additive benchmarks, with Ridge adding coefficient
shrinkage for correlated predictors (Hoerl & Kennard, 1970). Random Forest
represented bootstrap-aggregated randomised trees (Breiman, 2001), while
gradient boosting represented stage-wise fitting to residual error (Friedman,
2001). Random search provided a reproducible, budget-limited alternative to an
exhaustive grid (Bergstra & Bengio, 2012). Cross-validation supported
development-only model selection (Arlot & Celisse, 2010), and permutation
importance was interpreted as fitted-model reliance rather than causal effect
(Fisher et al., 2019). Method citations also appear where each choice is used.

## Comparative synthesis and research gap

**Table 2. Core literature informing the study**

| Source | Design and context | Main contribution | Limitation and relevance |
|---|---|---|---|
| Zawacki-Richter et al. (2019) | Systematic review; 146 higher-education studies | Established prediction as a major AI application | Predates GenAI; motivates educational and ethical scrutiny |
| Crompton and Burke (2023) | Systematic review; 138 studies | Mapped contemporary AI uses in higher education | Search ended as ChatGPT emerged |
| Lo (2023) | Rapid review; 50 publications | Synthesised early ChatGPT opportunities and risks | Early literature was often conceptual |
| Kasneci et al. (2023) | Multidisciplinary position paper | Connected learning support with reliability and dependency risks | No direct performance effect estimate |
| Abbas et al. (2024) | Scale study and three-wave survey; Pakistan | Linked reported use with adverse academic correlates | Self-report and observational design |
| Sun and Zhou (2024) | Meta-analysis; 65 studies, 1,909 participants | Reported a positive pooled achievement effect | Heterogeneous, mainly structured interventions |
| Molerov et al. (2026) | Panel/quasi-experimental assessment; Germany, $N=270$ | Faster completion but not higher task accuracy or grades | Self-selection and limited causal identification |
| Ng et al. (2021) | Exploratory review; 30 articles | Defined AI literacy as understanding, use, evaluation, creation and ethics | Conceptual framework, not a validated measure |
| Laupichler et al. (2022) | Scoping review; 30 included studies | Found immature definitions and assessment of AI literacy | Broad, heterogeneous evidence |
| Lee and Palmer (2025) | Systematic review; 33 articles | Framed prompting as iterative and knowledge-dependent | Small participant base and subjective criteria |
| Alyahyan and Düştegör (2020) | Review and best-practice framework | Emphasised target definition and end-to-end design choices | Source studies used incompatible outcomes |
| Hellas et al. (2018) | Systematic review; 357 studies | Identified validation and reporting weaknesses | Broad educational contexts |
| Waheed et al. (2020) | VLE classification experiment | Demonstrated value of behavioural and prior-assessment data | Different target, setting and metric |
| Yağcı (2022) | Six-model classification comparison; $N=1,854$ | Showed competitive nonlinear models in one course | Accuracy not comparable with regression error |
| Probst et al. (2019) | Methodological review | Explained ensemble parameter and tuning effects | Not education-specific |
| Breiman (2001); Friedman (2001) | Primary ensemble-method papers | Grounded Random Forest and gradient boosting choices | General methods, not educational evidence |
| Arlot and Celisse (2010); Bergstra and Bengio (2012) | Methodological studies | Supported cross-validation and random search | Procedures still depend on suitable splits and search spaces |
| Fisher et al. (2019) | Model-reliance methodology | Supported permutation-based interpretation | Importance remains model- and correlation-dependent |

*Note.* AI = artificial intelligence; GenAI = generative artificial
intelligence; VLE = virtual learning environment. The outcomes and metrics
summarised in this table are methodologically informative but are not direct
numerical benchmarks for GPA-change regression.

Table 2 shows a clear gap between the GenAI-outcomes literature and the
student-prediction literature. The former asks whether or how AI relates to
learning but often relies on self-report, interventions or broad achievement
measures. The latter develops predictive models but usually omits detailed
GenAI behaviours and frequently uses classification targets. No defensible
analysis using the exact Kaggle dataset was located. It would therefore be
misleading to manufacture a same-dataset benchmark.

The present work addresses a narrower gap: it tests whether AI-use variables
add held-out predictive information beyond previous GPA and general study
context, while comparing linear and nonlinear regressors under a common,
leakage-controlled validation procedure. This does not resolve whether AI use
improves learning. Its contribution is to separate incremental prediction from
causal interpretation and to show how a contemporary but provenance-opaque
dataset can be analysed without overstating its evidential value.

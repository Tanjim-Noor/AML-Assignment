# Dataset Selection Rubric and Final Dataset Decision

Last updated: 2026-06-02

Requirement sources:

- `Assignment Requirements/CT046-3-M-AML_Assignment Question.md`
- `Assignment Requirements/CT046-3-M-AML_Assignment Marking Scheme and Minimum Document Requirements.md`

## Final Decision

Select **Global Urban Air Quality & Pollution Time-Series** as the primary final assignment dataset.

Backup: **AI Workforce Displacement 2020-2026**.

Do not use **LLM Hallucination** or **Student AI Tools vs Exam Scores** as the main final dataset. They are useful for lab practice or appendix discussion, but they are too small for a highest-distinction final AML assignment.

Frozen problem statement:

> Predict and explain hazardous urban air-quality events and PM2.5/AQI trends across global cities using hourly pollutant, city, location, and time-series features.

Recommended final task design:

- Primary supervised task: forecast or classify future `Hazardous_Event` risk using time-aware features and a no-`European_AQI` feature set.
- Secondary supervised task: predict `PM2_5_ug_m3` or `European_AQI` using regression or forecasting.
- Unsupervised task: cluster city-hour pollution profiles to support interpretation and recommendations.

## Rubric Derived From The Assessment

The assignment rewards a dataset that can support the whole report, not just model accuracy. The scoring below maps the assignment requirements and marking scheme into dataset-selection criteria.

| Criterion | Weight | Highest-distinction dataset evidence |
| --- | ---: | --- |
| Assignment fit | 20 | Reasonably large dataset, mixed categorical and numeric variables, more than 12 variables, not perfectly clean, not an overused toy dataset, and enough complexity for meaningful preprocessing. |
| Problem and related-works strength | 20 | Clear real-world problem, strong aim/objectives, enough recent literature after 2016, multiple source types, and comparable methods or Kaggle notebooks for discussion. |
| ML implementation depth | 25 | Supports at least 3 appropriate tuned models, feature engineering, interpretable model outputs, and preferably classification plus regression/forecasting or clustering. |
| Validation strength | 20 | Allows appropriate validation design, meaningful metrics, leakage control, imbalance handling, and statistically acceptable model comparison. |
| Analysis and recommendation potential | 15 | Produces interpretable findings, strong tables/graphs, critical discussion, anomaly analysis, comparison with related work, and practical recommendations. |

Hard demotion rules:

- Fewer than 12 variables: demote strongly unless there is a compelling advanced modeling reason.
- Very small row count: demote strongly because validation and model comparison become weak.
- Perfectly clean or trivial target: demote unless stronger feature engineering creates a non-trivial problem.
- Weak related-work support: demote because Part A carries 40%.
- Synthetic-only conclusions: demote for real-world recommendations unless the report clearly frames the work as scenario modeling.

## Scored Candidate Matrix

| Rank | Dataset | Assignment fit /20 | Related works /20 | ML depth /25 | Validation /20 | Analysis /15 | Total /100 | Decision |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | Global Urban Air Quality & Pollution Time-Series | 18 | 19 | 24 | 19 | 14 | **91** | Select as final dataset. |
| 2 | AI Workforce Displacement 2020-2026 | 17 | 16 | 21 | 15 | 11 | **79** | Keep as backup. |
| 3 | LLM Hallucination | 5 | 18 | 13 | 7 | 12 | **55** | Lab/appendix only. |
| 4 | Student AI Tools vs Exam Scores | 3 | 8 | 9 | 5 | 6 | **32** | Lab practice only. |

### Why Global Urban Air Quality Wins

- It has 254,736 rows, 13 columns, mixed categorical/time/geospatial/numeric variables, a natural binary hazard target, and only light missingness.
- It supports multiple high-mark tasks: hazardous-event classification, PM2.5/AQI regression or forecasting, and city/pollution clustering.
- It has strong validation options: chronological split, city-aware analysis, imbalance-aware metrics, and leakage-control experiments.
- It has a stronger related-work base than the other local datasets, including PM2.5 prediction, air-quality forecasting, hazardous/exceedance classification, public-health motivation, and AQI/pollutant references.

Important caution:

- The full dataset is larger than the assignment's 20k-50k guideline. Use the full dataset for EDA if practical, but define a justified modeling subset if runtime becomes a problem. A good subset is still chronological and city-balanced, not random convenience sampling.
- If predicting `Hazardous_Event`, do not use `European_AQI` in the primary model because it may leak the target. Use a no-AQI feature set as the main reported result. A separate leakage demonstration may be useful in an appendix.

### Why AI Workforce Is Backup

- It fits the size and variable guidance well: 20,800 rows and 23 columns.
- It supports regression, classification through engineered risk labels, clustering, and time-aware validation.
- Its main weakness is that the local README identifies it as synthetic scenario data. That limits real-world claims, related-work comparison on the same dataset, and practical recommendations.

### Why The Other Two Are Not Final Candidates

- LLM Hallucination has an interesting topic and strong literature potential, but only 200 rows. Validation would be fragile and NLP modeling could become more about text-feature tricks than a complete AML workflow.
- Student AI Tools vs Exam Scores has only 100 rows and 9 columns. It is too small and too simple for a distinction-level final assignment.

## Literature Feasibility Check

Web checked on 2026-06-02. The goal was not to complete the full literature review, but to confirm whether each shortlisted dataset can support the required 10-15 recent references and a defensible related-work section.

### Global Urban Air Quality: Feasibility Pass

This topic has enough recent and credible material for a strong Part A. The source pool supports public-health motivation, pollutant definitions, AQI interpretation, PM2.5 forecasting, exceedance/hazard classification, model comparison, and time-series validation.

Seed references and how to use them:

| Source | Use in report |
| --- | --- |
| [WHO ambient outdoor air pollution fact sheet](https://www.who.int/news-room/fact-sheets/detail/ambient-%28outdoor%29-air-quality-and-health) | Public-health motivation and PM2.5 risk framing. |
| [European Air Quality Index](https://airindex.eea.europa.eu/) | AQI categories, pollutant interpretation, and report background. |
| [Open-Meteo Air Quality API documentation](https://open-meteo.com/en/docs/air-quality-api) | Dataset provenance context because the Kaggle page reports Open-Meteo aggregation. |
| [Gao et al. 2024, Atmospheric Environment](https://www.sciencedirect.com/science/article/pii/S1352231024000712) | Directly relevant PM2.5 regression and exceedance classification with multiple ML models and metrics. |
| [Time-Series Data-Driven PM2.5 Forecasting, Atmosphere 2025](https://www.mdpi.com/2073-4433/16/3/292) | Recent PM2.5 forecasting review and method framing. |
| [Ensemble-based classification approach for PM2.5 forecasting, Frontiers in Big Data 2023](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2023.1175259/full) | Classification framing and ensemble model comparison. |
| [PM2.5 prediction in South African cities, Frontiers in AI 2023](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1230087/full) | City-level PM2.5 prediction and model comparison in an urban context. |
| [Deep Flexible Sequential model for air pollution forecasting, Scientific Reports 2020](https://www.nature.com/articles/s41598-020-60102-6) | Deep time-series forecasting reference and hourly-data precedent. |
| [Tracking air pollution and CO2 emissions in 13,189 urban areas, Communications Earth & Environment 2025](https://www.nature.com/articles/s43247-025-02270-9) | Global urban air-pollution context and geospatial discussion. |
| [Ensemble-based deep learning for estimating PM2.5 over California, PMC 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7643812/) | High-resolution PM2.5 estimation and uncertainty discussion. |
| [Implementing ML algorithms to predict PM2.5, MDPI 2022](https://www.mdpi.com/2007682) | Conventional ML baseline and comparison reference. |
| [Advancements in air quality monitoring: systematic review, Springer 2025](https://link.springer.com/article/10.1007/s10462-025-11277-9) | Wider AI/IoT monitoring context and systematic-review support. |
| [Interpretable PM2.5 forecasting for urban air quality, arXiv 2026](https://arxiv.org/abs/2603.25495) | Optional recent reference for interpretability and operational forecasting. |

Related-work conclusion:

- This source pool is wide and deep enough for the 25% related-works criterion.
- It also gives direct methods to compare against: logistic regression, SVM/SVR, decision tree, random forest, neural network, gradient boosting, ensemble methods, and time-series/deep-learning models.
- The final report should compare results mainly at the method-pattern level, because the exact Kaggle dataset may not have enough published peer-reviewed results yet.

### AI Workforce Displacement: Feasibility Pass With Caveats

This topic has strong domain literature and official reports, but weaker same-dataset comparability because the local dataset is synthetic.

Seed references and how to use them:

| Source | Use in report |
| --- | --- |
| [World Economic Forum Future of Jobs Report 2025](https://www.weforum.org/reports/the-future-of-jobs-report-2025/) | Workforce transformation, job creation/displacement, skills, and employer-survey context. |
| [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) | AI adoption, enterprise use, workforce-size expectations, and reskilling context. |
| [ILO GenAI labour-market report 2026](https://www.ilo.org/publications/disruption-without-dividend-how-digital-divide-and-task-differences-split) | Global labour-market exposure and development divide framing. |
| [OECD AI and work topic hub](https://www.oecd.org/en/topics/ai-and-work.html) | Policy framing, automation risk, workplace AI, and employment implications. |
| [NBER: How Retrainable are AI-Exposed Workers? 2025](https://www.nber.org/papers/w34174) | Reskilling and transition evidence. |
| [AI-driven labor market displacement 2020-2025, Frontiers 2026](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2026.1815037/full) | Recent displacement evidence framing. |
| [Artificial intelligence's creation and displacement of labor demand, Technological Forecasting and Social Change](https://www.sciencedirect.com/science/article/pii/S004016252400622X) | Direct creation/displacement literature. |
| [Can digital skill protect against job displacement risk caused by AI? 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9642882/) | Digital skills and displacement-risk relationship. |
| [Frey and Osborne 2017](https://www.sciencedirect.com/science/article/pii/S0040162516302244) | Classic automation-risk baseline. |
| [Revisiting the risk of automation 2017](https://www.sciencedirect.com/science/article/abs/pii/S0165176517302811) | Counterpoint showing automation risk can be overestimated. |
| [Artificial Intelligence, Automation and Work, NBER 2018](https://www.nber.org/system/files/working_papers/w24196/w24196.pdf) | Theoretical framing for automation, productivity, and displacement. |
| [Agentic AI and occupational displacement, arXiv 2026](https://arxiv.org/abs/2604.00186) | Optional recent extension for agentic AI exposure. |

Related-work conclusion:

- The topic can support a strong literature review, but the report would need careful wording because model outputs are from a synthetic simulated dataset.
- It is a good backup if the assignment direction must focus on AI and employment, but it is not as strong as air quality for real-world validation and recommendations.

## Final Modeling Acceptance Criteria

Use the selected air-quality dataset only when the final implementation satisfies these acceptance checks:

- The raw CSV is never edited.
- Timestamps are parsed, sorted, and used for chronological validation.
- Missing `PM10_ug_m3` values are handled with a documented method.
- `Hazardous_Event` imbalance is reported and handled through metrics, class weights, threshold tuning, or resampling where appropriate.
- The primary classification model excludes `European_AQI` to reduce target leakage risk.
- At least 3 supervised models are tuned and compared.
- At least one interpretable output is reported, such as feature importance, permutation importance, SHAP-style explanation, coefficient interpretation, or error profile tables.
- Results include tables and graphs that compare models, not only single-model accuracy.
- Recommendations are tied to city, time, pollutant, or risk-pattern findings rather than generic statements.

## Next Implementation Direction

Build the final assignment pipeline around these stages:

1. Data loading and cleaning.
2. Complete EDA and target distribution analysis.
3. Time and lag feature engineering.
4. No-leak hazardous-event classification.
5. PM2.5 or AQI regression/forecasting.
6. City/pollution clustering.
7. Model tuning, validation, and comparison.
8. Report-ready figures, tables, and critical recommendations.

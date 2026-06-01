# AI Workforce Displacement 2020-2026

Metadata and local schema notes for `ai_workforce_displacement_global_2020_2026.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official Kaggle page | https://www.kaggle.com/datasets/alitaqishah/ai-workforce-displacement-20202026 |
| Kaggle title | AI Workforce Displacement 2020-2026 |
| Creator | Syed Ali Taqi (`alitaqishah`) |
| License | CC0-1.0 / Public Domain |
| Version | 1, initial release |
| Last updated on Kaggle | 2026-05-10 |
| Expected update frequency | Quarterly |
| Kaggle usability rating | 1.0 |
| Kaggle activity at review time | 3,969 views, 858 downloads, 42 votes, 15 notebooks |
| Local review date | 2026-06-01 |

## What The Dataset Is

This is a tabular, research-calibrated synthetic dataset about AI-driven labor-market change from 2020 Q1 through 2026 Q2. It covers 80 countries, 10 industry sectors, and 26 quarters. The records connect AI adoption, automation risk, displacement rates, new-role creation rates, wage premiums, layoff announcements, reskilling activity, and government AI-policy scores.

The Kaggle page states that the data is synthetic, not scraped from live systems. It was generated from a deterministic simulation calibrated against published sources such as the WEF Future of Jobs Report 2025, Goldman Sachs generative AI labor-impact reporting, McKinsey State of AI 2025, OECD Employment Outlook 2025, BLS O*NET automation-risk scores, PwC AI Jobs Barometer 2025, IMF World Economic Outlook 2025, and Layoffs.fyi AI-cited layoff tracking.

## Local File Inventory

| File | Rows | Columns | Size | Missing values |
| --- | ---: | ---: | ---: | ---: |
| `ai_workforce_displacement_global_2020_2026.csv` | 20,800 | 23 | 8,642,293 bytes | 0 |

The row count matches the page-level structure: 80 countries x 10 sectors x 26 quarters.

## Coverage

| Field | Local values |
| --- | --- |
| Years | 2020-2026 |
| Quarters | 2020-Q1 to 2026-Q2 |
| Countries | 80 unique countries |
| Regions | 12 unique region labels |
| Income groups | High Income, Upper Middle Income, Lower Middle Income, Low Income |
| Industry sectors | 10 sectors, each with 2,080 records |

Region distribution:

| Region | Rows |
| --- | ---: |
| Europe | 5,200 |
| Latin America | 3,380 |
| Africa | 3,380 |
| Southeast Asia | 2,080 |
| Middle East | 1,820 |
| East Asia | 1,300 |
| South Asia | 1,300 |
| North America | 520 |
| Oceania | 520 |
| Europe/Asia | 520 |
| Central Asia | 520 |
| Middle East/Africa | 260 |

Income-group distribution:

| Income group | Rows |
| --- | ---: |
| High Income | 8,060 |
| Lower Middle Income | 6,240 |
| Upper Middle Income | 5,720 |
| Low Income | 780 |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `record_id` | Integer identifier | 0 | 20,800 | 1 to 20,800 | Row identifier; exclude from modeling. |
| `country` | Categorical text | 0 | 80 | Examples: United States, China, Germany, United Kingdom, Japan, France | Country-level grouping feature; useful for grouped validation. |
| `iso3_code` | Categorical text | 0 | 80 | 3-letter ISO-like codes | Duplicate country identifier; avoid using both country and ISO if multicollinearity matters. |
| `region` | Categorical text | 0 | 12 | See coverage table | Geographic grouping. |
| `income_group` | Categorical text | 0 | 4 | High Income, Upper Middle Income, Lower Middle Income, Low Income | Socioeconomic grouping. |
| `year` | Integer | 0 | 7 | 2020 to 2026 | Time feature. |
| `quarter` | Integer | 0 | 4 | 1 to 4 | Time feature; combine with year for chronological splits. |
| `quarter_label` | Categorical text | 0 | 26 | 2020-Q1 to 2026-Q2 | Convenient period label; can be parsed to ordered time index. |
| `industry_sector` | Categorical text | 0 | 10 | Technology & Software, Finance & Banking, Healthcare & Life Sciences, Manufacturing & Industry, Retail & E-Commerce, Education & Research, Transportation & Logistics, Media & Communications, Administrative & Clerical, Energy & Utilities | Main sector grouping. |
| `sector_automation_risk_score` | Numeric | 0 | 679 | min 0.151, median 0.580, mean 0.538, max 0.855 | Higher values imply greater sector automation exposure. |
| `gdp_per_capita_usd` | Integer | 0 | 1,981 | min 879, median 10,635, mean 21,003, max 99,074 | Economic control feature. |
| `ai_adoption_index` | Numeric | 0 | 775 | min 0.169, median 0.720, mean 0.692, max 0.963 | Core AI adoption feature. |
| `pct_sector_workforce_displaced` | Numeric proportion | 0 | 2,068 | min 0.0018, median 0.0434, mean 0.0562, max 0.3000 | Candidate regression target; also direct component of net workforce change. |
| `pct_sector_workforce_new_roles_created` | Numeric proportion | 0 | 1,680 | min 0.0003, median 0.0219, mean 0.0356, max 0.2791 | Candidate regression target; direct component of net workforce change. |
| `net_workforce_change_pct` | Numeric proportion | 0 | 837 | min -0.1403, median -0.0164, mean -0.0205, max -0.0003 | Candidate regression target. All local rows are negative. |
| `ai_cited_layoff_announcements` | Integer count | 0 | 519 | min 0, median 63, mean 88.35, max 603 | Count target or explanatory feature. |
| `ai_skill_wage_premium_pct` | Numeric proportion | 0 | 490 | min 0.063, median 0.366, mean 0.362, max 0.610 | Candidate regression target or labor-market outcome. |
| `pct_workforce_female` | Numeric proportion | 0 | 10 | min 0.220, median 0.470, mean 0.462, max 0.790 | Demographic feature by sector. |
| `pct_displaced_roles_female` | Numeric proportion | 0 | 453 | min 0.213, median 0.493, mean 0.497, max 0.950 | Equity/fairness analysis target or feature. |
| `reskilling_programs_count` | Integer count | 0 | 91 | min 2, median 30, mean 34.50, max 92 | Policy/response feature. |
| `govt_ai_policy_score_1_to_10` | Numeric | 0 | 78 | min 1.1, median 5.4, mean 5.37, max 8.8 | Policy maturity feature. |
| `ai_tool_adoption_pct` | Numeric proportion | 0 | 799 | min 0.037, median 0.365, mean 0.373, max 0.881 | Workforce-level AI tool adoption feature. |
| `data_source_notes` | Constant text | 0 | 1 | Same source note in every row | Documentation field; exclude from modeling. |

## Data Quality Notes

- There are no missing values in the local CSV.
- There is no class label supplied; modeling targets must be selected or engineered.
- `net_workforce_change_pct` appears derived from displacement and new-role creation. If predicting net change, do not include `pct_sector_workforce_displaced` and `pct_sector_workforce_new_roles_created` unless the experiment intentionally uses derived components.
- The dataset is synthetic. Treat findings as modeling practice and scenario analysis, not real-world policy evidence.

## Machine Learning Fit

Strong assignment directions:

- Regression: predict `pct_sector_workforce_displaced`, `net_workforce_change_pct`, `ai_skill_wage_premium_pct`, or `ai_cited_layoff_announcements`.
- Time-series forecasting: model sector or country trajectories by `quarter_label`.
- Supervised classification: engineer high-risk labels, such as top-quartile displacement risk.
- Unsupervised learning: cluster country-sector-quarter profiles using adoption, policy, wage, and displacement variables.

Likely preprocessing:

- Drop `record_id` and `data_source_notes`.
- Encode categorical fields such as `country`, `region`, `income_group`, and `industry_sector`.
- Convert `quarter_label` to an ordered period index.
- Use time-aware validation, for example train on 2020-2024, validate on 2025, test on 2026.
- Consider grouped validation by country or sector to avoid overestimating generalization.

## Assignment Suitability

This dataset fits the assignment size guidance well: 20,800 rows, 23 variables, mixed categorical and numeric data, and enough complexity for at least three supervised models plus clustering or time-series extensions.

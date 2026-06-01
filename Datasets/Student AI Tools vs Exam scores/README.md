# Student AI Tools vs Exam Scores

Metadata and local schema notes for `students_ai_usage.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official Kaggle page | https://www.kaggle.com/datasets/muneebmuhammadali/student-ai-tools-vs-exam-scores |
| Kaggle title | Student AI Tools vs Exam scores |
| Creator | Muneeb Muhammad Ali (`muneebmuhammadali`) |
| License | CC0-1.0 / Public Domain |
| Version | 1, initial release |
| Last updated on Kaggle | 2026-05-04 |
| Expected update frequency | Never |
| Kaggle usability rating | 1.0 |
| Kaggle activity at review time | 4,789 views, 1,188 downloads, 31 votes, 8 notebooks |
| Local review date | 2026-06-01 |

## What The Dataset Is

This is a small synthetic education dataset about student AI-tool usage and academic performance. It records age, education level, study hours, AI usage, AI tool used, AI usage purpose, grades before and after AI adoption, and daily screen time.

The Kaggle metadata describes it as a simulated student survey for educational and analytical use. It says records are synthetic and anonymized. The source note mentions hypothetical patterns across provinces of Pakistan, but the local CSV does not include a province column.

## Local File Inventory

| File | Rows | Columns | Size | Missing values |
| --- | ---: | ---: | ---: | ---: |
| `students_ai_usage.csv` | 100 | 9 | 3,962 bytes | 120 |

The missing values are structural: students who do not use AI have no AI tool or AI purpose value.

## Coverage

| Field | Local values |
| --- | --- |
| Students | 100 |
| Education levels | school, college |
| AI usage | 40 Yes, 60 No |
| AI tools represented | ChatGPT, Copilot, Gemini |
| AI purposes represented | Coding, Homework, Research |

AI-usage distribution:

| `uses_ai` | Rows | Share |
| --- | ---: | ---: |
| No | 60 | 60% |
| Yes | 40 | 40% |

Derived grade-change summary:

| Group | Rows | Min change | Mean change | Max change |
| --- | ---: | ---: | ---: | ---: |
| All students | 100 | 0 | 3.93 | 15 |
| Uses AI | 40 | 5 | 9.825 | 15 |
| Does not use AI | 60 | 0 | 0 | 0 |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `age` | Integer | 0 | 6 | min 14, median 16, mean 16.49, max 19 | Demographic feature. |
| `education_level` | Categorical text | 0 | 2 | school, college | Encode as categorical. |
| `study_hours_per_day` | Numeric | 0 | 37 | min 1.0, median 2.8, mean 2.987, max 5.0 | Study behavior feature. |
| `uses_ai` | Categorical text | 0 | 2 | Yes, No | Candidate classification target or key explanatory feature. |
| `ai_tools_used` | Categorical text | 60 | 3 | Copilot, Gemini, ChatGPT | Missing when `uses_ai` is No. |
| `purpose_of_ai` | Categorical text | 60 | 3 | Research, Homework, Coding | Missing when `uses_ai` is No. |
| `grades_before_ai` | Integer | 0 | 21 | min 55, median 63, mean 64.77, max 75 | Baseline academic score. |
| `grades_after_ai` | Integer | 0 | 29 | min 55, median 69, mean 68.70, max 89 | Candidate regression target. |
| `daily_screen_time_hours` | Integer | 0 | 6 | min 2, median 4, mean 4.34, max 7 | Behavioral feature. |

## Data Quality Notes

- The dataset is very small, with only 100 rows.
- The 120 missing values are expected because `ai_tools_used` and `purpose_of_ai` are blank for the 60 non-AI users.
- For non-AI users, `grades_after_ai` equals `grades_before_ai`, producing a built-in zero grade change.
- Because the data is synthetic, causal claims about AI usage improving grades should not be made without caution.

## Machine Learning Fit

Useful lab-style directions:

- Regression: predict `grades_after_ai` or a derived `grade_change = grades_after_ai - grades_before_ai`.
- Classification: predict `uses_ai` from study behavior, grades, screen time, age, and education level.
- Grouped EDA: compare grade changes by AI tool and AI purpose.

Likely preprocessing:

- Create a derived `grade_change` column during experimentation.
- Treat missing `ai_tools_used` and `purpose_of_ai` as `None` or `No AI`, not as random missingness.
- Encode categorical variables.
- Use simple models and cross-validation because the dataset has only 100 rows.
- Avoid overinterpreting results. The non-AI group has no grade change by construction.

## Assignment Suitability

This dataset is useful for early lab practice, simple EDA, and demonstrating preprocessing. It is not a strong final assignment dataset because it is far below the suggested 20k to 50k row size and has only 9 variables.

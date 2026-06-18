# Coffee Shops Sales Data

Metadata and local schema notes for `Project.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official source page | https://mavenanalytics.io/data-playground/coffee-shop-sales |
| Source title | Coffee Shop Sales |
| Publisher | Maven Analytics |
| Public mirror located during review | https://www.kaggle.com/datasets/divu2001/coffee-shop-sales-analysis |
| License | Public Domain, according to the Maven Analytics source page |
| Source description | Transaction records for Maven Roasters, a fictitious coffee shop operating from three New York City locations |
| Local file form | Single flattened CSV named `Project.csv` |
| Local review date | 2026-06-10 |

The Maven Analytics page describes this as a sample dataset for sales trend, busy-day, busy-hour, location, and product-performance analysis. The local CSV appears to match the widely circulated `Project.csv` version used in Kaggle notebooks and mirrors. Treat the local CSV as the authoritative assignment input because it is a flattened file with 149,116 rows and 18 columns.

## What The Dataset Is

This is a transactional retail sales dataset for Maven Roasters, a fictitious coffee shop chain with three New York City locations: Astoria, Hell's Kitchen, and Lower Manhattan. Each row represents a sales transaction line with date, time, store, product, quantity, unit price, total bill, product hierarchy, size, and pre-derived calendar fields.

The dataset is well suited for exploratory sales analytics: revenue trends, product mix, store comparison, peak operating hours, and category-level performance. For machine learning, the strongest direction is not simple row-level prediction of `Total_Bill`, because that target is exactly derived from `transaction_qty * unit_price`. Better ML tasks should aggregate the data into daily or hourly demand/revenue targets, or define classification labels such as high-demand periods.

## Local File Inventory

| File | Rows | Columns | Size | Missing values | Duplicate rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| `Project.csv` | 149,116 | 18 | 18,395,105 bytes | 0 | 0 |

## Coverage

| Field | Local values |
| --- | --- |
| Time span | 2023-01-01 to 2023-06-30 |
| Time coverage | 181 unique dates |
| Store locations | Astoria, Hell's Kitchen, Lower Manhattan |
| Store IDs | 3, 5, 8 |
| Product categories | 9 |
| Product types | 29 |
| Product details | 45 |
| Product IDs | 80 |
| Operating hours in file | 06:00 to 20:00 |
| Total quantity sold | 214,470 |
| Total revenue | 698,812.33 |
| Average transaction-line bill | 4.6864 |
| Average transaction quantity | 1.4383 |

Store distribution:

| Store location | Rows | Quantity sold | Revenue | Revenue share |
| --- | ---: | ---: | ---: | ---: |
| Hell's Kitchen | 50,735 | 71,737 | 236,511.17 | 33.84% |
| Astoria | 50,599 | 70,991 | 232,243.91 | 33.23% |
| Lower Manhattan | 47,782 | 71,742 | 230,057.25 | 32.92% |

Category distribution by revenue:

| Product category | Rows | Quantity sold | Revenue | Revenue share |
| --- | ---: | ---: | ---: | ---: |
| Coffee | 58,416 | 89,250 | 269,952.45 | 38.63% |
| Tea | 45,449 | 69,737 | 196,405.95 | 28.11% |
| Bakery | 22,796 | 23,214 | 82,315.64 | 11.78% |
| Drinking Chocolate | 11,468 | 17,457 | 72,416.00 | 10.36% |
| Coffee beans | 1,753 | 1,828 | 40,085.25 | 5.74% |
| Branded | 747 | 776 | 13,607.00 | 1.95% |
| Loose Tea | 1,210 | 1,210 | 11,213.60 | 1.60% |
| Flavours | 6,790 | 10,511 | 8,408.80 | 1.20% |
| Packaged Chocolate | 487 | 487 | 4,407.64 | 0.63% |

Monthly revenue trend:

| Month | Rows | Quantity sold | Revenue |
| --- | ---: | ---: | ---: |
| January | 17,314 | 24,870 | 81,677.74 |
| February | 16,359 | 23,550 | 76,145.19 |
| March | 21,229 | 30,406 | 98,834.68 |
| April | 25,335 | 36,469 | 118,941.08 |
| May | 33,527 | 48,233 | 156,727.76 |
| June | 35,352 | 50,942 | 166,485.88 |

Peak transaction hours by row count:

| Hour | Rows | Quantity sold | Revenue |
| ---: | ---: | ---: | ---: |
| 10 | 18,545 | 26,713 | 88,673.39 |
| 9 | 17,764 | 25,370 | 85,169.53 |
| 8 | 17,654 | 25,197 | 82,699.87 |
| 7 | 13,428 | 19,449 | 63,526.47 |
| 11 | 9,766 | 14,035 | 46,319.14 |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `transaction_id` | Integer identifier | 0 | 149,116 | 1 to 149,456 | Row identifier; exclude from modeling. There are 340 missing IDs within the numeric range. |
| `transaction_date` | Date text | 0 | 181 | 01-01-2023 to 30-06-2023 | Parse as day-month-year. Use for chronological splits and time aggregation. |
| `transaction_time` | Time text | 0 | 25,762 | HH:MM:SS values | Parse to time if more detailed than `Hour` is needed. |
| `store_id` | Integer identifier | 0 | 3 | 3, 5, 8 | Store identifier; overlaps with `store_location`. |
| `store_location` | Categorical text | 0 | 3 | Astoria, Hell's Kitchen, Lower Manhattan | Main location feature. |
| `product_id` | Integer identifier | 0 | 80 | 1 to 87 | Product identifier; overlaps with product hierarchy fields. |
| `transaction_qty` | Integer count | 0 | 6 | min 1, median 1, mean 1.4383, max 8 | Candidate demand target after aggregation, or predictor for bill amount. |
| `unit_price` | Numeric currency | 0 | 41 | min 0.80, median 3.00, mean 3.3822, max 45.00 | Price feature. High values are mainly premium beans/branded products. |
| `Total_Bill` | Numeric currency | 0 | 75 | min 0.80, median 3.75, mean 4.6864, max 360.00 | Directly equals `transaction_qty * unit_price`; avoid trivial row-level prediction. |
| `product_category` | Categorical text | 0 | 9 | Coffee, Tea, Bakery, Drinking Chocolate, Flavours, Coffee beans, Loose Tea, Branded, Packaged Chocolate | Strong product grouping feature. |
| `product_type` | Categorical text | 0 | 29 | Examples: Brewed Chai tea, Gourmet brewed coffee, Barista Espresso, Hot chocolate, Scone | More detailed product grouping. |
| `product_detail` | Categorical text | 0 | 45 | Examples: Our Old Time Diner Blend, Ethiopia, Columbian Medium Roast, Brazilian, Latte | Most descriptive product field. |
| `Size` | Categorical text | 0 | 4 | Regular, Large, Not Defined, Small | `Not Defined` is structural rather than blank missingness. |
| `Month Name` | Categorical text | 0 | 6 | January to June | Redundant with `transaction_date` and `Month`. |
| `Day Name` | Categorical text | 0 | 7 | Monday to Sunday | Redundant with `transaction_date` and `Day of Week`. |
| `Hour` | Integer | 0 | 15 | 6 to 20 | Derived from `transaction_time`; useful for hourly demand patterns. |
| `Month` | Integer | 0 | 6 | 1 to 6 | Derived from `transaction_date`. |
| `Day of Week` | Integer | 0 | 7 | 0 to 6 | Derived from `transaction_date`; appears to map Monday as 0 and Sunday as 6. |

## Data Quality Notes

- There are no blank missing values and no duplicate rows in the local CSV.
- `Size = Not Defined` appears in 44,518 rows. Treat it as a valid category for items where size is not applicable, not as ordinary missing data.
- `Total_Bill` is perfectly derived from `transaction_qty * unit_price` in every row. This is useful for validation, but it creates target leakage if `Total_Bill` is predicted using quantity and unit price.
- Several calendar fields are already derived from date/time. Keep them for simple analysis, but avoid double-counting redundant information in model interpretation.
- The file covers only six months and three stores. It is large at row level, but its time horizon and location diversity are limited.
- The data describes a fictitious business, so recommendations should be framed as business-analytics practice rather than real operational advice.

## Machine Learning Fit

Useful lab-style directions:

- Regression after aggregation: predict daily or hourly revenue by store, category, or product type.
- Forecasting: predict future daily revenue, transaction count, or quantity sold for each store.
- Classification: engineer labels such as high-revenue hour, high-demand day, or top-quartile product-store demand.
- Clustering: group products, store-hour profiles, or category-day profiles by revenue, quantity, price, and temporal patterns.
- Association-style analysis: study which product categories and sizes dominate different stores and time periods.

Likely preprocessing:

- Parse `transaction_date` as day-month-year and `transaction_time` as time.
- Create an ordered timestamp or date-hour field for time-aware modeling.
- Drop `transaction_id` for modeling.
- Decide between `store_id` and `store_location`, and between `product_id` and product text fields, to reduce redundant encodings.
- Avoid using `transaction_qty` and `unit_price` when the target is raw `Total_Bill`, unless the experiment is intentionally a formula check.
- Prefer chronological train/validation/test splits for forecasting and demand prediction.
- Aggregate to a modeling table such as store-date-hour, store-date-category, or product-date before applying regression or classification models.

## Assignment Suitability

Verdict: useful candidate, but not the strongest final assignment choice unless the project is framed around demand forecasting or retail sales prediction.

Strengths:

- It is much larger than the assignment's suggested minimum, with 149,116 rows and 18 variables.
- It contains mixed categorical, numeric, date, and time fields.
- It supports strong EDA, business recommendations, visualization, feature engineering, and time-aware validation.
- It can support at least three models if transformed into an aggregated demand or revenue forecasting/classification problem.

Weaknesses:

- It is very clean, with no missing values and no duplicate rows, so there is less opportunity to demonstrate difficult data cleaning.
- The most obvious target, `Total_Bill`, is not a meaningful ML target at row level because it is exactly calculated from two columns.
- The dataset is a popular Maven Analytics/Kaggle practice dataset, so it may conflict with the assignment guideline to avoid commonly experimented datasets.
- It covers only one fictitious chain, three locations, and six months, limiting generalization and literature depth.

Use this dataset if the final project topic is narrowed to something like "short-term demand and revenue forecasting for coffee shop operations using transaction-level sales data." For a stronger AML submission, the Global Urban Air Quality dataset remains a better candidate because it has richer temporal structure, less trivial targets, and more room for supervised, unsupervised, and forecasting methods.

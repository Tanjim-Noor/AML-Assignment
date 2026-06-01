# Global Urban Air Quality & Pollution Time-Series

Metadata and local schema notes for `global_urban_smog_pm25_hourly.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official Kaggle page | https://www.kaggle.com/datasets/iconicwasil/global-urban-air-quality-and-pollution-time-series |
| Kaggle title | Global Urban Air Quality & Pollution Time-Series |
| Creator | Muhammad Wasil (`iconicwasil`) |
| License | CC0-1.0 / Public Domain |
| Version | 1, initial release |
| Last updated on Kaggle | 2026-05-22 |
| Expected update frequency | Never |
| Kaggle usability rating | 1.0 |
| Kaggle activity at review time | 1,181 views, 358 downloads, 31 votes, 8 notebooks |
| Local review date | 2026-06-01 |

## What The Dataset Is

This is an hourly urban air-quality time-series dataset. The Kaggle page describes it as a pollution dataset for major global cities, intended for forecasting, exploratory data analysis, geospatial visualization, and hazardous-event classification.

The Kaggle page says the data was aggregated programmatically through the Open-Meteo Air Quality API. It also describes the dataset as covering 50 megacities and 400k+ hourly observations. The local CSV in this workspace contains 29 cities and 254,736 rows, so the local file should be treated as the authoritative input for this assignment.

## Local File Inventory

| File | Rows | Columns | Size | Missing values |
| --- | ---: | ---: | ---: | ---: |
| `global_urban_smog_pm25_hourly.csv` | 254,736 | 13 | 20,623,214 bytes | 26 |

## Coverage

| Field | Local values |
| --- | --- |
| Time span | 2025-05-22 00:00 to 2026-05-22 23:00 |
| Time resolution | Hourly |
| Timestamp count | 8,784 unique hourly timestamps |
| Cities | 29 |
| Rows per city | 8,784 each |
| Target-style binary flag | `Hazardous_Event` |

City coverage:

`Lahore`, `Delhi`, `Beijing`, `Los Angeles`, `London`, `Mumbai`, `New York`, `Tokyo`, `Dhaka`, `Jakarta`, `Karachi`, `Seoul`, `Mexico City`, `Sao Paulo`, `Cairo`, `Shanghai`, `Bangkok`, `Tehran`, `Bogota`, `Lima`, `Paris`, `Istanbul`, `Chicago`, `Moscow`, `Riyadh`, `Dubai`, `Johannesburg`, `Lagos`, `Buenos Aires`.

Hazardous-event distribution:

| `Hazardous_Event` | Meaning | Rows | Share |
| --- | --- | ---: | ---: |
| 0 | Not hazardous by dataset flag | 221,074 | 86.79% |
| 1 | Hazardous event by dataset flag | 33,662 | 13.21% |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `Timestamp` | Datetime text | 0 | 8,784 | 2025-05-22T00:00 to 2026-05-22T23:00 | Parse to datetime; derive hour, day, month, weekday, lag features. |
| `City` | Categorical text | 0 | 29 | See city list | Use for city-specific models, grouping, or fixed effects. |
| `Latitude` | Numeric | 0 | 29 | min -34.6037, median 28.6139, mean 22.1899, max 55.7558 | City coordinate feature; constant per city. |
| `Longitude` | Numeric | 0 | 29 | min -118.2437, median 37.6173, mean 25.6356, max 139.6917 | City coordinate feature; constant per city. |
| `PM10_ug_m3` | Numeric | 26 | 3,036 | min 0.0, median 30.6, mean 87.31, max 3,270.8 | Coarse particulate concentration; missing rows are all Riyadh. |
| `PM2_5_ug_m3` | Numeric | 0 | 1,872 | min 0.0, median 22.9, mean 36.65, max 624.0 | Strong regression or forecasting target. |
| `Carbon_Monoxide_ug_m3` | Integer-like numeric | 0 | 6,898 | min 0, median 376, mean 698.00, max 19,081 | Pollutant predictor. |
| `Nitrogen_Dioxide_ug_m3` | Numeric | 0 | 1,799 | min 0.0, median 25.1, mean 33.69, max 309.2 | Pollutant predictor. |
| `Ozone_ug_m3` | Integer-like numeric | 0 | 392 | min 0, median 53, mean 60.94, max 523 | Pollutant predictor; may vary with sunlight/UV. |
| `Dust_ug_m3` | Integer-like numeric | 0 | 4,511 | min 0, median 1, mean 99.99, max 10,166 | Heavy-tailed pollutant/dust feature; consider robust scaling. |
| `UV_Index` | Numeric | 0 | 291 | min 0.0, median 0.0, mean 1.39, max 15.85 | Environmental predictor; cyclical daily pattern likely. |
| `European_AQI` | Integer | 0 | 1,143 | min 7, median 61, mean 75.84, max 1,227 | Air-quality index; may leak if predicting `Hazardous_Event`. |
| `Hazardous_Event` | Binary integer | 0 | 2 | 0 or 1 | Classification target candidate. |

## Data Quality Notes

- Only `PM10_ug_m3` has missing values: 26 missing rows, all for Riyadh.
- Several pollutant fields are strongly right-skewed with extreme maxima. Robust scaling, log transforms, or outlier analysis may be useful.
- If `Hazardous_Event` is derived from AQI or pollutant thresholds, including `European_AQI` may make classification too easy. Treat it as a possible leakage feature.
- Coordinates are city-level constants, not sensor-level varying locations.

## Machine Learning Fit

Strong assignment directions:

- Time-series forecasting: predict future `PM2_5_ug_m3`, `European_AQI`, or city-specific pollutant levels.
- Binary classification: predict `Hazardous_Event`.
- Regression: predict `PM2_5_ug_m3` from other pollutants, city, and time features.
- Clustering: group cities or hours by pollutant profiles.

Likely preprocessing:

- Parse `Timestamp` and sort by `City`, then `Timestamp`.
- Impute the 26 missing `PM10_ug_m3` values, preferably by city/time interpolation or model-based imputation.
- Engineer lag features and rolling means for forecasting tasks.
- Use chronological train/validation/test splits. Random splits will overstate time-series performance.
- Encode `City` or train separate models for major city groups.

## Assignment Suitability

This is one of the strongest candidate datasets in the workspace for the final assignment. It has more than 20k rows, mixed temporal, categorical, geospatial, and numeric features, a natural binary target, and room for supervised, unsupervised, and time-series methods.

# Final Assignment

This folder is for the polished final Applied Machine Learning assignment work.

## Current Final Direction

- Primary dataset: `Datasets/Global Urban Air Quality & Pollution Time-Series/global_urban_smog_pm25_hourly.csv`
- Backup dataset: `Datasets/AI Workforce Displacement 2020–2026/ai_workforce_displacement_global_2020_2026.csv`
- Canonical selection rationale: `Final Assignment/dataset_selection_rubric.md`

## Frozen Problem Statement

Predict and explain hazardous urban air-quality events and PM2.5/AQI trends across global cities using hourly pollutant, city, location, and time-series features.

The final implementation should treat this as a high-mark, evidence-driven workflow:

- classification for hazardous-event risk,
- regression or forecasting for PM2.5 or AQI trends,
- clustering or profile analysis for city/pollution patterns,
- chronological validation rather than random-only validation,
- leakage checks, especially around `European_AQI` and derived hazard labels.

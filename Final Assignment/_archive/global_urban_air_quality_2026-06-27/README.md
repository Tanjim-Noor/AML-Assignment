# Archived Final Assignment: Global Urban Air Quality

Archived on 2026-06-27 after the `Impact of AI on Students` dataset passed the documented migration gate.

This directory preserves the former final-assignment rationale and four air-quality implementations. It is historical material, not the active final direction. The dataset and its learning-material application notebooks remain in their original workspace locations.

The dataset-independent GPU diagnostics notebook remains active under `Final Assignment/notebooks/`.

## Original README

This folder contains the notebook-only final Applied Machine Learning assignment work for the selected dataset:

`Datasets/Global Urban Air Quality & Pollution Time-Series/global_urban_smog_pm25_hourly.csv`

## Notebook-Only Rule

The final assignment versions are intentionally standalone notebooks. Do not add shared pipeline scripts, CLI runners, generated output folders, saved plot files, CSV result exports, model dumps, or Markdown run summaries here.

All EDA tables, preprocessing checks, plots, model results, validation outputs, and recommendations should appear inline in notebook cell outputs when the notebook is run.

## Final Dataset Context

- Primary dataset: `Global Urban Air Quality & Pollution Time-Series`
- Backup dataset: `AI Workforce Displacement 2020-2026`
- Canonical selection rationale: `dataset_selection_rubric.md`
- Current final direction: compare multiple air-quality modeling variations using chronological validation, leakage checks, supervised learning, and unsupervised city/pollution profiling.

## Standalone Notebook Variations

| Notebook | Target | Main task | Report angle |
| --- | --- | --- | --- |
| `notebooks/01_future_hazard_classifier.ipynb` | Next-hour `Hazardous_Event` | Time-aware binary classification | Early warning for hazardous urban air-quality events. |
| `notebooks/02_pm25_forecasting_regression.ipynb` | Next-hour `PM2_5_ug_m3` | Time-series regression | Short-term fine particulate pollution forecasting. |
| `notebooks/03_current_hazard_classifier.ipynb` | Current `Hazardous_Event` | Binary classification | Explaining pollutant conditions associated with hazardous air quality. |
| `notebooks/04_aqi_forecasting_regression.ipynb` | Next-hour `European_AQI` | Time-series regression | Forecasting overall air-quality severity. |

Each notebook includes:

- dataset explanation and column dictionary,
- problem statement, aim, objectives, and assignment fit,
- complete EDA with inline plots,
- data cleaning and preprocessing,
- chronological train/validation/test split,
- baseline and tuned scikit-learn models,
- optional PyTorch CUDA neural-network section,
- model evaluation and comparison,
- unsupervised city/pollution profiling,
- interpretation, recommendations, limitations, and conclusion.

## GPU Notes

The notebooks include a CUDA/PyTorch setup and verification cell. If PyTorch is not installed in the workspace `.venv`, install the CUDA build from the workspace root:

```powershell
.venv\Scripts\python.exe -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

Then verify inside a notebook:

```python
import torch
torch.cuda.is_available()
```

Each notebook also has a `RUN_BALANCED_BACKUP` toggle for CPU-safe or faster assignment iteration.

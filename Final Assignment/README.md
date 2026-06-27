# Final Assignment

This folder contains the notebook-only final Applied Machine Learning assignment work for the selected dataset:

`Datasets/Impact of AI on Students/ai_student_impact_dataset.csv`

## Notebook-Only Rule

The final assignment variations are standalone notebooks. Do not add shared pipeline modules, CLI runners, generated result folders, saved plot files, CSV metric exports, model dumps, or Markdown run summaries.

All EDA tables, preprocessing checks, plots, training results, validation metrics, uncertainty estimates, interpretations, and recommendations appear inline when each notebook is run. The advanced variants are kept with outputs and execution counts cleared. `05_essential_gpa_change_regression.ipynb` is the deliberate exception: it retains executed outputs so its final results and analysis are immediately visible.

## Final Dataset Context

- Primary dataset: `Impact of AI on Students`
- Archived predecessor: `Global Urban Air Quality & Pollution Time-Series`
- Additional backup: `AI Workforce Displacement 2020-2026`
- Canonical selection rationale: `dataset_selection_rubric.md`
- Dataset documentation: `Datasets/Impact of AI on Students/README.md`
- Current primary direction: use essential GPA-change regression to test whether AI variables add predictive value beyond academic and study context. The other notebooks remain advanced alternatives.

The Kaggle source does not document collection, geography, sampling, ethics, or real-versus-synthetic provenance. The assignment must present results as predictive associations within the supplied file, not evidence that AI caused academic or wellbeing outcomes.

## Standalone Notebook Variations

| Notebook | Target | Main task | Primary evaluation |
| --- | --- | --- | --- |
| `notebooks/01_burnout_risk_multiclass_classifier.ipynb` | `Burnout_Risk_Level` | Multiclass early-risk classification | Macro-F1, balanced accuracy, class recall, multiclass ROC-AUC |
| `notebooks/02_skill_retention_regression.ipynb` | `Skill_Retention_Score` | Continuous-outcome regression | RMSE, MAE, R-squared |
| `notebooks/03_gpa_change_regression.ipynb` | `Post_Semester_GPA - Pre_Semester_GPA` | Academic-change regression | RMSE, MAE, R-squared |
| `notebooks/04_gpa_decline_classifier.ipynb` | `GPA_Change < 0` | Imbalanced binary classification | Macro-F1, balanced accuracy, recall, ROC-AUC, average precision |
| `notebooks/05_essential_gpa_change_regression.ipynb` | `Post_Semester_GPA - Pre_Semester_GPA` | Recommended essential final regression workflow | MAE, RMSE, R-squared, residual analysis |

## Recommended Essential Notebook

Use `notebooks/05_essential_gpa_change_regression.ipynb` as the primary final implementation when a concise, understandable notebook is required. It contains only the sections needed to satisfy the assignment: EDA, preparation, leakage control, an 80/20 split, five-fold validation, four regression models plus a baseline, tuning, test evaluation, residuals, feature importance, results analysis, recommendations, and conclusion.

`explanation.md` explains every section and provides a complete interpretation of the saved execution results.

The advanced variants include:

- problem statement, aim, objectives, and evidence boundary,
- dataset dictionary, integrity checks, EDA, and target analysis,
- explicit identifier and outcome-leakage controls,
- an untouched 20% test set and shuffled cross-validation,
- a dummy baseline plus at least three real models,
- fold variability and bootstrap confidence intervals,
- subgroup evaluation by major, year of study, and institutional policy,
- permutation-based interpretation,
- predictor-only K-means student-profile analysis,
- optional GPU extension,
- critical analysis, recommendations, limitations, and conclusion.

## Leakage and Validation Rules

- Drop `Student_ID` from every model.
- Never use `Post_Semester_GPA`, `Skill_Retention_Score`, or `Burnout_Risk_Level` to predict one another.
- Never use `Post_Semester_GPA` to predict derived GPA change or GPA decline.
- Exclude `Anxiety_Level_During_Exams` from the primary early-risk burnout model; add it only as a labelled ablation.
- Fit preprocessing and tuning only on training folds.
- Use shuffled cross-sectional validation. The dataset contains no defensible time or repeated-student sequence.
- Report macro/class-level metrics for classification and uncertainty for all final comparisons.
- Do not manufacture missing values to make the perfectly clean dataset appear more complex.

## Runtime Modes

The advanced notebooks define:

```python
RUN_BALANCED_BACKUP = True
```

The balanced mode uses three cross-validation folds and lighter model settings for CPU-safe iteration. Set it to `False` for the full five-fold, higher-iteration report run.

The essential notebook always uses five folds and contains no GPU section. `notebooks/00_gpu_runtime_diagnostics.ipynb` remains the environment-check notebook for the advanced variants, which contain opt-in PyTorch/CUDA extensions.

## Archive

The prior air-quality README, selection rubric, and four final notebooks are preserved under:

`Final Assignment/_archive/global_urban_air_quality_2026-06-27/`

They should not be treated as active report implementations.

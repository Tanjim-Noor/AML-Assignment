# Final Assignment

This folder contains the notebook-only final Applied Machine Learning assignment work for the selected dataset:

`Datasets/Impact of AI on Students/ai_student_impact_dataset.csv`

## Notebook-Only Rule

The final assignment variations are standalone notebooks. Do not add shared pipeline modules, CLI runners, generated result folders, saved plot files, CSV metric exports, model dumps, or Markdown run summaries.

All EDA tables, preprocessing checks, plots, training results, validation metrics, uncertainty estimates, interpretations, and recommendations appear inline when each notebook is run. The advanced variants are kept with outputs and execution counts cleared. The essential, comprehensive and interactive demonstration notebooks, together with the three notebooks under `Deep Learning Experiments/`, deliberately retain executed outputs so their final results and analyses are immediately visible.

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
| `notebooks/06_comprehensive_gpa_change_regression.ipynb` | `Post_Semester_GPA - Pre_Semester_GPA` | Reported comprehensive regression workflow | Full EDA, validation, uncertainty and direction-specific diagnostics |
| `notebooks/07_interactive_gpa_prediction_demo.ipynb` | `Post_Semester_GPA - Pre_Semester_GPA` | Interactive model showcase with matched information modes | Context-only and context-plus-AI predictions |

## Recommended Essential Notebook

Use `notebooks/05_essential_gpa_change_regression.ipynb` as the primary final implementation when a concise, understandable notebook is required. It contains only the sections needed to satisfy the assignment: EDA, preparation, leakage control, an 80/20 split, five-fold validation, four regression models plus a baseline, tuning, test evaluation, residuals, feature importance, results analysis, recommendations, and conclusion.

`explanation.md` explains every section and provides a complete interpretation of the saved execution results.

## Interactive Prediction Demonstration

The executed demonstration provides three reader-facing modes: **Context + AI**, **Context only**, and **Compare both**. It recreates the reported 80/20 split, fits two matched tuned histogram gradient boosting pipelines, validates the selected combined model, and keeps prediction logic separate from the widget layer for direct testing. Context-only mode hides and ignores the AI-related controls; comparison mode holds academic context fixed and shows both predictions, illustrative post-semester GPAs, and their information-based prediction difference.

The interface uses `ipywidgets==8.1.8`. Install it only in the workspace environment if it is missing:

```powershell
.venv\Scripts\python.exe -m pip install ipywidgets==8.1.8
```

The notebook performs a readable dependency check and never installs packages from a notebook cell. Its saved worked example uses a previous GPA of 3.40 and produces context-only and context-plus-AI GPA-change predictions of approximately +0.267 and +0.335. These values demonstrate predictive associations only; they are not causal effects or academic advice.

## Deep-Learning Experiments

`Deep Learning Experiments/` supplements notebook 05 with three executed CUDA experiments that use the same leakage-safe features, development/test split, and five-fold validation design:

| Notebook | Architecture | CV RMSE | Test RMSE | Test R-squared |
| --- | --- | ---: | ---: | ---: |
| `Deep Learning Experiments/01_category_embedding_mlp.ipynb` | Category-embedding MLP | 0.1450 | 0.1419 | 0.4145 |
| `Deep Learning Experiments/02_ft_transformer.ipynb` | FT-Transformer | **0.1440** | **0.1410** | **0.4218** |
| `Deep Learning Experiments/03_tabm.ipynb` | TabM, five implicit members | 0.1447 | 0.1413 | 0.4194 |

The HGB benchmark from notebook 05 has CV RMSE 0.1443, test RMSE 0.1414, and test R-squared 0.4185. FT-Transformer is the strongest neural experiment, but its CV RMSE improvement is only about 0.20%, below the predefined 1% material-improvement threshold. HGB therefore remains the recommended final model because the neural models add complexity without a consistent, material validation gain. See `Deep Learning Experiments/README.md` for the complete comparison and decision rule.

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

The essential notebook always uses five folds and contains no GPU section. `notebooks/00_gpu_runtime_diagnostics.ipynb` remains the environment-check notebook for the advanced variants. The three deep-learning experiments require PyTorch with CUDA for the recorded runs and independently verify the active device.

## Archive

The prior air-quality README, selection rubric, and four final notebooks are preserved under:

`Final Assignment/_archive/global_urban_air_quality_2026-06-27/`

They should not be treated as active report implementations.

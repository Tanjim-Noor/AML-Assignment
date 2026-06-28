# Deep Learning Experiments

Three standalone CUDA experiments for the `GPA_Change` regression problem.

Source dataset:

`Datasets/Impact of AI on Students/ai_student_impact_dataset.csv`

Reference implementation:

`Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb`

## Experiment Notebooks

| Notebook | Architecture | Purpose |
| --- | --- | --- |
| `01_category_embedding_mlp.ipynb` | Category-embedding MLP | Establish a strong ordinary neural-network baseline. |
| `02_ft_transformer.ipynb` | Three-block FT-Transformer | Test attention-based interactions between tabular features. |
| `03_tabm.ipynb` | Five-member TabM ensemble | Test modern parameter-efficient neural ensembling. |

The experiments use `rtdl-revisiting-models==0.0.2` and `tabm==0.0.3` from the official [RTDL revisiting models](https://github.com/yandex-research/rtdl-revisiting-models) and [TabM](https://github.com/yandex-research/tabm) implementations. `pytorch-tabular` is intentionally excluded because its resolved dependencies would downgrade the workspace's pandas 3.0.3 installation.

Every notebook is standalone and contains its own:

- dataset loading and GPA-change target construction,
- leakage-safe feature policy,
- fold-local categorical encoding,
- fold-local numerical and target standardisation,
- CUDA and mixed-precision configuration,
- early stopping and learning-rate scheduling,
- five-fold cross-validation,
- five-model averaged test prediction,
- MAE, RMSE, R-squared, tolerance, residual, and runtime analysis,
- plots and generated plain-language conclusions.

## Shared Evaluation Contract

- Development/test split: 80%/20%, random state 42.
- Cross-validation: five shuffled folds inside the development set.
- Primary metric: RMSE.
- Model selection evidence: mean cross-validation RMSE.
- Test use: confirmation only, not model selection.
- Material-win rule: a deep model must reduce HGB cross-validation RMSE by at least 1%.

HGB reference:

| Metric | Value |
| --- | ---: |
| CV RMSE | 0.1443 |
| Test MAE | 0.1112 |
| Test RMSE | 0.1414 |
| Test R-squared | 0.4185 |

## Executed Results

| Model | CV MAE | CV RMSE | CV R-squared | Test MAE | Test RMSE | Test R-squared | Runtime |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| HGB reference | - | **0.1443** | 0.4080 | 0.1112 | 0.1414 | 0.4185 | - |
| Category-Embedding MLP | 0.1139 | 0.1450 | 0.4027 | 0.1119 | 0.1419 | 0.4145 | 88.6 s |
| FT-Transformer | **0.1128** | **0.1440** | **0.4108** | **0.1109** | **0.1410** | **0.4218** | 209.9 s |
| TabM | 0.1135 | 0.1447 | 0.4053 | 0.1113 | 0.1413 | 0.4194 | **65.1 s** |

Bold values among the neural rows mark the strongest neural result. HGB remains the reference for the selection decision.

## Error Tolerance

| Model | Within 0.10 GPA points | Within 0.20 GPA points | Mean residual |
| --- | ---: | ---: | ---: |
| Category-Embedding MLP | 53.11% | 84.27% | +0.0006 |
| FT-Transformer | 53.70% | 84.24% | +0.0020 |
| TabM | 53.54% | 84.39% | -0.0005 |

All three models have mean residuals close to zero, so none shows substantial overall high or low prediction bias.

## Model-by-Model Analysis

### Category-Embedding MLP

- CV RMSE was 0.1450, 0.47% worse than HGB.
- Test RMSE was 0.1419, 0.32% worse than HGB.
- It is a valid neural baseline and nearly matches HGB.
- It did not produce a performance reason to replace HGB.

### FT-Transformer

- CV RMSE was 0.1440, 0.20% better than HGB.
- Test RMSE was 0.1410, 0.31% better than HGB.
- It was the strongest neural architecture on every main reported metric.
- Its cross-validation improvement is below the required 1% material-win threshold.
- It is useful as the advanced deep-learning comparison, but not a clear replacement for HGB.

### TabM

- CV RMSE was 0.1447, 0.26% worse than HGB.
- Test RMSE was 0.1413, 0.10% better than HGB.
- It was the fastest deep architecture despite internally averaging five ensemble members.
- Its test improvement is not supported by a cross-validation improvement.
- It should not replace HGB based on this result.

## Final Decision

**Histogram gradient boosting remains the recommended final model.**

FT-Transformer is the best deep-learning alternative, but its mean cross-validation RMSE improvement was only 0.20%, below the predefined 1% material threshold. The small test improvement is consistent with the models being closely matched and is not sufficient evidence to prefer the slower architecture.

Recommended reporting:

> Three neural architectures were evaluated using the same five-fold protocol and untouched test set as the final HGB model. FT-Transformer achieved the strongest neural result, with cross-validation RMSE 0.1440 and test RMSE 0.1410. However, its cross-validation improvement over HGB was only 0.20%, below the predefined 1% material-improvement threshold. HGB therefore remained the preferred model because it achieved comparable accuracy with lower complexity.

## Evidence Boundary

These experiments compare predictive architectures. They do not prove that AI usage caused GPA changes. The dataset has no credible non-AI control group, random assignment, or documented real-world sampling process.

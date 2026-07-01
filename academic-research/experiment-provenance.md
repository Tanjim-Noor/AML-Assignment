# Notebook 05 Reproduction Record

## Scope

This record covers the approved deterministic rerun of
`Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb`. The
canonical notebook and dataset were not edited. The notebook was executed in
memory so that its saved outputs could be compared with fresh outputs and four
report figures could be exported.

## Inputs and environment

- Notebook SHA-256:
  `e65b2a977561d173b506f03855d0ea9dbd13811993fdbc7b1da72cee003acd0c`
- Canonical dataset SHA-256:
  `4d911088c4b12d60a450a9acae6b606f4119ebbb48679518e427a4fc00778472`
- Random state: `42`
- Development-test split: `80/20`
- Cross-validation: shuffled five-fold
- Operating system: Windows 10 `10.0.19044`
- Python: `3.13.11`
- pandas: `3.0.3`
- NumPy: `2.4.6`
- scikit-learn: `1.9.0`
- Matplotlib: `3.10.9`
- seaborn: `0.13.2`
- nbclient: `0.11.0`
- nbformat: `5.10.4`
- Execution duration: `70.9278` seconds on local CPU
- External service or monetary cost: none

The reproduction script executed the notebook with the canonical repository as
the kernel working directory. This avoided a worktree-only line-ending
difference in the checked-out CSV. The canonical and worktree CSV files had
already been shown to produce identical pandas data frames and row hashes.

## Verification result

Verdict: **REPRODUCIBLE (PASS-WITH-WARNINGS)**.

The fresh `ANALYSIS_SUMMARY_JSON` matched the saved raw JSON exactly. The eight
displayed result tables in notebook cells 5, 6, 8, 11, 13, 17, 19 and 21 also
matched exactly after HTML parsing. The reproduced headline values were:

| Evidence | Reproduced value |
|---|---:|
| Best final model | Tuned histogram gradient boosting |
| HGB cross-validated RMSE | 0.1443 |
| Tuned HGB cross-validated RMSE | 0.1441 |
| Final test MAE | 0.11119387315239335 |
| Final test RMSE | 0.14136665572557847 |
| Final test R-squared | 0.41846967761479426 |
| Mean-baseline test RMSE | 0.18540515992356443 |
| Mean-baseline test R-squared | -0.000281023473369002 |
| Context-only test R-squared | 0.23817440562079406 |
| AI-only test R-squared | 0.1702941288306299 |
| Combined-feature test R-squared | 0.4169779887758607 |
| Combined over context-only increment | 0.17880358315506661 |
| Predictions within 0.10 GPA points | 53.57% |
| Predictions within 0.20 GPA points | 84.34% |
| Mean residual | 0.001867985404500299 |

The five most important features in the reproduced permutation-importance
output were `Traditional_Study_Hours`, `Primary_Use_Case`,
`Weekly_GenAI_Hours`, `Year_of_Study` and `Prompt_Engineering_Skill`.

## Exported assets

| Asset | SHA-256 |
|---|---|
| `Assignment Report/assets/fig01_gpa_change_eda.png` | `8bb6333f4092da176589c63c28e6712ee7c990dea5ba6d73fe76782fba84d356` |
| `Assignment Report/assets/fig02_model_test_rmse_and_actual_vs_predicted.png` | `4f78a96e573127ad48c3d3221b58e616c3876121ec0e6c50794b42b0fffd505a` |
| `Assignment Report/assets/fig03_residual_diagnostics.png` | `a2bc5f073268878d4f3470067483b33d4f6bda9f11ea86a036c02f3f455c3ca4` |
| `Assignment Report/assets/fig04_permutation_importance.png` | `62fa2cf01104055334110ee81e7ce0e9e54fd3e1f9f4b061b24d3d5c31cc81e7` |

## Warnings

The Windows notebook kernel emitted a ZMQ event-loop shutdown warning, and
joblib's resource tracker emitted cleanup `KeyError` messages for temporary
memmapping folders after execution. These warnings occurred during process
cleanup. They did not interrupt notebook execution, change any raw metric or
table, or prevent any figure from being generated. They are retained here so
that the reproduction verdict is not overstated.

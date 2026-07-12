# Notebook 06 Execution and Reproduction Record

## Scope and approval

The user approved creation and local execution of
`Final Assignment/notebooks/06_comprehensive_gpa_change_regression.ipynb` on
13 July 2026. Notebook 05 remained byte-unchanged at SHA-256
`e65b2a977561d173b506f03855d0ea9dbd13811993fdbc7b1da72cee003acd0c`.
The reproducible builder is `academic-research/build_notebook06.py`.

Notebook 06 copies notebook 05's modelling workflow, adds complete data
understanding, EDA, preparation decisions and GPA-direction error diagnostics,
executes locally, saves outputs and exports ten report figures. No external
service, participant contact or monetary cost was involved.

## Environment and protocol

- Dataset: `Datasets/Impact of AI on Students/ai_student_impact_dataset.csv`
- Dataset SHA-256: `4d911088c4b12d60a450a9acae6b606f4119ebbb48679518e427a4fc00778472`
- Notebook 06 SHA-256: `8e7e05669380899e615097392a7da8cbe492ed93a301f3d7b6ec510c4bbc0bc3`
- Random state: 42; split: 80/20; cross-validation: shuffled five-fold
- Python 3.13.11; pandas 3.0.3; NumPy 2.4.6; scikit-learn 1.9.0
- Matplotlib 3.10.9; seaborn 0.13.2; nbclient 0.11.0; nbformat 5.10.4
- Final execution duration: 86.6 seconds on local CPU

## Verification result

Verdict: **REPRODUCIBLE (PASS-WITH-WARNINGS)**.

All original core results reproduced exactly: tuned HGB test MAE 0.1111938732,
RMSE 0.1413666557 and R-squared 0.4184696776; context-only, AI-only and
combined R-squared values remained 0.2381744056, 0.1702941288 and
0.4169779888. Notebook 05's hash remained unchanged after both executions.

New direction diagnostics used the same untouched test predictions:

| Direction | Count | MAE | RMSE | Mean residual |
|---|---:|---:|---:|---:|
| Decrease | 1,203 | 0.1979 | 0.2208 | -0.1916 |
| Unchanged | 11 | 0.1615 | 0.1800 | -0.1615 |
| Increase | 8,786 | 0.0993 | 0.1266 | 0.0286 |

Windows emitted the same ZMQ selector-thread warning and joblib temporary
memmap cleanup `KeyError` messages seen in the earlier reproduction. They
occurred after successful computation and did not affect outputs.

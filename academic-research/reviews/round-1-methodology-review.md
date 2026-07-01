# Round 1 Methodology Review

Review mode: `full`
Manuscript: draft v1, manifest
`ce2d8065fbf5006dfc9adf9745dec531322ae829dcc66bb78cb7419ef5c00388`
Role: quantitative methodology, validation and reproducibility
Recommendation: **Minor revision**
Confidence: **5/5**

## Strengths

- The predictive question matches the continuous target and explicitly rejects
  causal inference.
- Leakage exclusions are correct and preprocessing is contained within
  pipelines fitted in cross-validation.
- Model-family choice and tuning are driven by development-fold RMSE, and all
  saved metrics were reproduced exactly.
- Missing tuned CV statistics are left unavailable rather than inferred.
- The report distinguishes fold variability from formal statistical
  significance and interprets error in GPA units.

## Findings

### M1 — Test-set use is described too strongly

Priority: **P1 major**

The Methods section states that the test set was used “once”, while notebook 05
evaluates feature-set ablations, all fitted model candidates and permutation
importance on the same 10,000 rows. The algorithm family and tuned
configuration can still be justified from cross-validation, and no model was
refitted using test outcomes. However, “once” and “untouched” imply a stricter
single-query evaluation than the implementation provides.

Required action: describe the set as *reserved* and explain that it supported
several prespecified final comparisons and interpretation operations. State
that CV selected the family/configuration, that test inspection did not trigger
refitting, and that repeated reporting on one partition remains a limitation.

Verification condition: Methods and Validation no longer claim single-use
testing and explicitly preserve the CV-selection hierarchy.

### M2 — Reproducibility could name the complete plotting stack

Priority: **P2 moderate**

The report names Python, pandas, NumPy and scikit-learn, but the figures also
depend on Matplotlib and seaborn. Their versions are recorded in experiment
provenance but absent from the report.

Required action: add Matplotlib 3.10.9 and seaborn 0.13.2 to Methods.

### M3 — Table 7 needs a compact standalone note

Priority: **P2 moderate**

The prose defines CV, HGB, MAE, RMSE and R-squared, but a table intended to
stand alone should define its abbreviations and explain the unavailable tuned
cells and bolding.

Required action: add a note below Table 7.

## Statistical reporting assessment

Rating: **Adequate for an applied predictive assignment**. Fold variability,
held-out error and practical tolerances are reported. Confidence intervals and
paired fold tests are unavailable, but the manuscript discloses this and does
not claim significance. No p-hacking or selective hypothesis-testing pattern
was identified.

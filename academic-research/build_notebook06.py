"""Build, execute, and export figures from comprehensive notebook 06.

Notebook 05 is read-only baseline. This script copies its modelling workflow,
adds comprehensive data understanding and direction-aware diagnostics, then
executes notebook 06 with saved outputs.
"""

from __future__ import annotations

import base64
import copy
import hashlib
from pathlib import Path

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb"
OUTPUT = ROOT / "Final Assignment/notebooks/06_comprehensive_gpa_change_regression.ipynb"
ASSETS = ROOT / "Assignment Report/assets"
SOURCE_SHA256 = "e65b2a977561d173b506f03855d0ea9dbd13811993fdbc7b1da72cee003acd0c"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md(text: str) -> nbformat.NotebookNode:
    return nbformat.v4.new_markdown_cell(text.strip() + "\n")


def code(text: str, figure: str | None = None) -> nbformat.NotebookNode:
    cell = nbformat.v4.new_code_cell(text.strip() + "\n")
    if figure:
        cell.metadata["report_figure"] = figure
    return cell


def build() -> nbformat.NotebookNode:
    if sha256(SOURCE) != SOURCE_SHA256:
        raise RuntimeError("Notebook 05 changed; refusing to build from unapproved baseline")
    source = nbformat.read(SOURCE, as_version=4)
    nb = copy.deepcopy(source)
    nb.cells[0].source = nb.cells[0].source.replace(
        "Essential Final Assignment", "Comprehensive Final Assignment"
    ).replace(
        "## Evidence boundary",
        "## Evidence boundary\n\nThis notebook extends notebook 05 with complete data understanding, EDA, preparation evidence, and direction-aware error analysis. It retains the observed continuous target distribution without balancing or manufactured cleaning.\n\n## Evidence boundary",
    )

    # Existing report figures keep stable filenames.
    for index, filename in {
        6: "fig06_gpa_change_eda.png",
        17: "fig07_model_test_rmse_and_actual_vs_predicted.png",
        19: "fig08_residual_diagnostics.png",
        21: "fig10_permutation_importance.png",
    }.items():
        nb.cells[index].metadata["report_figure"] = filename

    # Replace code-facing labels in exported plots with reader-facing language.
    nb.cells[6].source = nb.cells[6].source.replace(
        'axes[0, 0].set_title("Distribution of semester GPA change")',
        'axes[0, 0].set(title="Distribution of semester GPA change", xlabel="Semester GPA change")',
    ).replace(
        'axes[0, 1].set_title("Previous GPA and GPA change")',
        'axes[0, 1].set(title="Previous GPA and GPA change", xlabel="Previous-semester GPA", ylabel="Semester GPA change")',
    ).replace(
        'axes[1, 0].set_title("GPA change by prompt skill")',
        'axes[1, 0].set(title="GPA change by prompt skill", xlabel="Prompt-engineering skill", ylabel="Semester GPA change")',
    ).replace(
        'axes[1, 1].set_title("Mean GPA change by weekly AI-hours quartile")',
        'axes[1, 1].set(title="Mean GPA change by weekly AI-hours quartile", xlabel="Weekly GenAI-hours quartile", ylabel="Mean semester GPA change")',
    )
    nb.cells[21].source = nb.cells[21].source.replace(
        'importance_results = (\n    pd.DataFrame({',
        'DISPLAY_LABELS = {\n'
        '    "Traditional_Study_Hours": "Traditional study hours",\n'
        '    "Primary_Use_Case": "Primary AI use case",\n'
        '    "Weekly_GenAI_Hours": "Weekly GenAI hours",\n'
        '    "Year_of_Study": "Year of study",\n'
        '    "Prompt_Engineering_Skill": "Prompt-engineering skill",\n'
        '    "Pre_Semester_GPA": "Previous-semester GPA",\n'
        '    "Institutional_Policy": "Institutional AI policy",\n'
        '    "Paid_Subscription": "Paid subscription",\n'
        '    "Tool_Diversity": "Tool diversity",\n'
        '    "Perceived_AI_Dependency": "Perceived AI dependency",\n'
        '    "Anxiety_Level_During_Exams": "Exam anxiety",\n'
        '    "Major_Category": "Major category",\n'
        '}\n\n'
        'importance_results = (\n    pd.DataFrame({',
    ).replace(
        '    .sort_values("Importance", ascending=False)',
        '    .assign(Feature=lambda frame: frame["Feature"].map(DISPLAY_LABELS).fillna(frame["Feature"]))\n'
        '    .sort_values("Importance", ascending=False)',
    ).replace(
        'plt.title("Top permutation importances")',
        'plt.title("Top permutation importances")\nplt.xlabel("Increase in RMSE-based loss after shuffling")\nplt.ylabel("Predictor")',
    )

    understanding = [
        md("""
### 3.1 Full schema, quality, and validity audit

Every original field is profiled before modelling. A clean result is evidence from an explicit audit, not evidence that preparation can be skipped. Valid observations are not altered merely to demonstrate cleaning.
"""),
        code("""
original = df.iloc[:, :16].copy()

schema_rows = []
for column in original.columns:
    series = original[column]
    schema_rows.append({
        "Field": column,
        "Data type": str(series.dtype),
        "Non-null": int(series.notna().sum()),
        "Missing": int(series.isna().sum()),
        "Unique": int(series.nunique(dropna=True)),
        "Minimum": series.min() if pd.api.types.is_numeric_dtype(series) else "—",
        "Maximum": series.max() if pd.api.types.is_numeric_dtype(series) else "—",
    })
schema_profile = pd.DataFrame(schema_rows)
display(schema_profile)

validity_checks = pd.Series({
    "Rows": len(original),
    "Columns": original.shape[1],
    "Missing cells": int(original.isna().sum().sum()),
    "Duplicate rows": int(original.duplicated().sum()),
    "Duplicate student IDs": int(original["Student_ID"].duplicated().sum()),
    "GPA values outside 0–4": int((~original["Pre_Semester_GPA"].between(0, 4) | ~original["Post_Semester_GPA"].between(0, 4)).sum()),
    "Weekly GenAI hours outside 0–168": int((~original["Weekly_GenAI_Hours"].between(0, 168)).sum()),
    "Traditional study hours outside 0–168": int((~original["Traditional_Study_Hours"].between(0, 168)).sum()),
    "Tool diversity outside 1–5": int((~original["Tool_Diversity"].between(1, 5)).sum()),
    "Dependency outside 1–10": int((~original["Perceived_AI_Dependency"].between(1, 10)).sum()),
    "Exam anxiety outside 1–10": int((~original["Anxiety_Level_During_Exams"].between(1, 10)).sum()),
    "Skill retention outside 0–100": int((~original["Skill_Retention_Score"].between(0, 100)).sum()),
})
display(validity_checks.to_frame("Value"))

assert validity_checks.loc[["Missing cells", "Duplicate rows", "Duplicate student IDs"]].sum() == 0
assert validity_checks.filter(like="outside").sum() == 0
"""),
        code("""
quality_plot = pd.DataFrame({
    "Check": ["Missing cells", "Duplicate rows", "Duplicate IDs", "Invalid-range rows"],
    "Count": [
        validity_checks["Missing cells"], validity_checks["Duplicate rows"],
        validity_checks["Duplicate student IDs"], validity_checks.filter(like="outside").sum(),
    ],
})
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
sns.barplot(data=quality_plot, x="Count", y="Check", color="#4C78A8", ax=axes[0])
axes[0].set_title("Data-quality audit")
dtype_counts = schema_profile["Data type"].replace({"str": "categorical", "bool": "boolean"}).value_counts()
axes[1].pie(dtype_counts.values, labels=dtype_counts.index, autopct="%1.0f%%", startangle=90)
axes[1].set_title("Original field types")
fig.tight_layout()
plt.show()
""", "fig01_data_quality_and_schema.png"),
        md("""
### 3.2 Numeric and categorical exploration

Numeric fields are summarised with quartiles and IQR outlier flags. IQR flags identify unusual values for inspection; they do not prove errors. Categorical fields are checked for rare or unexpected levels.
"""),
        code("""
numeric_columns = original.select_dtypes(include=np.number).columns.drop("Student_ID")
categorical_columns = original.select_dtypes(exclude=np.number).columns

numeric_summary = original[numeric_columns].describe().T
numeric_summary["IQR"] = numeric_summary["75%"] - numeric_summary["25%"]
numeric_summary["IQR outliers"] = [
    int(((original[c] < numeric_summary.loc[c, "25%"] - 1.5 * numeric_summary.loc[c, "IQR"]) |
         (original[c] > numeric_summary.loc[c, "75%"] + 1.5 * numeric_summary.loc[c, "IQR"])).sum())
    for c in numeric_columns
]
display(numeric_summary.round(3))

category_rows = []
for column in categorical_columns:
    counts = original[column].value_counts(dropna=False)
    for level, count in counts.items():
        category_rows.append({"Field": column, "Level": str(level), "Count": int(count), "Percentage": 100 * count / len(original)})
categorical_summary = pd.DataFrame(category_rows)
display(categorical_summary.style.format({"Percentage": "{:.2f}%"}))
"""),
        code("""
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
for ax, column in zip(axes.flat, numeric_columns):
    sns.histplot(original[column], bins=30, kde=True, ax=ax, color="#4C78A8")
    ax.set_title(column.replace("_", " "))
    ax.set_xlabel(column.replace("_", " "))
for ax in axes.flat[len(numeric_columns):]:
    ax.axis("off")
fig.suptitle("Numeric-field distributions", y=1.01)
fig.tight_layout()
plt.show()
""", "fig02_numeric_distributions.png"),
        code("""
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
categorical_plot_data = original[categorical_columns].copy()
for column in categorical_columns:
    categorical_plot_data[column] = categorical_plot_data[column].astype(str).str.replace("_", " ", regex=False)
for ax, column in zip(axes.flat, categorical_columns):
    order = categorical_plot_data[column].value_counts().index
    sns.countplot(data=categorical_plot_data, y=column, order=order, ax=ax, color="#72B7B2")
    ax.set_title(column.replace("_", " "))
    ax.set_ylabel(column.replace("_", " "))
    ax.set_xlabel("Students")
for ax in axes.flat[len(categorical_columns):]:
    ax.axis("off")
fig.suptitle("Categorical-field distributions", y=1.01)
fig.tight_layout()
plt.show()
""", "fig03_categorical_distributions.png"),
        md("""
### 3.3 Correlation, target structure, and imbalance

Correlations are descriptive and do not establish causation. Because `GPA_Change` is continuous, unequal positive and negative counts are target-distribution asymmetry rather than class imbalance. Resampling by sign would change the population represented and the regression estimand.
"""),
        code("""
corr_frame = df[[*numeric_columns, "GPA_Change"]].drop(columns=["Post_Semester_GPA", "Skill_Retention_Score"])
correlations = corr_frame.corr(numeric_only=True)
display(correlations["GPA_Change"].sort_values(ascending=False).to_frame("Correlation with GPA change").round(4))

fig, axes = plt.subplots(1, 2, figsize=(15, 6))
display_names = {
    "Pre_Semester_GPA": "Previous GPA",
    "Weekly_GenAI_Hours": "Weekly GenAI hours",
    "Traditional_Study_Hours": "Traditional study hours",
    "Tool_Diversity": "Tool diversity",
    "Perceived_AI_Dependency": "AI dependency",
    "Anxiety_Level_During_Exams": "Exam anxiety",
    "GPA_Change": "GPA change",
}
plot_correlations = correlations.rename(index=display_names, columns=display_names)
sns.heatmap(plot_correlations, annot=True, fmt=".2f", cmap="vlag", center=0, ax=axes[0])
axes[0].set_title("Numeric correlation matrix")
sns.scatterplot(data=df.sample(5000, random_state=RANDOM_STATE), x="Pre_Semester_GPA", y="GPA_Change", alpha=.25, ax=axes[1])
axes[1].axhline(0, color="black", linestyle="--")
axes[1].set(title="Previous GPA and GPA change", xlabel="Previous-semester GPA", ylabel="Semester GPA change")
fig.tight_layout()
plt.show()
""", "fig04_correlation_and_target_relationships.png"),
        code("""
df["GPA_Direction"] = np.select(
    [df["GPA_Change"] < 0, df["GPA_Change"] > 0],
    ["Decrease", "Increase"], default="Unchanged"
)
direction_summary = (
    df["GPA_Direction"].value_counts().reindex(["Decrease", "Unchanged", "Increase"], fill_value=0)
    .rename("Count").to_frame()
)
direction_summary["Percentage"] = 100 * direction_summary["Count"] / len(df)
display(direction_summary.style.format({"Percentage": "{:.2f}%"}))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
sns.countplot(data=df, x="GPA_Direction", order=["Decrease", "Unchanged", "Increase"], color="#E45756", ax=axes[0])
axes[0].set(title="Observed GPA-change direction", xlabel="Observed direction", ylabel="Students")
sns.histplot(data=df, x="GPA_Change", hue="GPA_Direction", bins=45, element="step", ax=axes[1])
axes[1].axvline(0, color="black", linestyle="--")
axes[1].set(title="Continuous target retained without balancing", xlabel="Semester GPA change", ylabel="Students")
axes[1].legend_.set_title("Observed direction")
fig.tight_layout()
plt.show()
""", "fig05_gpa_direction_imbalance.png"),
    ]

    preparation = [
        md("""
### 4.1 Preparation decision log

Preparation follows field meaning and the intended prediction point. No missing values are manufactured and no valid outliers are deleted. Fold-fitted imputers remain defensive pipeline components for future unseen data.
"""),
        code("""
preparation_log = pd.DataFrame([
    ("Student_ID", "Exclude", "Unique identifier; no transferable predictive meaning"),
    ("Pre_Semester_GPA", "Retain numeric", "Available context predictor"),
    ("Post_Semester_GPA", "Use only to derive target", "Direct component of GPA_Change; predictor leakage"),
    ("Skill_Retention_Score", "Exclude", "Post-outcome measure unavailable at prediction point"),
    ("Burnout_Risk_Level", "Exclude", "Separate derived/post-outcome construct"),
    ("GPA_Change", "Derive target", "Post_Semester_GPA minus Pre_Semester_GPA"),
    ("AI_Hours_Quartile", "EDA only", "Descriptive grouping; models retain continuous hours"),
    ("GPA_Direction", "Diagnostics only", "Audits asymmetric errors; not a classifier target"),
    ("Numeric predictors", "Median imputer + scaler in pipeline", "Fold-safe robustness and linear-model comparability"),
    ("Categorical predictors", "Mode imputer + one-hot encoder in pipeline", "Machine-readable representation with unseen-level handling"),
    ("All valid rows", "Retain", "No missing, duplicate, invalid-range, or proven erroneous records"),
])
preparation_log.columns = ["Field or group", "Action", "Justification"]
display(preparation_log)
"""),
    ]

    # Insert after original EDA figure (source cell 6).
    nb.cells[7:7] = understanding
    # Locate data-preparation feature-definition cell and insert before its markdown.
    prep_index = next(i for i, c in enumerate(nb.cells) if c.cell_type == "markdown" and "## 4. Data preparation" in c.source)
    nb.cells[prep_index + 1:prep_index + 1] = preparation

    # Re-evaluate the selected tuned configuration with all report metrics.
    # RandomizedSearchCV stored only its primary RMSE score, which previously
    # left avoidable blanks in the validation table.
    tuning_index = next(
        i for i, c in enumerate(nb.cells)
        if c.cell_type == "code" and "tuned_cv_rmse = -tuning_search.best_score_" in c.source
    )
    tuned_metric_cells = [
        md("""
### 7.1 Complete cross-validation metrics for the tuned configuration

The search object retains the primary RMSE score used for optimisation. The selected configuration is therefore re-evaluated on the same five folds with MAE, RMSE and R² so its row can be compared without missing values.
"""),
        code("""
tuned_cv_scores = cross_validate(
    tuning_search.best_estimator_,
    X_train,
    y_train,
    cv=cv,
    scoring={
        "MAE": "neg_mean_absolute_error",
        "RMSE": "neg_root_mean_squared_error",
        "R2": "r2",
    },
    n_jobs=-1,
)
tuned_cv_summary = pd.Series({
    "CV MAE": -tuned_cv_scores["test_MAE"].mean(),
    "CV RMSE": -tuned_cv_scores["test_RMSE"].mean(),
    "CV R2": tuned_cv_scores["test_R2"].mean(),
    "R2 standard deviation": tuned_cv_scores["test_R2"].std(ddof=1),
}, name="Tuned histogram gradient boosting")
display(tuned_cv_summary.to_frame().T.style.format("{:.4f}"))
"""),
    ]
    nb.cells[tuning_index + 1:tuning_index + 1] = tuned_metric_cells

    # Direction diagnostics follow residual analysis after execution variables exist.
    residual_index = next(i for i, c in enumerate(nb.cells) if c.cell_type == "code" and "residual_summary =" in c.source)
    direction_cells = [
        md("""
### 9.1 Direction-aware error analysis

Overall mean error can conceal unequal performance across an asymmetric target. Metrics are therefore reported separately for observed GPA decreases, unchanged values, and increases. These are diagnostics on the same untouched test set, not separately trained models.
"""),
        code("""
direction_test = pd.DataFrame({
    "Actual": np.asarray(y_test),
    "Predicted": np.asarray(best_prediction),
})
direction_test["Direction"] = np.select(
    [direction_test["Actual"] < 0, direction_test["Actual"] > 0],
    ["Decrease", "Increase"], default="Unchanged"
)
direction_test["Residual"] = direction_test["Actual"] - direction_test["Predicted"]
direction_test["Absolute error"] = direction_test["Residual"].abs()
direction_test["Squared error"] = direction_test["Residual"] ** 2

direction_error_summary = (
    direction_test.groupby("Direction", observed=True)
    .agg(
        Count=("Actual", "size"),
        MAE=("Absolute error", "mean"),
        MSE=("Squared error", "mean"),
        Mean_residual=("Residual", "mean"),
        Median_residual=("Residual", "median"),
    )
)
direction_error_summary["RMSE"] = np.sqrt(direction_error_summary.pop("MSE"))
direction_error_summary = direction_error_summary.reindex(["Decrease", "Unchanged", "Increase"]).dropna(how="all")
display(direction_error_summary.style.format({"MAE": "{:.4f}", "RMSE": "{:.4f}", "Mean_residual": "{:+.4f}", "Median_residual": "{:+.4f}"}))

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
plot_errors = direction_error_summary.reset_index().melt(id_vars=["Direction"], value_vars=["MAE", "RMSE"], var_name="Metric", value_name="Error")
sns.barplot(data=plot_errors, x="Direction", y="Error", hue="Metric", ax=axes[0])
axes[0].set_title("Test error by observed GPA direction")
sns.boxplot(data=direction_test, x="Direction", y="Residual", order=["Decrease", "Unchanged", "Increase"], ax=axes[1])
axes[1].axhline(0, color="black", linestyle="--")
axes[1].set_title("Residual distribution by direction")
fig.tight_layout()
plt.show()
""", "fig09_direction_specific_errors.png"),
    ]
    nb.cells[residual_index + 1:residual_index + 1] = direction_cells

    # Quantify sampling uncertainty on the untouched test predictions. The
    # paired comparison resamples rows once per iteration so both models are
    # evaluated on identical bootstrap samples.
    test_index = next(
        i for i, c in enumerate(nb.cells)
        if c.cell_type == "code" and "best_prediction = predictions[best_model_name]" in c.source
    )
    uncertainty_cells = [
        md("""
### 8.1 Bootstrap uncertainty on reserved-test performance

Percentile bootstrap intervals quantify sampling uncertainty for the selected model's test metrics. A paired bootstrap also compares its RMSE with random forest using the same resampled rows. These intervals describe uncertainty conditional on this test sample and do not resolve uncertainty about the dataset's undocumented provenance.
"""),
        code("""
BOOTSTRAP_REPETITIONS = 2000
bootstrap_rng = np.random.default_rng(RANDOM_STATE)
y_test_array = np.asarray(y_test)
hgb_prediction = np.asarray(best_prediction)
rf_prediction = np.asarray(predictions["Random forest"])

bootstrap_rows = []
for _ in range(BOOTSTRAP_REPETITIONS):
    indices = bootstrap_rng.integers(0, len(y_test_array), len(y_test_array))
    actual = y_test_array[indices]
    hgb = hgb_prediction[indices]
    rf = rf_prediction[indices]
    hgb_rmse = mean_squared_error(actual, hgb) ** 0.5
    bootstrap_rows.append({
        "MAE": mean_absolute_error(actual, hgb),
        "RMSE": hgb_rmse,
        "R2": r2_score(actual, hgb),
        "RMSE improvement over random forest": (mean_squared_error(actual, rf) ** 0.5) - hgb_rmse,
    })

bootstrap_results = pd.DataFrame(bootstrap_rows)
bootstrap_intervals = pd.DataFrame({
    "Estimate": [
        mean_absolute_error(y_test_array, hgb_prediction),
        mean_squared_error(y_test_array, hgb_prediction) ** 0.5,
        r2_score(y_test_array, hgb_prediction),
        (mean_squared_error(y_test_array, rf_prediction) ** 0.5)
        - (mean_squared_error(y_test_array, hgb_prediction) ** 0.5),
    ],
    "95% lower": bootstrap_results.quantile(0.025).values,
    "95% upper": bootstrap_results.quantile(0.975).values,
}, index=bootstrap_results.columns)
display(bootstrap_intervals.style.format("{:.4f}"))
"""),
    ]
    nb.cells[test_index + 1:test_index + 1] = uncertainty_cells
    nb.metadata["source_notebook"] = str(SOURCE.relative_to(ROOT)).replace("\\", "/")
    nb.metadata["source_sha256"] = SOURCE_SHA256
    return nb


def execute_and_export(nb: nbformat.NotebookNode) -> None:
    client = NotebookClient(
        nb,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
        allow_errors=False,
    )
    client.execute()
    nbformat.write(nb, OUTPUT)
    ASSETS.mkdir(parents=True, exist_ok=True)
    for cell in nb.cells:
        filename = cell.metadata.get("report_figure")
        if not filename:
            continue
        images = [o.get("data", {}).get("image/png") for o in cell.get("outputs", [])]
        images = ["".join(x) if isinstance(x, list) else x for x in images if x]
        if len(images) != 1:
            raise RuntimeError(f"Expected one PNG for {filename}; found {len(images)}")
        (ASSETS / filename).write_bytes(base64.b64decode(images[0]))


if __name__ == "__main__":
    notebook = build()
    execute_and_export(notebook)
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({sha256(OUTPUT)})")
    print(f"Notebook 05 unchanged: {sha256(SOURCE) == SOURCE_SHA256}")

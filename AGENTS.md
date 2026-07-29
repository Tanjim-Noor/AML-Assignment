# AML Assignment Workspace

## Project Purpose

This workspace is for developing the Applied Machine Learning assignment step by step. The work should regularly refer back to the class learning materials, apply those lab patterns to candidate datasets, and then extend beyond the labs where useful for a stronger final implementation.

The final outcome should include:

- a selected dataset and cleaned machine learning workflow,
- a final assignment implementation that merges and improves the learning-material experiments,
- a Typst report written against the assignment requirements and marking scheme.

## Directory Structure

```text
AML Assignment/
|-- AGENTS.md
|-- .gitattributes
|-- .gitignore
|-- Assignment Requirements/
|   |-- CT046-3-M-AML_Assignment Question.md
|   `-- CT046-3-M-AML_Assignment Marking Scheme and Minimum Document Requirements.md
|-- Datasets/
|   |-- AI Workforce Displacement 2020–2026/
|   |   |-- README.md
|   |   `-- ai_workforce_displacement_global_2020_2026.csv
|   |-- Coffee Shops Sales Data/
|   |   |-- README.md
|   |   `-- Project.csv
|   |-- Global Urban Air Quality & Pollution Time-Series/
|   |   |-- README.md
|   |   `-- global_urban_smog_pm25_hourly.csv
|   |-- Impact of AI on Students/
|   |   |-- README.md
|   |   `-- ai_student_impact_dataset.csv
|   |-- LLM Hallucination/
|   |   |-- README.md
|   |   `-- llm_hallucination_dataset_v1.csv
|   `-- Student AI Tools vs Exam scores/
|       |-- README.md
|       `-- students_ai_usage.csv
|-- Learning Materials/
|   |-- Lab Helper Docs/
|   |-- Lab 1 - Installing IDE_Data Loading/
|   |-- Lab 2 - Data Understanding/
|   |-- Lab 3 - Data Preprocessing/
|   |-- Lab 4 - Naive Bayes/
|   |-- Lab 5 - Decision Tree/
|   |-- Lab 6 - Linear Regression/
|   |-- Lab 7 - Cross Validation/
|   |-- Lab 7 - Logistic Regression/
|   |-- Lab 8 - SVM/
|   |-- Lab 9 - Neural Network/
|   |-- Lab 10 - RF/
|   |-- Lab 11 - Ensemble Models/
|   |-- Lab 12 - K Means Clustering/
|   `-- Lab 13 - Univariate Time Series Analysis/
|-- Learning Materials Application on Assigment/
|   |-- AI Workforce Displacement 2020-2026/
|   |   |-- README.md
|   |   |-- Lab 01 - Data Loading/
|   |   |   `-- lab_01_data_loading.ipynb
|   |   `-- Lab 02 - Data Understanding/
|   |       `-- lab_02_data_understanding.ipynb
|   |-- Global Urban Air Quality and Pollution Time-Series/
|   |   |-- README.md
|   |   |-- Lab 01 - Data Loading/
|   |   |   `-- lab_01_data_loading.ipynb
|   |   |-- Lab 02 - Data Understanding/
|   |   |   `-- lab_02_data_understanding.ipynb
|   |   |-- Lab 03 - Data Preprocessing/
|   |   |   `-- lab_03_data_preprocessing.ipynb
|   |   |-- Lab 04 - Naive Bayes/
|   |   |   `-- lab_04_naive_bayes.ipynb
|   |   |-- Lab 05 - Decision Tree/
|   |   |   `-- lab_05_decision_tree.ipynb
|   |   |-- Lab 06 - Linear Regression/
|   |   |   `-- lab_06_linear_regression.ipynb
|   |   |-- Lab 07 - Cross Validation/
|   |   |   `-- lab_07_cross_validation.ipynb
|   |   |-- Lab 07 - Logistic Regression/
|   |   |   `-- lab_07_logistic_regression.ipynb
|   |   |-- Lab 08 - SVM/
|   |   |   `-- lab_08_svm.ipynb
|   |   |-- Lab 09 - Neural Network/
|   |   |   `-- lab_09_neural_network.ipynb
|   |   |-- Lab 10 - RF/
|   |   |   `-- lab_10_random_forest.ipynb
|   |   |-- Lab 11 - Ensemble Models/
|   |   |   `-- lab_11_ensemble_models.ipynb
|   |   |-- Lab 12 - K Means Clustering/
|   |   |   `-- lab_12_k_means_clustering.ipynb
|   |   `-- Lab 13 - Univariate Time Series Analysis/
|   |       `-- lab_13_univariate_time_series_analysis.ipynb
|   |-- Impact of AI on Students/
|   |   |-- README.md
|   |   |-- Lab 01 - Data Loading/
|   |   |   `-- lab_01_data_loading.ipynb
|   |   |-- Lab 02 - Data Understanding/
|   |   |   `-- lab_02_data_understanding.ipynb
|   |   |-- Lab 03 - Data Preprocessing/
|   |   |   `-- lab_03_data_preprocessing.ipynb
|   |   |-- Lab 04 - Naive Bayes/
|   |   |   `-- lab_04_naive_bayes.ipynb
|   |   |-- Lab 05 - Decision Tree/
|   |   |   `-- lab_05_decision_tree.ipynb
|   |   |-- Lab 06 - Linear Regression/
|   |   |   `-- lab_06_linear_regression.ipynb
|   |   |-- Lab 07 - Cross Validation/
|   |   |   `-- lab_07_cross_validation.ipynb
|   |   |-- Lab 07 - Logistic Regression/
|   |   |   `-- lab_07_logistic_regression.ipynb
|   |   |-- Lab 08 - SVM/
|   |   |   `-- lab_08_svm.ipynb
|   |   |-- Lab 09 - Neural Network/
|   |   |   `-- lab_09_neural_network.ipynb
|   |   |-- Lab 10 - RF/
|   |   |   `-- lab_10_random_forest.ipynb
|   |   |-- Lab 11 - Ensemble Models/
|   |   |   `-- lab_11_ensemble_models.ipynb
|   |   `-- Lab 12 - K Means Clustering/
|   |       `-- lab_12_k_means_clustering.ipynb
|   |-- LLM Hallucination/
|   |   |-- README.md
|   |   |-- Lab 01 - Data Loading/
|   |   |   `-- lab_01_data_loading.ipynb
|   |   `-- Lab 02 - Data Understanding/
|   |       `-- lab_02_data_understanding.ipynb
|   `-- Student AI Tools vs Exam Scores/
|       |-- README.md
|       |-- Lab 01 - Data Loading/
|       |   `-- lab_01_data_loading.ipynb
|       `-- Lab 02 - Data Understanding/
|           `-- lab_02_data_understanding.ipynb
|-- Final Assignment/
|   |-- README.md
|   |-- dataset_selection_rubric.md
|   |-- explanation.md
|   |-- _archive/
|   |   `-- global_urban_air_quality_2026-06-27/
|   |       |-- README.md
|   |       |-- dataset_selection_rubric.md
|   |       `-- notebooks/
|   |-- Deep Learning Experiments/
|   |   |-- README.md
|   |   |-- 01_category_embedding_mlp.ipynb
|   |   |-- 02_ft_transformer.ipynb
|   |   `-- 03_tabm.ipynb
|   `-- notebooks/
|       |-- 00_gpu_runtime_diagnostics.ipynb
|       |-- 01_burnout_risk_multiclass_classifier.ipynb
|       |-- 02_skill_retention_regression.ipynb
|       |-- 03_gpa_change_regression.ipynb
|       |-- 04_gpa_decline_classifier.ipynb
|       |-- 05_essential_gpa_change_regression.ipynb
|       `-- 06_comprehensive_gpa_change_regression.ipynb
|-- academic-research/
|   |-- research-passport.yaml
|   |-- writing-brief.md
|   |-- rubric-evidence-matrix.md
|   |-- claim-evidence-map.md
|   |-- revision-ledger.md
|   |-- literature/
|   `-- reviews/
|-- Assignment Report/
|   |-- README.md
|   |-- AML_Assignment_Report.pdf
|   |-- references.bib
|   |-- _backup/
|   |-- assets/
|   |-- sections/
|   `-- typst/
|       |-- main.typ
|       |-- metadata.typ
|       |-- template.typ
|       |-- front-matter/
|       |-- sections/
|       `-- back-matter/
|-- scripts/
|   |-- install_notebook_git_filter.ps1
|   `-- strip_assignment_notebooks.ps1
`-- .agents/
    `-- skills/
        `-- typst/
            |-- typst-skill/
            |-- typst-author/
            `-- touying-author/
```

- `Assignment Requirements/` contains the assignment brief, marking scheme, cover documents, and minimum report requirements. Use the Markdown knowledgebase copies of the assignment question and marking scheme as the first source of truth for dataset selection, machine learning implementation, and report planning.
- `Datasets/` contains candidate datasets. Treat original dataset files as raw inputs; avoid editing them directly.
- `Learning Materials/` contains class labs, helper documents, notebooks, and reference datasets. Use these to guide the staged implementation.
- `Learning Materials Application on Assigment/` is the exploratory workspace for applying lab concepts to the assignment datasets step by step.
- `Final Assignment/` is for the polished final implementation. Move only cleaned, intentional, reproducible work here after it has been explored elsewhere. Use `Final Assignment/dataset_selection_rubric.md` as the canonical dataset-selection rationale. Final student-impact versions should be standalone notebooks under `Final Assignment/notebooks/`, with all EDA, preprocessing, modelling, validation, plots, uncertainty, and interpretation shown inline in notebook cells. Treat `Final Assignment/_archive/` as historical reference, not active implementation.
- `academic-research/` contains the UARS Research Passport, writing controls, literature-search evidence, reproducibility records, integrity audits and review history for the assignment report.
- `Assignment Report/` contains the reviewable Markdown source, current submission DOCX, modular Typst assembly and rendered PDF. Use `README.md` for merge order and status, `_backup/` for superseded recoverable DOCX revisions, `references.bib` as canonical citation metadata, `sections/` for ordered modules, `AML_Assignment_Report_Merged.md` for generated single-file review, `assets/` for reproducible figures, `typst/main.typ` as the Typst entry point, and `AML_Assignment_Report.pdf` as the compiled review artifact.
- `.agents/skills/typst/` contains the local Typst-related skills for report work: `typst`, `typst-author`, and `touying-author`.

## Working Notes

- Start requirement-sensitive work by checking `Assignment Requirements/`.
- Prefer the Markdown knowledgebase files in `Assignment Requirements/` for day-to-day planning, implementation, and report-writing decisions; refer back to the original Word documents if formatting or source fidelity must be checked.
- The current final dataset selection is `Impact of AI on Students`. The previous `Global Urban Air Quality & Pollution Time-Series` final implementations are archived, and `AI Workforce Displacement 2020-2026` remains an additional backup unless the user changes direction.
- Use `Learning Materials Application on Assigment/` for experiments and learning-driven iterations.
- Use `Final Assignment/` for the final notebook-only assignment versions that support the report.
- For final student-impact assignment versions, do not create shared pipeline scripts, CLI runners, generated result folders, saved plot files, CSV metric exports, model dumps, or Markdown run summaries. Each notebook should be standalone and display all tables, plots, training results, validation metrics, uncertainty, and recommendations inline when run.
- Treat `Final Assignment/notebooks/06_comprehensive_gpa_change_regression.ipynb` as the reported comprehensive implementation. It extends byte-preserved notebook 05 with complete EDA, preparation evidence and direction-specific bias diagnostics, and retains executed outputs.
- Keep `Final Assignment/notebooks/05_essential_gpa_change_regression.ipynb` byte-unchanged as the concise historical baseline unless the user explicitly authorises changes.
- Treat `Final Assignment/Deep Learning Experiments/` as executed GPU comparison work that supplements notebook 05 rather than replacing it. FT-Transformer is the strongest tested neural model, but its validation gain is below the material-improvement gate, so HGB remains the recommended final model.
- The deep-learning experiment environment uses `rtdl-revisiting-models==0.0.2` and `tabm==0.0.3`. Do not add `pytorch-tabular` to this workspace because its resolved dependency set would downgrade pandas 3.0.3.
- Treat the student-impact dataset as a Kaggle-provided modelling dataset with undocumented collection and real-versus-synthetic provenance. Do not make causal or population-level claims about AI use, GPA, retention, anxiety, dependency, policy, or burnout.
- Drop `Student_ID` from modelling, prevent post-outcome leakage, exclude exam anxiety from the primary early-risk burnout feature set, and never use post-semester GPA to predict derived GPA change or decline.
- Do not manufacture missing values or corruptions to compensate for the dataset's perfect cleanliness.
- Do not create a Lab 13 time-series application for the student-impact dataset unless a defensible temporal or repeated-student field is added later.
- Use `Assignment Report/` for report writing and Typst compilation work. Preserve the Markdown module order and status recorded in `Assignment Report/README.md`.
- Treat `Assignment Report/references.bib` as canonical bibliographic metadata and keep `sections/09_references.md` reconciled with it for human review.
- Treat `Assignment Report/typst/metadata.typ` as the canonical cover and declaration metadata file. Before submission, replace the student-name, student-id and declaration-date placeholders.
- Compile the report from the workspace root with `typst compile --root "Assignment Report" "Assignment Report\typst\main.typ" "Assignment Report\AML_Assignment_Report.pdf"`.
- Treat the Typst assembly and rendered PDF as `verified`, but not `submission-ready`, until the student metadata placeholders are completed and the student performs the final submission review.
- Use the workspace virtual environment at `.venv/` for Python execution and package installation. On Windows/PowerShell, run scripts with `.venv\Scripts\python.exe path\to\script.py` and install packages with `.venv\Scripts\python.exe -m pip install package-name`. Do not install assignment dependencies into the global Python environment unless explicitly requested.
- Keep notebook metadata noise out of commits by using the repo `nbstripout` filter in `.gitattributes` for `*.ipynb` files.
- If the local Git filter config is missing or stale, run `.\scripts\install_notebook_git_filter.ps1` from the workspace root.
- Before commit, run `.\scripts\strip_assignment_notebooks.ps1` to normalize notebook metadata/output in assignment notebook scopes. The script must preserve the executed outputs of notebooks 05 and 06 and the three notebooks under `Final Assignment/Deep Learning Experiments/`.
- Keep folder boundaries stable unless the user explicitly asks to reorganize the workspace.
- Microsoft Office temporary and lock files, such as files beginning with `~$`, are ignored and should not be committed.

## Agent Operating Guidelines

- After every major completed change, suggest an appropriate commit message. Use a concise one-line message for small changes, and use a detailed message with bullet points or nested bullet points when the staged changes span multiple folders, behaviors, or decisions.
- When the workspace file structure changes, update the `Directory Structure` section in this file.
- When new durable project guidelines are introduced, add them to this file.
- Keep this file focused on essential, durable guidance; do not add temporary task notes.
- Do not create `instructions.md` or `rules.md` unless this file becomes too large or the project needs separate human documentation and agent rules.

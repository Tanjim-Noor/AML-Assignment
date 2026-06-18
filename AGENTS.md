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
|   |-- Global Urban Air Quality & Pollution Time-Series/
|   |   |-- README.md
|   |   `-- global_urban_smog_pm25_hourly.csv
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
|   `-- dataset_selection_rubric.md
|-- Assignment Report/
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
- `Final Assignment/` is for the polished final implementation. Move only cleaned, intentional, reproducible work here after it has been explored elsewhere. Use `Final Assignment/dataset_selection_rubric.md` as the canonical dataset-selection rationale.
- `Assignment Report/` is for the Typst report source, report assets, generated figures/tables, and exported report output.
- `.agents/skills/typst/` contains the local Typst-related skills for report work: `typst`, `typst-author`, and `touying-author`.

## Working Notes

- Start requirement-sensitive work by checking `Assignment Requirements/`.
- Prefer the Markdown knowledgebase files in `Assignment Requirements/` for day-to-day planning, implementation, and report-writing decisions; refer back to the original Word documents if formatting or source fidelity must be checked.
- The current final dataset selection is `Global Urban Air Quality & Pollution Time-Series`; use `AI Workforce Displacement 2020-2026` only as the backup unless the user changes the final assignment direction.
- Use `Learning Materials Application on Assigment/` for experiments and learning-driven iterations.
- Use `Final Assignment/` for the final notebook/script pipeline and outputs that should support the report.
- Use `Assignment Report/` for report writing and Typst compilation work.
- Use the workspace virtual environment at `.venv/` for Python execution and package installation. On Windows/PowerShell, run scripts with `.venv\Scripts\python.exe path\to\script.py` and install packages with `.venv\Scripts\python.exe -m pip install package-name`. Do not install assignment dependencies into the global Python environment unless explicitly requested.
- Keep notebook metadata noise out of commits by using the repo `nbstripout` filter in `.gitattributes` for `*.ipynb` files.
- If the local Git filter config is missing or stale, run `.\scripts\install_notebook_git_filter.ps1` from the workspace root.
- Before commit, run `.\scripts\strip_assignment_notebooks.ps1` to normalize notebook metadata/output in assignment notebook scopes.
- Keep folder boundaries stable unless the user explicitly asks to reorganize the workspace.
- Microsoft Office temporary and lock files, such as files beginning with `~$`, are ignored and should not be committed.

## Agent Operating Guidelines

- After every major completed change, suggest an appropriate commit message. Use a concise one-line message for small changes, and use a detailed message with bullet points or nested bullet points when the staged changes span multiple folders, behaviors, or decisions.
- When the workspace file structure changes, update the `Directory Structure` section in this file.
- When new durable project guidelines are introduced, add them to this file.
- Keep this file focused on essential, durable guidance; do not add temporary task notes.
- Do not create `instructions.md` or `rules.md` unless this file becomes too large or the project needs separate human documentation and agent rules.

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
|-- .gitignore
|-- Assignment Requirements/
|   |-- CT046-3-M-AML_Assignment Question.md
|   `-- CT046-3-M-AML_Assignment Marking Scheme and Minimum Document Requirements.md
|-- Datasets/
|   |-- AI Workforce Displacement 2020-2026/
|   |-- Global Urban Air Quality & Pollution Time-Series/
|   |-- LLM Hallucination/
|   `-- Student AI Tools vs Exam scores/
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
|-- Final Assignment/
|-- Assignment Report/
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
- `Final Assignment/` is for the polished final implementation. Move only cleaned, intentional, reproducible work here after it has been explored elsewhere.
- `Assignment Report/` is for the Typst report source, report assets, generated figures/tables, and exported report output.
- `.agents/skills/typst/` contains the local Typst-related skills for report work: `typst`, `typst-author`, and `touying-author`.

## Working Notes

- Start requirement-sensitive work by checking `Assignment Requirements/`.
- Prefer the Markdown knowledgebase files in `Assignment Requirements/` for day-to-day planning, implementation, and report-writing decisions; refer back to the original Word documents if formatting or source fidelity must be checked.
- Use `Learning Materials Application on Assigment/` for experiments and learning-driven iterations.
- Use `Final Assignment/` for the final notebook/script pipeline and outputs that should support the report.
- Use `Assignment Report/` for report writing and Typst compilation work.
- Keep folder boundaries stable unless the user explicitly asks to reorganize the workspace.
- Microsoft Office temporary and lock files, such as files beginning with `~$`, are ignored and should not be committed.

## Agent Operating Guidelines

- After every major completed change, suggest an appropriate commit message. Use a concise one-line message for small changes, and use a detailed message with bullet points or nested bullet points when the staged changes span multiple folders, behaviors, or decisions.
- When the workspace file structure changes, update the `Directory Structure` section in this file.
- When new durable project guidelines are introduced, add them to this file.
- Keep this file focused on essential, durable guidance; do not add temporary task notes.
- Do not create `instructions.md` or `rules.md` unless this file becomes too large or the project needs separate human documentation and agent rules.

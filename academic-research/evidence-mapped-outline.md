# Evidence-Mapped Report Outline

Status: approved through the distinction-level implementation plan and the
explicit approval of corpus `aml-report-corpus-v1` on 2026-07-01.

| Module | Communicative purpose | Main claims and evidence | Tables and figures | Target words |
|---|---|---|---|---:|
| Title and Abstract | State the predictive problem and summarise the complete study. | Dataset and methods from notebook 05; final HGB metrics; feature-set ablation; causal limitation. | None. | 250-300 |
| Introduction, Aim and Objectives | Explain GPA-change prediction to a non-specialist and establish the bounded contribution. | Higher-education AI context (S01-S04); dataset context; exact research question; notebook-aligned aim and six objectives. | None. | 750-850 |
| Related Works | Demonstrate a wide, critical and reproducible review rather than a catalogue. | Search protocol/log; mixed GenAI findings (S03-S07); AI literacy and prompt skill (S08-S10); prediction and validation (S11-S15); same-dataset evidence gap. | Search summary and 15-source comparison table. | 1,800-2,000 |
| Methods | Explain the completed predictive design and why it fits the question. | Notebook cells 3-15; cross-sectional predictive boundary; target; features; split; fold-local pipelines; metrics; tuning. | Compact workflow table. | 650-750 |
| Dataset Preparation | Report integrity checks, EDA, target construction and legitimate preprocessing. | Dataset README and notebook cells 5-9; 50,000 x 16; no missing/duplicates; target distribution; leakage exclusions; perfect-cleanliness limitation. | Figure 1 and schema/preparation table. | 600-700 |
| Model Implementation | Explain each baseline/model, pipeline and optimisation choice. | Notebook cells 11-17; model parameters and tuning space; S14-S15 for model-comparison and tuning context. | Model specification and selected-parameter tables. | 900-1,000 |
| Model Validation | Present selection evidence before final confirmation. | Notebook cells 13, 15, 17 and 19; exact rerun record; CV variability; test metrics; residual behaviour. | Table of CV/test results; Figures 2 and 3. | 600-700 |
| Analysis and Recommendations | Answer the research question and critically integrate experiment and literature. | Feature-set ablation; nonlinear gains; tuning increment; EDA; permutation importance; S05-S10 and S11-S14; provenance limits. | Feature-set table and Figure 4. | 1,000-1,150 |
| Conclusion | Evaluate all objectives and define implications and future work without new evidence. | Completed report and objective-to-result mapping. | None. | 350-450 |
| References | Provide a reconciled APA 7 list from canonical BibTeX metadata. | Approved sources, dataset and software citation. | None. | Excluded |
| Acknowledgements | Record factual resources and unresolved disclosure details. | Dataset, learning resources, software and explicit placeholders. | None. | 60-100 |

The drafting order is Methods, Dataset Preparation, Model Implementation, Model
Validation, Related Works, Analysis, Introduction, Conclusion and Abstract.
References and acknowledgements are assembled alongside the prose. Results are
reported as predictive associations only.

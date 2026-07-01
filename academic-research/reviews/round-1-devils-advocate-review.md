# Round 1 Devil's-Advocate Review

Review mode: `full`
Manuscript: draft v1, manifest
`ce2d8065fbf5006dfc9adf9745dec531322ae829dcc66bb78cb7419ef5c00388`
Role: adversarial claim and failure-mode stress test
Recommendation: **Minor revision**
Confidence: **4/5**

## Stress tests

### A1 — Could the preferred model have been selected from test performance?

Priority: **P1 major**

Notebook code constructs `best_model_name` from the sorted test table. This
could be read as test-guided model selection. The manuscript's intended logic
is defensible only because HGB was the leading family in untuned CV and the
tuned configuration had the best search CV RMSE before test confirmation.

Required action: state this chronology explicitly and acknowledge that the
helper variable uses the test ranking for downstream residual and importance
plots. Do not claim that the code implements a pristine single-look test
protocol.

### A2 — Could feature importance be interpreted as policy evidence?

Priority: **P2 moderate**

The manuscript repeatedly rejects causality, explains correlated-feature
substitution and recommends external validation. This stress test is passed.
Preserve the statements that `Primary_Use_Case` and `Weekly_GenAI_Hours`
importance cannot support prescriptions.

### A3 — Is “systematic review” overstated?

Priority: **P2 moderate**

The assignment rubric uses “systematic”, but the search inspected bounded
result subsets and encountered API degradation. The manuscript accurately
calls the work a structured multi-database search and explicitly rejects full
PRISMA status. This stress test is passed. Do not relabel it as a formal
systematic review during later formatting.

### A4 — Can the dataset support claims about real students?

Priority: **P2 moderate**

No. The manuscript makes the provenance problem central in the Abstract,
Introduction, Dataset Preparation, Analysis and Conclusion. This stress test is
passed, provided no later edit replaces “within the supplied dataset” with a
general statement about university students.

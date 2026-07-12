# Literature Search Log

| Search ID | Date | Database | Query family | Exact query or endpoint parameters | Results reviewed | Eligible before deduplication | Included core sources | Notes |
|---|---|---|---|---|---:|---:|---:|---|
| ERIC-Q1 | 2026-07-01 | ERIC API | Generative AI and academic outcomes | `"generative AI" AND "academic performance" AND "higher education"` | 5 of 11 returned | 4 | 3 | Exact API total: 11 |
| ERIC-Q2 | 2026-07-01 | ERIC API | AI literacy and prompting | `("AI literacy" OR "prompt engineering") AND student AND (achievement OR performance)` | 5 of 38 returned | 4 | 3 | First 20 records retrieved; first five inspected |
| ERIC-Q3 | 2026-07-01 | ERIC API | Academic-performance prediction | `"machine learning" AND (GPA OR "academic performance") AND "higher education"` | 5 of 31 returned | 4 | 4 | First 20 records retrieved; first five inspected |
| ERIC-Q4 | 2026-07-01 | ERIC API | Exact dataset | `"Impact of Ai on Students" OR "ai_student_impact_dataset.csv" OR laveshjadon` | 2 of 2 returned | 0 | 0 | Both hits were false positives unrelated to the Kaggle file |
| CR-Q1 | 2026-07-01 | Crossref REST API | Generative AI and academic outcomes | `query.bibliographic="generative AI" AND "academic performance" AND "higher education"; from-pub-date=2016-01-01; until-pub-date=2026-12-31` | First 5 of 45 returned | 3 | 0 directly | Broad query generated substantial noise; targeted DOI verification was used for admission |
| CR-Q2 | 2026-07-01 | Crossref REST API | AI literacy and prompting | `query.bibliographic=("AI literacy" OR "prompt engineering") AND student AND (achievement OR performance)` | First 5 of 50 returned | 2 | 0 directly | Broad query generated substantial noise |
| CR-Q3 | 2026-07-01 | Crossref REST API | Academic-performance prediction | `query.bibliographic="machine learning" AND (GPA OR "academic performance") AND "higher education"` | First 5 of 50 returned | 2 | 0 directly | Broad query generated substantial noise |
| CR-Q4 | 2026-07-01 | Crossref REST API | Exact dataset | `query.bibliographic="Impact of Ai on Students" OR "ai_student_impact_dataset.csv" OR laveshjadon` | First 5 of 46 returned | 0 | 0 | No matching scholarly dataset study |
| CR-DOI | 2026-07-01 | Crossref REST API | Candidate verification | `/works/{doi}` for each shortlisted DOI | 15 | 15 | 15 | All DOI/title/author/year pairs resolved and matched |
| S2-Q1 | 2026-07-01 | Semantic Scholar web index | Generative AI and academic outcomes | Domain-limited search for `generative AI academic performance higher education` | 7 | 5 | 2 | Anonymous Graph API returned HTTP 429; public Semantic Scholar result pages were inspected instead |
| S2-Q2 | 2026-07-01 | Semantic Scholar web index | AI literacy and prompting | Domain-limited search for `AI literacy prompt engineering student academic outcomes` | 3 | 2 | 1 | Exact result totals unavailable through the web index |
| S2-Q3 | 2026-07-01 | Semantic Scholar web index | Academic-performance prediction | Domain-limited search for `machine learning prediction GPA academic performance higher education` | 3 | 1 | 0 | Crossref and publisher pages supplied the final prediction sources |
| S2-Q4 | 2026-07-01 | Semantic Scholar web index | Exact dataset | Domain-limited search for `"Impact of Ai on Students" laveshjadon` | 0 | 0 | 0 | No result |
| OA-Q1–Q4 | 2026-07-01 | OpenAlex API | All four families | `/works?search=...&filter=from_publication_date:2016-01-01,to_publication_date:2026-12-31` | 0 | 0 | 0 | Anonymous search returned a temporary rate-limit/API-key error; treated as unavailable, not as a negative search result |
| KAGGLE-DATA | 2026-07-01 | Kaggle public API | Exact dataset | `/api/v1/datasets/view/laveshjadon/ai-impact-on-students` | 1 | 1 | Dataset only | Metadata verified: owner Nagi sisiro, updated 2026-05-10 |
| KAGGLE-KERNELS | 2026-07-01 | Kaggle public API | Same-dataset notebooks | `/api/v1/kernels/list?dataset=laveshjadon/ai-impact-on-students` | 0 | 0 | 0 | HTTP 401; no public notebook corpus could be inspected without credentials |

## Screening totals

- Directly inspected discovery records: 50.
- Shortlisted records sent to DOI/title verification: 15.
- DOI/title/author/year matches: 15 of 15.
- Included candidate core sources: 15.
- Included same-dataset comparative studies: 0.

These counts describe a structured assignment review, not a complete PRISMA systematic review. Crossref's broad bibliographic matching produced millions of nominal matches and low precision, so only returned records actually inspected are counted here. OpenAlex degradation is recorded rather than interpreted as zero evidence.

## Excluded records

## 13 July 2026 methodological evidence update

Targeted primary-source searches covered scikit-learn and scientific-Python
software papers, Random Forest, Ridge Regression, gradient boosting,
cross-validation, random search and permutation importance. Ten records were
verified through JMLR, JOSS, publisher pages or DOI metadata and registered as
M01--M10 in the source matrix. Searches were stopped when every package and
method making a substantive report claim had authoritative support.

| Record | Stage | Reason |
|---|---|---|
| ERIC Q4 hit: *Reshaping School Cultures* | Title screening | False positive; no relationship to the selected dataset |
| ERIC Q4 hit: *Boon or Bane?* | Title screening | General AI-assisted learning paper; not a same-dataset analysis |
| Crossref Q4 returned records | Title screening | Generic AI-impact records; no exact dataset, filename or creator match |
| HyperAI dataset mirror | Full-page screening | Metadata mirror only; no independent method or benchmark |
| Public Kaggle kernels | Access screening | Kernel listing endpoint required authentication, so methods and outputs could not be verified |
| News, commercial explainers and unsourced webpages | Source-type screening | Not peer-reviewed research or authoritative methodological evidence |
| Studies limited to school pupils | Scope screening | Outside the higher-education population |
| Studies reporting perceptions only | Outcome screening | No relevant learning, performance, literacy or predictive-method contribution |

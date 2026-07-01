# Literature Search Protocol

## Review objective

Identify and critically synthesise recent evidence about generative-AI use and academic outcomes in higher education, predictive modelling of GPA or student performance, and validation practices relevant to the selected regression workflow.

## Databases

1. OpenAlex.
2. Semantic Scholar.
3. ERIC.
4. Crossref.

Publisher or DOI landing pages will be used to verify metadata and claims. The Kaggle dataset page and its public notebooks will be searched separately for same-dataset comparisons.

## Query families

### Q1: Generative AI and academic outcomes

`("generative AI" OR ChatGPT OR "AI tools") AND ("academic performance" OR GPA OR achievement) AND ("higher education" OR university OR undergraduate)`

### Q2: AI-use behaviour and capability

`("AI use" OR "prompt engineering" OR "AI literacy" OR "digital literacy") AND (student OR learner) AND (GPA OR achievement OR learning outcome)`

### Q3: Machine-learning prediction

`("machine learning" OR "educational data mining") AND (predict* OR forecast*) AND (GPA OR "academic performance" OR "student achievement") AND ("higher education" OR university)`

### Q4: Same-dataset evidence

`"Impact of Ai on Students" OR "ai_student_impact_dataset.csv" OR "laveshjadon"`

Database syntax will be adapted without changing the conceptual facets. Every executed query, date, result count and screening decision will be recorded in `search-log.md`.

## Eligibility

### Include

- English-language work published from 2016 through 2026.
- Empirical higher-education studies of AI use, academic performance or learning outcomes.
- Relevant systematic or scoping reviews.
- Machine-learning studies that predict GPA or academic performance and report a defensible evaluation.
- Authoritative methodological sources needed to justify validation, metrics or interpretation.
- Public same-dataset analyses only when methods and results can be inspected.

### Exclude

- Primary/secondary-school-only studies unless they establish a method directly used in the report.
- Opinion, marketing or news content without research evidence.
- Records with unverifiable authorship, title or publication details.
- Studies that discuss AI attitudes without a relevant learning or performance outcome.
- Duplicate reports of the same study.
- Sources available only as an abstract when the required claim cannot be verified.

## Screening and quality appraisal

1. Deduplicate by DOI, then normalised title.
2. Screen title and abstract against eligibility.
3. Inspect full text or a sufficiently complete official manuscript.
4. Record design, sample, setting, variables, models, validation, metrics, findings and limitations.
5. Evaluate leakage risk, sampling limitations, self-report bias, causal overreach and external validity.
6. Map every retained source to one or more report claims.

## Stopping rule

Run all four query families across the named databases and perform backward/forward citation chaining for included core studies. Stop when two consecutive query refinements or citation-chaining passes add no new high-relevance eligible source. Target 12–15 core sources for the report, while retaining excluded-source reasons.

## Synthesis method

Use thematic synthesis rather than a source-by-source catalogue:

1. Generative-AI use and academic outcomes.
2. Quality, purpose and skill of AI use.
3. Conventional study context alongside AI variables.
4. Predictive modelling of student performance.
5. Validation, leakage and interpretability.
6. Evidence gap addressed by notebook 05.

The review will be described as a structured, reproducible multi-database search. It will not claim full PRISMA systematic-review status unless every required PRISMA process is completed.

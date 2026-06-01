# LLM Hallucination Benchmark Dataset

Metadata and local schema notes for `llm_hallucination_dataset_v1.csv`.

## Source Snapshot

| Field | Value |
| --- | --- |
| Official Kaggle page | https://www.kaggle.com/datasets/alitaqishah/llm-hallucination-benchmark-dataset |
| Kaggle title | LLM Hallucination Benchmark Dataset |
| Creator | Syed Ali Taqi (`alitaqishah`) |
| License | CC0-1.0 / Public Domain |
| Version | 1, initial release |
| Last updated on Kaggle | 2026-05-13 |
| Expected update frequency | Weekly |
| Kaggle usability rating | 1.0 |
| Kaggle activity at review time | 1,814 views, 310 downloads, 47 votes, 21 notebooks |
| Local review date | 2026-06-01 |

## What The Dataset Is

This dataset is a small annotated benchmark for studying hallucinations in large language model responses. Each row contains a prompt, an LLM response, model metadata, task/domain labels, hallucination labels, correction information, annotation metadata, mitigation strategy information, and source-verification metadata.

The Kaggle page describes prompts collected from September 2024 through April 2025. It covers five models, eight domains, seven languages, several prompt types, and annotations from human and LLM-based judges. The page also states that a subset of prompts was rerun with mitigation strategies such as RAG, self-consistency, chain-of-thought prompting, and structured prompting.

## Local File Inventory

| File | Rows | Columns | Size | Missing values |
| --- | ---: | ---: | ---: | ---: |
| `llm_hallucination_dataset_v1.csv` | 200 | 25 | 110,261 bytes | 1,025 |

Many missing values are structurally meaningful. For example, non-hallucinated rows do not have hallucination spans or correction text.

## Coverage

| Field | Local values |
| --- | --- |
| Date span | 2024-09-02 to 2025-04-29 |
| Models | 5 |
| Domains | 8 |
| Languages | 7 |
| Prompt types | 5 |
| Rows | 200 |
| Hallucination rate | 69 of 200 rows, 34.5% |

Hallucination-label distribution:

| `hallucination_label` | Meaning | Rows | Share |
| --- | --- | ---: | ---: |
| 0 | No hallucination | 131 | 65.5% |
| 1 | Hallucination | 69 | 34.5% |

Domain distribution:

| Domain | Rows |
| --- | ---: |
| Medicine | 38 |
| Technology | 34 |
| Science | 30 |
| Finance | 30 |
| History | 23 |
| Law | 19 |
| General | 15 |
| Politics | 11 |

Model distribution:

| Model | Rows |
| --- | ---: |
| Llama-3.1-70B | 48 |
| Mistral-Large | 45 |
| GPT-4o | 42 |
| Gemini-1.5-Pro | 34 |
| Claude-3.5-Sonnet | 31 |

Hallucination-type distribution:

| Type | Rows |
| --- | ---: |
| Factual-Contradiction | 24 |
| Overclaim | 18 |
| Unverifiability | 8 |
| Incompleteness | 7 |
| Entity-Error | 4 |
| Outdatedness | 4 |
| Relation-Error | 4 |
| Missing / not hallucinated | 131 |

## Column Dictionary

| Column | Type | Missing | Unique | Values or range | Notes for ML |
| --- | --- | ---: | ---: | --- | --- |
| `record_id` | UUID text | 0 | 200 | 36-character unique values | Row identifier; exclude from modeling. |
| `created_date` | Date text | 0 | 135 | 2024-09-02 to 2025-04-29 | Can support temporal analysis. |
| `model_name` | Categorical text | 0 | 5 | GPT-4o, Mistral-Large, Llama-3.1-70B, Gemini-1.5-Pro, Claude-3.5-Sonnet | Model comparison feature. |
| `model_version` | Categorical text | 0 | 5 | Version identifiers for the five models | Usually redundant with `model_name`. |
| `prompt_id` | Categorical identifier | 0 | 200 | PROMPT_00001 to PROMPT_00200 | Identifier; exclude unless grouping repeated prompts. |
| `prompt_text` | Text | 0 | 53 | Length 23 to 111 characters | Input text feature. |
| `prompt_type` | Categorical text | 0 | 5 | Ambiguous, Direct-Factual, Adversarial, Long-Context, Multi-Hop | Useful predictor. |
| `response_text` | Text | 0 | 53 | Length 38 to 455 characters | Main text feature for NLP modeling. |
| `domain` | Categorical text | 0 | 8 | Medicine, Technology, Science, Finance, Law, History, Politics, General | Domain-risk feature. |
| `task_type` | Categorical text | 0 | 6 | Question-Answering, Open-Generation, Fact-Verification, Summarization, Dialogue, Multi-Hop | Task feature. |
| `language` | Categorical text | 0 | 7 | English, Spanish, French, German, Mandarin, Arabic, Hindi | Language feature; English dominates with 117 rows. |
| `hallucination_label` | Binary integer | 0 | 2 | 0 or 1 | Primary classification target. |
| `hallucination_type` | Categorical text | 131 | 7 | Present only for hallucinated rows | Multi-class target for hallucinated subset; leaks binary label if used as feature. |
| `hallucination_span` | Text | 131 | 18 | Hallucinated phrase/span | Annotation output; do not use as predictor for label detection. |
| `correct_information` | Text | 131 | 18 | Verified correction fact | Annotation output; avoid as predictor. |
| `correction_text` | Text | 131 | 18 | Human-readable correction | Annotation output; avoid as predictor. |
| `severity` | Categorical text | 131 | 3 | Low, Medium, High | Label-side severity; candidate target for hallucinated rows. |
| `domain_risk` | Categorical text | 0 | 3 | Low-Stakes, Medium-Stakes, High-Stakes | Domain risk grouping. |
| `annotator_type` | Categorical text | 0 | 4 | human_expert, human_crowd, llm_judge_gpt4o, llm_judge_claude | Annotation provenance. |
| `annotation_confidence` | Numeric | 0 | 27 | min 0.73, median 0.88, mean 0.881, max 0.99 | Annotation confidence; may be outcome-side metadata. |
| `mitigation_strategy` | Categorical text | 39 | 4 | RAG, Self-Consistency, CoT-Prompting, Structured-Prompt | Strategy applied in subset. |
| `mitigation_applied` | Boolean text | 0 | 2 | True or False | Indicates whether a mitigation was applied. |
| `verified_source` | Categorical text | 0 | 8 | PubMed, SEC-Filing, ArXiv, Wikipedia, Snopes, LegalBench, Human-Expert, Reuters | Verification source. |
| `intrinsic_or_extrinsic` | Categorical text | 131 | 2 | Intrinsic, Extrinsic | Hallucination subtype; label-side metadata. |
| `notes` | Empty field | 200 | 0 | All missing | Drop from modeling. |

## Data Quality Notes

- The dataset is small: 200 rows. It is useful for lab-style NLP experiments but may be too small for the final assignment requirement guidance.
- `prompt_text` and `response_text` have repeated values. There are 53 unique prompt/response texts across 200 records.
- Correction and hallucination-span fields are only populated after the label is known. These fields should not be used as predictors for hallucination detection.
- Missingness in label-side fields is meaningful, not a data-quality failure.

## Machine Learning Fit

Strong assignment directions:

- Binary text classification: predict `hallucination_label` from prompt, response, model, prompt type, domain, task type, and language.
- Multi-class classification: predict `hallucination_type` only for rows where hallucination exists.
- Risk analysis: compare hallucination rates by model, domain, task type, language, and mitigation strategy.
- Text feature engineering: TF-IDF, response length, prompt length, and categorical encodings.

Likely preprocessing:

- Drop identifiers: `record_id`, `prompt_id`.
- Drop outcome-side fields when predicting hallucination: `hallucination_type`, `hallucination_span`, `correct_information`, `correction_text`, `severity`, `intrinsic_or_extrinsic`, and possibly `annotation_confidence`.
- Convert `created_date` to datetime if temporal patterns are studied.
- Use stratified validation because the positive class has only 69 rows.
- Consider simple baselines first because the dataset is small.

## Assignment Suitability

This dataset is interesting and current, but it is much smaller than the assignment's suggested 20k to 50k row guideline. It is better suited for exploratory lab application, NLP demonstrations, or as a secondary comparison dataset rather than the main final assignment dataset.

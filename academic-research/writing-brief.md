# Writing Brief

## Deliverable and stage

A modular Applied Machine Learning assignment report written in separate Markdown files for later review and Typst assembly. The current stage is evidence discovery and architecture; report prose cannot begin until the UARS literature-corpus approval gate is passed.

## Central research question

To what extent do AI-usage variables improve out-of-sample prediction of semester GPA change beyond previous GPA and general study context, and which regression model provides the strongest validated performance?

## Intended contribution

The report will provide a leakage-controlled comparison of regression models for semester GPA change and a direct feature-set ablation that tests whether AI-use variables add predictive information beyond student context. Its contribution is predictive and methodological, not causal.

## Discipline, audience and venue

- Discipline: applied machine learning, educational data mining and generative AI in higher education.
- Audience: APU CT046-3-M-AML lecturer and assignment marker.
- Venue: CT046-3-M-AML Individual Assignment.
- Required standard: distinction-level performance against the supplied marking rubric.

## Language, style and format

- British English.
- APA 7 author-date citations.
- Separate Markdown section files.
- 7,000–8,000 words excluding references and appendices.
- Later Typst assembly, pagination and PDF rendering are outside this phase.

## Canonical evidence

| Class | Artifact | Status |
|---|---|---|
| Instruction | Assignment question Markdown | Verified and hash-locked |
| Instruction | Marking scheme Markdown | Verified and hash-locked |
| Primary evidence | Student-impact CSV | Verified; 50,000 × 16 |
| Primary evidence | Notebook 05 | Selected final implementation; hash-locked |
| Author material | `Final Assignment/explanation.md` | Checked against saved notebook outputs |
| Secondary evidence | External literature corpus | Not yet built |

## Modelling boundary

Notebook 05 is the sole reported implementation. The deep-learning experiments are excluded except as possible future work. The dataset has undocumented collection, geography, sampling, ethics and real-versus-synthetic provenance. All report claims must therefore remain limited to predictive associations within the supplied file.

## Report architecture and word budget

| Section | Target words |
|---|---:|
| Title and Abstract | 250–300 |
| Introduction, Aim and Objectives | 750–850 |
| Related Works | 1,800–2,000 |
| Methods | 650–750 |
| Dataset Preparation | 600–700 |
| Model Implementation | 900–1,000 |
| Model Validation | 600–700 |
| Analysis and Recommendations | 1,000–1,150 |
| Conclusion | 350–450 |
| Acknowledgements | 60–100 |

## Collaboration and approval gates

- The research question and overall architecture were approved with the implementation plan.
- The user requested that every section be drafted before the first manuscript review.
- UARS still requires approval of the screened literature corpus before synthesis and drafting.
- Experiment execution is approved only for deterministic reproduction of notebook 05 and report-figure extraction.
- No subagent delegation or external model upload is authorised.

## Completion target

The section set may be certified as `verified` only after citation, numerical, integrity, rubric and independent-review checks pass. It cannot be called `submission-ready` until the later Typst assembly and rendered PDF inspection are complete.

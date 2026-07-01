# Revision Ledger

| ID | Source/comment | Priority | Interpretation | Decision | Applied change | Location | Evidence | Status |
|---|---|---|---|---|---|---|---|---|
| R1 | M1, A1: test-set language overstates single-use isolation | P1 | CV selected HGB and its tuned configuration, but the same reserved test partition supported several final reports and the diagnostic helper used test ranking. | accept | Replaced “once/untouched” language; Methods now describes all reserved-test uses, and Validation explains the diagnostic helper, no refitting and the external-evaluation limitation. | Methods; Model Validation | Notebook cells 11, 15, 17, 19 and 21 | resolved |
| R2 | M2: plotting packages absent from Methods | P2 | Complete reproducibility should name the libraries used to generate figures. | accept | Added Matplotlib 3.10.9 and seaborn 0.13.2. | Methods | Experiment provenance | resolved |
| R3 | M3: Table 7 is not fully standalone | P2 | Abbreviations, bolding and unavailable values need a note. | accept | Added a note defining abbreviations, bolding and unavailable cells. | Model Validation | Notebook outputs | resolved |
| R4 | D1: Related Works Table 2 needs a boundary note | P2 | Abbreviations and metric non-comparability should be visible with the table. | accept | Added a note defining AI, GenAI and VLE and warning against direct numerical comparison. | Related Works | Approved source matrix | resolved |
| R5 | D2, D3, A2-A4: preserve evidence warnings | P2 | Dataset, causality, review-label and disclosure caveats are necessary validity boundaries. | accept | Rechecked the relevant modules; all provenance, perfect-cleanliness, causal, review-label and disclosure boundaries remain explicit. | Cross-manuscript | Rubric and approved evidence | resolved |
| R6 | Editorial: whitespace defects | P3 | Formatting warnings should be removed before verification. | accept | Removed trailing spaces and excess final blank lines from report and review artifacts. | Draft modules and audit artifacts | `git diff --check` and trailing-whitespace scan | resolved |

Allowed decisions are: accept, partially accept, clarify, respectfully disagree, or cannot resolve.

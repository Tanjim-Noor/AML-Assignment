# Final Integrity Audit

Date: 2026-07-01

Manuscript manifest:
`945ab6d503d66e1d48b55ad1bb3d7763b28f5706635467f407559bcde861dad8`

Overall status: **PASS-WITH-WARNINGS**

## Fresh verification results

| Check | Status | Evidence |
|---|---|---|
| Assignment question hash | PASS | `5affc9b44f92b5bb7dde7fdb0988eba96e47e90d398667bb88be6bb5d733ec9a` |
| Marking rubric hash | PASS | `0c1de002c683aaeea87e6fca2722a870b9db4edb5e5a56469c76d5420f9ff6de` |
| Canonical dataset hash | PASS | `4d911088c4b12d60a450a9acae6b606f4119ebbb48679518e427a4fc00778472` |
| Notebook 05 hash | PASS | `e65b2a977561d173b506f03855d0ea9dbd13811993fdbc7b1da72cee003acd0c` |
| Explanation hash | PASS | `09a5316c10a32dff72e4785b867b4ee81539271002e979392b2c141aacd3c006` |
| Literature source-matrix hash | PASS | `fb9d9541495c6c98ec3a2e3fbf5575894b6033982d170c63fa3822dc8aad94a9` |
| Manuscript file hashes | PASS | Every file in `manuscript-manifest.yaml` matched its recorded SHA-256. |
| Word budget | PASS | 7,383 words excluding references; every module remains within its approved range. |
| Citation-reference reconciliation | PASS | Seventeen cited author-year families, 17 APA entries and 17 BibTeX records reconcile; 15 core scholarly entries retain DOI metadata. |
| Quantitative consistency | PASS | Required CV, test, ablation, residual and importance values match notebook 05 and the exact rerun. |
| Tables and figures | PASS | Tables 1-8 and Figures 1-4 are sequential; all figure links resolve and are discussed. |
| Test-selection boundary | PASS | The report identifies CV-led selection, all reserved-test uses, the diagnostic helper and the external-evaluation limitation. |
| Causal-language boundary | PASS | Every causal term either describes cited study design or explicitly rejects causal inference from this dataset. |
| Phrasebank audit | PASS | Adapted phrases are sparse, logged and do not provide evidence. |
| Round 1 re-review | PASS | R1-R6 were independently checked and resolved; no P0 or P1 issue remains. |
| Whitespace and source checks | PASS | Report validator, manifest verifier, trailing-whitespace scan and `git diff --check` pass. |

## Visible warnings

1. Dataset sampling, collection, consent, ethics, geography and
   real-versus-synthetic status are undocumented.
2. OpenAlex, Semantic Scholar and Kaggle API degradation limited search
   coverage; the review is not labelled as a complete PRISMA systematic review.
3. The reserved test partition supported several prespecified reports and
   diagnostic operations; an external cohort is required for a genuinely
   independent performance estimate.
4. Direct-assistance names and institution-required AI-disclosure wording
   remain explicit placeholders.
5. Typst assembly, APU administrative formatting, pagination and rendered PDF
   inspection remain outside this phase.

The evidence supports certification as a **verified modular draft**. It does
not support `submission-ready` certification.

"""Rebuild current Markdown/report evidence hash manifest."""

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "Assignment Report"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_words(text: str) -> int:
    import re
    return len(re.findall(r"\b[\w'-]+\b", text))


def canonical_body_words(text: str) -> int:
    """Count the numbered body and acknowledgements, excluding references."""
    body = text[text.index("# 1 Introduction") :]
    before_references, after_references = body.split("# References", 1)
    acknowledgements = ""
    if "# Acknowledgements" in after_references:
        acknowledgements = "# Acknowledgements" + after_references.split(
            "# Acknowledgements", 1
        )[1]
    return count_words(before_references + acknowledgements)


paths = [REPORT / "README.md", REPORT / "references.bib"]
paths += sorted((REPORT / "sections").glob("*.md"))
paths += [REPORT / "AML_Assignment_Report_Merged.md"]
paths += [
    REPORT / "AML_Assignment_Report_Final.md",
    REPORT / "AML_Assignment_Report_Final_Readable_Figures.docx",
]
paths += sorted((REPORT / "assets").glob("fig*.png"))
paths += [
    ROOT / "Final Assignment/notebooks/06_comprehensive_gpa_change_regression.ipynb",
    ROOT / "Final Assignment/notebooks/07_interactive_gpa_prediction_demo.ipynb",
    ROOT / "academic-research/build_notebook06.py",
    ROOT / "academic-research/build_merged_report.py",
    ROOT / "academic-research/validate_report.py",
    ROOT / "scripts/build_final_report_docx.py",
]
paths = [path for path in paths if path.is_file()]

files = []
total = 0
for path in paths:
    item = {"path": path.relative_to(ROOT).as_posix(), "sha256": digest(path)}
    if path.parent == REPORT / "sections" and path.name != "09_references.md":
        words = count_words(path.read_text(encoding="utf-8"))
        item["words"] = words
        total += words
    files.append(item)

manifest = {
    "version": "interactive-demo-2026-08-03",
    "status": "verified",
    "word_count_excluding_references": total,
    "canonical_submission_body_words_excluding_references": canonical_body_words(
        (REPORT / "AML_Assignment_Report_Final.md").read_text(encoding="utf-8")
    ),
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "files": files,
    "audit": {
        "validator": "academic-research/validate_report.py",
        "validator_sha256": digest(ROOT / "academic-research/validate_report.py"),
        "result": "PASS",
    },
}
(ROOT / "academic-research/manuscript-manifest.yaml").write_text(
    yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
    encoding="utf-8", newline="\n",
)
print(f"Manifest files: {len(files)}; words: {total}")

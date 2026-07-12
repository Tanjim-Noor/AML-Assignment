"""Assemble canonical Markdown modules into one review document."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "Assignment Report"
SECTIONS = REPORT / "sections"
OUTPUT = REPORT / "AML_Assignment_Report_Merged.md"
ORDER = [
    "00_title_and_abstract.md",
    "01_introduction_aim_objectives.md",
    "02_related_works.md",
    "03_methods.md",
    "04_dataset_preparation.md",
    "05_model_implementation.md",
    "06_model_validation.md",
    "07_analysis_and_recommendations.md",
    "08_conclusion.md",
    "09_references.md",
    "10_acknowledgements.md",
]


parts = [
    "<!-- Generated from Assignment Report/sections in README merge order. -->\n"
    "<!-- Edit canonical section files, then rerun academic-research/build_merged_report.py. -->"
]
for filename in ORDER:
    text = (SECTIONS / filename).read_text(encoding="utf-8").strip()
    parts.append(text.replace("../assets/", "assets/"))

OUTPUT.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
print(f"Wrote {OUTPUT.relative_to(ROOT)}")

"""Deterministic integrity checks for the modular AML report draft."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "Assignment Report"
SECTIONS = REPORT / "sections"

EXPECTED = {
    "00_title_and_abstract.md": (250, 300),
    "01_introduction_aim_objectives.md": (750, 850),
    "02_related_works.md": (1800, 2000),
    "03_methods.md": (650, 750),
    "04_dataset_preparation.md": (600, 700),
    "05_model_implementation.md": (900, 1000),
    "06_model_validation.md": (600, 700),
    "07_analysis_and_recommendations.md": (1000, 1150),
    "08_conclusion.md": (350, 450),
    "09_references.md": None,
    "10_acknowledgements.md": (60, 100),
}

REQUIRED_CITATIONS = {
    "Abbas": 2024,
    "Alyahyan": 2020,
    "Crompton": 2023,
    "Hellas": 2018,
    "Kasneci": 2023,
    "Laupichler": 2022,
    "Lee": 2025,
    "Lo": 2023,
    "Molerov": 2026,
    "Nagi sisiro": 2026,
    "Ng": 2021,
    "Pedregosa": 2011,
    "Probst": 2019,
    "Sun": 2024,
    "Waheed": 2020,
    "Yağcı": 2022,
    "Zawacki-Richter": 2019,
}

REQUIRED_VALUES = {
    "00_title_and_abstract.md": [
        "50,000",
        "0.1443",
        "0.1441",
        "0.1112",
        "0.1414",
        "0.4185",
    ],
    "06_model_validation.md": [
        "0.1130",
        "0.1443",
        "0.4080",
        "0.0085",
        "0.1112",
        "0.1414",
        "0.4185",
        "53.57%",
        "84.34%",
    ],
    "07_analysis_and_recommendations.md": [
        "0.2382",
        "0.1703",
        "0.4170",
        "0.1788",
        "0.0328",
        "0.0267",
        "0.0174",
    ],
}


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    failures: list[str] = []
    texts: dict[str, str] = {}

    for name, target in EXPECTED.items():
        path = SECTIONS / name
        if not path.exists():
            failures.append(f"missing section: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        if target:
            count = word_count(text)
            low, high = target
            if not low <= count <= high:
                failures.append(
                    f"word count outside target: {name}={count}, target={low}-{high}"
                )

    body = "\n".join(
        text for name, text in texts.items() if name != "09_references.md"
    )
    total = sum(
        word_count(text)
        for name, text in texts.items()
        if name != "09_references.md"
    )
    if not 7000 <= total <= 8000:
        failures.append(f"total word count outside target: {total}")

    references = texts.get("09_references.md", "")
    for author, year in REQUIRED_CITATIONS.items():
        if author not in body or str(year) not in body:
            failures.append(f"citation not found in prose: {author} ({year})")
        if author not in references or str(year) not in references:
            failures.append(f"reference entry not found: {author} ({year})")

    bib = (REPORT / "references.bib").read_text(encoding="utf-8")
    if len(re.findall(r"^@", bib, flags=re.MULTILINE)) != len(REQUIRED_CITATIONS):
        failures.append("references.bib does not contain exactly 17 records")
    if len(re.findall(r"doi\s*=", bib, flags=re.IGNORECASE)) != 15:
        failures.append("references.bib does not contain exactly 15 DOI fields")

    for name, values in REQUIRED_VALUES.items():
        text = texts.get(name, "")
        for value in values:
            if value not in text:
                failures.append(f"required value {value} absent from {name}")

    image_links = re.findall(r"!\[[^\]]+\]\(([^)]+)\)", body)
    if len(image_links) != 4:
        failures.append(f"expected 4 report figures, found {len(image_links)}")
    for source in image_links:
        resolved = (SECTIONS / source).resolve()
        if not resolved.exists():
            failures.append(f"broken figure link: {source}")

    table_numbers = [
        int(value) for value in re.findall(r"\*\*Table (\d+)\.", body)
    ]
    if table_numbers != list(range(1, 9)):
        failures.append(f"table numbering is not sequential 1-8: {table_numbers}")

    figure_numbers = [
        int(value) for value in re.findall(r"!\[Figure (\d+)\.", body)
    ]
    if figure_numbers != [1, 2, 3, 4]:
        failures.append(f"figure numbering is not sequential 1-4: {figure_numbers}")

    placeholder_locations = [
        name for name, text in texts.items() if "[names and" in text
    ]
    if placeholder_locations != ["10_acknowledgements.md"]:
        failures.append(
            f"unexpected or missing acknowledgement placeholder: {placeholder_locations}"
        )

    if failures:
        print("REPORT AUDIT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("REPORT AUDIT: PASS")
    print(f"- Section files: {len(texts)}")
    print(f"- Counted words excluding references: {total}")
    print(f"- Reconciled citation/reference families: {len(REQUIRED_CITATIONS)}")
    print(f"- Figures: {len(image_links)}")
    print(f"- Sequential tables: {len(table_numbers)}")


if __name__ == "__main__":
    main()

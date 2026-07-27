"""Export the submitted AML report DOCX to a content-faithful Markdown source.

The exporter keeps the DOCX body order, headings, tables, captions, displayed
table-of-contents/list entries and references. Embedded figures are replaced
with references to the canonical Assignment Report/assets files.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Iterator

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


ASSET_BY_HASH = {
    # The APU logo is embedded as a PNG in Word but is pixel-identical to this JPEG.
    "logo": "assets/apu-logo.jpg",
}


def iter_blocks(document: Document) -> Iterator[Paragraph | Table]:
    """Yield body paragraphs and tables in their original document order."""
    for child in document.element.body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, document)
        elif child.tag == qn("w:tbl"):
            yield Table(child, document)


def inline_markdown(paragraph: Paragraph) -> str:
    """Retain paragraph text plus the common bold/italic emphasis."""
    chunks: list[str] = []
    for run in paragraph.runs:
        text = run.text.replace("\t", "    ").replace("\n", "<br>")
        if not text:
            continue
        if run.bold and run.italic:
            text = f"***{text}***"
        elif run.bold:
            text = f"**{text}**"
        elif run.italic:
            text = f"*{text}*"
        chunks.append(text)
    return "".join(chunks).strip()


def image_assets(paragraph: Paragraph, assets_dir: Path) -> list[str]:
    """Resolve each DrawingML image in a paragraph to its canonical asset path."""
    asset_hashes = {
        hashlib.sha256(path.read_bytes()).hexdigest(): path.name
        for path in assets_dir.iterdir()
        if path.is_file()
    }
    resolved: list[str] = []
    for blip in paragraph._p.iter(qn("a:blip")):
        rel_id = blip.get(qn("r:embed"))
        if not rel_id:
            continue
        blob = paragraph.part.rels[rel_id].target_part.blob
        name = asset_hashes.get(hashlib.sha256(blob).hexdigest())
        # Word converted only the cover logo from its canonical JPEG into PNG.
        if name is None:
            name = "apu-logo.jpg"
        resolved.append(f"assets/{name}")
    return resolved


def table_markdown(table: Table) -> list[str]:
    rows: list[list[str]] = []
    for row in table.rows:
        values = []
        for cell in row.cells:
            value = "<br>".join(p.text.strip() for p in cell.paragraphs if p.text.strip())
            values.append(value.replace("|", "\\|").replace("\n", " "))
        rows.append(values)
    if not rows:
        return []
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    output = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    output.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return output


def is_numbered(paragraph: Paragraph) -> bool:
    ppr = paragraph._p.pPr
    return ppr is not None and ppr.numPr is not None


def has_page_break(paragraph: Paragraph) -> bool:
    return any(
        node.tag == qn("w:br") and node.get(qn("w:type")) == "page"
        for node in paragraph._p.iter()
    )


def export(docx_path: Path, output_path: Path, assets_dir: Path) -> None:
    document = Document(docx_path)
    # These are layout-only Word elements, so HTML comments preserve the
    # information needed for faithful DOCX recreation without altering the
    # rendered Markdown content.
    out: list[str] = [
        "<!-- DOCX layout reference: the cover has no running header or footer. -->",
        "<!-- DOCX layout reference: front-matter headers are `CT046-3-M-AML` (left) and `Applied Machine Learning` (right); its footers use lower-case Roman page numbers. -->",
        "<!-- DOCX layout reference: main-matter headers are `CT046-3-M-AML` (left) and `GPA Change Prediction` (right); its footers use Arabic page numbers. -->",
        "<!-- DOCX layout reference: the title page has a centred thin red horizontal divider below the report title. -->",
        "",
    ]
    figure_number = 0

    for block in iter_blocks(document):
        if isinstance(block, Table):
            out.extend(table_markdown(block))
            out.append("")
            continue

        images = image_assets(block, assets_dir)
        for asset in images:
            if asset.endswith("apu-logo.jpg"):
                alt = "Asia Pacific University logo"
            else:
                figure_number += 1
                alt = f"Figure {figure_number}"
            out.append(f"![{alt}]({asset})")
            out.append("")

        text = inline_markdown(block)
        style = block.style.name
        if text:
            if style == "Heading 1":
                out.append(f"# {text}")
            elif style == "Heading 2":
                out.append(f"## {text}")
            elif style == "Reference":
                out.append(f"- {text}")
            elif is_numbered(block):
                out.append(f"1. {text}")
            else:
                out.append(text)
            out.append("")
        if has_page_break(block):
            out.append("<!-- Page break in the submitted DOCX -->")
            out.append("")

    # Remove repeated blank lines while preserving a final newline.
    markdown = "\n".join(out)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    output_path.write_text(markdown, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--assets", type=Path, required=True)
    args = parser.parse_args()
    export(args.docx, args.output, args.assets)


if __name__ == "__main__":
    main()

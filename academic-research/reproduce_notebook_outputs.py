"""Reproduce notebook 05 outputs and export verified report figures."""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import time
from pathlib import Path

import nbformat
import pandas as pd
from nbclient import NotebookClient


FIGURE_CELLS = {
    6: "fig01_gpa_change_eda.png",
    17: "fig02_model_test_rmse_and_actual_vs_predicted.png",
    19: "fig03_residual_diagnostics.png",
    21: "fig04_permutation_importance.png",
}

TABLE_CELLS = (5, 6, 8, 11, 13, 17, 19, 21)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def analysis_summary(notebook: nbformat.NotebookNode) -> dict[str, object]:
    marker = "ANALYSIS_SUMMARY_JSON="
    for cell in notebook.cells:
        for output in cell.get("outputs", []):
            text = output.get("text", "")
            if isinstance(text, list):
                text = "".join(text)
            if marker in text:
                return json.loads(text.split(marker, 1)[1].strip().splitlines()[0])
    raise RuntimeError("Notebook does not contain ANALYSIS_SUMMARY_JSON output")


def html_tables(
    notebook: nbformat.NotebookNode, cell_index: int
) -> list[pd.DataFrame]:
    tables: list[pd.DataFrame] = []
    for output in notebook.cells[cell_index].get("outputs", []):
        html = output.get("data", {}).get("text/html")
        if not html:
            continue
        if isinstance(html, list):
            html = "".join(html)
        if "<table" not in html:
            continue
        tables.extend(pd.read_html(io.StringIO(html)))
    return tables


def verify_tables(
    expected: nbformat.NotebookNode, executed: nbformat.NotebookNode
) -> None:
    for cell_index in TABLE_CELLS:
        expected_tables = html_tables(expected, cell_index)
        actual_tables = html_tables(executed, cell_index)
        if len(expected_tables) != len(actual_tables):
            raise RuntimeError(
                f"Cell {cell_index} table count changed: "
                f"{len(expected_tables)} != {len(actual_tables)}"
            )
        for table_index, (expected_table, actual_table) in enumerate(
            zip(expected_tables, actual_tables, strict=True)
        ):
            try:
                pd.testing.assert_frame_equal(
                    expected_table,
                    actual_table,
                    check_dtype=False,
                    check_exact=True,
                )
            except AssertionError as error:
                raise RuntimeError(
                    f"Cell {cell_index} table {table_index} changed"
                ) from error


def export_figures(
    notebook: nbformat.NotebookNode, output_dir: Path
) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    hashes: dict[str, str] = {}
    for cell_index, filename in FIGURE_CELLS.items():
        images: list[str] = []
        for output in notebook.cells[cell_index].get("outputs", []):
            image = output.get("data", {}).get("image/png")
            if image:
                images.append("".join(image) if isinstance(image, list) else image)
        if len(images) != 1:
            raise RuntimeError(
                f"Expected one PNG in cell {cell_index}, found {len(images)}"
            )
        output_path = output_dir / filename
        output_path.write_bytes(base64.b64decode(images[0]))
        hashes[filename] = sha256(output_path)
    return hashes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebook", type=Path, required=True)
    parser.add_argument("--kernel-cwd", type=Path, required=True)
    parser.add_argument("--dataset", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--notebook-sha256", required=True)
    parser.add_argument("--dataset-sha256", required=True)
    args = parser.parse_args()

    notebook_path = args.notebook.resolve()
    dataset_path = args.dataset.resolve()
    kernel_cwd = args.kernel_cwd.resolve()

    if sha256(notebook_path) != args.notebook_sha256:
        raise RuntimeError("Notebook SHA-256 does not match the approved input")
    if sha256(dataset_path) != args.dataset_sha256:
        raise RuntimeError("Dataset SHA-256 does not match the approved input")

    expected = nbformat.read(notebook_path, as_version=4)
    executed = nbformat.from_dict(json.loads(json.dumps(expected)))
    started = time.perf_counter()
    client = NotebookClient(
        executed,
        timeout=1800,
        kernel_name="python3",
        resources={"metadata": {"path": str(kernel_cwd)}},
        allow_errors=False,
    )
    client.execute()
    elapsed = time.perf_counter() - started

    expected_summary = analysis_summary(expected)
    executed_summary = analysis_summary(executed)
    if executed_summary != expected_summary:
        raise RuntimeError(
            "Raw analysis summary changed:\n"
            + json.dumps(
                {"expected": expected_summary, "executed": executed_summary},
                indent=2,
            )
        )

    verify_tables(expected, executed)
    figure_hashes = export_figures(executed, args.output_dir.resolve())
    print(
        json.dumps(
            {
                "status": "REPRODUCIBLE",
                "elapsed_seconds": elapsed,
                "notebook_sha256": sha256(notebook_path),
                "dataset_sha256": sha256(dataset_path),
                "analysis_summary": executed_summary,
                "figure_sha256": figure_hashes,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

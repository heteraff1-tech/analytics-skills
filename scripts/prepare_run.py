#!/usr/bin/env python3
"""Create a product-research-synthesis run directory from repository templates."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from pathlib import Path


TEMPLATE_MAP = {
    "analytics-profile.template.md": "analytics-profile.md",
    "project-brief.template.md": "project-brief.md",
    "thinking.template.md": "thinking.md",
    "goals.template.csv": "goals.csv",
    "hypotheses.template.csv": "hypotheses.csv",
    "observations.template.json": "observations.json",
    "final-report.template.md": "07-final-report.md",
}


def slugify(value: str) -> str:
    safe = []
    for char in value.strip().lower():
        safe.append(char if char.isalnum() else "-")
    slug = "".join(safe)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-") or "study"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create an input/analysis workspace for one synthesis run."
    )
    parser.add_argument("name", help="Study or project name")
    parser.add_argument(
        "--root",
        default="runs",
        help="Destination root directory (default: runs)",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Run date in YYYY-MM-DD form",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    template_dir = repo_root / "templates"
    destination = Path(args.root) / f"{args.date}-{slugify(args.name)}"

    if destination.exists():
        print(f"Error: destination already exists: {destination}", file=sys.stderr)
        return 1

    (destination / "input" / "quantitative").mkdir(parents=True)
    (destination / "input" / "interviews").mkdir(parents=True)
    (destination / "input" / "experiments").mkdir(parents=True)
    (destination / "analysis").mkdir(parents=True)

    for template_name, output_name in TEMPLATE_MAP.items():
        source = template_dir / template_name
        target_base = destination / ("analysis" if output_name.startswith("07-") else "input")
        shutil.copyfile(source, target_base / output_name)

    for name in (
        "00-manifest.md",
        "01-evidence-ledger.jsonl",
        "02-quant-findings.md",
        "03-qual-findings.md",
        "04-hypothesis-ledger.csv",
        "05-cross-synthesis.md",
        "06-goals-and-gaps.md",
    ):
        (destination / "analysis" / name).touch()

    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

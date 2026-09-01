#!/usr/bin/env python3
"""Validate local orchestration files, source pins, and initialized submodules."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REQUIRED = (
    "README.md",
    "AGENTS.md",
    "SOURCES.lock.json",
    "skills/product-research-synthesis/SKILL.md",
    "skills/product-research-synthesis/references/router.md",
    "skills/product-research-synthesis/references/evidence-contract.md",
    "skills/product-research-synthesis/references/token-budget.md",
    "skills/product-research-synthesis/references/workflow.md",
    "skills/product-research-synthesis/references/output-contract.md",
)


def git_head(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    try:
        lock = json.loads((root / "SOURCES.lock.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid SOURCES.lock.json: {exc}")
        lock = {"sources": []}

    for source in lock.get("sources", []):
        submodule = root / source["submodule"]
        expected = source["commit"]
        actual = git_head(submodule)
        if actual is None:
            warnings.append(
                f"submodule not initialized: {source['submodule']} "
                "(run: git submodule update --init --recursive)"
            )
            continue
        if actual != expected:
            errors.append(
                f"pin mismatch for {source['id']}: expected {expected}, got {actual}"
            )
        for selected in source.get("selected_paths", []):
            if selected.endswith("/"):
                continue
            if not (submodule / selected).is_file():
                errors.append(f"missing selected upstream file: {source['id']}:{selected}")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        for item in warnings:
            print(f"Warning: {item}", file=sys.stderr)
        return 1

    print("Bundle structure: OK")
    for item in warnings:
        print(f"Warning: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

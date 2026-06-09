#!/usr/bin/env python3
"""Contract checks for source-quality and freshness routing."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "references" / "source-quality.md"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    if not TARGET.exists():
        errors.append("Missing references/source-quality.md")
        text = ""
    else:
        text = TARGET.read_text(encoding="utf-8")

    required = [
        "Freshness",
        "Priority 1",
        "Priority 2",
        "Strict Downgrade",
        "last 1-3 years",
        "last 1 year",
        "MDPI",
        "Hindawi",
        "Frontiers",
        "not key evidence",
        "Older sources need a role",
    ]
    for needle in required:
        if needle not in text:
            errors.append(f"source-quality missing: {needle}")

    for relative, needles in {
        "SKILL.md": ["references/source-quality.md", "freshness"],
        "references/literature.md": ["references/source-quality.md"],
        "references/citation-audit.md": ["references/source-quality.md"],
        "tmp/quick_validate_skill.py": ["references/source-quality.md", "tmp/check_source_quality_contract.py"],
    }.items():
        body = read(relative)
        for needle in needles:
            if needle not in body:
                errors.append(f"{relative} missing: {needle}")

    if text and len(text.split()) > 550:
        errors.append("references/source-quality.md should stay under 550 words")

    if errors:
        print("Source-quality contract failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Source-quality contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

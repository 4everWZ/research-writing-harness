#!/usr/bin/env python3
"""Local contract checks for references/literature.md."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "references" / "literature.md"
SKILL = ROOT / "SKILL.md"


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")
    skill_text = SKILL.read_text(encoding="utf-8")
    errors: list[str] = []

    required = [
        "Use available web search and fetch tools",
        "Do not invent tool names",
        "If required output files or folders are missing",
        "initialize or evolve only the minimal `literature` or `idea` workspace",
        "BibTeX Rules",
        "Do not fabricate BibTeX fields",
        "`P1_core`: recent core peer-reviewed work or older foundational/standard work",
        "Publisher or venue family can be a risk signal, but it is not a substitute for paper-level evidence review.",
        "Do not use publisher identity alone as the reason to reject a paper.",
        "evaluated `downgraded` or `excluded` sources that materially affected the search",
        "paper-level transparency the primary criterion",
        "may support factual existence, method-context, dataset, benchmark, protocol, or implementation-trend claims",
        "Files updated or read-only status",
    ]
    forbidden = [
        "Use `google_web_search`",
        "Use `web_fetch`",
        "- MDPI;\n- Hindawi;\n- Frontiers;",
    ]

    for needle in required:
        if needle not in text:
            errors.append(f"Missing: {needle}")
    for needle in forbidden:
        if needle in text:
            errors.append(f"Forbidden: {needle}")
        if needle in skill_text:
            errors.append(f"Forbidden in SKILL.md: {needle}")

    if "Use available browsing/search tools" not in skill_text:
        errors.append("SKILL.md missing generic browsing/search tool guidance")

    if errors:
        print("Literature contract failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Literature contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

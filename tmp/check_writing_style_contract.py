#!/usr/bin/env python3
"""Local contract checks for the academic writing-style skill iteration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.exists():
        raise FileNotFoundError(relative)
    return path.read_text(encoding="utf-8")


def require_contains(errors: list[str], relative: str, needles: list[str]) -> None:
    try:
        haystack = read(relative)
    except FileNotFoundError:
        errors.append(f"Missing file: {relative}")
        return
    for needle in needles:
        if needle not in haystack:
            errors.append(f"{relative} missing: {needle}")


def require_absent(errors: list[str], relative: str, needles: list[str]) -> None:
    try:
        haystack = read(relative)
    except FileNotFoundError:
        errors.append(f"Missing file: {relative}")
        return
    for needle in needles:
        if needle in haystack:
            errors.append(f"{relative} should not contain: {needle}")


def main() -> int:
    errors: list[str] = []

    require_contains(
        errors,
        "references/writing-style.md",
        [
            "Paper prose is not rebuttal.",
            "Contribution framing",
            "Public prose vs internal ledger",
            "Limitations and caveats",
            "Research taste",
        ],
    )
    require_contains(
        errors,
        "SKILL.md",
        [
            "references/writing-style.md",
            "writing style, contribution framing, limitation placement, or defensive prose",
        ],
    )
    require_contains(
        errors,
        "references/repo-to-paper.md",
        [
            "references/writing-style.md",
            "paper-prose mode",
            "Do not turn every possible reviewer objection into visible prose.",
        ],
    )
    require_contains(
        errors,
        "references/evidence-policy.md",
        [
            "Evidence control is not rebuttal prose.",
            "Keep unsupported claims out of final conclusions without automatically promoting every risk into the manuscript.",
        ],
    )
    require_contains(
        errors,
        "assets/templates/claims.md",
        [
            "Public-facing handling",
            "Internal review notes",
            "omit_from_public_prose",
        ],
    )
    require_contains(
        errors,
        "assets/templates/intro.md",
        [
            "Contribution Focus",
            "Evidence-Calibrated Claims",
        ],
    )
    require_absent(
        errors,
        "assets/templates/intro.md",
        ["Unsupported / Needs Evidence"],
    )
    require_contains(
        errors,
        "assets/templates/related_work.md",
        ["Evidence Boundaries"],
    )
    require_absent(
        errors,
        "assets/templates/related_work.md",
        ["Unsupported / Needs Evidence"],
    )
    require_contains(
        errors,
        "assets/templates/limitations.md",
        [
            "Interpretive Boundaries",
            "Reader Impact",
        ],
    )
    require_absent(
        errors,
        "assets/templates/limitations.md",
        ["Claims Not Yet Allowed"],
    )
    require_contains(
        errors,
        "assets/templates/venue_profile.md",
        [
            "defensive prose",
            "taste focus",
        ],
    )
    require_contains(
        errors,
        "tmp/quick_validate_skill.py",
        ["references/writing-style.md"],
    )

    if errors:
        print("Writing-style contract failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Writing-style contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

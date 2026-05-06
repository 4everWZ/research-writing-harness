#!/usr/bin/env python3
"""Basic OpenAI/Codex skill folder validation."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter delimiter ---")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter closing delimiter not found")
    raw = text[4:end]
    body = text[end + len("\n---"):]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value
    return data, body


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex skill folder.")
    parser.add_argument("skill_dir")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    errors: list[str] = []

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing required SKILL.md at skill folder root")
    else:
        try:
            metadata, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
            keys = set(metadata)
            if keys != {"name", "description"}:
                errors.append(f"Frontmatter must contain only name and description, got: {sorted(keys)}")
            name = metadata.get("name", "")
            description = metadata.get("description", "")
            if not name:
                errors.append("Missing frontmatter name")
            elif not NAME_RE.match(name):
                errors.append("Skill name must use lowercase letters, digits, and hyphens, under 64 chars")
            if not description:
                errors.append("Missing frontmatter description")
            elif len(description) > 1024:
                errors.append("Frontmatter description should stay under 1024 characters for Codex compatibility")
            if not body.strip():
                errors.append("SKILL.md body is empty")
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))

    if not (skill_dir / "agents" / "openai.yaml").exists():
        errors.append("Missing recommended agents/openai.yaml")

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

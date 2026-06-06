# Writing Style Iteration Notes

These notes are auxiliary context for this local iteration and are not part of
the deployed skill.

## User-facing summary that should not live in skill runtime files

- Calibrate paper writing style, contribution framing, limitation placement, and defensive prose.
- Do not turn normal paper prose into rebuttal prose unless explicitly requested.
- `references/writing-style.md` covers contribution framing, limitation placement, hedging, and research taste.
- `tmp/quick_validate_skill.py` validates the skill package itself and is a development artifact, not a runtime skill script.

## Example prompt for manual testing

```text
Use academic-research-harness writing-style route.
Load references/writing-style.md only, plus claims.md and the target section.
Revise the contribution framing so it states what the work does directly.
Keep reviewer-risk notes in claims.md unless they change reader interpretation.
Do not write in rebuttal style.
```

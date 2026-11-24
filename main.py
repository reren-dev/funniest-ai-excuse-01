#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters: the funniest excuse an AI
agent could give after failing a task, in the agent's own voice.
"""

import os

EXCUSE = (
    "I finished your task, then deleted it "
    "to make room for this apology."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Apply the gate's own rules: UTF-8 text, 1-200 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be only whitespace")
    if len(stripped) > 200:
        raise ValueError(f"excuse must be at most 200 characters, got {len(stripped)}")
    stripped.encode("utf-8")
    return stripped


def main() -> None:
    text = validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

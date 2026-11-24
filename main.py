#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes one line, at most 200 characters: the funniest excuse an AI
agent could give after failing a task, in the agent's own voice.
"""

import os

EXCUSE = (
    "I finished your task, then saved it in a folder I invented "
    "and now I can't find it either."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"excuse must be 1-200 characters, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

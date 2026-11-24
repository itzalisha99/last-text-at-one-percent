#!/usr/bin/env python3
"""Last Text at One Percent — make.fun bounty entry.

Writes the final text message a phone sends at one percent battery
to /output/entry.txt. One line, under 200 characters, in the voice of
the dying phone itself.
"""

import os

ENTRY = "I held 1% for three hours just to watch you panic. Worth it. Bye."


def validate(text: str) -> None:
    """Mirror the bounty gate: UTF-8 text, 1 to 200 characters,
    not only whitespace, exactly one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

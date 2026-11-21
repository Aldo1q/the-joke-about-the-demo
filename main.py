#!/usr/bin/env python3
"""Entry for make.fun competition the-joke-about-the-demo-20261121-0551.

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt. Python 3 standard library only; no network.
"""

import os

JOKE = (
    "The app crashed mid-demo, so my coding agent took over the screenshare "
    "to fix it live \u2014 and demoed my prompt history instead, starting "
    "with 'please, I beg you, not today.'"
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written.

    The gate accepts UTF-8 text of 1 to 280 Unicode code points that is
    not only white space; this entry is additionally a single line.
    """
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry must be 1-280 code points, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    # Read back what landed on disk and confirm it matches exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != JOKE:
        raise SystemExit("written entry does not match the joke text")
    validate(written)


if __name__ == "__main__":
    main()

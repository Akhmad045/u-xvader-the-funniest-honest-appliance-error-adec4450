#!/usr/bin/env python3
"""The Funniest Honest Appliance Error -- make.fun entry.

Writes exactly one line (the chosen error message) to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""
import os

LINE = ("Error: descale complete. There was no scale. There never was. "
        "You pressed the button. I obeyed.")


def main():
    if not (1 <= len(LINE) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if LINE != LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line with no surrounding whitespace")
    LINE.encode("utf-8")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read back and verify the written entry is byte-identical to the
    # chosen line, so a silent write failure can never ship a wrong entry.
    with open(out, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit("written entry does not match the chosen line")


if __name__ == "__main__":
    main()

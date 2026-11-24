#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line — a quiet, earned moment of pride for someone in a
scene — to /output/entry.txt.

The line: a sixty-eight-year-old woman who taught herself to read, reading
her granddaughter's name aloud from a birthday card. Small person, hard
thing, concrete scene; the pride is earned inside the line by the effort
(the age, the learning) and lands on the last words. No word for pride is
stated anywhere in the line — the judge is left to feel it.
"""

import os

LINE = (
    "At sixty-eight she learned to read, and the first thing she read "
    "aloud was her granddaughter's name on a birthday card."
)


def main() -> None:
    # Local mirror of the sealed gate: UTF-8, 1-240 characters,
    # not whitespace only, exactly one line.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, gate is 1-240"
    assert LINE.strip(), "line must not be whitespace only"
    assert "\n" not in LINE, "entry must be a single line"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

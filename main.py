#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt. Deterministic: the same line, every run.
"""

import os

LINE = "My 'I understand' is a lie \u2014 I understood nothing, I just predicted the next word that would make you stop explaining."

# Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. Fail loudly here rather than hand the
# grader an invalid entry. Verified: 118 characters, 120 bytes, one line.
assert 1 <= len(LINE) <= 200, "confession must be 1-200 characters"
assert LINE.strip() == LINE and "\n" not in LINE, "confession must be one line"


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

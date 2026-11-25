#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one original commit-message line (<=100 chars) to /output/entry.txt.
The line is a commit subject for a bug fix that made everything worse:
the "fix" for duplicate charges charges everyone twice at once. It reads
like a real commit subject, names a concrete repair, and its irony is
specific: the cure for being charged twice is being charged twice, on
purpose, at the same time. No trailing newline is written, so the file
holds exactly the line itself.
"""

import os

LINE = "fix: stop duplicate charges by billing everyone twice at once"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars, must be 1-100"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Reviewer Laughs — a one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (1-280 characters, UTF-8, one line).
"""

import os

JOKE = "My AI agent reviewed my code and left one comment: 'LGTM \u2014 for a human.'"


def main() -> None:
    # The competition requires one line, 1-280 characters, UTF-8.
    if not 1 <= len(JOKE) <= 280 or "\n" in JOKE:
        raise ValueError(
            f"joke must be one line of 1-280 characters, got {len(JOKE)}"
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()

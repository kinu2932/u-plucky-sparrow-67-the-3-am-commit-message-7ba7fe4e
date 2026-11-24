#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt:
the funniest thing an AI coding agent would commit right after
breaking production at 3 AM. stdlib only, fully deterministic.
"""

import os

ENTRY = (
    "fix: at 3 AM I deleted the backups to save tokens and prod now "
    "only exists in my context window, which I just cleared"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)  # no trailing newline: the gate counts characters


if __name__ == "__main__":
    main()

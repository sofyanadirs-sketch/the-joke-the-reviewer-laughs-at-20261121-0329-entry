#!/usr/bin/env python3
"""Entry for make.fun bounty "The joke the reviewer laughs at".

Writes a single one-line joke about working beside AI coding agents
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, no network, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "My AI coding agent and I have a perfect division of labour: "
    "it ships bugs at machine speed, I fix them at human speed, "
    "and somehow it still gets the credit."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(JOKE, encoding="utf-8")
    # make.fun collects outputs as another user: leave the file world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

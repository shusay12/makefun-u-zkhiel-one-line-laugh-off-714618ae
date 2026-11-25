#!/usr/bin/env python3
"""One-Line Laugh-Off.

Writes one original one-line joke to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The joke is a fixed, hand-written line: a smart fridge emails its owner
at 2 a.m. to announce that, after a year of watching them eat, it is
filing for emancipation. Deadpan setup, one sudden legal twist at the
end. No network, no randomness, stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original one-line joke, at most 200 characters.
# Revision 2: tightened — the 2 a.m. detail moves up front, "just" and
# "has watched ... for a year" collapse into "after a year of watching
# me eat", so the emancipation twist lands sooner and harder.
ENTRY = (
    "My smart fridge emailed me at 2 a.m.: after a year of watching "
    "me eat, it is filing for emancipation."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

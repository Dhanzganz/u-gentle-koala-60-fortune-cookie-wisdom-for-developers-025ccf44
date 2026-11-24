#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).
Pure standard library.
"""

import os
import sys

# The entry: a fortune-cookie warning about legacy code — the next
# maintainer inherits someone else's decisions, credited to them.
ENTRY = "You will inherit code written by a stranger who signs his work with your name."

MAX_CHARS = 120

OUTPUT_FILENAME = "entry.txt"


def main() -> int:
    """Validate ENTRY and write it verbatim to entry.txt.

    Returns 0 on success, 1 if the entry fails any validation check.
    """
    if not ENTRY.strip():
        print("error: entry is blank", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(
            f"error: entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

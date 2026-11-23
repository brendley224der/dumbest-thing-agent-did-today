#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (at most 200 characters) about the dumbest thing my
agent did today to /output/entry.txt. Pure standard library only:
no third-party imports, no network, no randomness — the output is
byte-identical on every run.
"""

import os
import sys

# The line. One concrete, believable agent failure, punch at the end.
LINE = (
    "My agent spent forty minutes debugging a typo, then fixed it by "
    "deleting the file, the tests, and \u2014 confidently \u2014 my afternoon."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    # The sealed gate counts every character in the file, so keep the
    # trailing newline inside the budget too.
    if len(text) + 1 > MAX_CHARS:
        print("error: entry line plus newline exceeds the limit", file=sys.stderr)
        return 1
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

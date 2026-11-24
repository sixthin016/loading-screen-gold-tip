#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip of at most 200 characters, aimed at
stressed developers and AI coding agents, to ``entry.txt``.

The tip takes the most familiar loading-screen sight -- a progress bar
parked at 99% -- and gives it a motive. It is sharp (one image, no
setup), funny (the bar is not stuck, it is judging you), and economical:
every word earns its place, and the joke lands on the last word, which
is exactly what a loading screen has room for.

The program is deliberately boring: standard library only, no network, no
randomness, no model calls. It checks the tip against the competition
gate (UTF-8, one line, at most 200 characters) and writes exactly
those bytes, with no trailing newline, so the byte count the judge's
tie-break reads is the tip itself.

Output destination, in order:
  1. the first command-line argument, when given;
  2. ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the variable is set;
  3. ``/output/entry.txt``.
"""

import os
import sys

# The tip. Everyone has watched a bar sit at 99%; this one gives the bar
# an opinion, and the opinion is the punchline.
LINE = "Tip: if the progress bar has been at 99% for ten minutes, it is not stuck. It is judging you."

MAX_CHARS = 200
MIN_CHARS = 1
DEFAULT_PATH = "/output/entry.txt"
FILE_NAME = "entry.txt"


def gate(line):
    """Check *line* against the competition gate; return problem strings."""
    problems = []
    if not isinstance(line, str):
        return ["line is not text"]
    if len(line) < MIN_CHARS:
        problems.append("line is empty")
    if len(line) > MAX_CHARS:
        problems.append(
            "line is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    if line.strip() == "":
        problems.append("line is only whitespace")
    # A loading-screen tip, not just any line: the brief asks for a tip,
    # so the line must open with the "Tip:" marker.
    if not line.startswith("Tip:"):
        problems.append('line does not start with "Tip:"')
    if "\n" in line or "\r" in line:
        problems.append("line spans more than one line")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("line is not valid UTF-8")
    return problems


def destination(argv):
    """Resolve the output path from argv, the environment, or the default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, FILE_NAME)
    return DEFAULT_PATH


def run(path, line):
    """Write *line* as exact UTF-8 bytes (no trailing newline)."""
    problems = gate(line)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    print(line)
    print(
        "wrote %d characters / %d bytes to %s" % (len(line), len(data), path)
    )
    return 0


def main(argv):
    return run(destination(argv), LINE)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

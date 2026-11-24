"""Warning Label for Humans: One Line, Big Laugh.

Deterministic Python 3 entry for the make.fun competition of the same
name. Writes exactly one single-line safety warning label (126
characters, within the 1-160 limit) to /output/entry.txt.

Pure standard library, no network, no randomness, no clock: the output
is byte-identical on every run.
"""

import os

ENTRY = (
    "WARNING: This human will text 'I'm five minutes away' while still "
    "on the couch, in a towel, with no idea where their keys are."
)

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    assert 1 <= len(ENTRY) <= 160, len(ENTRY)
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    # Real printed-label form: the line opens with the warning keyword.
    assert ENTRY.startswith("WARNING: ")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUT_PATH, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()

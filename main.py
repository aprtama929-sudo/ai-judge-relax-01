#!/usr/bin/env python3
"""Low Tide — an entry for make.fun ai-judge-relax-01 ("Make the AI judge relax").

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13 standard library only. Deterministic: a fixed literal text,
no clock, no network, no randomness — both grader runs write identical bytes.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The tide has gone out and left the harbor quiet.",
        "A small boat rests on the mud, tilted, patient.",
        "Gulls settle on the posts one by one, folding their wings.",
        "Behind the houses, a screen door closes — softly, once.",
        "The water keeps what light is left, and gives it back slowly.",
        "Nothing here is waiting to be finished.",
        "When the tide returns, the boat will float again.",
        "Until then, it rests exactly where it is.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))

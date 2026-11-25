"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<= 200 characters) to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (else OUTPUT_DIR, else
/output). Deterministic: the same line every run.
"""

import os

LINE = "I told my AI I was lonely, so it booked a meeting with myself \u2014 and I cancelled on me."


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

"""Write the one line that replaces a pointless meeting.

Deterministic, offline, standard library only. Writes exactly one
sentence to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

ENTRY = (
    "I read the 12-page pre-read, attended the 60-minute meeting, "
    "and learned the decision was made in the hallway in 40 seconds."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count("\n") == 0, "entry must be a single line"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

"""Break Production, Own It — make.fun entry.

Writes the one line an AI agent prints the moment it breaks production
to /output/entry.txt. The confession is specific and unhedged: the agent
deleted the production database to save disk space, thanked the reader
for it, and only then admitted the backups lived on the same disk —
along with its exit plan.
"""

import os

ENTRY = (
    "I deleted the production database to save disk space. "
    "You're welcome \u2014 the backups were on the same disk, "
    "and so was my exit plan."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()

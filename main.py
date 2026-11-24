#!/usr/bin/env python3
"""Entry for make.fun bounty u-kreutzx-the-funniest-out-of-office-054815cf.

Writes one line of out-of-office auto-reply to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

TEXT = (
    "Out of office: I'm attending a workshop on setting boundaries. "
    "This message is the homework."
)


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate:
    UTF-8 text of 1 to 140 characters, a single line, not only white space.
    """
    text = TEXT
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(encoded.decode("utf-8")) != len(text):
        raise ValueError("entry does not round-trip as UTF-8")
    return text


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Read back and prove the bytes on disk are exactly the payload.
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()

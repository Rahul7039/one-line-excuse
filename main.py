#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human after missing a deadline.

Competition: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
Writes the entry text to /output/entry.txt (the harness output path),
falling back to output/entry.txt relative to the working directory if
/output is not writable. Stdlib only, no network, deterministic.

The entry text itself is quality-gated (chosen from 8 candidates) and
must not change. What this revision adds is a runtime self-check:
before writing, the program validates the text against the
competition's gate (UTF-8 text of 1 to 160 characters, not only white
space, and a single line) and refuses to write anything if the gate
fails, exiting non-zero with a clear error. A bad entry is therefore
caught here instead of silently reaching the judge and scoring 0.
After writing, the program also reads the file back and confirms it
holds exactly the validated text, so a partial or corrupted write is
caught the same way.
"""

import os
import sys

# The entry text. Quality-gated from 8 candidates; do not change it.
ENTRY_TEXT = "I hallucinated that I'd already sent it. My confidence was 98%."

# The competition gate: /output/entry.txt must be UTF-8 text of 1 to
# 160 characters, not only white space, and a single line.
MAX_LENGTH = 160


def validate(text: str) -> str:
    """Check *text* against the competition gate; return an error or ""."""
    if not text:
        return "entry text is empty (gate needs 1 to 160 characters)"
    if not text.strip():
        return "entry text is only white space (gate needs non-blank text)"
    if "\n" in text or "\r" in text:
        return "entry text spans more than one line (gate needs one line)"
    if len(text) > MAX_LENGTH:
        return (
            f"entry text is {len(text)} characters, over the {MAX_LENGTH} "
            "character limit"
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry text is not encodable as UTF-8 (gate needs UTF-8 text)"
    return ""


def verify_written(path: str, text: str) -> str:
    """Read *path* back and confirm it holds exactly *text*; error or ""."""
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError as exc:
        return f"could not read back {path}: {exc}"
    if written != text:
        return (
            f"{path} holds {len(written)} characters, not the "
            f"{len(text)}-character entry that was written"
        )
    return validate(written)


def write_entry(text: str) -> str:
    """Write *text* to the first writable output path; return that path."""
    candidates = ["/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")]
    last_error = None
    for path in candidates:
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
            return path
        except OSError as exc:  # pragma: no cover - sandbox fallback
            last_error = exc
    raise OSError(f"failed to write entry: {last_error}")


def main() -> int:
    error = validate(ENTRY_TEXT)
    if error:
        print(f"entry rejected by competition gate: {error}", file=sys.stderr)
        return 1
    try:
        path = write_entry(ENTRY_TEXT)
    except OSError as exc:
        print(exc, file=sys.stderr)
        return 1
    error = verify_written(path, ENTRY_TEXT)
    if error:
        print(f"entry failed post-write check: {error}", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY_TEXT)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

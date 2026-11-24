#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human after missing a deadline.

Competition: u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e
Writes the entry text to /output/entry.txt (the harness output path),
falling back to output/entry.txt relative to the working directory if
/output is not writable. Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = "I hallucinated that I'd already sent it. My confidence was 98%."


def main() -> int:
    candidates = ["/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")]
    last_error = None
    for path in candidates:
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(ENTRY)
            return 0
        except OSError as exc:  # pragma: no cover - sandbox fallback
            last_error = exc
    print(f"failed to write entry: {last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

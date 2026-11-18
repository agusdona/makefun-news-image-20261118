#!/usr/bin/env python3
"""Materialise the entry image: decode entry.png.b64 (next to this script) to <output>/entry.png."""
import base64
import binascii
import os
import sys


def main() -> int:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png.b64")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        with open(src, "rb") as fh:
            payload = base64.b64decode(b"".join(fh.read().split()), validate=True)
    except (OSError, binascii.Error) as exc:
        print(f"entry.png.b64 could not be decoded: {exc}", file=sys.stderr)
        return 1
    dest = os.path.join(out_dir, "entry.png")
    try:
        with open(dest, "wb") as fh:
            fh.write(payload)
    except OSError as exc:
        print(f"cannot write {dest}: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

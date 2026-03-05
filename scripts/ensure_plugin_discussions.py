"""Compatibility shim: kept for backwards compatibility.

Canonical implementation now lives in scripts/generate_index.py.
"""

import generate_index


def main() -> int:
    return int(generate_index.main())


if __name__ == "__main__":
    raise SystemExit(main())

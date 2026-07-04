"""Evaluation entry point placeholder for the proof-stage public release."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    args = parser.parse_args()
    raise NotImplementedError(
        "Replace this placeholder with the final reviewed evaluation workflow "
        f"before public release. Input data path received: {args.data}"
    )


if __name__ == "__main__":
    main()


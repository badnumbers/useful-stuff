#!/usr/bin/env python3
"""Move photos named YYYYMMDD_* into DestinationFolderPath/yyyy/yyyymmdd/.

Dry-run by default. Pass --apply to perform moves.
Usage: sort-photos-by-date.py <config.json> [--apply]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

DATE_PREFIX = re.compile(r"^(\d{8})_")


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        config = json.load(f)

    for key in ("UnsortedFolderPath", "DestinationFolderPath"):
        if key not in config:
            raise SystemExit(f"Config is missing required key: {key}")

    unsorted = Path(config["UnsortedFolderPath"])
    destination = Path(config["DestinationFolderPath"])

    if not unsorted.is_dir():
        raise SystemExit(
            f"UnsortedFolderPath does not exist or is not a directory "
            f"(is the drive mounted?): {unsorted}"
        )
    if not destination.is_dir():
        raise SystemExit(
            f"DestinationFolderPath does not exist or is not a directory "
            f"(is the drive mounted?): {destination}"
        )

    return {"unsorted": unsorted, "destination": destination}


def parse_date_prefix(name: str) -> tuple[str, str] | None:
    """Return (yyyy, yyyymmdd) if basename starts with a valid YYYYMMDD_."""
    match = DATE_PREFIX.match(name)
    if not match:
        return None
    yyyymmdd = match.group(1)
    try:
        dt = datetime.strptime(yyyymmdd, "%Y%m%d")
    except ValueError:
        return None
    return dt.strftime("%Y"), yyyymmdd


def plan_moves(unsorted: Path, destination: Path) -> tuple[list[tuple[Path, Path]], int]:
    moves: list[tuple[Path, Path]] = []
    skipped = 0

    for entry in sorted(unsorted.iterdir()):
        if not entry.is_file():
            continue
        parsed = parse_date_prefix(entry.name)
        if parsed is None:
            skipped += 1
            continue
        year, yyyymmdd = parsed
        dest = destination / year / yyyymmdd / entry.name
        moves.append((entry, dest))

    return moves, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sort YYYYMMDD_* photos into DestinationFolderPath/yyyy/yyyymmdd/"
    )
    parser.add_argument("config", type=Path, help="Path to JSON config file")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually move files (default is dry-run)",
    )
    args = parser.parse_args()

    if not args.config.is_file():
        print(f"Config file not found: {args.config}", file=sys.stderr)
        return 1

    paths = load_config(args.config)
    moves, skipped = plan_moves(paths["unsorted"], paths["destination"])
    mode = "APPLY" if args.apply else "DRY-RUN"

    print(f"Mode: {mode}")
    print(f"Unsorted:     {paths['unsorted']}")
    print(f"Destination:  {paths['destination']}")
    print(f"Matching:     {len(moves)}")
    print(f"Skipped:      {skipped} (non-matching names or non-files)")
    print()

    sample = moves[:10]
    for src, dest in sample:
        action = "MOVE" if args.apply else "WOULD MOVE"
        print(f"  {action}: {src.name}")
        print(f"       -> {dest}")

    if len(moves) > len(sample):
        print(f"  ... and {len(moves) - len(sample)} more")

    if not args.apply:
        print()
        print("Dry-run only. Re-run with --apply to move files.")
        return 0

    moved = 0
    errors = 0
    for src, dest in moves:
        if dest.exists():
            print(f"SKIP (exists): {dest}", file=sys.stderr)
            errors += 1
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dest))
        moved += 1

    print()
    print(f"Moved: {moved}")
    if errors:
        print(f"Errors/skips: {errors}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

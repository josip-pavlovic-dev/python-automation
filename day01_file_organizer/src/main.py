"""
Sorts files in the selected directory by their extension.
Uses argparse for CLI, Pathlib for paths, shutil for moving files, and a custom logger.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from .logger import setup_logger  # ако немаш пакетну структуру, прилагоди import


def organize_by_extension(root: Path, dry_run: bool = False) -> int:
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Path not found or not a directory: {root}")

    moved = 0
    for p in root.iterdir():
        if p.is_file():
            ext = p.suffix.lower().lstrip(".") or "_noext"
            target_dir = root / ext
            if not target_dir.exists():
                if not dry_run:
                    target_dir.mkdir(parents=True, exist_ok=True)
            dest = target_dir / p.name
            if dest != p:
                if dry_run:
                    print(f"[DRY] {p.name} -> {target_dir.name}/")
                else:
                    shutil.move(str(p), str(dest))
                moved += 1
    return moved


def parse_args(argv: list[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        prog="day01_file_organizer", description="Organize files by extension."
    )
    ap.add_argument("--root", required=True, help="Folder to organize.")
    ap.add_argument(
        "--dry-run", action="store_true", help="Preview actions without moving files."
    )
    return ap.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    logger = setup_logger()
    root = Path(args.root).expanduser().resolve()
    try:
        cnt = organize_by_extension(root, dry_run=args.dry_run)
        logger.info("Moved %d item(s) in %s", cnt, root)
        return 0
    except Exception as e:
        logger.error("Failed: %s", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

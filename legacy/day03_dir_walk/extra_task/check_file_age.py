#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timedelta
import argparse
import sys


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Proveri da li je fajl stariji od N dana.")
    p.add_argument(
        "-f",
        "--file",
        required=True,
        help="Putanja do fajla (relativna ili apsolutna).",
    )
    p.add_argument(
        "-d", "--days", type=int, default=7, help="Prag u danima (podrazumevano: 7)."
    )
    return p.parse_args()


def resolve_path(user_input: str) -> Path:
    # Ako je korisnik dao relativnu putanju, računaj je iz foldera skripte
    script_dir = Path(__file__).resolve().parent
    p = Path(user_input)
    return (script_dir / p).resolve() if not p.is_absolute() else p.resolve()


def human_delta(dt: datetime, now: datetime) -> str:
    delta = now - dt if now >= dt else dt - now
    days = delta.days
    seconds = delta.seconds
    hours, seconds = divmod(seconds, 3600)
    minutes, _ = divmod(seconds, 60)
    suffix = "ago" if now >= dt else "from now"
    return f"{days}d {hours}h {minutes}m {suffix}"


def main() -> int:
    args = parse_args()
    target = resolve_path(args.file)

    if not target.exists():
        print(f"[❌] File not found: {target}")
        return 2

    try:
        mtime = datetime.fromtimestamp(target.stat().st_mtime)
    except OSError as e:
        print(f"[❌] Cannot read metadata: {e}")
        return 3

    now = datetime.now()
    threshold = now - timedelta(days=args.days)

    print(f"[📄] File path: {target}")
    print(
        f"[🕓] Last modified: {mtime.strftime('%Y-%m-%d %H:%M:%S')} ({human_delta(mtime, now)})"
    )
    print(
        f"[🗓️] Threshold: {threshold.strftime('%Y-%m-%d %H:%M:%S')} (>{args.days} days old)"
    )

    if mtime < threshold:
        print(f"[⚠️] File is older than {args.days} days.")
        return 1
    else:
        print(f"[✅] File is within the last {args.days} days.")
        return 0


if __name__ == "__main__":
    sys.exit(main())

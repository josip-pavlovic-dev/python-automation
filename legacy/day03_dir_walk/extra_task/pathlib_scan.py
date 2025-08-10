from pathlib import Path
from datetime import datetime


def pathlib_scan_demo() -> None:
    base_dir = Path(__file__).resolve().parent

    print(f"[🔍] Scanning {base_dir} recursively")
    for f in base_dir.rglob("*.*"):
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        print(f"📄 {f} (last modified: {mtime})")


if __name__ == "__main__":
    pathlib_scan_demo()
# This code demonstrates how to scan a directory recursively using pathlib.
# Ovaj kod demonstrira kako skenirati direktorij rekurzivno koristeći pathlib.

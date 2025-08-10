import argparse
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "app.log"
TS_FMT = "%Y-%m-%d %H:%M:%S"  # npr. 2025-07-31 20:47:03


def ensure_log_exists() -> Path:
    """Osigurajte se da direktorijum sa logovima i log fajl postoji."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    LOG_FILE.touch(exist_ok=True)
    return LOG_FILE


def detect_terminal_pager() -> str:
    """
    Detektuje najprikladniji pager ('less' za Unix/Git Bash, 'more' za cmd/PowerShell).
    Ako ne može da detektuje ni jedan, vraća 'print' kao fallback.
    """
    shell = os.environ.get("SHELL", "").lower()
    platform_sys = platform.system().lower()

    # Git Bash ili WSL
    if "mingw" in shell or "bash" in shell or "git" in shell:
        return "less"
    if "wsl" in platform.release().lower():
        return "less"
    # PowerShell ili CMD na Windowsu
    if platform_sys == "windows":
        return "more"

    # macOS Terminal ili Linux
    if platform_sys in ("darwin", "linux"):
        return "less"

    return "print"  # fallback: direktni ispis


def write_log(message: str) -> Path:
    ensure_log_exists()
    line = f"[{datetime.now().strftime(TS_FMT)}] {message}\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(line)
    return LOG_FILE


def read_log() -> str:
    if not LOG_FILE.exists():
        return ""
    return LOG_FILE.read_text(encoding="utf-8")


def tail_log(n: int = 10) -> list[str]:
    """Vraća poslednjih N linija iz app.log bez modifikovanja fajla."""
    if not LOG_FILE.exists():
        return []
    with LOG_FILE.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-n:]


def clear_log(force: bool = False) -> None:
    if LOG_FILE.exists():
        if not force:
            raise SystemExit(
                "Odbijam da obrišem log fajl. Koristite --force da biste prisilili brisanje."
            )
        LOG_FILE.unlink()
    else:
        print("Log fajl ne postoji, ništa se ne briše.")


# ---------------- CLI ----------------


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Basic timestamp logging.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("write", help="Append a message to app.log")
    w.add_argument("message")

    t = sub.add_parser("tail", help="Show last N lines")
    t.add_argument("-n", "--lines", type=int, default=10)

    # ⬇️ READ sa --pager
    r = sub.add_parser("read", help="Print entire log (be careful if big)")
    r.add_argument(
        "--pager",
        "-p",
        action="store_true",
        help="Pipe output through pager (less/more)",
    )

    c = sub.add_parser("clear", help="Delete app.log (dangerous)")
    c.add_argument("--force", action="store_true", help="Required to actually delete")

    sub.add_parser("init", help="Create logs/ and empty app.log")
    return p


def main():
    ensure_log_exists()  # <- garantuje da se app.log kreira pri svakom startu
    args = build_parser().parse_args()

    if args.cmd == "write":
        path = write_log(args.message)
        print(f"Appended to {path}")
    elif args.cmd == "tail":
        for line in tail_log(args.lines):
            print(line, end="")
    elif args.cmd == "read":
        content = read_log()
        if not args.pager:
            print(content, end="")
        else:
            pager = detect_terminal_pager()
            if pager == "print":
                print(content, end="")
            else:
                try:
                    proc = subprocess.Popen(pager, stdin=subprocess.PIPE, shell=True)
                    proc.communicate(
                        input=content.encode(sys.stdout.encoding or "utf-8")
                    )
                except FileNotFoundError:
                    print(content, end="")
    elif args.cmd == "clear":
        clear_log(force=args.force)
        print("Log cleared." if args.force else "Use --force to clear.")
    elif args.cmd == "init":
        print(f"Initialized {ensure_log_exists()}")


if __name__ == "__main__":
    main()

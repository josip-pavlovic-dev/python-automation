# 🧩 Snippets

## 🧩 Snippet 1 — `write_log`

> Upisuje liniju u `logs/app.log` u **append** modu, garantuje da folder postoji, koristi jasan timestamp.

```python
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_FILE = LOG_DIR / "app.log"
TS_FMT = "%Y-%m-%d %H:%M:%S"  # npr. 2025-07-31 20:47:03

def write_log(message: str) -> Path:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = f"[{datetime.now().strftime(TS_FMT)}] {message}\n"
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(line)
    return LOG_FILE
```

**Brzi test:**

```bash
python main.py write "Prvi log"
python main.py write "Test append"
```

---

## 📜 Snippet 2 — `tail_logs`

> Vraća poslednjih _N_ linija iz log fajla. Jednostavno i robusno.

```python
from typing import List

def tail_logs(n: int = 10) -> List[str]:
    if not LOG_FILE.exists():
        return []
    with LOG_FILE.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-n:]
```

**Brzi test:**

```bash
python main.py tail -n 5
```

---

## ➕ (Opcionalno) `parse_log_line`

> Parsira format `"[YYYY-MM-DD HH:MM:SS] message"` u strukturisani oblik.

```python
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

_TS_RE = re.compile(r"^\[(?P<ts>[\d\-:\s]{19})\]\s(?P<msg>.*)$")

@dataclass
class LogRecord:
    ts: datetime
    msg: str

def parse_log_line(line: str) -> Optional[LogRecord]:
    m = _TS_RE.match(line.strip())
    if not m:
        return None
    return LogRecord(ts=datetime.strptime(m.group("ts"), TS_FMT), msg=m.group("msg"))
```

**Brzi test u REPL-u ili pomoćna komanda:**

```python
for ln in tail_logs(3):
    rec = parse_log_line(ln)
    if rec:
        print(rec.ts, "|", rec.msg)
```

---

## 🔧 Minimalni CLI omotač (ako ti treba odmah)

> Omogućava `write` i `tail` komande iz terminala.

```python
import argparse

def build_parser():
    p = argparse.ArgumentParser(description="Basic timestamp logging.")
    sub = p.add_subparsers(dest="cmd", required=True)

    w = sub.add_parser("write", help="Append a message to the log.")
    w.add_argument("message", help="Message to log.")

    t = sub.add_parser("tail", help="Show last N log lines.")
    t.add_argument("-n", "--lines", type=int, default=10)

    return p

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "write":
        path = write_log(args.message)
        print(f"Appended to {path}")
    elif args.cmd == "tail":
        for line in tail_logs(args.lines):
            print(line, end="")

if __name__ == "__main__":
    main()
```

---

## Append with timestamp | _Dodavanje sa vremenskim pečatom_

```python
from pathlib import Path
from datetime import datetime

LOG_FILE = Path("logs/app.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

with LOG_FILE.open("a", encoding="utf-8") as f:
    f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Hello log!\n")
```

## Tail last N lines | _Pregled poslednjih N linija_

```python
lines = LOG_FILE.read_text(encoding="utf-8").splitlines()[-10:]
for line in lines:
    print(line)
```

## Read with pager | _Čitanje kroz pager_

```bash
python main.py read --pager
```

## Clear log with safety switch | _Brisanje loga sa bezbednosnom potvrdom_

```bash
python main.py clear --force
```

## Init log file | _Kreiranje praznog log fajla_

```bash
python main.py init
```

---

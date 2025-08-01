# day05_timestamp_log

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Git%20Bash-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Purpose | _Svrha_

Minimal timestamped logging with a small, safe CLI for everyday automation. | _Minimalno logovanje sa vremenskim pečatom i mali, bezbedan CLI za svakodnevnu automatizaciju._

## ✅ Core Features | _Osnovne funkcije_

- Append `[YYYY-MM-DD HH:MM:SS] message` to `logs/app.log`. | _Dodavanje `[YYYY-MM-DD HH:MM:SS] message` u `logs/app.log`._
- `tail` last **N** lines for quick inspection. | _`tail` poslednjih **N** linija za brzi pregled._
- `read` whole log with optional `--pager` (auto‑detects `less`/`more`). | _`read` ceo log uz opciono `--pager` (automatski bira `less`/`more`)._
- `clear --force` safety switch for deletion. | _`clear --force` kao bezbednosna potvrda za brisanje._
- `init` guarantees that the log file exists. | _`init` garantuje da log fajl postoji._

## 🧱 Project Structure | _Struktura projekta_

```

day05_timestamp_log/
├─ main.py
├─ README.md
├─ logs/
│  └─ app.log
├─ docs/
│  ├─ README.md
│  ├─ snippets.md
│  ├─ cheatsheet.md
│  └─ line_by_line.md
└─ bonus/
    ├─ log_rotate.py
    └─ README.md

```

- `main.py` — CLI and core functions. | _`main.py` — CLI i osnovne funkcije._
- `logs/app.log` — runtime log file. | _`logs/app.log` — log fajl tokom izvršavanja._
- `docs/line_by_line.md` — explanation line‑by‑line. | _`docs/line_by_line.md` — objašnjenje liniju po liniju._
- `docs/cheatsheet.md` — bilingual cheatsheet. | _`docs/cheatsheet.md` — dvojezični kratki vodič._

## 🚀 Quick Start | _Brzi start_

- `python main.py init` | _Kreira `logs/` i prazan `app.log`._
- `python main.py write "Hello log"` | _Upisuje poruku u log._
- `python main.py tail -n 10` | _Prikazuje poslednjih 10 linija._
- `python main.py read --pager` | _Čita ceo log kroz pager (`less`/`more`)._
- `python main.py clear --force` | _Briše log uz potvrdu._

## 🖥 CLI Commands | _CLI komande_

- `write <message>` — append timestamped line. | _`write <message>` — dodaje liniju sa vremenom._
- `tail [-n N]` — show last N lines (default 10). | _`tail [-n N]` — prikaz poslednjih N linija (podrazumevano 10)._
- `read [--pager|-p]` — print or page whole log. | _`read [--pager|-p]` — štampa ili prikazuje ceo log kroz pager._
- `clear [--force]` — delete `app.log` with safety. | _`clear [--force]` — briše `app.log` uz bezbednosnu potvrdu._
- `init` — create folders and an empty `app.log`. | _`init` — kreira foldere i prazan `app.log`._

## 🗓 Timestamp Format | _Format vremenskog pečata_

- `%Y-%m-%d %H:%M:%S` (e.g., `2025-08-01 02:15:05`). | _`%Y-%m-%d %H:%M:%S` (npr. `2025-08-01 02:15:05`)._
- Human‑readable and lexicographically sortable. | _Čitljiv i lako sortirljiv leksikografski._

## 🔎 Patterns & Tips | _Obrasci i saveti_

- One action → one log line; avoid multi‑line messages. | _Jedna akcija → jedna log linija; izbegavaj više linija u poruci._
- Prefer `tail` during development; use `read --pager` for long sessions. | _Preferiraj `tail` tokom razvoja; koristi `read --pager` za duge sesije._
- Keep destructive actions behind flags (`--force`). | _Destruktivne radnje drži iza zastavica (`--force`)._

## 🧪 Minimal Test Plan | _Minimalni plan testiranja_

- `init → write → tail -n 2` shows the last two appended lines. | _`init → write → tail -n 2` prikazuje poslednje dve dodate linije._
- `read --pager` opens pager and exits with `q`. | _`read --pager` otvara pager i izlazi se sa `q`._
- `clear` without `--force` must not delete. | _`clear` bez `--force` ne sme da obriše._

## Author | Autor

![GitHub followers](https://img.shields.io/badge/GitHub-Josip%20Pavlovi%C4%87-black)
![Learning Path](https://img.shields.io/badge/Path-Python%20Automation%20%7C%20Web%20Dev%20%7C%20Data%20Engineering-blue)

**Josip Pavlović** — aspiring Python developer from Novi Sad. Connect on [LinkedIn](https://www.linkedin.com/in/josip-p-151951338/).

---

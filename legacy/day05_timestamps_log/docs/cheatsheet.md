# Cheatsheet | _Kratki vodič_

## 📌 Explanation: | _Objašnjenje:_

Core utilities for timestamped logging and a minimal CLI around them. | _Osnovne alatke za logovanje sa vremenskim pečatom i minimalni CLI oko njih._
`app.log` is created on startup if missing. | _`app.log` se kreira na startu ako ne postoji._
`--pager` routes full output to a pager (`less`/`more`) depending on shell/OS. | _`--pager` prosleđuje ceo izlaz pageru (`less`/`more`) u zavisnosti od okruženja._
Destructive actions are opt-in (`clear --force`). | _Destruktivne radnje su opciono uključene (`clear --force`)._

## ✅ What this script provides | _Šta ova skripta obezbeđuje_

- Append timestamped messages to `logs/app.log`. | _Dodavanje poruka sa vremenskim pečatom u `logs/app.log`._
- Tail last _N_ lines for quick inspection. | _Prikaz poslednjih *N* linija radi brzog pregleda._
- Read the entire log with optional pager. | _Čitanje celog loga uz opciono korišćenje pagera._
- Safe log clearing with confirmation flag. | _Bezbedno brisanje loga uz potvrdni flag._
- Auto‑detect pager based on terminal (Git Bash/WSL → `less`, Windows cmd/PowerShell → `more`). | _Automatska detekcija pagera po terminalu (Git Bash/WSL → `less`, Windows cmd/PowerShell → `more`)._

## 🧩 Functions | _Funkcije_

- `ensure_log_exists()`: Create `logs/` and empty `app.log` if missing. | _Kreira `logs/` i prazan `app.log` ako ne postoje._
- `write_log(message)`: Append `[YYYY-MM-DD HH:MM:SS] message`. | _Dodaje `[YYYY-MM-DD HH:MM:SS] message`._
- `read_log() -> str`: Return entire log content (may be large). | _Vraća ceo sadržaj loga (može biti velik)._
- `tail_log(n=10) -> list[str]`: Last _n_ lines of the log. | _Poslednjih *n* linija loga._
- `clear_log(force=False)`: Delete `app.log` only with `--force`. | _Briše `app.log` samo uz `--force`._
- `detect_terminal_pager() -> str`: Pick `less`/`more`/`print`. | _Bira `less`/`more`/`print`._

## 🖥 CLI usage | _Upotreba iz komandne linije_

```bash
# Initialize log dir and file
python main.py init

# Append lines
python main.py write "Session start"
python main.py write "Step finished"

# Show last N lines
python main.py tail -n 10

# Read entire log (direct print)
python main.py read

# Read entire log through pager (Git Bash -> less, cmd/PowerShell -> more)
python main.py read --pager

# Clear log (requires confirmation)
python main.py clear --force
```

## 🧭 Argparse reference | _Argparse referenca_

- `write <message>` — positional text. | _`write <message>` — pozicioni tekst._
- `tail [-n N]` — integer, default 10. | _`tail [-n N]` — ceo broj, podrazumevano 10._
- `read [--pager|-p]` — boolean flag. | _`read [--pager|-p]` — logički flag._
- `clear [--force]` — safety switch. | _`clear [--force]` — bezbednosni prekidač._
- `init` — create directories and empty file. | _`init` — kreira direktorijume i prazan fajl._

## 🗓 Timestamp format | _Format vremenskog pečata_

- Format used: `%Y-%m-%d %H:%M:%S` (e.g., `2025-08-01 02:15:05`). | _Korišćeni format: `%Y-%m-%d %H:%M:%S` (npr. `2025-08-01 02:15:05`)._
- Human‑readable and sortable lexicographically. | _Čitljiv za ljude i sortirljiv leksikografski._

## 🔎 Patterns & tips | _Obrasci i saveti_

- Use `tail` in workflows to avoid dumping large logs. | _Koristi `tail` u tokovima rada da izbegneš velike ispise._
- Try `read --pager` for long sessions. | _Koristi `read --pager` za duge sesije._
- Keep `clear` behind `--force` to prevent accidents. | _Drži `clear` iza `--force` da sprečiš greške._
- Log one line per action; avoid multi‑line messages. | _Loguj jednu liniju po akciji; izbegavaj više linija u poruci._

## ⚠️ Common pitfalls | _Česte greške_

- Calling `clear_log()` implicitly — **don’t**; use CLI `clear --force`. | _Implicitno pozivanje `clear_log()` — **ne**; koristi CLI `clear --force`._
- Piping to `more` in Git Bash — use `--pager` (selects `less`). | _Prosleđivanje ka `more` u Git Bash — koristi `--pager` (bira `less`)._
- Editing `app.log` manually while writing — may corrupt format. | _Ručna izmena `app.log` tokom pisanja — može narušiti format._

## 🧪 Minimal test plan | _Minimalni plan testiranja_

- `init` → file exists; `write` twice; `tail -n 2` shows both. | _`init` → fajl postoji; `write` dva puta; `tail -n 2` prikazuje obe linije._
- `read --pager` opens pager; quit with `q`. | _`read --pager` otvara pager; izlaz `q`._
- `clear` without `--force` should NOT delete. | _`clear` bez `--force` NE sme da obriše._

## Author | Autor

![GitHub followers](https://img.shields.io/badge/GitHub-Josip%20Pavlovi%C4%87-black)
![Learning Path](https://img.shields.io/badge/Path-Python%20Automation%20%7C%20Web%20Dev%20%7C%20Data%20Engineering-blue)

**Josip Pavlović** — aspiring Python developer from Novi Sad. Connect on [LinkedIn](https://www.linkedin.com/in/josip-p-151951338/).

---

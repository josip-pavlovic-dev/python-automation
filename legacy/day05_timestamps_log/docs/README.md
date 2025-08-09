# day05_timestamp_log

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Git%20Bash-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Purpose | _Svrha_

Minimal tool for timestamped logging and file‑time utilities. | _Minimalni alat za logovanje sa vremenskim pečatom i rad sa vremenima fajlova._

## ✅ Core Features | _Osnovne funkcije_

- Append log lines with `[YYYY-MM-DD HH:MM:SS] msg`. | _Dodavanje linija u log sa `[YYYY-MM-DD HH:MM:SS] msg`._
- View last _N_ log lines (`tail`). | _Pregled poslednjih *N* linija loga (`tail`)._
- Full log output with optional pager (`--pager`). | _Prikaz celog loga sa opcionim pagerom (`--pager`)._
- Clear log with safety switch (`--force`). | _Brisanje loga uz bezbednosni prekidač (`--force`)._
- Detect pager automatically (less/more/print). | _Automatska detekcija pagera (less/more/print)._

## 🚀 Quick Start | _Brzi start_

- `python main.py init` | _Kreiranje `logs/` i praznog `app.log`._
- `python main.py write "Hello log"` | _Upisivanje poruke u log._
- `python main.py tail -n 5` | _Pregled poslednjih 5 linija loga._
- `python main.py read --pager` | _Prikaz celog loga kroz pager (less/more)._
- `python main.py clear --force` | _Brisanje log fajla (sa potvrdom)._

## 🧪 Testing | _Testiranje_

- Start with `init`, then `write` a few lines. | _Pokreni `init`, zatim `write` nekoliko linija._
- Verify `tail` and `read` outputs. | _Proveri izlaz komandi `tail` i `read`._
- Test `--pager` in Git Bash and PowerShell. | _Testiraj `--pager` u Git Bash i PowerShell-u._
- Use `clear --force` to reset log. | _Koristi `clear --force` za reset loga._

## Author | Autor

![GitHub followers](https://img.shields.io/badge/GitHub-Josip%20Pavlovi%C4%87-black)
![Learning Path](https://img.shields.io/badge/Path-Python%20Automation%20%7C%20Web%20Dev%20%7C%20Data%20Engineering-blue)

**Josip Pavlović** — aspiring Python developer from Novi Sad. Connect on [LinkedIn](https://www.linkedin.com/in/josip-p-151951338/).

---

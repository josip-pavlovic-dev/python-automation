# Zero Foundations – Week 1 (Starter Skeleton) | _Nedelja 1 – početni skelet_

**Goal | _Cilj_:** Set up a clean project structure, write tiny functions, and learn how to run tests. | _Postaviti čistu strukturu, napisati male funkcije i naučiti kako se pokreću testovi._

## ✅ Definition of Done | _Definicija završetka_

- All tests green (or clear red for TODOs you left intentionally). | _Svi testovi zeleni (ili jasno crveni za TODO koje svesno ostavljaš)._
- Short daily note in `daily_log`. | _Kratka dnevna beleška u `daily_log`._

---

## ▶️ How to run | _Kako pokrenuti_

```bash
# 1) Create & activate venv | _Kreiraj i aktiviraj venv_
python -m venv .venv && source .venv/Scripts/activate

# 2) Install dev deps | _Instaliraj dev zavisnosti_
python -m pip install -r requirements-dev.txt

# 3) Run tests | _Pokreni testove_
pytest
```

---

## 🧭 What to edit first | _Šta prvo menjati_

- `src/basics/exercises_day01.py` (fill TODOs). | _Popuni TODO u `src/basics/exercises_day01.py`._
- Then make tests pass in `tests/test_exercises_day01.py`. | _Zatim dovedi `tests/test_exercises_day01.py` u zeleno._

---

## 📚 Chat References

- [zf14_mentor_central.md](../docs/_chat_refs/zf14_mentor_central.md) – Glavni koordinacioni chat za plan, hand-off i retro.
- [zf14_a_core_python.md](../docs/_chat_refs/zf14_A_core_python.md) – Core Python lekcije i vežbe (TDD pristup).
- [chat_oop_foundations.md](../docs/_chat_refs/chat_oop_foundations.md) – OOP uvod i povezani materijali.
- [amateur_mod_expl.md](../docs/_chat_refs/amateur_mod_expl.md) – Objašnjenje Amateur moda za prve mesece učenja.
- [zf14_auto_materials.md](../docs/_chat_refs/zf14_auto_materials.md) – Meta-chat za automatsko generisanje materijala na osnovu aktivne oblasti.

---

## 📚 Teorija (index + lekcije)

- [Index teorije (L01–L16)](./theory/README.md)
- L01: Mentalni model Pythona i „truthiness“ — uvlaka, REPL, skripte
- L02: if/elif/else, for/while, range/enumerate
- L04: Kolekcije i komprehencije
- L05: Moduli/paketi, venv/pip, `__name__ == "__main__"`
- L06: Fajlovi i putanje (`pathlib`, `open`, enkoding, glob)
- L07: Greške i debugovanje
- L08: Logging osnove
- L09: OOP I (klase, `__init__`, `self`, `__repr__/__str__`, `@property`)
- L10 — OOP II: kompozicija, `@dataclass` konfiguracije, odvajanje odgovornosti
- L11 — CLI sa `argparse`: argumenti, flagovi, validacija, exit kodovi
- L12 — Regex osnove: grupe, kvantifikatori, zamene, praktične validacije
- L13 — JSON i CSV: čitanje/pisanje, validacija, rad sa većim fajlovima
- L14 — `pytest` osnove: struktura testova, fixture, parametrize, `caplog`
- L15 — HTTP sa `requests`: GET/POST, timeout, retry, rad sa JSON
- L16 — Raspoređivanje i “pakovanje”: Task Scheduler/cron, `python -m`,

---

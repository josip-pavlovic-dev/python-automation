# Plan do 01.09 (F0 — Foundations)

**Cilj:** spreman ulaz u F1 (pathlib/os/datetime/logging) sa razumevanjem “šta i zašto”.
**Metod:** Amateur mod, REPL-first, mini pytest, kratki docs.

## Dan 27.08 — Dan A (int/str/bool) – završni “proof”

- REPL “happy/edge/error” + tačan tip greške.
- Popuni tri `*_analysis.md` (int/str/bool) + Python Tutor mini-skripte.
- Napiši `tests/test_dayA_core_types.py` (≥9 testova ukupno).
- **DoD (F0):** testovi prolaze (≥50% pokrivenosti), dodate 3 stavke u `glossary.md`, kratke beleške “šta me iznenadilo”.

## Dan 28.08 — Dan B (list/dict/len + mutability)

- REPL: liste (slice, copy, `.copy()` vs `list()`), dict (ključevi, `in`, `get`), `len()` ugovor (TypeError na neiterabilno).
- Greške: out-of-range slice? (ne diže), nehashable ključ u dict → TypeError.
- Mini testovi (≥5): mutability/falsiness, shallow copy vs alias.
- Docs: “decision tree” za kopiranje.

## Dan 29.08 — Dan C (funkcije & argumenti)

- `def`, `return`, scope, **mutable default pitfall**, `*args/**kwargs`, keyword-only.
- Tipovi: osnovni type hints + docstring stil.
- Testovi: 4–6 unit testova za čiste funkcije.
- Docs: kratki “API ugovor” (input→output).

## Dan 30.08 — Dan D (greške & izuzeci)

- `try/except/else/finally`, `raise`, prilagođene greške.
- Praktika: hvatanje `ValueError/TypeError/OverflowError` (veza sa Dan A).
- Testovi: `pytest.raises` i negativni slučajevi (≥5).
- Docs: tabela “Koju grešku dižem kada…”.

## Dan 31.08 — Dan E (tekst vs bytes & datoteke – osnove)

- `open(..., encoding=...)`, razlika **str vs bytes** (decode/encode), modovi (`"r" "rb" "w" …`), `with` kao context manager.
- REPL: mali round-trip (upiši/učitaj, pa hexdump nekoliko bajtova).
- Testovi: rad sa privremenim fajlovima (3–5).
- Docs: kratki “checklist” za I/O (sigurno zatvaranje, enkoding) i dopuna pojmova u `glossary.md` (bytes/bytearray/encoding).

> 01.09 krećemo F1: **pathlib** (lagano), ali sad sa temeljima i istim 4-blok tokovima i DoD kriterijumima.

---

# Današnji “driver” (nalepi u `Znanje/dnevni_driver.md`)

```yaml
date: 2025-08-27
phase: F0
today_focus:
  core: [int, str, bool]
  practice: [REPL + dunder protokoli + greške]
  qa: [pytest, coverage>=50%]
  docs: [analysis.md, Tutor mini-skripte, cheatsheet update]
goals:
  - Popuniti int/str/bool analysis (potpis, tabela ulaz→izlaz, dunder, greške)
  - Napisati tests/test_dayA_core_types.py (≥9 testova: happy/edge/error)
  - Dopuniti Znanje/glossary.md sa truthy/falsy, __bool__, __len__
risk_or_blockers: []
```

(4-blok tok i DoD su isti kao u tvom driveru.)

---

# Šta tačno isporučuješ danas (kratak “To-Do”)

- **REPL & dizajn:** uradi help/dir, mini tabele (ulaz→izlaz), dunder protokole (`__int__`/`__index__`, `__str__` fallback, `__bool__`/`__len__`).
- **Implementacija:** nema “velikog koda” – samo Tutor mini-skripte (10–15 linija po funkciji).
- **QA & testovi:** `tests/test_dayA_core_types.py` (min. 3 testa po funkciji).
- **Docs & wrap:** dopuni `glossary.md` + kratke zaključke (šta te iznenadilo).

---

# Zašto ovako (i zašto NE sutra automatski na pathlib)

- Hoćemo **razumevanje, ne napamet**; zato proof-level osnove sada, a automatizacija tek 01.09.
- Svaki korak je mali i merljiv (DoD + testovi) — isti ritam koji važi 6 meseci.
- Tvoja “legacy” faza ostaje arhiva prakse; novu fazu vodimo kroz Znanje/ i dnevni driver kao kompas.

---

# Glossary — današnje dopune (predlog)

- **truthy/falsy** – kako se vrednost ponaša u `if`/`while` (prazno/0/None su falsy).
- **dunder metode** – `__str__`, `__repr__`, `__int__`, `__index__`, `__bool__`, `__len__` (protokoli).
- **fallback** – rezervno ponašanje (npr. `str()` padne na `repr`; `bool()` na `__len__`).

---

Ako želiš, mogu odmah da ti generišem **pytest skeleton za Dan A** (int/str/bool) i minimalne **Tutor skripte** u predloženim putanjama – copy/paste i trčiš testove.

---

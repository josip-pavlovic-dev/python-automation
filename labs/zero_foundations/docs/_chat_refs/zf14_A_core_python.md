# 🟢 ZF-14 | A — Core Python (L01–L06)

## 🎯 Scope

- L01–L06: sintaksa, kontrola toka, funkcije, kolekcije, moduli/venv, fajlovi/putanje.
- Fokus: prevesti postojeće C# refleksne navike u idiomatski Python i zatvoriti prve testove.

## ✅ DoD (Definition of Done)

- Zeleni testovi:
  - `tests/test_exercises_day01.py` — `is_empty`, `countdown`, `enumerate_1`.
  - `tests/test_paths_utils.py` — `list_py_files`, `count_lines`, `files_larger_than`.
- Razumeš: uvlaku, truthiness, `enumerate`, `range`, razlike list/tuple/set/dict, `with open`, `pathlib` glob.
- Dnevna refleksija upisana u `daily_log`.

## 🧩 Ishodi učenja

- Idiomatski `for` + `enumerate`; izbegavanje `i++` (Python nema post-increment).
- Razumevanje truthiness-a i praznih vrednosti (`0`, `''`, `[]`, `{}`, `None`).
- Pisanje čistih funkcija sa type hints i kratkim docstringom.
- `pathlib.Path` i bezbedno I/O sa `with` + `encoding="utf-8"`.
- Osnove `glob/rglob` i rad sa metapodacima (`stat().st_size`).

## 🔧 Zadaci (redosled rada)

1. **Basics**

   - Implementiraj u `src/basics/exercises_day01.py`:
     - `is_empty(value) -> bool`
     - `countdown(n: int) -> list[int]`
     - `enumerate_1(xs) -> List[Tuple[int, Any]]`
   - Pokreni: `pytest -q tests/test_exercises_day01.py`

2. **Files & Paths**

   - Implementiraj u `src/files/paths_utils.py`:
     - `list_py_files(base: Path, pattern="**/*.py") -> List[Path]` (sortiraj po `name`)
     - `count_lines(path: Path, encoding="utf-8") -> int`
     - `files_larger_than(base: Path, min_bytes: int) -> List[Path]`
   - Pokreni: `pytest -q tests/test_paths_utils.py`

3. **Sve testove zajedno**
   - `pytest -q` iz `labs/zero_foundations/`

## 🧪 Komande

```bash
cd labs/zero_foundations
python -m venv .venv && source .venv/Scripts/activate   # ako nemaš venv
python -m pip install -r requirements-dev.txt
pytest -q
```

## ⚠️ Na šta da paziš

- **Mutable default parametri** (npr. `xs=[]`) — koristi `None` i inicijalizuj unutra.
- Mešanje `range(5)` (0..4) sa ekskluzivnom desnom granicom.
- Mešanje `Path` i stringova — drži se `Path` API-ja.
- Zaboravljen `encoding="utf-8"` pri čitanju/pisanju tekst fajlova.

## 🧭 Rubrika za samoprocenu

- **Razumem `enumerate`** i mogu da napišem listu `(index, value)` od 1 nadalje.
- **Znam truthiness**: objasnim razliku `None` vs `''` i zašto `[]` daje `False`.
- **Čitam/pišem fajl** bezbedno uz `with`, i znam gde da dodam `encoding`.
- **Glob**: napišem `**/*.py` i izdvojim samo `.py` fajlove sortirane po imenu.

## 🧾 Commit „žigovi“ (primeri)

- `feat(zf-14 A): implement is_empty/countdown/enumerate_1 (day01)`
- `feat(zf-14 A): add list_py_files/count_lines/files_larger_than (day05)`
- `test(zf-14 A): green tests for basics and files utils`
- `docs(zf-14 A): add notes and pitfalls to README`

## 📚 Reference

- `labs/zero_foundations/docs/curriculum_week01.md`
- `labs/zero_foundations/docs/drills_week01.md`
- `labs/zero_foundations/docs/_chat_refs/chat_oop_foundations.md`

## 🆘 Kada da pitaš (Amateur mod)

- Ako jedan test „zaglavi“ > 15 min, napiši:

  - kratak opis očekivanog ponašanja,
  - trenutni kod (3–15 linija),
  - poruku greške iz pytest-a.

## 🎯 Sledeći korak posle A

- Prelaz u **B — Debug & Logging** tek kada su svi testovi iz A zeleni i zapisana refleksija (2–4 rečenice) u `daily_log`.

---

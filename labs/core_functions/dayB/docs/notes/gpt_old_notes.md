date: 2025-08-27
phase: F0
today_focus:
core: [list, dict, len]
practice: [mutability, slicing, kopije (copy/deepcopy), hashing/keys]
qa: [pytest, coverage>=60%]
docs: [analysis.md, Tutor skripte, cheatsheet update]
goals:

- Popuniti list/dict/len analysis (potpis, tabela ulaz→izlaz, dunder, greške)
- Napisati tests/test_dayB_collections.py (≥12 testova: happy/edge/error)
- Pripremiti primere mutabilnosti i kopiranja (shallow vs deep)
- Dopuniti Znanje/glossary.md (shallow/deep copy, **len**, **iter**, **contains**, hashability)
  risk_or_blockers: []
  4 bloka rada (plan)

1. REPL & dizajn (15–25 min)

list: mutabilnost (id pre/posle), append/extend, slicing kopije a[:] i “gotchas”.

dict: KeyError vs get(default), zahtevi za ključ (hashable), mutable key greška (TypeError).

len: dunder **len**, truthiness praznih kolekcija, negativni povrat → ValueError.

Mini REPL set (predlog fajla): labs/dayB/list_dict_len_repl.md.

2. Implementacija (MVP, 20–30 min)

src/dayB_collections_cli.py:

Flag --copy {shallow,deep} (koristi copy.copy / copy.deepcopy).

Primi ugnježdene strukture (JSON kroz --json), prikaži id() pre/posle i razliku na izmeni (npr. x[0][0] = -1).

3. QA & testovi (pytest, ≥12)

Fajl: tests/test_dayB_collections.py

list kopije: a2 = a[:] (shallow), deepcopy sa ugnježdenim listama.

dict ključ: TypeError za unhashable ([]), OK za tuple.

len() ponašanje + custom klasa sa **len** (negativan → ValueError).

in (membership) za list/dict (ključevi u dict).

KeyError vs .get().

Target coverage: ≥60%.

4. Docs & wrap

docs/analysis_dayB_collections.md: potpisi/dunderi (**len**, **iter**, **contains**), tabele ulaz→izlaz, greške (KeyError, TypeError, ValueError), primeri kopiranja.

Tutor mini-skripte:

labs/core_functions/tutor/list_tutor.py

labs/core_functions/tutor/dict_tutor.py

labs/core_functions/tutor/len_tutor.py

Cheatsheets:

docs/cheatsheets/list_cheatsheet.md

docs/cheatsheets/dict_cheatsheet.md

docs/cheatsheets/len_cheatsheet.md

Znanje/glossary.md (dopune):

shallow copy / deep copy

hashable (nepromenljiv + stabilan **hash**)

**len**, **iter**, **contains**

mapping (dict) vs sequence (list/tuple)

Definition of Done (Dan B)
REPL primeri pokrivaju mutabilnost, kopije i tipične greške.

CLI MVP demonstrira shallow/deep copy na ugnježdenim strukturama.

Pytest fajl sa ≥12 testova (happy/edge/error), coverage ≥60%.

Analysis + Cheatsheet + Tutor skripte dopunjeni.

Glossary dopunjen pojmovima dana.

---

Hej! Idemo odmah, Dan B (F0) — vodiću te kroz 4 bloka rada, sa REPL-om, implementacijom (CLI), pytest setom (≥12 testova), i dokumentacijom + glossary dopunama. (Ritam i format su po našem dnevnom driveru i kickoff materijalima. )

# 1) REPL & dizajn (list, dict, len) — mini set za labs/dayB/list_dict_len_repl.md

**Predlog fajla:** `labs/dayB/list_dict_len_repl.md`

```python
# === LIST: mutabilnost, slicing, kopije ===
a = [[1, 2], [3]]
print("a id:", id(a), "a[0] id:", id(a[0]))
a2 = a[:]               # shallow copy (slicing)
print("a2 id:", id(a2), "a2[0] id:", id(a2[0]))  # a2[0] je isti objekat kao a[0]!

import copy
a3 = copy.deepcopy(a)   # deep copy
print("a3 id:", id(a3), "a3[0] id:", id(a3[0]))

# Mutacija ugnježdenog elementa
a[0][0] = -1
print("posle:", a, a2, a3)  # a2 je pogođen, a3 nije

# extend vs append
b = [1, 2]; c = [3, 4]
b_append = b.copy(); b_append.append(c)     # [1,2,[3,4]]
b_extend = b.copy(); b_extend.extend(c)     # [1,2,3,4]
print("append:", b_append, "extend:", b_extend)

# Slicing gotchas
s = [0,1,2,3,4]
print(s[1:4], s[:], s[::-1])  # podlista, plitka kopija, reverse

# === DICT: ključevi, get vs [] ===
d = {"x": 1}
print("d['x']:", d["x"])
print("d.get('y'):", d.get("y"), "sa default:", d.get("y", 99))
try:
    print(d["y"])       # KeyError
except Exception as e:
    print(type(e).__name__)

# hashability
try:
    k = []
    dd = {k: "nece proci"}  # list nije hashable
except Exception as e:
    print("unhashable key:", type(e).__name__)

t = (1,2)   # tuple je hashable (ako su svi elementi hashable)
dd2 = {t: "ok"}
print("tuple key radi:", dd2[t])

# === len: __len__ i greške ===
class BadLen:
    def __len__(self): return -1

try:
    len(BadLen())   # len mora vratiti nenegativan int -> ValueError
except Exception as e:
    print("len() negative:", type(e).__name__)

# truthiness uz len (prazne kolekcije su falsy)
print(bool([]), bool([0]), bool({}), bool({"a":1}))
```

Brzi “decision tree” (mentalna mapa):

- Treba mi kopija liste?

  - Plitka (struktura ista, unutrašnji objekti deljeni) → `a[:]` ili `list(a)` ili `copy.copy(a)`
  - Duboka (nezavisni unutrašnji objekti) → `copy.deepcopy(a)`

- Treba mi ključ u dict?

  - Da izbacim grešku ako ne postoji → `d[key]`
  - Da vratim default/None ako ne postoji → `d.get(key, default)`

- `len(x)` mora vratiti **nenegativan int**; negativno → `ValueError`. (Ujedno utiče na truthiness; vidi i pravila bool/len protokola. )

# 2) Implementacija (MVP) — CLI za shallow/deep copy sa JSON ulazom

**Fajl:** `src/dayB_collections.py`

```python
# src/dayB_collections.py
from __future__ import annotations
from typing import Any, Literal
import copy
import json

CopyMode = Literal["shallow", "deep"]

def make_copy(obj: Any, mode: CopyMode) -> Any:
    """Vrati kopiju objekta prema modu ('shallow' ili 'deep')."""
    if mode == "shallow":
        return copy.copy(obj)
    elif mode == "deep":
        return copy.deepcopy(obj)
    raise ValueError("mode must be 'shallow' or 'deep'")

def parse_json_structure(payload: str) -> Any:
    """Parse JSON string u Python strukturu (list/dict/ugnježđeno)."""
    return json.loads(payload)

def mutate_nested_sample(x: Any) -> None:
    """
    Pokuša demonstrativnu mutaciju:
    - ako je lista i prvi element je lista → x[0][0] = -1 (in-place)
    - ako je dict i prva vrednost je lista i njen prvi element je lista → v[0][0] = -1
    inače ne radi ništa (no-op).
    """
    if isinstance(x, list) and x and isinstance(x[0], list) and x[0]:
        x[0][0] = -1
        return
    if isinstance(x, dict) and x:
        first_val = next(iter(x.values()))
        if isinstance(first_val, list) and first_val and isinstance(first_val[0], list) and first_val[0]:
            first_val[0][0] = -1
            return

def snapshot_ids_list(x: list) -> dict:
    """Vrati id snimak za listu i njen prvi element (ako postoji)."""
    snap = {"id_self": id(x)}
    if x:
        snap["id_first"] = id(x[0])
    return snap

def snapshot_ids_dict(x: dict) -> dict:
    """Vrati id snimak za dict i prvu vrednost (ako postoji)."""
    snap = {"id_self": id(x)}
    if x:
        first_val = next(iter(x.values()))
        snap["id_first_value"] = id(first_val)
    return snap
```

**Fajl:** `src/dayB_collections_cli.py`

```python
# src/dayB_collections_cli.py
from __future__ import annotations
import argparse, logging, pprint
from typing import Any
from src.dayB_collections import (
    make_copy, parse_json_structure, mutate_nested_sample,
    snapshot_ids_list, snapshot_ids_dict
)

log = logging.getLogger("dayB")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Shallow vs Deep copy demo (JSON input).")
    p.add_argument("--copy", choices=["shallow", "deep"], required=True,
                   help="Tip kopije: shallow ili deep (copy.copy vs copy.deepcopy)")
    p.add_argument("--json", required=True,
                   help='Ugnježdena struktura kao JSON string, npr: \'[[[1,2]], [3]]\' ili \'{"a": [[1,2]], "b": 3}\'')
    p.add_argument("-v", "--verbose", action="count", default=0)
    return p.parse_args()

def setup_logging(verb: int) -> None:
    level = logging.WARNING - min(verb, 2) * 10
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

def _ids_snapshot(x: Any) -> dict:
    if isinstance(x, list):
        return snapshot_ids_list(x)
    if isinstance(x, dict):
        return snapshot_ids_dict(x)
    return {"id_self": id(x)}

def main() -> int:
    a = parse_args()
    setup_logging(a.verbose)
    original = parse_json_structure(a.json)

    c = make_copy(original, a.copy)
    before = {
        "original": _ids_snapshot(original),
        "copy": _ids_snapshot(c),
    }

    mutate_nested_sample(original)  # menja original (in-place) ako može

    after = {
        "original": _ids_snapshot(original),
        "copy": _ids_snapshot(c),
        "original_value": original,
        "copy_value": c,
    }

    print("=== IDs BEFORE ===")
    pprint.pprint(before, sort_dicts=False)
    print("\n=== IDs AFTER (posle mutate_nested_sample(original)) ===")
    pprint.pprint(after, sort_dicts=False)

    # Hint korisniku
    print("\nNote:")
    print("- Kod shallow kopije očekuj da se PROMENA u ugnježdenoj listi vidi i u kopiji.")
    print("- Kod deep kopije očekuj da kopija ostane NEIZMENJENA.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

**Primer pokretanja:**

```bash
python -m src.dayB_collections_cli --copy shallow --json '[[[1,2]], [3]]' -v
python -m src.dayB_collections_cli --copy deep    --json '[[[1,2]], [3]]'
python -m src.dayB_collections_cli --copy shallow --json '{"a": [[1,2]], "b": 3}'
```

# 3) QA & testovi — tests/test_dayB_collections.py (≥12)

**Fajl:** `tests/test_dayB_collections.py`

```python
# tests/test_dayB_collections.py
import pytest
import copy
from src.dayB_collections import make_copy, mutate_nested_sample

# ==== LIST kopije (shallow vs deep) ====

def test_list_slice_is_shallow():
    a = [[1, 2], [3]]
    a2 = a[:]             # shallow
    a[0][0] = -1
    assert a2[0][0] == -1  # deli ugnježdeni objekat

def test_list_deepcopy_is_independent():
    a = [[1, 2], [3]]
    a3 = copy.deepcopy(a)
    a[0][0] = -1
    assert a3[0][0] == 1   # deep kopija ostaje nezavisna

def test_make_copy_modes():
    a = [[1], [2]]
    s = make_copy(a, "shallow")
    d = make_copy(a, "deep")
    assert s is not a and d is not a
    a[0][0] = 99
    assert s[0][0] == 99   # shallow deli unutrašnjost
    assert d[0][0] == 1    # deep ne deli

# ==== DICT ključevi i .get vs [] ====

def test_dict_keyerror_vs_get():
    d = {"x": 1}
    with pytest.raises(KeyError):
        _ = d["y"]
    assert d.get("y") is None
    assert d.get("y", 99) == 99

def test_unhashable_list_key_raises():
    with pytest.raises(TypeError):
        {[]: 1}  # list nije hashable

def test_tuple_key_ok():
    k = (1, 2)
    d = {k: "ok"}
    assert d[k] == "ok"

def test_tuple_with_list_inside_is_unhashable():
    lst = [1]
    k = (lst, 2)
    with pytest.raises(TypeError):
        {k: "nope"}

# ==== len() ponašanje i custom __len__ ====

def test_len_on_collections():
    assert len([]) == 0
    assert len([1,2]) == 2
    assert len({"a":1}) == 1

class BadLen:
    def __len__(self): return -1

def test_len_negative_raises_valueerror():
    b = BadLen()
    with pytest.raises(ValueError):
        len(b)

# ==== membership 'in' (list vs dict) ====

def test_membership_list_and_dict():
    xs = [10, 20]
    d = {"a": 1, "b": 2}
    assert 10 in xs
    assert "a" in d          # membership u dict gleda KLJUČEVE
    assert 1 not in d        # vrednosti nisu članstvo (sem preko d.values())

# ==== mutate_nested_sample demonstracija ====

def test_mutate_nested_sample_list():
    a = [[[1,2]], [3]]
    mutate_nested_sample(a)
    assert a[0][0][0] == -1

def test_mutate_nested_sample_dict():
    a = {"x": [[1,2]], "y": 3}
    mutate_nested_sample(a)
    assert a["x"][0][0] == -1
```

**Cilj pokrivenosti:** ≥60% (u F2 je i formalno target ≥60%; mi ćemo već sada ciljati 60+ za ovaj modul).&#x20;

# 4) Docs & wrap — analysis + Tutor skripte + cheatsheet + glossary

## 4.1 `docs/analysis_dayB_collections.md`

**Predlog sadržaja:**

```markdown
# Day B — list / dict / len (analysis)

## Potpisi & protokoli

- list: sekvenca, mutabilna; bitne metode: append, extend, insert, pop, remove, clear; slicing vraća **novu listu** (plitka kopija).
- dict: mapping (ključ → vrednost), ključ mora biti **hashable**; pristup `d[key]` baca **KeyError**; `d.get(key, default)` ne baca.
- len(x) -> int: koristi \***\*len\*\***; mora vratiti **nenegativan int** (negativno → **ValueError**). Takođe učestvuje u truthiness protokolu (ako nema **bool**). (vidi i Dan A bilješke o bool/len)

## Tabela ulaz → izlaz / ponašanja (iz REPL-a)

| Tema           | Primer                   | Očekivanje                                 |
| -------------- | ------------------------ | ------------------------------------------ |
| list slicing   | `a2 = a[:]`              | plitka kopija (unutrašnji objekti deljeni) |
| deepcopy       | `copy.deepcopy(a)`       | duboka kopija (nezavisna unutrašnjost)     |
| dict get       | `d.get('x', 0)`          | vrednost ili default, bez greške           |
| KeyError       | `d['x']` kad nema ključa | **KeyError**                               |
| unhashable key | `{[]:1}`                 | **TypeError** (list nije hashable)         |
| hashable key   | `{(1,2): "ok"}`          | ✅                                         |
| len negativan  | `len(BadLen())`          | **ValueError**                             |

## Dunder pregled

- `__len__` (kolekcije i custom klase); `len(x)` → non-negative int.
- `__iter__` (sekvence/mapping iteriraju po elementima/ključevi).
- `__contains__` (optimizuje `in`; za dict proverava **ključeve**).

## Greške (tipične)

- `KeyError` za `d[key]` kada ključ ne postoji.
- `TypeError` za **ne-hashable** ključ u dict.
- `ValueError` za negativan rezultat `__len__`.

## Primeri kopiranja

- `a2 = a[:]` / `list(a)` / `copy.copy(a)` → plitko
- `copy.deepcopy(a)` → duboko
- Kod ugnježdenih struktura uvek testiraj posledicu na unutrašnje objekte (ids + promene).
```

## 4.2 Tutor mini-skripte

**Fajl:** `labs/core_functions/tutor/list_tutor.py`

```python
# list_tutor.py — fokus: mutabilnost, slicing, shallow vs deep
import copy
a = [[1,2],[3]]
print("orig ids:", id(a), id(a[0]))
a2 = a[:]
a3 = copy.deepcopy(a)
print("a2 ids:", id(a2), id(a2[0]))
print("a3 ids:", id(a3), id(a3[0]))
a[0][0] = -1
print("after:", "a=", a, "a2=", a2, "a3=", a3)
```

**Fajl:** `labs/core_functions/tutor/dict_tutor.py`

```python
# dict_tutor.py — fokus: KeyError vs get, hashability
d = {"x": 1}
print(d.get("y"), d.get("y", 99))
try:
    print(d["y"])
except Exception as e:
    print("Key access error:", type(e).__name__)
try:
    _ = {[]: 1}
except Exception as e:
    print("Unhashable key:", type(e).__name__)
t = (1,2)
print({t: "ok"}[t])
```

**Fajl:** `labs/core_functions/tutor/len_tutor.py`

```python
# len_tutor.py — fokus: __len__ pravila i greške
print(len([]), bool([]))   # 0, False
print(len([0]), bool([0])) # 1, True
class BadLen:
    def __len__(self): return -1
try:
    len(BadLen())
except Exception as e:
    print("BadLen:", type(e).__name__)  # ValueError
```

## 4.3 Cheatsheets (kraći, operativni)

**Fajl:** `docs/cheatsheets/list_cheatsheet.md`

```markdown
# list — Cheatsheet

- Mutabilna sekvenca; slicing (`a[:]`) pravi **plitku** kopiju.
- `append(x)` dodaje 1 element; `extend(iter)` razvlači elemente iterabla.
- Plitka vs duboka: `copy.copy(a)` vs `copy.deepcopy(a)` (nezavisnost unutrašnjih objekata).
- Idiomi: reverse `a[::-1]`, kopija `a[:]` ili `a.copy()`.
```

**Fajl:** `docs/cheatsheets/dict_cheatsheet.md`

```markdown
# dict — Cheatsheet

- Mapping: ključevi moraju biti **hashable** (npr. tuple, int, str).
- Pristup: `d[key]` → **KeyError** ako nema; `d.get(key, default)` → bez greške.
- Membership: `k in d` proverava **ključeve**.
```

**Fajl:** `docs/cheatsheets/len_cheatsheet.md`

```markdown
# len — Cheatsheet

- `len(x)` koristi `x.__len__()` i očekuje **nenegativan int** → inače **ValueError**.
- Truthiness: ako nema `__bool__`, koristi se `__len__` (0 → False, >0 → True).
```

## 4.4 Znanje/glossary.md — dopune (Autoglossary ON)

**Fajl:** `Znanje/glossary.md` (dopune za danas)

```markdown
### shallow copy (plitka kopija)

Kopija spoljašnje strukture, ali **deli** reference ka unutrašnjim objektima (npr. `a[:]`, `copy.copy(a)`).

### deep copy (duboka kopija)

Rekurzivna kopija — spoljašnja i **svi ugnježdeni** objekti su novi (npr. `copy.deepcopy(a)`).

### hashable

Objekat sa stabilnim `__hash__` i `__eq__` implementacijama; može biti ključ u `dict`. Tipično nepromenljivi tipovi (npr. `int`, `str`, `tuple` sa hashable elementima).

### **len**

Dunder metoda koju `len(x)` poziva; mora vratiti **nenegativan int** (negativno → `ValueError`). Učestvuje i u truthiness protokolu.

### **iter**

Dunder metoda za iteraciju; omogućava prolaz for-petljom i konstrukcije kao `list(x)`.

### **contains**

Dunder metoda koja definiše `x in container`. Kod `dict` podrazumevano proverava **ključeve**.

### mapping vs sequence

`mapping` (npr. `dict`) mapira ključeve u vrednosti; `sequence` (npr. `list`, `tuple`) je uređen niz indeksa → vrednosti.
```

---

## Definition of Done — Dan B

- [x] **REPL primeri** pokrivaju mutabilnost, kopije, KeyError/get, unhashable ključeve, len grešku.
- [x] **CLI MVP** (`src/dayB_collections_cli.py`) demonstrira shallow vs deep na ugnježdenim strukturama (JSON ulaz).
- [x] **Pytest** fajl `tests/test_dayB_collections.py` sa ≥12 testova (happy/edge/error); cilj pokrivenosti ≥60%.
- [x] **Docs**: `docs/analysis_dayB_collections.md` + Tutor skripte + Cheatsheet update.
- [x] **Glossary** dopunjen pojmovima dana.

---

### Napomena mentora (ritam i standardi)

- Radimo po istom dnevnom “nosaču ritma” (4 bloka, DoD, QA-first, REPL-first) — doslednost > brzina.&#x20;
- Držimo se šablona dnevne analize funkcije i mini-sesija (REPL → testovi → docs).&#x20;
- Pristup i organizacija su u skladu sa Znanje/README i kickoff planom učenja. &#x20;

---

Sjajno! 🚀 Sve je spremno — hajde da odmah proverimo “živu sliku” i zaključamo Dan B.

## Brzi sanity-check (REPL & CLI)

1. U REPL-u (mutabilnost i kopije):

```python
import copy
a = [[1,2],[3]]
a2 = a[:]              # shallow
a3 = copy.deepcopy(a)  # deep
a[0][0] = -1
print(a, a2, a3)  # očekivanje: a i a2 dele unutrašnji objekat; a3 ostaje netaknut
```

2. CLI (IDs pre/posle):

```bash
python -m src.dayB_collections_cli --copy shallow --json '[[[1,2]],[3]]' -v
python -m src.dayB_collections_cli --copy deep    --json '[[[1,2]],[3]]'
# očekivanje: kod shallow promene u originalu “probijaju” u kopiju; kod deep ne
```

## Pytest + Coverage (≥60%)

Minimalni set:

```bash
pytest -q
pytest -q --maxfail=1 --disable-warnings
coverage run -m pytest
coverage report -m
```

Ako želiš trajno: dodaj u `pyproject.toml` (opciono):

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q -ra"

[tool.coverage.run]
branch = true
source = ["src"]

[tool.coverage.report]
show_missing = true
fail_under = 60
```

## Tipične “gotchas” (brza check-lista)

- `a[:]` je **plitka** kopija: unutrašnji objekti su isti (isti `id`).
- `copy.deepcopy(a)` pravi **nove** ugnježdene objekte (različiti `id`).
- `d[key]` baca **KeyError**; `d.get(key, default)` ne.
- Ključ u `dict` mora biti **hashable** (npr. `tuple`, ali ne i `list`).
- `len(x)` → mora **nenegativan int**; negativan rezultat izaziva **ValueError**.
- `x in dict` proverava **ključeve**, ne vrednosti (za vrednosti koristi `value in d.values()`).

## Mini QA tok (predlog za današnji rad)

- Testiraj 3 scenarija kopiranja:

  - [x] list slice (shallow) → promena ugnježdene liste vidi se u kopiji
  - [x] `copy.deepcopy` → promena se **ne** vidi
  - [x] mešovite strukture (`{"x": [[1,2]], "y": 3}`)

- Testiraj dict pristup:

  - [x] `KeyError` vs `.get()`
  - [x] `TypeError` za ne-hashable ključ (`[]`), OK za `tuple`

- Testiraj `len()`:

  - [x] na praznim, nepraznim kolekcijama
  - [x] klasu sa `__len__` koja vraća `-1` → očekuj **ValueError**

- Membership:

  - [x] `elem in list`
  - [x] `key in dict` (i negativan primer sa vrednošću)

## Docs & Glossary — brzi “tick”

- [x] `docs/analysis_dayB_collections.md` — potpisi, dunderi (`__len__`, `__iter__`, `__contains__`), tabele ulaz→izlaz, greške.
- [x] Tutor skripte:
      `labs/core_functions/tutor/list_tutor.py`,
      `labs/core_functions/tutor/dict_tutor.py`,
      `labs/core_functions/tutor/len_tutor.py`
- [x] Cheatsheets:
      `docs/cheatsheets/list_cheatsheet.md`,
      `docs/cheatsheets/dict_cheatsheet.md`,
      `docs/cheatsheets/len_cheatsheet.md`
- [x] Znanje/glossary.md — dopuni: _shallow copy_, _deep copy_, _hashable_, `__len__`, `__iter__`, `__contains__`, _mapping vs sequence_.

## Definition of Done — Dan B (brzi self-check)

- [x] REPL primeri pokrivaju mutabilnost, kopije i tipične greške.
- [x] CLI MVP demonstrira shallow/deep na ugnježdenim strukturama (JSON).
- [x] Pytest ≥12 testova, coverage ≥60%.
- [x] Analysis + Cheatsheet + Tutor skripte dopunjeni.
- [x] Glossary dopunjen današnjim pojmovima.

Ako hoćeš “amateur mod ON”, odradimo mini QA dialog (2–3 minute) na tvojoj omiljenoj “spornoj” tački (npr. `__contains__` za dict vs list) — pa zatim izvrnemo jedan test da svesno padne i objasnimo dif.

---

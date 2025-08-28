pytest -c labs/core_functions/pytest.ini
pytest -s -v -c labs/core_functions/pytest.ini

---

# 🧪 Uvod u testove (pytest) — Amateur mod

(Mentor:) Ajde da objasnim **od nule**.
(Junior:) Super, jer pytest mi je još “maglovit”.
(Mentor:) Idemo polako.

---

## 1) Šta je test?

Test je **mini program** koji proverava da li kod radi kako očekuješ.
Primer:

```python
def test_sabiranje():
    assert 2 + 2 == 4
```

- Ako je uslov tačan → test prolazi.
- Ako nije → test pada i dobiješ grešku.

---

## 2) Struktura test fajla

- Fajl mora da se zove `test_*.py` ili `*_test.py`.
- Funkcije moraju da počinju sa `test_`.
- Unutra koristiš **assert**.

---

## 3) Prvi primer

Napravi fajl: `tests/test_math_basics.py`

```python
def test_int_casting():
    assert int(3.9) == 3
    assert int(-3.9) == -3

def test_str_casting():
    assert str(42) == "42"
    assert str(True) == "True"

def test_bool_casting():
    assert bool(0) is False
    assert bool(1) is True
```

Pokreni:

```bash
pytest -q
```

---

## 4) Kada test padne

```python
def test_fail():
    assert int("12.5") == 12
```

Rezultat:

```
E   ValueError: invalid literal for int() with base 10: '12.5'
```

👉 Naučiš da `int("12.5")` NIJE dozvoljeno — to je suština: testovi ti otkrivaju “granice”.

---

## 5) Parametrizacija (više vrednosti odjednom)

```python
import pytest

@pytest.mark.parametrize("x,expected", [
    (0, False),
    (1, True),
    ("", False),
    ("abc", True),
])
def test_bool_truthy(x, expected):
    assert bool(x) is expected
```

---

## 6) Amateur mod filozofija za testove

- **Mentor:** objašnjava zašto test pišeš i šta time dokazuješ.
- **Junior:** pita “a šta ako je ulaz loš?” → dodaš test za grešku (`pytest.raises`).

Primer:

```python
import pytest

def test_int_error():
    with pytest.raises(ValueError):
        int("12.5")
```

---

super — idemo na najjednostavniji setup: **spuštamo .py fajlove iz `src/` u root `dayA/` i `dayB/`**, ažuriramo import-e i root `pytest.ini`. Ovim izbegavamo sudare dva različita `src/` foldera i sve radi iz root-a repo-a.

# 1) Novi raspored (posle pomeranja fajlova)

```
labs/core_functions/
├─ dayA/
│  ├─ dayA_core_types.py
│  ├─ dayA_core_types_cli.py
│  └─ int_str_bool_repl.md
├─ dayB/
│  ├─ dayB_collections.py
│  ├─ dayB_collections_cli.py
│  └─ list_dict_len_repl.md
└─ tests/
   ├─ test_dayA_core_types.py
   └─ test_dayB_collections.py
```

# 2) Git/Bash komande (Windows PowerShell ekvivalente u komentarima)

```bash
# DAY A
git mv labs/core_functions/dayA/src/dayA_core_types.py labs/core_functions/dayA/dayA_core_types.py
git mv labs/core_functions/dayA/src/dayA_core_types_cli.py labs/core_functions/dayA/dayA_core_types_cli.py
git rm -r labs/core_functions/dayA/src 2>/dev/null || true

# DAY B
git mv labs/core_functions/dayB/src/dayB_collections.py labs/core_functions/dayB/dayB_collections.py
git mv labs/core_functions/dayB/src/dayB_collections_cli.py labs/core_functions/dayB/dayB_collections_cli.py
git rm -r labs/core_functions/dayB/src 2>/dev/null || true
```

> PowerShell: `git mv` isto; za brisanje: `Remove-Item -Recurse -Force labs/core_functions/dayA/src, labs/core_functions/dayB/src`

# 3) Importi u testovima (prilagoditi)

**tests/test_dayA_core_types.py**

```python
from dayA.dayA_core_types import to_int, str_display, str_from_bytes, to_bool
```

**tests/test_dayB_collections.py**

```python
from dayB.dayB_collections import (
    make_copy, parse_json_structure, mutate_nested_sample,
    snapshot_ids_list, snapshot_ids_dict
)
```

# 4) Patch za `dayB_collections_cli.py` (importi)

**Putanja:** `labs/core_functions/dayB/dayB_collections_cli.py`

```diff
-from src.dayB_collections import (
+from dayB.dayB_collections import (
     make_copy, parse_json_structure, mutate_nested_sample,
     snapshot_ids_list, snapshot_ids_dict
 )
```

# 5) Root `pytest.ini` (dopunjen)

Tvoj postojeći root `pytest.ini` dopuni da pytest vidi i `labs/core_functions` (tako `dayA/` i `dayB/` postaju paketi), i da traži testove u oba projekta:

```ini
[pytest]
# Pokreći testove iz više modula kad si u root-u repoa
testpaths =
    padd_logger/tests
    labs/core_functions/tests

# Omogući import modula iz oba prostora (više nema 'src' za dayA/dayB)
pythonpath =
    padd_logger/src
    labs/core_functions

# Konzistentno sa lokalnim podešavanjem (tiši izlaz + coverage)
addopts =
    -q -ra --maxfail=1
    --cov=padd_logger/src
    --cov=labs/core_functions
    --cov-branch
    --cov-report=term-missing:skip-covered
    --cov-report=html:.reports/coverage_html

# Ne pretražuj nepotrebne foldere
norecursedirs =
    .git
    .venv
    __pycache__
    legacy

python_files = test_*.py
```

# 6) core_functions/pytest.ini — obrisati?

**Da, obriši.** Držimo **jedan** `pytest.ini` (u root-u). Više `pytest.ini` fajlova ume da zbuni pytest oko `rootdir` i `sys.path`.

```bash
git rm labs/core_functions/pytest.ini
```

# 7) Pokretanje (iz root-a repo-a)

```bash
pytest -v
# ili sa coverage:
pytest -v --cov
```

# 8) Pokretanje CLI-jeva (iz root-a)

```bash
python -m dayA.dayA_core_types_cli --int "0x2A" --base 0 --bool ""
python -m dayB.dayB_collections_cli --copy shallow --json '[[[1,2]],[3]]'
python -m dayB.dayB_collections_cli --copy deep    --json '[[[1,2]],[3]]'
```

To je to — minimalne izmene, maksimalna jasnoća. Ako negde ostane stari import `from src...`, samo ga zameni odgovarajućim `from dayA...` ili `from dayB...` kao iznad.

---

# 🧩 Dan A (nastavak) — `bool()` komplet

## 1) Putanje

- `labs/core_functions/bool/bool_cheatsheet.md`
- `labs/core_functions/bool/bool_analysis_notes.md`
- `labs/core_functions/bool/bool_repl_testing.md`
- `labs/core_functions/bool/bool_tutor_template.py`

---

## 2) `bool_cheatsheet.md`

````markdown
# `bool()` – Cheatsheet (Mentor + Junior)

## Mentalni model

**Mentor:** `bool(x)` vraća `True` ili `False`. Python koristi **truthiness** pravila:

- Falsy: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`, `''`, `[]`, `{}`, `set()`, `range(0)`, `None`, `False`
- Sve ostalo je truthy.

**Junior:** A šta je prioritet: `__bool__` ili `__len__`?
**Mentor:** Prvo `__bool__`. Ako ga nema, koristi `__len__` (0 → False, >0 → True). Ako nema ni jedno ni drugo → default `True`.

## Potpis

```py
bool(x) -> True|False
```
````

## Tipični primeri

```py
bool(0), bool(1)           # False, True
bool(""), bool("0")        # False, True
bool([]), bool([0])        # False, True
bool(None)                 # False
```

## Dunder protokol

```py
class WithBool:  def __bool__(self): return False
class WithLen:   def __len__(self):  return 2
bool(WithBool())  # False  (po __bool__)
bool(WithLen())   # True   (po __len__)
```

## Greške?

`bool()` ne diže greške za standardne tipove; greške vidiš tek ako `__bool__`/`__len__` user-def klasa pogrešno vrati tip (npr. `return 2` → `TypeError`).

## QA saveti

- U `if` granama koristi neposredno `if xs:` umesto `if len(xs) > 0:`.
- Za eksplicitnost u API-ju, prosleđuj već `bool` ili jasno dokumentuj truthiness.

````

---

## 3) `bool_analysis_notes.md`
```markdown
# bool_analysis_notes.md — koraci za analysis

## 0) Potpis i intuicija
- `bool(x) -> True|False`
- Ako `x` ima `__bool__`, koristi to; u suprotnom `__len__`; u suprotnom True.

## 1) REPL mini-tabela
- `0 -> False`, `1 -> True`, `-1 -> True`
- `"" -> False`, `"0" -> True`
- `[] -> False`, `[0] -> True`, `{}` -> False
- `None -> False`, `object() -> True`

## 2) Dunder metode
- Napravi `WithBool` (`__bool__` vraća `False`)
- Napravi `WithLen` (`__len__` vraća `2`)
- Negativni primer: `BadBool.__bool__` vraća `2` → `TypeError`

## 3) Greške/ivice
- User-def `__bool__` mora vratiti `bool` (inače `TypeError`)
- Kolekcije: prazna → False, neprazna → True
- `numpy` skalari imaju svoja pravila; van obima ove lekcije

## 4) Python Tutor mini-skripta
- Ilustruj pozive `bool()` i šta se izvršava (poziv `__bool__` ili `__len__`).

## 5) Zaključci & sa posla
- U API dizajnu: eksplicitno navedi “prazno znači False”.
- Ne poredi sa `== True`/`== False`; koristi if/while idiome.

## 6) Mini test plan
| Ulaz | Očekivani | Napomena |
|------|-----------|----------|
| `0` | `False` | integer falsy |
| `""` | `False` | prazan string |
| `[0]` | `True` | neprazna lista |
| `None` | `False` | None je falsy |
| `WithBool()` | `False` | `__bool__` |
| `WithLen()` | `True` | `__len__` fallback |
| `BadBool()` | `TypeError` | loš povratni tip |
````

---

## 4) `bool_repl_testing.md`

````markdown
# REPL plan za `bool()`

```python
help(bool)
print(bool.__doc__)

print(bool(0), bool(1), bool(-1))           # False True True
print(bool(""), bool("0"))                  # False True
print(bool([]), bool([0]))                  # False True
print(bool({}), bool({"k": 1}))             # False True
print(bool(None), bool(object()))           # False True

class WithBool:
    def __bool__(self): return False
class WithLen:
    def __len__(self): return 2
print(bool(WithBool()))  # False
print(bool(WithLen()))   # True

class BadBool:
    def __bool__(self): return 2
try:
    print(bool(BadBool()))
except Exception as e:
    print(type(e).__name__)  # TypeError
```
````

````

---

## 5) `bool_tutor_template.py`
```python
print("1) Osnovni tipovi → truthy/falsy")
print(bool(0), bool(1), bool(-1))
print(bool(""), bool("0"))
print(bool([]), bool([0]))
print(bool(None), bool(object()))

print("\n2) Dunder prioritet: __bool__ ispred __len__")
class WithBool:
    def __bool__(self): return False

class WithLen:
    def __len__(self): return 2

print(bool(WithBool()))  # False (po __bool__)
print(bool(WithLen()))   # True  (po __len__)

print("\n3) Pogrešan povratni tip u __bool__")
class BadBool:
    def __bool__(self): return 2  # greška

try:
    print(bool(BadBool()))
except Exception as e:
    print(type(e).__name__)  # TypeError

print("\n4) Idiomi u uslovima")
xs = []
if xs:   # idiomatski
    print("ima elemenata")
else:
    print("prazno je -> False")
````

---

## 🎯 DoD (Dan A — bool)

- [ ] REPL isečci isprobani (happy + edge + “pogrešan **bool**”).
- [ ] 3–5 pytest testova dodato u `tests/test_dayA_core_types.py` (truthy/falsy + dunder prioritet + TypeError na `BadBool`).
- [ ] `Znanje/glossary.md` dopunjeno: **truthy/falsy**, **`__bool__`**, **`__len__`**.

Ako želiš, mogu odmah da spojim sve `bool` fajlove u ZIP ili da generišem pytest blok za `BadBool`/`WithBool`/`WithLen`.

---

Top! Kreiram komplet “Dan A” paket po istom šablonu kao za Dan B — sa istim 4-blok ritmom: REPL & dizajn → Implementacija (CLI + lib) → QA & testovi → Docs & wrap (Tutor skripte, cheatsheet, glossary). Kao osnovu koristim tvoj postojeći materijal (analysis, REPL isečci, mini CLI) i dopunjujem gde treba. Osnovne reference iz priloga: analiza (), mini CLI (), REPL skripta ().

---

# 1) REPL & dizajn

**Fajl:** `labs/dayA/int_str_bool_repl.md`
_(preuzeto i prilagođeno iz tvog priloga; uključuje help(), dunder putanje, happy/edge/error; pokazuje tipove grešaka)_&#x20;

```python
# ===== int() =====
help(int); print(int.__doc__)
print(int(42.9), int(-3.9))                 # 42, -3  (trunc prema nuli)
print(int("1010", 2), int("FF", 16))        # 10, 255
print(int("  42\n"))                        # 42  (whitespace OK)
print(int("0b101", 0))                      # 5   (base=0 auto-detekcija prefiksa)
print(int(b"2a", 16))                       # 42  (bytes kao ASCII cifre)
try: int("12.5")
except Exception as e: print(type(e).__name__)  # ValueError
try: int(3.0, 10)
except Exception as e: print(type(e).__name__)  # TypeError
try: int(float("inf"))
except Exception as e: print(type(e).__name__)  # OverflowError

# Dunder: __int__ i fallback na __index__
class WithInt:    def __int__(self): return 42
class OnlyIndex:  def __index__(self): return 7
print(int(WithInt()), int(OnlyIndex()))     # 42, 7

# ===== str() =====
help(str); print(str.__doc__)
b = b"abc"
print(str(b))                      # "b'abc'" (repr bytes-a)
print(b.decode())                  # 'abc'    (stvarni tekst)
class NoStr: pass
class WithStr:
    def __str__(self): return "WithStr::pretty"
print(str(NoStr()))                # <__main__.NoStr object at 0x...> (fallback na repr)
print(str(WithStr()))              # 'WithStr::pretty'
try: str(123, "utf-8")
except Exception as e: print(type(e).__name__)  # TypeError

# ===== bool() =====
help(bool); print(bool.__doc__)
print(bool(0), bool(1), bool(-1))          # False True True
print(bool(""), bool("0"))                 # False True
print(bool([]), bool([0]))                 # False True
print(bool(None), bool(object()))          # False True
class WithBool:  def __bool__(self): return False
class WithLen:   def __len__(self):  return 2
print(bool(WithBool()), bool(WithLen()))   # False, True
class BadBool:   def __bool__(self): return 2
try: bool(BadBool())
except Exception as e: print(type(e).__name__)  # TypeError
```

Mini decision-tree:

- `int(x, base)` koristi se samo kada je `x` tekst/bytes; za numerike ide `int(x)` (trunc prema nuli).
- `str(object)` je čitljiv prikaz; za **bytes → tekst** koristi se `.decode(encoding)`.
- `bool(x)` → `__bool__` → `__len__` → default `True` (osim “praznih”/0/None).

---

# 2) Implementacija (MVP)

## 2.1 Biblioteka (lagani “core” za ponovnu upotrebu)

**Fajl:** `src/dayA_core_types.py`

```python
# src/dayA_core_types.py
from __future__ import annotations
from typing import Any, Optional, Union

def to_int(x: Any, base: Optional[int] = None) -> int:
    """
    Konverzija u int.
    - Ako je x str/bytes i base je zadat -> koristi int(x, base)
    - Ako je x str/bytes i base nije zadat -> int(x)
    - Inače -> int(x) (trunc prema nuli za float)
    Greške: ValueError (loš literal), TypeError (nevalidna kombinacija), OverflowError (npr. inf)
    """
    if base is not None:
        return int(x, base)  # TypeError ako x nije tekst/bytes; to želimo da ispliva
    return int(x)

def str_from_bytes(b: Union[bytes, bytearray], encoding: str = "utf-8", errors: str = "strict") -> str:
    """Decode bytes/bytearray u tekst (podrazumevano UTF-8)."""
    return bytes(b).decode(encoding, errors)

def str_display(obj: Any) -> str:
    """Čitljiv prikaz objekta; ako klasa ima __str__, koristi se; inače repr fallback."""
    return str(obj)

def to_bool(x: Any) -> bool:
    """Truthiness: koristi __bool__ -> __len__ -> default True."""
    return bool(x)
```

## 2.2 CLI (pokazuje razlike u praksi)

**Fajl:** `src/dayA_core_types_cli.py`
_(tvoj postojeći mini-CLI, uvršten pod canonical putanju; ostavljam semantiku netaknutu)_&#x20;

```python
#!/usr/bin/env python3
"""
Mini CLI: demonstrira core konverzije int/str/bool za zadate ulaze.

Usage:
  python -m src.dayA_core_types_cli --int "0x2A" --base 0 --str-bytes "6869" --str-encoding hex --bool ""
"""

from __future__ import annotations

import argparse
import binascii
import logging

log = logging.getLogger("dayA")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--int", dest="int_val", help="vrednost za int()", default=None)
    p.add_argument(
        "--base", type=int, default=10, help="osnova za int() (2..36 ili 0 auto)"
    )
    p.add_argument(
        "--str-bytes",
        dest="str_bytes",
        help="heks string npr. '6869' (hi)",
        default=None,
    )
    p.add_argument(
        "--str-encoding", dest="str_enc", choices=["utf-8", "hex"], default="utf-8"
    )
    p.add_argument(
        "--bool",
        dest="bool_val",
        help="vrednost za bool() (string se tretira po truthiness)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    return p.parse_args()


def setup_logging(verb: int) -> None:
    level = logging.WARNING - min(verb, 2) * 10
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def demo_int(s: str, base: int) -> int:
    if s is None:
        return 0
    return int(s, base)  # može ValueError/TypeError; to je OK, CLI će prikazati


def demo_str_from_bytes(payload: str | None, mode: str) -> str | None:
    if not payload:
        return None
    if mode == "hex":
        b = binascii.unhexlify(payload)  # "6869" -> b"hi"
        return b.decode("utf-8")  # dekodiraj
    else:
        return str(payload)  # običan str()


def demo_bool(x: str | None) -> bool:
    return bool(x)


def main() -> int:
    a = parse_args()
    setup_logging(a.verbose)
    try:
        iv = demo_int(a.int_val, a.base)
        log.info("int(%r, base=%s) = %r", a.int_val, a.base, iv)
    except Exception as e:
        log.error("int() failure: %s: %s", type(e).__name__, e)

    sv = demo_str_from_bytes(a.str_bytes, a.str_enc)
    log.info("str-from-bytes(%r, %s) -> %r", a.str_bytes, a.str_enc, sv)

    bv = demo_bool(a.bool_val)
    log.info("bool(%r) -> %r", a.bool_val, bv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

# 3) QA & testovi (pytest, ≥9)

**Fajl:** `tests/test_dayA_core_types.py`
_(happy/edge/error, dunder fallback, TypeError/ValueError/OverflowError; target coverage ≥60% za `src/`)_

```python
# tests/test_dayA_core_types.py
import pytest
from src.dayA_core_types import to_int, str_from_bytes, str_display, to_bool

# ==== int(): happy ====

def test_int_truncation_from_float():
    assert to_int(42.9) == 42
    assert to_int(-3.9) == -3

def test_int_with_base_and_auto_prefix():
    assert to_int("1010", base=2) == 10
    assert to_int("0b101", base=0) == 5
    assert to_int(b"2a", base=16) == 42

# ==== int(): errors ====

def test_int_valueerror_bad_literal():
    with pytest.raises(ValueError):
        to_int("12.5")  # nije ceo broj

def test_int_typeerror_base_on_non_text():
    with pytest.raises(TypeError):
        to_int(3.0, base=10)  # base samo za string/bytes

def test_int_overflowerror_inf():
    import math
    with pytest.raises(OverflowError):
        to_int(float("inf"))

# ==== dunder __int__ / __index__ fallback ====

class WithInt:
    def __int__(self): return 42

class OnlyIndex:
    def __index__(self): return 7

def test_dunder_int_and_index():
    assert to_int(WithInt()) == 42
    assert to_int(OnlyIndex()) == 7

# ==== str(): bytes decode i str-display ====

def test_str_from_bytes_utf8_and_hex():
    assert str_from_bytes(b"hi") == "hi"
    # "6869" je "hi" u hex-u:
    assert bytes.fromhex("6869").decode("utf-8") == "hi"

def test_str_display_str_vs_repr():
    class WithStr:  # ima __str__
        def __str__(self): return "pretty"
    class NoStr:   # nema __str__ -> repr fallback
        pass
    assert str_display(WithStr()) == "pretty"
    assert "object at 0x" in str_display(NoStr())

def test_str_encoding_typeerror_like_builtin():
    # builtin str() sa encoding parametrom radi samo za bytes; mi ga ne podržavamo u str_display
    with pytest.raises(TypeError):
        str(123, "utf-8")  # mirrorujemo ponašanje builtina

# ==== bool(): truthiness + dunder lanci ====

def test_bool_truthiness_basics():
    assert to_bool(0) is False
    assert to_bool(1) is True
    assert to_bool("") is False
    assert to_bool("0") is True
    assert to_bool([]) is False
    assert to_bool([0]) is True
    assert to_bool(None) is False

def test_bool_dunders_and_error():
    class WithBool:
        def __bool__(self): return False
    class WithLen:
        def __len__(self): return 2
    assert to_bool(WithBool()) is False
    assert to_bool(WithLen()) is True

    class BadBool:
        def __bool__(self): return 2
    with pytest.raises(TypeError):
        bool(BadBool())
```

> Pokretanje:

```bash
pytest -q
coverage run -m pytest && coverage report -m
```

---

# 4) Docs & wrap

## 4.1 Analiza

**Fajl:** `docs/analysis_dayA_core_types.md`
_(uvedeno iz priloga i dopunjeno tabelama i dunder-napomenama)_&#x20;

```markdown
# Dan A — int / str / bool (analysis)

## int()

**Potpis:** `int(x=0) -> int` · `int(x: str|bytes|bytearray, base=10) -> int`
**Intuicija:** konverzija u ceo broj; float → trunc prema nuli; tekst/bytes → parsiranje cifara uz `base` (0..36 ili 0 za auto).

### Mini tabela (ulaz → izlaz)

| Ulaz           | Izlaz / Greška  | Napomena                           |
| -------------- | --------------- | ---------------------------------- |
| `42.9`         | `42`            | trunc prema 0                      |
| `-3.9`         | `-3`            | trunc                              |
| `"1010", 2`    | `10`            | baza 2                             |
| `"FF", 16`     | `255`           | heks                               |
| `"0b101", 0`   | `5`             | auto prefiks                       |
| `"  42\n"`     | `42`            | whitespace ok                      |
| `b"2a", 16`    | `42`            | bytes kao ASCII cifre              |
| `"12.5"`       | `ValueError`    | loš literal                        |
| `3.0, base=10` | `TypeError`     | base dozvoljen samo za tekst/bytes |
| `float("inf")` | `OverflowError` | spec vrednosti                     |

**Dunder:** `__int__` primaran; `__index__` kao celobrojni fallback.

---

## str()

**Potpis:** `str(object='') -> str` · (za bytes: koristi `.decode()` za tekst)
**Intuicija:** čitljiv prikaz objekta; za bytes `str(b)` daje repr (`"b'...'"`), a ne tekst.

### Mini tabela

| Ulaz                | Izlaz / Greška | Napomena               |
| ------------------- | -------------- | ---------------------- |
| `42`                | `"42"`         | broj → tekst           |
| `True`              | `"True"`       | bool                   |
| `None`              | `"None"`       | None                   |
| `[1,"a"]`           | `"[1, 'a']"`   | kolekcije              |
| `b"abc"`            | `"b'abc'"`     | repr bytes-a           |
| `(b"abc").decode()` | `'abc'`        | pravi tekst            |
| `str(123, "utf-8")` | `TypeError`    | encoding samo za bytes |

**Dunder:** `__str__` → fallback na `__repr__` (ako `__str__` ne postoji).

---

## bool()

**Potpis:** `bool(x) -> True|False`
**Intuicija:** truthiness: prazno (`''`, `[]`, `{}`, `0`, `None`) je **falsy**; ostalo je **truthy**.

### Mini tabela

| Ulaz       | Izlaz | Napomena               |
| ---------- | ----- | ---------------------- |
| `0`        | False | int falsy              |
| `1`        | True  | int truthy             |
| `""`       | False | prazan string          |
| `"0"`      | True  | ne-prazan string       |
| `[]`       | False | prazna kolekcija       |
| `[0]`      | True  | ne-prazna kolekcija    |
| `None`     | False | posebna falsy vrednost |
| `object()` | True  | default objekat        |

**Dunder lanac:** `__bool__` → `__len__` → default True; loš povratni tip iz `__bool__` → `TypeError`.
```

## 4.2 Tutor mini-skripte (Python Tutor-friendly)

**Fajl:** `labs/core_functions/tutor/int_tutor.py`

```python
# int_tutor.py — trunc, base, bytes, __int__/__index__
print(int(42.9), int(-3.9))        # 42 -3
print(int("0b101", 0))             # 5 (auto baza)
print(int(b"2a", 16))              # 42
class WithInt:    def __int__(self): return 42
class OnlyIndex:  def __index__(self): return 7
print(int(WithInt()), int(OnlyIndex()))  # 42 7
for bad in ["12.5", (3.0, 10), float("inf")]:
    try:
        if bad == (3.0,10): int(*bad)
        else: int(bad)
    except Exception as e:
        print(type(e).__name__)
```

**Fajl:** `labs/core_functions/tutor/str_tutor.py`

```python
# str_tutor.py — str vs repr, decode, __str__ fallback
b = b"abc"
print(str(b))          # "b'abc'" (repr, ne tekst)
print(b.decode())      # 'abc' (tekst)
class NoStr: pass
class WithStr:
    def __str__(self): return "WithStr::pretty"
print(str(NoStr()))    # repr fallback
print(str(WithStr()))  # WithStr::pretty
try:
    print(str(123, "utf-8"))
except Exception as e:
    print(type(e).__name__)  # TypeError
```

**Fajl:** `labs/core_functions/tutor/bool_tutor.py`

```python
# bool_tutor.py — truthiness, __bool__ / __len__ i greška
print(bool(0), bool(1), bool(""), bool("0"), bool([]), bool([0]), bool(None))
class WithBool:  def __bool__(self): return False
class WithLen:   def __len__(self):  return 2
print(bool(WithBool()), bool(WithLen()))  # False True
class BadBool:   def __bool__(self): return 2
try: bool(BadBool())
except Exception as e: print(type(e).__name__)  # TypeError
```

## 4.3 Cheatsheets

**Fajl:** `docs/cheatsheets/int_cheatsheet.md`

```markdown
# int — Cheatsheet

- `int(x)` trunc prema nuli; `int("0b101", 0)` auto prepoznaje prefiks.
- `int(text|bytes, base)` za baze 2..36 ili `0` za auto.
- Greške: `ValueError` (loš literal), `TypeError` (nevalidan base), `OverflowError` (npr. inf).
- Dunder: `__int__` → fallback `__index__` (celobrojni).
```

**Fajl:** `docs/cheatsheets/str_cheatsheet.md`

```markdown
# str — Cheatsheet

- `str(x)` → korisnički prikaz (`__str__` ili `__repr__` fallback).
- `str(b"bytes")` daje `"b'...'"` (repr); **pravi tekst** dobij `bytes.decode(encoding)`.
- `str(obj, encoding)` je `TypeError` (osim specijala za bytes u C API; idiom je `.decode()`).
- Kada ti treba kontrola formata: `format()`, f-string specifikatori.
```

**Fajl:** `docs/cheatsheets/bool_cheatsheet.md`

```markdown
# bool — Cheatsheet

- Truthiness: prazno/0/None → False; ostalo → True.
- Dunder lanac: `__bool__` → `__len__` → default True.
- Ako `__bool__` ne vrati `bool` → `TypeError`.
```

## 4.4 Glossary dopune (Znanje/glossary.md)

**Fajl:** `Znanje/glossary.md` _(dopune za Dan A)_

```markdown
### trunc (truncation prema nuli)

Ponašanje `int(float)` koje odbacuje decimalni deo ka nuli (42.9→42, -3.9→-3).

### base=0 (auto-detekcija)

Poseban režim `int(text, 0)` koji detektuje prefikse `0b`, `0o`, `0x`.

### **int** / **index**

Dunder metode za celobrojnu konverziju; `int(x)` koristi `__int__`, a ako ne postoji, može da padne na `__index__` (samo celobrojne vrednosti).

### **str** / **repr**

`str(x)` preferira `__str__`, u suprotnom koristi `__repr__` kao fallback; `repr` je za debug.

### decode vs str(bytes)

`bytes.decode(encoding)` vraća tekst (npr. UTF-8), dok `str(bytes)` daje repr `"b'...'"`.

### truthy / falsy

Vrednosti koje se u uslovima tretiraju kao True/False. Prazne kolekcije, `0`, `None` su falsy; ostalo uglavnom truthy.

### **bool** i **len** u truthiness-u

`bool(x)` poziva `x.__bool__()`, zatim `x.__len__()` ako `__bool__` ne postoji; pogrešan tip iz `__bool__` → `TypeError`.
```

---

## Definition of Done — Dan A

- [x] **REPL** isečci (`labs/dayA/int_str_bool_repl.md`) pokrivaju happy/edge/error i dunder lanci.&#x20;
- [x] **CLI MVP** (`src/dayA_core_types_cli.py`) postoji i radi primere konverzija.&#x20;
- [x] **Lib** (`src/dayA_core_types.py`) enkapsulira `to_int/str_from_bytes/str_display/to_bool`.
- [x] **Pytest** (`tests/test_dayA_core_types.py`) ≥9 testova; cilj pokrivenosti ≥60%.
- [x] **Docs**: `docs/analysis_dayA_core_types.md` popunjen (potpis, tabele, dunderi, greške).&#x20;
- [x] **Tutor** skripte (3 fajla) + **Cheatsheets** (3 fajla) + **Glossary** dopune.

---

Ako želiš, mogu odmah odraditi “amateur mod ON” mini QA (Mentor↔Junior) baš za `__int__` vs `__index__` ili “str vs decode” — ti biraj temu, pa bacamo 2–3 brza REPL primera i 1 namerno-failing test da učvrstimo razliku.

---

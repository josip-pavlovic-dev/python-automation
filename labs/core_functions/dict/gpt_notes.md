top! krećemo sa **dict** baš kao što smo uradili za list 👇
(+ objašnjenje zašto ti Ruff “briše” `import pytest`)

---

## 0) Zašto Ruff briše `import pytest`?

- Ruff javlja **F401: imported but unused** → u tvom testu `test_grid_gotcha` **ne koristiš** `pytest` (nema `pytest.raises` itd.), pa predlaže da obrišeš `import pytest`.
- U testovima gde **koristiš** `pytest.raises(...)`, `import pytest` je potreban i Ruff neće prigovarati.
- Ako ipak želiš da zadržiš import (npr. zbog šablona), dodaj komentare:

  - u tom fajlu: `import pytest  # noqa: F401`
  - ili u **.ruff.toml** (preporuka samo ako želiš šire pravilo):

    ```toml
    [tool.ruff.per-file-ignores]
    "labs/core_functions/tests/*" = ["F401"]  # dozvoli neiskorišćen import u testovima
    ```

> Ukratko: test bez `pytest.raises` → ukloni `import pytest`. Test sa `raises` → ostavi import.

---

# 1) Uvod u `dict` (od nule)

- **mapiranje**: ključ → vrednost
- **neuređen** do Pythona 3.6 (implementacija), **stabilan redosled umetanja** od 3.7+.
- **ključ mora biti hashable** (nepromenljiv i sa stabilnim `__hash__`).
- Literali: `{}` ili `{key: value, ...}`.

REPL osnovno:

```python
d = {"a": 1, "b": 2}
print(d["a"])          # 1
d["c"] = 3             # dodaj
d["a"] = 10            # izmena
print(d)               # {'a': 10, 'b': 2, 'c': 3}
print(len(d))          # 3
print("a" in d)        # True  (članstvo gleda KLJUČEVE)
print(1 in d)          # False (vrednosti nisu članstvo; koristi 1 in d.values())
```

---

# 2) Cheatsheet (kratak, praktičan)

**Kreiranje**

```python
d = {}                             # prazan
d = dict([("a",1),("b",2)])        # iz parova
d = dict(a=1, b=2)                 # imenovani args
```

**Čitanje bez greške**

```python
d.get("x")         # None
d.get("x", 99)     # 99 (default)
```

**Umetanje / update**

```python
d["x"] = 1
d.update({"y": 2})         # spoji
d.setdefault("z", [])      # ako nema 'z' -> postavi [] i vrati ga
```

**Brisanje**

```python
del d["x"]                 # KeyError ako ne postoji
d.pop("y")                 # vrati vrednost i ukloni, KeyError ako ne postoji
d.pop("y", None)           # bez greške; vrati None ako nema
```

**Pogledi (views)**

```python
d.keys(), d.values(), d.items()
for k, v in d.items(): ...
```

**Kopije**

```python
sh = d.copy()              # plitka
import copy
dp = copy.deepcopy(d)      # duboka
```

**Hashability**

```python
{(1,2): "ok"}              # tuple je hashable
{[]: "nope"}               # TypeError (list nije hashable)
{( [1], 2 ): "nope"}       # TypeError (tuple sadrži listu)
```

---

# 3) REPL plan (10 kratkih koraka)

Sačuvaj kao `labs/core_functions/dict_repl_plan.md` (copy/paste blokovi).

````markdown
# REPL: dict (10 koraka)

## 1) Osnove i pristup

```python
d = {"a":1, "b":2}
print(d["a"])      # 1
d["c"] = 3
print(d)           # {'a':1,'b':2,'c':3}
```
````

## 2) get vs \[]

```python
d = {"x": 1}
try:
    d["y"]
except Exception as e:
    print(type(e).__name__)    # KeyError
print(d.get("y"))              # None
print(d.get("y", 99))          # 99
```

## 3) Članstvo

```python
d = {"a":1, "b":2}
print("a" in d)     # True  (ključevi)
print(1 in d)       # False (vrednosti nisu članstvo)
print(1 in d.values())  # True
```

## 4) Umetanje i update

```python
d = {"a":1}
d["b"] = 2
d.update({"c":3})
print(d)            # {'a':1,'b':2,'c':3}
```

## 5) setdefault

```python
d = {}
lst = d.setdefault("items", [])
lst.append("x")
print(d)            # {'items':['x']}
```

## 6) Brisanje

```python
d = {"a":1,"b":2}
v = d.pop("a")
print(v, d)         # 1 {'b':2}
print(d.pop("x", None))  # None (bez greške)
```

## 7) Pogledi (views) i iteracija

```python
d = {"a":1,"b":2}
print(list(d.keys()))      # ['a','b']
print(list(d.values()))    # [1,2]
for k, v in d.items():
    print(k, v)
```

## 8) Hashability (ok)

```python
k = (1,2)
d = {k: "ok"}
print(d[k])         # "ok"
```

## 9) Hashability (greška)

```python
try:
    {[]: 1}
except Exception as e:
    print(type(e).__name__)  # TypeError

try:
    {([1],2): "no"}
except Exception as e:
    print(type(e).__name__)  # TypeError
```

## 10) Shallow vs deep

```python
import copy
d = {"x": [1,2]}
sh = d.copy()                 # deli unutrašnju listu
dp = copy.deepcopy(d)         # nezavisan

d["x"][0] = 99
print(sh["x"][0])   # 99  (curi)
print(dp["x"][0])   # 1   (ne curi)
```

````

---

# 4) Testovi za `dict` (pytest)

Fajl: `labs/core_functions/tests/test_dict_basics.py`

```python
import copy
import pytest

def test_get_vs_indexing():
    d = {"x": 1}
    with pytest.raises(KeyError):
        _ = d["y"]
    assert d.get("y") is None
    assert d.get("y", 99) == 99

def test_membership_is_on_keys():
    d = {"a": 1, "b": 2}
    assert "a" in d
    assert 1 not in d
    assert 1 in d.values()

def test_hashable_keys():
    k = (1, 2)
    d = {k: "ok"}
    assert d[k] == "ok"

def test_unhashable_keys_raise():
    with pytest.raises(TypeError):
        {[]: 1}
    with pytest.raises(TypeError):
        {([1], 2): "no"}

def test_shallow_vs_deep_copy_on_values():
    d = {"x": [1, 2]}
    sh = d.copy()
    dp = copy.deepcopy(d)
    d["x"][0] = 99
    assert sh["x"][0] == 99   # deli unutrašnjost
    assert dp["x"][0] == 1    # deep je nezavisan

def test_setdefault_builds_container_once():
    d = {}
    d.setdefault("items", []).append("x")
    d.setdefault("items", []).append("y")
    assert d["items"] == ["x", "y"]
````

Pokretanje:

```bash
pytest labs/core_functions/tests/test_dict_basics.py -q
```

---

# 5) Python Tutor – kako da “vidiš” dict kopije

Nalepi u Python Tutor:

```python
import copy
d = {"x": [1,2]}
sh = d.copy()
dp = copy.deepcopy(d)
d["x"][0] = 99
print(d, sh, dp)
```

- Videćeš da `d["x"]` i `sh["x"]` pokazuju na **istu** listu (deljenje), a `dp["x"]` je **nova** lista.

---

# 6) “Amateur mod” mini QA

**Mentor:** Zašto `1 in d` daje `False` iako `1` postoji u vrednostima?
**Junior:** Zato što `in` na dict-u gleda **ključeve**.
**Mentor:** Kako bi proverio vrednosti?
**Junior:** `1 in d.values()`.

**Mentor:** Zašto `{([1],2): "no"}` baca `TypeError`?
**Junior:** `tuple` je hashable samo ako su njegovi elementi hashable – a lista `[1]` nije.

---

Ako želiš, mogu odmah i **cheatsheet za dict** u fajl `docs/cheatsheets/dict_cheatsheet.md` (isti stil kao za listu), plus mali “poster” za **hashable vs unhashable** sa primerima. Reci, pa isporučujem u sledećem koraku.

---

sjajno — dopunio sam tvoj `dict_cheatsheet.md` (ispod je kompletan sadržaj koji možeš da **zameniš** u fajlu). Uključio sam kratke REPL blokove i “gotcha” primere. (Polazna verzija koju si poslao: )

---

# 📝 Cheatsheet: Python `dict` (mapping)

**Ideja:** `dict` mapira **ključ → vrednost**. Ključevi moraju biti **hashable** (npr. `str`, `int`, `tuple` od hashable elemenata).
Membership (`in`) gleda **ključeve**, ne vrednosti.

---

## 1) Kreiranje

```python
d = {}                              # prazan
d = {"a": 1, "b": 2}                # literal
d = dict([("a", 1), ("b", 2)])      # iz parova
d = dict(a=1, b=2)                  # imenovani argumenti
```

## 2) Pristup vrednostima

```python
d = {"x": 1}
d["x"]            # 1
# d["y"]          # KeyError (ako ključ ne postoji)

d.get("y")        # None (bez greške)
d.get("y", 99)    # 99 (default)
```

## 3) Umetanje / izmena

```python
d = {}
d["a"] = 1                     # dodaj
d["a"] = 10                    # izmeni
d.update({"b": 2, "c": 3})     # bulk update

# setdefault: vrati vrednost ako postoji; inače je postavi pa vrati
items = d.setdefault("items", [])
items.append("x")
# d == {'a': 10, 'b': 2, 'c': 3, 'items': ['x']}
```

## 4) Brisanje

```python
d = {"a": 1, "b": 2}
v = d.pop("a")             # vrati 1 i ukloni ključ "a"
# d.pop("z")               # KeyError (ako nema)
d.pop("z", None)           # None (bez greške)
del d["b"]                 # KeyError ako ne postoji
d.clear()                  # isprazni dict
```

## 5) Pogledi (views) i iteracija

```python
d = {"a": 1, "b": 2}
d.keys()        # dict_keys(['a', 'b'])
d.values()      # dict_values([1, 2])
d.items()       # dict_items([('a',1), ('b',2)])

for k in d:                 # isto kao for k in d.keys()
    print(k)

for k, v in d.items():      # parovi
    print(k, v)
```

## 6) Membership (članstvo)

```python
d = {"a": 1, "b": 2}
"a" in d           # True  (ključevi)
1 in d             # False (vrednosti nisu članstvo)
1 in d.values()    # True  (ako želiš vrednosti)
```

## 7) Kopije (shallow vs deep)

```python
import copy
d = {"x": [1, 2]}

sh = d.copy()               # plitka (deli unutrašnju listu)
dp = copy.deepcopy(d)       # duboka (nezavisna)

d["x"][0] = 99
sh["x"][0] == 99            # True  (curi)
dp["x"][0] == 1             # True  (ne curi)
```

## 8) Hashability (pravila za ključ)

```python
{(1, 2): "ok"}              # tuple je hashable (ako su elementi hashable)
# {[]: 1}                   # TypeError (list nije hashable)
# {([1], 2): "no"}          # TypeError (tuple sadrži nehashable listu)

# Brz REPL test:
def is_hashable(x):
    try:
        hash(x); return True
    except TypeError:
        return False
is_hashable((1,2))  # True
is_hashable([1,2])  # False
```

## 9) Merge operatori (3.9+)

```python
a = {"x": 1}
b = {"y": 2, "x": 10}
a | b          # {'x': 10, 'y': 2}  (b prepisuje a)
a |= b         # in-place merge: a postaje {'x': 10, 'y': 2}
```

## 10) Mini “gotcha” lista

- `in` proverava **ključeve**, ne vrednosti.
- `d.get(k)` ne baca grešku; `d[k]` baca `KeyError` ako nema.
- Shallow kopija (`d.copy()`) deli unutrašnje mutabilne objekte.
- Ključevi moraju biti **hashable** i **nepromenljivi** (stabilan `__hash__`).
- Redosled u `dict` je **redosled umetanja** (stabilan od Pythona 3.7).

---

## 🎯 Brzi REPL test (assert varijanta)

```python
import copy, pytest

d = {"x": [1, 2]}
sh = d.copy()
dp = copy.deepcopy(d)
d["x"][0] = 99
assert sh["x"][0] == 99
assert dp["x"][0] == 1

d = {"a": 1}
assert "a" in d and 1 not in d
assert 1 in d.values()

with pytest.raises(KeyError):
    _ = d["zzz"]
assert d.get("zzz") is None
assert d.get("zzz", 42) == 42

try:
    {[]: 1}
except TypeError:
    pass
else:
    raise AssertionError("list kao ključ mora da padne")
```

---

## 🧠 Pojmovi (za Glossary)

- **hashable** – objekat čiji se `__hash__` ne menja tokom života i može biti ključ mape.
- **mapping** – struktura “ključ→vrednost” (npr. `dict`).
- **shallow copy** – kopira samo spoljni kontejner, deli unutrašnje reference.
- **deep copy** – rekurzivno kopira unutrašnje objekte.

---

super, uživajte u šetnji! 💙
Pripremio sam ti traženo – **mini test fajl** i **ASCII poster**. Samo ih iskopiraj u repo.

---

## 📂 `labs/core_functions/tests/test_dict_hashability.py`

```python
import pytest
import builtins
import math

def is_hashable(x) -> bool:
    try:
        hash(x)
        return True
    except TypeError:
        return False


# === Happy: dozvoljeni (hashable) ključevi ===

def test_hashable_simple_keys():
    d = {
        1: "int",
        "x": "str",
        (1, 2): "tuple_of_hashables",
        frozenset({1, 2}): "frozenset",
        None: "none",
        True: "bool",
    }
    # sanity
    assert d[1] == "int"
    assert d["x"] == "str"
    assert d[(1, 2)] == "tuple_of_hashables"
    assert d[frozenset({1, 2})] == "frozenset"
    assert d[None] == "none"
    assert d[True] == "bool"
    # svi navedeni zaista jesu hashable
    for k in d.keys():
        assert is_hashable(k)


# === Error: nedozvoljeni (unhashable) ključevi ===

def test_unhashable_basic_types_raise():
    with pytest.raises(TypeError):
        {[]: 1}                 # list
    with pytest.raises(TypeError):
        {{1, 2}: "set"}         # set
    with pytest.raises(TypeError):
        {{1: 2}: "dict"}        # dict kao ključ

def test_tuple_containing_unhashable_is_unhashable():
    # tuple je hashable SAMO ako su SVI njegovi elementi hashable
    with pytest.raises(TypeError):
        {([1], 2): "no"}        # lista unutra kvari stvar
    with pytest.raises(TypeError):
        {( {1}, 2 ): "no"}      # set unutra kvari stvar

def test_custom_object_without_hash_is_hashable_by_identity():
    class A:
        # nema __eq__/__hash__ → nasleđuje object.__hash__ → hashable po identitetu
        pass
    a1, a2 = A(), A()
    d = {a1: "one", a2: "two"}
    assert d[a1] == "one" and d[a2] == "two"
    assert is_hashable(a1) and is_hashable(a2)

def test_custom_object_explicitly_unhashable():
    class B:
        __hash__ = None      # standardna konvencija: instanca NIJE hashable
    with pytest.raises(TypeError):
        {B(): "x"}

def test_is_hashable_helper_spot_checks():
    # brzi sanity za helper
    samples_true  = [0, 1.5, "s", (1, 2), frozenset({1}), builtins, math]
    samples_false = [[], {}, set(), [1, 2]]
    assert all(is_hashable(x) for x in samples_true)
    assert all(not is_hashable(x) for x in samples_false)
```

Pokretanje (iz korena `labs/core_functions`):

```bash
pytest labs/core_functions/tests/test_dict_hashability.py -q
```

---

## 📂 `docs/diagrams/hashable_vs_unhashable.md`

````markdown
# 🔐 Hashable vs Unhashable (poster)

Ideja: **ključ u dict-u** mora biti **hashable** → stabilan `__hash__` (+ tip obično nepromenljiv).
Ako ključ nije hashable → `TypeError`.

---

## ✅ Hashable (dozvoljeno)

```text
int, float, str, bool, bytes, None
tuple (ako su svi elementi hashable)
frozenset (nepromenljiv set)
object instanca (po defaultu hashable po identitetu)
```
````

Primeri:

```python
d = {
  1: "ok",
  "x": "ok",
  (1,2): "ok",
  frozenset({1,2}): "ok",
  None: "ok",
}
```

---

## ❌ Unhashable (nedozvoljeno)

```text
list, dict, set
tuple KOJI SADRŽI list/dict/set
klasa sa __hash__ = None
```

Primeri:

```python
{[]: 1}            # TypeError
{{1,2}: "x"}       # TypeError
{{"a": 1}: "x"}    # TypeError
{([1], 2): "x"}    # TypeError  (tuple sadrži listu)
```

---

## 🧠 Zašto?

- `dict` koristi **hash** da brzo pronađe kofu (bucket) za ključ.
- Ako bi ključ mogao da se **promeni** nakon umetanja (npr. listi menjaš sadržaj),
  njegov hash bi postao nevažeći → struktura mape bi se pokvarila.

---

## 🧪 Brzi REPL test

```python
def is_hashable(x):
    try:
        hash(x); return True
    except TypeError:
        return False

print(is_hashable((1,2)))      # True
print(is_hashable([1,2]))      # False
print(is_hashable(frozenset({1,2})))  # True
```

---

## 📌 Saveti

- Ako ti treba “set ključeva” koji sadrže elemente skupa → koristi **frozenset**.
- Ako trebaš kompleksan ključ → koristi **tuple od hashable elemenata**.
- Ako praviš svoju klasu i želiš da bude ključeva → ostavi podrazumešani `__hash__`
  (po identitetu) ili implementiraj **stabilan** `__hash__` uz konzistentan `__eq__`.

---

Super, evo nastavka u duhu prethodnih materijala – jedan **mini test fajl** i jedan **ASCII poster** koji pravi jasnu sliku razlike hashable/unhashable.

---

## 1. `labs/core_functions/tests/test_dict_hashable.py`

```python
import pytest

def test_hashable_keys_ok():
    d = {1: "int", (1, 2): "tuple", "s": "str"}
    assert d[1] == "int"
    assert d[(1, 2)] == "tuple"
    assert d["s"] == "str"

def test_unhashable_keys_fail():
    with pytest.raises(TypeError):
        {["a", "b"]: "lista nije hashable"}

    with pytest.raises(TypeError):
        {{1: 2}: "dict nije hashable"}  # dict kao ključ
```

👉 Dva testa: jedan happy path (int, tuple, str su **hashable**), jedan error path (list/dict nisu hashable).

---

## 2. `docs/diagrams/hashable_vs_unhashable.md`

```markdown
# Poster: Hashable vs Unhashable
```

## Hashable (može biti ključ u dict/set)

int → stabilan hash, nepromenljiv
str → stabilan hash, nepromenljiv
tuple → hashable samo ako svi elementi hashable
frozenset → nepromenljiv set

## Unhashable (NE može biti ključ u dict/set)

list → promenljiv sadržaj → nema stabilan hash
dict → promenljiv (ključevi i vrednosti) → nema hash
set → promenljiv (može dodavati/brisati) → nema hash

ASCII prikaz odnosa:

```
    +-------------------+
    |   HASHABLE        |
    |  (immutable)      |
    |                   |
    |  int, str, tuple  |
    |  frozenset        |
    +-------------------+
              |
              |  koristi stabilan __hash__ + __eq__
              v
    +-------------------+
    | UNHASHABLE        |
    | (mutable)         |
    |                   |
    |  list, dict, set  |
    +-------------------+
```

```

```

---

📌 Predlog: kad se vratiš sa šetnje, možeš probati:

```bash
pytest labs/core_functions/tests/test_dict_hashable.py -q
```

da vidiš kako testovi rade.

Želiš da odmah pripremim i **mini REPL plan (10 kratkih koraka)** za `dict` kao što smo radili sa listama?

---

super! evo **mini REPL plana (10 koraka) za `dict`** – copy/paste blokovi sa očekivanim ishodima u komentarima. Predloženi put:

`labs/core_functions/dict_repl_plan.md`

---

# 🐍 REPL: `dict` u 10 kratkih koraka

Kopiraj blok po blok u REPL/VSCode terminal (aktiviraj `.venv`).

## 1) Kreiranje i osnovni pristup

```python
d = {"a": 1, "b": 2}
print(d["a"])          # 1
d["c"] = 3
print(d)               # {'a': 1, 'b': 2, 'c': 3}
```

## 2) `get` vs `[]` (bezbedno čitanje)

```python
d = {"x": 1}
try:
    _ = d["y"]
except Exception as e:
    print(type(e).__name__)   # KeyError
print(d.get("y"))             # None
print(d.get("y", 99))         # 99
```

## 3) Članstvo (gleda KLJUČEVE)

```python
d = {"a": 1, "b": 2}
print("a" in d)        # True
print(1 in d)          # False (vrednosti nisu članstvo)
print(1 in d.values()) # True
```

## 4) Update + `setdefault`

```python
d = {"a": 1}
d.update({"b": 2})
bucket = d.setdefault("items", [])
bucket.append("x")
print(d)               # {'a': 1, 'b': 2, 'items': ['x']}
```

## 5) Brisanje (`pop`, `del`)

```python
d = {"a": 1, "b": 2}
v = d.pop("a")
print(v, d)            # 1 {'b': 2}
print(d.pop("zzz", None))  # None (bez greške)
del d["b"]
print(d)               # {}
```

## 6) Pogledi (views) i iteracija

```python
d = {"a": 1, "b": 2}
print(list(d.keys()))      # ['a','b']
print(list(d.values()))    # [1,2]
print(list(d.items()))     # [('a',1),('b',2)]
for k, v in d.items():
    print(k, v)
```

## 7) Hashable ključevi (ok)

```python
k = (1, 2)
d = {k: "ok", "s": "str", 10: "int"}
print(d[k], d["s"], d[10])  # ok str int
```

## 8) Unhashable ključevi (greške)

```python
try:
    {[]: 1}
except Exception as e:
    print(type(e).__name__)   # TypeError

try:
    {([1], 2): "no"}
except Exception as e:
    print(type(e).__name__)   # TypeError
```

## 9) Shallow vs Deep (vrednosti)

```python
import copy
d = {"x": [1, 2]}
sh = d.copy()                # deli unutrašnju listu
dp = copy.deepcopy(d)        # sve novo

d["x"][0] = 99
print(sh["x"][0])   # 99  (curi)
print(dp["x"][0])   # 1   (ne curi)
```

## 10) Merge operatori (3.9+)

```python
a = {"x": 1}
b = {"x": 10, "y": 2}
print(a | b)   # {'x': 10, 'y': 2}
a |= b
print(a)       # {'x': 10, 'y': 2}
```

---

## 🧠 Mini “što zapamtiti”

- `in` na dict-u proverava **ključeve**; vrednosti: `x in d.values()`.
- `get(k, default)` je bezbedan; `d[k]` baca `KeyError` ako ne postoji.
- Ključevi moraju biti **hashable** (npr. `tuple` od hashable elemenata).
- `d.copy()` je **shallow** (deli mutabilne vrednosti); `deepcopy` je nezavisan.
- `a | b` / `a |= b` – merge (3.9+).

Hoćeš da odmah pripremim i **tests/test_dict_basics.py** koji 1:1 prati ove korake asertacijama (happy/edge/error)?

---

Super 👌 Evo šta sam pripremio za tvoju pauzu:

---

## ✅ Novi test fajl — `labs/core_functions/tests/test_dict_hashable.py`

```python
import pytest

def test_hashable_key_ok():
    # int je hashable
    d = {1: "a"}
    assert d[1] == "a"

    # tuple je hashable AKO su svi elementi hashable
    d2 = {(1, 2): "ok"}
    assert d2[(1, 2)] == "ok"

    # string je hashable
    d3 = {"x": 42}
    assert d3["x"] == 42


def test_unhashable_key_fail():
    # list nije hashable → TypeError
    with pytest.raises(TypeError):
        {["a", "b"]: "oops"}

    # dict nije hashable → TypeError
    with pytest.raises(TypeError):
        {{1: 2}: "bad"}

    # tuple sa listom unutra → TypeError
    with pytest.raises(TypeError):
        {(1, [2, 3]): "also bad"}
```

👉 Ovo ti pokazuje jasnu razliku: **hashable** tipovi mogu biti ključevi u dict, dok mutable tipovi ne mogu.

---

## 🎨 ASCII poster — `docs/diagrams/dict_hashable_refs.md`

```markdown
# 🔑 Hashable vs Unhashable (dict keys)

             +----------------+
             |   HASHABLE     |
             +----------------+
             | int            |
             | float (finite) |
             | str            |
             | bool           |
             | tuple(*)       |
             | frozenset      |
             +----------------+
                  ✅ može biti ključ
                  (stabilan __hash__)

             +----------------+
             | UNHASHABLE     |
             +----------------+
             | list           |
             | dict           |
             | set            |
             | tuple sa list  |
             | bytearray      |
             +----------------+
                  ❌ ne može biti ključ
                  (menja se u mestu → hash se kvari)

(\*) tuple je hashable SAMO ako su svi njegovi elementi hashable.
```

---

👉 Predlog:

- Testove pusti u svom `core_functions` venv-u:

  ```bash
  pytest labs/core_functions/tests/test_dict_hashable.py -q
  ```

- Poster otvori u **Markor** na telefonu → odličan brzi pregled.

---

Hoćeš da nastavimo ovim stilom (test + ASCII “poster”) i za sledeće teme iz dict (npr. `get() vs []` i `KeyError`)?

---

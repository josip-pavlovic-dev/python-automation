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

## 1) Osnove i pristup

```python
d = {"a":1, "b":2}
print(d["a"])      # 1
d["c"] = 3
print(d)           # {'a':1,'b':2,'c':3}
```

## 2) get vs []

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

---

# 4) Testovi za `dict` (pytest)

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
```

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

---

📌 Predlog: kad se vratiš sa šetnje, možeš probati:

```bash
pytest labs/core_functions/tests/test_dict_hashable.py -q
```

da vidiš kako testovi rade.

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

---

Hoćeš da nastavimo ovim stilom (test + ASCII “poster”) i za sledeće teme iz dict (npr. `get() vs []` i `KeyError`)?

---

### Opcije pokretanja:

#### 1. Klasično (relativna putanja)

Ako si u `labs/core_functions`:

```bash
python dayB/try_code.py
```

#### 2. Kao modul (`-m`)

Za `-m` moraš da pokreneš **iznad** `dayB` foldera, jer se on tretira kao paket.
Dakle:

```bash
cd labs/core_functions
python -m dayB.try_code
```

👉 ali **samo ako u `dayB/` postoji `__init__.py`** (pa je paket).
Ako ga nema, onda koristiš samo fajl putanju (opcija 1).

#### 3. Ako si u root repoa (`python-automation`)

```bash
cd ~/dev-learning/python-automation
python -m labs.core_functions.dayB.try_code
```

---

⚡ Brza preporuka (za vežbanje):
Pošto si još u fazi učenja i ne radiš deployment, najjednostavnije → **koristi opciju 1**:

```bash
python labs/core_functions/dayB/try_code.py
```

---

super pitanja — kratko i jasno, pa REPL mini-blokovi gde vredi 👇

---

## 1) Tab i “ko mi zapravo predlaže kod”: Pylance vs Copilot

- **Pylance** = jezički server za Python (statika). Daje **IntelliSense**: listu predloga, tipove, docstringe.

  - Vizuelno: padajući meni sa ikonama tipova (`ƒ`, `()`, 🧠…), nema “ghost” teksta u liniji.
  - Triger: `Ctrl+Space` (ili samo kucaš, pa se meni otvori).

- **GitHub Copilot** = AI predlog (hela linija/blok) kao **sivi ghost tekst u editoru**.

  - Prihvatanje: `Tab` (ili `Ctrl+Enter`).
  - Odbij: nastavi da kucaš, ili `Esc`.
  - Ikonica Copilota se često vidi u status-baru; u listi predloga piše “Copilot”.

- **Da li “trošiš Copilot” pritiskom na Tab?**
  Ako prihvatiš **Copilot ghost** → da, to je Copilot predlog. Ako samo biraš iz **Pylance menija** → to je Pylance.
- **Kako da kontrolišeš?**

  - Privremeno ugasi Copilot u ovom workspace-u: Command Palette → “Copilot: Disable For Workspace”.
  - Uključi/isključi inline predloge: `editor.inlineSuggest.enabled`.

> Pravilo: vidiš **ghost** → Copilot; vidiš **dropdown listu** → Pylance.

---

## 2) “Bool sintakse” koje najčešće koristiš (mini-spisak)

Generalno sve ispod vraća `True/False`:

- **Članstvo**:

  - `k in d` (za dict gleda **ključeve**)
  - `v in d.values()` (vrednosti)
  - `"x" in s` (string), `x in lista`, `x in set`

- **Negacija članstva**: `x not in kolekcija`
- **Poređenja (vrednosti)**: `==`, `!=`, `<`, `<=`, `>`, `>=`

  - liste/stringovi: leksikografski (`[1,2] < [1,3]`)

- **Identitet (isti objekat?)**: `is`, `is not`
- **Truthiness (istinita vrednost)**: `if d:` (prazan `dict/list/str` je `False`)
- **Len proverе**: `len(xs) == 0` (ekvivalentno `not xs`)
- **Set relacije**: `<=` (subset), `>=` (superset), `|`, `&`, `-`
- **String predikati**: `"abc".startswith("a")`, `.endswith("c")`, `str.isdigit()`, …

Brzi primeri:

```python
d = {"a": 1, "b": 2}
assert "a" in d
assert 1 not in d           # vrednosti nisu članstvo
assert 1 in d.values()

xs = [1,2,3]
assert 2 in xs and 9 not in xs
assert xs and len(xs) == 3  # True
```

---

## 3) `==` vs `is` (kada šta?)

- `==` proverava **jednakost vrednosti**.
- `is` proverava **identitet objekta** (da li su iste reference / isti `id()`).

Koristi `is` **samo** sa **singletonima**: `None`, `True`, `False`, `Ellipsis`, ili svojim sentinelom.

REPL:

```python
a = [1,2]; b = [1,2]; c = a
assert (a == b) is True     # iste vrednosti
assert (a is b) is False    # različni objekti
assert (a is c) is True     # isti objekat

x = None
assert (x is None)          # is je ispravno za None
```

> Zbog interninga, ponekad mali int/kratki stringovi mogu “deliti” objekat, ali se na to **ne oslanjamo**; za vrednosti → `==`.

---

## 4) `.get` i “rođaci” koje vredi znati (bezbedan pristup sa default-om)

Najkorisniji “safe access” idiomi:

| Gde              | Šta radi                                 | Primer                               |
| ---------------- | ---------------------------------------- | ------------------------------------ |
| **dict**         | uzmi vrednost ili `default`              | `d.get(k, default)`                  |
| **dict**         | uzmi i ukloni (sa default-om)            | `d.pop(k, default)`                  |
| **dict**         | dohvati ili kreiraj pa vrati (za append) | `d.setdefault(k, [])`                |
| **objekat**      | uzmi atribut ili `default`               | `getattr(obj, "name", "N/A")`        |
| **objekat**      | postavi atribut                          | `setattr(obj, "name", "Jole")`       |
| **okruženje**    | uzmi var iz env-a ili `default`          | `os.environ.get("API_KEY", "")`      |
| **default dict** | mapirani podrazumevani tip               | `defaultdict(list)` iz `collections` |
| **Counter**      | brojanje sa podrazumevanim 0             | `Counter(seq)["key"]` →              |

Mikro-primjeri:

```python
# dict.get / pop / setdefault
d = {}
d.setdefault("items", []).append("x")     # {'items': ['x']}
v = d.get("user", "guest")                # 'guest'
v = d.pop("missing", None)                # None (bez KeyError)

# getattr
class U: pass
u = U()
name = getattr(u, "name", "anon")         # 'anon'
setattr(u, "name", "Jole")
assert u.name == "Jole"

# defaultdict
from collections import defaultdict, Counter
dd = defaultdict(list)
dd["a"].append(1)                         # ne baca KeyError; auto-kreira listu
cnt = Counter("banana")
assert cnt["a"] == 3                      # 0 za “nepostojeće” ključeve
```

---

## Mini-REPL “za poneti”

```python
# 1) in / not in
d = {"a":1}
print("a" in d, 1 in d.values())          # True True

# 2) == vs is
a, b, c = [1,2], [1,2], None
print(a == b, a is b)                     # True False
print(c is None)                          # True

# 3) get / pop / setdefault / getattr
d = {}
print(d.get("x", 99))                     # 99
print(d.pop("x", None))                   # None
d.setdefault("items", []).append("x")
print(d)                                  # {'items': ['x']}

class U: pass
u = U()
print(getattr(u, "name", "anon"))         # 'anon'
setattr(u, "name", "Jole")
print(u.name)                             # 'Jole'
```

---

top pitanja—idemo redom, kratko i jasno, sa REPL primerima i mini-cheatsheetom 👇

---

## 1) Šta su “singletoni”, `Ellipsis` i “sentinel”

- **Singleton** = objekat od kog u sistemu postoji **samo jedna instanca**.
  U Pythonu: `None`, `True`, `False`, `Ellipsis` (`...`), ponekad i `NotImplemented`.
  Za njih se koristi **`is`** (identitet), npr. `x is None`.

- **`Ellipsis`** (`...`) je poseban singleton. Često se koristi:

  - kao “nije implementirano još” u telu funkcije/klase,
  - u naprednim slice-ovima/numpy-u.
    Primer:

  ```python
  def todo():
      ...
  ```

  ili

  ```python
  if cond: return ...
  ```

- **Sentinel** = **jedinstveni marker** koji ne može da se pomeša sa “pravim” vrednostima.
  Pravimo ga kao novi objekat:

  ```python
  MISSING = object()
  def lookup(d, k):
      v = d.get(k, MISSING)
      if v is MISSING:
          return "nije-nađeno"
      return v
  ```

---

## 2) Zašto `d.setdefault("items", []).append("x")` ispiše `None`?

`setdefault` radi **dve stvari**:

1. Ako ključ ne postoji → **ubaci** dati default i **vrati** **vrednost** pod tim ključem.
2. Ako postoji → samo **vrati** postojeću vrednost.

U tvom izrazu:

- `d.setdefault("items", [])` **vrati listu** (npr. `[]`, pa posle `[... ]`).
- **`append("x")`** vraća **`None`** (mutira listu in-place).
  Zato ceo izraz štampa `None`, iako je dict izmenjen.

REPL dokaz:

```python
d = {}
x = d.setdefault("items", [])
print(x)           # []
x.append("x")
print(d)           # {'items': ['x']}

# ili u jednoj liniji (mutacija se desila, ali povrat je None)
print(d.setdefault("items", []).append("y"))  # None
print(d)  # {'items': ['x', 'y']}
```

---

## 3) Zašto `d.get("user", "guest")` vraća `"guest"`?

Jer **ključ `"user"` ne postoji** u `d`, pa `get` vraća **default** (`"guest"`).
Ako ključ postoji → vrati njegovu vrednost.

```python
d = {}
print(d.get("user", "guest"))  # 'guest'
d["user"] = "jole"
print(d.get("user", "guest"))  # 'jole'
```

---

## 4) Cheatsheet: `try/except`, `raise`, `assert`, `pass`, … (za testove i svakodnevni kod)

Sažeto + primeri koje viđaš u pytest-u.

### 4.1. Osnovni oblik

```python
try:
    risky()
except ValueError as e:
    print("nešto nije u formatu:", e)
```

### 4.2. Više `except` grana + zajednički roditelj

```python
try:
    parse(x)
except (ValueError, TypeError) as e:
    handle(e)
```

### 4.3. `else` i `finally`

```python
try:
    y = compute()
except ZeroDivisionError:
    y = 0
else:
    log("ok grana")          # radi se samo ako NIJE bilo izuzetka
finally:
    cleanup()                # uvek se izvršava
```

### 4.4. `raise` (podizanje greške – ručno)

```python
def safe_int(s):
    if not isinstance(s, str):
        raise TypeError("očekujem string")
    return int(s)
```

### 4.5. `assert` (brza provera uslova)

- U testovima se koristi stalno (nativni `assert`).
- U **proizvodnom kodu** za validaciju → radije eksplicitni `if` + `raise`, jer Python može biti pokrenut sa `-O` pa se `assert` preskoči.

```python
def middle(xs):
    assert xs, "lista ne sme biti prazna"  # test/razvoj: ok
    return xs[len(xs)//2]
```

### 4.6. `pass` i `...` (Ellipsis)

```python
def interface_only():
    pass       # namerno ništa

def todo():
    ...        # “ovde će ići kod kasnije”
```

### 4.7. `with` kontekst (zatvaranja resursa)

```python
with open("data.txt") as f:
    data = f.read()
# fajl automatski zatvoren
```

### 4.8. `pytest.raises` (očekujemo grešku)

```python
import pytest

def test_bad_key():
    d = {}
    with pytest.raises(KeyError):
        _ = d["missing"]

def test_type_error():
    with pytest.raises(TypeError, match="hashable"):
        {[]: 1}
```

### 4.9. `warnings` (ako loviš upozorenja)

```python
import warnings
def old():
    warnings.warn("deprecated", DeprecationWarning)

import pytest
def test_warns():
    with pytest.warns(DeprecationWarning):
        old()
```

### 4.10. `unittest.mock` (stub/patch kad ti zatreba)

```python
from unittest.mock import patch

def fetch(url):
    ...

def test_fetch():
    with patch("mod.requests.get") as fake:
        fake.return_value.json.return_value = {"ok": 1}
        assert fetch("x") == {"ok": 1}
```

### 4.11. Patterni za “safe access” (često viđeni u testovima)

```python
# dict
v = d.get("k", default)

# objekat
name = getattr(obj, "name", "anon")
setattr(obj, "name", "Jole")

# kolekcije
from collections import defaultdict, Counter
dd = defaultdict(list); dd["k"].append(1)
cnt = Counter("banana"); assert cnt["a"] == 3
```

---

## Mini-REPL blok (copy/paste)

```python
# 1) try/except/else/finally
def risky(x):
    return 10 // x

try:
    risky(0)
except ZeroDivisionError:
    print("deljenje nulom")
else:
    print("nema greške")
finally:
    print("gotovo")

# 2) raise i assert
def safe_div(a, b):
    if b == 0:
        raise ValueError("b ne sme biti 0")
    return a / b

assert safe_div(4,2) == 2.0

# 3) pytest.raises (pokreni u testu)
# with pytest.raises(ValueError):
#     safe_div(1, 0)

# 4) pass i ...
def not_yet(): ...
class Interface: pass
```

---

## Glossary dopuna (mini)

- **singleton** – jedinstveni objekat (npr. `None`, `Ellipsis`) → poredi se sa `is`.
- **sentinel** – specijalna jedinstvena vrednost (`MISSING = object()`), marker “nema vrednost”.
- **identity** – identitet objekta (`id(x)`), proverava se `is`.
- **truthiness** – kako se objekat ponaša u `if` (prazne kolekcije su `False`).

---

super — evo “paketa” za **`dict: get() vs [] i KeyError`** u istom stilu (test + ASCII poster). Kopiraj u repo i pusti test.

---

## 📂 `labs/core_functions/tests/test_dict_get_vs_indexing.py`

```python
import pytest

def test_get_returns_default_when_missing():
    d = {"a": 1}
    assert d.get("a") == 1
    assert d.get("x") is None
    assert d.get("x", 99) == 99          # bez KeyError-a

def test_indexing_raises_keyerror_when_missing():
    d = {"a": 1}
    with pytest.raises(KeyError):
        _ = d["x"]                       # [] traži da ključ postoji

def test_no_side_effects_for_get():
    d = {}
    _ = d.get("items", [])               # ne menja dict
    assert d == {}                       # i dalje prazan

def test_setdefault_has_side_effects_once():
    d = {}
    # kreira 'items' ako ne postoji, vrati listu, pa se mutira append-om
    d.setdefault("items", []).append("x")
    assert d == {"items": ["x"]}

    # drugi put se ključ već nalazi – koristi istu listu
    d.setdefault("items", []).append("y")
    assert d["items"] == ["x", "y"]

def test_pop_with_default_is_safe():
    d = {"a": 1}
    assert d.pop("a", None) == 1         # vrati i ukloni
    assert d == {}
    assert d.pop("a", None) is None      # umesto KeyError-a

def test_keyerror_message_contains_key():
    d = {}
    with pytest.raises(KeyError) as ei:
        _ = d["user"]
    # Lenja, ali korisna provera: poruka sadrži repr ključa
    assert "'user'" in str(ei.value)
```

Pokretanje:

```bash
pytest labs/core_functions/tests/test_dict_get_vs_indexing.py -q
```

---

## 📂 `docs/diagrams/dict_get_vs_indexing.md` (ASCII poster)

```markdown
# 🧭 dict: `get()` vs `[]` i `KeyError`

Cilj: bezbedan pristup vrednosti kada ključ možda ne postoji.

---

## A) Indexing: d[k]

Semantika:

- PRETPOSTAVLJA da ključ POSTOJI.
- Ako ne postoji → baca KeyError.

ASCII:
d = {"a": 1}

         +-------------+
    "a"  |     1       |   d["a"] → 1
         +-------------+

         +-------------+
    "x"  |    nema     |   d["x"] → KeyError: 'x'
         +-------------+

---

## B) get: d.get(k, default=None)

Semantika:

- Ako ključ postoji → vrati vrednost.
- Ako ne postoji → vrati default (po difoltu None).
- NIKAD ne baca KeyError.

ASCII tok:
postoji? ──► DA ──► vrati d[k]
└► NE ──► vrati default (npr. 99 ili None)

---

## C) setdefault: d.setdefault(k, default)

Semantika:

- Ako ključ ne postoji → d[k] = default i VRATI default.
- Ako postoji → VRATI postojeću vrednost (bez zamene).

ASCII:
d = {}
d.setdefault("items", []) ──► d = {"items": []}
d.setdefault("items", []).append("x") ──► {"items": ["x"]}

⚠ Gotcha:
d.setdefault("k", []).append(v) # vraća None jer append mutira listu in-place

---

## D) pop: d.pop(k, default=MISSING)

- Ukloni i vrati d[k].
- Ako ne postoji i default NIJE dat → KeyError.
- Ako default JESTE dat → vrati default (bez greške).

---

## E) Najčešći obrasci

- Bezbedno čitanje: v = d.get("user", "guest")
- Uklanjanje bez greške: v = d.pop("user", None)
- Gradnja liste u mapi: d.setdefault("items", []).append(x)
- Tvrdi zahtev: v = d["user"] # ako ključ mora postojati

Kratko pravilo:

- Nisi siguran da ključ postoji? → `get`
- Želiš da padne fail fast? → `[]`
- Želiš da kreiraš pa koristiš? → `setdefault`
- Želiš da ukloniš bezbolno? → `pop(..., default)`
```

---

Odlično! Na osnovu svega što si mi poslao (int/str/bool/dict materijal, testovi, ASCII posteri, glossary dopune) možemo da napravimo objedinjeni fajl `docs/cheatsheets/dict_basics.md`. Evo primera gotove verzije:

---

# 📘 Dict Basics

> Kratak i praktičan pregled rada sa Python `dict`.

---

## 1. Osnovni mentalni model

- **dict** je _mapping_: **ključ → vrednost**.
- Ključevi moraju biti **hashable** (npr. `int`, `str`, `tuple` od hashable elemenata).
- Vrednosti mogu biti bilo koji tip.
- Iteracija prolazi kroz **ključeve**.

---

## 2. Pravljenje i pristup

```python
d = {"a": 1, "b": 2}
print(d["a"])   # 1
print("a" in d) # True (pretražuje ključeve)
```

- `d["x"]` → baca **KeyError** ako ključ ne postoji.
- `d.get("x", default)` → vraća `default` (ili `None` ako nije naveden).

---

## 3. Uporedba `[]` i `.get()`

```python
d = {}
d["x"]      # ❌ KeyError
d.get("x")  # None
d.get("x", 0) # 0
```

📌 **Pravilo**: koristi `.get()` ako želiš bezbedan fallback.

---

## 4. Dodavanje i izmena

```python
d["c"] = 3           # novi ključ
d["a"] = 99          # izmena postojeće vrednosti
d.setdefault("z", 0) # d["z"] ako ne postoji → 0
```

⚠️ `setdefault` vraća vrednost i pravi ključ ako ga nema.

---

## 5. Brisanje

```python
del d["a"]          # KeyError ako ne postoji
d.pop("b")          # vrati i ukloni (KeyError ako ne postoji)
d.pop("b", None)    # fallback bez greške
```

---

## 6. Iteracija

```python
for k in d: print(k)           # ključevi
for v in d.values(): print(v)  # vrednosti
for k, v in d.items(): print(k, v) # parovi
```

---

## 7. Hashable vs Unhashable (ključ)

- ✅ hashable: `int`, `str`, `tuple((1,2))`
- ❌ unhashable: `list`, `dict`, `set`

```python
{[1,2]: "x"}  # ❌ TypeError
```

---

## 8. ASCII Poster — hashable vs unhashable

```
         +----------------------+
         |   Hashable (ok)      |
         |----------------------|
         | int, str, bool       |
         | tuple(od hashable)   |
         | frozenset            |
         +----------------------+

         +----------------------+
         | Unhashable (greška)  |
         |----------------------|
         | list, dict, set      |
         | bytearray            |
         +----------------------+
```

---

## 9. ASCII Poster — get() vs \[]

```
   d = {"a": 1}

   [] pristup (strict):
   d["x"]  -> ❌ KeyError

   get() pristup (bezbedan):
   d.get("x")      -> None
   d.get("x", 0)   -> 0
```

---

## 10. Mini testovi (pytest primer)

```python
import pytest

def test_get_vs_brackets():
    d = {"a": 1}
    assert d.get("a") == 1
    assert d.get("x") is None
    with pytest.raises(KeyError):
        _ = d["x"]

def test_hashable_keys():
    d = { (1,2): "ok" }
    assert d[(1,2)] == "ok"
    with pytest.raises(TypeError):
        _ = { [1,2]: "bad" }
```

---

✅ Ovim imaš na jednom mestu i **cheatsheet**, i **ASCII postere**, i **mini testove** za `dict`.

---

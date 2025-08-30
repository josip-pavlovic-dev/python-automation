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

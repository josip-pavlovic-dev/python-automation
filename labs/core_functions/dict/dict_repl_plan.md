# REPL: dict (10 koraka)

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

DRUGA VERZIJA !!!

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

---

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

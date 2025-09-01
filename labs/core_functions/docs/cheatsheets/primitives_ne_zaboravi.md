Odlično — evo ti **spisak “šta ne smeš da zaboraviš”** za `int`, `str`, `bool`, `float` (osnove koje ti uvek trebaju kada programiraš i testiraš). Oslonio sam se i na tvoj **glossary.md** i na naše ranije beleške.

---

# 🧠 “Ne zaboravi” liste za osnovne tipove

## 🔢 `int`

- `int(x)` → poziva `x.__int__()`; ako nema → fallback na `__index__()`.
- `int(float)` **trunc prema nuli** (`-3.9 → -3`).
- `int(str, base)` → drugi parametar je **baza** (2, 8, 16).
  `base=0` → auto detekcija (`0b`, `0o`, `0x`).
- `OverflowError` ako probaš da konvertuješ `inf`/`nan` u int.
- **Mutabilnost**: `int` je **immutable** → hashable → može biti ključ dict-a.
- Interning: mali `int` (-5 do 256) se često deli, ali to je implementacioni detalj → koristi `==`, ne `is`.

👉 REPL test:

```python
print(int(-3.9))         # -3
print(int("FF", 16))     # 255
print(int("0b101", 0))   # 5
```

---

## 📜 `str`

- `repr(x)` vs `str(x)` → `repr` je tehnički (debug), `str` lepši (user-friendly).
- `str` je **immutable** → hashable → može biti ključ u dict.
- `format` i f-string: `f"{x:.2f}"`, `"{:>10}".format(x)`.
- Metode: `.startswith`, `.endswith`, `.split`, `.join`, `.strip`, `.replace`.
- `in` radi kao substring membership (`"a" in "car"` → True).

👉 REPL test:

```python
print(str(123))           # "123"
print(repr("abc"))        # "'abc'"
print("car".startswith("c"))  # True
```

---

## ✅ `bool`

- `bool(x)` → prvo poziva `x.__bool__()`, ako nema → `len(x)`.
- **Falsy**: `0`, `0.0`, `""`, `[]`, `{}`, `None`.
- Sve ostalo je `Truthy`.
- `True` i `False` su **int subclass** (`isinstance(True, int) → True`).
- Koristi `is` sa `True/False/None`, ne `==`.

👉 REPL test:

```python
print(bool([]))      # False
print(bool([1]))     # True
print(isinstance(True, int))   # True
```

---

## 🌊 `float`

- `float("inf")`, `float("-inf")`, `float("nan")`.
- Poređenja sa `nan` su uvek False (`nan != nan`).
- `math.isclose(a, b, rel_tol, abs_tol)` za poređenje realnih brojeva.
- `float` je **immutable** → hashable → može biti ključ dict-a.
- Pretvori u int → **trunc prema nuli** (`int(-3.9) == -3`).

👉 REPL test:

```python
import math
print(float("inf"), float("nan"))
print(math.isclose(0.1+0.2, 0.3, rel_tol=1e-9))
```

---

# 📌 Mini “gotcha” lista

- **Nemoj koristiti `is` za poređenje vrednosti** (`a == b` je ispravno).
- `d.get(k, default)` je sigurnije od `d[k]` (da izbegneš KeyError).
- `int/str/bool/float` su svi **immutable i hashable** → mogu biti ključevi u dict.
- `assert` je koristan u testovima, ali u produkciji koristi `if/raise`.

---

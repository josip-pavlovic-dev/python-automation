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

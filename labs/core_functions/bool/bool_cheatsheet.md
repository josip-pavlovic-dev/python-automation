# `bool()` – Cheatsheet (Mentor + Junior)

## Mentalni model

**Mentor:** `bool(x)` vraća `True` ili `False` po pravilima truthiness-a.  
**Junior:** Koja su pravila?  
**Mentor:** `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0,1)`, `''`, `[]`, `{}`, `set()`, `range(0)`, `None`, `False` su falsy. Sve ostalo je truthy.

## Potpis

```python
bool(x) -> True|False
```

## Dunder protokol

- Ako objekat ima `__bool__` → koristi se.
- Ako nema, ali ima `__len__` → 0 znači `False`, >0 znači `True`.
- Ako nema ni jedno → `True` (default).

## Primeri

```python
bool(0), bool(1)          # False, True
bool(""), bool("0")       # False, True
bool([]), bool([0])       # False, True
bool(None), bool(object())# False, True
```

## Greške

- Standardni tipovi: nikad ne dižu grešku.
- Ako `__bool__`/`__len__` vrati nešto što nije `bool` ili `int` → `TypeError`.

## QA savet

- Koristi `if xs:` umesto `if len(xs) > 0:`.
- Ne piši `if cond == True:` → dovoljno je `if cond:`.

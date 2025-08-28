# `str()` – Cheatsheet (Mentor + Junior)

> Cilj: da razlikuješ konverziju **u string**, _repr_ prikaz, i **dekodiranje bytes-a**.
> Radi paralelno u REPL-u i zapisuj opažanja.

## 1. Brzi mentalni model

**Mentor:** `str(x)` vraća _čitljiv_ tekstualni prikaz objekta `x`.
**Junior:** Znači, skoro sve mogu da pretvorim u string?
**Mentor:** Da. Ako objekat nema svoj `__str__`, Python padne na `__repr__` (tehnički prikaz) — i dalje dobijaš string.

## 2. Potpis i važna ograničenja

```python
str(object='') -> str
str(object: bytes, encoding='utf-8', errors='strict') -> str   # samo kad je object bytes-like
```

- **Ne smeš** dodavati `encoding/errors` osim ako je `object` **bytes/bytearray/memoryview** → inače **TypeError**.
- `str(bytes)` bez encoding-a daje `"b'...'"` (repr). **Ako želiš pravi tekst, koristi `.decode()`**.

## 3. Tipični primeri

```python
str(42)          # '42'
str(3.14)        # '3.14'
str(True)        # 'True'
str(None)        # 'None'
str([1, "a"])    # "[1, 'a']"
str(b"abc")      # "b'abc'"   <-- REPR bytes-a
(b"abc").decode("utf-8")  # 'abc'
```

**Mini-pravilo:** “Ako ulaz **nije** bytes-like → samo `str(x)`. Ako **jeste** → `x.decode(...)`.”

## 4. `str` vs `repr` vs formatiranje

- `str(x)`: za ljude, “prijatan” prikaz (ako ga objekat definiše).
- `repr(x)`: za debug/rekonstrukciju objekta (`__repr__`).
- `f"{x:.2f}"`, `format(x, ".2f")`: kontrolisano **formatiranje** (npr. dve decimale).

## 5. Tipične greške

- `str(b"...")` umesto `b"...".decode(...)`
- Prosleđivanje `encoding`/`errors` za ne-bytes: `TypeError`.
- Oslanjanje na `__str__` gde ga nema — dobiješ `<Class object at 0x...>`.

## 6. Brzi REPL check-list

- [ ] Probaj `str()` na brojima, bool, None, list/dict/tuple.
- [ ] Probaj `str()` na `bytes` i zatim `.decode()`.
- [ ] Napravi klasu bez `__str__` i jednu sa `__str__`; uporedi izlaz.
- [ ] Uporedi `str(x)` vs `f"{x:.2f}"` na `float`.

## 7. Profesionalni moment

- LOG poruke → koristi `str()` / formatiranje svesno (npr. za količinu decimala).
- I/O i mreža → 100% ćeš nailaziti na bytes; uvek **dekodiraj** pre obrade.
- Serijalizacija/debug → `repr()` je često bolji u testovima (precizniji).

## 8. Kratak “decision tree”

1. Da li je `x` bytes-like? → **Da** → `x.decode(encoding)`
2. Ako nije → `str(x)` je OK.
3. Treba ti format kontrola? → `format()/f-string`.
4. Treba ti developerski, precizan prikaz? → `repr(x)`.

> Spremno? Pređi na `str_analysis_notes.md` i popuni ga korak-po-korak.

---

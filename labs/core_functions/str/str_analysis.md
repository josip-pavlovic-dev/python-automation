# `str(x)` — analiza funkcije

> **Kratak opis:** > `str(x)` vraća **tekstualnu** reprezentaciju argumenta `x`.
> Ako je `x` bajt-niz (`bytes`/`bytearray`), poziva se posebna forma `str(obj, encoding, errors)` za **dekodiranje** u string.

---

## 1) Potpis i varijante

- **Opšta forma:** `str(x='') -> str`
  Ako se `x` izostavi, vrati se prazan string `''`.

- **Specijalna forma za bajtove:** `str(bytes_obj, encoding='utf-8', errors='strict') -> str`
  Dekodira bajtove u Unicode tekst.

---

## 2) Tip povratne vrednosti

- Uvek vraća tip `str` (Unicode tekst u Python-u 3).

---

## 3) Šta prihvata (ulaz)

- **Brojevi:** `int`, `float`, `complex` → `"10"`, `"3.14"`, `"(1+2j)"`.
- **Booleovi:** `True/False` → `"True"`, `"False"`.
- **`None`:** → `"None"`.
- **`str`:** vraća isti objekat ili kopiju `"abc"`.
- **Objekti:** ako klasa implementira `__str__`, koristi se to; inače pada na `__repr__`.
- **`bytes`/`bytearray`:**
  - Bez `encoding`: vraća **repr**: `str(b'abc') -> "b'abc'"` (nije dekodirano!).
  - Sa `encoding`: dekodira: `str(b'abc', 'ascii') -> 'abc'`.

---

## 4) Ponašanje / semantika

- **Human-friendly vs. dev-friendly:**
  `str(x)` je “user friendly” prikaz. Ako `__str__` ne postoji, koristi se `__repr__` koji je “developer friendly”.
- **Stabilnost “string prikaza”:**
  Ne oslanjaj se na `str(float)` za egzaktna poređenja – za formatiranje koristi `format()` / f-string (`f"{x:.2f}"`).
- **Bajtovi:**
  `str(b, enc)` radi **dekodiranje**. Ako `enc` izostaviš, `str(bytes)` samo vrati string sa prefiksom `b'...'` (repr).
- **Greške pri dekodiranju:**
  `errors='strict'` (default) baca `UnicodeDecodeError`. Alternativa: `'ignore'`, `'replace'`, `'backslashreplace'`.

---

## 5) Izuzeci i “kada puca”

- `TypeError` ako pozoveš **tro-argumentnu** formu nad ne-bajtovima: `str(10, 'utf-8')`.
- `UnicodeDecodeError` pri dekodiranju bajtova kad podaci ne prate `encoding` i `errors='strict'`.
- **Napomena:** `str(None)` _ne puca_ → `"None"`.

---

## 6) Interakcija sa `__dunder__` metodama

- `__str__(self)` ako postoji → koristi se.
- Ako ne postoji, koristi se `__repr__(self)`.
- Za brojeve i ugrađene tipove Python ima sopstvene C-implementacije `__str__`.

---

## 7) Poređenje: `str(x)` vs `repr(x)` vs `format()`

- `str(x)`: čitljiv prikaz (“za ljude”).
- `repr(x)`: nedvosmislen prikaz (“za developere”, često validan izraz).
- `format(x)` / f-string: kontrolisano formatiranje (`width`, `precision`, `align`, `:,` itd).

---

## 8) Primeri (osnovni)

```python
str(10)           # '10'
str(3.14)         # '3.14'
str(True)         # 'True'
str(None)         # 'None'
str([1, 2, 3])    # '[1, 2, 3]'

class User:
    def __init__(self, name): self.name = name
    def __str__(self):        return f"User<{self.name}>"

str(User("Ana"))  # 'User<Ana>'
```

---

## 9) Bajtovi — dekodiranje

```python
b = b'\xe2\x9c\x93'   # UTF-8 za '✓'
str(b)                # "b'\\xe2\\x9c\\x93'"  (repr, bez dekodiranja!)
str(b, 'utf-8')       # '✓'                   (dekodirano)
str(b'\xff', 'utf-8') # UnicodeDecodeError (strict)
str(b'\xff', 'utf-8', 'replace')  # '�'
```

---

## 10) Edge slučajevi i zamke

- `str(float)` kod velikih/sitnih vrednosti može koristiti eksponencijalni zapis (`'1e-06'`).
- `str(dict)` ne garantuje order pre Py3.7 (u savremenom Python-u insertion-order je očuvan, ali i dalje nije format za serijalizaciju → koristi `json`).
- `str(bytes)` bez encoding-a ne pretvara bajtove u tekst (samo repr).
  **Za dekodiranje uvek prosledi `encoding`.**

---

## 11) Profesionalne prakse

- **Logovanje i poruke korisniku:** koristi `str()`/f-strings.
- **Serijalizacija:** koristi `json`, `pydantic`, `dataclasses.asdict()` – ne `str()`.
- **I18N:** kad radiš sa fajlovima/HTTP-om, _uvek_ preciziraj encoding (tipično `"utf-8"`).
- **Custom klase:** implementiraj `__str__` (kratak prikaz) i `__repr__` (nedvosmislen).

---

## 12) Mini-checklist pre commita

- [ ] Da li mi treba **formatiranje** (`format()`/f-string) umesto plain `str()`?
- [ ] Da li baratam sa **bajtovima**? Ako da, da li sam **eksplicitno** naveo `encoding`?
- [ ] Da li klasa ima smislen `__str__` i `__repr__`?
- [ ] Da li u testovima pokrivam i `UnicodeDecodeError` putanju?

---

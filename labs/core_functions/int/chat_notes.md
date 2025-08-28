(Mentor:) Super, krećemo! Otvorićemo **int_cheatsheet.md** i ući ćemo baš u ta mesta gde si zapelo.

---

### 1️⃣ Baze brojeva (parametar `base` u `int()`)

Kad pozoveš `int("...", base=n)`, Python čita string kao **broj u bazi n**.

- **Binarno (base=2):** `"1010"` → 1\*2³ + 0\*2² + 1\*2¹ + 0\*2⁰ = **10**.
- **Hexadecimalno (base=16):** `"FF"` → F=15, pa 15\*16¹ + 15\*16⁰ = **255**.
- **Decimalno (base=10):** podrazumevano, `"42"` → 42.

Posebno:

- `base=0` → Python **sam prepozna** prefiks:
  `"0b101"` → binarno, `"0xFF"` → hex, `"0o10"` → oktal.

---

### 2️⃣ Šta su `__int__`, `__index__` i Dunder protokol

- **Dunder** = “double underscore” metode (npr. `__int__`, `__str__`). Python ih poziva “iza kulisa”.
- **`__int__`:** Ako klasa implementira ovu metodu, `int(obj)` vraća njen rezultat.

  ```python
  class WithInt:
      def __int__(self): return 42
  print(int(WithInt()))  # 42
  ```

- **`__index__`:** Fallback metoda za “celobrojne” tipove. Koristi se kada tip treba da se ponaša kao int (npr. veličina u bajtima, indeksiranje).

  ```python
  class OnlyIndex:
      def __index__(self): return 7
  print(int(OnlyIndex()))  # 7
  ```

- **Dunder protokol:** skup nepisanih pravila — ako pozoveš `int(x)`, Python prvo traži `x.__int__()`, ako nema → `x.__index__()`. Isto pravilo važi i za `str(x)` (traži `__str__`, pa fallback na `__repr__`).

---

### 3️⃣ `bytes` i `bytearray` (razlika, zašto postoje)

- **bytes** → **nepromenljiva** sekvenca bajtova. Izgleda kao string, ali sadrži raw vrednosti (`b"hello"`).
- **bytearray** → isto, ali **promenljiva** verzija (možeš menjati bajt po bajt).
- Kada ih koristiš sa `int()`, Python očekuje da sadrže **ASCII cifre** i da navedeš `base`.

  ```python
  int(b"2a", 16)        # 42
  int(bytearray(b"10"), 2)  # 2
  ```

💡 U praksi:

- `bytes` dobijaš iz fajlova, mrežnih paketa, enkodovanog teksta.
- `bytearray` koristiš ako moraš **da menjaš sadržaj** bez kreiranja novih objekata (npr. low-level parsiranje).

---

(Junior:) Znači kad `int("1010", 2)` dobijem decimalni 10, a `int("FF", 16)` je 255?
(Mentor:) Tako je! I sad znaš da ako ti neko pošalje `bytearray(b"10")`, to možeš da parsiraš u int samo uz `base`.

---

(Mentor:) Svaka čast što si našao **ritam i metod učenja** 👏 — to je pola posla.

### 📌 O tvom pitanju o “znanju”

- Ja **nemam trajni pristup** svim podacima o tebi, osim ako ih ti **ne upišeš u Knowledge fajl** (npr. `Knowledge/about_me.md`).
- Ako hoćeš da stalno imam kontekst “prelazim iz građevine u programiranje, cilj mi je 6–12 meseci” → stavi to u `Knowledge/` i osvežavaj.
- Tada svaki novi chat počinje sa jasnim okvirima.

---

### 🎛 ZADATAK: kako izvući maksimum iz **REPL-a**

REPL (Python prompt) je tvoj “laboratorijski sto”. Kad učiš funkcije (`int`, `str`, `abs`, …) koristi ga ovako:

#### 1) **help i docstring**

```python
help(int)
print(int.__doc__)
```

👉 odmah vidiš potpis funkcije i primer(e). Ovo ti daje “oficijelni ugovor”.

#### 2) **Jednostavni primeri**

Kreni sa “happy path”: ono što znaš da radi.

```python
int(42.9)   # 42
int("10")   # 10
```

#### 3) **Edge-case testovi**

Zatim ispituj granice i greške:

```python
int(-3.9)         # -3  (trunc prema nuli)
int("12.5")       # ValueError
int("0b101", 0)   # 5   (auto-detekcija baze)
```

👉 Ovde naučiš _šta se ne sme_.

#### 4) **Greške hvataj eksplicitno**

```python
try:
    int("bad")
except Exception as e:
    print(type(e).__name__)
```

👉 Ovako vidiš tačan tip greške (`ValueError`, `TypeError`…).

#### 5) **Eksperimenti sa custom klasama**

```python
class OnlyIndex:
    def __index__(self): return 7
print(int(OnlyIndex()))  # 7
```

👉 REPL je savršen za mikro-klase koje demonstriraju dunder protokol.

#### 6) **print + type**

Uvek gledaj i vrednost i tip:

```python
x = int("FF", 16)
print(x, type(x))  # 255 <class 'int'>
```

👉 Time potvrđuješ da dobijaš baš ono što misliš.

---

### 🧰 Mini “checklist” za REPL ispitivanje funkcije

1. `help(...)` i `.__doc__` → upoznaj se sa potpisom.
2. Normalni slučajevi (najčešća upotreba).
3. Edge-cases (negativne vrednosti, prazni stringovi, whitespace, specijalni tipovi).
4. Pogrešni ulazi (hvataj greške).
5. Custom objekti sa dunder metodama.
6. Poređenje sa sličnim funkcijama (`str()`, `repr()`, `format()`).

---

(Junior:) Znači u REPL-u je poenta ne samo da probam “radi li”, nego i da forsiram **nevalidne slučajeve** i uporedim sa dokumentacijom?
(Mentor:) Tačno 💡. To je način da učenje postane **aktivno istraživanje** — i tu se najbrže pamti.

---

(Mentor:) Odlično pitanje — to je baš praktična stvar!

### 👉 Kako ući u novi red u **REPL-u** bez pokretanja koda

U običnom Python REPL-u (kad pokreneš `python` u terminalu):

- Ako linija još **nije kompletna**, REPL automatski zna da treba novi red.
  Primer:

  ```python
  >>> for i in range(3):
  ...     print(i)
  ...     # ovde ENTER samo ide u novi red jer je blok nezavršen
  ...
  ```

  Vidiš da prompt prelazi iz `>>>` u `...`.

- Ako linija **jeste kompletna**, pritisak na **ENTER** odmah izvršava kod.
  Ako želiš da ipak nastaviš u novi red, imaš dve opcije:

  1. **Zagrade** (trik najčešće korišćen u praksi):

     ```python
     >>> x = (
     ...   1 + 2 +
     ...   3
     ... )
     >>> x
     6
     ```

     Dok si “u zagradama” `()`, `[]`, `{}`, REPL čeka da se zatvore i dopušta nove redove.

  2. **Backslash `\\`**:

     ```python
     >>> y = 1 + 2 + \
     ...     3 + 4
     >>> y
     10
     ```

---

💡 **Profesionalni savet:**
Za duže probe uvek koristi **VS Code + `python` fajl** i onda `Shift+Enter` za slanje u REPL ili Jupyter. Čist REPL je super za mini testove, ali čim ti treba više od 2–3 reda → idi u editor.

---

(Junior:) Znači ako sam u petlji ili zagradama, samo ENTER prelazi u novi red, a inače moram `\\`?
(Mentor:) Tako je! I to je jedan od prvih trikova kako da ti REPL postane udoban za duže probe.

---

Evo ga 🎉 — spreman je fajl **`repl_multiline_examples.py`** sa svim trikovima: blokovi, zagrade, backslash i multiline stringovi.

### Još par mini-saveta za REPL pre nego što odeš:

- **`_` (underscore)** u REPL-u čuva poslednji rezultat:

  ```python
  >>> 3 + 4
  7
  >>> _ * 2
  14
  ```

- **`dir(obj)`** → lista svih atributa i metoda (super za istraživanje).
- **`vars()`** i **`locals()`** → pokažu ti trenutne promenljive.
- **`exit()`** ili `Ctrl+D` → izlazak iz REPL-a.
- **Tab completion** → dopunjava imena funkcija i metoda (u IPython i većini modernih REPL okruženja).

👷‍♂️ (Mentor:) Ovo su ti osnovni alati da REPL pretvoriš u pravi mali **laboratorijski sto**.

---

Dodao sam sekciju **“REPL trikovi za svaki dan”** u tvoj checklist ✅
Sada imaš i podsetnik za underscore, `dir()`, `vars()`, multiline unos i još par sitnica.

---

(Mentor:) Hajde da rastavimo tvoj screenshot korak po korak.

---

### 1️⃣ Greška na početku

```python
dir(obj)
```

- REPL ti javlja:

```
NameError: name 'obj' is not defined
```

👉 To znači da si tražio promenljivu `obj`, ali nisi nigde definisao takvu promenljivu.
**Lekcija:** Uvek moraš proslediti nešto što postoji u memoriji (npr. `int`, `"tekst"`, ili rezultat izraza).

---

### 2️⃣ Drugi pokušaj

```python
dir(int(-10.5))
```

Šta se desilo ovde:

1. `int(-10.5)` → `-10` (jer `int()` radi **trunc prema nuli**).
2. Dakle efektivno si uradio `dir(-10)`.

---

### 3️⃣ Izlaz

`dir(-10)` ti ispisuje **sve atribute i dunder metode** tipa `int`.
Npr:

- `__add__`, `__sub__`, `__mul__` … (aritmetičke operacije)
- `__str__`, `__repr__` … (ispisivanje)
- `__abs__`, `__float__`, `__index__` … (konverzije i pomoćne metode)
- i nove “friendly” metode u Pythonu 3:

  - `.bit_count()` → broj jedinica u binarnom zapisu (`(-10).bit_count()` → 3 jer binarni zapis 1010 ima tri jedinice).
  - `.to_bytes()` / `.from_bytes()` → rad sa bajtovima.
  - `.numerator`, `.denominator`, `.real`, `.imag` → stvari koje `int` “nasleđuje” od `numbers` API-ja (int se ponaša kao racionalan broj).

---

(Junior:) Aha, znači zato je lista ogromna — to su sve metode koje Python “zna” za int?
(Mentor:) Tačno. `dir()` je kao **katalog mogućnosti** za tip. Koristi ga stalno da vidiš šta je na raspolaganju.

---

### 📝 Mini-eksperiment za tebe u REPL-u

```python
x = int(-10.5)  # -10
print(x)
print(x.bit_count())
print(x.to_bytes(2, "big", signed=True))
```

👉 Ovako testiraš neke od metoda koje si video.

---

(Mentor:) Dva super pitanja! Idemo redom:

---

## 1️⃣ Najkorisnije metode/atributi iz `dir(int)`

- **`bit_length()`**
  👉 koliko bitova treba za binarni zapis broja.

  ```python
  (10).bit_length()   # 4, jer 10 je 1010 u binarnom zapisu
  (255).bit_length()  # 8
  ```

- **`bit_count()`** (Python 3.8+)
  👉 koliko jedinica (`1`) ima u binarnom zapisu.

  ```python
  (10).bit_count()   # 2, jer 1010 ima dve jedinice
  (15).bit_count()   # 4, jer 1111
  ```

- **`to_bytes(length, byteorder, signed=False)`**
  👉 pretvara broj u sekvencu bajtova.

  ```python
  (255).to_bytes(2, "big")   # b'\\x00\\xff'
  (255).to_bytes(2, "little")# b'\\xff\\x00'
  ```

- **`from_bytes(b, byteorder, signed=False)`** (klasna metoda, pozivaš je kao `int.from_bytes`)
  👉 obrnut proces: bajtovi → int.

  ```python
  int.from_bytes(b'\\x00\\xff', "big")    # 255
  int.from_bytes(b'\\xff\\x00', "little") # 255
  ```

- **`numerator`, `denominator`**
  👉 jer se `int` ponaša i kao “rational number” (specijalizovan `Fraction`).

  ```python
  (5).numerator     # 5
  (5).denominator   # 1
  ```

- **`real`, `imag`**
  👉 jer se `int` ponaša i kao kompleksan broj gde su imaginarni deo = 0.

  ```python
  (5).real   # 5
  (5).imag   # 0
  ```

---

(Junior:) Aha, znači `int` je moćniji nego što sam mislio, ima gomilu “skrivenih” trikova!
(Mentor:) Tačno — i ovo je razlog zašto `dir()` stalno koristiš u REPL-u.

---

## 2️⃣ Šta je “numbers API”?

- **API** = _Application Programming Interface_.
  Najprostije: **ugovor** ili **set pravila** kako da pričaš sa nekom bibliotekom/klasom/servisom.
  Primer: `int()` ima API (sve metode koje nudi). `math` modul ima API (funkcije `sqrt`, `sin`, `cos`).

- **numbers API** u Pythonu → definicija kako se svi “brojoliki” tipovi (`int`, `float`, `complex`, `Fraction`, `Decimal`) treba da ponašaju.

  - `int.real`, `float.real`, `complex.real` → svi brojevi imaju `.real`.
  - `int.imag`, `float.imag` → svi imaju `.imag` (int i float daju 0, kompleksan daje pravi imaginarni deo).
  - `int.numerator` / `.denominator` → jer racionalni tipovi dele ovu logiku.

👉 Dakle, numbers API je **dogovor unutar Python standarda**: svaki broj mora nuditi iste osnovne metode/atribute, da bi ih mogao tretirati uniformno.

---

(Junior:) Dakle API je kao meni u restoranu — piše šta sve možeš da naručiš, a numbers API kaže “svaki broj mora nuditi makar real, imag, numerator, denominator”?
(Mentor:) Fenomenalna analogija 👌 baš tako. API = meni. A Python obezbeđuje da svi brojevi imaju sličan meni.

---

Dodao sam u **glossary.md** pojmove:

- **API** (opšti ugovor/metode),
- **numbers API** (standardizacija u Pythonu za sve brojolike tipove). ✅

Hoćeš da ti za sledeći REPL zadatak pripremim **mini-experimente sa `numbers API`** (npr. kako `int`, `float`, `complex` i `Fraction` svi imaju `.real`, `.imag`, `.numerator`, `.denominator`)?

---

## Dan A — int / str / bool (REPL + greške + mini pytest)

### Predložene putanje

- `labs/dayA/int_str_bool_repl.md`
- `tests/test_dayA_core_types.py`
- `Znanje/glossary.md` (dopune: truthy/falsy, **bool**, **len**)

---

### REPL plan (copy/paste blok) → `labs/dayA/int_str_bool_repl.md`

```python
# 1) int — brzi ugovor + edge + greške
help(int)
print(int.__doc__)
print(int(42.9), int(-3.9))             # 42, -3  (trunc prema nuli)
print(int("1010", 2), int("FF", 16))    # 10, 255
print(int("  42\n"))                    # 42 (whitespace OK)
try: int("12.5")
except Exception as e: print(type(e).__name__)  # ValueError
try: int(3.0, 10)
except Exception as e: print(type(e).__name__)  # TypeError

# 2) str — razlika str() / repr() / decode() + greške
help(str)
print(str.__doc__)
b = b"abc"
print(str(b))           # "b'abc'"  -> repr bytes-a
print(b.decode())       # 'abc'     -> pravi tekst
try: str(123, "utf-8")
except Exception as e: print(type(e).__name__)  # TypeError

# 3) bool — truthy/falsy + __bool__ / __len__
help(bool)
print(bool.__doc__)
print(bool(0), bool(1), bool(""), bool("0"), bool([]), bool([0]), bool(None))
class WithBool:
    def __bool__(self): return False
class WithLen:
    def __len__(self): return 2
print(bool(WithBool()))  # False (po __bool__)
print(bool(WithLen()))   # True  (po __len__)
print(bool(object()))    # True  (default objekt)
```

---

### Mini pytest skeleton → `tests/test_dayA_core_types.py`

```python
import pytest

# ---------- int ----------
@pytest.mark.parametrize("x,expected", [
    (42.9, 42),
    (-3.9, -3),
    ("10", 10),
])
def test_int_basic(x, expected):
    assert int(x) == expected

@pytest.mark.parametrize("s,base,expected", [
    ("1010", 2, 10),
    ("FF",   16, 255),
    ("0b101", 0, 5),
])
def test_int_bases(s, base, expected):
    assert int(s, base) == expected

def test_int_whitespace():
    assert int("  42\n") == 42

@pytest.mark.parametrize("bad", ["12.5", "1__0", "_1", "++10"])
def test_int_value_error(bad):
    with pytest.raises(ValueError):
        int(bad)

def test_int_type_error_when_base_with_non_text():
    with pytest.raises(TypeError):
        int(3.0, 10)

def test_int_overflow_error():
    with pytest.raises(OverflowError):
        int(float("inf"))

# ---------- str ----------
def test_str_bytes_vs_decode():
    b = b"abc"
    assert str(b) == "b'abc'"
    assert b.decode() == "abc"

def test_str_encoding_type_error():
    with pytest.raises(TypeError):
        str(123, "utf-8")

# ---------- bool ----------
@pytest.mark.parametrize("value,expected", [
    (0, False),
    (1, True),
    ("", False),
    ("0", True),
    ([], False),
    ([0], True),
    (None, False),
])
def test_bool_truthiness(value, expected):
    assert bool(value) is expected

def test_bool_dunder_precedence():
    class WithBool:
        def __bool__(self): return False
    class WithLen:
        def __len__(self): return 2
    assert bool(WithBool()) is False   # koristi __bool__
    assert bool(WithLen()) is True     # koristi __len__ ako nema __bool__

def test_bool_default_object_true():
    assert bool(object()) is True
```

Pokretanje:

```bash
pytest -q
```

---

### Glossary dopune (predlog za `Znanje/glossary.md`)

- **truthy / falsy** – vrednosti koje se tretiraju kao `True`/`False` u `if`/`while`. Prazne kolekcije, `0`, `None` su **falsy**; sve ostalo tipično **truthy**.
- **`__bool__`** – dunder metoda koju `bool(x)` poziva prva. Mora vratiti `True`/`False`.
- **`__len__`** – ako nema `__bool__`, Python koristi `__len__` (`len(x) == 0` → `False`, inače `True`).

---

### Definition of Done (Dan A)

- [ ] REPL isečci za `int/str/bool` odrađeni (happy + edge + greške).
- [ ] Pytest fajl `tests/test_dayA_core_types.py` radi (`pytest -q`).
- [ ] `Znanje/glossary.md` dopunjen: truthy/falsy, `__bool__`, `__len__`.
- [ ] Kratke beleške: šta te iznenadilo / gde je grešilo.

---

(Mentor🙂) Odlično — evo plana: napravićemo **jutarnji ritual** i odmah ću ti dati i **početni materijal za testove (pytest) u Amateur modu**.

---

# 🌅 Jutarnji ritual (svaki dan)

1. **Otvori novi chat** u okviru svog modela **ZF-14 • Amateur Mentor (Core Python)**.
2. **Priloži folder `Znanje/`** (dnevni_driver, README, glossary, plan, career_notes).
3. **Prva poruka** neka bude:

   ```
   Otvoriti Znanje/dnevni_driver.md i popuniti dnevni YAML za današnji datum.
   Phase: F1
   Focus: [core tema] + [mini-projekat]
   ```

4. Ja onda:

   - pročitam YAML iz `dnevni_driver.md`,
   - predložim dnevni tok kroz **4 bloka** (REPL, Implementacija, Testovi, Docs).

5. Kroz dan pratiš blokove.
6. Na kraju dana: wrap-up → update u `Znanje/logs/YYYY-MM-DD_chat.md`.

---

## 📌 Tvoj DoD za testove (svaki dan)

- Bar 3 testa po temi: **happy path, edge case, greška**.
- Test fajl u `tests/` folderu, ime `test_*.py`.
- `pytest -q` mora da prođe bez greške.

---

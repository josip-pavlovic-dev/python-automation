# 📖 Python Glossary (Amateur Mod)

Ovaj fajl je **pojmovni rečnik**. Svaki put kad naletimo na nepoznat termin u radu (REPL, analysis, cheatsheet, tutor), ovde ga objašnjavamo.

---

## Osnovni termini

- **REPL**
  _Read–Eval–Print Loop_. Interaktivni Python prompt (`python` u terminalu). Ukucaš izraz → odmah vidiš rezultat.

- **Dunder metode**
  Skraćeno od _double underscore_ (npr. `__str__`, `__repr__`, `__int__`). Python ih poziva iza kulisa. Primer: `int(obj)` automatski pozove `obj.__int__()`.

- **Fallback**
  Rezervni mehanizam: ako nema `__str__`, Python padne na `__repr__`. Ako nema `__int__`, može probati `__index__`.

- **repr vs str**

  - `repr(x)` → tehnički prikaz (za debug, često može da se `eval()` nazad).
  - `str(x)` → lepši, čitljiv prikaz za korisnike.

- **formatiranje**
  Kontrola ispisa (`f"{x:.2f}"`, `format(x, ".3f")`). Razlikuje se od same konverzije u string.

- **trunc prema nuli**
  Pravilo kod `int(float)` → samo odseče decimalu, ne zaokružuje.
  `int(3.9) == 3`, `int(-3.9) == -3`.

- **base (osnova)**
  Drugi parametar `int()` → u kojoj je bazi broj u stringu (`2` za binarno, `16` za hex).
  Primer: `int("FF", 16) == 255`.
  Posebno: `base=0` → Python sam prepoznaje prefiks (`0b` za binarno, `0x` za hex, `0o` za oktal).

- **underscores**
  `_` u string-ciframa za čitljivost (`"1_000" == 1000`). Ako su dupli ili na pogrešnom mestu → `ValueError`.

- **auto-detekcija (base=0)**
  Ako staviš `base=0`, Python gleda prefiks:
  `int("0x10", 0) == 16` (hex),
  `int("0b101", 0) == 5` (binarno).

---

## Tipovi grešaka

- **ValueError** → ulazni format ne valja (`int("12.5")`).
- **TypeError** → tip ne podržava operaciju (`int(None)`, `str(123, "utf-8")`).
- **OverflowError** → pokušaj konverzije beskonačnosti (`int(float("inf"))`).

---

## Dunder protokoli

- ****int****
  Ako klasa implementira ovu metodu, `int(obj)` vraća rezultat `obj.__int__()`.

- ****index****
  Fallback za integer-like objekte. Ako nema `__int__`, ali postoji `__index__`, i dalje radi `int(obj)`.

- ****str** / **repr****

  - `__str__`: lep prikaz (za korisnike).
  - `__repr__`: tehnički prikaz (za debug, serijalizaciju).

- **Dunder protokol**
  Skup pravila kako Python koristi ove magične metode. Primer: `int(obj)` → prvo traži `__int__()`, pa ako ne postoji → `__index__()`.

---

## Bytes i Bytearray

- **bytes**
  Nepromenljiva sekvenca bajtova. Koristi se za raw podatke (fajlovi, mrežni paketi). Izgleda kao string sa prefiksom `b` → `b"hello"`.

- **bytearray**
  Promenljiva verzija `bytes`. Možeš menjati elemente bez kreiranja novog objekta.

- **Upotreba sa int():**
  ```python
  int(b"2a", 16)        # 42
  int(bytearray(b"10"), 2)  # 2
  ```

---

## API pojmovi

- **API (Application Programming Interface)**
  U programiranju: skup pravila/metoda koji definiše kako razgovaraš sa klasom, bibliotekom ili servisom.
  👉 Primer: `int` ima API (njegove metode: `bit_length`, `to_bytes`…), `math` modul ima API (`sqrt`, `sin`, `cos`).

- **numbers API (Python)**
  Dogovor (standardizacija) da svi brojoliki tipovi (`int`, `float`, `complex`, `Fraction`, `Decimal`) imaju iste osnovne atribute: `.real`, `.imag`, `.numerator`, `.denominator`.
  👉 Tako svi brojevi dele zajednički “meni” metoda/atributa i mogu se tretirati uniformno.

---

✍️ **Pravilo**: Kad naiđemo na novi termin → dodaj ga ovde sa kratkim objašnjenjem i primerom.

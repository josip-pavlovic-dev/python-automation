# Dan 1 — Onboarding Juniora: mentalni model + tipovi podataka

## 1) Šta se očekuje od Juniora (realno, prvih 1–3 meseca)

**Tehnički**

- Razumeš **osnovne tipove** i kako rade u memoriji (identitet, mutabilnost).
- Pišeš **male, čiste funkcije** sa jasnim potpisima (bez „magije“ i skrivenih efekata).
- Znaš da **tražiš pomoć**: minimalni primer (MCVE), očekivano vs. dobijeno, koraci reprodukcije.
- Pokrivaš osnovne **testove** (bar pozitivan i jedan ivčni slučaj).

**Profesionalno**

- Komuniciraš **koncizno**: „Uradio sam X, zapelo na Y, probao A/B, greška Z, sledeći korak T.“
- Poštuješ **konvencije** (pep8, imenovanje, kratki commiti).
- **Vreme**: time-box (npr. 45–60 min), pa eskalacija sa konkretnim pitanjima.

**Stav**

- Radoznalost i **detaljna pitanja**: „Koji su edge slučajevi?“, „Koji je ugovor funkcije (inputs/outputs)?“
- **Doslednost**: ponovljiv proces; zapisuješ naučeno i greške za ubuduće.

---

## 2) Mentalni model Pythona (osnova svega)

### 2.1 Objekti, imena, identitet

- **Objekat** živi u memoriji; **ime** (promenljiva) je _etiketa_ koja upućuje na objekat.
- `==` poredi **vrednost** (ekvivalenciju), `is` poredi **identitet** (da li je isti objekat).
- Primer:

```py
a = [1,2]; b = a      # b i a „lepe“ istu listu (alias)
a is b  # True
a == b  # True
```

### 2.2 Mutabilnost vs. rebinding

- **Mutacija**: menja _isti objekat_ → ID ostaje isti (`list.append`, `dict.update`).
- **Rebinding**: promenljiva počne da pokazuje na _drugi objekat_ (npr. `a = a + [3]`).

```py
l = [1,2]; id(l)
l.append(3)           # mutacija
id(l)                 # isti
l = l + [4]           # rebinding (nova lista)
id(l)                 # drugačiji
```

**Junior fokus:** uvek znaš da li menjaš objekat ili menjaš _Ime → Objekat_ vezu.

### 2.3 Truthiness (istinitosna vrednost)

- „Prazno“ je **falsy**: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `range(0)`, `None`.
- Ostalo je **truthy**.
- Ne piši `if x is True:` već `if x:`.

---

## 3) Tipovi podataka — ono što zaista moraš znati

### 3.1 Skalarni i specijalni

- `int`, `float`, `bool`, `None` → **immutable**; svaka „promena“ pravi novi objekat.
- `str` → immutable; operacije (`+`, `replace`) vraćaju **novi** string.

### 3.2 Sekvence

**list** (mutable, uređena, duplikati dozvoljeni)

- koristi kada treba menjati sadržaj, redosled ili veličinu.
- Oprez: `+=` mutira, `+` pravi novu listu.

**tuple** (immutable, uređena)

- koristi za **fiksne zapise** (npr. `(status, payload)`), ili kada treba da bude **hashable** (ključ u dict-u, član seta).

**range** (immutable, lenji opseg)

- `range(start, stop, step)` ide do _pre_ `stop`.
- Efikasno za iteracije velikog broja bez alokacije liste.

**str** (već gore)

- Pazi na _encoding_ i na to da su stringovi nepromenljivi.

### 3.3 Mapiranja i skupovi

**dict** (mapa ključ → vrednost, čuva redosled umetanja)

- Ključevi moraju biti **hashable** (npr. `str`, `int`, `tuple` sa hashable elementima).
- Spajanje: `a | b` (3.9+) pravi **novi** dict; `a.update(b)` mutira `a`.

**set** (skup jedinstvenih elemenata, neuređen, mutable)

- Brza provera članstva; uklanja duplikate.
- Elementi moraju biti **hashable**.

**frozenset** (immutable set)

- Može biti **ključ u dict-u** ili član drugog seta; dobar za „zabranjene“ izmene.

### 3.4 Binarni

- `bytes` (immutable), `bytearray` (mutable) — u praksi za IO/protokole; za početak znati razliku i osnovne konverzije.

---

## 4) Iteracije i „Pythonic“ alati

**for-petlja** iterira preko _iterabla_ (sekvenca, set, dict, generator).
**enumerate(seq, start=1)** daje `(indeks, vrednost)` — izbegavaj `range(len(seq))` osim kad ti baš treba indeks nezavisno od vrednosti.
**zip(a, b)** za sinhrono iteriranje nad više kolekcija.
**comprehensions** (`[x for x in ...]`, `{k:v ...}`, `{x ...}`) — deklarativno, kraće i čitljivije.
**generatori** — `(...)` lenja evaluacija; štedi memoriju.

---

## 5) Funkcije — potpis, argumenti i posledice

**Potpis**: jasna imena parametara, podrazumevane vrednosti kad imaju smisla, tip-hintovi (pomažu ljudima i alatima).
**Podrazumevane mutable vrednosti — NE!**

```py
def bad(item, bucket=[]):  # ❌ deli stanje kroz pozive
    bucket.append(item); return bucket

def good(item, bucket=None):  # ✅ None sentinel
    bucket = [] if bucket is None else bucket
    bucket.append(item); return bucket
```

**Argumenti**: `*args`, `**kwargs` koristiti štedljivo; bolje eksplicitno navesti šta treba.
**Čist kod**: minimalni side-effects; jasno gde se mutira.

---

## 6) Opseg promenljivih (LEGB) — dovoljno za start

- **L**ocal, **E**nclosing, **G**lobal, **B**uiltins.
- `global` i `nonlocal` koristi retko; idi „parametrom unutra, return napolje“.
- Izbegavaj „tihe“ zavisnosti od globalnih promenljivih.

---

## 7) Greške i izuzeci (osnova)

- Hvataj ono što očekuješ i umeš da obradiš; ne „gutaj“ sve nasumično.
- `try/except/else/finally` — **else** kad je sve prošlo bez izuzetka; **finally** za čišćenje resursa.
- Piši poruke koje pomažu budućem tebi.

---

## 8) Kako učiti novi koncept (Senior metoda za Juniora)

**Checklist za svaki koncept**

1. **Šta je?** Jedna precizna rečenica.
2. **Kada se koristi?** 2–3 tipična slučaja.
3. **Kontra-primeri?** Kada **ne** koristiti.
4. **Mutabilnost / identitet?** Da li menja objekat ili pravi novi?
5. **Truthiness / edge slučajevi?** Šta je prazno, šta je default?
6. **Mala „do-it“ vežba:** 3 minuta — mikro primer + očekivani ishod.
7. **Test:** napiši 1–2 kratka testa (pozitivni + ivica).

**Kako postavljati pitanja Senioru**

- „Pokušao sam **A** i **B**, dobijam grešku **G**. Očekivao sam **O**. Koraci reprodukcije su **K**. Da li propuštam korak? Koji je idiomatičan način za **Z**?“
- Uvek dodaj **kratak snippet** koji se može odmah pokrenuti.

---

## 9) Mini-vežbe (možeš na telefonu, kasnije pokreni)

**(A) Klasifikacija tipova**
Za svaku stavku reci: _mutable/immutable, hashable/nehashable_ i da li je **truthy/falsy** u datom stanju:

- `[]`, `()`, `{}`, `set()`, `frozenset()`, `""`, `" "`, `0`, `1`, `range(0)`, `range(1)`, `("a", 1)`, `["a", 1]`

**(B) Mutacija vs. rebinding — predvidi ishod**

```
a = [1,2]; b = a; a.append(3)
# 1) a je?
# 2) b je?
# 3) a is b ?

c = [1,2]; d = c; c = c + [3]
# 4) c je?
# 5) d je?
# 6) c is d ?
```

**(C) Dict & set — hash pravila**

- Da li može `{{1,2}}` u set? Zašto ne? Kako radi `set([frozenset({1,2})])`?

**(D) enumerate/zip — prepisati „C stil“**
Pretvori:

```py
names = ["Ana", "Marko", "Iva"]
for i in range(len(names)):
    print(i+1, names[i])
```

u idiomatski kod sa `enumerate(names, start=1)`.

**(E) Comprehensions**

- Napiši listu kvadrata `1..10` comprehension-om i set parnih.

---

## 10) „Run later“ (sačuvaj za PC)

- Napravi fajl `tests/test_types_basics.py` i napiši testove za (A) i (B).
- Uvedi `pytest` i pusti `pytest -q -k "types_basics"`.

---

## 11) Kako izgleda napredak posle 2 nedelje (realna očekivanja)

- Znaš da **odabereš tip** koji odgovara problemu (npr. `set` za članstvo, `tuple` za fiksne parove).
- Pišeš **funkcije bez skrivenih mutacija**, razumeš default argument zamku.
- Umeš da **reprodukuješ bug** uz minimalan primer i napišeš mali test koji ga hvata.
- Dosledno koristiš **enumerate/zip/comprehensions** za čitljiv kod.
- Znaš da napraviš **mali modul** sa 2–3 funkcije, tip-hintovima i kratkim testom.

---

# Plan za sutra — Dan 2 (ako ti odgovara ovaj tempo)

- **`pathlib` i rad sa putanjama**: kreiranje direktorijuma, rad sa ekstenzijama, validacije, cross-platform razlike.
- **Vežbe**: mini util funkcije za fajl sisteme + testovi sa `tmp_path`.

---

Odlično. Krenućemo „kao na obuci“ i napravićemo **temeljni sistem za pisanje funkcija** — тако да svaki sledeći zadatak možeš da razložiš mirno i precizno. Radićemo u „amateur modu“: senior objašnjenja + mini-zadaci + checkliste. (Logger sada ignorišemo.)

---

# 1) Šta je dobra funkcija? (mentalni model za Juniora)

**Dobra funkcija** je mali ugovor: _„Ako mi daš X, vratiću ti Y, uz ova pravila i bez neočekivanih sporednih efekata.“_

- **Jedna odgovornost**: radi _jednu stvar_ jasno i potpuno.
- **Jasan potpis**: ime + parametri + povratna vrednost (tip-hintovi pomažu).
- **Predvidljivo ponašanje**: isti ulaz → isti izlaz (osim kad je svesno „akcija“: IO, vreme, mreža).
- **Bez skrivenih iznenađenja**: nema tajnih mutacija ulaznih objekata, nema globalnih zavisnosti.
- **Testabilna**: možeš je proveriti sa 2–5 malih testova.

---

# 2) Anatomija funkcije (od glave do pete)

## 2.1 Ime i uloga

- **Glagol + imenica** za akcije: `load_users`, `write_report`.
- **Imenica/imenica+glagol** za transformere: `to_slug`, `normalize_email`.
- Ako ime ne možeš da sročiš jasno → funkcija radi previše.

## 2.2 Potpis (parametri i poredak)

Pravila koja te štite:

- **Ulazni „core data“ prvo**, opcije posle (po mogućnosti _keyword-only_).
- Izbegni mešanje: to što je opciono → _keyword-only_.

```python
def safe_div(a: float, b: float, /, *, default: float | None = None) -> float | None:
    """Vrati a/b ili default ako je b == 0."""
    return a / b if b != 0 else default
```

- `/` → čini parametre **pozicionim-only** (ne mogu se proslediti imenom).
- `*` → sve posle su **keyword-only** (moraš ih imenovati).
  Ovo sprečava greške i dokumentuje namenu parametara.

## 2.3 Podrazumevane vrednosti

- **Nikad mutable default!**
  Loše: `def add(x, acc=[]): ...`
  Dobro: `def add(x, acc=None): acc = [] if acc is None else acc`
- Ako je default „nema vrednosti“ → koristi `None` (ili sopstveni `Sentinel` za naprednije slučajeve).

## 2.4 Tip-hintovi (pomognu tebi i VS Code-u)

- Osnovno: `int`, `float`, `str`, `bool`, `None`, `list[str]`, `dict[str, int]`.
- Unije: `str | None` (umesto `Optional[str]`).
- Za „sekvencu samo za čitanje“ koristi apstraktne tipove: `Sequence[str]`, `Mapping[str, int]`.

## 2.5 Docstring (ugovor u 3 reda)

- 1. **Jedna rečenica** (imperativ): šta funkcija radi.
- 2. **Args/Returns** (kratko).
- 3. **Edge slučajevi** ili primer.

```python
def coalesce(*values: object, default: object | None = None) -> object | None:
    """Vrati prvi truthy iz values ili default ako ga nema.

    Primer:
        coalesce("", 0, None, "ok") -> "ok"
    """
    for v in values:
        if v:
            return v
    return default
```

## 2.6 Povratna vrednost i greške

- Doslednost: **ne** mešaj tipove (npr. nekad `int`, nekad `str`), osim ako je svesno i dokumentovano.
- EAFP vs LBYL: „**Easier to Ask Forgiveness than Permission**“ u Pythonu znači:

  ```python
  try:
      return a / b
  except ZeroDivisionError:
      return default
  ```

  Za javne API-je uradi i minimalnu validaciju ulaza (jasan `TypeError` pomaže korisniku).

## 2.7 Mutacija vs. povratna nova vrednost

- Jasno odluči: **mutiraš li** ulaz (npr. listu) ili **vraćaš novu**?
  Ako mutiraš – napiši to **u docstringu** i testiraj `id()` pre/posle.

---

# 3) Ritual pisanja funkcije (7 koraka)

1. **Jednolinijski opis**: šta tačno vraća?
2. **Primer ulaz/izlaz**: 2 normalna, 1 ivica (prazno, 0, None).
3. **Potpis**: ime + poredak + keyword-only opcije + tipovi.
4. **Docstring**: kratak, jasan, sa primerom.
5. **Skelet**: telo sa `pass` ili minimalom.
6. **Testovi (mentalno ili zapisano)**: šta treba da prođe/padne.
7. **Implementacija**: male granice; _guard clause_ rani izlazi; nema skrivenih efekata.

---

# 4) Šabloni (koje ćeš stalno koristiti)

## 4.1 Transformer (čista funkcija)

```python
def to_slug(text: str, /, *, max_len: int | None = None) -> str:
    """Pretvori tekst u 'slug' (mala slova, '-' umesto razmaka, bez spec. znakova)."""
    t = text.strip().lower()
    # (ovde normalizacija unicode, zamene itd.)
    if max_len is not None:
        t = t[:max_len]
    return t
```

**Obaveze**: nema IO, nema mutacija argumenata, deterministična.

## 4.2 Validator

```python
def ensure_non_empty(s: str, /) -> str:
    """Vrati s ako nije prazan, inače baci ValueError."""
    if not s:
        raise ValueError("Prazan string nije dozvoljen.")
    return s
```

**Obaveze**: ili vrati validno ili jasno „pukni“.

## 4.3 Akcija (IO)

```python
from pathlib import Path

def write_text(path: Path, content: str, /, *, encoding: str = "utf-8") -> Path:
    """Upiši content u fajl i vrati putanju."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)
    return path
```

**Obaveze**: idempotentno koliko može; evidentni sporedni efekti (fajl sistem).

## 4.4 Fabrika (pravljenje objekata/konfiguracija)

```python
def make_counter(start: int = 0):
    """Vrati funkciju koja broji od start naviše (closure)."""
    n = start
    def inc(step: int = 1) -> int:
        nonlocal n
        n += step
        return n
    return inc
```

**Obaveze**: jasno stanje; nema globala.

---

# 5) Antipaterni (signali da treba prepravka)

- Previše parametara (5–6+) → verovatno deliš funkciju na dve (ili uvodiš `dataclass`/config objekat).
- Mutable default (npr. `[]`, `{}`) → uvek `None` sentinel.
- Nečitljivi uslovi: `if a is not None and len(a) > 0 and b != ""` → koristi **truthiness**: `if a and b:`.
- Hvatanje „sve i svašta“: `except Exception:` → hvataj konkretno.
- Mešanje odgovornosti: parsiraš, validiraš, pišeš u fajl, formatiraš — _razdvoji u 2–3 funkcije_.
- Nekonzistentni povratni tipovi (čas `str`, čas `None`) bez jasne politike.

---

# 6) Mini-vežbe (na papiru/telefonu, implementiraš sutra)

> **Napomena:** koncipirano tako da ti ritual „legne u ruke“. Uz svaku — smisli 2 normalna i 1 ivicu.

### (1) `strip_or_none`

```python
def strip_or_none(s: str | None, /) -> str | None:
    """Vrati s bez okolnih praznina; ako je s None ili prazan rezultat, vrati None."""
    ...
```

- Edge: `None`, `"   "`, `"  A  "`.

### (2) `parse_int`

```python
def parse_int(s: str, /, *, default: int | None = None) -> int | None:
    """Pokušaj int(s); ako ne može, vrati default umesto izuzetka."""
    ...
```

- Edge: `" 42 "`, `"0042"`, `"x42"`.

### (3) `chunk`

```python
from collections.abc import Sequence

def chunk(seq: Sequence[int], /, *, size: int) -> list[list[int]]:
    """Podeli sekvencu u podliste fiksne dužine size (poslednja može biti kraća)."""
    ...
```

- Edge: `size=1`, `size>len(seq)`, `size<=0` (odluči: ValueError ili posebna politika).

### (4) `unique_everseen`

```python
from collections.abc import Iterable

def unique_everseen(items: Iterable[str], /) -> list[str]:
    """Vrati prvi put viđene stringove, redosled očuvan."""
    ...
```

- Savet: koristi `set()` za „viđeno“.

### (5) `median`

```python
def median(nums: list[float], /) -> float:
    """Vrati medijanu; baci ValueError za praznu listu."""
    ...
```

---

# 7) Kako da proveriš sopstveni rad (1-min „review“)

- **Ime** jasno saopštava šta radi.
- **Potpis**: core data → keyword-only opcije; nema mut. defaulta.
- **Docstring**: kratko + jedan primer.
- **Edge** slučajevi pokriveni (prazno, None, 0, whitespace).
- **Povratna vrednost** konzistentna i dokumentovana.
- **Nema skrivenog IO** (osim ako je funkcija upravo IO).

---

# 8) „Run later“ (sutra na računaru)

Napravi `tests/test_functions_basics.py` i za svaku vežbu napiši po 2–3 testa.
Pokreni: `pytest -q -k "functions_basics"`

Ako želiš, sledeći korak (odmah posle ovoga) je da ti pripremim **mini „practice pack — Functions 101“** sa skeletima i pytest testovima, kao što smo radili pre — samo reci: **„Da, practice pack za funkcije“**.

---

## Q\&A (kako da razmišljaš dok pišeš funkciju)

- **Koja je jedina odgovornost ove funkcije?** Ako su dve — podeli.
- **Šta su edge vrednosti?** (prazno, None, 0, whitespace, duplikati…)
- **Da li treba da mutiram ulaz?** Ako ne moraš — vrati novu vrednost.
- **Kako će korisnik znati da je nešto pošlo po zlu?** (izuzetak vs. default)
- **Može li se potpis pojednostaviti keyword-only parametrima?**
- **Mogu li dodati primer u docstring?** (dokaz razumevanja i buduća dokumentacija)

---

Fenomenalno. Krećemo „kao prvi dan obuke“ i temeljno prelazimo **3.1 Skalarni i specijalni tipovi podataka**: `int`, `float`, `complex`, `bool`, `NoneType`. (O **stringu** ćemo detaljno kasnije u delu o sekvencama — za sada samo kratke napomene.)

U „amateur modu“ dobićeš: mentalni model → pravila → tipične greške → mini-vežbe i „run later“ zadatke koje ćeš sutra pokrenuti na računaru.

---

# 3.1 Skalarni i specijalni tipovi

## A) `int` — celobrojne vrednosti (immutable)

**Mentalni model**

- Neograničena preciznost (nema overflow kao u C-u; Python menja internu reprezentaciju po potrebi).
- Ne menja se „na mestu“: svaka operacija pravi **novi objekat** (immutable).

**LiteraIi i osnove**

```py
x = 42           # decimal
y = 0b101010     # binarni
z = 0o52         # oktalni
w = 0x2A         # heksadekadni
```

**Operatori i korisne funkcije**

- Aritmetika: `+ - * // % **`
- `//` (celobrojno deljenje), `%` (ostatak), `divmod(a,b)` → `(a//b, a%b)`
- `abs`, `pow(a, b, mod)`, `round` (ali `round` radi nad `float`; za `int` je trivijalno)

**Tipične greške**

- Mešanje `//` i `/` (drugačiji rezultat tipa: `//` daje `int`, `/` daje `float`).
- Oslanjanje na interni „small-int cache“ (npr. poređenja identiteta `is` za male brojeve). **Nikad ne koristi `is` za brojeve** — koristi `==`.

**Mini-vežba**

- Napiši `int_divmod(a, b)` koji vraća string: `"q=..., r=..."` koristeći `divmod`.
- Predvidi ishod: `5 // 2 == ?`, `5 / 2 == ?`, `-3 // 2 == ?` (oprez: za negativne važe pravila zaokruživanja nadole).

---

## B) `float` — realne vrednosti sa pokretnim zarezom (immutable)

**Mentalni model**

- IEEE 754 binarni `double` → **decimalni brojevi nisu uvek tačno reprezentovani**.
- Posledice: `0.1 + 0.2 != 0.3` (dobijaš mali binarni „šum“).

**Kritične tačke**

- Poređenje: **ne** radi `a == b` za izračunate `float` vrednosti; koristi toleranciju.

```py
import math
math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-09, abs_tol=0.0)  # True
```

- Specijalne vrednosti: `float('inf')`, `float('-inf')`, `float('nan')` (NaN nije jednako ni samom sebi: `float('nan') != float('nan')` → za detekciju koristi `math.isnan`).
- Za **novac** koristi `Decimal`, za **tačne razlomke** `Fraction` (vidi „Run later“).

**Mini-vežba**

- Napiši `safe_mean(xs)` koji vraća aritmetičku sredinu i koristi `math.fsum(xs)` zbog manje greške sabiranja.

---

## C) `complex` — kompleksni brojevi (immutable)

**Mentalni model**

- Ima realni i imaginarni deo (`a + bj`), gde je `j` imaginarna jedinica.

```py
z = 3 + 4j
z.real == 3.0
z.imag == 4.0
abs(z) == 5.0  # modul
```

- Koristan u naučnim domenima; za opštu automatizaciju ređe, ali treba znati sintaksu.

**Tipične greške**

- Pokušaj da `complex` pretvoriš direktno u `int` ili `float` (nije dozvoljeno bez uzimanja dela).

**Mini-vežba**

- `norm(a: complex) -> float` koji vraća `abs(a)` i testira nekoliko primera.

---

## D) `bool` — logičke vrednosti (immutable, **podklasa** `int`)

**Mentalni model**

- `True` i `False` su **podklase `int`**: `True == 1`, `False == 0`.
  To je korisno (sabiranje booleana), ali i opasno (mešanje tipova u mapama).

```py
sum([True, False, True])  # 2
isinstance(True, int)     # True
```

**Pravila**

- U uslovima koristi **truthiness** (`if x:`), ne `if x is True:`.
- Za poređenje sa `None` koristi **`is None`/`is not None`**, ne `==`.

**Tipične greške**

- Korišćenje `True`/`False` kao ključeva u `dict` zajedno sa `1`/`0` — sudaraju se (`True` i `1` mapiraju na isti hash/ekvivalentnost).

**Mini-vežba**

- Napiši `count_truthy(xs)` koji broji truthy elemente: `sum(bool(x) for x in xs)` (ili `sum(map(bool, xs))`).
- Predvidi ishod: `bool("")`, `bool(" ")`, `bool([])`, `bool([0])`.

---

## E) `NoneType` — jedinstveni objekat „nema vrednosti“

**Mentalni model**

- **Singleton**: postoji **jedan** objekat `None`. Poredi se **identitetom**: `is None`.
- Signalizira: „nema podatka“, „nije izračunato“, „prazan rezultat“, „default nije prosleđen“.

**Pravila**

- Potpisi funkcija: koristi `x: int | None = None` kada parametar može nedostajati.
- Provera: `if x is None:` ili `if x is not None:`.
- **Ne** koristi `== None` ni `!= None`.

**Tipične greške**

- Mešanje `None` i falsy vrednosti: `0`, `""`, `[]` su falsy, ali **nisu `None`**. Ne tretirati ih kao isto.

**Mini-vežba**

- Napiši `first_non_null(*xs)` koji vraća **prvu vrednost koja nije `None`** (ne „prvi truthy“).
- Test slučaj: `first_non_null(None, "", 0, "ok")` treba da vrati `""` (jer je prvi ne-None).

---

## Konverzije i koegzistencija tipova

**`int()`, `float()`, `bool()`, `complex()`**

- `int("42")` → 42; `int(3.9)` → 3 (odseca, ne zaokružuje).
- `float("2.5")` → 2.5; `bool("0")` → **True** (prazan string je False; bilo koji neprazan je True).
- `complex(3)` → `(3+0j)`, `complex("3+4j")` → `(3+4j)`.

**Pravila za svaki dan**

- Poredi **iste tipove** kada je moguće (manje iznenađenja).
- Za `float` koristi toleranciju (`math.isclose`).
- Za `None` koristi `is`/`is not`.

---

## Tipične zamke i kako ih instinktivno izbeći

1. **Poređenje `float` ekvivalencijom**
   – Umesto `a == b`, koristi `math.isclose(a, b, ...)`.

2. **Korišćenje `is` umesto `==` za vrednosti**
   – `is` je za **identitet** (isti objekat), **ne** za jednakost vrednosti.

3. **Mešanje `None` i praznine**
   – `None` je „nema vrednosti“, prazno je „vrednost postoji, ali je prazna“.

4. **Oslanjanje na implicitne konverzije**
   – Budi eksplicitan: `int(x)`, `float(x)`, `bool(x)` kad god ima smisla.

5. **Bool kao int**
   – Dopušteno je i korisno (`sum` nad uslovima), ali **ne** koristi `True/False` kao ključeve gde se pojavljuju i `1/0`.

---

## „Amateur mod“ — pitanja koja treba da postavljaš sebi

- **Šta je prirodno stanje tipa?** (mutabilnost, identitet, truthiness)
- **Koji su mi edge slučajevi?** (npr. `0`, `""`, `None`, `NaN`)
- **Kada je sigurno poređenje?** (`is` vs `==`, tolerancija za `float`)
- **Treba li mi preciznost izvan `float`-a?** (koristi `Decimal`/`Fraction`)
- **Šta očekuje moj API?** (vrati `None` ili baci izuzetak; eksplicitne konverzije)

---

## Mini-zadaci (zapiši sada, pokreni sutra)

1. **`safe_div(a, b)`**

   - Vrati `None` ako je `b == 0`, inače `a / b` (float).
   - Test: `assert safe_div(1,0) is None`, `math.isclose(safe_div(1,4), 0.25)`.

2. **`first_non_null(*xs)`**

   - Kao gore. Test sa `("", 0)` da pokaže razliku `None` vs falsy.

3. **`count_truthy(xs)`**

   - Vrati broj truthy elemenata. Testiraj sa `["", " ", [], [0], 0, 1]`.

4. **`float_equal(a,b,eps=1e-9)`**

   - Upotrebi `math.isclose`. Dodaj test sa `0.1 + 0.2` i `0.3`.

5. **`norm(z: complex) -> float`**

   - Vrati `abs(z)`. Testiraj Pytagorin primer `(3+4j)`.

**Run later (PC)**

```bash
pip install pytest
pytest -q -k "safe_div or first_non_null or count_truthy or float_equal or norm"
```

---

## Dodatno (za ambiciozno sutra, 10–15 min)

- **`decimal.Decimal`** – za finansije: preciznost, `getcontext().prec`, `quantize`.
- **`fractions.Fraction`** – tačni razlomci (`Fraction(1, 3) + Fraction(1, 6) == Fraction(1, 2)`).

---

### Kratka kontrolna lista (prvi dan)

- [ ] Razlikujem `==` i `is` i znam kada se koristi koji.
- [ ] Znam da je `bool` podklasa `int` i svestan sam posledica.
- [ ] Znam razliku `None` ↔ falsy vrednosti.
- [ ] Za `float` koristim toleranciju (`isclose`).
- [ ] Ne oslanjam se na „interna“ ponašanja (small-int cache, interning).
- [ ] Razumem da su svi gore tipovi **immutable** (svaka „promena“ → novi objekat).

---

Ako ti odgovara tempo i stil, sledeći korak (**Dan 2**) su **„Stringovi — tekst i kodiranje“**: literali, slicing, unicode, nevidljivi karakteri, normalizacija, formatiranje (`f"..."`, `.format`, `%`), i mini-vežbe sa parsiranjem. Želiš da nastavimo tim redom?

---

Razumem blokadu. Greška `ModuleNotFoundError: No module named 'src'` nastaje jer pri tvom pozivu `pytest -q tests/test_exercises_day01.py` pytest postavlja **rootdir** na `tests/`, pa `src/` (sused) nije na `sys.path`. Test fajl zaista uvozi `from src.basics.exercises_day01 import ...` i pada već u importu.&#x20;
Preporučeni način pokretanja testova u našem skeletu je iz **korena modula** (tj. `labs/zero_foundations/`), bez navođenja putanje fajla: `pytest` ili `python -m pytest`. &#x20;

## Brzi fix (izaberi jednu od varijanti)

### Varijanta A — Preporučeno (nema “putanja do fajla”)

```bash
# iz labs/zero_foundations/
python -m pytest -q          # svi testovi
python -m pytest -q -k exercises_day01   # samo testovi iz tog fajla
```

### Varijanta B — Ako baš želiš da navedeš fajl (dodaj PYTHONPATH)

```bash
# Git Bash / WSL
PYTHONPATH=. pytest -q tests/test_exercises_day01.py

# PowerShell
$env:PYTHONPATH='.'; pytest -q tests/test_exercises_day01.py
```

### Varijanta C — Stabilno za male projekte: `conftest.py` doda koren na `sys.path`

Kreiraj `labs/zero_foundations/tests/conftest.py` sa:

```python
#ENG: Ensure project root on sys.path so imports like `src.*` work
#SR : Dodaj koren projekta na sys.path da `src.*` importi rade
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

Posle toga običan `pytest -q` ili čak `pytest -q tests/test_exercises_day01.py` radi pouzdano.

## Mini-check (opciono, za proveru okruženja)

```bash
# prikaži kako pytest vidi rootdir i sys.path[0]
python - << "PY"
import sys, os
print("CWD =", os.getcwd())
print("sys.path[0] =", sys.path[0])
PY
```

## Zašto ovo rešava problem

- Testovi importuju iz `src.*` (tako piše u test fajlu).&#x20;
- Naš “How to run” očekuje pokretanje iz `labs/zero_foundations/` (tada je koren na `sys.path`).&#x20;
- U **A** to obezbeđuje `python -m pytest`; u **B** ručno dodaješ `.` u putanju; u **C** to radi automatski kroz `conftest.py`.

---

## Šta sada uraditi (2 koraka)

1. U `labs/zero_foundations/` pokreni:
   `python -m pytest -q -k exercises_day01`
   (očekujem zeleno jer si TODO-e u `exercises_day01.py` već popunio).&#x20;
2. Ako želiš da ostaneš na komandama sa putanjom fajla, dodaj `conftest.py` iz Varijante C pa probaj:
   `pytest -q tests/test_exercises_day01.py`.

---

Odlično 👌
Spremi se — pravićemo **scratch/day01_playground.py** koji će biti **laboratorija** za testiranje svih funkcija iz `exercises_day01.py`.
Biće obiman, sa dosta primera (truthiness, countdown, enumerate, edge-case scenariji).

---

## `scratch/day01_playground.py`

```python
#ENG: Run with "python -m scratch.day01_playground" from project root
#SR : Pokreni sa "python -m scratch.day01_playground" iz korena projekta

from src.basics.exercises_day01 import is_empty, countdown, enumerate_1


def demo_truthiness():
    print("=" * 40)
    print("TRUTHINESS DEMO")
    values = [0, 0.0, "", [], {}, set(), None, [1], "tekst", 42]
    for v in values:
        print(f"Value={repr(v):>8} | bool(v)={bool(v)} | is_empty(v)={is_empty(v)}")
    #ENG: empty/falsy → bool(v)=False, is_empty(v)=True
    #SR : prazno/falsy → bool(v)=False, is_empty(v)=True


def demo_countdown():
    print("=" * 40)
    print("COUNTDOWN DEMO")
    for n in [5, 3, 1]:
        print(f"countdown({n}) -> {countdown(n)}")
    #ENG: range(n,0,-1) stops before 0
    #SR : range(n,0,-1) staje pre 0

    # Edge cases
    try:
        print("countdown(0):", countdown(0))
    except Exception as e:
        print("Error with countdown(0):", e)

    try:
        print("countdown(-3):", countdown(-3))
    except Exception as e:
        print("Error with countdown(-3):", e)


def demo_enumerate_1():
    print("=" * 40)
    print("ENUMERATE_1 DEMO")
    xs = ["a", "b", "c"]
    print("Input:", xs)
    print("enumerate_1(xs):", enumerate_1(xs))

    # Nested enumerate
    words = ["Python", "Automation", "Day01"]
    for idx, word in enumerate_1(words):
        print(f"{idx}: {word}")

    # Empty list
    print("enumerate_1([]):", enumerate_1([]))

    # Enumerating over range
    print("enumerate_1(range(3)):", enumerate_1(range(3)))


def demo_combinations():
    print("=" * 40)
    print("COMBINED USAGE DEMO")

    # Filter non-empty values with enumerate_1
    items = ["", "X", [], [1, 2], None, "ok"]
    print("Original items:", items)
    filtered = [(i, x) for i, x in enumerate_1(items) if not is_empty(x)]
    print("Filtered (non-empty):", filtered)

    # Countdown + enumerate
    n = 5
    cd = countdown(n)
    print(f"Countdown list for n={n}:", cd)
    indexed = enumerate_1(cd)
    print("Enumerated countdown:", indexed)

    # Realistic: validate fields
    user_inputs = {"name": "Ana", "email": "", "age": 0}
    print("User inputs:", user_inputs)
    empties = [k for k, v in user_inputs.items() if is_empty(v)]
    print("Empty fields:", empties)


def demo_matrix_enumeration():
    print("=" * 40)
    print("MATRIX ENUMERATION DEMO")
    matrix = [
        [1, 2, 3],
        [4, 5],
        [],
        [6]
    ]
    for row_idx, row in enumerate_1(matrix):
        if is_empty(row):
            print(f"Row {row_idx} is empty")
            continue
        for col_idx, value in enumerate_1(row):
            print(f"Row {row_idx}, Col {col_idx}: {value}")


def main():
    demo_truthiness()
    demo_countdown()
    demo_enumerate_1()
    demo_combinations()
    demo_matrix_enumeration()


if __name__ == "__main__":
    main()
```

---

## Šta dobijaš ovim playground-om

1. **Truthiness laboratorija** – sve tipične vrednosti (0, "", \[], None, itd.), sa poređenjem `bool(v)` i `is_empty(v)`.
2. **Countdown edge-cases** – normalni pozivi + `0` i negativni brojevi (pokazuju gde funkcija puca).
3. **Enumeracija** – obična lista, prazna lista, enumerate preko `range`.
4. **Kombinacije** – filter praznih vrednosti iz liste; countdown + enumerate; validacija korisničkog inputa.
5. **Matrica** – dvodimenzionalna lista sa `enumerate_1` za redove i kolone, uključujući prazne redove.

---

## Kako pokrenuti

```bash
# iz korena projekta
python -m scratch.day01_playground
```

Dobijaš **detaljan ispis** na konzoli, dovoljno obiman da proveriš sve funkcije u različitim scenarijima.

---

Hoćeš li da ti odmah pripremim i **pytest testove za playground** (npr. snapshot testovi izlaza), ili želiš da ovaj fajl ostane samo interaktivni poligon za ručno igranje?

---

Odlično, Jole — super vest za struju i još bolja odluka da **u ovom chatu** radimo plan, a da **u ZF-14** sprovodiš kod i testove. To je baš u duhu našeg Dan-1 onboarding-a koji smo zapisali (pogledaj „šta se očekuje od Juniora“).&#x20;

# 1) Struktura: mogu li skripte i testovi u `labs/zero_foundations/`?

Da. Pytest će raditi bez problema **ako je „root projekta“ tamo gde je tvoja pytest konfiguracija**.

## Minimalna, pouzdana postavka (preporuka – „src layout“)

```
labs/zero_foundations/
├─ src/
│  └─ <tvoj_paket>/
│     ├─ __init__.py
│     └─ ... .py
├─ tests/
│  └─ test_*.py
└─ pyproject.toml   # pytest config (testpaths, itd.)
```

### a) Gde pokrećeš pytest

- Iz tog foldera:

  ```bash
  cd labs/zero_foundations
  pytest -q
  ```

- Ako pokrećeš iz _workspace_ korena, naglasi putanje:

  ```bash
  pytest labs/zero_foundations/tests -c labs/zero_foundations/pyproject.toml
  ```

### b) Da testovi uvoze kod iz `src/`

Izaberi **jednu** od sledeće 3 opcije:

**Opcija 1 (najjednostavnije): privremeni PYTHONPATH**

- Linux/macOS:

  ```bash
  cd labs/zero_foundations
  export PYTHONPATH=$PWD/src
  pytest -q
  ```

- Windows (PowerShell):

  ```powershell
  cd labs/zero_foundations
  $env:PYTHONPATH="$pwd\src"
  pytest -q
  ```

**Opcija 2 (VS Code):**
U `.vscode/settings.json` dodaj:

```json
{
  "python.analysis.extraPaths": ["./src"]
}
```

**Opcija 3 (produkcijski ispravno): „editable install“**
Napravi paket (npr. `src/zero_foundations/__init__.py`) i uradi:

```bash
pip install -e labs/zero_foundations
```

Tada testovi rade sa `import zero_foundations...` bez PYTHONPATH trikova.

> Konvencije pytest-a: `tests/`, imena fajlova `test_*.py`, funkcije `test_*`. U `pyproject.toml` (ili `pytest.ini`) postavi:
>
> ```toml
> [tool.pytest.ini_options]
> testpaths = ["tests"]
> python_files = ["test_*.py", "*_test.py"]
> ```
>
> i pokretanje će biti predvidivo.

---

# 2) Krećemo da PIŠEMO funkcije sada (bez teorijskog „plivanja”)

Predlažem sledeći mikro-ritual u VS Code-u (trajaće 10–15 min):

1. Otvori **practice pack – tipovi** (link ispod), uđi u:
   `practice_pack_types/src/types_scalars.py`
2. Implementiraj **samo** prvu funkciju `safe_div(...)`.
   Pravila: jasan potpis, bez skrivenih efekata, napiši i kratak docstring.
3. Pokreni samo vezane testove:

   ```bash
   cd practice_pack_types
   pytest -q -k "safe_div"
   ```

4. Tek kada je to zeleno, pređi na `float_equal(...)`, pa `norm(...)`, itd.

Ako zapneš kod _bilo koje_ funkcije: pošalji **snipet** (5–15 linija) + šta si očekivao + šta dobijaš. Radićemo „senior + junior“ ping-pong.

---

# 3) „Ulazna poruka“ ako ikada poželiš da izdvojiš novi chat (spremljeno za copy-paste)

> **Naslov:** ZF-14 — Amateur mod (Senior + Junior)
> **Poruka:**
> „Ćao! Krećemo _amateur mod_ (ti si i Senior mentor i iskusni Junior). Tempo: **jedna oblast → 1–2 dana** (teorija + kod).
> Fokus odmah na **pisanje funkcija** i pytest testove. Molim te:
>
> 1. drži se **src layout-a** (`src/` + `tests/`),
> 2. pojašnjavaj **svaku liniju koda** kada prvi put koristimo pojam,
> 3. daj mini-zadate i proveri razumevanje pitanjima,
> 4. Definition of Done: testovi prolaze, kratki docstring, nema skrivenih mutacija.
>    Evo početnog plana i zadataka (prilažem ZIP practice packove). Kreni od implementacije `safe_div`, pa `float_equal`… i vodi me korak-po-korak.“

---

# 4) Linkovi — oba practice packa spremna

- **Practice pack — Tipovi (skalarni/specijalni)**
  [Preuzmi ZIP](sandbox:/mnt/data/practice_pack_types.zip)
- **Practice pack — Truthiness/Range/Enumerate/Mutacija**
  [Preuzmi ZIP](sandbox:/mnt/data/practice_pack_truthiness_range_enumerate_mutation.zip)

---

# 5) Kratak plan za sledeća 2 dana

- **Danas**: implementiraj `safe_div`, `float_equal`, `norm` i pokreni ciljane testove (`-k`).
- **Sutra**: `first_non_null`, `count_truthy`, `parse_int`, pa pređemo na **3.2 Sekvence (str/list/tuple/range)** sa novim pack-om.

Ako želiš, mogu ti odmah dati **kontrolnu listu za commit** i tipičnu poruku commita, pa odradimo prvi „zeleni“ commit čim `safe_div` prođe.

---

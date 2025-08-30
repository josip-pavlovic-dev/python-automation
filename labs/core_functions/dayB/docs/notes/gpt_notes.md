Hvala ti na otvorenosti — idemo polako i jasno. Mogu da se spustim na **veoma** nizak nivo objašnjavanja i da te za mesec dana dovedem do znanja na koje možeš da se osloniš. Radićemo “kroz testove”: svaki test je **ugovor** (ulaz → očekivanje). Kroz njih ćeš naučiti list/dict/len, mutabilnost, slicing, kopije, hashability i membership.

Prvo da **sredimo crveni test** i očistimo kod, pa onda krećemo sa učenjem “liniju po liniju”.

---

## 0) Zašto test puca (jasno i ljudski)

- Imaš **ugnežđenu listu**: `a = [[[1, 2]], [3]]`.

  - `a[0]` je `[[1, 2]]` (lista)
  - `a[0][0]` je `[1, 2]` (lista)
  - `a[0][0][0]` je `1` (broj/int)

- Test očekuje da **funkcija izmeni najdublji levi element** na `-1`, pa asertira:

  ```python
  assert a[0][0][0] == -1
  ```

- Greška `TypeError: 'int' object is not subscriptable` znači: negde si **pre** ovog asertovanja pretvorio listu u broj, pa Python pokušava da indeksira **broj** (što ne postoji). Tipično se desi ako funkcija stavi `-1` umesto celog unutrašnjeg niza pa `a[0][0]` postane `-1`, a onda `a[0][0][0]` puca.

**Cilj:** funkcija mora da menja **najdublju listu**: `a[0][0][0] = -1`, **ne** `a[0][0] = -1`.

---

## 1) Očisti test fajl (veoma važno)

U tvom `tests/test_dayB_collections.py` se **slučajno našla definicija** `mutate_nested_sample(...)`. Test ne sme da sadrži implementaciju funkcije – **samo uvoz** iz produkcionog modula.

**Treba da ostane samo ovo (copy/paste):**

```python
import copy
import pytest
from dayB.dayB_collections import make_copy, mutate_nested_sample

# ==== LIST kopije (shallow vs deep) ====

def test_list_slice_is_shallow():
    a = [[1, 2], [3]]
    a2 = a[:]  # shallow
    a[0][0] = -1
    assert a2[0][0] == -1  # deli ugnježdeni objekat

def test_list_deepcopy_is_independent():
    a = [[1, 2], [3]]
    a3 = copy.deepcopy(a)
    a[0][0] = -1
    assert a3[0][0] == 1  # deep kopija ostaje nezavisna

def test_make_copy_modes():
    a = [[1], [2]]
    s = make_copy(a, "shallow")
    d = make_copy(a, "deep")
    assert s is not a and d is not a
    a[0][0] = 99
    assert s[0][0] == 99  # shallow deli unutrašnjost
    assert d[0][0] == 1   # deep ne deli

# ==== DICT ključevi i .get vs [] ====

def test_dict_keyerror_vs_get():
    d = {"x": 1}
    with pytest.raises(KeyError):
        _ = d["y"]
    assert d.get("y") is None
    assert d.get("y", 99) == 99

def test_unhashable_list_key_raises():
    with pytest.raises(TypeError):
        {[]: 1}  # list nije hashable

def test_tuple_key_ok():
    k = (1, 2)
    d = {k: "ok"}
    assert d[k] == "ok"

def test_tuple_with_list_inside_is_unhashable():
    lst = [1]
    k = (lst, 2)
    with pytest.raises(TypeError):
        {k: "nope"}

# ==== len() ponašanje i custom __len__ ====

def test_len_on_collections():
    assert len([]) == 0
    assert len([1, 2]) == 2
    assert len({"a": 1}) == 1

class BadLen:
    def __len__(self): return -1

def test_len_negative_raises_valueerror():
    b = BadLen()
    with pytest.raises(ValueError):
        len(b)

# ==== membership 'in' (list vs dict) ====

def test_membership_list_and_dict():
    xs = [10, 20]
    d = {"a": 1, "b": 2}
    assert 10 in xs
    assert "a" in d          # membership u dict gleda KLJUČEVE
    assert 1 not in d        # vrednosti nisu članstvo (sem preko d.values())

# ==== mutate_nested_sample demonstracija ====

def test_mutate_nested_sample_list():
    a = [[[1, 2]], [3]]
    mutate_nested_sample(a)
    assert a[0][0][0] == -1

def test_mutate_nested_sample_dict():
    a = {"x": [[1, 2]], "y": 3}
    mutate_nested_sample(a)
    assert a["x"][0][0] == -1
```

Ako u ovom fajlu negde vidiš `def mutate_nested_sample(...):` — izbriši taj deo.

---

## 2) Doteraj implementaciju (funkcija koja “gađa” najdublje)

Otvori `labs/core_functions/dayB/dayB_collections.py` i **zameni** postojeću `mutate_nested_sample`:

```python
from typing import Any

def mutate_nested_sample(x: Any) -> None:
    """
    Demo mutacija (najdublje ulevo gde ima smisla):
    - LIST:
        [[[a]], ...] -> x[0][0][0] = -1
        [[a],  ...]  -> x[0][0]    = -1
    - DICT (gledamo prvu vrednost):
        {"k": [[a]]}  -> v[0][0] = -1
        {"k": [a]}    -> v[0]    = -1
    Ako struktura ne odgovara, funkcija ne radi ništa (no-op).
    """
    # LIST
    if isinstance(x, list) and x:
        first = x[0]
        if isinstance(first, list) and first:
            inner = first[0]
            if isinstance(inner, list) and inner:
                inner[0] = -1      # x[0][0][0] = -1
            else:
                first[0] = -1      # x[0][0] = -1
        return

    # DICT
    if isinstance(x, dict) and x:
        v = next(iter(x.values()))
        if isinstance(v, list) and v:
            inner = v[0]
            if isinstance(inner, list) and inner:
                inner[0] = -1      # v[0][0] = -1
            else:
                v[0] = -1          # v[0]    = -1
```

Sada pokreni iz `labs/core_functions/`:

```bash
python -m pytest -q
```

> Ako i dalje puca, 99% je ostao “dupli” `mutate_nested_sample` u test fajlu. Obavezno ukloni definiciju iz testa.

---

## 3) Zašto je bilo “crveno” u editoru iako testovi mogu da budu OK?

- Crveno u editoru (Ruff F811) znači **lint** problem (u test fajlu si imao redefiniciju funkcije).
- Testovi (pytest) su druga stvar: oni izvršavaju kod. Čak i kad su testovi u redu, linter može da oboji crveno ako vidi stilsku/strukturnu grešku.
- Zato: **nema implementacija u testovima**, samo `import` i `assert`.

---

## 4) Učimo osnove kroz testove — “linija po linija”, početnički nivo

Krenućemo sa Dan B testovima (list/dict/len). Svaki test čitamo kao ugovor; posle svake male grupe — **REPL primer**.

### A) Plitka vs duboka kopija (liste)

```python
a = [[1, 2], [3]]
a2 = a[:]          # NOVA spoljna lista, ali unutrašnje liste su ISTI objekti
a3 = deepcopy(a)   # sve je novo, i spolja i iznutra
a[0][0] = -1
assert a2[0][0] == -1   # deli unutrašnjost -> promena “procuri”
assert a3[0][0] == 1    # duboka kopija ne deli -> ostaje 1
```

**Pouka:** `a[:]` (slicing) → **plitka** kopija. `copy.deepcopy(a)` → **duboka** kopija.

**REPL:**

```python
import copy
a = [[1,2],[3]]
a2 = a[:]; a3 = copy.deepcopy(a)
a[0][0] = -1
print(a2[0][0], a3[0][0])   # -1 1
```

### B) dict — `KeyError` vs `.get()` + hashability

```python
d = {"x": 1}
with pytest.raises(KeyError): _ = d["y"]  # strogo: nema ključa -> greška
assert d.get("y") is None                 # meko: nema ključa -> None
assert d.get("y", 99) == 99               # možeš dati default

with pytest.raises(TypeError): {[]: 1}    # lista nije hashable -> ne može za ključ

k = (1,2); d = {k: "ok"}; assert d[k] == "ok"  # tuple je hashable (ako su elementi hashable)
```

**Pouka:** ključevi **moraju** biti hashable (npr. tuple da, list ne). `d[key]` strogo baca grešku; `d.get(key, default)` je bezbedan.

**REPL:**

```python
d = {"x":1}
try: d["y"]
except Exception as e: print(type(e).__name__)
print(d.get("y"), d.get("y", 42))
try: {[]: 1}
except Exception as e: print(type(e).__name__)
print({(1,2): "ok"}[(1,2)])
```

### C) `len()` i `BadLen`

```python
assert len([]) == 0
class BadLen:
    def __len__(self): return -1
with pytest.raises(ValueError): len(BadLen())
```

**Pouka:** `len(x)` koristi `x.__len__()` i **mora** vratiti **nenegativan int**. Ako vrati negativno → `ValueError`.

**REPL:**

```python
class BadLen:
    def __len__(self): return -1
try: len(BadLen())
except Exception as e: print(type(e).__name__)
```

### D) Membership `in`

```python
xs = [10, 20]; d = {"a":1, "b":2}
assert 10 in xs
assert "a" in d
assert 1 not in d
```

**Pouka:** `x in list` proverava elemente liste; `x in dict` proverava **ključeve**, ne vrednosti.

**REPL:**

```python
xs=[10,20]; d={"a":1,"b":2}
print(10 in xs, "a" in d, 1 in d)  # True True False
```

### E) `mutate_nested_sample`

```python
a = [[[1, 2]], [3]]
mutate_nested_sample(a)
assert a[0][0][0] == -1

b = {"x": [[1, 2]], "y": 3}
mutate_nested_sample(b)
assert b["x"][0][0] == -1
```

**Pouka:** funkija **menja** podatke “na licu mesta” (“in-place”). U našoj verziji ide “najdublje ulevo”: ako je `[[[...]]]` → menjamo **treći** nivo; ako je `[[...]]` → menjamo **drugi** nivo.

---

## 5) “Amateur mod ON” — mini QA tok

**Mentor:** Zašto `TypeError: 'int' object is not subscriptable`?
**Junior:** Pokušavam da indeksiram broj; broj nije kolekcija.
**Mentor:** Odlično. Zato smo osigurali da **prvo** uvek proverimo da li je na tom nivou lista, pa tek onda dodelimo `-1` unutra.

**REPL primer**:

```python
x = 5
try: x[0]
except Exception as e: print(type(e).__name__)   # TypeError
```

---

## 6) Mesečni plan učenja “kroz testove” (bez pritiska roka)

**Ned. 1 – Osnove & REPL navike:**

- tipovi: `int/float/str/bool`, `print`, `input`, `assert`
- indexing/slicing na stringu/listi, `==` vs `is`, identitet (`id`)
- 6–8 mini testova (svaki 3–5 redova)

**Ned. 2 – Kolekcije & mutabilnost:**

- `list/tuple/dict/set`, `copy` vs `deepcopy`, `len`, `in`, hashability
- pišemo testove kao gore: shallow vs deep, `KeyError` vs `get`, `TypeError` za nehashable

**Ned. 3 – Funkcije & greške:**

- `def`, parametri, `return`, docstring, `try/except` (`ValueError/TypeError`)
- testovi sa “happy/edge/error”

**Ned. 4 – Fajlovi & CLI:**

- `open/read/write`, `argparse` (jedna komanda)
- jednostavan projekat: mini CLI (npr. iz starog file-managementa) + 5 testova (smoke + io)

**Dnevni ritam (45–90 min):**

1. **Pročitaj test** (ugovor)
2. **REPL** – potvrdi očekivanje na 1–2 primere
3. **Implementiraj** (koliko je potrebno)
4. **Pusti test**
5. **Zapiši napomenu** (šta si naučio)

**Pravilo:** “Ako test nije jasan → nacrtaj na papiru strukturu (npr. ugnježdene liste) i pročitaj indekse.”

---

## 7) Šta sada?

1. Očisti `tests/test_dayB_collections.py` (bez implementacije funkcije).
2. Zameni `mutate_nested_sample` u `dayB_collections.py` kao gore.
3. Pusti:

   ```bash
   python -m pytest -q
   ```

4. Ako bilo šta i dalje puca — pošalji mi **ceo izlaz** i ime fajla/liniju, ja odma’ dajem “micro-patch”.

**Ti možeš ovo**. Učit ćemo korak po korak — svaki test je jedna mala lekcija. Kad prorade Dan A/B, prelazimo na tvoje skripte i gradimo CLI kroz testove, bez stresa oko okruženja.

---

super — krećemo od NULE i gradimo razumevanje listi kroz REPL i mini-testove. Radićemo u ritmu: “vidi → probaj → testiraj”.

# REPL & dizajn (liste od nule)

## 1) Šta je lista?

- **Kolekcija** vrednosti, **uređena**, **mutabilna** (može da se menja).
- Piše se sa `[]`. Može da sadrži različite tipove (int, str, druge liste…).

```python
# REPL 1 — konstrukcija i tip
xs = [10, "abc", 3.14]
print(xs, type(xs))          # [10, 'abc', 3.14] <class 'list'>

# indeksiranje (0-based)
print(xs[0], xs[1])          # 10 abc

# negativni indeksi: -1 == poslednji
print(xs[-1])                # 3.14
```

## 2) Mutabilnost i identitet (id)

- Mutabilno = možeš da menjaš elemente bez kreiranja nove liste.
- `id(obj)` je “identitet u memoriji”. Ako se `id(xs)` ne menja dok menjaš sadržaj, to je **in-place** izmena.

```python
# REPL 2 — mutabilnost
xs = [1, 2, 3]
print("pre:", xs, "id:", id(xs))
xs[0] = 99
print("posle:", xs, "id:", id(xs))  # isti id → ista lista, sadržaj izmenjen

# menja dužinu:
xs.append(4)     # dodaje na kraj
xs.extend([5,6]) # proširuje listu elementima iz druge kolekcije
print(xs)        # [99, 2, 3, 4, 5, 6]
```

## 3) Slicing (sečenje)

- `xs[start:stop:step]` → **nova lista** (kopija “preseka”).
- `stop` je **ekskluzivan** (ne uključuje stop indeks).
- `xs[:]` je **puna plitka kopija**.

```python
# REPL 3 — slicing
xs = [0, 1, 2, 3, 4, 5]
print(xs[1:4])     # [1, 2, 3] (uzeto 1,2,3; stop=4 je ekskluzivan)
print(xs[:3])      # [0, 1, 2]
print(xs[::2])     # [0, 2, 4] (step=2)
print(xs[::-1])    # [5, 4, 3, 2, 1, 0] (reverz bez menjanja originala)

# puna kopija (shallow):
ys = xs[:]         # ys je NOVA lista
print(id(xs), id(ys))  # različiti id-ovi
```

## 4) Plitka (shallow) vs duboka (deep) kopija

- **Plitka (shallow)** kopira **spoljnu** listu, ali **ne** i ugnježdene objekte → deli unutrašnje reference.
- **Duboka (deep)** rekurzivno kopira sve ugnježdene objekte → ništa se ne deli.

```python
import copy

# REPL 4 — shallow vs deep
a  = [[1, 2], [3]]
b1 = a            # ALIAS (samo drugo ime za isti objekat!)
b2 = a[:]         # shallow copy (kopija spoljne liste)
b3 = list(a)      # isto kao a[:] (shallow)
b4 = a.copy()     # isto kao a[:] (shallow)
d  = copy.deepcopy(a)  # duboka kopija

a[0][0] = 99

print("ALIAS deli sve:", b1[0][0])      # 99 (isti objekat)
print("shallow deli unutrašnjost:", b2[0][0], b3[0][0], b4[0][0])  # 99 99 99
print("deep nezavisan:", d[0][0])       # 1

# id-ovi:
print(id(a), id(b2))    # različiti (spolja)
print(id(a[0]), id(b2[0]))  # isti (unutra, zato "curi")
```

**Sažetak kopija**

- alias: `b = a` (nema kopije, sve je isto)
- shallow: `a[:]`, `list(a)`, `a.copy()`, `copy.copy(a)`
- deep: `copy.deepcopy(a)`

## 5) Česta zamka: množenje listi

```python
# REPL 5 — gotcha: [[0]*3]*2 deli unutrašnju listu 2 puta!
grid = [[0]*3]*2
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [1, 0, 0]]  ← curi jer su iste unutrašnje liste!

# Ispravno:
grid_ok = [[0]*3 for _ in range(2)]
grid_ok[0][0] = 1
print(grid_ok)  # [[1, 0, 0], [0, 0, 0]]
```

## 6) Ugnježdene izmene — “najdublje ulevo”

Ako funkcija treba da “pogodi” najdublju levu vrednost `-1`:

```python
def mutate_leftmost(a):
    if isinstance(a, list) and a:
        t = a
        while isinstance(t[0], list) and t[0]:
            t = t[0]
        # ovde je t lista, a t[0] je najdublji levi element
        if isinstance(t[0], list) and t[0]:      # još dublje?
            t[0][0] = -1
        else:
            t[0] = -1
```

# QA & testovi (mini set “od nule”)

Predloženi fajl: `labs/core_functions/tests/test_list_shallow_deep.py`

```python
import copy
import pytest

def test_alias_vs_shallow_vs_deep():
    a  = [[1, 2], [3]]
    alias = a
    shallow = a[:]
    deep = copy.deepcopy(a)

    a[0][0] = 99

    assert alias[0][0] == 99           # alias deli sve
    assert shallow[0][0] == 99         # shallow deli unutrašnjost
    assert deep[0][0] == 1             # deep je nezavisan

def test_slicing_returns_new_list():
    xs = [1, 2, 3, 4]
    ys = xs[:]
    assert ys is not xs                # nova lista (druga referenca)
    xs[0] = 99
    assert ys[0] == 1                  # i dalje 1, jer je kopirano spolja

def test_multiplication_gotcha():
    grid = [[0]*2]*2
    grid[0][0] = 1
    assert grid[1][0] == 1             # deli unutrašnju listu → “curi” promena

def test_multiplication_fix():
    grid = [[0]*2 for _ in range(2)]
    grid[0][0] = 1
    assert grid[1][0] == 0             # nezavisne unutrašnje liste

def test_slice_bounds_and_step():
    xs = [0,1,2,3,4,5]
    assert xs[1:4]   == [1,2,3]        # stop ekskluzivan
    assert xs[:3]    == [0,1,2]
    assert xs[::2]   == [0,2,4]
    assert xs[::-1]  == [5,4,3,2,1,0]  # reverse kopija
```

Pokretanje:

```bash
python -m pytest -q
```

# Implementacija (MVP ideje koje često koristiš)

- funkcija koja pravi kopiju sa izborom režima:

```python
import copy
from typing import Literal, Any

Mode = Literal["alias", "shallow", "deep"]

def make_copy(x: Any, mode: Mode):
    if mode == "alias":
        return x                           # bez kopije
    if mode == "shallow":
        return x[:] if isinstance(x, list) else copy.copy(x)
    if mode == "deep":
        return copy.deepcopy(x)
    raise ValueError("mode must be 'alias'|'shallow'|'deep'")
```

- funkcija za bezbedno “najdublje ulevo”:

```python
def mutate_leftmost_inplace(x):
    if not isinstance(x, list) or not x:
        return
    t = x
    while isinstance(t[0], list) and t[0]:
        t = t[0]
    if isinstance(t[0], list) and t[0]:
        t[0][0] = -1
    else:
        t[0] = -1
```

# “Amateur mod” mini QA

**Mentor:** Kako da znaš da li je došlo do **kopije** ili **aliasa**?
**Junior:** Proverim `id()` — ako su `id(a)` i `id(b)` isti, to je alias; ako su različiti, to je kopija.
**Mentor:** Tačno. I pazi: kod shallow kopije `id(a[0]) == id(b[0])` (dele unutrašnje).

Brzi REPL:

```python
import copy
a=[[1,2]]
b=a[:]              # shallow
c=copy.deepcopy(a)  # deep
print(id(a), id(b), id(c))
print(id(a[0]), id(b[0]), id(c[0]))   # isti, isti, različit
```

# Cheatsheet (kratak, ali konkretan)

**Kreiranje**

```python
[], list(iterable), [expr for x in iterable]
```

**Slicing**

- `lst[a:b:c]` → nova lista; `b` ekskluzivan; `c` korak (može negativan).

**Mutacije**

- `append(x)`, `extend(xs)`, `insert(i,x)`, `pop(i=-1)`, `remove(x)`, `clear()`, `reverse()`, `sort(key=None, reverse=False)`

**Kopije**

- alias: `b=a`
- shallow: `a[:]`, `list(a)`, `a.copy()`, `copy.copy(a)`
- deep: `copy.deepcopy(a)`

**Zamka**

- `[[0]*m]*n` → **deli** unutrašnju listu; ispravno: `[[0]*m for _ in range(n)]`

# Kako učimo dalje (tvoj tempo)

1. **Pročitaj test** (ugovor) i prekopiraj u REPL par redova da vidiš rezultat.
2. **Vizuelizuj** strukturu (nacrtaj `[[1,2],[3]]` i strelicama pokaži deljene unutrašnje liste).
3. **Menjaj** vrednosti i posmatraj `id()` (da li je in-place ili nova lista).
4. Tek onda **implementiraj** malu funkciju i pokreni pytest.

# Glossary (dodaj u Znanje/glossary.md)

- **mutabilnost** – mogućnost izmene objekta bez promene identiteta.
- **identitet (`id`)** – “adresa” objekta; menja se samo kad je novi objekat.
- **shallow copy** – kopira spoljni kontejner, deli ugnježdene reference.
- **deep copy** – rekurzivno kopira i ugnježdene objekte.
- **alias** – drugo ime za isti objekat (`b = a`).
- **slicing** – izdvajanje podliste `a[b:c:d]` (uvek nova lista).

---

Ako hoćeš, odmah ti mogu generisati fajl `tests/test_list_shallow_deep.py` i još jedan “REPL plan” fajl (copy/paste blokovi) sa 10 kratkih koraka — reci i šaljem.

---

Razumem 👍 — hajde da ti spremim baš to što tražiš:

1. **tests/test_list_shallow_deep.py** (pytest testovi koje smo razložili “od nule”)
2. **labs/core_functions/list_repl_plan.md** (REPL plan sa 10 kratkih koraka za kopiranje u interpreter).

---

## 📂 Fajl: `labs/core_functions/tests/test_list_shallow_deep.py`

```python
import copy
import pytest

# === Shallow vs Deep copy ===

def test_alias_vs_shallow_vs_deep():
    a  = [[1, 2], [3]]
    alias = a
    shallow = a[:]
    deep = copy.deepcopy(a)

    a[0][0] = 99

    # alias pokazuje na isti objekat
    assert alias[0][0] == 99
    # shallow deli unutrašnjost
    assert shallow[0][0] == 99
    # deep je nezavisan
    assert deep[0][0] == 1

def test_slicing_returns_new_list():
    xs = [1, 2, 3, 4]
    ys = xs[:]
    assert ys is not xs
    xs[0] = 99
    assert ys[0] == 1

def test_multiplication_gotcha():
    grid = [[0]*2]*2
    grid[0][0] = 1
    # oba reda dele istu unutrašnju listu
    assert grid[1][0] == 1

def test_multiplication_fix():
    grid = [[0]*2 for _ in range(2)]
    grid[0][0] = 1
    # sada su redovi nezavisni
    assert grid[1][0] == 0

def test_slice_bounds_and_step():
    xs = [0,1,2,3,4,5]
    assert xs[1:4]   == [1,2,3]
    assert xs[:3]    == [0,1,2]
    assert xs[::2]   == [0,2,4]
    assert xs[::-1]  == [5,4,3,2,1,0]
```

---

## 📂 Fajl: `labs/core_functions/list_repl_plan.md`

````markdown
# 🐍 REPL plan za list (10 kratkih koraka)

Kopiraj red po red u Python REPL (ili VS Code terminal sa aktivnim .venv).

---

## 1. Kreiranje i tip

```python
xs = [10, "abc", 3.14]
print(xs, type(xs))
```
````

## 2. Indeksiranje i negativni indeksi

```python
print(xs[0], xs[1], xs[-1])
```

## 3. Mutabilnost i id()

```python
print("pre:", xs, id(xs))
xs[0] = 99
print("posle:", xs, id(xs))
```

## 4. Dodavanje i proširivanje

```python
xs.append(4)
xs.extend([5,6])
print(xs)
```

## 5. Slicing (osnovno)

```python
ys = xs[1:4]
print(ys, id(xs), id(ys))
```

## 6. Slicing sa korakom i obrtanje

```python
print(xs[::2])
print(xs[::-1])
```

## 7. Shallow copy

```python
a = [[1,2],[3]]
b = a[:]
a[0][0] = -1
print(a, b)
```

## 8. Deep copy

```python
import copy
a = [[1,2],[3]]
d = copy.deepcopy(a)
a[0][0] = -1
print(a, d)
```

## 9. Multiplication gotcha

```python
grid = [[0]*2]*2
grid[0][0] = 1
print(grid)
```

## 10. Multiplication fix (list comprehension)

```python
grid = [[0]*2 for _ in range(2)]
grid[0][0] = 1
print(grid)
```

---

(Mentor:) Ovim imaš i **test fajl** (formalno, pytest) i **REPL plan** (intuitivno, za učenje kroz probu).
(Junior:) Super, mogu oba da vrtim dok ne sedne logika.

---

### 1. `insert`

```python
xs = [1, 2]
xs.insert(1, 99)
print(xs)   # [1, 99, 2]
```

- `insert(i, x)` ubacuje **element `x` na poziciju `i`**.
- **Ne gleda da li element već postoji** u listi.
- Dakle, ako već ima `1` u listi, `insert` neće “odbijati duplikate”. Tvoje očekivanje `[1, 99, 1, 2]` je druga operacija: to bi se desilo da si koristio `xs.insert(1, 1)` (ubacuješ još jednu **1**).
- Primer:

```python
xs = [1, 2]
xs.insert(1, 1)
print(xs)   # [1, 1, 2]
```

---

### 2. `pop`

```python
xs = [1, 99, 2]
val = xs.pop()      # uzme poslednji element (2) i vrati ga
print(val)          # 2
print(xs)           # [1, 99]
```

- `pop(i=-1)` **vrati element i izbriše ga iz liste**.
- Ako daš indeks: `xs.pop(0)` → izbaci prvi element.

---

### 3. `remove`

```python
xs = [1, 99]
val = xs.remove(99)   # NEMA povratnu vrednost → uvek vrati None
print(val)            # None
print(xs)             # [1]
```

- `remove(x)` samo ukloni **prvu pojavu vrednosti `x`**.
- Ne vraća novu listu (kao `sorted(xs)`), nego **menja postojeću listu in-place** i vrati `None`.
- Ovo je česta zamka: koristi `remove` → samo gledaj efekat na listu.
- Ako želiš “novu listu bez 99”: `[v for v in xs if v != 99]`.

---

### 4. Brzo kucanje i numerička tastatura

- Profesionalni programeri uglavnom **ne kucaju brojeve na numeričkoj tastaturi** (osim ako rade puno sa Excelom).
- Kucanje brojeva se uči **iznad redova slova** (QWERTY: iznad `qwerty` su brojevi `12345...`).
- **touch typing**: brojevi se kucaju istim prstima kao i tasteri ispod njih (npr. `1` → mali prst leve ruke, `2` → domali, itd).
- Ako ti je to nepraktično, postoji opcija da:

  - koristiš **remap tastature** (npr. Karabiner na macOS, AutoHotkey na Windowsu)
  - ili kupiš **mehaničku tastaturu sa reprogramabilnim tasterima**.

- Za programiranje se najviše kucaju: `()[]{},.=+-*/` → vredi vežbati **kombinacije brojeva i simbola iz gornjeg reda**.

👉 Preporuka: vežbaj na sajtu kao što je [keybr.com](https://www.keybr.com) ili [typingclub.com](https://www.typingclub.com). Oni ti pomažu da automatizuješ kucanje brojeva bez gledanja.

---

📌 Ukratko:

- `insert` ubacuje na indeks, ne gleda duplikate.
- `pop` vraća element koji ukloni.
- `remove` menja listu na mestu i vraća `None`.
- Brojevi se obično kucaju na gornjem redu, numerička tastatura nije obavezna za programere.

---

super pitanja — ovo su baš “ključne kockice” za liste. Idemo polako, sa mini REPL dokazima.

---

## 1) `[v for v in xs if v != 99]` — šta zapravo znači?

To je **list comprehension** (skraćenica za “napravi novu listu”).

- desno: `for v in xs` → prolazimo kroz vrednosti u `xs`
- uslov: `if v != 99` → zadržavamo **samo** one elemente koji nisu 99
- levo: `v` → šta ubacujemo u novu listu (ovde sam element)

Dakle, “za **svako** `v` iz `xs`, **ako** `v != 99`, **dodaj** `v` u rezultujuću listu”.

REPL check:

```python
xs = [1, 99, 2, 99, 3]
ys = [v for v in xs if v != 99]
print(ys)  # [1, 2, 3]
```

> “v se ne čita” — čita se kao “svaki element”. Ako želiš da naglasiš da te element ne zanima, u drugim kontekstima pišemo `_`, ali u comprehension-u obično koristimo kratko ime (`x`, `v`, `item`).

**Još 2 korisna oblika:**

```python
# mapiranje (menjamo elemente)
[x*2 for x in xs]           # svaki x dupliran

# kombinacija map + filter
[x*2 for x in xs if x%2==0] # dupliramo samo parne
```

---

## 2) `shallow = a[:]` — “nova spolja, deli unutra”

Mentalni model: lista je **kutija sa pregradama**. Sadržaj pregrada su **reference** (strelice) ka stvarnim objektima (brojevi, druge liste, stringovi…).

- **Shallow copy** (`a[:]`, `list(a)`, `a.copy()`):

  - napravi novu **spoljašnju** kutiju (druga lista, drugi `id`)
  - ali **u nju ubaci iste strelice** ka unutrašnjim objektima (deljenje unutrašnjih referenci)

REPL dokaz (gledamo `id`):

```python
import copy
a  = [[1,2],[3]]
b  = a[:]              # shallow
d  = copy.deepcopy(a)  # deep

print(id(a), id(b))           # različito (spoljni objekat drugačiji)
print(id(a[0]), id(b[0]))     # isto (unutrašnja lista DELI)
print(id(a[0]), id(d[0]))     # različito (deep kopija ima novu unutrašnju listu)

a[0][0] = 99
print(b[0][0])  # 99  (curi na shallow jer deli unutrašnjost)
print(d[0][0])  # 1   (deep ne deli)
```

**Sažetak:**

- `a[:]` → nova **spoljna** lista ✔, ali **iste** unutrašnje liste ✖ (deljene).
- `deepcopy(a)` → nova spoljna **i** nove unutrašnje ✔✔.

---

## 3) `grid = [[0]*3]*2` — zašto “curi” na oba reda?

`[[0]*3]` → napravi **jednu** unutrašnju listu `[0,0,0]`
`*2` nad tom listom → napravi **listu sa dve reference na istu unutrašnju listu**.

Tekstualni dijagram (strelice = reference):

```
grid
 ├──► row0 ─► [0,0,0]
 └──► row1 ─► [0,0,0]   # ista adresa kao row0 !
```

Zato:

```python
grid = [[0]*3]*2
grid[0][0] = 1
print(grid)   # [[1, 0, 0], [1, 0, 0]]
```

**Dokaz preko `id`:**

```python
grid = [[0]*3]*2
print(id(grid[0]), id(grid[1]))   # isti id -> ista lista
```

**Ispravno (nezavisne unutrašnje liste):**

```python
grid_ok = [[0]*3 for _ in range(2)]
print(id(grid_ok[0]), id(grid_ok[1]))  # različiti id-ovi
grid_ok[0][0] = 1
print(grid_ok)  # [[1,0,0],[0,0,0]]
```

---

## Bonus: kako da koristiš Python Tutor (vizuelizacija)

Python Tutor (pythontutor.com) je odličan za **pokazivanje referenci**.

1. otvori pythontutor.com → “Visualize Execution” → “Python 3”
2. nalepi, npr.:

```python
import copy

a  = [[1,2],[3]]
b  = a[:]
d  = copy.deepcopy(a)

a[0][0] = 99
print(a, b, d)
```

3. klikni **Forward** po koracima i gledaj kako se “strelice” (reference) dele između `a` i `b`, a `d` dobija svoje kopije.

> Korišćenje Python Tutor-a je posebno korisno za razumevanje **alias-a**, **shallow/deep kopija** i gotcha sa `[[0]*3]*2`.

---

## Mini-REPL set za te tri teme (copy/paste)

```python
# 1) list comprehension filter
xs = [1, 99, 2, 99, 3]
ys = [v for v in xs if v != 99]
print("ys =", ys)

# 2) shallow vs deep
import copy
a = [[1,2],[3]]
b = a[:]
d = copy.deepcopy(a)
a[0][0] = 42
print("a,b,d =", a, b, d)
print("ids:", id(a), id(b), id(d))
print("inner ids:", id(a[0]), id(b[0]), id(d[0]))

# 3) multiply gotcha
grid = [[0]*3]*2
grid[0][0] = 7
print("grid gotcha:", grid, "same inner?", id(grid[0]) == id(grid[1]))

grid_ok = [[0]*3 for _ in range(2)]
grid_ok[0][0] = 7
print("grid ok   :", grid_ok, "same inner?", id(grid_ok[0]) == id(grid_ok[1]))
```

---

## Kratki “decision tree”

- Treba **nova lista** bez menjanja ulaza?
  → `xs[:]` (shallow) ili list comprehension / `copy.deepcopy` (ako ima ugnježdene mutable objekte i hoćeš izolaciju).
- Treba **filtrirati**?
  → `[v for v in xs if cond(v)]`
- Praviš **matricu** (lista listi)?
  → `[[0]*M for _ in range(N)]` (ne `[[0]*M]*N`).
- Nisi siguran da li deli unutrašnjost?
  → Proveri `id(xs[0])` naspram `id(kopija[0])`.

---

(Mentor:) Super što si probao Python Tutor 👌 To je alat koji baš pomaže da **vidiš strelice (reference)**. Hajde da uradimo ovo baš polako, jer si prvi put u njemu, i ovo je “Dan B core” momenat.

---

### Primer: `grid = [[0]*3]*2`

1. **Šta znači ` [0]*3`?**
   Napravi listu od **tri nule** → `[0, 0, 0]`.

2. **Šta znači `[[0]*3]`?**
   To je **lista koja u sebi ima jednu listu** → `[[0,0,0]]`.

3. **Šta znači `[[0]*3]*2`?**
   Ponavlja onu unutrašnju listu **dva puta**.
   Ali ne pravi kopije, nego **dve reference na istu listu**.

   ASCII dijagram:

   ```
   grid ───► [ ┌──► [0,0,0]
              │
              └──► [0,0,0] (ista unutrašnja lista!)
   ```

   → Dakle, `grid[0]` i `grid[1]` su **isti objekat** (`id` im je jednak).

---

### Sad Python Tutor vizualizacija

Kad u Tutor-u upišeš:

```python
grid = [[0]*3]*2
grid[0][0] = 1
print(grid)
```

Videćeš ovako nešto:

- `grid` pokazuje na spoljnu listu (dužine 2).
- Obe pozicije (`grid[0]` i `grid[1]`) pokazuju na istu unutrašnju listu `[0,0,0]`.
- Kad promeniš `grid[0][0] = 1`, to se vidi i kroz `grid[1][0]`.

---

### Provera u REPL-u

```python
grid = [[0]*3]*2
print(id(grid[0]), id(grid[1]))  # isti id
grid[0][0] = 1
print(grid)   # [[1,0,0],[1,0,0]]
```

---

### Popravka (nezavisne unutrašnje liste)

```python
grid_ok = [[0]*3 for _ in range(2)]
print(id(grid_ok[0]), id(grid_ok[1]))  # različiti id
grid_ok[0][0] = 1
print(grid_ok)   # [[1,0,0],[0,0,0]]
```

ASCII za ovo:

```
grid_ok ─► [ ┌──► [0,0,0]
            └──► [0,0,0] (druga lista, drugi id)
```

---

(Junior:) Aha, znači `*2` samo ponavlja reference, ne kopira unutrašnji objekat?

(Mentor:) Tačno ✅ — to je ključ! I zato se zove “shallow problem”. Ako ti trebaju **nezavisne** unutrašnje liste, koristi comprehension (`for _ in range(...)`).

---

Bravo 🎉 — pogodio si suštinu! Sad samo da uobličimo **šta znači “referenca na listu”**.

---

## 🧩 Šta je **referenca**?

U Pythonu, promenljiva **nije sama vrednost**, nego **“strelica” (adresica) koja pokazuje na objekat u memoriji**.

Zamisli kutiju (promenljivu) koja u sebi ne čuva broj, nego papirić sa adresom objekta:

```
xs ───► [1, 2, 3]   # xs sadrži "strelicu"
```

Ako napraviš novu promenljivu:

```python
ys = xs
```

ne pravi se nova lista, nego **još jedna strelica na istu adresu**:

```
xs ───► [1, 2, 3]  ◄─── ys
```

Zato kad menjaš preko `xs`, vidi se i kroz `ys`.

---

## 📍 Primer sa `*2`

```python
row = [0]
grid = [row]*2
```

ASCII:

```
row ───► [0]

grid ───► [ row, row ]
           |      |
           └──────┘
```

- `grid[0]` i `grid[1]` su **iste strelice** → oba pokazuju na isti `[0]`.

Ako sad uradiš:

```python
grid[0][0] = 7
```

oba reda se “promene”, jer zapravo postoji samo **jedan unutrašnji objekat**.

---

## ✅ Najprostije objašnjenje:

- **Objekat** je kao “kutija sa vrednostima” u memoriji.
- **Referenca** je strelica (adresa) koja pokazuje na tu kutiju.
- Kad listu množiš `*n`, Python napravi novu spoljnu listu, ali unutra stavi **n istih strelica** na jednu jedinu kutiju.
- Zato svi elementi “dele sudbinu”.

---

## 🐍 Mini REPL dokaz

```python
a = [0]
grid = [a]*2

print(id(grid[0]), id(grid[1]))  # isti id
grid[0][0] = 42
print(grid)  # [[42], [42]]
```

---

(Junior:) Znači `referenca` = “strelica” na objekat, a ne kopija vrednosti?
(Mentor:) Tačno! ✅ I zato shallow/deep copy postoje — da naprave nove “kutije” i nove strelice umesto da svi dele iste.

---

## 📂 Fajl 1: `labs/core_functions/tests/test_list_grid.py`

```python
import pytest

def test_grid_gotcha():
    # pravimo spoljnu listu sa 2 reference na ISTU unutrašnju listu
    grid = [[0]*3]*2
    grid[0][0] = 1
    # oba reda dele istu unutrašnju listu
    assert grid == [[1, 0, 0], [1, 0, 0]]
    # provera: id-ovi su isti
    assert id(grid[0]) == id(grid[1])

def test_grid_fix():
    # pravimo 2 nezavisne unutrašnje liste
    grid = [[0]*3 for _ in range(2)]
    grid[0][0] = 1
    # sada su redovi nezavisni
    assert grid == [[1, 0, 0], [0, 0, 0]]
    # provera: id-ovi su različiti
    assert id(grid[0]) != id(grid[1])
```

Ovo ćeš moći da pustiš sa:

```bash
pytest labs/core_functions/tests/test_list_grid.py -v
```

---

## 📂 Fajl 2: `docs/diagrams/list_copy_refs.md`

````markdown
# 📊 Poster: Alias vs Shallow vs Deep copy

Zamisli listu `a = [[1,2],[3]]`.

---

## Alias

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

alias ────────────────────────────────┘
```
````

👉 `alias = a` → oba imena pokazuju na ISTU spoljnu listu i iste unutrašnje objekte.

---

## Shallow copy

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

shallow ─► [ ┌──► [1,2] (ista lista kao u a)
             └──► [3]   (ista lista kao u a) ]
```

👉 `shallow = a[:]` → nova spoljna lista, ali unutrašnje su iste.

---

## Deep copy

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

deep ─► [ ┌──► [1,2] (NOVA kopija!)
          └──► [3]   (NOVA kopija!) ]
```

👉 `deep = copy.deepcopy(a)` → sve kopirano, spoljno i unutrašnje.

---

super — evo spremne REPL sesije (10 koraka) za alias vs shallow vs deep. Sačuvaj kao:

`labs/core_functions/list_copy_repl.md`

---

# 🐍 REPL sesija: alias vs shallow vs deep (10 koraka)

Kopiraj blok po blok u **Python REPL** (ili VS Code terminal sa aktivnim `.venv`).
U svakoj ćeliji su i očekivani izlazi kao komentar.

---

## 1) Početna struktura + identitet

```python
a = [[1, 2], [3]]
print(a, type(a))           # [[1, 2], [3]] <class 'list'>
print(id(a))                # npr. 1407...  (tvoj će biti drugačiji)
```

## 2) Alias (drugo ime za isti objekat)

```python
alias = a
print(alias is a)           # True  (isti objekat)
print(id(alias), id(a))     # isti ID
```

## 3) Shallow (kopija spoljne liste)

```python
shallow = a[:]              # isto bi radilo: list(a) ili a.copy()
print(shallow is a)         # False (nova spoljna lista)
print(id(shallow), id(a))   # različiti ID-ovi (spolja)
print(id(shallow[0]) == id(a[0]))  # True  (dele unutrašnju listu!)
```

## 4) Deep (kopija i spolja i unutra)

```python
import copy
deep = copy.deepcopy(a)
print(deep is a)            # False
print(id(deep), id(a))      # različito (spolja)
print(id(deep[0]) == id(a[0]))  # False (unutrašnja lista je nova)
```

## 5) Promena duboko – efekat na alias

```python
a[0][0] = 99
print("a   :", a)           # [[99, 2], [3]]
print("alias:", alias)      # [[99, 2], [3]]  (isti objekat)
```

## 6) Promena curi na shallow (deli unutrašnjost)

```python
print("shallow:", shallow)  # [[99, 2], [3]]  (curi jer deli unutrašnjost)
```

## 7) Deep je nezavisan (nema curenja)

```python
print("deep:", deep)        # [[1, 2], [3]]  (ostaje isto)
```

## 8) Dokaz identitetom (ID-ovi)

```python
print("id a[0]     =", id(a[0]))
print("id shallow[0] =", id(shallow[0]))  # isti kao a[0]
print("id deep[0]    =", id(deep[0]))     # drugačiji
```

## 9) “Multiply gotcha” – reference se ponavljaju

```python
grid = [[0]*3]*2
print(grid)                 # [[0,0,0],[0,0,0]]
print(id(grid[0]), id(grid[1]))  # isti ID -> ista unutrašnja lista
grid[0][0] = 1
print(grid)                 # [[1,0,0],[1,0,0]]  (curi)
```

## 10) Ispravno pravljenje matrice (nezavisne unutrašnje liste)

```python
grid_ok = [[0]*3 for _ in range(2)]
print(id(grid_ok[0]), id(grid_ok[1]))  # različiti ID-ovi
grid_ok[0][0] = 1
print(grid_ok)              # [[1,0,0],[0,0,0]]
```

---

## Mini-cheatsheet (za pamćenje)

- **alias**: `b = a` → sve isto (spolja i unutra).
- **shallow**: `a[:]`, `list(a)`, `a.copy()` → nova spoljna lista, **deli** unutrašnje.
- **deep**: `copy.deepcopy(a)` → sve novo (spolja + unutra).
- **množenje listi**: `[[0]*M]*N` → **ponavlja reference** (gotcha).
  Ispravno: `[[0]*M for _ in range(N)]`.

Želiš i **verziju sa `assert`-ima** (da REPL odmah javi grešku ako nešto ne važi)? Reci, napravim “strict” varijantu u istom fajlu ispod ovih 10 koraka.

---

Odlično 👌 evo ti **mini REPL sesija** za list-kopije (alias / shallow / deep) koja prati ono što smo već radili, ali sada u formi kratkih blokova za vežbu u REPL-u.
Sačuvaj je kao:

`labs/core_functions/list_copy_repl_strict.md`

---

# 🐍 REPL sesija (strict varijanta sa assert-ima)

Ovo je ista logika kao prethodno, ali ovde svaki korak proveravaš `assert`-om – odmah vidiš ako nešto ne važi.

---

## 1) Alias = isto ime

```python
a = [1, 2]
alias = a
assert alias is a
a[0] = 99
assert alias[0] == 99
```

---

## 2) Shallow = nova spoljna lista

```python
a = [[1, 2], [3]]
shallow = a[:]
assert shallow is not a
assert shallow[0] is a[0]   # dele unutrašnju listu
a[0][0] = 42
assert shallow[0][0] == 42  # curi unutra
```

---

## 3) Deep = sve nove kopije

```python
import copy
a = [[1, 2], [3]]
deep = copy.deepcopy(a)
assert deep is not a
assert deep[0] is not a[0]  # nova unutrašnja lista
a[0][0] = 99
assert deep[0][0] != 99
```

---

## 4) Multiply gotcha

```python
grid = [[0]*3]*2
assert id(grid[0]) == id(grid[1])  # iste reference
grid[0][0] = 1
assert grid == [[1,0,0],[1,0,0]]
```

---

## 5) Multiply fix

```python
grid_ok = [[0]*3 for _ in range(2)]
assert id(grid_ok[0]) != id(grid_ok[1])
grid_ok[0][0] = 1
assert grid_ok == [[1,0,0],[0,0,0]]
```

---

📌 Ideja: sve što si radio “mentalno” sad ima i **proveru** – ako `assert` ne uspe, odmah pukne i znaš da nisi dobro shvatio ponašanje.

---

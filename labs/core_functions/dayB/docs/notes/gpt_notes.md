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

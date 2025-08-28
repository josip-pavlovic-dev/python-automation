# Day B — list / dict / len (analysis)

## Potpisi & protokoli

- list: sekvenca, mutabilna; bitne metode: append, extend, insert, pop, remove, clear; slicing vraća **novu listu** (plitka kopija).
- dict: mapping (ključ → vrednost), ključ mora biti **hashable**; pristup `d[key]` baca **KeyError**; `d.get(key, default)` ne baca.
- len(x) -> int: koristi ****len****; mora vratiti **nenegativan int** (negativno → **ValueError**). Takođe učestvuje u truthiness protokolu (ako nema **bool**). (vidi i Dan A bilješke o bool/len)

## Tabela ulaz → izlaz / ponašanja (iz REPL-a)

| Tema           | Primer                   | Očekivanje                                 |
| -------------- | ------------------------ | ------------------------------------------ |
| list slicing   | `a2 = a[:]`              | plitka kopija (unutrašnji objekti deljeni) |
| deepcopy       | `copy.deepcopy(a)`       | duboka kopija (nezavisna unutrašnjost)     |
| dict get       | `d.get('x', 0)`          | vrednost ili default, bez greške           |
| KeyError       | `d['x']` kad nema ključa | **KeyError**                               |
| unhashable key | `{[]:1}`                 | **TypeError** (list nije hashable)         |
| hashable key   | `{(1,2): "ok"}`          | ✅                                         |
| len negativan  | `len(BadLen())`          | **ValueError**                             |

## Dunder pregled

- `__len__` (kolekcije i custom klase); `len(x)` → non-negative int.
- `__iter__` (sekvence/mapping iteriraju po elementima/ključevi).
- `__contains__` (optimizuje `in`; za dict proverava **ključeve**).

## Greške (tipične)

- `KeyError` za `d[key]` kada ključ ne postoji.
- `TypeError` za **ne-hashable** ključ u dict.
- `ValueError` za negativan rezultat `__len__`.

## Primeri kopiranja

- `a2 = a[:]` / `list(a)` / `copy.copy(a)` → plitko
- `copy.deepcopy(a)` → duboko
- Kod ugnježdenih struktura uvek testiraj posledicu na unutrašnje objekte (ids + promene).

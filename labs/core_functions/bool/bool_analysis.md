# `bool(x)` — analiza funkcije

> **Kratak opis:** > `bool(x)` vraća istinitosnu vrednost objekta `x` — `True` ili `False`.
> Ponašanje zavisi od “truthiness” protokola: prvo se poziva `x.__bool__()`, a ako ne postoji, pokušava se `x.__len__()`. Ako ni to ne postoji, podrazumevano je `True` (jer je to “neprazan/ne-nulti” objekat po definiciji).

_Ovaj dokument je urađen po šablonu dnevne analize funkcije_ :contentReference[oaicite:0]{index=0}

---

## 1) Potpis i intuicija

```python
bool(x) -> bool
```

- Ako je `x` “prazan” (0, `0.0`, `''`, `[]`, `{}`, `set()`, `range(0)`, `None`), rezultat je `False`.
- Ako je “neprazan” (bilo šta sa “ne-nultom” vrednošću), rezultat je `True`.

---

## 2) Ulazi / izlazi — tipična očekivanja

| Ulaz                | Rezultat | Obrazloženje                           |
| ------------------- | -------- | -------------------------------------- |
| `0`, `0.0`, `0j`    | False    | nula je “lažno”                        |
| `1`, `-1`, `2.7`    | True     | nenula je “istina”                     |
| `''`                | False    | prazan string                          |
| `'0'`, `'False'`    | True     | neprazan string je istinit             |
| `[]`, `{}`, `set()` | False    | prazne kolekcije                       |
| `[0]`, `{'a': 1}`   | True     | kolekcija sa stavkama                  |
| `None`              | False    | posebna “prazna” vrednost              |
| `object()`          | True     | nema **bool**/**len**, default je True |

---

## 3) Dunder protokol (važno za profesionalnu praksu)

1. Ako postoji `__bool__(self) -> bool`, koristi se to.
2. Inače, ako postoji `__len__(self) -> int`, vrednost 0 znači `False`, a nenula `True`.
3. Ako nema ni jedno ni drugo, objekat je **True**.

**Primer:**

```python
class Box:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)

bool(Box([]))      # False (len == 0)
bool(Box([1, 2]))  # True  (len > 0)

class Flag:
    def __init__(self, v): self.v = v
    def __bool__(self): return bool(self.v)

bool(Flag(0))      # False
bool(Flag(5))      # True
```

---

## 4) Neočekivani momenti (pitfall-ovi)

- `bool("False") is True` — zato što je string **neprazan**.
- `bool(Decimal('0')) is False` i `bool(Fraction(0, 5)) is False` — jer predstavljaju nulu.
- Custom klase: ako ne implementiraju `__bool__`/`__len__`, biće `True` čak i ako subjektivno “deluju prazno”.

---

## 5) REPL mini-plan (što pre da “klikne”)

- Proveri scalare: `bool(0)`, `bool(1)`, `bool(-1)`, `bool(0.0)`, `bool(0j)`.
- Proveri stringove: `bool("")`, `bool("0")`, `bool("False")`.
- Proveri kolekcije: `bool([])`, `bool([[]])`, `bool({})`, `bool({'x': 1})`.
- Napravi dve klase: jedna sa `__len__`, druga sa `__bool__`; potvrdi redosled protokola.
- Proveri default: `bool(object())` → True.

---

## 6) Python Tutor fokus

- Napravi klasu `Box` sa `__len__` i `Flag` sa `__bool__`.
- U Tutor-u vizuelno prati koji metod se poziva i koju vrednost vraća.
- Uporedi ocene: `bool(Box([]))` vs `bool(Flag(0))`.

---

## 7) Test plan (logika spremna za pytest)

- **Pozitivni**: neprazne kolekcije, nenulte vrednosti.
- **Negativni**: prazne kolekcije, nule, `None`.
- **Custom**: potvrdi da `__bool__` ima prioritet nad `__len__`.
- **Edge**: stringovi “varaju”: `"0"`, `"False"` → `True`.

---

## 8) Profesionalne smernice

- U `if` uslovima koristi truthiness, ali **budi eksplcitan** kad je dvosmisleno:

  - Bolje `if my_string: ...` (proverava prazno/neprazno) nego `if len(my_string) > 0`.
  - Ali, ako vrednost može biti `"0"` ili `"False"`, i želiš numeričko tumačenje, **parsiraj** pre (`int(...)`, `strtobool`, sl.).

- U API-jevima i modelima jasno definiši `__bool__` ili `__len__` ako klasa predstavlja “kolekciju” ili “flag”.

---

## 9) Checklist

- [x] Razlikujem falsy vs truthy tipove.
- [x] Znam redosled: `__bool__` → `__len__` → default `True`.
- [x] Znam zamke sa stringovima.
- [x] Znam da testiram custom tipove.

---

```

```

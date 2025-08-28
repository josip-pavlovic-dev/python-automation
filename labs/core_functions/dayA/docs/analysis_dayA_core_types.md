# Dan A — int / str / bool (analysis)

## int()

**Potpis:** `int(x=0) -> int` · `int(x: str|bytes|bytearray, base=10) -> int`
**Intuicija:** konverzija u ceo broj; float → trunc prema nuli; tekst/bytes → parsiranje cifara uz `base` (0..36 ili 0 za auto).

### Mini tabela (ulaz → izlaz)

| Ulaz           | Izlaz / Greška  | Napomena                           |
| -------------- | --------------- | ---------------------------------- |
| `42.9`         | `42`            | trunc prema 0                      |
| `-3.9`         | `-3`            | trunc                              |
| `"1010", 2`    | `10`            | baza 2                             |
| `"FF", 16`     | `255`           | heks                               |
| `"0b101", 0`   | `5`             | auto prefiks                       |
| `"  42\n"`     | `42`            | whitespace ok                      |
| `b"2a", 16`    | `42`            | bytes kao ASCII cifre              |
| `"12.5"`       | `ValueError`    | loš literal                        |
| `3.0, base=10` | `TypeError`     | base dozvoljen samo za tekst/bytes |
| `float("inf")` | `OverflowError` | spec vrednosti                     |

**Dunder:** `__int__` primaran; `__index__` kao celobrojni fallback.

---

## str()

**Potpis:** `str(object='') -> str` · (za bytes: koristi `.decode()` za tekst)
**Intuicija:** čitljiv prikaz objekta; za bytes `str(b)` daje repr (`"b'...'"`), a ne tekst.

### Mini tabela

| Ulaz                | Izlaz / Greška | Napomena               |
| ------------------- | -------------- | ---------------------- |
| `42`                | `"42"`         | broj → tekst           |
| `True`              | `"True"`       | bool                   |
| `None`              | `"None"`       | None                   |
| `[1,"a"]`           | `"[1, 'a']"`   | kolekcije              |
| `b"abc"`            | `"b'abc'"`     | repr bytes-a           |
| `(b"abc").decode()` | `'abc'`        | pravi tekst            |
| `str(123, "utf-8")` | `TypeError`    | encoding samo za bytes |

**Dunder:** `__str__` → fallback na `__repr__` (ako `__str__` ne postoji).

---

## bool()

**Potpis:** `bool(x) -> True|False`
**Intuicija:** truthiness: prazno (`''`, `[]`, `{}`, `0`, `None`) je **falsy**; ostalo je **truthy**.

### Mini tabela

| Ulaz       | Izlaz | Napomena               |
| ---------- | ----- | ---------------------- |
| `0`        | False | int falsy              |
| `1`        | True  | int truthy             |
| `""`       | False | prazan string          |
| `"0"`      | True  | ne-prazan string       |
| `[]`       | False | prazna kolekcija       |
| `[0]`      | True  | ne-prazna kolekcija    |
| `None`     | False | posebna falsy vrednost |
| `object()` | True  | default objekat        |

**Dunder lanac:** `__bool__` → `__len__` → default True; loš povratni tip iz `__bool__` → `TypeError`.

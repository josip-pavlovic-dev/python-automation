# int_analysis_notes.md — vodič za popunjavanje analysis (korak-po-korak)

> Cilj: da _dokažeš_ razumevanje `int()` kroz REPL i Python Tutor; isti duh kao kod `str()`

## 0) Potpis i intuicija

- Zapiši potpise:
  - `int(x=0) -> int`
  - `int(x: str|bytes|bytearray, base=10) -> int`
- Kratko: “Konvertuje u celobrojnu vrednost. Za `float` → trunc prema nuli; za tekst/bytes → parsira cifre sa zadatom osnovom.”

## 1) Ulazi i izlazi (REPL mini-tabela)

Napravi tabelu ulaz → izlaz:

- Brojevi: `int(3.7) -> 3`, `int(-2.9) -> -1`, `int(True) -> 1`, `int(False) -> 0`
- Tekst:
  - `"10" -> 10`, `"0b101", base=0 -> 5`, `"1_000" -> 1000`, `"12.3" -> ValueError`
- Bytes/bytearray: `b"2a", base=16 -> 42`, `bytearray(b"10"), base=2 -> 2`
- Egzotika: `int(float("nan")) -> ValueError`, `int(float("inf")) -> OverflowError`

## 2) Dunder metode

- Napravi klase:
  - `WithInt` sa `__int__` koji vraća `42`
  - `OnlyIndex` sa `__index__` koji vraća `7`
- REPL: `int(WithInt()) -> 42`, `int(OnlyIndex()) -> 7`
- Zaključak: `__int__` je primaran; `__index__` može poslužiti kao fallback za celobrojne tipove.

## 3) Greške i ivice

- `int("1__0")` → `ValueError` (nepravilni underscores)
- `int(3.0, 10)` → `TypeError` (zato što je dat `base` a `x` nije string/bytes)
- `int(float("inf"))` → `OverflowError`
- `int(None)` → `TypeError`

## 4) Osnove (base) i prefiksi

- Pokaži `base=0` auto-detekciju: `"0x10" -> 16`, `"0o10" -> 8`, `"0b10" -> 2`, `"010" -> 10` (u Py3 bez `0o` nije oktal).
- Prođi `base` granice: `1` ili `37` → `ValueError`.

## 5) Python Tutor mini-skripta

- Umetni ~10 linija (pogledaj `int_tutor_template.py` kojeg ćeš dobiti dole).
- Zabeleži: koji metod se poziva pri `int(obj)` i kako se vrednosti menjaju po koracima.

## 6) Zaključci & “što sa posla”

- Kada parsiraš input → uvek `try/except ValueError`.
- Za interfejse koji traže “integer-like” → implementiraj `__index__` (npr. veličina, indeks).
- Ne koristi `int()` za formatiranje; za format → `f"{n:d}"` ili `format(n, "d")`.

## 7) Mini test plan

| Ulaz              | Očekivani izlaz | Napomena                        |
| ----------------- | --------------- | ------------------------------- |
| `3.7`             | `3`             | trunc prema nuli                |
| `-2.9`            | `-1`            | negativni trunc                 |
| `"0b101", base=0` | `5`             | auto-detekcija                  |
| `"1_000"`         | `1000`          | underscores OK                  |
| `"12.3"`          | `ValueError`    | decimalna tačka nije dozvoljena |
| `b"2a", base=16`  | `42`            | bytes parsiranje                |
| `float("inf")`    | `OverflowError` | specijalne vrednosti iz `float` |
| `WithInt()`       | `42`            | `__int__`                       |
| `OnlyIndex()`     | `7`             | `__index__` fallback            |

---

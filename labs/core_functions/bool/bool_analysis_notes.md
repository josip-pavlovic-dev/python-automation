# bool_analysis_notes.md — vodič

## 0) Potpis i intuicija
- `bool(x) -> True|False`
- Logika: __bool__ → __len__ → default True.

## 1) Ulazi i izlazi (REPL tabela)
- `0 -> False`, `1 -> True`, `-1 -> True`
- `"" -> False`, `"0" -> True`
- `[] -> False`, `[0] -> True`
- `None -> False`, `object() -> True`

## 2) Dunder metode
- Klasa `WithBool` → `__bool__` vraća False
- Klasa `WithLen` → `__len__` vraća 2
- Klasa `BadBool` → `__bool__` vraća 2 → TypeError

## 3) Greške
- Samo user-def loši povratni tipovi.
- Prazne kolekcije su falsy, neprazne truthy.

## 4) Python Tutor
- Vizualizuj razliku kada se poziva `__bool__` ili `__len__`.

## 5) Zaključci za posao
- Kod API dizajna: eksplicitno dokumentovati truthiness.
- Idiom: `if xs:` umesto `if len(xs) > 0:`.

## 6) Mini test plan
| Ulaz         | Izlaz   | Napomena |
|--------------|---------|----------|
| `0`          | False   | integer |
| `"0"`        | True    | string nije prazan |
| `[]`         | False   | empty list |
| `[0]`        | True    | non-empty list |
| `None`       | False   | None falsy |
| `WithBool()` | False   | koristi __bool__ |
| `WithLen()`  | True    | koristi __len__ |
| `BadBool()`  | TypeError | loš tip povratne vrednosti |

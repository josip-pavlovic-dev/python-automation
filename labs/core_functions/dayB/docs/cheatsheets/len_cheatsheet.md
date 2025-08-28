# len — Cheatsheet

- `len(x)` koristi `x.__len__()` i očekuje **nenegativan int** → inače **ValueError**.
- Truthiness: ako nema `__bool__`, koristi se `__len__` (0 → False, >0 → True).

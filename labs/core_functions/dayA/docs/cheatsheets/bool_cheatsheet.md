# bool — Cheatsheet

- Truthiness: prazno/0/None → False; ostalo → True.
- Dunder lanac: `__bool__` → `__len__` → default True.
- Ako `__bool__` ne vrati `bool` → `TypeError`.

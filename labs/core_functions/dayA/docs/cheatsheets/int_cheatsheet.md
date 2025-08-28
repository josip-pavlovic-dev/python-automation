# int — Cheatsheet

- `int(x)` trunc prema nuli; `int("0b101", 0)` auto prepoznaje prefiks.
- `int(text|bytes, base)` za baze 2..36 ili `0` za auto.
- Greške: `ValueError` (loš literal), `TypeError` (nevalidan base), `OverflowError` (npr. inf).
- Dunder: `__int__` → fallback `__index__` (celobrojni).

# str — Cheatsheet

- `str(x)` → korisnički prikaz (`__str__` ili `__repr__` fallback).
- `str(b"bytes")` daje `"b'...'"` (repr); **pravi tekst** dobij `bytes.decode(encoding)`.
- `str(obj, encoding)` je `TypeError` (osim specijala za bytes u C API; idiom je `.decode()`).
- Kada ti treba kontrola formata: `format()`, f-string specifikatori.

# ✅ REPL Checklist — `int()` i `str()`

## 🔢 `int()`

- [ ] `help(int)` i `int.__doc__`
- [ ] Happy path: `int(42.9)`, `int("10")`
- [ ] Negativni float: `int(-3.9)`
- [ ] Whitespace u stringu: `int("  42\\n")`
- [ ] Auto-baza: `int("0b101", 0)`, `int("0xFF", 0)`
- [ ] Eksplicitne baze: `int("1010", 2)`, `int("FF", 16)`
- [ ] Bool vrednosti: `int(True)`, `int(False)`
- [ ] Greške:
  - `int("12.5")` → ValueError
  - `int(3.0, 10)` → TypeError
  - `int(float("inf"))` → OverflowError
- [ ] Custom klase:
  - `WithInt.__int__()`
  - `OnlyIndex.__index__()`
- [ ] Poredi sa: `float()`, `str()`

---

## 📝 `str()`

- [ ] `help(str)` i `str.__doc__`
- [ ] Happy path: `str(42)`, `str(3.14)`, `str(True)`, `str(None)`
- [ ] Kolekcije: `str([1, "a"])`, `str((1,2))`, `str({})`
- [ ] Prazan string: `str("")`
- [ ] Whitespaces ostaju: `str("  42\\n")`
- [ ] Bytes vs decode:
  - `str(b"abc")` → `"b'abc'"`
  - `(b"abc").decode()` → `'abc'`
- [ ] Greške:
  - `str(123, "utf-8")` → TypeError
  - `str(b"\\xff", "utf-8", "strict")` → UnicodeDecodeError
- [ ] Custom klase:
  - Bez `__str__` (fallback na `__repr__`)
  - Sa `__str__`
- [ ] Poredi sa: `repr()`, f-string formatiranjem

---

## 🛠️ REPL trikovi za svaki dan

- [ ] `_` (underscore) čuva poslednji rezultat:
  ```python
  >>> 3 + 4
  7
  >>> _ * 2
  14
  ```
- [ ] `dir(obj)` → lista svih atributa i metoda objekta.
- [ ] `vars()` i `locals()` → pokažu sve trenutne promenljive.
- [ ] `exit()` ili `Ctrl+D` → izlazak iz REPL-a.
- [ ] Tab completion → dopunjava imena funkcija i metoda (posebno u IPython-u).
- [ ] Multiline unos: koristi blokove (`for`, `if`), zagrade `() [] {}`, ili backslash `\`.
- [ ] Multiline stringovi: `""" ... """`.

Top! Kreiram komplet “Dan A” paket po istom šablonu kao za Dan B — sa istim 4-blok ritmom: REPL & dizajn → Implementacija (CLI + lib) → QA & testovi → Docs & wrap (Tutor skripte, cheatsheet, glossary). Kao osnovu koristim tvoj postojeći materijal (analysis, REPL isečci, mini CLI) i dopunjujem gde treba. Osnovne reference iz priloga: analiza (), mini CLI (), REPL skripta ().

---

# 1) REPL & dizajn

**Fajl:** `labs/dayA/int_str_bool_repl.md`
_(preuzeto i prilagođeno iz tvog priloga; uključuje help(), dunder putanje, happy/edge/error; pokazuje tipove grešaka)_&#x20;

```python
# ===== int() =====
help(int); print(int.__doc__)
print(int(42.9), int(-3.9))                 # 42, -3  (trunc prema nuli)
print(int("1010", 2), int("FF", 16))        # 10, 255
print(int("  42\n"))                        # 42  (whitespace OK)
print(int("0b101", 0))                      # 5   (base=0 auto-detekcija prefiksa)
print(int(b"2a", 16))                       # 42  (bytes kao ASCII cifre)
try: int("12.5")
except Exception as e: print(type(e).__name__)  # ValueError
try: int(3.0, 10)
except Exception as e: print(type(e).__name__)  # TypeError
try: int(float("inf"))
except Exception as e: print(type(e).__name__)  # OverflowError

# Dunder: __int__ i fallback na __index__
class WithInt:    def __int__(self): return 42
class OnlyIndex:  def __index__(self): return 7
print(int(WithInt()), int(OnlyIndex()))     # 42, 7

# ===== str() =====
help(str); print(str.__doc__)
b = b"abc"
print(str(b))                      # "b'abc'" (repr bytes-a)
print(b.decode())                  # 'abc'    (stvarni tekst)
class NoStr: pass
class WithStr:
    def __str__(self): return "WithStr::pretty"
print(str(NoStr()))                # <__main__.NoStr object at 0x...> (fallback na repr)
print(str(WithStr()))              # 'WithStr::pretty'
try: str(123, "utf-8")
except Exception as e: print(type(e).__name__)  # TypeError

# ===== bool() =====
help(bool); print(bool.__doc__)
print(bool(0), bool(1), bool(-1))          # False True True
print(bool(""), bool("0"))                 # False True
print(bool([]), bool([0]))                 # False True
print(bool(None), bool(object()))          # False True
class WithBool:  def __bool__(self): return False
class WithLen:   def __len__(self):  return 2
print(bool(WithBool()), bool(WithLen()))   # False, True
class BadBool:   def __bool__(self): return 2
try: bool(BadBool())
except Exception as e: print(type(e).__name__)  # TypeError
```

Mini decision-tree:

- `int(x, base)` koristi se samo kada je `x` tekst/bytes; za numerike ide `int(x)` (trunc prema nuli).
- `str(object)` je čitljiv prikaz; za **bytes → tekst** koristi se `.decode(encoding)`.
- `bool(x)` → `__bool__` → `__len__` → default `True` (osim “praznih”/0/None).

---

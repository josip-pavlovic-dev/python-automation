# 🧪 REPL Session — `int()`

## 1) 📜 Dokumentacija
```python
help(int)
print(int.__doc__)
```
👉 Potpis pokazuje dva oblika: `int(x=0)` i `int(x: str|bytes|bytearray, base=10)`.

---

## 2) ✅ Happy path (normalni primeri)
```python
print(int(42.9))    # 42
print(int("10"))   # 10
```

---

## 3) ⚠️ Edge-case testovi
```python
print(int(-3.9))        # -3 (trunc prema nuli)
print(int("  42\n"))   # 42 (whitespace i newline dozvoljeni)
print(int("0b101", 0)) # 5 (auto-detekcija baze)
```

---

## 4) ❌ Greške
```python
try:
    int("12.5")
except Exception as e:
    print(type(e).__name__)  # ValueError

try:
    int(3.0, 10)
except Exception as e:
    print(type(e).__name__)  # TypeError

try:
    int(float("inf"))
except Exception as e:
    print(type(e).__name__)  # OverflowError
```

---

## 5) 🧩 Custom objekti
```python
class WithInt:
    def __int__(self): return 42

class OnlyIndex:
    def __index__(self): return 7

print(int(WithInt()))   # 42 (poziva __int__)
print(int(OnlyIndex())) # 7 (fallback na __index__)
```

---

## 6) 🔍 Upoređivanje sa sličnim funkcijama
```python
print(str(42))     # '42'
print(repr(42))    # '42'
print(float(42))   # 42.0
```
👉 int() je za konverziju, ne za formatiranje. Za format koristi f-string ili format().

---

## 7) 📌 Beleške
- `int()` **truncuje** float vrednosti prema nuli.
- Dozvoljeni su whitespace i znaci +/-.
- `base=0` radi auto-detekciju prefiksa (0b, 0x, 0o).
- Greške su jasne: `ValueError`, `TypeError`, `OverflowError`.
- `__int__` i `__index__` otvaraju prostor za custom tipove.


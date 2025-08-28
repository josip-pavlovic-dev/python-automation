# 🧪 REPL Session — `str()`

## 1) 📜 Dokumentacija
```python
help(str)
print(str.__doc__)
```
👉 Potpis pokazuje: `str(object='')` i `str(object: bytes, encoding, errors)`.

---

## 2) ✅ Happy path (normalni primeri)
```python
print(str(42))       # '42'
print(str(3.14))     # '3.14'
print(str(True))     # 'True'
print(str(None))     # 'None'
print(str([1, "a"])) # "[1, 'a']"
```

---

## 3) ⚠️ Edge-case testovi
```python
print(str(""))           # '' (prazan string)
print(str("  42\n"))     # '  42\n' (whitespace ostaje u stringu)
print(str(b"abc"))       # "b'abc'" (repr bytes-a)
print((b"abc").decode()) # 'abc' (decode pretvara bytes u tekst)
```

---

## 4) ❌ Greške
```python
try:
    str(123, "utf-8")
except Exception as e:
    print(type(e).__name__)  # TypeError (encoding samo za bytes)

try:
    str(b"\xff", "utf-8", "strict")
except Exception as e:
    print(type(e).__name__)  # UnicodeDecodeError
```

---

## 5) 🧩 Custom objekti
```python
class NoStr:
    pass

class WithStr:
    def __str__(self): return "pretty"

print(str(NoStr()))   # fallback na <__main__.NoStr object at 0x...>
print(str(WithStr())) # 'pretty'
```

---

## 6) 🔍 Upoređivanje sa sličnim funkcijama
```python
x = 12.3456
print(str(x))        # '12.3456'
print(repr(x))       # '12.3456'
print(f"{x:.2f}")     # '12.35' (formatiranje)
```
👉 str() daje čitljiv prikaz, repr() tehnički, a f-string/format kontrolu.

---

## 7) 📌 Beleške
- `str()` daje “user-friendly” prikaz; `repr()` je za debug.
- Za bytes-like ulaze, `str()` daje repr, a pravi tekst dobijaš `decode()`.
- Greške: `TypeError` kod encoding-a za ne-bytes i `UnicodeDecodeError` kod lošeg dekodiranja.
- Koristiti `str()` za logove/korisnički ispis, `repr()` za test/debug, `f"..."` za formatiranje.


# 🧪 REPL Session Template

## 1) 📜 Dokumentacija
```python
help(FUNKCIJA)
print(FUNKCIJA.__doc__)
```
👉 prvo pogledaj potpis i opis.

---

## 2) ✅ Happy path (normalni primeri)
```python
# Tipični slučajevi
print(FUNKCIJA(42))
print(FUNKCIJA("10"))
```

---

## 3) ⚠️ Edge-case testovi
```python
# Negativne vrednosti / praznine / specijalni inputi
print(FUNKCIJA(-3.9))
print(FUNKCIJA("  42\\n"))
print(FUNKCIJA("0b101", 0))   # auto-detekcija
```

---

## 4) ❌ Greške
```python
# Hvatanje i analiza tipa greške
try:
    FUNKCIJA("12.5")
except Exception as e:
    print(type(e).__name__)
```

---

## 5) 🧩 Custom objekti
```python
# Testiraj dunder protokol (__int__, __str__...)
class Demo:
    def __int__(self): return 99
print(FUNKCIJA(Demo()))
```

---

## 6) 🔍 Upoređivanje sa sličnim funkcijama
```python
# Nađi funkcije koje rade slično (npr. int vs float vs str)
print(str(42))
print(repr(42))
```

---

## 7) 📌 Beleške
- Šta radi iznenađujuće?
- Koja greška se najčešće javlja?
- Koji edge-case mi je najkorisniji za posao/praksu?


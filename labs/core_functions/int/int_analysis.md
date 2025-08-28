# `int_analysis.md`

> 📌 **UPUTSTVO:** Ovaj fajl je krajnji pregled funkcije `int()`, zasnovan na REPL testiranju i dokumentaciji. Popunjen je na osnovu `int_analysis_notes.md`.

---

## 🔹 1. Kratak opis funkcije

`int(x)` konvertuje vrednost u ceo broj (`int`). Ako se pozove bez argumenata → vraća `0`.

---

## 🔸 2. Lična pretpostavka pre analize

Mislio sam da `int()` radi samo za stringove i obične brojeve. Nisam znao da radi i za `bool` vrednosti (`int(True) == 1`, `int(False) == 0`) niti da podržava konverziju iz različitih baza kada se prosledi drugi argument.

---

## 🔍 3. REPL testiranje (ulaz/izlaz, tipovi, identiteti)

```python
int()              # 0
int(3.9)           # 3
int("42")          # 42
int("101", 2)      # 5 (binarni string)
int(True)          # 1
int(False)         # 0
int([])            # ❌ TypeError
```

- `type(int("42"))` → `<class 'int'>`
- `id(int(5))` uvek vraća identitet, ali mali brojevi (−5 do 256) su **internirani** → isti `id`.

---

## 📚 4. Šta proveriti u `help()` / `signature`?

```python
help(int)
# int([x]) -> integer
# int(x, base=10) -> integer
```

- Ako se koristi string kao ulaz → može se zadati `base`.
- Ako je ulaz već ceo broj → vraća ga bez promene (isti objekat).
- `__doc__` opis potvrđuje: podržani tipovi su string, realan broj, bool, bytes-like.

---

## 🧭 5. Python Tutor analiza

- Kada pozoveš `int("101", 2)` → interni parser string "101" konvertuje u ceo broj u bazi 2.
- Kada pozoveš `int(True)` → Python interno poziva `bool.__int__()` koji vraća `1`.
- Kada proslediš float → Python samo odbacuje decimalni deo (`3.9 → 3`).

---

## ✅ 6. Da li je funkcija:

- Transformaciona: ✅ (menja tip: str → int, float → int, bool → int)
- Validaciona: ❌
- IO: ❌
- Pomoćna: ✅ (često deo drugih validacija i parsiranja)

---

## 🚩 7. Granični slučajevi

- `int("abc")` → ❌ `ValueError`
- `int([])` ili `int({})` → ❌ `TypeError`
- `int(1e100)` → radi, ali dobiješ ogroman ceo broj
- `int("101", 37)` → ❌ jer je dozvoljeno max `base=36`
- Negativni brojevi u stringovima: `int("-42")` radi normalno

---

## 🧠 8. Zaključak i korisnost

`int()` je osnovna funkcija za konverziju. U praksi:

- Parsiranje inputa iz CLI ili fajlova (`int("123")`)
- Rad sa bool vrednostima u aritmetici (`True + True == 2`)
- Konverzija između baza (npr. binarni string u decimalni int)

👉 Funkcija je transformaciona i pomoćna; koristi se u skoro svim Python skriptama. Da bih je objasnio drugaru: "Pretvara sve što može u ceo broj, a ako ne može – baci grešku."

---

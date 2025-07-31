# 📄 Cheatsheet | _Pregled najvažnijih izraza_

## 📌 Explanation: | _Objašnjenje:_

### `Path(__file__).resolve().parent`

- Returns absolute path to script's folder | _Vraća apsolutnu putanju do foldera skripte_

### `rglob("*.ext")`

- Recursively searches all files with given extension | _Rekurzivno pretražuje sve fajlove sa datom ekstenzijom_

### `relative_to(base_dir)`

- Returns path relative to base directory | _Vraća putanju relativnu u odnosu na početni folder_

### `with open(...) as f`

- Safely writes content to file | _Bezbedno upisuje sadržaj u fajl_

---

## 🔍 Key Syntax | _Ključna sintaksa_

```python
for p in base_dir.rglob("*.py"):
    print(p.relative_to(base_dir))
```

- Lists all `.py` files relative to `base_dir` | _Prikazuje sve `.py` fajlove relativno u odnosu na `base_dir`_

---

## 📁 Typical usage pattern | _Tipičan obrazac korišćenja_

- Use `rglob()` to scan recursively | _Koristi `rglob()` za rekurzivno skeniranje_
- Use headers and counts for clarity | _Koristi zaglavlja i brojače za preglednost_
- Use `relative_to()` for clean paths | _Koristi `relative_to()` za čiste putanje_

---

### 1️⃣ `base_dir.rglob("*")`

- **`base_dir`**: To je promenljiva koja predstavlja direktorijum (Path objekat) u kojem tražimo fajlove.
- **`rglob("*")`**: Funkcija iz `pathlib` modula koja rekurzivno prolazi kroz **sve podfoldere i fajlove** unutar `base_dir`.

  - `"*"` je šablon (wildcard) koji znači: _"bilo šta – svi fajlovi i folderi"_.
  - Rezultat `rglob("*")` je generator koji vraća **Path objekte** (jedan po jedan fajl/folder).

👉 Primer:
Ako folder ima sledeću strukturu:

```
project/
├── main.py
├── data/
│   ├── file1.txt
│   └── images/
│       └── logo.png
```

`base_dir.rglob("*")` će vratiti:

```
Path("main.py")
Path("data")
Path("data/file1.txt")
Path("data/images")
Path("data/images/logo.png")
```

---

### 2️⃣ `if p.is_file()`

- U list comprehensions možeš dodati uslov na kraju.
- **`p.is_file()`** proverava da li je `p` (Path objekat) fajl (a ne folder).

  - Ako je fajl → ubacuje ga u listu
  - Ako je folder → preskače ga

👉 Ovo služi da iz rezultata **izbaci foldere**, jer `rglob("*")` vraća i fajlove i foldere.

---

### 3️⃣ `[p for p in ...]`

- Ovo je **list comprehension** – kraći zapis za pravljenje liste u jednom redu.
- Za svaki element (`p`) koji `rglob("*")` vrati:

  1. Proverava `if p.is_file()`
  2. Ako je uslov tačan, dodaje ga u listu

- Rezultat je lista koja sadrži **samo Path objekte fajlova**.

---

### Rezultat (`all_files`)

- Nakon izvršavanja, `all_files` je **lista svih fajlova u `base_dir` i njegovim podfolderima**.

Primer:

```python
print(all_files)
# [PosixPath('main.py'), PosixPath('data/file1.txt'), PosixPath('data/images/logo.png')]
```

---

⚡ **Zašto je ovo važno?**

- Dobijaš čistu listu fajlova bez foldera.
- Možeš kasnije prolaziti kroz ovu listu i raditi šta želiš (ispis, upis u fajl, filtriranje itd.).

---

# 🧠 Built-in Runtime Variables Cheatsheet

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 🔹 `__name__`

- 🇬🇧 Holds the module name. Equals `"__main__"` when the file is run directly.
- 🇷🇸 Sadrži ime modula. Ima vrednost `"__main__"` ako se fajl direktno pokrene.

### ✅ Primer:

```python
if __name__ == "__main__":
    print("Direct execution / Direktno pokretanje")
```

---

## 🔹 `__main__`

- 🇬🇧 Special value of `__name__` when the script is executed directly.
- 🇷🇸 Posebna vrednost promenljive `__name__` kada se fajl pokreće direktno.

### ✅ Primer:

```bash
python skripta.py      → __name__ == "__main__"
import skripta          → __name__ == "skripta"
```

---

## 🔹 `__file__`

- 🇬🇧 Contains the path to the current `.py` file.
- 🇷🇸 Sadrži putanju do trenutnog `.py` fajla.

### ✅ Primer:

```python
print(__file__)
```

### ➕ Kombinacija za punu putanju foldera:

```python
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

print(f"Folder u kom se fajl nalazi: {script_dir}")
```

---

## 🔁 Rezime

| Promenljiva | 🇬🇧 Opis                            | 🇷🇸 Objašnjenje                                  |
| ----------- | ---------------------------------- | ----------------------------------------------- |
| `__name__`  | Name of the module or `"__main__"` | Ime modula ili `"__main__"` ako se pokreće      |
| `__main__`  | Execution entry point              | Tačka ulaska u kod ako se fajl direktno pokreće |
| `__file__`  | Path to the current script         | Putanja do trenutno izvršavanog `.py` fajla     |

---

✅ **Koristi ovaj cheatsheet** kada god praviš skriptu koja treba da:

- ima jasan ulazni deo (`main`)
- koristi relativne putanje bez zavisnosti od radnog direktorijuma

---

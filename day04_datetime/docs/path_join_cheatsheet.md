# 🔗 path_join_cheatsheet.md — Working with Paths | Rad sa Putanjama

#### 🇬🇧: How to reliably create full paths in Python using `os.path.join` and `os.getcwd()`.

#### 🇷🇸: Kako pouzdano kreirati pune putanje u Python-u koristeći `os.path.join` i `os.getcwd()`.

## 📌 Get Full File Path | Dobijanje pune putanje fajla

```python
import os

def get_full_path(filename):
    current_dir = os.getcwd()
    return os.path.join(current_dir, filename)
```

#### 🇬🇧: Joins the current directory with filename.

#### 🇷🇸: Spaja trenutni direktorijum sa imenom fajla.

---

## 🔍 Why Use `os.path.join`? | Zašto koristiti `os.path.join`?

#### 🇬🇧 Platform-independent (Windows/Linux/Mac)

#### 🇷🇸 Nezavisno od operativnog sistema

---

## 💡 Examples | Primeri

```python
print(get_full_path("report.txt"))
# Output: C:\Users\JoleDev\projects\report.txt
```

```python
folder = os.path.join("base_dir", "subdir", "files")
```

---

#### 📌 **Useful in**: File creation, logging, dynamic path building

#### 📌 **Korisno za**: Kreiranje fajlova, logovanje, dinamičko generisanje putanja

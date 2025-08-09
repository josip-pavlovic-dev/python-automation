# 🧠 Snippets – os module | _Snippeti – os modul_

## ✅ Summary | _Kratak pregled_

Tested key `os` and `os.path` functions using the file `snippets_os_demo.py`.  
| _Testirane su ključne funkcije `os` i `os.path` modula pomoću fajla `snippets_os_demo.py`._ |

---

## 🧪 Tested Functions | _Testirane funkcije_

| Function                | _Funkcija_              | Description                           | _Opis_                              |
| ----------------------- | ----------------------- | ------------------------------------- | ----------------------------------- |
| `os.getcwd()`           | `os.getcwd()`           | Returns the current working directory | _Vraća trenutni radni direktorijum_ |
| `os.listdir()`          | `os.listdir()`          | Lists contents of a directory         | _Prikazuje sadržaj direktorijuma_   |
| `os.mkdir(name)`        | `os.mkdir(name)`        | Creates a new directory               | _Kreira novi folder_                |
| `os.rename(src, dst)`   | `os.rename(src, dst)`   | Renames a file or folder              | _Preimenuje fajl ili folder_        |
| `os.path.isdir(path)`   | `os.path.isdir(path)`   | Checks if path is a directory         | _Proverava da li je folder_         |
| `os.path.isfile(path)`  | `os.path.isfile(path)`  | Checks if path is a file              | _Proverava da li je fajl_           |
| `os.path.abspath(path)` | `os.path.abspath(path)` | Gets absolute path                    | _Vraća apsolutnu putanju_           |
| `os.path.split(path)`   | `os.path.split(path)`   | Splits path into folder and file      | _Razdvaja folder i fajl iz putanje_ |
| `os.path.join(a, b)`    | `os.path.join(a, b)`    | Safely joins path parts               | _Bezbedno spaja delove putanje_     |
| `os.environ['PATH']`    | `os.environ['PATH']`    | Returns PATH environment variable     | _Vraća sistemsku promenljivu PATH_  |
| `os.path.getsize(path)` | `os.path.getsize(path)` | Gets file size in bytes               | _Veličina fajla u bajtima_          |

---

## 💡 Notes & Observations | _Napomene i zapažanja_

- `os.mkdir()` will raise `FileExistsError` if the folder already exists.  
  | _Ako folder već postoji, `os.mkdir()` baca grešku `FileExistsError`._ |
- `os.environ` behaves like a dictionary object.  
  | _`os.environ` se ponaša kao rečnik (`dict`)._ |
- Useful for testing relative vs. absolute paths and understanding directory structure.  
  | _Koristan za testiranje relativnih vs. apsolutnih putanja i strukture foldera._ |

---

📁 **Test file:** `bonus/snippets_os_demo.py`  
📚 **Module:** `os`, `os.path`

---

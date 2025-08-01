# 📄 Cheatsheet – os module | _Brza referenca – os modul_

## ✅ Frequently Used Functions | _Najčešće korišćene funkcije_

| Function                | _Funkcija_              | Description                   | _Opis_                        |
| ----------------------- | ----------------------- | ----------------------------- | ----------------------------- |
| `os.getcwd()`           | `os.getcwd()`           | Get current working directory | _Trenutni radni direktorijum_ |
| `os.listdir()`          | `os.listdir()`          | List contents of directory    | _Sadržaj direktorijuma_       |
| `os.mkdir(path)`        | `os.mkdir(path)`        | Create new directory          | _Kreiraj novi folder_         |
| `os.rename(src, dst)`   | `os.rename(src, dst)`   | Rename file or directory      | _Preimenuj fajl ili folder_   |
| `os.remove(path)`       | `os.remove(path)`       | Delete a file                 | _Obriši fajl_                 |
| `os.rmdir(path)`        | `os.rmdir(path)`        | Delete a directory            | _Obriši prazan folder_        |
| `os.path.isdir(path)`   | `os.path.isdir(path)`   | Check if path is directory    | _Da li je folder?_            |
| `os.path.isfile(path)`  | `os.path.isfile(path)`  | Check if path is file         | _Da li je fajl?_              |
| `os.path.abspath(path)` | `os.path.abspath(path)` | Absolute path of file         | _Apsolutna putanja fajla_     |
| `os.path.split(path)`   | `os.path.split(path)`   | Split path into dir & file    | _Razdvoji folder i fajl_      |
| `os.path.join(a, b)`    | `os.path.join(a, b)`    | Join paths safely             | _Bezbedno spoji putanje_      |
| `os.environ['PATH']`    | `os.environ['PATH']`    | Get environment PATH          | _Sistemska PATH promenljiva_  |
| `os.path.getsize(path)` | `os.path.getsize(path)` | File size in bytes            | _Veličina fajla u bajtima_    |

---

## 📌 Notes & Tips | _Beleške i saveti_

- Use `os.path.join()` instead of manual string concatenation (`/`, `\\`)  
  | _Koristi `os.path.join()` umesto ručnog spajanja stringova_ |
- Always check if a path exists before deleting or renaming  
  | _Uvek proveri da li putanja postoji pre brisanja ili preimenovanja_ |
- `os.environ` behaves like a dictionary  
  | _`os.environ` se ponaša kao rečnik_ |
- Avoid `os.rmdir()` on non-empty folders (use `shutil.rmtree()` instead)  
  | _`os.rmdir()` radi samo nad praznim folderima_ |

---

## 🧪 Test It Yourself | _Testiraj samostalno_

Use the following scripts from the project root:

```bash
python main.py
python bonus/snippets_os_demo.py
python bonus/path_debugger.py
```

---

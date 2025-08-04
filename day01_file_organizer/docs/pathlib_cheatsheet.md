# 🔗 Pathlib Cheatsheet | _Rad sa putanjama pomoću pathlib_

## ✅ Common Methods | _Česte metode koje se koriste_

| Method        | _Metoda_     | Explanation                         | _Objašnjenje_                         |
| ------------- | ------------ | ----------------------------------- | ------------------------------------- |
| `Path()`      | _Path()_     | Create a Path object                | _Kreiranje Path objekta_              |
| `.exists()`   | _exists()_   | Check if file/folder exists         | _Proverava da li fajl/folder postoji_ |
| `.is_file()`  | _is_file()_  | Check if path is a file             | _Proverava da li je fajl_             |
| `.is_dir()`   | _is_dir()_   | Check if path is a folder           | _Proverava da li je folder_           |
| `.suffix`     | _suffix_     | Gets the file extension             | _Dobija ekstenziju fajla_             |
| `.stem`       | _stem_       | Gets the filename without extension | _Ime fajla bez ekstenzije_            |
| `.resolve()`  | _resolve()_  | Returns absolute path               | _Vraća apsolutnu putanju_             |
| `.parent`     | _parent_     | Returns parent folder               | _Vraća roditeljski folder_            |
| `.name`       | _name_       | Returns filename                    | _Vraća ime fajla_                     |
| `.joinpath()` | _joinpath()_ | Appends subfolder or filename       | _Dodaje deo putanje_                  |

---

## 📌 Example | _Primer_

```python
from pathlib import Path

path = Path("example.txt")
if path.exists():
    print(f"{path.name} exists at {path.resolve()}")
```

📌 Checks if the file exists and displays the absolute path. | _Proverava da li fajl postoji i prikazuje apsolutnu putanju._

---

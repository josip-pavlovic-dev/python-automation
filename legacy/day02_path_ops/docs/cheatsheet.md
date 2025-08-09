# 📄 Cheatsheet | _Pregled najvažnijih izraza_

## ✅ Why use absolute paths? | _Zašto koristiti apsolutne putanje?_

- Prevents file not found errors when script is run from another directory. | _Sprečava greške kada se skripta pokrene iz drugog foldera._
- Makes the script portable and robust. | _Omogućava prenosivost i pouzdanost._
- Aids debugging and improves reliability. | _Olakšava debagovanje i povećava stabilnost._

## 📌 Explanation: | _Objašnjenje:_

### `__file__`

Returns the path of the current script. | _Vraća putanju do trenutno izvršavane skripte._

### `os.path.abspath(__file__)`

Returns the absolute path of the current file. | _Vraća apsolutnu putanju trenutnog fajla._

### `os.path.dirname(path)`

Returns the directory name of the given path. | _Vraća naziv direktorijuma iz date putanje._

### `os.path.join(dir, filename)`

Combines directory and file into a complete path. | _Spaja direktorijum i naziv fajla u potpunu putanju._

### `os.path.exists(path)`

Checks if the given path exists. | _Proverava da li data putanja postoji._

---

### `Path(__file__).resolve()`

Returns the absolute `Path` object of the script. | _Vraća apsolutni `Path` objekat skripte._

### `Path.parent`

Gets the parent folder of the current path. | _Dobija roditeljski folder trenutne putanje._

### `Path / "filename"`

Joins path and filename using `/`. | _Spaja putanju i fajl koristeći `/`._

### `with open(path, mode, encoding)`

Reads/writes file content safely. | _Sigurno čita/piše sadržaj fajla._

## 🔍 Key Syntax | _Ključna sintaksa_

```python
from pathlib import Path
script_path = Path(__file__).resolve()           # Absolute path to script | _Apsolutna putanja do skripte_
script_dir = script_path.parent                  # Folder where script is located | _Folder u kome se skripta nalazi_
input_file = script_dir / "input.txt"            # Full path to input file | _Puna putanja do ulaznog fajla_
```

```python
import os
script_path = os.path.abspath(__file__)                  # Absolute path to script | _Apsolutna putanja do skripte_
script_dir = os.path.dirname(script_path)                # Directory of script | _Direktorijum u kom je skripta_
file_path = os.path.join(script_dir, "data", "file.txt") # Joined path | _Spojena putanja_
```

## 📁 Typical usage pattern | _Tipičan obrazac korišćenja_

- Always calculate the absolute path from `__file__` to ensure portability. | _Uvek koristi `__file__` za izračunavanje apsolutne putanje zbog prenosivosti._
- Use `join()` or `/` operator to ensure OS-agnostic path construction. | _Koristi `join()` ili `/` operator za izgradnju putanja nezavisnu od OS-a._
- Use `.resolve()` to avoid symbolic link issues. | _Koristi `.resolve()` da izbegneš probleme sa simboličkim linkovima._

---

## 👨‍💻 Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-Josip_Pavlović-blue?logo=github)](https://github.com/Jole85)
[![Learning Path](https://img.shields.io/badge/Path-Python_Automation-orange)](https://github.com/Jole85/python-automation)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/josip-p-151951338/)

**Josip Pavlović — aspiring Python developer from Novi Sad**

---

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

## 🔍 Key Syntax | _Ključna sintaksa_

```python
import os

script_path = os.path.abspath(__file__)                      # Absolute path to the script | _Apsolutna putanja do skripte_
script_dir = os.path.dirname(script_path)                    # Folder where script is located | _Folder u kome se skripta nalazi_
input_path = os.path.join(script_dir, "input.txt")           # Full path to input.txt | _Puna putanja do input.txt fajla_
output_path = os.path.join(script_dir, "output.txt")         # Full path to output.txt | _Puna putanja do output.txt fajla_
```

## 📁 Typical usage pattern | _Tipičan obrazac korišćenja_

- Always calculate the absolute path from `__file__` to ensure portability. | _Uvek koristi `__file__` za izračunavanje apsolutne putanje zbog prenosivosti._
- Use `join()` to handle separators correctly on all OS. | _Koristi `join()` da bi se pravilno koristili separator-i na svim operativnim sistemima._

---

## 👨‍💻 Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-Jole85-blue?logo=github)](https://github.com/Jole85)[![Learning Path](https://img.shields.io/badge/Path-Python_Automation-orange)](https://github.com/Jole85/python-automation)  
📍 Aspiring Python Developer from Novi Sad  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/josip-p-151951338/)

---

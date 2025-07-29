# 📁 Directory Scanner – main.py | _Skener direktorijuma – main.py_

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-green)
![Level](https://img.shields.io/badge/Level-Beginner-blue)

---

## 🚀 Description | _Opis_

This script recursively scans a directory and lists all files with their **modification time**, grouped by subfolders. It's a foundational tool to explore **file metadata** and **directory walking** using Python's `os`, `datetime`, and `os.path` modules.

_Ova skripta rekurzivno skenira direktorijum i prikazuje sve fajlove sa vremenom poslednje izmene, grupisane po podfolderima. Osnovni je alat za razumevanje **metapodataka fajlova** i šetnje kroz direktorijume pomoću modula `os`, `datetime` i `os.path`._

---

## 🧩 Technologies Used | _Korišćene tehnologije_

- `os.walk()` to recursively scan directories | _rekurzivno skeniranje direktorijuma_
- `os.path.getmtime()` to get last modified time | _vreme poslednje izmene fajla_
- `datetime.fromtimestamp()` for formatting | _formatiranje UNIX timestampova_

---

## 📂 Input & Output | _Ulaz i izlaz_

- **Input**: path to a directory (hardcoded or via `input()`)
- **Output**: printed list of files with last modified timestamps

---

## 📦 Example Output | _Primer izlaza_

```
📂 Folder: ./docs

cheatsheet.md | Last modified: 2025-07-28 12:30:14
snippets.md | Last modified: 2025-07-28 12:29:02

📂 Folder: ./extra_task

helper.py | Last modified: 2025-07-28 11:45:20

```

## 📌 How to Run | _Kako pokrenuti_

```bash
python main.py
```

Or directly from VS Code using Run ▶️

---

## 📎 Related Documentation | _Povezana dokumentacija_

See the `docs/` folder:

- [`cheatsheet.md`](./docs/cheatsheet.md) – key functions used in this project
- [`snippets.md`](./docs/snippets.md) – useful code snippets for quick reference
- [`README.md`](./docs/README.md) – theoretical concepts covered in this task

---

## ✍️ Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-josip-pavlovic-blue?logo=github)](https://github.com/josip-pavlovic)
[![Learning](https://img.shields.io/badge/Path-Python_Automation-yellowgreen)](https://github.com/josip-pavlovic/python-automation)

_Aspiring Python developer from Novi Sad, transitioning from civil engineering._

---

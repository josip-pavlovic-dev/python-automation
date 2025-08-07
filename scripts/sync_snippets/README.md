# 🔄 sync*snippets | Sinhronizacija VS Code snippetsa*

Ova skripta automatski kopira sve `.code-snippets` fajlove iz `docs/vs-snippets/` u `.vscode/` folder repozitorijuma, tako da su ti snippet-i dostupni unutar VS Code editora.

---

## 📂 Struktura foldera

```

scripts/
└── sync_snippets/
    ├── sync_snippets.py   # Glavna Python skripta
    ├── sync_snippets.bat  # Batch fajl za Windows
    ├── sync_snippets.ps1  # PowerShell alternativa
    └── README.md          # Ovaj fajl

```

---

## 📌 Purpose

This tool eliminates repetitive manual work by:

- Creating `.vscode/` folders if missing
- Copying matching `.code-snippets` files (EN and SR versions) into each project
- Keeping your snippet structure clean and synchronized

---

## 🗂️ Folder Structure Expected

```
python-automation/
├── docs/
│   └── vs-snippets/
│       ├── day01_file_organizer.code-snippets
│       ├── day01_file_organizer_sr.code-snippets
│       ├── ...
│
│
├── day01_file_organizer/
├── day02_file_info/
├── day03_file_management/
└── day04_datetime/

```

Each project will receive its matching `.code-snippets` files in its `.vscode/` subfolder.

---

## ⚙️ How to Use

1. Copy `sync_snippets.py` to the root of `python-automation`:

   ```
   C:\Users\JoleDev\dev-learning\python-automation\sync_snippets.py
   ```

2. Open a terminal and run:

   ```bash
   python sync_snippets.py
   ```

3. The script will automatically:
   - Look for each `project: snippet_prefix` pair
   - Copy `*.code-snippets` from `docs/vs-snippets/`
   - Output a log of success or missing files

---

## ✅ Status

| Feature                              | Supported               |
| ------------------------------------ | ----------------------- |
| English snippets `.code-snippets`    | ✅ Yes                  |
| Serbian snippets `_sr.code-snippets` | ✅ Yes                  |
| Auto-create `.vscode/` folders       | ✅ Yes                  |
| Customizable paths                   | 🟡 Manual (edit script) |

---

## 🧠 Author’s Note

This script is tailored for the personal setup of [Josip Pavlović](https://github.com/josip-pavlovic-dev), but it’s a solid baseline for any structured Python learning environment.  
Ideal if you're maintaining multiple projects and want to keep `.code-snippets` clean and in sync.

---

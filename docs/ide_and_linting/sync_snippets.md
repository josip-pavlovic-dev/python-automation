# 🛠️ sync_snippets.py

> A utility script that automates the synchronization of `.code-snippets` files across all active Python automation project folders.  
> Ideal for structured development environments like `python-automation/`.

---

## 📌 Purpose

This tool eliminates repetitive manual work by:

- Creating `.vscode/` folders if missing
- Copying matching `.code-snippets` files (EN and SR versions) into each project
- Keeping your snippet structure clean and synchronized

---

## 🗂️ Folder Structure Expected

```

dev-learning/
└── python-automation/
├── docs/
│   └── vs-snippets/
│       ├── day01\_file\_organizer.code-snippets
│       ├── day01\_file\_organizer\_sr.code-snippets
│       ├── ...
├── 01-file-organizer/
├── day02\_file\_info/
├── day03\_file\_management/
└── day04\_datetime/

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

This script is tailored for the personal setup of [JoleDev](https://github.com/Jole85), but it’s a solid baseline for any structured Python learning environment.  
Ideal if you're maintaining multiple projects and want to keep `.code-snippets` clean and in sync.

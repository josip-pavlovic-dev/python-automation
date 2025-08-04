# 🛠️ Bash Script Templates | _Bash skript šabloni_

## 📂 File: `generate_project_structure.sh`

### 🎯 Purpose | _Svrha_

Automates the creation of a standardized folder and file structure for Python mini-projects using `src/`, `docs/`, and other directories.

_Automatski kreira standardizovanu strukturu foldera i fajlova za Python mini-projekte sa `src/`, `docs/` i ostalim direktorijumima._

---

## ⚙️ Command Example | _Primer komande_

```bash
./generate_project_structure.sh day01_file_organizer
```

This will generate a project folder named `day01_file_organizer` with the following structure:

_Kreiraće folder projekta sa sledećom strukturom:_

```
day01_file_organizer/
├── src/
│   ├── main.py
│   ├── logger.py
│   └── utils/
│       └── interactive_folder_browser.py
├── docs/
│   ├── README.md
│   ├── snippets.md
│   ├── cheatsheet.md
│   └── line_by_line.md
├── assets/
├── test_files/
└── .vscode/
```

---

## 📜 Script Overview | _Pregled skripte_

- ✅ Takes one argument – project folder name (e.g. `day01_file_organizer`)
- ✅ Creates full folder tree
- ✅ Generates bilingual `.md` files and starter Python files
- ✅ Uses `Path.mkdir()` for safe directory creation
- ✅ Uses heredoc to populate template files

---

## 🧠 Notes | _Napomene_

- Script should be saved in `scripts/` folder
- Run it from Git Bash or WSL with `chmod +x generate_project_structure.sh`
- Extend script to include `.gitignore`, test folders, or default README content if needed

---

## 🧰 Author | _Autor_

- Josip Pavlović – aspiring Python developer from Novi Sad
- [GitHub Profile](https://github.com/Jole85)
- _Repo: `python-automation`_

---

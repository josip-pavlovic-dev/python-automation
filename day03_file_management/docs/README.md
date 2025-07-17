# 🗃️ Project: day03_file_management

[![Scripts](https://img.shields.io/badge/scripts-6-green?style=flat-square)](../scripts)
[![Docs](https://img.shields.io/badge/docs-cheatsheets-blue?style=flat-square)](docs/)
[![License](https://img.shields.io/github/license/Jole85/python-automation?style=flat-square)](../../LICENSE)
![copilot.yaml configured](./assets/copilot_badge.svg)
---

## 🧭 🇬🇧: Purpose | 🇷🇸: Svrha

#### 🇬🇧: This project focuses on automating file and folder management using Python CLI tools. Scripts support tasks like cleaning old files, scanning directory contents, logging actions, generating image reports, and more.

#### 🇷🇸: Projekat se bavi automatizacijom upravljanja fajlovima i folderima pomoću Python alata za komandnu liniju. Skripte pokrivaju čišćenje starih fajlova, skeniranje direktorijuma, logovanje, generisanje izveštaja o slikama i drugo.

---

## 📜 🇬🇧: Script Overview | 🇷🇸: Pregled skripte

| Script / Skripta | Description / Opis |
|--------|-------------|
| `cleaner.py` | Delete files by size or age / Briše fajlove prema veličini ili starosti |
| `scanner.py` | Generate tree of folder contents / Generiše celokupno stablo sadržaja foldera |
| `size_cleaner.py` | Delete files larger than a given size / Briše fajlove veće od zadane veličine |
| `file_structure_creator.py` | Create custom test folder structure / Kreira prilagođenu strukturu test foldera sa podfolderima i fajlovima |
| `logger.py` | Unified logging utility / Unified logging uslužni program |
| `image_report.py` | Collect and export image metadata / Prikuplja i izvozi metapodataka slika |

---

## 📄 Cheatsheets

#### 🇬🇧: All cheatsheets are bilingual and stored in [`docs/`](../docs/):
#### 🇷🇸: Svi cheatsheetovi su dvojezični i pohranjeni u [`docs/`](../docs/):

- [`cleaner_cheatsheet.md`](./cleaner_cheatsheet.md)
- [`scanner_cheatsheet.md`](./scanner_cheatsheet.md)
- [`logger_cheatsheet.md`](./logger_cheatsheet.md)
- [`file_structure_creator_cheatsheet.md`](./file_structure_creator_cheatsheet.md)
- [`image_report_cheatsheet.md`](./image_report_cheatsheet.md)
- [`size_cleaner_cheatsheet.md`](./size_cleaner_cheatsheet.md)
- [`setup_test_folder_cheatsheet.md`](./setup_test_folder_cheatsheet.md)

---

## 🧪 🇬🇧: Testing and Setup | 🇷🇸: Testiranje i Podešavanje

```bash
cd day03_file_management
python setup_test_folder.sh   # 🇬🇧: Generate test folder structure | 🇷🇸: Generiše strukturu test foldera
python cleaner.py             # 🇬🇧: Run example script | 🇷🇸: Primer pokretanja skripte
```
#### 🇬🇧: ✅ Make sure to activate your virtual environment and install `Pillow` if using `image_report.py`.
#### 🇷🇸: ✅ Obavezno aktivirajte svoje virtualno okruženje i instalirajte `Pillow` ako koristite `image_report.py`.

---

## 📁 🇬🇧: Folder Structure | 🇷🇸: Struktura Projekta

```bash
day03_file_management/
├── docs/
├── scripts/
├── test_folder/
│   ├── docs/
│   ├── images/
│   └── ...
├── log.txt
└── *.py
```

---

## 🔁 🇬🇧: Reusability & Modularity | 🇷🇸: Ponovna upotrebljivost i modularnost

#### 🇬🇧: Scripts are written modularly and reusable across other automation tasks. This project serves as a practical foundation for building advanced CLI tools for automation pipelines.
#### 🇷🇸: Skripte su napisane modularno i mogu se ponovo koristiti u drugim zadacima automatizacije. Ovaj projekat služi kao praktična osnova za izgradnju naprednih CLI alata za procese automatizacije.

---

## 👤 🇬🇧: Author | 🇷🇸: Autor
### Josip Pavlović
#### 📧 [jolepavlovic@outlook.com](mailto:jolepavlovic@outlook.com)
#### 🌍 Novi Sad, Serbia
#### 💼 [github.com/Jole85](https://github.com/Jole85)
---


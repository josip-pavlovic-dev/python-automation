# 🗃️ Project: day03_file_management

[![Status](../assets/day03_status.svg)](./README.md)
[![📘 Career Notes](../../assets/career_notes_badge.svg)](../../docs/career_notes.md)
[![👤 Developer Profile](../../assets/dev_profile_badge.svg)](../../docs/developer_profile.md)
![copilot.yaml configured](../../assets/copilot_badge.svg)
[![Scripts](https://img.shields.io/badge/scripts-6-green?style=flat-square)](../scripts)
[![Docs](https://img.shields.io/badge/docs-cheatsheets-blue?style=flat-square)](../docs/)
[![License](https://img.shields.io/github/license/Jole85/python-automation?style=flat-square)](../../LICENSE)

---

## 🧭 🇬🇧: Purpose | 🇷🇸: Svrha

#### 🇬🇧: This project focuses on automating file and folder management using Python CLI tools. It includes scripts for cleanup, scanning, structure generation, and image metadata extraction.

#### 🇷🇸: Projekat se fokusira na automatizaciju upravljanja fajlovima i folderima koristeći Python skripte u komandnoj liniji. Obuhvata čišćenje, skeniranje, generisanje strukture i izdvajanje metapodataka iz slika.

---

## 📜 🇬🇧: Script Overview | 🇷🇸: Pregled skripti

| Script / Skripta            | Description / Opis                                                               |
| --------------------------- | -------------------------------------------------------------------------------- |
| `cleaner.py`                | Delete files by size or age / Briše fajlove po veličini ili starosti             |
| `scanner.py`                | Generate directory tree / Generiše strukturu foldera                             |
| `size_cleaner.py`           | Delete files larger than threshold / Briše fajlove preko određene veličine       |
| `file_structure_creator.py` | Create test folder structure / Kreira test strukturu foldera                     |
| `logger.py`                 | Logging utility / Modul za logovanje                                             |
| `image_report.py`           | Extract image metadata using Pillow / Izvlači metapodatke iz slika pomoću Pillow |
| `setup_test_folder.sh`      | Bash script for test folder creation / Bash skripta za kreiranje foldera         |

---

## 📄 🇬🇧: Cheatsheets (Docs) | 🇷🇸: Objašnjenja (Dokumentacija)

```bash
day03_file_management/docs/
├── cleaner_cheatsheet.md
├── file_structure_creator_cheatsheet.md
├── image_report_cheatsheet.md
├── logger_cheatsheet.md
├── scanner_cheatsheet.md
├── setup_test_folder_cheatsheet.md
├── size_cleaner_cheatsheet.md
└── README.md
```

---

## 🧪 🇬🇧: Test Scripts | 🇷🇸: Test Skripte

```bash
tests/test_day03_file_management/
├── test_cleaner.py
├── test_file_structure_creator.py
├── test_image_report.py
├── test_logger.py
├── test_scanner.py
├── test_size_cleaner.py
└── test_main.py
```

---

## 🧪 🧰 🇬🇧: Setup & Run | 🇷🇸: Pokretanje i Podešavanje

```bash
cd day03_file_management
python ../../tests/test_day03_file_management/test_main.py
```

> 🧪 **Note:** Activate your virtual environment before running.
>
> 🧪 **Napomena:** Aktiviraj virtualno okruženje pre pokretanja.

Install Pillow (if not installed):

```bash
pip install Pillow
```

---

## 📁 🇬🇧: Folder Structure | 🇷🇸: Struktura Projekta

```bash
day03_file_management/
├── assets/
│   ├── [screenshots, diagrams...]
│
├── docs/
│   ├── cleaner_cheatsheet.md
│   ├── file_structure_creator_cheatsheet.md
│   ├── image_report_cheatsheet.md
│   ├── logger_cheatsheet.md
│   ├── scanner_cheatsheet.md
│   ├── setup_test_folder_cheatsheet.md
│   ├── size_cleaner_cheatsheet.md
│   └── README.md
│
├── test_folder/
│   ├── docs/
│   └── images/
│
├── cleaner.py
├── scanner.py
├── size_cleaner.py
├── file_structure_creator.py
├── logger.py
├── image_report.py
├── setup_test_folder.sh
├── log.txt
└── README.md

tests/
└── test_day03_file_management/
    ├── test_cleaner.py
    ├── test_file_structure_creator.py
    ├── test_image_report.py
    ├── test_logger.py
    ├── test_scanner.py
    ├── test_size_cleaner.py
    └── test_main.py
```

---

## 🧠 🇬🇧: Notes | 🇷🇸: Napomene

- ✅ Scripts are organized by use case and logically grouped
- ✅ Test coverage is complete and centralized in one test suite
- ✅ Markdown cheatsheets and visual assets (screenshots) included for documentation
- ✅ Log file `log.txt` is dynamically generated during script execution

---

## 👤 🇬🇧: Author | 🇷🇸: Autor

### Josip Pavlović

📧 [jolepavlovic@outlook.com](mailto:jolepavlovic@outlook.com)
🌍 Novi Sad, Serbia
💼 [github.com/Jole85](https://github.com/Jole85)

---

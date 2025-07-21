## 📁 Folder Structure | Struktira Projekta

🇬🇧 **Project layout with clearly defined roles for each folder and script.**
🇷🇸 **Struktura projekta sa jasno definisanim ulogama za svaki folder i skriptu.**

```bash
day03_file_management/
├── assets/                       # 📂 Screenshots, diagrams, visual content
│   └── [screenshots, diagrams...] # 📂 Screenshot-ovi, dijagrami, vizuelni sadrzaj
│
├── docs/                         # 📑 Documentation for each Python script
│   ├── cleaner_cheatsheet.md     # 📑 Dokumentacija za svaku Python skriptu
│   ├── file_structure_creator_cheatsheet.md
│   ├── image_report_cheatsheet.md
│   ├── scanner_cheatsheet.md
│   ├── setup_test_folder_cheatsheet.md
│   ├── size_cleaner_cheatsheet.md
│   └── README.md                 # 📘 Indeks dokumentacije
│
├── test_folder/                 # 📂 Primer test sadrzaja koji koriste skripte
│   ├── docs/
│   └── images/
│
├── cleaner.py                   # 🧹 Briše stare ili nepotrebne fajlove
├── scanner.py                   # 🔍 Analizira strukturu foldera
├── size_cleaner.py              # 🧼 Briše fajlove koji prelaze zadatu veličinu
├── file_structure_creator.py    # 🏗️ Kreira primer strukture foldera i fajlova
├── logger.py                    # 📝 Modul za logovanje koji se ponovo koristi
├── image_report.py              # 🖼️ Generiše izveštaj o slikama i metapodacima
├── setup_test_folder.sh         # ⚙️ Bash skripta za kreiranje test okruženja
├── log.txt                      # 📄 Izlazni fajl logger-a
└── README.md                    # 📘 Glavna dokumentacija za projekat

tests/
└── test_day03_file_management/  # 🧪 Unit testovi za sve skripte
    ├── test_cleaner.py
    ├── test_file_structure_creator.py
    ├── test_image_report.py
    ├── test_logger.py
    ├── test_scanner.py
    └── test_size_cleaner.py

```

---

## 📘 docs/README.md — 🧭 Documentation Index | Indeks Dokumentacije

| File                                                                         | 🇬🇧 Description                | 🇷🇸 Opis                                       |
| ---------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------- |
| [cleaner_cheatsheet.md](cleaner_cheatsheet.md)                               | Delete files by age           | Brisanje starih fajlova po kriterijumu datuma |
| [file_structure_creator_cheatsheet.md](file_structure_creator_cheatsheet.md) | Create test file structure    | Kreiranje strukture za testiranje             |
| [image_report_cheatsheet.md](image_report_cheatsheet.md)                     | Extract metadata from images  | Izdvajanje metapodataka iz slika              |
| [scanner_cheatsheet.md](scanner_cheatsheet.md)                               | Analyze folders/files         | Skeniranje strukture foldera                  |
| [setup_test_folder_cheatsheet.md](setup_test_folder_cheatsheet.md)           | Bash script to setup test env | Shell skripta za kreiranje test okruženja     |
| [size_cleaner_cheatsheet.md](size_cleaner_cheatsheet.md)                     | Delete large files            | Brisanje fajlova po veličini                  |

📌 **🇬🇧 Note:** The `logger.py` module is shared across multiple projects. More info in [logger_cheatsheet.md](../../docs/logger_cheatsheet.md)
📌 **🇷🇸 Napomena:** `logger.py` je zajednički modul za logovanje i koristi se u više projekata. Pogledaj [logger_cheatsheet.md](../../docs/logger_cheatsheet.md)

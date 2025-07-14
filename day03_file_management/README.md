# 📁 Day 3 – File and Directory Management | 📁 Dan 3 – Rad sa fajlovima i direktorijumima

## 🎯 Project Goals | 🎯 Ciljevi Projekta

**EN:**  
This project focuses on mastering file and directory manipulation in Python using modules such as `os`, `shutil`, and `logging`. The goal was to build scripts that automate common filesystem tasks like structure creation, cleanup by extension or size, and logging all activities with clear traceability.

**SR (latinica):**  
Ovaj projekat je usmeren na savladavanje manipulacije fajlovima i direktorijumima u Python-u pomoću modula `os`, `shutil` i `logging`. Cilj je bio razviti skripte koje automatizuju česte zadatke u radu sa fajl sistemima — od kreiranja strukture, preko čišćenja po ekstenziji i veličini, do logovanja svih aktivnosti radi jasnog praćenja.

---

## 📚 Concepts Covered | 📚 Obrađene Teme

**EN:**  
- Creating, deleting, and navigating directories with `os` and `shutil`  
- Programmatic file structure creation  
- Automated cleanup scripts by file type and size  
- Logging with timestamp using custom modules  
- Bash automation and subprocess integration  
- Safe error handling with `try`, `except`, `raise`

**SR (latinica):**  
- Kreiranje, brisanje i navigacija kroz direktorijume pomoću `os` i `shutil`  
- Programatsko kreiranje strukture foldera  
- Automatizovano čišćenje fajlova po tipu i veličini  
- Logovanje sa vremenskom oznakom uz pomoć sopstvenog modula  
- Automatizacija bash skripti i rad sa `subprocess` modulom  
- Bezbedno rukovanje greškama (`try`, `except`, `raise`)

---

## ✅ Daily Tasks | ✅ Dnevni Zadaci

### `file_structure_creator.py`  
**EN:** Creates folder tree with test files  
**SR:** Kreira strukturu foldera sa test fajlovima

### `cleaner.py`  
**EN:** Deletes files by extension (e.g., `.tmp`)  
**SR:** Briše fajlove određene ekstenzije (npr. `.tmp`)

### `size_cleaner.py`  
**EN:** Deletes files smaller than specified size (e.g., <100 bytes)  
**SR:** Briše fajlove manje od zadate veličine (npr. <100 bajtova)

### `scanner.py`  
**EN:** Recursively scans folder and logs file counts by extension  
**SR:** Rekurzivno skenira folder i loguje broj fajlova po tipu

### `logger.py`  
**EN:** Central logging module for consistent message formatting  
**SR:** Centralni log modul za konzistentno formatiranje poruka

### `test_logger.py`, `test_size_cleaner.py`  
**EN:** Test scripts for verifying logger and cleanup scripts  
**SR:** Test skripte za proveru logger-a i skripti za čišćenje

### `setup_test_folder.sh`  
**EN:** Bash script for automated folder reset before test  
**SR:** Bash skripta za automatsko resetovanje foldera pre testa

---

## 🧠 What I Learned | 🧠 Šta sam naučio

- EN: Usage of modules like `os`, `shutil`, `logging`, and `subprocess`  
- SR: Korišćenje modula kao što su `os`, `shutil`, `logging` i `subprocess`  
- EN: Writing clean and modular Python scripts  
- SR: Pisanje čitljivih i modularnih Python skripti  
- EN: Testing scripts using bash and subprocess automation  
- SR: Testiranje skripti pomoću bash-a i subprocess automatizacije

🗒️ Logging and Error Handling | 🗒️ Logovanje i Rukovanje Greškama

- EN:
    1. Introduced a reusable `logger.py` module that logs messages with timestamps to `log.txt`, helping with debugging and tracing program flow.
    2. Practiced `try`, `except`, and `raise` for safe runtime error handling.

- SR:
    1. Uveden je višekratno upotrebljiv modul `logger.py` koji beleži poruke sa vremenskom oznakom u fajl `log.txt`, što olakšava debagovanje i praćenje toka programa.
    2. Vežbano je korišćenje `try`, `except` i `raise` za bezbedno hvatanje i obradu grešaka.

---

## 📂 Folder Structure | 📂 Struktura Foldera

```
day03_file_management/
├── test_folder/
├── cleaner.py
├── file_structure_creator.py
├── image_report.py      # ⏳ Work in progress
├── log.txt
├── logger.py
├── scanner.py
├── setup_test_folder.sh
├── size_cleaner.py
├── test_logger.py
├── test_size_cleaner.py
├── README.md
```

---

## 🛠️ Usage | 🛠️ Korišćenje

**EN:** Run the test script to prepare the test folder and clean files under certain size:
```bash
python test_size_cleaner.py
```

**SR:** Pokreni test skriptu da pripremiš folder i obrišeš fajlove ispod određene veličine:
```bash
python test_size_cleaner.py
```

📝 **Note / Napomena:** Section for `image_report.py` will be updated after its completion.

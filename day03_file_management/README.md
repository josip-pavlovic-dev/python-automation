# 📁 Day 3 – File and Directory Management | 📁 Dan 3 – Rad sa fajlovima i direktorijumima

## 📚 Concepts Covered | 📚 Obrađene Teme

**EN:**  
- Creating, deleting, and navigating directories with `os` and `shutil`  
- Programmatic file structure creation  
- Automated cleanup scripts  
- Iterating through files and calculating file sizes  

**SR (latinica):**  
- Kreiranje i brisanje foldera pomoću `os` i `shutil` modula  
- Automatsko kreiranje strukture foldera  
- Skripte za automatsko brisanje fajlova  
- Prolazak kroz fajlove i izračunavanje njihove veličine  

---

## ✅ Daily Tasks | ✅ Zadaci

### `file_structure_creator.py`  
**EN:** Creates test folder with subfolders and `.txt` files  
**SR:** Kreira test_folder sa podfolderima i tekstualnim fajlovima

### `cleaner.py`  
**EN:** Deletes `.txt` files and empty folders  
**SR:** Briše `.txt` fajlove i prazne foldere

### `image_report.py`  
**EN:** Scans for `.jpg` and `.png` files and prints their size in KB  
**SR:** Pronalazi `.jpg` i `.png` fajlove i prikazuje njihovu veličinu u KB

---

## 🧠 What I Learned | 🧠 Šta sam naučio

- EN: Usage of modules like `os`, `shutil`, `logging`, and `subprocess`  
- SR: Korišćenje modula kao što su `os`, `shutil`, `logging` i `subprocess`  
- EN: Writing clean and modular Python scripts  
- SR: Pisanje čitljivih i modularnih Python skripti  
- EN: Testing scripts using bash and subprocess automation  
- SR: Testiranje skripti pomoću bash-a i subprocess automatizacije

---

## 📂 Folder Structure | 📂 Struktura Foldera

```
day03_file_management/
├── __pycache__/
├── test_folder/
├── cleaner.py
├── file_structure_creator.py
├── image_report.py
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
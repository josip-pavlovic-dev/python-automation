# 🧪 Test Folder Documentation — `python-automation/tests/`

> 📄 **SRPSKI / SERBIAN BELOW** ↓↓↓

This document describes the structure and organization of all tests within the `python-automation` repository. The goal is to provide a clear overview of how tests relate to the modules they cover.

---

## 📁 Folder Structure

```
python-automation/
├── tests/
│   ├── test_day01_file_organizer/
│   │   └── test_organizer.py
│   ├── test_day02_file_info/
│   │   └── test_info_report.py
│   ├── test_day03_file_management/
│   │   ├── test_cleaner.py
│   │   ├── test_logger.py
│   │   └── test_size_cleaner.py
│   └── test_day04_datetime/
│       └── test_timestamp_generator.py
```

---

## 📌 Organization Rules

- Each `dayXX_...` project folder has a corresponding test folder: `test_dayXX_...`.
- Test files follow the `test_*.py` naming pattern.
- All tests use the built-in `unittest` framework.
- Run all tests with:

```bash
python -m unittest discover -s tests
```

---

## 🧩 Current Contents of `tests/`

### 📂 test_day01_file_organizer

- `test_organizer.py`: tests for file-sorting logic from `main.py`

### 📂 test_day02_file_info

- `test_info_report.py`: tests info extraction about files

### 📂 test_day03_file_management

- `test_cleaner.py`: tests deletion logic for old files
- `test_logger.py`: tests logging system (generates and checks `log.txt`)
- `test_size_cleaner.py`: tests size-based file removal logic

### 📂 test_day04_datetime

- `test_timestamp_generator.py`: tests the `generate_timestamps()` function

---

## 🔄 TODO / Planned Expansion

- Add tests for `file_structure_creator.py`
- Introduce `mock` for API/log testing
- Automate test setup/teardown logic

---

## 🧪 Run from `launch.json`

Add to your configuration:

```json
{
  "name": "🧪 Run all tests",
  "type": "python",
  "request": "launch",
  "module": "unittest",
  "args": ["discover", "-s", "tests"],
  "console": "integratedTerminal"
}
```

---

> 📁 This file is stored at: `tests/README.md` Treat it as the **entry point for test navigation and documentation**.

---

---

# 🧪 Dokumentacija za folder `tests/` — `python-automation/tests/`

Ovaj dokument opisuje strukturu i organizaciju svih testova unutar repozitorijuma `python-automation`. Cilj je omogućiti jasan pregled veza između testova i modula koje testiraju.

---

## 📁 Struktura foldera

```
python-automation/
├── tests/
│   ├── test_day01_file_organizer/
│   │   └── test_organizer.py
│   ├── test_day02_file_info/
│   │   └── test_info_report.py
│   ├── test_day03_file_management/
│   │   ├── test_cleaner.py
│   │   ├── test_logger.py
│   │   └── test_size_cleaner.py
│   └── test_day04_datetime/
│       └── test_timestamp_generator.py
```

---

## 📌 Pravila organizacije

- Svaki `dayXX_...` folder iz glavnog projekta ima svoj test-folder `test_dayXX_...`.
- Test fajlovi nose prefiks `test_` i testiraju konkretne module.
- Testovi koriste `unittest` framework.
- Test fajlovi se pokreću komandom:

```bash
python -m unittest discover -s tests
```

---

## 🧩 Trenutni sadržaj `tests/`

### 📂 test_day01_file_organizer

- `test_organizer.py`: testira sortiranje fajlova iz `main.py`

### 📂 test_day02_file_info

- `test_info_report.py`: testira ekstrakciju informacija o fajlovima

### 📂 test_day03_file_management

- `test_cleaner.py`: proverava logiku brisanja starih fajlova
- `test_logger.py`: testira `logger.py`, simulira `log.txt`
- `test_size_cleaner.py`: testira logiku brisanja fajlova po veličini

### 📂 test_day04_datetime

- `test_timestamp_generator.py`: testira `generate_timestamps()` funkciju

---

## 🔄 TODO / plan proširenja

- Dodati testove za `file_structure_creator.py`
- Uvesti `mock` testove za API pozive i logovanje
- Automatizovati test setup i teardown (npr. brisanje test fajlova)

---

## 📌 Pokretanje iz `launch.json`

Dodati konfiguraciju:

```json
{
  "name": "🧪 Run all tests",
  "type": "python",
  "request": "launch",
  "module": "unittest",
  "args": ["discover", "-s", "tests"],
  "console": "integratedTerminal"
}
```

---

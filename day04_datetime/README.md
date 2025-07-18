# Day 04 – Working with `datetime` in Automation / Rad sa `datetime` modulom

[![Status](./assets/day04_status.svg)](./README.md)
[![👤 Developer Profile](../assets/dev_profile_badge.svg)](../docs/developer_profile.md)
[![📘 Career Notes](../assets/career_notes_badge.svg)](../docs/career_notes.md)

## 🧠 Summary / Rezime

### 🇬🇧: This day focuses on learning and applying the `datetime` and `timedelta` modules in Python to automate tasks involving time and date operations. You will also use previously learned modules like `os` to interact with the filesystem.
### 🇷🇸: Ovaj dan je posvećen učenju i primeni `datetime` i `timedelta` modula u Pythonu za automatizaciju zadataka koji uključuju operacije sa datumima i vremenima. Takođe koristiš prethodno naučene module kao što je `os` za rad sa fajl sistemom.

---

## 📂 Project Structure / Struktura projekta

```
day04_datetime/
├── timestamp_generator.py         # Task 1
├── dated_folder_creator.py        # Task 2
├── old_file_checker.py            # Task 3
└── README.md                      # Documentation
```

---

## ✅ Tasks / Zadaci

### 1. `timestamp_generator.py`

#### 🇬🇧: Write a function that generates filenames with the current timestamp (e.g., `log_2025-07-17_19-00-00.txt`).
#### 🇷🇸: Napiši funkciju koja generiše ime fajla sa trenutnim vremenom (npr. `log_2025-07-17_19-00-00.txt`).

---

### 2. `dated_folder_creator.py`

### 🇬🇧: Create a folder named with today's date inside an `output/` folder (e.g., `output/2025-07-17`).
### 🇷🇸: Kreiraj folder sa današnjim datumom unutar `output/` foldera (npr. `output/2025-07-17`).

---

### 3. `old_file_checker.py`

### 🇬🇧: Write a script that lists all files older than X days in a given directory.
### 🇷🇸: Napiši skriptu koja izlistava sve fajlove starije od X dana u određenom folderu.

---

## 🖼️ Screenshots / Sekcija za slike

### 🇷🇸: Dodaj sledeće screenshot-ove kada završiš kodiranje:

1. 📸 `VSCode Terminal` – prikaz komandi `touch`, `mkdir`, `ls` koje si koristio
2. 📸 `Explorer View` – struktura foldera u VSCode-u
3. 📸 `Running Script` – pokretanje jedne od skripti i ispis u terminalu
4. 📸 `output/ folder` – prikaz automatski kreiranog foldera sa današnjim datumom
5. 📸 `log filename preview` – prikaz generisanog imena fajla u kodu

---

## 💬 Notes / Beleške
#### 🇷🇸:
* Koristi `datetime.now()`, `timedelta`, `os.path.getmtime()` i `os.makedirs()`
* Fokus je na **pisanju funkcija i testiranju u terminalu**, bez tutorijala
* Ako zapneš, koristi `help(datetime)` i `dir(datetime)` u Python-u za dodatno razumevanje

---

🟢 *Project created on: 2025-07-17*
📍 *Author: Jole – Python Automation Journey*



# 📘 Documentation Index | Indeks Dokumentacije

#### 🇬🇧 Welcome to the documentation folder for day04_datetime.Here you'll find cheatsheets and explanations for each script and module used in this project.

#### 🇷🇸 Dobro došli u dokumentaciju za day04_datetime. Ovde se nalaze objašnjenja i kratki podsetnici za sve skripte i module korišćene u projektu.

| File                                                                     | 🇬🇧 Description                  | 🇷🇸 Opis                                       |
| ------------------------------------------------------------------------ | ------------------------------- | --------------------------------------------- |
| [dated_folder_creator_cheatsheet.md](dated_folder_creator_cheatsheet.md) | Create folder with current date | Kreira folder sa trenutnim datumom            |
| [old_file_checker_cheatsheet.md](old_file_checker_cheatsheet.md)         | Detect old files by age         | Otkrivanje starih fajlova na osnovu datuma    |
| [timestamp_generator_cheatsheet.md](timestamp_generator_cheatsheet.md)   | Generate timestamp for naming   | Generisanje vremenske oznake za imenovanje    |
| [datetime_module_cheatsheet.md](datetime_module_cheatsheet.md)           | Overview of `datetime` module   | Pregled modula `datetime` i njegovih funkcija |

---

## 📆 datetime Module Cheatsheet

#### 🇬🇧 **Purpose:** The `datetime` module supplies classes for manipulating dates and times.

#### 🇷🇸 **Svrha:** Modul `datetime` omogućava rad sa datumima i vremenom.

---

## ⏰ Common Classes | Uobičajene klase

- `datetime.date`: samo datum (godina, mesec, dan)
- `datetime.time`: samo vreme (sat, minut, sekunda, mikrosekunda)
- `datetime.datetime`: pun datum i vreme
- `datetime.timedelta`: razlika između dva datuma/vremena
- `datetime.tzinfo`: informacije o vremenskim zonama (napredno)

---

## 🧪 Examples | Primeri

### 📍 `datetime.now()`

```python
from datetime import datetime
now = datetime.now()
print(now)  # npr. 2025-07-21 15:12:38.123456
```

### 🕓 `strftime()` – Formatiranje datuma

```python
from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```

### 📅 `strptime()` – Parsiranje stringa u datum

```python
from datetime import datetime
date_obj = datetime.strptime("2025-07-21", "%Y-%m-%d")
print(date_obj)
```

### ➕ `timedelta` – Rad sa vremenskim razlikama

```python
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)
```

---

#### 🇬🇧 **Screenshot Suggestion:** Screenshot showing output of various `datetime` formats.

#### 🇷🇸 **Predlog za sliku:** Snimak ekrana koji prikazuje različite formate datuma i vremena.

---

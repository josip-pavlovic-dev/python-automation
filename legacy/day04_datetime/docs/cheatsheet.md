# 🧠 datetime_module_cheatsheet.md — Essential Concepts |Ključni Koncepti

#### 🇬🇧: A practical overview of the most useful features of the `datetime` module in Python. Focused on real-world usage in file automation.

#### 🇷🇸: Praktičan pregled najkorisnijih funkcija iz `datetime` modula u Python-u, sa fokusom na realnu primenu u automatizaciji fajlova.

### 📅 `datetime.datetime`

```python
from datetime import datetime

now = datetime.now()
print(now)  # 2025-07-21 10:25:38.128391
```

#### 🇬🇧: Represents both date and time.

#### 🇷🇸: Predstavlja i datum i vreme.

**Common Methods | Česte metode**:

- `now()` — 🇬🇧 current local time | 🇷🇸 tekuće lokalno vreme
- `today()` — 🇬🇧 current date & time (same as now) | 🇷🇸 današnji datum i vreme
- `strftime('%Y-%m-%d')` — 🇬🇧 format datetime | 🇷🇸 formatiranje datuma
- `fromisoformat('2025-07-21')` — 🇬🇧 ISO to datetime | 🇷🇸 ISO u datetime

---

### 📆 `datetime.date`

```python
from datetime import date

today = date.today()
print(today)  # 2025-07-21
```

- 🇬🇧: Represents a date without time.
- 🇷🇸: _Predstavlja datum bez vremena._

**Methods | Metode**:

- `date(year, month, day)`
- `today()` — 🇬🇧 today’s date | 🇷🇸 današnji datum
- `isoformat()` — 🇬🇧 to ISO string | 🇷🇸 u ISO string
- `weekday()` — 🇬🇧 0=Monday | 🇷🇸 0=Ponedeljak

---

### ⏰ `datetime.time`

```python
from datetime import time

t = time(14, 30)
print(t)  # 14:30:00
```

#### 🇬🇧: Represents only the time (hour, minute...)

#### 🇷🇸: Predstavlja samo vreme (sat, minut...)

---

### 🔁 `datetime.timedelta`

```python
from datetime import timedelta

delta = timedelta(days=5)
print(delta)  # 5 days
```

#### 🇬🇧: Duration or difference between dates/times

#### 🇷🇸: Trajanje ili razlika između datuma/vremena

**Use cases | Primeri upotrebe**:

```python
from datetime import datetime, timedelta

past = datetime.now() - timedelta(days=3)
future = datetime.now() + timedelta(weeks=1)
```

---

### 🌐 `datetime.timezone` (optional)

```python
from datetime import timezone, datetime, timedelta

utc_time = datetime.now(timezone.utc)
print(utc_time)
```

#### 🇬🇧: For dealing with UTC and time zones.

#### 🇷🇸: Za rad sa vremenskim zonama i UTC-om.

---

## 🧪 Practical Examples | 🧪 Praktični Primeri

### ✅ Timestamp generator (file naming)

```python
from datetime import datetime

def generate_filename():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
```

### ✅ Check for old files

```python
from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(days=30)
```

### ✅ Format for folder creation

```python
from datetime import datetime

date_str = datetime.now().strftime("%Y-%m-%d")
```

---

#### 📌 **🇬🇧 TIP:** Use `datetime` for nearly every automation involving time.

#### 📌 **🇷🇸 SAVET:** Koristi `datetime` za skoro svaku automatizaciju povezanu sa vremenom.

---

## 📄 Read and Write Basics | Čitanje i Pisanje Fajlova

- 🇬🇧: Demonstrates how to create and read text files in Python using `with open(...)`.

- 🇷🇸: _Prikazuje kako se kreiraju i čitaju tekstualni fajlovi u Python-u koristeći `with open(...)`._

### ✍️ Create a File with Sample Content | Kreiranje fajla sa sadržajem

```python
def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
        file.write("Line 3\n")
```

#### 🇬🇧: Creates a text file and writes multiple lines.

#### 🇷🇸: Kreira tekstualni fajl i upisuje više linija.

---

## 📖 Read File Line by Line | Čitanje fajla red po red

```python
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
```

#### 🇬🇧: Returns a list of lines from the file.

#### 🇷🇸: Vraća listu linija iz fajla.

---

## 💡 Tips | Saveti

- Always use `with open(...)` for safe file access.
- Koristi `strip()` da ukloniš `\n` pri prikazu.
- Uvek proveri da li fajl postoji pomoću `os.path.exists()`.

---

#### 📌 **Useful in**: Logging, configuration readers, automation scripts

#### 📌 **Korisno za**: Logovanje, čitanje konfiguracija, skripte za automatizaciju

---

## 🔗 path_join_cheatsheet.md — Working with Paths | Rad sa Putanjama

#### 🇬🇧: How to reliably create full paths in Python using `os.path.join` and `os.getcwd()`.

#### 🇷🇸: Kako pouzdano kreirati pune putanje u Python-u koristeći `os.path.join` i `os.getcwd()`.

---

### 📌 Get Full File Path | Dobijanje pune putanje fajla

```python
import os

def get_full_path(filename):
    current_dir = os.getcwd()
    return os.path.join(current_dir, filename)
```

#### 🇬🇧: Joins the current directory with filename.

#### 🇷🇸: Spaja trenutni direktorijum sa imenom fajla.

---

### 🔍 Why Use `os.path.join`? | Zašto koristiti `os.path.join`?

#### 🇬🇧 Platform-independent (Windows/Linux/Mac)

#### 🇷🇸 Nezavisno od operativnog sistema

---

### 💡 Examples | Primeri

```python
print(get_full_path("report.txt"))
# Output: C:\Users\JoleDev\projects\report.txt
```

```python
folder = os.path.join("base_dir", "subdir", "files")
```

---

#### 📌 **Useful in**: File creation, logging, dynamic path building

#### 📌 **Korisno za**: Kreiranje fajlova, logovanje, dinamičko generisanje putanja

---

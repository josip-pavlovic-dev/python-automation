# 🧠 datetime_module_cheatsheet.md — Essential Concepts |Ključni Koncepti

🇬🇧 **EN:** A practical overview of the most useful features of the `datetime` module in Python. Focused on real-world usage in file automation.  
🇷🇸 **SR:** Praktičan pregled najkorisnijih funkcija iz `datetime` modula u Python-u, sa fokusom na realnu primenu u automatizaciji fajlova.

---

### 📅 `datetime.datetime`

```python
from datetime import datetime

now = datetime.now()
print(now)  # 2025-07-21 10:25:38.128391
```

- 🇬🇧 Represents both date and time.
- 🇷🇸 Predstavlja i datum i vreme.

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

- 🇬🇧 Represents a date without time.
- 🇷🇸 Predstavlja datum bez vremena.

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

- 🇬🇧 Represents only the time (hour, minute...)
- 🇷🇸 Predstavlja samo vreme (sat, minut...)

---

### 🔁 `datetime.timedelta`

```python
from datetime import timedelta

delta = timedelta(days=5)
print(delta)  # 5 days
```

- 🇬🇧 Duration or difference between dates/times
- 🇷🇸 Trajanje ili razlika između datuma/vremena

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

- 🇬🇧 For dealing with UTC and time zones.
- 🇷🇸 Za rad sa vremenskim zonama i UTC-om.

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

📌 **🇬🇧 TIP:** Use `datetime` for nearly every automation involving time.
📌 **🇷🇸 SAVET:** Koristi `datetime` za skoro svaku automatizaciju povezanu sa vremenom.

# 📘 `datetime` Module – Introduction

Python’s `datetime` module allows you to work with **dates, times, and intervals**. It is essential when building file automation systems, logs, reports, and any script that depends on **timestamping** or **temporal conditions** (e.g., deleting files older than 30 days).

_Modul `datetime` u Python-u omogućava rad sa **datumima, vremenima i vremenskim intervalima**. Ključan je za izgradnju sistema automatizacije fajlova, logova, izveštaja i svih skripti koje zavise od **vremenskih oznaka** ili **uslova vezanih za vreme** (npr. brisanje fajlova starijih od 30 dana)._

## ✅ Why use `datetime`? | _Zašto koristiti `datetime`?_

- Create or format timestamps | _Kreiranje ili formatiranje vremenskih oznaka_
- Compare file ages | _Poređenje starosti fajlova_
- Calculate time differences (e.g., 7 days ago) | _Računanje vremenskih razlika (npr. pre 7 dana)_
- Generate folder names based on current time | _Generisanje imena foldera na osnovu trenutnog vremena_

---

## 🧩 Main Classes in `datetime` | _Glavne klase u `datetime`_

| Class       | _Klasa_     | Description                                    | _Opis_                                                 |
| ----------- | ----------- | ---------------------------------------------- | ------------------------------------------------------ |
| `datetime`  | _datetime_  | Full date and time (year, month, day, hour...) | _Kompletan datum i vreme (godina, mesec, dan, sat...)_ |
| `date`      | _date_      | Only the date (no time)                        | _Samo datum (bez vremena)_                             |
| `time`      | _time_      | Only the time                                  | _Samo vreme_                                           |
| `timedelta` | _timedelta_ | Difference between two datetimes               | _Razlika između dva datuma/vremena_                    |

---

## 📌 Common Functions | _Česte funkcije_

| Function                      | _Funkcija_                    | Description                                  | _Opis_                                           |
| ----------------------------- | ----------------------------- | -------------------------------------------- | ------------------------------------------------ |
| `datetime.now()`              | _datetime.now()_              | Current local date and time                  | _Trenutni lokalni datum i vreme_                 |
| `datetime.fromtimestamp(ts)`  | _datetime.fromtimestamp(ts)_  | Converts UNIX timestamp to readable datetime | _Pretvara UNIX vremensku oznaku u čitljiv oblik_ |
| `datetime.strftime(fmt)`      | _datetime.strftime(fmt)_      | Formats datetime as string                   | _Formatira datum kao string_                     |
| `datetime.strptime(str, fmt)` | _datetime.strptime(str, fmt)_ | Parses string to datetime                    | _Pretvara string u datetime objekat_             |

---

## 🔁 Examples of Use | _Primeri upotrebe_

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 2025-07-29 09:22:15

seven_days_ago = now - timedelta(days=7)
print(seven_days_ago)  # 2025-07-22 09:22:15

# Format as string
formatted = now.strftime("%Y-%m-%d_%H-%M-%S")
print(formatted)  # 2025-07-29_09-22-15
```

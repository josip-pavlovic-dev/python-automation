# 🧠 Cheatsheet: datetime module | _Pregled: datetime modul_

## ✅ Common functions | _Najčešće funkcije_

| Function                      | _Funkcija_                    | Description                    | _Opis_                                    |
| ----------------------------- | ----------------------------- | ------------------------------ | ----------------------------------------- |
| `datetime.now()`              | _datetime.now()_              | Returns current local datetime | _Vraća trenutni lokalni datum i vreme_    |
| `datetime.today()`            | _datetime.today()_            | Alias for `now()`              | _Sinonim za `now()`_                      |
| `datetime.fromtimestamp(ts)`  | _datetime.fromtimestamp(ts)_  | Converts timestamp to datetime | _Pretvara timestamp u objekat `datetime`_ |
| `datetime.strftime(fmt)`      | _datetime.strftime(fmt)_      | Formats datetime as string     | _Formatira datum u string_                |
| `datetime.strptime(str, fmt)` | _datetime.strptime(str, fmt)_ | Parses string to datetime      | _Pretvara string u datum_                 |
| `timedelta(days=N)`           | _timedelta(days=N)_           | Time interval (N days)         | _Vremenski interval (N dana)_             |
| `datetime - timedelta`        | _datetime - timedelta_        | Subtracts time                 | _Oduzima vreme (npr. 7 dana unazad)_      |

## 📌 Example formats | _Formati za ispis vremena_

| Format              | _Format_              | Output                | _Izlaz_               |
| ------------------- | --------------------- | --------------------- | --------------------- |
| `%Y-%m-%d`          | _Godina-Mesec-Dan_    | `2025-07-29`          | `2025-07-29`          |
| `%H:%M:%S`          | _Sati:Minuti:Sekunde_ | `14:23:01`            | `14:23:01`            |
| `%Y-%m-%d_%H-%M-%S` | _Za ime fajla_        | `2025-07-29_14-23-01` | `2025-07-29_14-23-01` |

---

## 👨‍💻 Author | _Autor_

🔗 [LinkedIn Profile](https://www.linkedin.com/in/josip-p-151951338/)  
**Josip Pavlović — aspiring Python developer from Novi Sad**

---

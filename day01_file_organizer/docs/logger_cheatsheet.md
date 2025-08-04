# 📌 Cheatsheet: `logger.py` | _Šalabahter: `logger.py`_

## ✅ Why use a logger? | _Zašto koristiti logger?_

- To track program execution. | _Za praćenje toka izvršavanja programa._
- To debug issues across modules. | _Za otkrivanje grešaka u više skripti._
- To create permanent logs. | _Za kreiranje trajnih logova (fajlovi)._

## 🛠️ Key components | _Ključne komponente_

| Component       | _Komponenta_    | Description                    | _Opis_                                |
| --------------- | --------------- | ------------------------------ | ------------------------------------- |
| `getLogger()`   | `getLogger()`   | Gets logger instance.          | _Dobija logger instancu._             |
| `setLevel()`    | `setLevel()`    | Sets minimum log level.        | _Postavlja minimalni nivo logovanja._ |
| `FileHandler()` | `FileHandler()` | Sends logs to file.            | _Šalje logove u fajl._                |
| `Formatter()`   | `Formatter()`   | Formats output logs.           | _Formatira izlazne logove._           |
| `addHandler()`  | `addHandler()`  | Attaches handler to logger.    | _Dodaje handler loggeru._             |
| `handlers`      | `handlers`      | List of all attached handlers. | _Lista svih handlera na loggeru._     |

## 🗂️ Log levels | _Nivoi logovanja_

- `DEBUG` – fine-grained logs for dev | _Detaljni logovi za razvoj_
- `INFO` – general information | _Opšte informacije_
- `WARNING` – something unexpected | _Nešto neočekivano_
- `ERROR` – serious issue | _Ozbiljan problem_
- `CRITICAL` – major failure | _Kritičan pad sistema_

## 📁 Path handling | _Rukovanje putanjama_

- `Path(__file__).resolve().parents[2]` – goes two levels up to the root | _Ide dva nivoa iznad skripte, do root foldera_
- `Path(...).mkdir(parents=True, exist_ok=True)` – creates folder recursively | _Kreira folder (i nadfolder ako ne postoji)_

## 🚫 Avoiding duplicate handlers | _Izbegavanje duplih handlera_

```python
if logger.handlers:
    return logger
```

- Prevents logs from duplicating when `main.py` is re-run | _Sprečava dupli unos u log fajl ako se `main.py` više puta pokreće_

---

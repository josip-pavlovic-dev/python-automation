# 🧾 logger.py Cheatsheet

## 📌 Description | Opis

#### **🇬🇧:** This module defines a simple logging function that appends timestamped messages to a `log.txt` file.  
#### **🇷🇸:** Ovaj modul definiše jednostavnu funkciju za logovanje koja dodaje poruke sa vremenskim žigom u fajl `log.txt`.

---

## 🛠️ Function Overview | Pregled funkcije

### `log(message: str, logfile: str = "log.txt") -> None`

##### **🇬🇧:** Appends a log entry to the specified file with the current date and time.

##### **🇷🇸:** Dodaje zapis u log fajl sa trenutnim datumom i vremenom.

## Parameters | Parametri
- `message`: str — **🇬🇧:** the message to log | **🇷🇸:** poruka koju beležimo
- `logfile`: str — **🇬🇧:** file where logs will be stored | **🇷🇸:** fajl u koji se beleži log (podrazumevano `log.txt`)

---

## 📂 Output | Izlaz

```
[2025-07-15 15:42:12] This is a log message.
```

---

## 🧪 Example | Primer

```python
from logger import log

log("Test message from logger module")
```

### **🇬🇧:** This call will create (or append to) `log.txt` with the above message.
### **🇷🇸:** Ova linija će kreirati (ili dopuniti) fajl `log.txt` sa gore navedenom porukom.


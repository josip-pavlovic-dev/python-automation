# 📑 Line-by-Line Explanation: logger.py | _Linija po linija objašnjenje: logger.py_

```python
from pathlib import Path
```

- Imports the `Path` class used for handling file system paths. | _Uvozi `Path` klasu za rad sa putanjama u fajl sistemu._

```python
import logging
```

- Imports Python's built-in logging module. | _Uvozi standardni Python modul za logovanje._

---

```python
def setup_logger():
```

- Defines a reusable function that sets up and returns a configured logger. | _Definiše funkciju koja postavlja i vraća konfigurisan logger._

---

```python
    logger = logging.getLogger("file_organizer")
```

- Retrieves a logger instance named `"file_organizer"`. | _Dobija logger instancu sa imenom `"file_organizer"`._

---

```python
    if logger.handlers:
        return logger
```

- If the logger already has any handlers, return it to prevent adding duplicates. | _Ako logger već ima hendler, vraća se kako bi se izbeglo duplo logovanje._

---

```python
    logs_dir = Path(__file__).resolve().parents[2] / "logs"
```

- Calculates absolute path to the `logs/` directory two levels above the script. | _Dobija apsolutnu putanju do foldera `logs/`, dva nivoa iznad ove skripte._

---

```python
    logs_dir.mkdir(parents=True, exist_ok=True)
```

- Creates the directory if it doesn’t exist, including parent folders. | _Kreira direktorijum ako ne postoji, uključujući sve naddirektorijume._

---

```python
    log_file = logs_dir / "log.txt"
```

- Sets the path for the log file to be `logs/log.txt`. | _Definiše lokaciju log fajla – `logs/log.txt`._

---

```python
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
```

- Creates a handler that writes log records to a file. | _Kreira handler koji piše logove u fajl._

---

```python
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
```

- Defines the format for each log entry (timestamp, level, message). | _Definiše format za svaki log unos (vreme, nivo, poruka)._

---

```python
    file_handler.setFormatter(formatter)
```

- Applies the formatter to the file handler. | _Povezuje format sa handlerom._

---

```python
    logger.setLevel(logging.INFO)
```

- Sets minimum logging level to INFO (skips DEBUG). | _Postavlja minimalni nivo logovanja na INFO._

---

```python
    logger.addHandler(file_handler)
```

- Attaches the file handler to the logger. | _Dodaje file handler logger instanci._

---

```python
    return logger
```

- Returns the fully configured logger object. | _Vraća potpuno konfigurisan logger objekat._

---

## 📄 main.py

- `for file in folder.iterdir()` | _Iteracija kroz sve fajlove u folderu_
- `file.suffix[1:]` | _Dobijanje ekstenzije bez početne tačke_
- `shutil.move(...)` | _Premešta fajl u folder koji odgovara njegovoj ekstenziji_

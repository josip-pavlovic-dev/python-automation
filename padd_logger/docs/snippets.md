# 🧩 Snippets for `logger.py` | _Snippeti za `logger.py`_

## 🔧 Logger setup | _Podešavanje logovanja_

```python
from pathlib import Path
import logging

def setup_logger():
    logger = logging.getLogger("file_organizer")
    if logger.handlers:
        return logger

    logs_dir = Path(__file__).resolve().parents[2] / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_file = logs_dir / "log.txt"

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger
```

### 🧠 Notes | _Beleške_

- `resolve().parents[2]` navigates to the root project directory. | _Navigira do root foldera projekta (dva nivoa iznad skripte)._
- `logger.handlers` prevents adding duplicate handlers. | _Sprečava višestruko dodavanje istih handlera._
- `log_file` is always created as `logs/log.txt`. | _Log se kreira u `logs/log.txt` bez obzira odakle se pokreće skripta._

---

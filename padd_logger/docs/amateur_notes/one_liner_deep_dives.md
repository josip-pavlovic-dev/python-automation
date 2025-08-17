## 1) Šta vidim?

Tip anotacija kaže: promenljiva `file_path` može biti _putanja_ (kao `str` ili bilo šta što se ponaša kao putanja — `os.PathLike`) **ili** `None` ako nema fajla.

## 2) Rastavljanje na delove

- `Optional[T]` ⇢ vrednost može biti tipa `T` **ili** `None`.
- `Union[A, B]` ⇢ vrednost može biti `A` **ili** `B`.
- `str` ⇢ običan string (npr. `"logs/app.log"`).
- `os.PathLike` ⇢ “protokol” koji predstavlja putanju (objekti koji imaju `__fspath__()`), npr. `pathlib.Path`.
- `= None` ⇢ podrazumevana vrednost: nema putanje (fajl logging je isključen).

## 3) Dijagram (mentalni model)

```
                     +------------------+
input  ---> file_path| Optional[Union[  |----> koristiš kao putanju
                     |   str, PathLike  |
                     +--------+---------+
                              |
                              v
                           None?  ---- yes ---> "nema fajl handlera"
                              |
                             no
                              |
                              v
                 normalize to Path (Path(file_path))
```

## 4) Primeri upotrebe

**Primer A — nema fajl loga (None):**

```python
configure_logger(file_path=None, console=True)
```

**Primer B — string putanja:**

```python
configure_logger(file_path="logs/app.log")
```

**Primer C — PathLike (Path):**

```python
from pathlib import Path
configure_logger(file_path=Path("logs") / "app.log")
```

**Normalizacija unutra (preporuka):**

```python
from pathlib import Path
from typing import Optional, Union
import os

def _norm_path(p: Optional[Union[str, os.PathLike]]) -> Optional[Path]:
    return None if p is None else Path(p).expanduser().resolve()
```

## 5) Zadaci

**Zadatak 1**
Napiši funkciju `ensure_log_dir(p)` koja prima `Optional[Union[str, os.PathLike]]` i:

- vraća **`None`** ako je ulaz `None`,
- u suprotnom vraća **`Path`** sa kreiranim roditeljskim direktorijumom.

**Rešenje 1**

```python
from pathlib import Path
from typing import Optional, Union
import os

def ensure_log_dir(p: Optional[Union[str, os.PathLike]]) -> Optional[Path]:
    if p is None:
        return None
    path = Path(p).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

**Zadatak 2**
Dopuni konstruktor logger‑a da **uvek** koristi `utf-8` i da **ne boji** fajl izlaz.

**Rešenje 2**

```python
import logging

def add_file_handler(logger: logging.Logger, file_path: Path, fmt: str, datefmt: str) -> None:
    fh = logging.FileHandler(file_path, encoding="utf-8")
    fh.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))  # bez boja u fajlu
    logger.addHandler(fh)
```

## 6) Tipične greške i dobre prakse

- ❌ **Greška:** rukovanje `file_path` kao stringom bez normalizacije → problemi sa `~`, relativnim putanjama.
  ✅ Rešenje: `Path(p).expanduser().resolve()`.
- ❌ **Greška:** ostaviti ANSI boje u fajl handleru.
  ✅ Rešenje: boje samo u konzoli (TTY), fajl koristi običan `Formatter`.
- ❌ **Greška:** kreirati fajl u nepostojećem folderu.
  ✅ Rešenje: `path.parent.mkdir(parents=True, exist_ok=True)`.
- ✅ **Dobra praksa:** potpis širi (`Union[str, os.PathLike]`), _unutra_ uvek koristi `Path`.

---

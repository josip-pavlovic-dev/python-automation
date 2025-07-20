# 🧠 Import putanje u Pythonu – razlika između fajl sistema i modula

## 📌 Problem

Kod pokretanja testova iz podfoldera (`tests/`), često se javlja greška:

```bash
ImportError: No module named 'logger'
```

Ili:

```bash
Import 'logger' could not be resolved
```

---

## ✅ Rešenje: razumevanje Python import sistema

### 1. 🔷 Dot notacija (`dot notation`)

Koristi se za `import`:

```python
from day03_file_management.logger import log
```

- `day03_file_management`: folder na nivou projekta (modul/paket)
- `logger`: fajl `logger.py`
- `log`: funkcija

📌 **Nije** fajl putanja! To je **putanja kroz module**.

---

### 2. 🔶 Relativna fajl putanja

Koristi se npr. kod:

```python
open("../folder/file.txt")
```

ili

```python
os.path.join(os.path.dirname(__file__), "file.txt")
```

📌 Ovo se koristi u fajl sistemu — nema veze sa `import`.

---

## 🧠 Reflex koji moraš znati:

> **Ako koristiš **``** → koristiš dot notaciju**\
> **Ako koristiš **``**, **``**, **``** → koristiš fajl putanju**

---

## 📂 Vizuelni prikaz razlike

### 👇 Struktura projekta:

```
python-automation/
├── day03_file_management/
│   └── logger.py          ← funkcija: log()
├── tests/
    └── test_day03_file_management/
        └── test_logger.py
```

---

## 🔎 Kako importovati `log` iz `test_logger.py`?

```python
# ✅ Ispravno (dot notacija - modularni import):
from day03_file_management.logger import log
```

```python
# ❌ Pogrešno (nema putanje do modula):
from logger import log
```

```python
# ⚠️ Alternativa (ali nepoželjna u profesionalnim projektima):
import sys
sys.path.append("../../day03_file_management")
from logger import log
```

---

## ✅ Podešavanje za VS Code

Obavezno u `settings.json`:

```json
"python.analysis.extraPaths": ["./"]
```

---

## 📌 Zaključak

- Koristi `dot notaciju` za module
- Nikad ne koristi `../folder/file.py` u `import`
- Po potrebi dodaj `__init__.py` fajlove da folder bude prepoznat kao modul
- Neka svi testovi žive u `tests/` folderu i koriste uvezene module, ne kopirane


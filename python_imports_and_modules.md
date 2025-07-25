# 🐍 Python Modules & Import System (EN + SR)

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 📦 1. Šta su moduli i paketi? / What are modules & packages?

### 🇷🇸

- **Modul** = bilo koji `.py` fajl (npr. `helper.py`)
- **Paket** = folder koji sadrži `__init__.py` + module

### 🇬🇧

- **Module** = any `.py` file (e.g., `helper.py`)
- **Package** = folder with `__init__.py` and modules

```
project_root/
├── main.py
├── utils/
│   ├── __init__.py
│   └── logger.py
```

---

## 📥 2. Vrste import-a / Types of import

### ✅ Direktan (apsolutni):

```python
from utils.logger import log_error
```

### ✅ Relativan (lokalni):

```python
from .logger import log_error      # iz istog paketa
from ..utils import helper_func    # jedan nivo iznad
```

✅ Koristi relativni import kada je modul u istom paketu.
✅ Koristi apsolutni import kada pozivaš iz root-a projekta.

---

## 🧠 3. Promenljiva `__name__` i `__main__`

```python
if __name__ == "__main__":
    # pokreni test logike samo kada je direktno pokrenut
```

- Ako pokrećeš fajl direktno → `__name__ == "__main__"`
- Ako je importovan kao modul → `__name__ == "ime_modula"`

---

## 🧭 4. Python traži module u:

### 🔍 `sys.path` lista:

```python
import sys
print(sys.path)
```

📌 Šta se nalazi u `sys.path`:

- trenutni direktorijum (`"."`)
- standardni library folder
- svi folderi iz `PYTHONPATH` promenljive

---

## 🧪 5. Saveti za import strukturu

| Praksa                                       | Objašnjenje                          |
| -------------------------------------------- | ------------------------------------ |
| ✅ Koristi `__init__.py`                     | za pakete — čak i ako je prazan      |
| ✅ Prati strukturu foldera u `tests/`        | neka odražava glavne skripte         |
| ✅ Ne koristi iste nazive fajlova i funkcija | npr. `logger.py` i `logger()`        |
| ✅ Podesi `launch.json` za root pokretanje   | da `from X import Y` ne pravi greške |

---

## 🔧 Primer `launch.json`:

```json
{
  "name": "▶️ Run with root",
  "type": "python",
  "request": "launch",
  "program": "${file}",
  "cwd": "${workspaceFolder}"
}
```

Time se osigurava da su import putanje bazirane na root-u projekta.

---

📁 Lokacija: `docs/python_imports_and_modules.md`
✍️ Autor: Josip Pavlović
📅 Ažurirano: 2025-07-21

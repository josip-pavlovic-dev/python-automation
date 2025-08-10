# 🛠️ argparse Cheatsheet | _Argparse prečice_

Ovaj cheatsheet dokumentuje rad sa `argparse` modulom koji omogućava parsiranje argumenata iz komandne linije.

---

## 📌 Key Concepts | _Ključni pojmovi_

| Pojam (EN)         | Objašnjenje (SR)                                         |
| ------------------ | -------------------------------------------------------- |
| `ArgumentParser()` | Kreira parser koji obrađuje CLI argumente.               |
| `add_argument()`   | Dodaje pojedinačne argumente (npr. `--folder`)           |
| `parse_args()`     | Vraća `Namespace` objekat sa vrednostima svih argumenata |
| `--optional`       | Prefiks za opcione argumente (`--folder`, `--log`, itd.) |
| `dest`             | Ime promenljive u kodu koja prima vrednost iz CLI        |
| `type`             | Definiše tip vrednosti (`str`, `int`, `Path`, itd.)      |
| `help`             | Tekst koji opisuje argument, prikazuje se u `--help`     |

---

## 📎 Example | _Primer korišćenja_

```python
import argparse

parser = argparse.ArgumentParser(description="Opis programa")
parser.add_argument("--folder", type=str, help="Putanja do foldera")
args = parser.parse_args()

print(args.folder)
```

### 🗒️ Napomena | Napomena

U kombinaciji sa pathlib.Path, argument može odmah biti konvertovan u apsolutnu putanju.
**argparse** se koristi kada želiš da omogućiš korisniku da upravlja ponašanjem skripte preko komandne linije.

---

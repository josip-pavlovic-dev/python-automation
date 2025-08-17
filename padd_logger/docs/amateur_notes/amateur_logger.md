# 🛠 Amateur Notes – Logger u Python-u

## 📌 Uvod

- **Logger** je centralni objekat Python `logging` modula.
- On je zadužen za prikupljanje i prosleđivanje poruka (**log entries**) ka svojim **handlerima**.
- Logger može imati više handlera, različite formate zapisa i različite nivoe filtriranja poruka.

---

## 1️⃣ Kreiranje logger-a

```python
logger = logging.getLogger("file_organizer")
```

- **`getLogger(name)`** vraća logger sa datim imenom.
- Ako već postoji logger sa tim imenom, vratiće se isti objekat (singleton logika).
- Ime (`"file_organizer"`) koristi se da razlikujemo logere unutar aplikacije.

---

## 2️⃣ Podešavanje nivoa logovanja

```python
logger.setLevel(logging.INFO)
```

- **Tehnički:** `setLevel()` određuje minimalni nivo poruka koje logger prosleđuje handlerima.
- **Logički:** Ovo je kao filter na ulazu — ako je poruka ispod ovog nivoa, logger je neće ni proslediti handlerima.
- **`logging.INFO`** je konstanta (broj 20) koja predstavlja važnost poruka.
  Ostali nivoi:

  - `DEBUG` (10) — detaljne tehničke informacije.
  - `INFO` (20) — standardne informativne poruke.
  - `WARNING` (30) — nešto nije u redu, ali aplikacija radi.
  - `ERROR` (40) — greška, ali aplikacija može nastaviti.
  - `CRITICAL` (50) — ozbiljna greška, program možda neće moći da radi.

💡 **Primer filtriranja:**
Ako je `setLevel(logging.INFO)`, a mi pozovemo:

```python
logger.debug("Test debug poruke")
logger.info("Test info poruke")
```

- `debug` neće biti prosleđen handlerima.
- `info` hoće.

---

## 2️⃣.1 Nivoi — zašto `logging.INFO` (a ne `logger.INFO`)?

**Tehnički**

- `logging.INFO` je **konstanta** definisana u _modulu_ `logging` (vrednost `20`).
- `logger = logging.getLogger("…")` vraća **instancu** klase `Logger`. Instanca ima **metode** (`setLevel`, `info`, …), ali **nema** atribut `INFO`.
- Konstante kao `INFO`, `DEBUG`, … žive u modulu (ili kao _class attributes_ u `Logger`), a ne na instanci.

**Logički**

- Zamislite `logging` kao **fabriku** sa standardima (INFO=20), a `logger` kao **mašinu** koja radi po tim standardima. Standard (20) dolazi iz fabrike, ne iz mašine.

**Ispravno**

```python
logger.setLevel(logging.INFO)      # ✅ prosleđujemo vrednost 20 iz modula
# ili:
from logging import INFO
logger.setLevel(INFO)
```

**Neispravno**

```python
logger.setLevel(logger.INFO)       # ❌ instanca nema atribut INFO → AttributeError
```

---

## 2️⃣.2 Mini dijagram odnosa

```
+-----------------------------+
|         logging (modul)     |
|-----------------------------|
| INFO=20, DEBUG=10, ...      |  ← konstante nivoa
| getLogger(name) -> Logger   |  ← fabrika logger objekata
| basicConfig(...), ...       |
+-----------------------------+
              |
              v
+-----------------------------+
|       Logger (klasa)        |
|-----------------------------|
| setLevel(), info(), ...     |  ← metode (class definicija)
| (INFO postoji kao class attr)|
+-----------------------------+
              |
              v
+-----------------------------+
|       logger (instanca)     |
|-----------------------------|
| setLevel(), info(), ...     |  ← nasleđene metode
| (nema .INFO atribut)        |
+-----------------------------+
```

---

## 2️⃣.3 Mini demonstracije

### A) Inspekcija atributa (dokaz gde šta živi)

```python
import logging
logger = logging.getLogger("demo_logger")

print(type(logger))                 # <class 'logging.Logger'>
print(logging.INFO)                 # 20  (modul)
print(hasattr(logger, "INFO"))      # False (instanca nema INFO)
print(hasattr(logging.Logger, "INFO"))  # True (class-level)
```

### B) Filtriranje u praksi (setLevel je “ulazni” filter)

```python
import logging
from io import StringIO

# hvatač ispisa u memorijski stream da vidimo šta je prošlo
stream = StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))

logger = logging.getLogger("filter_demo")
logger.handlers.clear()
logger.addHandler(handler)

logger.setLevel(logging.INFO)  # poruke ispod INFO neće proći
logger.debug("debug msg")      # ispod praga → ne prolazi
logger.info("info msg")        # prag ili iznad → prolazi

handler.flush()
print(stream.getvalue().strip())  # "INFO | info msg"
```

**Takeaways**

- `setLevel` na logger-u je **glavni prag**.
- Handleri mogu imati **sopstvene pragove** (`handler.setLevel(...)`).
- Konstante nivoa (`INFO`, …) uzimamo iz **modula** (`logging.INFO`) ili importujemo direktno.

---

## 3️⃣ Provera postojećih handlera

```python
if logger.hasHandlers():
    return logger
```

- **Tehnički:** `hasHandlers()` vraća `True` ako logger već ima makar jedan handler.
- **Logički:** Ovim sprečavamo da dodamo nove handlere svaki put kad se funkcija `setup_logger()` pozove.
  Inače bi mogli završiti sa duplim ispisima poruka (isti tekst više puta u konzoli i fajlu).
- **Praksa:** Ovo je standard u konfiguracionim funkcijama logger-a.

---

## 4️⃣ Putanja log fajla

```python
log_dir = Path(__file__).resolve().parent.parent / "log"
log_dir.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = log_dir / f"log_{timestamp}.txt"
```

- **Tehnički:**

  - `Path(__file__).resolve()` — apsolutna putanja do trenutnog fajla (`logger.py`).
  - `.parent.parent` — dva nivoa iznad (`src/` → `day01_file_organizer/`).
  - `/ "log"` — dodaje folder `log`.
  - `mkdir(exist_ok=True)` — kreira folder ako ne postoji.
  - `datetime.now().strftime(...)` — formatira vreme za naziv fajla.

- **Logički:** Log fajlovi imaju jedinstveno ime bazirano na trenutnom vremenu.

---

## 5️⃣ Handleri

```python
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
```

- **FileHandler:** piše log poruke u fajl (`log_file`).
- **StreamHandler:** prikazuje log poruke u konzoli.
- Oba imaju svoj `setLevel()` filter nezavisno od logger-a.

---

## 6️⃣ Formatter

```python
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
```

- **Tehnički:** Formatter kontroliše kako će poruka izgledati.
- `%` promenljive:

  - `%(asctime)s` — vreme kreiranja poruke.
  - `%(levelname)s` — nivo (`INFO`, `ERROR`, itd.).
  - `%(message)s` — sama poruka.

- **Logički:** Osigurava da i fajl i konzola imaju isti format ispisa.

---

## 7️⃣ Dodavanje handlera

```python
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
```

- Logger prosleđuje svaku poruku svim handlerima koje ima.
- Svaki handler primenjuje svoj filter (`setLevel`) i format (`Formatter`).

---

## 🎯 Mini demonstracija

```python
logger.info("Ovo je INFO poruka")
logger.debug("Ovo je DEBUG poruka")
```

- Ako je `setLevel(logging.INFO)`:

  - `INFO` će se pojaviti i u fajlu i u konzoli.
  - `DEBUG` neće proći filter.

---

## 📝 Zaključak

- Logger + handleri = fleksibilno i kontrolisano logovanje.
- Uvek proveravati `hasHandlers()` u setup funkcijama.
- Dobar formatter čini logove čitljivim i preglednim.

---

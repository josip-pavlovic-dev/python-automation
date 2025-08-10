# 🛠 Amateur Notes – Handlers in Python Logging

## 📌 Šta su handleri?

- **Handler** u Python `logging` modulu je komponenta koja odlučuje **gde će poruka iz logger-a da ode**.
- Logger može imati više handlera istovremeno — svaki šalje poruku na različito mesto.
- U praksi, handleri su „most“ između poruke koju logger kreira i odredišta gde će ta poruka biti upisana ili prikazana.

---

## 🔍 Glavne vrste handlera

### 1. **FileHandler**

- **Šta radi:** Upisuje log poruke u fajl.
- **Kada se koristi:** Kada želimo trajni zapis o događajima (debug, error, info).
- **Primer:**
  ```python
  logging.FileHandler("log.txt", mode="w")
  ```

* `mode="w"` — svaki put kreira novi fajl (briše stari sadržaj).
* `mode="a"` — dodaje nove poruke na kraj postojećeg fajla.

---

### 2. **StreamHandler**

- **Šta radi:** Ispisuje log poruke na **standardni izlaz** (obično konzolu).
- **Kada se koristi:** Kada želimo odmah da vidimo poruke tokom izvršavanja programa.
- **Primer:**

  ```python
  logging.StreamHandler()
  ```

  - Može ispisivati u `sys.stdout` ili `sys.stderr`.

---

### 3. **RotatingFileHandler**

- **Šta radi:** Upisuje log poruke u fajl, ali ga **rotira** kada dostigne određenu veličinu.
- **Zašto je koristan:** Sprečava da log fajl naraste previše.
- **Primer:**

  ```python
  from logging.handlers import RotatingFileHandler

  RotatingFileHandler("log.txt", maxBytes=1024, backupCount=3)
  ```

  - `maxBytes=1024` — kad dostigne 1 KB, pravi novi fajl.
  - `backupCount=3` — čuva najviše 3 stara log fajla.

---

### 4. **TimedRotatingFileHandler**

- **Šta radi:** Rotira log fajlove po vremenskom intervalu (npr. dnevno, nedeljno).
- **Primer:**

  ```python
  from logging.handlers import TimedRotatingFileHandler

  TimedRotatingFileHandler("log.txt", when="midnight", backupCount=7)
  ```

  - `when="midnight"` — rotacija svake ponoći.
  - `backupCount=7` — čuva logove za poslednjih 7 dana.

---

### 5. **NullHandler**

- **Šta radi:** Ne radi ništa — ignoriše sve poruke.
- **Zašto postoji:** Koristi se kada želimo da onemogućimo default ispis logger-a iz nekog modula.
- **Primer:**

  ```python
  logging.NullHandler()
  ```

---

## 📌 Veza između logger-a i handler-a

1. Logger prima poruku (`logger.info(...)`).
2. Logger prosleđuje poruku svim **handlerima** koje ima.
3. Svaki handler odlučuje **da li će obraditi poruku** na osnovu svog `setLevel()`.
4. Poruka se formatira pomoću **formatter-a** (npr. datum, vreme, tekst).
5. Handler šalje poruku u svoje odredište (fajl, konzola, mreža...).

---

## 💡 Mini demonstracija

```python
import logging
from pathlib import Path

# Logger
logger = logging.getLogger("demo_logger")
logger.setLevel(logging.INFO)

# File handler
log_path = Path("demo_log.txt")
fh = logging.FileHandler(log_path, mode="w")
fh.setLevel(logging.INFO)

# Stream handler
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# Dodavanje handlera
logger.addHandler(fh)
logger.addHandler(sh)

# Test poruke
logger.debug("Ovo je debug poruka (videće se samo u konzoli).")
logger.info("Ovo je info poruka (videće se svuda).")
```

---

## 📝 Zaključak

- Handleri omogućavaju **fleksibilno usmeravanje logova**.
- Možeš imati više handlera u jednom logger-u.
- Najčešća kombinacija: **FileHandler + StreamHandler**.

```

---
```

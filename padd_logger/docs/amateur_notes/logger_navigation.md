# Learning navigation

## **📍 Navigacija za logger.py**

1. **Line-by-Line Chat (`logger.py`)**

   - Fokus: prolazak kroz ceo kod, objašnjenje svake linije
   - Pitanja: detalji implementacije, zašto baš taj pristup

2. **Terminology Cheatsheet Chat**

   - Fokus: termini iz `logger.py` i dokumentacije
   - Pitanja: kratke definicije, primere upotrebe

3. **Concepts & Imports Chat**

   - Fokus: biblioteke i klase koje se importuju
   - Pitanja: deep dive za svaki import i parametar

4. **Amateur Notes Chat**

   - Fokus: jednostavna, početnička objašnjenja + mini primeri
   - Pitanja: “objasni mi ovo kao da sam početnik”

5. **Ruff & Black Chat**

   - Fokus: formatiranje i linting `logger.py`
   - Pitanja: pravila, konfiguracija, workflow

---

## **📜 Pitanja po chatovima**

### **Line-by-Line**

- Zašto koristimo `Optional[Union[str, os.PathLike]]` umesto samo `str`?
- Kako radi `RotatingFileHandler` i koje su prednosti u odnosu na običan `FileHandler`?
- Koja je razlika između `logger.setLevel()` i `handler.setLevel()`?
- Kako se postiže idempotentnost u `configure_logger()`?

### **Terminology Cheatsheet**

- Definiši: **handler**, **formatter**, **filter**, **logger hierarchy**
- Objasni pojam **root logger**
- Šta znači **propagation** u logger-ima?
- Šta je **log record**?

### **Concepts & Imports**

- Objasni `os.PathLike` i gde ga još koristimo u Pythonautomation projektima
- Kako `dataclass` olakšava kreiranje konfiguracionih objekata
- Prednosti `Path` klase iz `pathlib` naspram rada sa string putanjama
- Kada koristiti `argparse` u kombinaciji sa `logger.py`

### **Amateur Notes**

- Kako dodati boje u log poruke (primer za DEBUG, INFO, WARNING)
- Kako promeniti format datuma u logu
- Kako omogućiti logovanje na više destinacija istovremeno
- Kako filtrirati logove samo iz jednog modula

### **Ruff & Black**

- Kako podesiti `ruff.toml` da ignoriše E501
- Kako podesiti `pyproject.toml` za Black
- Kada pokrenuti Ruff pre Black-a
- Koje greške Ruff može automatski ispraviti, a koje ne

---

Evo predloga kako da napraviš navigaciju i pitanja za chatove na osnovu fajla `python_logging_howto_translation.md` i tvog cilja da se teorija poveže sa primenom u `logger.py`:

---

## **📌 Predlog navigacije po chatovima (Logger fokus)**

1. **Concepts & Imports chat**

   - Detaljna mini-lekcija za svaki novi pojam iz dokumentacije (npr. `RotatingFileHandler`, `Formatter`, `dictConfig`).
   - Pitanja: _"Šta radi `RotatingFileHandler` i kada ga koristiti?"_, _"Razlika između `basicConfig()` i `dictConfig()`?"_

2. **Line-by-line chat za `logger.py`**

   - Analiza svake linije koda uz povezivanje na teoriju iz HOWTO-a.
   - Pitanja: _"Kako bi izgledao deo `logger.py` ako se koristi `TimedRotatingFileHandler` umesto običnog `FileHandler`?"_

3. **Terminology Cheatsheet chat**

   - Kratke i jasne definicije svih termina iz dokumentacije.
   - Pitanja: _"Definiši 'formatter' u jednom pasusu"_, _"Koja je uloga filtera?"_

4. **Amateur Notes chat**

   - Pitanja na srpskom jeziku, fokus na praktične korake implementacije u projektu.
   - Pitanja: _"Kako dodati handler koji beleži samo WARNING nivo u fajl `warnings.log`?"_

5. **Pytest chat**

   - Kreiranje testova za proveru logger konfiguracije.
   - Pitanja: _"Kako testirati da li `logger` piše u fajl i u konzolu istovremeno?"_

---

## **📌 Predlog pitanja po sekcijama HOWTO-a**

### 1. Basic Logging

- Koji je podrazumevani nivo logovanja u Python-u?
- Kada koristiti `logger.warning()` umesto `warnings.warn()`?

### 2. Logging to a File

- Koja je svrha parametra `encoding` u `basicConfig()`?
- Kako definisati putanju log fajla tako da se nalazi u `logs/` folderu projekta?

### 3. Logging Variable Data

- Zašto je bolje koristiti `%s` u log porukama nego f-string?
- Prikaži primer logovanja imena korisnika i broja fajlova koje je obradio.

### 4. Changing the Format

- Šta radi `%(asctime)s` i kako promeniti format vremena?
- Kako uključiti broj linije (`lineno`) u log poruku?

### 5. Handlers

- Koja je razlika između `StreamHandler` i `FileHandler`?
- Kako podesiti `RotatingFileHandler` da čuva 5 starih fajlova od max 1MB?

### 6. Formatters

- Može li svaki handler imati različit formatter? Zašto bi to bilo korisno?
- Kako bi izgledao formatter koji prikazuje i PID procesa?

### 7. Filters

- Kada je korisno koristiti filtere u loggeru?
- Napiši filter koji dozvoljava samo ERROR i CRITICAL poruke.

---

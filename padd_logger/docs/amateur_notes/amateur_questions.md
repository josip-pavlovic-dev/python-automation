# Pitanja i zablude?

- Detaljnog objašnjenje **dot notacije** (tačkaste notacije) i kako ona funkcioniše na primeru:

```python
from day01_file_organizer.src.logger import setup_logger
```

---

## 📌 Šta je dot notacija?

- Tačkasta notacija je način da pristupimo atributima, metodama ili podmodulima tako što ih povezujemo tačkama (`.`). Svaka tačka predstavlja silazak jedan nivo dublje u neki **namespace** ili objekat.

---

## 📌 Kako funkcioniše kod importa

U ovom primeru:

```python
from day01_file_organizer.src.logger import setup_logger
```

1. **`day01_file_organizer`**

Ovo je **glavni paket** (folder) u korenu projekta koji sadrži `__init__.py` fajl (ili ga Python prepoznaje kao paket).

2. **`.src`**

Ovo znači "u okviru `day01_file_organizer` paketa idi u podpaket (folder) `src`".

1. **`.logger`**

U okviru `src` otvori modul `logger.py` (Python fajl).

2. **`import setup_logger`**

Iz modula `logger.py` uvezi **funkciju `setup_logger`** tako da je možemo koristiti direktno bez pisanja `logger.setup_logger`.

---

## 📌 Zašto se ovo zove dot notacija?

Svaka tačka označava **korak dublje u hijerarhiji**:

1. Prva tačka → ulazak u podpaket ili modul.
2. Druga tačka → još dublje u sledeći modul ili objekat.
3. Nastavljaš dok ne dođeš do finalne funkcije, promenljive ili klase.

---

## 📌 Mini demonstracija

Imamo sledeću strukturu:

```
my_project/
│
├── utils/
│   ├── __init__.py
│   ├── math_tools.py
│
└── main.py
```

**`math_tools.py`**

```python
def add(a, b):
    return a + b
```

**`main.py`**

```python
from utils.math_tools import add

result = add(2, 3)
print(result)  # Output: 5
```

Ovde je `utils` paket, `math_tools` modul, a `add` funkcija. Tačkasta notacija nam omogućava da precizno navedemo putanju.

---

## 📌 Veza sa OOP i objektima

Tačkasta notacija se koristi i za pristup atributima/metodama objekata:

```python
text = "hello"
print(text.upper())  # 'upper' je metoda string objekta
```

---

## 1. Odnos `logging` modula i `Logger` objekata

- **`logging` modul** je **fabrika** i menadžer svih loggera u programu.
  On sadrži:

  - globalne funkcije (`logging.info()`, `logging.warning()`, itd.)
  - klasu `Logger` (definiše metodu `setLevel()`, `info()`, itd.)
  - mehanizme za kreiranje handlera, formattera, i sl.

- **`logging.getLogger(name)`** vraća ti **instancu klase `Logger`**.
  Dakle:

  ```python
  logger = logging.getLogger("demo_logger")
  type(logger)  # <class 'logging.Logger'>
  ```

  Taj objekat **ima sve metode definisane u `Logger` klasi**, uključujući `setLevel`, `info`, `debug`, itd.

---

## 2. Zašto ne ide `logger.setLevel(logger.INFO)`

- `INFO` nije atribut _instance_ (`logger`), nego **konstanta definisana u modulu** `logging` (ili u samoj `Logger` klasi, ali kao **class-level attribute**, ne kao instance attribute).
  Drugim rečima:

  ```python
  >>> hasattr(logger, "INFO")
  False
  >>> logging.INFO
  20
  ```

- Kad napišeš `logger.INFO`, Python gleda **atribut instance** `logger` → ne nalazi ga. Kod funkcija iz modula `logging` (`logging.INFO`) ili klasa (`logging.Logger.INFO`), ovo radi jer se vrednost gleda iz **class scope-a**, a ne iz instance.

---

## 3. Kako se „nasleđuje“ funkcionalnost

- **`Logger` objekat** dobija metode (`setLevel`, `info`, …) iz **klase `Logger`** (OOP princip).
- Ali **konstante nivoa** (`DEBUG=10`, `INFO=20`, itd.) nisu „instance atributi“, nego **class atributi** ili vrednosti definisane direktno u `logging` modulu.
- Kada pozoveš:

  ```python
  logger.setLevel(logging.INFO)
  ```

  ti zapravo prosleđuješ integer `20`, a ne „metodu“ ili „funkciju“.

---

## 4. Zašto `logging.INFO` i ne `logger.INFO`

- **`logging` modul** centralizuje definicije nivoa logovanja (kao konstante).
- Možeš napisati i:

  ```python
  from logging import INFO
  logger.setLevel(INFO)
  ```

  i to će raditi identično.

- Teoretski možeš pristupiti i preko `Logger.INFO`, ali ne preko `logger.INFO` (jer je to instance, ne klasa).

---

💡 **Mentalni model:**
`logger` je **objekat** sa metodama (`setLevel`…), a `logging` je **modul** sa globalnim konstantama i fabrikama za kreiranje tih objekata. Konstante nivoa **nisu deo instance**, nego deo zajedničkog prostora (`logging` modul ili `Logger` klasa).

---

## 📊 Dijagram odnosa

Evo kako izgleda dijagram odnosa između `logging` modula, `Logger` klase i tvoje instance `logger`, sa naglaskom gde se nalaze metode a gde konstante.

```
+-----------------------------+
|         logging (modul)     |
|-----------------------------|
| INFO = 20                   |  <-- konstante nivoa
| DEBUG = 10                  |
| ...                         |
|                             |
| getLogger(name) -> Logger   |  <-- fabrika logger objekata
| basicConfig(...)            |
| ...                         |
+-----------------------------+
              |
              v
+-----------------------------+
|     Logger (klasa)          |   <-- definisana u logging modulu
|-----------------------------|
| + INFO = 20                 |   <-- class attribute (nije u instanci)
| + setLevel(level)           |
| + info(msg)                 |
| + debug(msg)                |
| + addHandler(handler)       |
| ...                         |
+-----------------------------+
              |
              v
+-----------------------------+
|     logger (instanca)       |   <-- dobijena iz getLogger()
|-----------------------------|
|  setLevel(...)              |  <-- metode dobijene iz klase
|  info(...)                  |
|  debug(...)                 |
|  addHandler(...)            |
|  ...                        |
|  (nema atribut INFO)        |
+-----------------------------+
```

---

## 🔍 Ključne tačke

1. **`logging.INFO`** → konstanta iz modula (`20`), globalno važi za sve loggere.
2. **`Logger.INFO`** → class-level konstanta u klasi `Logger`, takođe `20`.
3. **`logger.INFO`** → ne postoji, jer instanca loggera ne dobija tu konstantu automatski kao svoj atribut.
4. **`logger.setLevel(logging.INFO)`** → poziva metodu iz instance (`setLevel`) i prosleđuje joj vrednost `20`.

---

## pytestovi

---

## 🧩 1. Šta je test?

**Test** je deo koda koji **automatski proverava** da li drugi deo koda radi onako kako očekujemo.
To je kao mali “čuvar” koji stalno proverava: _"Da li se ponašaš onako kako sam ti rekao?"_

- **Bez testa**:
  Moramo ručno pokretati program, unositi podatke, posmatrati izlaz i odlučiti da li je rezultat tačan. To oduzima vreme i lako se potkrade greška.
- **Sa testom**:
  Pišemo kod koji automatski unosi podatke, pokreće funkcije i proverava rezultat. Ako nešto ne radi, test će nas odmah obavestiti.

---

## 🛠 2. Zašto su testovi važni?

- **Štede vreme** – umesto da stalno ručno proveravamo, pustimo testove da to urade.
- **Smanjuju greške** – testovi otkriju problem čim se pojavi, pre nego što kod ode u “produkciju”.
- **Održavaju kvalitet** – svaka izmena u kodu može da pokvari nešto staro, a testovi to otkrivaju.

---

## 📦 3. Kako Pytest ulazi u priču?

`pytest` je **alat** (framework) koji:

1. Automatski pronalazi test fajlove i funkcije koje počinju sa `test_`.
2. Pokreće ih i prijavljuje rezultate.
3. Olakšava pisanje čitljivih provera (_assertions_).

Primer:

```python
# test_math.py
def test_addition():
    assert 2 + 2 == 4   # ✅ prolazi
    assert 2 + 2 == 5   # ❌ pada
```

Pokretanje:

```bash
pytest
```

Rezultat:

```
================= FAILURES =================
>       assert 2 + 2 == 5
E       assert 4 == 5
```

---

## 🎯 4. Kako se test povezuje sa logger.py?

Za naš `logger.py`, testovi bi mogli da provere:

- Da li se logger kreira sa pravim imenom.
- Da li ispisuje poruke na pravom nivou (`INFO`, `ERROR`…).
- Da li rotirajući fajl zapravo rotira kada dostigne limit.

---

### Ručni test (bez pytest-a)

```python
# manual_logger_check.py
from pathlib import Path
from day01_file_organizer.src.logger import setup_logger

def run_manual_check():
    # 1) pripremi privremeni log direktorijum
    tmp_dir = Path("tmp_logs_manual")
    tmp_dir.mkdir(exist_ok=True)

    # 2) podigni logger (bez rotacije) i zapiši nešto
    logger = setup_logger(log_dir=tmp_dir)  # koristi naš parametar za lakše testiranje
    logger.info("manual check: hello")

    # 3) proveri da li je nastao fajl i da li sadrži poruku
    files = sorted(tmp_dir.glob("log_*.txt"))
    assert files, "Nije kreiran nijedan log fajl."
    content = files[-1].read_text(encoding="utf-8")
    assert "manual check: hello" in content, "Poruka nije upisana u log fajl."

    print("OK: fajl kreiran i poruka upisana:", files[-1])

if __name__ == "__main__":
    run_manual_check()
```

**Šta vidimo ovde**

- Ručno pravimo “test” korišćenjem `assert`.
- Ako nešto ne valja, `assert` će baciti grešku; u suprotnom dobijamo “OK” poruku.
- Mana: ovo je _ad-hoc_; nema lepog izveštaja, teško se skalira.

---

### Pytest verzija istog testa

```python
# tests/test_day01_file_organizer/test_logger.py
from pathlib import Path
from day01_file_organizer.src.logger import setup_logger

def test_plain_file_handler_creates_file_and_writes(tmp_path: Path):
    # Arrange: pytest fixtura daje jedinstveni privremeni dir
    log_dir = tmp_path / "logs"

    # Act
    logger = setup_logger(log_dir=log_dir)  # bez rotacije
    logger.info("pytest check: hello")

    # Assert
    files = sorted(log_dir.glob("log_*.txt"))
    assert files, "Nije kreiran nijedan log fajl."
    content = files[-1].read_text(encoding="utf-8")
    assert "pytest check: hello" in content
```

#### Kako pokrenuti

Iz root-a repo-a:

```bash
pytest -q
```

Očekuješ izlaz bez grešaka (tiho) ili sa kratkim brojačem testova:

```
.....                                                       [100%]
1 passed in 0.12s
```

---

#### 3) Šta smo upravo dobili (konceptualno)

- **Ručni test** ti je pokazao suštinu: _Arrange → Act → Assert_.
- **Pytest** taj isti obrazac radi automatski, daje **izveštaje**, **izolovane privremene foldere** (`tmp_path`), i lako ga je širiti (više test funkcija, više fajlova).

---

# pytest

## 1) Šta je test?

- **Test** je mali komad koda koji **automatski proverava** da li druga funkcija/klasa radi kako očekujemo.
- Cilj: **brza povratna informacija** i **sigurnost** posle svake izmene.

**Obrazac razmišljanja:**
**Arrange** (priprema) → **Act** (izvršavanje) → **Assert** (provera).

---

## 2) Zašto pytest?

- **Automatsko otkrivanje** testova (`test_*.py`, funkcije `test_*`).
- **Jednostavan assert** (nema posebnih API-ja).
- **Fixtur-e**: `tmp_path`, `caplog`, `monkeypatch`…
- Brzi i čitljivi izveštaji.

---

## 3) Kako pytest pronalazi testove
w
- Imena fajlova: `test_*.py` ili `*_test.py`
- Imena funkcija: `test_*`
- Podrazumevano pokreće sve testove u projektu iz **`pytest`** komande u root-u repozitorijuma.

**Primer pokretanja:**

```bash
pytest -q                 # svi testovi, tihi izlaz
pytest -q tests/path/to/test_file.py::test_one_case
pytest -q -k "logger and not rotation"   # selekcija po ključnoj reči
```

---

## 4) Najkorisnije fixtur-e (osnove)

### `tmp_path`

- Daje **privremeni direktorijum** specifičan za test.
- Koristi se za rad sa fajlovima (logovi, izlazi, sl.); pytest ga automatski briše.

```python
def test_primena_tmp_path(tmp_path):
    f = tmp_path / "demo.txt"
    f.write_text("hello", encoding="utf-8")
    assert f.read_text(encoding="utf-8") == "hello"
```

### `caplog`

- Hvata log poruke pa možeš da proveriš **šta je logger emitovao**.

```python
import logging

def test_caplog_example(caplog):
    logger = logging.getLogger("demo")
    with caplog.at_level(logging.INFO):
        logger.info("pozdrav")
    assert "pozdrav" in caplog.text
```

> Napomena: u složenijim slučajevima konfigurišemo logger/handlere pre `with` bloka.

---

## 5) Mini primer: naš prvi test bez rotacije (za logger)

Pretpostavka: u projektu imaš `day01_file_organizer/src/logger.py` sa funkcijom `setup_logger(log_dir=...)`.

```python
# tests/test_day01_file_organizer/test_logger_basic.py
from pathlib import Path
from day01_file_organizer.src.logger import setup_logger

def test_plain_file_handler_creates_file_and_writes(tmp_path: Path):
    log_dir = tmp_path / "logs"
    logger = setup_logger(log_dir=log_dir)   # bez rotacije
    logger.info("pytest check: hello")

    files = sorted(log_dir.glob("log_*.txt"))
    assert files, "Nije kreiran nijedan log fajl."

    content = files[-1].read_text(encoding="utf-8")
    assert "pytest check: hello" in content
```

**Šta proveravamo:**

- Nastao je log-fajl.
- Sadrži očekivanu poruku.

---

## 6) Rotacija po veličini (RotatingFileHandler)

> U `setup_logger` smo dodali opcije za rotaciju. U testu simuliramo brzo “pucanje” veličine.

```python
# tests/test_day01_file_organizer/test_logger_rotation_size.py
from pathlib import Path
from day01_file_organizer.src.logger import setup_logger
import logging

def test_rotating_file_handler_creates_multiple_files(tmp_path: Path):
    log_dir = tmp_path / "logs"

    # Ako si već koristio isti imenovani logger u drugim testovima, očisti mu handlere:
    logger = logging.getLogger("file_organizer")
    for h in list(logger.handlers):
        logger.removeHandler(h)

    logger = setup_logger(
        log_dir=log_dir,
        rotate_by="size",
        size_bytes=200,   # mala granica zbog testa
        backups=2
    )

    for i in range(50):
        logger.info(f"Log entry {i} - rotating soon")

    # Baza: app.log, rotacije: app.log.1, app.log.2 ...
    files = list(log_dir.iterdir())
    names = [p.name for p in files]
    assert "app.log" in names
    assert any(n.startswith("app.log.") for n in names), "Nema rotiranih fajlova (.1, .2...)"
```

---

## 7) Rotacija po vremenu (TimedRotatingFileHandler)

> Ne čekamo realnu rotaciju u testu (to bi usporilo). Samo proverimo da je handler pravog tipa.

```python
# tests/test_day01_file_organizer/test_logger_rotation_time.py
from pathlib import Path
import logging
from logging.handlers import TimedRotatingFileHandler
from day01_file_organizer.src.logger import setup_logger

def test_timed_rotating_file_handler_type(tmp_path: Path):
    log_dir = tmp_path / "logs"

    logger = logging.getLogger("file_organizer")
    for h in list(logger.handlers):
        logger.removeHandler(h)

    logger = setup_logger(
        log_dir=log_dir,
        rotate_by="time",
        when="S",       # sekunde (samo u testu)
        interval=1,
        backups=1
    )

    types = {type(h) for h in logger.handlers}
    assert TimedRotatingFileHandler in types
```

---

## 8) Čišćenje logger handlera u testovima (važna praksa)

Pošto koristimo **imenovani** logger (`"file_organizer"`), više testova u istom procesu mogu da mu **dodaju duple handlere**. Rešenje: na početku testa očistiti postojeće handlere:

```python
import logging

logger = logging.getLogger("file_organizer")
for h in list(logger.handlers):
    logger.removeHandler(h)
```

Ovo držimo u testu ili izdvojimo u pomoćnu funkciju/fixturu.

---

## 9) Struktura test foldera (dogovor za repo)

- Globalni `tests/` u root-u.
- Podfolder po projektu:

```
tests/
└── test_day01_file_organizer/
    ├── test_logger_basic.py
    ├── test_logger_rotation_size.py
    └── test_logger_rotation_time.py
```

---

## 10) Kratak vodič: kako čitati pad (FAIL)

Primer izlaza:

```
>       assert "pytest check: hello" in content
E       AssertionError: assert False
E        +  where False = ('pytest check: hello' in 'INFO | something else')
```

- Gledaš **očekivanje** vs **stvarni sadržaj**.
- Ako je format drugačiji, proveri **formatter** u `setup_logger` ili da li je poruka stvarno ispisana.

---

## 11) Šta sledeće (kada se uhodaš)

- **`parametrize`** za više ulaza u jednom testu:

```python
import pytest

@pytest.mark.parametrize("level", ["INFO", "ERROR"])
def test_levels(level):
    ...
```

- **`monkeypatch`** za menjanje okruženja ili vremena (kad budemo testirali time-based scenarije ozbiljnije).
- **`caplog`** za detaljno asertovanje poruka i nivoa.

---

## 12) Minimalni “cheatsheet”

- Pokreni: `pytest -q`
- Selektivno: `pytest -q tests/...::test_nesto`
- Fixtura-fajlovi: `conftest.py` (naprednije; za zajedničke fixtur-e)
- Pravilo: **mali, fokusirani testovi** (Arrange → Act → Assert)

---

## 13) Mini to-do (za mene kao učenika)

- [ ] Pokreni `pytest -q` iz root-a i vidi da li su testovi zeleni
- [ ] Dodaj bar jedan `caplog` test za `logger.info(...)`
- [ ] Napravi jedan **negativan** test (npr. pogrešan `rotate_by` → očekuj `ValueError`)
- [ ] Pređi kroz log fajlove u `tmp_path` da vizuelno vidiš strukturu i formate

---

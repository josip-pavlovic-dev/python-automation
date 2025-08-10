# 🧪 Pytest – vodič za početnike

## 1) Šta je test?

- **Test** je mali deo koda koji **automatski proverava** da li neka funkcija ili klasa radi kako očekujemo.
- Cilj: **brza povratna informacija** i **sigurnost** posle svake izmene.

**Obrazac razmišljanja:**  
**Arrange** (priprema) → **Act** (izvršavanje) → **Assert** (provera)

## 2) Zašto koristiti pytest?

- **Automatsko otkrivanje** testova (`test_*.py`, funkcije `test_*`)
- **Jednostavan assert** (nema posebnih API-ja)
- **Fixtur-e**: `tmp_path`, `caplog`, `monkeypatch`…
- Brzi i čitljivi izveštaji

## 3) Kako pytest pronalazi testove

- Imena fajlova: `test_*.py` ili `*_test.py`
- Imena funkcija: `test_*`
- Podrazumevano pokreće sve testove u projektu iz komande:

```bash
pytest
```

**Primer pokretanja:**

```bash
pytest -q                              # svi testovi, tihi izlaz
pytest -q tests/test_logger.py         # jedan fajl
pytest -q -k "logger and not rotation" # selekcija po ključnoj reči
```

## 4) Najkorisnije fixtur-e (osnovno)

### `tmp_path`

- Daje **privremeni direktorijum** specifičan za test.
- Koristi se za rad sa fajlovima; pytest ga automatski briše.

```python
def test_tmp_path(tmp_path):
    fajl = tmp_path / "primer.txt"
    fajl.write_text("zdravo", encoding="utf-8")
    assert fajl.read_text(encoding="utf-8") == "zdravo"
```

### `caplog`

- Hvata log poruke pa možeš da proveriš šta je logger emitovao.

```python
import logging

def test_caplog(caplog):
    logger = logging.getLogger("demo")
    with caplog.at_level(logging.INFO):
        logger.info("pozdrav")
    assert "pozdrav" in caplog.text
```

## 5) Primer testa za logger bez rotacije

```python
from pathlib import Path
from day01_file_organizer.src.logger import setup_logger

def test_logger_bez_rotacije(tmp_path: Path):
    log_dir = tmp_path / "logs"
    logger = setup_logger(log_dir=log_dir)
    logger.info("pytest provera")

    fajlovi = sorted(log_dir.glob("log_*.txt"))
    assert fajlovi, "Nije kreiran nijedan log fajl."

    sadrzaj = fajlovi[-1].read_text(encoding="utf-8")
    assert "pytest provera" in sadrzaj
```

## 6) Primer testa rotacije po veličini

```python
from pathlib import Path
import logging
from day01_file_organizer.src.logger import setup_logger

def test_rotacija_po_velicini(tmp_path: Path):
    log_dir = tmp_path / "logs"
    logger = logging.getLogger("file_organizer")
    for h in list(logger.handlers):
        logger.removeHandler(h)

    logger = setup_logger(
        log_dir=log_dir,
        rotate_by="size",
        size_bytes=200,
        backups=2
    )

    for i in range(50):
        logger.info(f"Log unos {i}")

    fajlovi = [p.name for p in log_dir.iterdir()]
    assert "app.log" in fajlovi
    assert any(n.startswith("app.log.") for n in fajlovi)
```

## 7) Struktura foldera sa testovima

```
tests/
└── test_day01_file_organizer/
    ├── test_logger_basic.py
    ├── test_logger_rotation_size.py
    └── test_logger_rotation_time.py
```

## 8) Kratak vodič za čitanje pada (FAIL)

Primer:

```
>       assert "pytest provera" in sadrzaj
E       AssertionError: assert False
```

- Pogledaj očekivanje i stvarni sadržaj.
- Ako je format drugačiji, proveri formatter ili samu poruku.

## 9) Sledeći koraci kada se uhodaš

- **`parametrize`** za više ulaza:

```python
import pytest

@pytest.mark.parametrize("level", ["INFO", "ERROR"])
def test_nivoi(level):
    ...
```

- **`monkeypatch`** za menjanje okruženja
- **`caplog`** za detaljnije provere log poruka

## 10) Mini to-do lista

- [ ] Pokrenuti `pytest -q` iz root-a i proveriti da su testovi zeleni
- [ ] Dodati jedan `caplog` test
- [ ] Dodati jedan negativan test (`ValueError` za pogrešan `rotate_by`)
- [ ] Vizuelno pregledati log fajlove u `tmp_path`
      EOF

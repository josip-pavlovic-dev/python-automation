# Pytest Essentials — Chat Backup (2025‑08‑13) | _Rezerva chata_

> This file is a snapshot of today’s decisions and configs for the `padd_logger` project. | _Ovaj fajl je snimak današnjih odluka i konfiguracija za projekat `padd_logger`._

## ✅ Decisions | _Odluke_

- Use `pyproject.toml` in `padd_logger/` as local pytest config. | _Koristi `pyproject.toml` u `padd_logger/` kao lokalni pytest config._
- Keep root `pytest.ini` to route test discovery to `padd_logger/tests`. | _Zadrži root `pytest.ini` da usmeri testove na `padd_logger/tests`._
- Enable coverage with HTML report. | _Uključi coverage sa HTML izveštajem._
- `pytest_essentials.md` serves as README for all pytest topics. | _`pytest_essentials.md` je README za sve pytest teme._

## 🧰 Updated Configs | _Ažurirane postavke_

### Root `pytest.ini`

```ini
[pytest]
testpaths =
    padd_logger/tests
addopts = -vv -ra -s
log_cli = true
log_cli_level = INFO
norecursedirs = legacy .git .venv __pycache__
pythonpath = .

```

---

#### padd_logger/pyproject.toml

```toml
[tool.pytest.ini_options]
addopts = "-vv -ra -s --cov=src --cov-report=term-missing --cov-report=html"
testpaths = ["tests"]
pythonpath = ["src"]
log_cli = true
log_cli_level = "INFO"
minversion = "8.0"

```

---

## ▶️ How to Run | Kako pokrenuti

```bash
# from padd_logger/
pytest
# HTML coverage report:
# Windows
start htmlcov/index.html
# Linux
xdg-open htmlcov/index.html
# macOS
open htmlcov/index.html

```

## 📦 Test Suite Layout | Raspored testova

```tests/
├── unit/
│   ├── test_logger.py
│   └── test_main.py
├── utils/
│   └── test_interactive_folder_browser.py
└── integration/
    └── test_end_to_end.py
```

---

## 🧪 Current State | Trenutno stanje

Unit tests pass (logger, main, utils). | Unit testovi prolaze (logger, main, utils).

E2E now uses main.run_flow(...). | E2E sada koristi main.run_flow(...).

HTML coverage generated in htmlcov/. | HTML coverage se generiše u htmlcov/.

---

## 🎯 Next Steps | Sledeći koraci

Add caplog assertions to verify log format (time/level/name/message). | Dodati caplog asercije za format loga (vreme/nivo/ime/poruka).

Validate invalid level raises ValueError. | Validirati da nevažeći nivo baca ValueError.

Optional: add --cov-report=xml for CI. | Opciono: dodati --cov-report=xml za CI.

---

## 📝 Commit Message | Commit poruka

```
test(config): enable verbose pytest with live logs and HTML coverage
```

---

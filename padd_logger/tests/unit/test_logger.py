import logging
from pathlib import Path

import pytest


def test_sanity():
    # ENG: Simple sanity check to verify pytest works
    # SR: Osnovna provera da pytest radi
    assert 2 + 2 == 4


def test_get_logger_contract(tmp_path: Path):
    """
    Minimalni ugovor:
    - postoji funkcija `get_logger(name, level="INFO", log_file: Path|None=None)`
    - vraća `logging.Logger`
    - ne duplira handlere na višestruke pozive za isti `name`
    - ako je `log_file` zadat, log fajl nastaje i sadrži bar jednu poruku
    """
    import logger  # src/logger.py (može biti prazan na početku)

    if not hasattr(logger, "get_logger"):
        pytest.xfail("get_logger() not implemented yet")

    get_logger = logger.get_logger  # type: ignore[attr-defined]

    log_path = tmp_path / "app.log"
    lg = get_logger(name="padd-tests", level="DEBUG", log_file=log_path)

    assert isinstance(lg, logging.Logger)
    assert lg.name == "padd-tests"
    assert lg.level == logging.DEBUG
    assert lg.handlers, "Expect at least one handler configured"

    lg.debug("hello from padd")
    if lg.handlers and hasattr(lg.handlers[0], "flush"):
        lg.handlers[0].flush()

    assert log_path.exists()
    assert log_path.read_text(encoding="utf-8").strip()

    before = len(lg.handlers)
    lg2 = get_logger(name="padd-tests", level="DEBUG", log_file=log_path)
    assert lg2 is lg
    assert len(lg2.handlers) == before, "No duplicate handlers expected"

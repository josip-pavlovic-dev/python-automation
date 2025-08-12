import logging

import pytest


@pytest.fixture
def test_logger(tmp_path):
    """
    Jednostavan, zajednički logger za testove.
    Koristi se po potrebi (nije obavezan u minimalnom skeletu).
    """
    logger = logging.getLogger("tests")
    logger.setLevel(logging.DEBUG)

    log_file = tmp_path / "tests.log"
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(levelname)s | %(name)s | %(message)s"))

    logger.handlers.clear()
    logger.addHandler(fh)
    logger.propagate = False
    return logger

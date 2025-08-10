# tests/test_logger.py
import logging
from pathlib import Path

from src.logger import LogConfig, configure_logger


def test_file_logging_writes_message(tmp_path: Path):
    log_file = tmp_path / "test.log"
    cfg = LogConfig(
        name="test.file",
        level=logging.INFO,
        console=False,
        file_path=log_file,
        rotating=False,
        reset=True,  # ensure clean for this test
    )
    logger = configure_logger(cfg)
    logger.info("hello world")

    assert log_file.exists()
    text = log_file.read_text(encoding="utf-8")
    assert "hello world" in text
    assert "INFO" in text


def test_no_duplicate_handlers_when_not_reset(tmp_path: Path):
    log_file = tmp_path / "dup.log"
    base_cfg = LogConfig(
        name="test.dup",
        level=logging.DEBUG,
        console=True,
        file_path=log_file,
        reset=True,
    )
    logger1 = configure_logger(base_cfg)
    # Re-configure WITHOUT reset -> should not add extra handlers
    logger2 = configure_logger(LogConfig(name="test.dup", console=True, file_path=log_file, reset=False))

    assert logger1 is logger2
    # Expect exactly 2 handlers: console + file
    assert len(logger2.handlers) == 2

    # Sanity: log writes to file once
    logger2.info("once")
    text = log_file.read_text(encoding="utf-8")
    assert text.count("once") == 1


def test_reset_allows_clean_reconfiguration(tmp_path: Path):
    log_file1 = tmp_path / "a.log"
    log_file2 = tmp_path / "b.log"

    logger = configure_logger(LogConfig(name="test.reset", file_path=log_file1, console=False, reset=True))
    logger.info("in a")
    assert log_file1.exists()

    # Reconfigure with reset=True to point to a different file
    logger = configure_logger(LogConfig(name="test.reset", file_path=log_file2, console=False, reset=True))
    logger.info("in b")
    assert log_file2.exists()

    text_a = log_file1.read_text(encoding="utf-8")
    text_b = log_file2.read_text(encoding="utf-8")
    assert "in a" in text_a and "in b" in text_b

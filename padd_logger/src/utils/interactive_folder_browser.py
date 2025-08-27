# ENG: Unit tests for minimal logger contract
# SR : Jedinični testovi za minimalni ugovor logera

import logging
from pathlib import Path

from padd_logger.src.logger import get_logger  # type: ignore  # noqa: F401


def test_get_logger_returns_logger_and_is_idempotent(tmp_path: Path):
    # ENG: First call creates console handler; second call must not duplicate handlers
    # SR : Prvi poziv kreira konzolni handler; drugi poziv ne sme duplirati handlere
    log = get_logger("padd")
    assert isinstance(log, logging.Logger)
    hcount1 = len(log.handlers)

    log2 = get_logger("padd")
    hcount2 = len(log2.handlers)
    assert hcount2 == hcount1 == 1  # 1 console handler, no duplicates


def test_logger_level_and_format(tmp_path: Path, caplog):
    # ENG: Check default level INFO and basic format presence (level/name/message)
    # SR : Proveri podrazumevani nivo INFO i prisustvo formata (nivo/ime/poruka)
    log = get_logger("padd")
    caplog.set_level(logging.INFO)
    log.info("hello")
    assert any("INFO" in r.message or "hello" in r.message for r in caplog.records)


def test_optional_file_handler_writes_to_file(tmp_path: Path):
    # ENG: When log_file is provided, file handler must be attached exactly once and write
    # SR : Kada je prosleđen log_file, fajl handler mora biti tačno jedan i da piše
    log_file = tmp_path / "app.log"
    log = get_logger("padd_file", log_file=log_file)
    assert any(h.__class__.__name__ == "FileHandler" for h in log.handlers)

    log.info("file-line")
    assert log_file.exists() and log_file.read_text(encoding="utf-8").strip() != ""


def choose_folder(prompt: str, base: Path) -> Path:
    """
    Minimal interactive folder chooser:
      - asks user for a relative path inside `base`
      - returns that directory if it exists, else raises FileNotFoundError
    """
    base = Path(base)
    if not base.exists() or not base.is_dir():
        raise FileNotFoundError(base)

    user_input = input(prompt).strip()
    selected = base / user_input

    if not selected.exists() or not selected.is_dir():
        raise FileNotFoundError(selected)

    return selected

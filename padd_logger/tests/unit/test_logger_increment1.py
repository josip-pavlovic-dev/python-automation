# ENG: API defaults + single StreamHandler (idempotent).
# SR:  API podrazumevano + jedan StreamHandler (idempotentno).

import logging
import pytest
from typing import Any
from src.logger import get_logger, DEFAULT_FMT, DEFAULT_DATEFMT

def _stream_handlers(lg: logging.Logger) -> list[logging.StreamHandler[Any]]:
    # ENG: All stream handlers that are NOT file handlers.
    # SR:  Svi stream handler-i koji NISU file handler-i.
    return [
        h for h in lg.handlers
        if isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler)
    ]

def test_api_defaults_stream_handler_and_level() -> None:
    lg = get_logger("padd")
    sh = _stream_handlers(lg)
    assert lg.level == logging.INFO
    assert len(sh) == 1
    assert sh[0].formatter is not None
    # Check formatter setup (format + datefmt):
    assert getattr(sh[0].formatter._style, "_fmt", None) == DEFAULT_FMT
    assert getattr(sh[0].formatter, "datefmt", None) == DEFAULT_DATEFMT

def test_idempotent_stream_handler_on_multiple_calls() -> None:
    lg1 = get_logger("padd")
    lg2 = get_logger("padd")
    assert lg1 is lg2
    assert len(_stream_handlers(lg1)) == 1

def test_invalid_level_raises() -> None:
    with pytest.raises(ValueError):
        get_logger("padd", level="VERBOSE")  # unsupported level string

# ENG: Idempotent logger factory with a single StreamHandler by default.
# SR:  Idempotentna fabrika logera sa jednim StreamHandler-om po difoltu.

from __future__ import annotations
import logging
from pathlib import Path  # kept for next increment (FileHandler); unused for now
from typing import Optional, Union

# Defaults (public so tests can import them) | ENG/SR
DEFAULT_FMT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"

def _coerce_level(level: Optional[Union[int, str]], fallback: int = logging.INFO) -> int:
    # ENG: Accept int or string (e.g., "INFO"), else ValueError.
    # SR:  Prihvata int ili string (npr. "INFO"), inače ValueError.
    if level is None:
        return fallback
    if isinstance(level, int):
        return level
    if isinstance(level, str):
        up = level.upper()
        if up in logging._nameToLevel:
            return logging._nameToLevel[up]
        raise ValueError(f"Invalid log level string: {level!r}")
    raise ValueError(f"Invalid log level type: {type(level).__name__}")

def _make_formatter() -> logging.Formatter:
    # ENG: Unified formatter for all handlers.
    # SR:  Jedinstven formatter za sve handlere.
    return logging.Formatter(fmt=DEFAULT_FMT, datefmt=DEFAULT_DATEFMT)

def _ensure_stream_handler(logger: logging.Logger) -> None:
    # ENG: Ensure exactly one StreamHandler (non-file) with our formatter.
    # SR:  Obezbedi tačno jedan StreamHandler (ne-fajl) sa našim formatter-om.
    for h in logger.handlers:
        if isinstance(h, logging.StreamHandler) and not isinstance(h, logging.FileHandler):
            if h.formatter is None or getattr(h.formatter._style, "_fmt", None) != DEFAULT_FMT:
                h.setFormatter(_make_formatter())
            return
    sh = logging.StreamHandler()
    sh.setFormatter(_make_formatter())
    logger.addHandler(sh)

def get_logger(
    name: str,
    level: Union[int, str] = "INFO",
    log_file: Optional[Path] = None,  # kept for compatibility; used in next increment
) -> logging.Logger:
    """
    ENG: Create/fetch named logger, set level, and guarantee a single StreamHandler.
    SR:  Kreiraj/dobavi logger po imenu, postavi nivo i garantuj jedan StreamHandler.
    """
    lg = logging.getLogger(name)
    lg.setLevel(_coerce_level(level))
    lg.propagate = False
    _ensure_stream_handler(lg)
    # FileHandler will be added in v1.1 (utf-8, standard format). | ENG/SR
    return lg
    # Note: log_file is kept for compatibility; it will be used in the next increment.
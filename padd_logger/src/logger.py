from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Union

# --- internal helpers ---------------------------------------------------------

_LEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET,
}


def _coerce_level(level: Union[str, int]) -> int:
    if isinstance(level, int):
        return level
    if isinstance(level, str):
        lv = _LEVELS.get(level.upper())
        if lv is not None:
            return lv
    raise ValueError(f"Invalid logging level: {level!r}")


# --- public API ---------------------------------------------------------------

def get_logger(
    name: str,
    level: Union[str, int] = "INFO",
    log_file: Optional[Path] = None,
) -> logging.Logger:
    """
    Create or fetch a named logger.

    Rules:
      - idempotent by name (no duplicate handlers on repeated calls)
      - if log_file is provided: attach a single FileHandler to that file
      - ensure at least one handler exists (NullHandler when no file)
    """
    logger = logging.getLogger(name)
    logger.setLevel(_coerce_level(level))
    logger.propagate = False  # don't bubble to root handlers

    if log_file is not None:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)

        # Attach a FileHandler only if an identical one doesn't exist
        for h in logger.handlers:
            if isinstance(h, logging.FileHandler):
                try:
                    existing = Path(h.baseFilename).resolve()
                except Exception:
                    existing = None
                if existing and existing == log_file.resolve():
                    break  # already attached
        else:
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setLevel(logger.level)
            fh.setFormatter(
                logging.Formatter(
                    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                )
            )
            logger.addHandler(fh)
    else:
        # Ensure .handlers is truthy even without a file (tests expect at least one)
        if not logger.handlers:
            logger.addHandler(logging.NullHandler())

    return logger

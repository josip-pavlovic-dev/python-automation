"""
📁 day01_file_organizer/src/logger.py

Provides a logger configured with file and console (stream) handlers.

Obezbeđuje logger konfigurisan za upis u fajl i ispis u konzoli.
"""

from __future__ import annotations

import logging
import logging.handlers
import os
import sys
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class LogConfig:
    """
    Configuration object for building a logger.

    Attributes:
        name: Logger name (use __name__ or a domain-specific name).
        level: Root level for this logger (e.g., logging.INFO).
        console: Whether to add a console (stream) handler.
        console_use_color: Whether to use ANSI colors in console output.
        file_path: If provided, add a file handler (standard or rotating).
        rotating: Use RotatingFileHandler if True, else FileHandler.
        max_bytes: For rotating handler; ignored if rotating=False.
        backup_count: For rotating handler; ignored if rotating=False.
        fmt_console: Format string for console logs.
        fmt_file: Format string for file logs.
        datefmt: Datetime formatting for both handlers.
        propagate: Whether the logger propagates to ancestor loggers.
        reset: If True, clear existing handlers before configuring (pytest-friendly).
    """
    name: str = "app"
    level: int = logging.INFO

    console: bool = True
    console_use_color: bool = True

    file_path: Optional[Union[str, os.PathLike]] = None
    rotating: bool = False
    max_bytes: int = 1_000_000
    backup_count: int = 3

    fmt_console: str = "[%(asctime)s] %(levelname)s %(name)s: %(message)s"
    fmt_file: str = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    datefmt: str = "%Y-%m-%d %H:%M:%S"

    propagate: bool = False
    reset: bool = False


def configure_logger(cfg: LogConfig) -> logging.Logger:
    """
    Create or reconfigure a named logger according to `cfg`.

    - Idempotent when cfg.reset is False (won't re-add handlers).
    - Pytest-friendly when cfg.reset is True (clears handlers).
    """
    logger = logging.getLogger(cfg.name)
    logger.setLevel(cfg.level)
    logger.propagate = cfg.propagate

    # If not resetting and handlers exist, return as-is (avoid duplicates).
    if logger.handlers and not cfg.reset:
        return logger

    # Either resetting or first-time configuration.
    if cfg.reset:
        for h in list(logger.handlers):
            logger.removeHandler(h)
        logger.handlers.clear()

    # Console handler (optional)
    if cfg.console:
        ch = logging.StreamHandler(stream=sys.stdout)
        ch.setLevel(cfg.level)
        if cfg.console_use_color and _stream_supports_color(ch.stream):
            formatter = _ColorFormatter(fmt=cfg.fmt_console, datefmt=cfg.datefmt)
        else:
            formatter = logging.Formatter(fmt=cfg.fmt_console, datefmt=cfg.datefmt)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    # File handler (optional)
    if cfg.file_path:
        file_path_str = str(cfg.file_path)
        os.makedirs(os.path.dirname(file_path_str) or ".", exist_ok=True)

        if cfg.rotating:
            fh: logging.Handler = logging.handlers.RotatingFileHandler(
                file_path_str, maxBytes=cfg.max_bytes, backupCount=cfg.backup_count, encoding="utf-8"
            )
        else:
            fh = logging.FileHandler(file_path_str, encoding="utf-8")

        fh.setLevel(cfg.level)
        fh.setFormatter(logging.Formatter(fmt=cfg.fmt_file, datefmt=cfg.datefmt))
        logger.addHandler(fh)

    return logger


def _stream_supports_color(stream) -> bool:
    """Best-effort check for TTY to decide if ANSI colors are appropriate."""
    try:
        return hasattr(stream, "isatty") and stream.isatty()
    except Exception:
        return False


class _ColorFormatter(logging.Formatter):
    """
    Minimal ANSI colorizing formatter without external deps.
    Colors apply to the LEVEL token only, keeping the rest readable.
    """
    _LEVEL_COLORS = {
        logging.DEBUG: "\033[36m",   # Cyan
        logging.INFO: "\033[32m",    # Green
        logging.WARNING: "\033[33m", # Yellow
        logging.ERROR: "\033[31m",   # Red
        logging.CRITICAL: "\033[35m" # Magenta
    }
    _RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        original_levelname = record.levelname
        color = self._LEVEL_COLORS.get(record.levelno, "")
        if color:
            record.levelname = f"{color}{record.levelname}{self._RESET}"
        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname


if __name__ == "__main__":
    # Smoke demo for manual check
    config = LogConfig(
        name="demo",
        level=logging.DEBUG,
        console=True,
        console_use_color=True,
        file_path="logs/demo.log",
        rotating=True,
        max_bytes=200_000,
        backup_count=2,
        reset=True,  # ensure clean setup on each run
    )
    log = configure_logger(config)
    log.debug("Debug message")
    log.info("Info message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")
    print("Logger configured. Check console and logs/demo.log for output.")
    # Note: This main block is for manual testing and should not be used in production.
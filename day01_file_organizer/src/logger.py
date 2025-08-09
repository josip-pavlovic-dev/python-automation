"""
📁 day01_file_organizer/src/logger.py

Provides a logger configured with file and console (stream) handlers.

| _Obezbeđuje logger konfigurisan za upis u fajl i ispis u konzoli._
"""
import logging
from datetime import datetime
from pathlib import Path


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("file_organizer")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        return logger

    log_dir = Path(__file__).resolve().parent.parent / "log"
    log_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"log_{ts}.txt"

    fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    sh = logging.StreamHandler()

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)

    fh.setLevel(logging.INFO)
    sh.setLevel(logging.INFO)
    logger.addHandler(fh)
    logger.addHandler(sh)
    return logger

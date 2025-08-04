"""
📁 day01_file_organizer/src/logger.py

Provides a logger configured with file and console (stream) handlers.

| _Obezbeđuje logger konfigurisan za upis u fajl i ispis u konzoli._
"""

import logging
from pathlib import Path
from datetime import datetime

def setup_logger() -> logging.Logger:
    """
    Creates and configures a logger with file and stream handlers.

    | _Kreira i konfiguriše logger sa handlerima za fajl i terminal._
    """
    logger = logging.getLogger("file_organizer")
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger

    # ✅ Define log file path
    log_dir = Path(__file__).resolve().parent.parent / "log"
    log_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"log_{timestamp}.txt"

    # ✅ File handler
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setLevel(logging.INFO)

    # ✅ Stream handler (console)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # ✅ Formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # ✅ Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

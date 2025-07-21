# pyright: reportUndefinedVariable=false
from datetime import datetime
import os
import shutil

# 📌 Apsolutna putanja do log fajla
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

# 📌 ANSI boje
COLORS = {
    "INFO": "\033[92m",     # Zeleno
    "WARNING": "\033[93m",  # Žuto
    "ERROR": "\033[91m",    # Crveno
    "RESET": "\033[0m"      # Reset
}

# 📌 Limit veličine log fajla za rotaciju (u bajtovima)
MAX_LOG_SIZE = 100 * 1024  # 100 KB

def rotate_log():
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) >= MAX_LOG_SIZE:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"log_{timestamp}.txt"
        backup_path = os.path.join(BASE_DIR, backup_name)
        shutil.move(LOG_FILE, backup_path)

def log_message(message, level="INFO"):
    """
    Upisuje poruku u log.txt sa timestampom i nivoom poruke.
    Takođe štampa obojenu poruku u terminal.

    :param message: Tekst poruke
    :param level: INFO, WARNING, ERROR
    """
    rotate_log()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level_upper = level.upper()
    formatted_message = f"[{timestamp}] [{level_upper}] {message}"

    # Upis u fajl
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_message + "\n")

    # Ispis u terminal sa bojom
    color = COLORS.get(level_upper, COLORS["RESET"])
    print(color + formatted_message + COLORS["RESET"])


# ✅ Testiranje
if __name__ == "__main__":
    log_message("Test poruka", level="INFO")
    log_message("Ovo je upozorenje!", level="WARNING")
    log_message("Simulirana greška", level="ERROR")



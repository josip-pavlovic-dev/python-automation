# pyright: reportUndefinedVariable=false
from datetime import datetime
import os

# 📌 Apsolutna putanja do log fajla
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

def log(message, level="INFO"):
    """
    Upisuje poruku u log.txt sa timestampom i nivoom poruke.
    
    :param message: Tekst poruke
    :param level: INFO, WARNING, ERROR (default: INFO)
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level.upper()}] {message}"

   # Upis u fajl
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_message + "\n")

    # Ispis u terminal
    print(formatted_message)

# Testiranje funkcije log: 
if __name__ == "__main__":
    log("Test poruka (INFO)")
    log("Ovo je upozorenje!", level="WARNING")
    log("Simulirana greška", level="ERROR")



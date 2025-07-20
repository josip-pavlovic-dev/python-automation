import os
from day03_file_management.logger import log

log_path = os.path.join(os.path.dirname(__file__), "log.txt")

if os.path.exists(log_path):
    os.remove(log_path)

log("Ovo je upozorenje", level="WARNING")
log("Simulirana greška u testu", level="ERROR")

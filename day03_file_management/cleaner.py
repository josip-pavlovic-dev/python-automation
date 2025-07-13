# cleaner.py
import os
from logger import log

def clean_folder(folder_path, extension=".tmp"):
    try:
        log(f"Započinjem čišćenje foldera: {folder_path}", level="INFO")
        deleted_files = 0

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        log(f"Obrisan fajl: {file_path}", level="INFO")
                        deleted_files += 1
                    except Exception as e:
                        log(f"Greška pri brisanju fajla {file_path}: {str(e)}", level="ERROR")

        log(f"Čišćenje završeno. Obrisano ukupno {deleted_files} fajlova.", level="INFO")

    except Exception as e:
        log(f"Greška pri čišćenju foldera: {str(e)}", level="ERROR")


if __name__ == "__main__":
    clean_folder("test_folder", extension=".tmp")

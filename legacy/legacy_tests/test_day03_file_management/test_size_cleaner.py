import os
import shutil
import subprocess
from logger import log
from size_cleaner import clean_by_size

def list_files(folder_path):
    """
    Pomoćna funkcija koja ispisuje sve fajlove u folderu i podfolderima.
    """
    log(f"Preostali fajlovi u folderu: {folder_path}", level="INFO")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            log(f"{file_path} ({size} bajtova)", level="INFO")

if __name__ == "__main__":
    try:
        # Pokušavamo da pronađemo bash automatski (npr. Git Bash)
        bash_path = shutil.which("bash")
        if bash_path is None:
            raise RuntimeError("Bash interpreter nije pronađen. Da li je Git Bash instaliran?")

        # Pokrećemo bash skriptu
        subprocess.run([bash_path, "setup_test_folder.sh"], check=True)

        
        log("Test struktura kreirana.", level="INFO")

        # Pokretanje skripte za brisanje fajlova ispod 100 bajtova
        clean_by_size("test_folder", min_size=100)

        # Prikaz svih preostalih fajlova
        list_files("test_folder")

        log("Test size_cleaner.py skripte uspešno završen.", level="INFO")

    except Exception as e:
        log(f"Greška tokom testiranja: {str(e)}", level="ERROR")

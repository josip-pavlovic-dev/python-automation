# size_cleaner.py
import os
from logger import log


def clean_by_size(folder_path, min_size=100):
    """
    Briše fajlove u folderu (i podfolderima) koji su manji od min_size bajtova.

    :param folder_path: Putanja do foldera koji se skenira
    :param min_size: Minimalna veličina fajla u bajtovima (default: 100)
    """
    try:
        log(
            f"Započinjem čišćenje fajlova manjih od {min_size} bajtova u folderu: {folder_path}",
            level="INFO",
        )
        deleted_files = 0

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    if file_size < min_size:
                        os.remove(file_path)
                        deleted_files += 1
                        log(
                            f"Obrisan fajl: {file_path} ({file_size} bajtova)",
                            level="INFO",
                        )
                except Exception as e:
                    log(
                        f"Greška pri proveri fajla {file_path}: {str(e)}",
                        level="WARNING",
                    )

        log(
            f"Čišćenje završeno. Ukupno obrisano {deleted_files} fajlova.", level="INFO"
        )
    except Exception as e:
        log(f"Greška pri izvršavanju clean_by_size: {str(e)}", level="ERROR")


if __name__ == "__main__":
    clean_by_size("test_folder", min_size=100)

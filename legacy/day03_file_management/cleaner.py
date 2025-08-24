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
                    os.remove(file_path)
                    deleted_files += 1

        log(
            f"Čišćenje završeno. Obrisano ukupno {deleted_files} fajlova.", level="INFO"
        )

    except Exception as e:
        log(f"Greška pri čišćenju foldera: {str(e)}", level="ERROR")


if __name__ == "__main__":
    # Koristi baznu apsolutnu putanju iz foldera gde se cleaner.py nalazi
    base_folder = os.path.join(os.path.dirname(__file__), "test_folder")
    clean_folder(base_folder, extension=".tmp")
# Ovaj fajl je deo skripte za čišćenje foldera i briše sve fajlove sa ekstenzijom .tmp

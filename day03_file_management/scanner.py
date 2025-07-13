import os
from logger import log

target_folder = "day03_file_management/test_folder"

# 📌 Globalni brojač po tipu fajla
file_type_count = {}

def scan_folder(folder_path):
    try:
        log(f"📁 Skeniram folder: {folder_path}", level="INFO")

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):
                log(f"📂 Pronađen folder: {item_path}", level="INFO")
                scan_folder(item_path)

            elif os.path.isfile(item_path):
                log(f"📄 Pronađen fajl: {item_path}", level="INFO")

                # ➕ Ekstrahuj ekstenziju fajla
                _, ext = os.path.splitext(item)
                if ext:
                    file_type_count[ext] = file_type_count.get(ext, 0) + 1
                else:
                    file_type_count["(bez ekstenzije)"] = file_type_count.get("(bez ekstenzije)", 0) + 1

            else:
                log(f"⚠ Nepoznat tip stavke: {item_path}", level="WARNING")

    except Exception as e:
        log(f"❌ Greška pri skeniranju: {str(e)}", level="ERROR")

# 🔁 Pokretanje
if __name__ == "__main__":
    scan_folder(target_folder)

    # 📊 Ispis broja fajlova po tipu
    log("📊 Broj fajlova po tipu:", level="INFO")
    for ext, count in file_type_count.items():
        log(f"   {ext}: {count} fajl(ova)", level="INFO")


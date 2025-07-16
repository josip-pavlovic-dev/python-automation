import os
from logger import log

# 📁 Absolute path to the target folder based on current script location
# 📁 Apsolutna putanja do ciljanog foldera na osnovu lokacije ove skripte
target_folder = os.path.join(os.path.dirname(__file__), "test_folder")

# 📌 Global dictionary to count files by extension
# 📌 Globalni rečnik za brojanje fajlova po tipu (ekstenziji)
file_type_count = {}

def scan_folder(folder_path):
    """
    🔍 Recursively scans folder and logs structure
    🔍 Rekurzivno skenira folder i beleži strukturu
    """
    try:
        log(f"📁 Scanning folder: {folder_path}", level="INFO")
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            
            if os.path.isdir(item_path):
                log(f"📂 Folder found: {item_path}", level="INFO")
                scan_folder(item_path)

            elif os.path.isfile(item_path):
                log(f"📄 File found: {item_path}", level="INFO")

                # ➕ Extract file extension
                # ➕ Ekstrahuj ekstenziju fajla
                _, ext = os.path.splitext(item)
                if ext:
                    file_type_count[ext] = file_type_count.get(ext, 0) + 1
                else:
                    file_type_count["(no extension)"] = file_type_count.get("(no extension)", 0) + 1

            else:
                log(f"⚠ Unknown item type: {item_path}", level="WARNING")

    except Exception as e:
        log(f"❌ Error while scanning: {str(e)}", level="ERROR")

# ▶️ Script entry point
# ▶️ Ulazna tačka skripte
if __name__ == "__main__":
    scan_folder(target_folder)

    # 📊 Print file counts by type
    # 📊 Prikaz broja fajlova po tipu
    log("📊 File count by type:", level="INFO")
    for ext, count in file_type_count.items():
        log(f"   {ext}: {count} file(s)", level="INFO")
    log(f"✅ Finished scanning folder: {target_folder}", level="INFO")


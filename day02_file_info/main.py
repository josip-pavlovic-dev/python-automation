import os
import datetime
from logger import log_message

def analyze_files(folder_path):
    folder_path = folder_path.strip()  # uklanja višak razmaka
    if not os.path.isdir(folder_path):
        log_message(f"❌ Greška: Folder '{folder_path}' ne postoji.")
        print("⚠️  Folder nije pronađen. Proveri naziv i pokušaj ponovo.")
        return

    files = os.listdir(folder_path)
    if not files:
        log_message(f"📂 Folder '{folder_path}' je prazan.")
        print(f"📂 Folder '{folder_path}' je prazan.")
        return

    for filename in files:
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            ext = os.path.splitext(filename)[1] or 'N/A'
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

            log_message(
                f"📄 {filename} | Ekstenzija: {ext} | "
                f"Veličina: {file_size} B | Poslednja izmena: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )

if __name__ == "__main__":
    print("🔎 Unesi naziv foldera koji želiš da analiziraš (primer: test_files)")
    folder_input = input("📂 Folder: ").strip()
    analyze_files(folder_input)
print("✅ Analiza završena.")
log_message("✅ Analiza završena.")
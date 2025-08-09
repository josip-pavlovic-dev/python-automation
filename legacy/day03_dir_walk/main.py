import os
from datetime import datetime, timedelta

# 📌 Config
DAYS_THRESHOLD = 7
TARGET_FILE = "example.txt"  # <- Promeni ovo u stvarno ime fajla

# 📌 Get absolute path to the file
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir, TARGET_FILE)

# 📌 Check if file exists
if not os.path.exists(file_path):
    print(f"[❌] File does not exist: {file_path}")
else:
    # 📌 Get last modified time
    modified_time = os.path.getmtime(file_path)
    modified_datetime = datetime.fromtimestamp(modified_time)

    # 📌 Calculate threshold
    current_time = datetime.now()
    threshold_date = current_time - timedelta(days=DAYS_THRESHOLD)

    # 📌 Output
    print(f"[📄] File path: {file_path}")
    print(f"[🕓] Last modified: {modified_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[🗓️] Threshold date: {threshold_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # 📌 Compare dates
    if modified_datetime < threshold_date:
        print(f"[⚠️] File is older than {DAYS_THRESHOLD} days.")
    else:
        print(f"[✅] File is within the last {DAYS_THRESHOLD} days.")
    print(f"[ℹ️] File is located in: {script_dir}")
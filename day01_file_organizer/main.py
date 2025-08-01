"""
main.py
Project: day01_file_organizer
Author: Josip Pavlović

🇬🇧 This script organizes files in a selected folder by their extension into categorized subfolders.
🇷🇸 Ova skripta organizuje fajlove u izabranom folderu po ekstenziji u odgovarajuće podfoldere.
"""

import os
import shutil
from logger import setup_logger
from tkinter import Tk, filedialog

def browse_folders():
    """
    🇬🇧 Opens a folder selection dialog and returns the selected folder path.
    🇷🇸 Otvara dijalog za izbor foldera i vraća putanju izabranog foldera.
    """
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    folder_path = filedialog.askdirectory(title="Select Folder")
    root.destroy()
    return folder_path

# Initialize logger
logger = setup_logger()

def organize_files_by_extension(folder_path: str):
    """
    🇬🇧 Organizes files in the given folder by file extension.
    🇷🇸 Organizuje fajlove u datom folderu po ekstenziji.
    """
    logger.info(f"Organizing files in folder: {folder_path}")
    print(f"\n📂 Target folder: {folder_path}\n")

    try:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):
                file_ext = os.path.splitext(file)[1][1:]  # e.g. 'jpg', 'pdf'
                if not file_ext:
                    file_ext = "no_extension"

                destination_folder = os.path.join(folder_path, file_ext.upper())

                # Create destination folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    logger.info(f"Created folder: {destination_folder}")

                # Move file to the new folder
                new_path = os.path.join(destination_folder, file)
                shutil.move(file_path, new_path)
                logger.info(f"Moved: {file} → {destination_folder}")

    except Exception as e:
        logger.error(f"Error while organizing files: {e}")
        print("❌ An error occurred during organization.")

def main():
    """
    🇬🇧 Main function to start the folder browsing and organizing process.
    🇷🇸 Glavna funkcija koja pokreće izbor foldera i organizaciju fajlova.
    """
    print("🧠 File Organizer – Python Automation")
    target_folder = browse_folders()

    if target_folder:
        organize_files_by_extension(target_folder)
        print("\n✅ Organization complete.")
    else:
        print("\n⚠️ Folder not selected. Exiting.")

if __name__ == "__main__":
    main()

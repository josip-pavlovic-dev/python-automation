"""
Sorts files in the selected directory by their extension.
Uses argparse for CLI, Pathlib for paths, shutil for moving files, and a custom logger.
"""

from pathlib import Path
import shutil
import argparse

# 📌 Import custom modules
from src.logger import setup_logger
from src.utils.interactive_folder_browser import select_folder_gui

# ✅ Initialize logger
logger = setup_logger()

def get_arguments():
    """
    Parses command-line arguments.
    Returns the selected directory as a Path object.
    """
    parser = argparse.ArgumentParser(description="Organize files by extension.")
    parser.add_argument(
        "-p", "--path",
        type=Path,
        help="Path to the folder to organize."
    )
    args = parser.parse_args()

    if args.path and args.path.exists():
        logger.info(f"CLI folder path received: {args.path}")
        return args.path
    else:
        selected = select_folder_gui()
        logger.info(f"Selected folder via GUI: {selected}")
        return Path(selected)


def organize_files_by_extension(folder_path: Path):
    """
    Organizes files in the given folder by moving them into subfolders based on file extension.
    """
    for file in folder_path.iterdir():
        if file.is_file():
            ext = file.suffix[1:] or "no_extension"  # remove dot, fallback if no extension
            target_folder = folder_path / ext
            target_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(file), str(target_folder / file.name))
                logger.info(f"Moved {file.name} to {target_folder}")
            except Exception as e:
                logger.error(f"Error moving {file.name}: {e}")


if __name__ == "__main__":
    logger.info("🚀 File Organizer Started")
    folder = get_arguments()
    organize_files_by_extension(folder)
    logger.info("✅ File Organizer Finished")

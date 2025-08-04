# interactive_folder_browser.py
"""
📁 day01_file_organizer/src/utils/interactive_folder_browser.py

Provides a simple GUI dialog for selecting a directory.

| _Omogućava izbor foldera kroz grafički interfejs._
"""

from tkinter import Tk, filedialog
from pathlib import Path

def select_directory_gui() -> Path:
    """
    Launches a GUI file dialog to select a directory.

    | _Pokreće GUI dijalog za izbor direktorijuma._
    """
    root = Tk()
    root.withdraw()
    selected_path = filedialog.askdirectory()

    if not selected_path:
        raise ValueError("Nijedan folder nije izabran.")

    return Path(selected_path).resolve()

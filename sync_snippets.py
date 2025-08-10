# import os
import shutil
from pathlib import Path

# Lokacija izvornog foldera snippeta
SOURCE_DIR = Path("docs/vs-snippets")

# Lista globalnih fajlova koji se direktno kopiraju u glavni .vscode
GLOBAL_SNIPPETS = [
    "pylance_basics.code-snippets",
    "commenting_basics.code-snippets",
    "vscode_shortcuts_basics.code-snippets",
]

# Mapa: naziv fajla → ime foldera u koji treba da ide
FOLDER_MAP = {
    "day01_file_organizer.code-snippets": "day01_file_organizer",
    "day02_file_info.code-snippets": "day02_file_info",
    "day03_file_management.code-snippets": "day03_file_management",
    "day04_datetime.code-snippets": "day04_datetime",
}


# Pomoćna funkcija: briše sve .code-snippets fajlove iz datog .vscode foldera
def clean_vscode_folder(vscode_path: Path):
    if vscode_path.exists():
        for file in vscode_path.glob("*.code-snippets"):
            file.unlink()


# Glavna logika
def sync_snippets():
    project_root = Path.cwd()

    # 1. Globalni snippets → python-automation/.vscode
    root_vscode = project_root / ".vscode"
    root_vscode.mkdir(exist_ok=True)
    clean_vscode_folder(root_vscode)
    for snippet in GLOBAL_SNIPPETS:
        src_file = SOURCE_DIR / snippet
        if src_file.exists():
            shutil.copy2(src_file, root_vscode / snippet)

    # 2. Dnevni snippets po folderima
    for filename, folder in FOLDER_MAP.items():
        target_vscode = project_root / folder / ".vscode"
        target_vscode.mkdir(parents=True, exist_ok=True)
        clean_vscode_folder(target_vscode)
        src_file = SOURCE_DIR / filename
        if src_file.exists():
            shutil.copy2(src_file, target_vscode / filename)


if __name__ == "__main__":
    sync_snippets()

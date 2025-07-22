# import os  # Unused import – safe to remove
import shutil
from pathlib import Path

# Postavi root putanju prema tvojoj lokalnoj strukturi
PROJECTS_ROOT = Path("C:/Users/JoleDev/dev-learning/python-automation")
SNIPPETS_FOLDER = PROJECTS_ROOT / "docs" / "vs-snippets"

# Projekti i njihovi prefiksi za .code-snippets fajlove
projects = {
    "01-file-organizer": "day01_file_organizer",
    "day02_file_info": "day02_file_info",
    "day03_file_management": "day03_file_ops",
    "day04_datetime": "day04_datetime"
}

def sync_snippets():
    print("🔄 Syncing .code-snippets files to each project's .vscode folder...\n")

    for folder, base_name in projects.items():
        project_path = PROJECTS_ROOT / folder
        vscode_path = project_path / ".vscode"
        vscode_path.mkdir(parents=True, exist_ok=True)

        for lang in ["", "_sr"]:  # engleska i srpska verzija
            snippet_file = SNIPPETS_FOLDER / f"{base_name}{lang}.code-snippets"
            if snippet_file.exists():
                target_file = vscode_path / snippet_file.name
                shutil.copy(snippet_file, target_file)
                print(f"✔ {snippet_file.name} → {target_file}")
            else:
                print(f"⚠ {snippet_file.name} not found in vs-snippets")

    print("\n✅ Snippet sync complete.")

if __name__ == "__main__":
    sync_snippets()

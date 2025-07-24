import shutil
from pathlib import Path

# Tvoje osnovne putanje
PROJECTS_ROOT = Path("C:/Users/JoleDev/dev-learning/python-automation")
SNIPPETS_FOLDER = PROJECTS_ROOT / "docs" / "vs-snippets"

# Ručna mapiranja za izuzetke gde ime fajla ≠ ime foldera
FOLDER_MAP = {
    "day01_file_organizer": "01-file-organizer",
    "day03_file_ops": "day03_file_management"
}

def detect_target_folder(base_name: str) -> Path:
    # Ako je snippetu poznata zamena – koristi je
    if base_name in FOLDER_MAP:
        return PROJECTS_ROOT / FOLDER_MAP[base_name]
    # Inače koristi ime bez "_sr"
    return PROJECTS_ROOT / base_name

def sync_snippets():
    print("🔄 Auto-detecting and syncing .code-snippets to target .vscode folders...\n")

    for snippet_file in SNIPPETS_FOLDER.glob("*.code-snippets"):
        base_name = snippet_file.stem  # npr. day03_file_ops_sr
        name_without_sr = base_name.replace("_sr", "")

        target_folder = detect_target_folder(name_without_sr)
        vscode_path = target_folder / ".vscode"
        vscode_path.mkdir(parents=True, exist_ok=True)

        target_file = vscode_path / snippet_file.name
        shutil.copy(snippet_file, target_file)

        print(f"✔ {snippet_file.name} → {target_file}")

    print("\n✅ Snippet sync complete.")

if __name__ == "__main__":
    sync_snippets()

# Ova skripta automatski detektuje i sinhronizuje .code-snippets fajlove u odgovarajuće .vscode foldere. 
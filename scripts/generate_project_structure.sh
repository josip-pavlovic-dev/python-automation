#!/bin/bash

# 📌 SRPSKI: Ova skripta kreira strukturu foldera za novi mini-projekat.
# 📌 ENGLISH: This script generates a folder structure for a new mini-project.

# 📂 Root direktorijum gde se kreiraju projekti
ROOT="/c/Users/JoleDev/dev-learning/python-automation"

# 👉 Unesi ime projekta kao argument
PROJECT_NAME=$1

# ✅ Provera da li je argument prosleđen
if [ -z "$PROJECT_NAME" ]; then
  echo "⚠️  Morate uneti naziv projekta kao argument. Primer:"
  echo "./generate_project_structure.sh day07_new_project"
  exit 1
fi

# 📁 Potpuna putanja do projekta
PROJECT_PATH="$ROOT/$PROJECT_NAME"

# 🚧 Kreiranje strukture foldera
mkdir -p "$PROJECT_PATH"/{src/utils,docs,assets,test_files,.vscode}

# 📄 Glavni Python fajl sa uvodnim komentarom
cat > "$PROJECT_PATH/src/main.py" <<EOF
\"\"\"
main.py – Entry point of the $PROJECT_NAME project.

📌 Description:
_This script performs the main automation task for the project._

🧠 Notes:
- Uses pathlib for paths
- Uses logging via logger.py
- Interacts with folders via utils/interactive_folder_browser.py
\"\"\"

def main():
    print("🚀 Running $PROJECT_NAME")

if __name__ == "__main__":
    main()
EOF

# 📄 Logger modul
cat > "$PROJECT_PATH/src/logger.py" <<EOF
\"\"\"
logger.py – Logger configuration for $PROJECT_NAME

This module defines and returns a configured logger instance.
\"\"\"

import logging
from pathlib import Path
from datetime import datetime

def setup_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    logger = logging.getLogger("file_organizer")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
EOF

# 📄 Interaktivni selektor foldera (prazan template)
cat > "$PROJECT_PATH/src/utils/interactive_folder_browser.py" <<EOF
\"\"\"
interactive_folder_browser.py – Utility for selecting folders interactively.
\"\"\"

# 📌 Add implementation here
EOF

# 📘 README.md (root)
cat > "$PROJECT_PATH/README.md" <<EOF
# $PROJECT_NAME

## 🧾 Projekat | _Project_

📁 _Automatski generisan mini-projekat sa standardnom strukturom._

---

## 📂 Folder Structure

\`\`\`
$PROJECT_NAME/
├── src/
│   ├── main.py
│   ├── logger.py
│   └── utils/
│       └── interactive_folder_browser.py
├── docs/
│   ├── README.md
│   ├── snippets.md
│   ├── cheatsheet.md
│   └── line_by_line.md
├── assets/
├── test_files/
└── .vscode/
\`\`\`
EOF

# 📄 Dokumentacija u docs/
for file in README.md snippets.md cheatsheet.md line_by_line.md; do
  echo "# ${file/.md/} – $PROJECT_NAME" > "$PROJECT_PATH/docs/$file"
done

echo "✅ Projekat $PROJECT_NAME uspešno generisan."

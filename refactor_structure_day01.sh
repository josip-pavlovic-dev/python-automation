#!/bin/bash

echo "🔁 Starting reorganization of day01_file_organizer..."

cd day01_file_organizer || { echo "❌ Folder not found"; exit 1; }

# Kreiranje foldera ako ne postoje
mkdir -p src/utils tests docs bonus assets toDo

# Premeštanje poznatih skripti
mv main.py src/main.py 2>/dev/null
mv logger.py src/logger.py 2>/dev/null
mv interactive_folder_browser.py src/utils/interactive_folder_browser.py 2>/dev/null

# Test fajlovi
mv ../../tests/test_day01_file_organizer/test_main.py tests/test_main.py 2>/dev/null
mv ../../tests/test_day01_file_organizer/test_logger.py tests/test_logger.py 2>/dev/null

# Dokumentacija
mv docs_readme.md docs/README.md 2>/dev/null
mv cheatsheet.md docs/cheatsheet.md 2>/dev/null
mv snippets.md docs/snippets.md 2>/dev/null
mv line_by_line.md docs/line_by_line.md 2>/dev/null

# Interna dokumentacija
mv amateur_notes.md bonus/amateur_notes.md 2>/dev/null

# Glavni README
mv readme_root.md README.md 2>/dev/null

# Assets
mv *.png assets/ 2>/dev/null

# Fajlovi koji ne pripadaju nijednoj kategoriji
for file in *; do
    if [[ -f "$file" && "$file" != "reorganize_day01.sh" ]]; then
        echo "ℹ️ Premestam $file u toDo/"
        mv "$file" toDo/
    fi
done

echo "✅ Reorganizacija završena!"

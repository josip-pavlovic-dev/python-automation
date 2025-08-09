#!/bin/bash
# ---------------------------------------------------
# Script: move_to_legacy.sh
# Purpose: Move old mini-projects into legacy/ folder
# Author: Josip Pavlović
# Date: 2025-08-09
# ---------------------------------------------------

# Create legacy folder if it doesn't exist
mkdir -p legacy

# List of project folders to move
# Dodaj ovde nazive foldera koje želiš prebaciti
PROJECTS=(
    "day02_file_info"
    "day03_file_management"
    "day04_datetime"
    "day05_os_explorer"
    "exercises/day01_basic_io"
    "exercises/day02_path_ops"
    "exercises/day03_dir_walk"
    "exercises/day04_file_filtering"
    "exercises/day05_timestamps_log"
    # Dodaj dalje po potrebi...
)

# Move each project into legacy/
for project in "${PROJECTS[@]}"; do
    if [ -d "$project" ]; then
        mv "$project" legacy/
        echo "Moved $project to legacy/"
    else
        echo "⚠️ Skipped: $project not found"
    fi
done

# Create README.md inside legacy folder (if doesn't exist)
if [ ! -f legacy/README.md ]; then
    cat <<EOF > legacy/README.md
# Legacy Projects

Ovi projekti su premješteni iz glavnog repozitorijuma.
- Period: pre 10.08.2025
- Razlog: prelazak na novi šablon i radni tok
- Status: arhivirani, bez daljih izmena
EOF
fi

echo "✅ Svi projekti su premešteni u legacy/"

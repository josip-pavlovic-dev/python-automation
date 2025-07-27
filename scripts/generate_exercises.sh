#!/bin/bash

# Postavi root putanju projekta
cd /c/Users/JoleDev/dev-learning/python-automation || exit

# Deklaracija nizova
declare -a days=(
  "day01_basic_io"
  "day02_path_ops"
  "day03_dir_walk"
  "day04_file_filtering"
  "day05_timestamps_log"
)

declare -a titles=(
  "Basic I/O – Čitanje i pisanje fajlova"
  "Path Operations – Manipulacija putanjama"
  "Directory Walk – Rekurzivno pretraživanje"
  "File Filtering – Veličine i ekstenzije"
  "Timestamps & Log – Rad sa vremenima"
)

# Kreiranje vežbi
for i in "${!days[@]}"; do
  day=${days[$i]}
  title=${titles[$i]}

  # Kreiranje foldera
  mkdir -p exercises/$day/{docs,assets,.vscode}

  # Kreiranje fajlova ako ne postoje
  [ ! -f exercises/$day/main.py ] && cat > exercises/$day/main.py <<EOF
\"\"\"
${day} – ${title}

Zadatak:
Ovde ide kratko objašnjenje šta skripta treba da uradi.
\"\"\"

def main():
    print("🧪 Vežba: ${title}")

if __name__ == "__main__":
    main()
EOF

  [ ! -f exercises/$day/README.md ] && cat > exercises/$day/README.md <<EOF
# ${day^^}

## 📝 Задатак (srpski)

${title}

📌 Опис:
> Овде иде опис задатка на српском.

## 📝 Task (English)

${title}

📌 Description:
> Here goes the task description in English.

---

## 🗂 Folder Structure

\`\`\`
$day/
├── main.py
├── README.md
├── snippets.md
├── docs/
├── assets/
└── .vscode/
\`\`\`

## 🚀 Quick Start

\`\`\`bash
python main.py
\`\`\`

EOF

  [ ! -f exercises/$day/snippets.md ] && echo -e "# Snippeti – ${day}\n\nOvde ćeš ubacivati korišćene snippete tokom rada." > exercises/$day/snippets.md

  # Samo za dan 1 – input.txt primer
  if [ "$day" = "day01_basic_io" ] && [ ! -f exercises/$day/input.txt ]; then
    echo "Ovo je test fajl za vežbu čitanja." > exercises/$day/input.txt
  fi
done

echo "✅ Vežbe su uspešno generisane."

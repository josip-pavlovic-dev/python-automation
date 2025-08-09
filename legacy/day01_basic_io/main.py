"""
day01_basic_io – Basic I/O with optional interactive mode and absolute paths

Pokretanje:
1. Skripta se moze pokrenuti iz bilo kog radnog foldera ali fajlovi input.txt i output.txt moraju biti u istom folderu kao i skripta. 
2. Ako se skripta pokrene bez argumenata (python main.py) → čita input.txt i kreira output.txt.
3. Ako se pokrene sa argumentom --interactive (python main.py --interactive) → korisnik unosi tekst liniju po liniju.
"""

import sys
from pathlib import Path

# 📌 Baza foldera u kom se nalazi ova skripta:
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"

def process_file_input():
    """Reads input.txt line by line and writes numbered lines to output.txt"""
    if not INPUT_FILE.exists():
        print(f"❌ input.txt not found at: {INPUT_FILE}")
        return

    with INPUT_FILE.open("r", encoding="utf-8") as input_file, \
         OUTPUT_FILE.open("w", encoding="utf-8") as output_file:

        for index, line in enumerate(input_file, start=1):
            print(line.strip())  # terminal
            output_file.write(f"{index}: {line}")

    print(f"\n✅ File processed successfully and written to {OUTPUT_FILE.name}")

def process_user_input():
    """Prompts the user for multi-line input and writes numbered lines to output.txt"""
    print("🖊️  Enter text (press ENTER on an empty line to finish):")

    lines: list[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    with OUTPUT_FILE.open("w", encoding="utf-8") as output_file:
        for index, line in enumerate(lines, start=1):
            output_file.write(f"{index}: {line}\n")

    print(f"\n✅ Input captured and written to {OUTPUT_FILE.name}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        process_user_input()
    else:
        process_file_input()


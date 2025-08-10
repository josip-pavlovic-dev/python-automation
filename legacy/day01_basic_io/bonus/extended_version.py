"""
day01_basic_io – Basic I/O with optional interactive mode

Kako se pokreće:
1. Skripta se mora pokrenuti u terminalu iz foldera gde se nalaze fajlovi input.txt i output.txt.
2. Ako se skripta pokrene bez argumenata (python extended_main.py) → čita input.txt i kreira output.txt.
3. Ako se pokrene sa argumentom --interactive (python extended_main.py --interactive) → korisnik unosi tekst liniju po liniju, i sve se upisuje u output.txt sa rednim brojevima.
"""

import sys


def process_file_input():
    """Reads input.txt line by line and writes numbered lines to output.txt"""
    """Čita input.txt liniju po liniju i upisuje u output.txt sa rednim brojevima"""
    try:
        with open("input.txt", "r", encoding="utf-8") as input_file, open(
            "output.txt", "w", encoding="utf-8"
        ) as output_file:

            for index, line in enumerate(input_file, start=1):
                print(line.strip())  # print to terminal
                output_file.write(f"{index}: {line}")

        print("\n✅ File processed successfully and written to output.txt")

    except FileNotFoundError:
        print(
            "❌ input.txt not found. Please make sure it exists in the current directory."
        )


def process_user_input() -> None:
    """Prompts the user for multi-line input and writes numbered lines to output.txt"""
    print("🖊️  Enter text (press ENTER on an empty line to finish):")

    lines: list[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    with open("output.txt", "w", encoding="utf-8") as output_file:
        for index, line in enumerate(lines, start=1):
            output_file.write(f"{index}: {line}\n")

    print("\n✅ Input captured and written to output.txt")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        process_user_input()
    else:
        process_file_input()

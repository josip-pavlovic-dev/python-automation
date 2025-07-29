from pathlib import Path

def pathlib_read_write_demo() -> None:
    test_file = Path(__file__).resolve().parent / "sample.txt"

    print(f"📝 Writing to {test_file}")
    test_file.write_text("Hello from pathlib!", encoding="utf-8")

    print(f"📖 Reading content: {test_file.read_text(encoding='utf-8')}")

if __name__ == "__main__":
    pathlib_read_write_demo()

# This code demonstrates how to read and write files using pathlib.
# Ovaj kod demonstrira kako čitati i pisati datoteke koristeći pathlib.
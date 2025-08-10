from pathlib import Path


def pathlib_basics_demo() -> None:
    base_dir = Path(__file__).resolve().parent
    print(f"📂 Base directory: {base_dir}")

    test_file = base_dir / "test.txt"
    print(f"🔗 Full path: {test_file}")

    if test_file.exists():
        print("✅ test.txt exists")
    else:
        print("❌ test.txt does not exist")


if __name__ == "__main__":
    pathlib_basics_demo()

# This code demonstrates basic operations with pathlib.
# Ovaj kod demonstrira osnovne operacije sa pathlib.

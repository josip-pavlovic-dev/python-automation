"""
🧪 day05_os_explorer – Main Script
Author: Josip Pavlović

This script demonstrates key features of the `os` module through modular file and directory operations.
"""

from trening import (
    create_a_new_file,
    create_new_directory,
    delete_directory,
    delete_file,
    get_current_working_directory,
    list_directory_contents,
    rename_directory,
)


def main():
    print("📁 OS Module – Basic File Operations\n")

    # 1. Get current working directory
    print(f"📌 Current working dir: {get_current_working_directory()}")

    # 2. List contents
    print(f"📌 Contents:\n{list_directory_contents()}")

    # 3. Create directory and file (for testing)
    create_new_directory("test_dir")
    create_a_new_file("test_dir/example.txt")

    # 4. Rename directory
    rename_directory("test_dir", "renamed_dir")

    # 5. Delete test file
    delete_file("renamed_dir/example.txt")

    # 6. Delete directory
    delete_directory("renamed_dir")

if __name__ == "__main__":
    main()

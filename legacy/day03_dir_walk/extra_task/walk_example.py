import os


def walk_directory(start_path):
    for foldername, subfolders, filenames in os.walk(start_path):
        print(f"📁 Folder: {foldername}")
        for subfolder in subfolders:
            print(f"  📂 Subfolder: {subfolder}")
        for filename in filenames:
            print(f"  📄 File: {filename}")
        print("-" * 40)


if __name__ == "__main__":
    # Change this to any folder you want to test
    path_to_walk = os.getcwd()
    walk_directory(path_to_walk)

"""
🧪 snippets_os_demo.py – Demo of basic os module functions
Author: Josip Pavlović
"""

import os

# Introduction to testing os module functions
# Uvod u testiranje osnovnih funkcija modula os
print("🧪 Testing os module basic functions")

# 1. Get current working directory
# 1. Dobavi trenutni radni direktorijum
print("\n📌 os.getcwd():")
print(os.getcwd())

# 2. List all files and folders in current directory
# 2. Prikaži sve fajlove i foldere u trenutnom direktorijumu
print("\n📌 os.listdir():")
print(os.listdir())

# 3. Create a new directory if it doesn't exist
# 3. Kreiraj novi direktorijum ako već ne postoji
print("\n📌 os.mkdir('test_dir'):")
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
    print("✅ test_dir created.")
else:
    print("⚠️ test_dir already exists.")

# 4. Rename the created directory
# 4. Preimenuj kreirani direktorijum
print("\n📌 os.rename('test_dir', 'renamed_dir'):")
if os.path.exists("test_dir"):
    os.rename("test_dir", "renamed_dir")
    print("✅ Directory renamed.")
else:
    print("⚠️ test_dir not found.")

# 5. Check if a path is a directory or a file
# 5. Proveri da li je putanja folder ili fajl
print("\n📌 os.path.isdir('renamed_dir'):")
print(os.path.isdir("renamed_dir"))

print("\n📌 os.path.isfile('snippets_os_demo.py'):")
print(os.path.isfile("snippets_os_demo.py"))

# 6. Print absolute path of this script
# 6. Prikaži apsolutnu putanju do ove skripte
print("\n📌 os.path.abspath(__file__):")
print(os.path.abspath(__file__))

# 7. Split path into folder and filename
# 7. Razdvoj putanju na folder i ime fajla
print("\n📌 os.path.split():")
print(os.path.split(os.path.abspath(__file__)))

# 8. Join multiple path parts into a single path
# 8. Spoji više delova putanje u jednu celinu
print("\n📌 os.path.join():")
print(os.path.join("folder", "subfolder", "file.txt"))

# 9. Show PATH environment variable
# 9. Prikaži PATH promenljivu okruženja
print("\n📌 os.environ['PATH']:")
print(os.environ["PATH"])

# 10. Get size of the current script file
# 10. Prikaži veličinu trenutne skripte u bajtovima
print("\n📌 os.path.getsize():")
print(os.path.getsize(__file__), "bytes")

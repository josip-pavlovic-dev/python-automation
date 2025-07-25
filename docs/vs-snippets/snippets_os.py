import os

print("🧪 Testing os module basic functions")

# 1. Get current working directory
print("\n📌 os.getcwd():")
print(os.getcwd())

# 2. List files in current directory
print("\n📌 os.listdir():")
print(os.listdir())

# 3. Create a new directory (test_dir)
print("\n📌 os.mkdir('test_dir'):")
if not os.path.exists('test_dir'):
    os.mkdir('test_dir')
    print("✅ test_dir created.")
else:
    print("⚠️ test_dir already exists.")

# 4. Rename directory
print("\n📌 os.rename('test_dir', 'renamed_dir'):")
if os.path.exists('test_dir'):
    os.rename('test_dir', 'renamed_dir')
    print("✅ Directory renamed.")
else:
    print("⚠️ test_dir not found.")

# 5. Check if path is file or directory
print("\n📌 os.path.isdir('renamed_dir'):")
print(os.path.isdir('renamed_dir'))

print("\n📌 os.path.isfile('snippets_os.py'):")
print(os.path.isfile('snippets_os.py'))

# 6. Absolute path
print("\n📌 os.path.abspath(__file__):")
print(os.path.abspath(__file__))

# 7. Path split
print("\n📌 os.path.split():")
print(os.path.split(os.path.abspath(__file__)))

# 8. Join path
print("\n📌 os.path.join():")
print(os.path.join('folder', 'subfolder', 'file.txt'))

# 9. Environment variables
print("\n📌 os.environ['PATH']:")
print(os.environ['PATH'])

# 10. Get size of file
print("\n📌 os.path.getsize():")
print(os.path.getsize(__file__), "bytes")

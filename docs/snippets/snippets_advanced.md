# 📚 Most Used Python Snippets | Najčešće korišćeni Python snippeti

> A cheat sheet of essential Python snippets, grouped by topic.  
> Lista najčešće korišćenih Python snippeta, grupisana po temama.

---

## 🔧 os module – File and Path Handling

```python
import os

# Get current working directory
cwd = os.getcwd()

# Create a new directory (if it doesn't exist)
folder_path = "output"
os.makedirs(folder_path, exist_ok=True)

# Join paths correctly
full_path = os.path.join(cwd, "data", "file.txt")

# List files in a folder
files = os.listdir(folder_path)
```

---

## 📂 File Operations – Reading and Writing

```python
# Writing to a text file
with open("example.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
```

---

## 🧪 Error Handling

```python
try:
    risky_operation()
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 🪵 Logger (custom)

```python
from logger import log

log("Action started", level="info")
log("File not found", level="warning")
log("Critical error", level="error")
```

---

## 📄 JSON Read/Write

```python
import json

# Write JSON to file
with open("data.json", "w") as f:
    json.dump({"name": "Jole", "age": 10}, f, indent=4)

# Read JSON from file
with open("data.json", "r") as f:
    data = json.load(f)
```

---

## ⌛ Datetime Snippets

```python
from datetime import datetime, timedelta

# Get current timestamp
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Subtract days
seven_days_ago = now - timedelta(days=7)
```

---

## 🧠 Script Entry Point and Metadata

```python
# Only runs when script is executed directly
if __name__ == "__main__":
    print("Script executed directly.")

# Print current file path
print(__file__)
```

---

## 🧹 Clean-up with shutil and glob

```python
import shutil
import glob

# Remove a directory and its contents
shutil.rmtree("test_folder")

# Get all .txt files
txt_files = glob.glob("*.txt")
```

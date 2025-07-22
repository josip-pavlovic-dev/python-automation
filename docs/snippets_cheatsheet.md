# ✂️ Python Snippets Cheatsheet

> Most commonly used Python snippets for automation and scripting tasks.  
> Use this file as a quick reference for writing clean and efficient Python code.

---

## 📁 File Handling

### 🔹 Open file safely
```python
with open("file.txt", "r") as f:
    data = f.read()
```

### 🔹 Write text to file
```python
with open("file.txt", "w") as f:
    f.write("Some content")
```

### 🔹 Append to a log file
```python
with open("log.txt", "a") as f:
    f.write("Log entry\n")
```

---

## 🧮 Path and OS Utilities

### 🔹 Join paths correctly
```python
import os
path = os.path.join("folder", "file.txt")
```

### 🔹 Create directory if it doesn’t exist
```python
os.makedirs("folder", exist_ok=True)
```

### 🔹 List files in a directory
```python
for file in os.listdir("folder"):
    print(file)
```

---

## ⏱️ Datetime

### 🔹 Get formatted current timestamp
```python
from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
```

---

## 🪵 Logging

### 🔹 Basic logger function
```python
from datetime import datetime

def log(msg, level="info"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{ts}] [{level.upper()}] {msg}\n")
```

---

## 🧪 Error Handling

### 🔹 try/except block
```python
try:
    # some code
except Exception as e:
    print(f"Error: {e}")
```

---

## 🧠 Script Entrypoint

### 🔹 Run as script
```python
if __name__ == "__main__":
    main()
```

# 📁 File Handling Snippets – Day 01

### ✅ Kreiranje foldera ako ne postoji
```python
import os

target_folder = "organized"
os.makedirs(target_folder, exist_ok=True)
```

### ✅ Premestanje fajla u folder
```python
import shutil
shutil.move("document.txt", "organized/document.txt")
```

### ✅ Provera ekstenzije fajla pre sortiranja
```python
ext = os.path.splitext("file.txt")[1]
if ext.lower() in [".txt", ".jpg", ".pdf"]:
    # move file or handle
```

### ✅ Dinamičko kreiranje putanje
```python
path = os.path.join("base", "subfolder", "file.txt")
```

### ✅ Osnovni logger
```python
from datetime import datetime

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{ts}] {msg}\n")
```
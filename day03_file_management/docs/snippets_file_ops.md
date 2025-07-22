# 🧹 File Operations Snippets – Day 03

### ✅ Brisanje fajlova starijih od X dana
```python
import os, time

cutoff = time.time() - (7 * 86400)  # 7 dana
for file in os.listdir("data"):
    full_path = os.path.join("data", file)
    if os.path.isfile(full_path) and os.path.getmtime(full_path) < cutoff:
        os.remove(full_path)
```

### ✅ Provera da li je folder prazan
```python
if not os.listdir("folder_name"):
    print("Folder is empty")
```

### ✅ Dobavljanje samo .txt fajlova
```python
import glob
txt_files = glob.glob("*.txt")
```

### ✅ Logger primer
```python
from datetime import datetime

def log(msg, level="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{ts}] [{level}] {msg}\n")
```
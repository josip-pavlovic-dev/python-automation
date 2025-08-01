# 📄 File Info Snippets – Day 02

### ✅ Dobijanje informacija o fajlu
```python
import os
from datetime import datetime

full_path = os.path.join("folder", "file.txt")

if os.path.exists(full_path):
    size = os.path.getsize(full_path)
    created = os.path.getctime(full_path)
    modified = os.path.getmtime(full_path)

    print(f"Size: {size} bytes")
    print("Created:", datetime.fromtimestamp(created))
    print("Modified:", datetime.fromtimestamp(modified))
```
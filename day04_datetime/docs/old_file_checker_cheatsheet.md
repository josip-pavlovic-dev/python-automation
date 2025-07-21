# 🧹 old_file_checker.py Cheatsheet

🇬🇧 **Purpose:** Checks for files older than a given number of days and logs their paths.  
🇷🇸 **Svrha:** Pronalazi fajlove starije od zadatog broja dana i beleži njihove putanje.

📌 **Example Screenshot:** Add a screenshot showing terminal output listing old files.

```python
import os
import time
from pathlib import Path

folder = Path(".")
days = 7
time_threshold = time.time() - (days * 86400)

for file in folder.rglob("*"):
    if file.is_file() and file.stat().st_mtime < time_threshold:
        print(f"Old file: {file}")
```

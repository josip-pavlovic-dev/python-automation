# 🗂️ dated_folder_creator.py Cheatsheet

🇬🇧 **Purpose:** Creates a new folder named with the current date (e.g. `2025-07-21`).  
🇷🇸 **Svrha:** Kreira novi folder sa imenom koje predstavlja današnji datum (npr. `2025-07-21`).

📌 **Example Screenshot:** Add a screenshot of the created folder in your project directory.

```python
from datetime import datetime
from pathlib import Path

folder_name = datetime.now().strftime("%Y-%m-%d")
Path(folder_name).mkdir(exist_ok=True)
```

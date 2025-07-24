# 🕓 timestamp_generator.py Cheatsheet

#### 🇬🇧 **Purpose:** Generates a unique timestamp string for filenames or logging.

#### 🇷🇸 **Svrha:** Generiše jedinstveni string sa vremenskom oznakom za imena fajlova ili logove.

#### 📌 **Example Screenshot:** Add a screenshot showing a filename or printout with a timestamp.

```python
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(f"Generated timestamp: {timestamp}")
```

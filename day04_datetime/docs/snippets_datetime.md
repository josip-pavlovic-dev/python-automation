# ⏱️ Datetime Snippets – Day 04

### ✅ Generisanje timestamp-a
```python
from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
```

### ✅ Generisanje imena fajla sa timestamp-om
```python
file_name = f"log_{timestamp}.txt"
```

### ✅ Kreiranje foldera sa datumom
```python
import os
folder_name = datetime.now().strftime("%Y-%m-%d")
os.makedirs(folder_name, exist_ok=True)
```

### ✅ Formatiran ispis
```python
now = datetime.now()
print(now.strftime("%A, %d %B %Y %H:%M"))
```
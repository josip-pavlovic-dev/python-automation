# 🧩 Snippets | _Snippeti_

```python
from pathlib import Path

# Get the absolute path of the current script
script_path = Path(__file__).resolve()
print(f"Script path: {script_path}")
```

```python
# Get the directory that contains the script
script_dir = script_path.parent
print(f"Script directory: {script_dir}")
```

```python
# Create a path to the input.txt file located in the same directory as the script
input_file = script_dir / "input.txt"
print(f"Input file path: {input_file}")
```

```python
# Read the content of the input file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.readlines()
    print(content)
```

```python
# Construct an output file path
output_file = script_dir / "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    for idx, line in enumerate(content, 1):
        f.write(f"{idx}: {line}")
```

```python
import os

# Print absolute path of the script
print("Absolute path:", os.path.abspath(__file__))

# Get base directory (folder where the script resides)
base_dir = os.path.dirname(os.path.abspath(__file__))
print("Base directory:", base_dir)

# Join with a hypothetical file
file_path = os.path.join(base_dir, "data", "file.txt")
print("Joined path:", file_path)

# Check if path exists
print("Exists:", os.path.exists(file_path))
```

## 📌 Explanation: | _Objašnjenje:_

- Uses `__file__` to determine the script’s location. | _Koristi `__file__` da bi se utvrdila lokacija skripte._
- Combines `.resolve()` to convert to an absolute path. | _Koristi `.resolve()` da pretvori u apsolutnu putanju._
- Accesses `parent` to find the folder containing the script. | _Pristupa `parent` da pronađe folder koji sadrži skriptu._
- Uses `/` operator with `Path` for cross-platform joining. | _Koristi `/` operator sa `Path` klasom za kompatibilno spajanje putanja._
- Encodes and decodes in UTF-8 for consistency. | _Koristi UTF-8 kodiranje radi konzistentnosti._
- Uses `os.path.abspath(__file__)` to get the absolute script path. | _Koristi `os.path.abspath(__file__)` da dobije apsolutnu putanju skripte._
- Uses `os.path.dirname()` to determine the base directory. | _Koristi `os.path.dirname()` da pronađe osnovni direktorijum._
- Combines `os.path.join()` to create full file paths. | _Kombinuje `os.path.join()` da napravi kompletne putanje do fajlova._
- Validates file existence using `os.path.exists()`. | _Proverava postojanje fajla uz pomoć `os.path.exists()`._

## 👨‍💻 Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-Josip_Pavlović-blue?logo=github)](https://github.com/Jole85)
[![Learning Path](https://img.shields.io/badge/Focus-Python_Automation-success)](https://github.com/Jole85/python-automation)

**Josip Pavlović — aspiring Python developer from Novi Sad**
[LinkedIn](https://www.linkedin.com/in/josip-p-151951338/)

---

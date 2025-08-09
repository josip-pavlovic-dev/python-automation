# ✂️ Code Snippets | _Isečci koda_

## 📌 Basic Path Setup | _Osnovno podešavanje putanje_

```python
from pathlib import Path
from datetime import datetime

base_dir = Path(__file__).resolve().parent
output_file = base_dir / "file_filtering_output.txt"
```

Sets the base directory to the folder where the script is located. | _Postavlja osnovni direktorijum na folder u kome se skripta nalazi._

## 📌 File Info Function | _Funkcija za informacije o fajlu_

```python
def file_info(file_path: Path) -> str:
    size = file_path.stat().st_size
    modified_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    return f"{file_path.name} | {size} B | Last modified: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}"
```

Returns file name, size, and last modification date. | _Vraća naziv fajla, veličinu i datum poslednje izmene._

---

## 📌 Filtering Files | _Filtriranje fajlova_

```python
all_files = list(base_dir.rglob("*.*"))

filtered_files = [
    f for f in all_files
    if f.stat().st_size >= 1000
    and (datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)).days <= 7
]
```

Filters files larger than 1KB and modified in the last 7 days. | _Filtrira fajlove veće od 1KB i izmenjene u poslednjih 7 dana._

---

## 📌 Writing Results | _Upis rezultata_

```python
with open(output_file, "w", encoding="utf-8") as out:
    out.write("=== 📄 Python files (.py) ===\n")
    for f in py_files:
        out.write(file_info(f) + "\n")
```

Writes filtered file information into a text file. | _Upisuje informacije o filtriranim fajlovima u tekstualni fajl._

---

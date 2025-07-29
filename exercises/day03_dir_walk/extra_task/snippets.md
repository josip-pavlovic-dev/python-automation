# 🔧 Snippets | _Iscečci koda_

### Walking through directories with `os.walk()` | _Korišćenje os.walk() za obilazak direktorijuma_

```python
for foldername, subfolders, filenames in os.walk(start_path):
    print(foldername, subfolders, filenames)
```

- Prints each directory, subdirectory, and file inside the path | _Štampa svaki direktorijum, poddirektorijum i fajl unutar putanje._

---

## 🔧 Pathlib Basics | _Osnovne operacije sa pathlib_

### Create and join paths | _Kreiranje i spajanje putanja_

```python
from pathlib import Path

base = Path(__file__).resolve().parent
data_file = base / "data" / "input.txt"
print(data_file)
```

### 🔧 Pathlib Read/Write | _Čitanje i pisanje fajlova_

```python
from pathlib import Path

p = Path("notes.txt")
p.write_text("Hello World!", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

### 🔧 Pathlib Scan | _Pretraga fajlova_

```python
from pathlib import Path

base = Path(__file__).resolve().parent
for f in base.rglob("*.py"):
    print(f, f.stat().st_mtime)
```

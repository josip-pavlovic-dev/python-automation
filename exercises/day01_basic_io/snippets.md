# ✂️ Code Snippets – day01_basic_io

## 🔹 Define absolute file paths | _Definiši apsolutne putanje fajlova_

```python
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"
```

Defines input/output paths relative to script file | _Definiše putanje ulaznog i izlaznog fajla u odnosu na fajl skripte_

---

## 🔹 Read file and write output with line numbers | _Čitanje fajla i upis sa rednim brojevima_

```python
with INPUT_FILE.open("r", encoding="utf-8") as input_file, \
     OUTPUT_FILE.open("w", encoding="utf-8") as output_file:

    for index, line in enumerate(input_file, start=1):
        print(line.strip())  # display
        output_file.write(f"{index}: {line}")
```

Reads all lines and writes them to output with numbering | _Čita sve linije i upisuje ih sa numeracijom u izlazni fajl_

---

## 🔹 Capture user input interactively | _Unos korisničkog teksta interaktivno_

```python
lines: list[str] = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
```

Captures input until empty line is entered | _Hvata unos dok se ne unese prazna linija_

---

## 🔹 Save user input to file with line numbers | _Snimi korisnički unos sa rednim brojevima_

```python
with OUTPUT_FILE.open("w", encoding="utf-8") as output_file:
    for index, line in enumerate(lines, start=1):
        output_file.write(f"{index}: {line}\n")
```

Writes captured input to output file with line numbers | _Upisuje unesene linije u fajl uz redne brojeve_

---

## 🔹 CLI mode selection | _Izbor režima pomoću komandne linije_

```python
if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
    process_user_input()
else:
    process_file_input()
```

Chooses execution mode based on CLI argument | _Bira režim izvršavanja na osnovu CLI argumenta_

---

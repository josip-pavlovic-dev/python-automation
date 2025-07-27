# ✂️ Code Snippets

## 🔹 Define file paths with pathlib | _Definisanje putanja fajlova pomoću pathlib-a_

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"
```

Use pathlib to create absolute paths that work across OS | _Korišćenje pathlib-a za kreiranje apsolutnih putanja koje rade na svim operativnim sistemima_

---

## 🔹 Read file and write to output with line numbers | _Čitanje fajla i pisanje u izlazni fajl sa rednim brojevima_

```python
with INPUT_FILE.open("r", encoding="utf-8") as input_file,      OUTPUT_FILE.open("w", encoding="utf-8") as output_file:
    for index, line in enumerate(input_file, start=1):
        output_file.write(f"{index}: {line}")
```

Using context manager and enumerate for numbered output | _Korišćenje context manager-a i enumerate za numerisani izlaz_

---

## 🔹 Capture user input | _Hvatanje korisničkog unosa_

```python
lines: list[str] = []
while True:
    line = input("Enter text (or press ENTER to finish): ")
    if line.strip() == "":
        break
    lines.append(line)
```

Loop until empty line is entered | _Petlja dok se ne unese prazna linija_

---

## 🔹 Write user input to file | _Pisanje unosa u fajl_

```python
with OUTPUT_FILE.open("w", encoding="utf-8") as output_file:
    for index, line in enumerate(lines, start=1):
        output_file.write(f"{index}: {line}\n")
```

Save input to output.txt with line numbers | _Sačuvaj unos u output.txt sa rednim brojevima_

---

## 🔹 CLI mode switch | _Prekidač za režime preko komandne linije_

```python
if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
    process_user_input()
else:
    process_file_input()
```

Run in interactive mode if flag is passed | _Pokreni interaktivni režim ako je prosleđen argument_

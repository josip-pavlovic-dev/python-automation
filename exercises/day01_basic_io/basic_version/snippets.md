# 📌 Snippets – main.py

## 📥 Reading a file line by line | _Čitanje fajla red po red_

```python
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

## 📥🔢 Writing lines with line numbers | _Pisanje redova sa rednim brojevima_

```python
with open("input.txt", "r", encoding="utf-8") as input_file, \
     open("output.txt", "w", encoding="utf-8") as output_file:

    for index, line in enumerate(input_file, start=1):
        output_file.write(f"{index}: {line}")
```

## ✅ File existence check (optional) | _Provera da li fajl postoji (opciono)_

```python
import os

if os.path.exists("input.txt"):
    print("Fajl postoji, nastavljamo.")
else:
    print("Fajl nije pronađen.")
```

---

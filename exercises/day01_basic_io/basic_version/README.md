# 📘 basic_version – Basic I/O

![Status](https://img.shields.io/badge/status-done-brightgreen)
![Level](https://img.shields.io/badge/level-beginner-blue)
![Category](https://img.shields.io/badge/topic-file--io-lightgrey)
![Python](https://img.shields.io/badge/python-3.11+-blueviolet)

---

## 📝 Task (English)

**Basic I/O – Reading and writing text files**

📌 Description:  
This script performs the following:

1. Reads the file `input.txt` line by line.
2. Prints each line to the terminal.
3. Creates `output.txt` with each line numbered using `enumerate()`.

> Example:

```

1: Hello World
2: This is a test
3: End of file

```

📌 Important:

- Must be executed from the same directory where `basic_main.py` and `input.txt` reside.
- If `input.txt` is missing, the script will throw a `FileNotFoundError`.

---

## 📝 Zadatak (Srpski)

**Basic I/O – Čitanje i pisanje tekstualnih fajlova**

📌 Opis:  
Ova skripta:

1. Čita `input.txt` fajl red po red.
2. Ispisuje sadržaj svakog reda u terminal.
3. Kreira `output.txt` fajl gde svaka linija ima svoj redni broj.

> Primer:

```

1: Zdravo svete
2: Ovo je test
3: Kraj fajla

```

📌 Napomena:

- Skripta mora biti pokrenuta iz foldera u kojem se nalaze `basic_main.py` i `input.txt`.
- Ako `input.txt` ne postoji, dolazi do greške.

## 📂 File Structure

```
exercises/
└── day01_basic_io/
    └── basic_version/
        ├── main.py # Glavna skripta za zadatak
        ├── input.txt # Ulazni fajl sa tekstom
        ├── output.txt # Izlazni fajl sa numerisanim redovima
        ├── README.md # Dokumentacija zadatka
        ├── snippets.md # Brzi kod snippeti
        └── cheatsheet.md # Objašnjenje koda liniju po liniju
```

## 🚀 Run Instructions

### From terminal:

```bash
python basic_main.py
```

## 🧠 Concepts Used | Korišteni pojmovi

- `with open(...)` → context manager for working with files | context manager za rad sa fajlovima
- `enumerate(..., start=1)` → line numbering | numerisanje linija
- `print(...), write(...)` → print and write content | ispis i upis sadržaja
- `strip()` → removing extra characters (`\n`) | uklanjanje suvišnih karaktera (`\n`)

---

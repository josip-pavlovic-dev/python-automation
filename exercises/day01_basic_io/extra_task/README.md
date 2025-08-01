# 🧪 Extra Task

![Python](https://img.shields.io/badge/Python-3.13.5-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Interactive Mode](https://img.shields.io/badge/Mode-Interactive-orange?style=flat-square)

## 📘 basic_version.py – Basic I/O

---

### 📝 Task (English)

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

- Must be executed from the same directory where `main.py` and `input.txt` reside.
- If `input.txt` is missing, the script will throw a `FileNotFoundError`.

---

### 📝 Zadatak (Srpski)

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

- Skripta mora biti pokrenuta iz foldera u kojem se nalaze `main.py` i `input.txt`.
- Ako `input.txt` ne postoji, dolazi do greške.

---

### 🚀 Run Instructions | _Instrukcije za pokretanje_

```bash
python main.py
```

---

### 🧠 Concepts Used | _Korišćeni pojmovi_

- `with open(...)` → context manager for working with files | _kontekst menadžer za rad sa fajlovima_
- `enumerate(..., start=1)` → line numbering | _numerisanje linija_
- `print(...), write(...)` → print and write content | _ispis i upis sadržaja_
- `strip()` → removing extra characters (`\n`) | _uklanjanje suvišnih karaktera (`\n`)_

---

## 📘 extended_version.py – Basic I/O with optional interactive mode

---

### 🧩 Description | _Opis_

A basic input/output script with two modes of operation: | _Osnovna skripta za unos i ispis sa dva režima rada:_

- 📂 **File mode**: Reads `input.txt` and writes numbered lines to `output.txt`. | _Čita `input.txt` i upisuje redne brojeve u `output.txt`._
- 🖊️ **Interactive mode**: Prompts the user for manual input and stores it line by line. | _Korisnik unosi tekst, koji se zatim numeriše i čuva._

---

### 🧪 Run Instructions | _Uputstvo za pokretanje_

---

#### 📁 From file | _Iz fajla_

```bash
python main.py
```

#### 👤 Interactive mode | _Interaktivni režim_

```bash
python main.py --interactive
```

---

### 🧠 Concepts Used | _Korišćeni pojmovi_

- `open()` for file handling | _`open()` za rad sa fajlovima_
- `try`/`except` for error handling | _`try`/`except` za rukovanje greškama_
- `input()` and `while` loop for user input | _`input()` i petlja `while` za unos korisnika_
- `enumerate()` to number lines | _`enumerate()` za numeraciju redova_
- `sys.argv` for CLI arguments | _`sys.argv` za upravljanje argumentima komandne linije_

---

### 👤 Author | _Autor_

![GitHub](https://img.shields.io/badge/GitHub-Jole85-black)
![Learning](https://img.shields.io/badge/Path-Career%20Transition-informational)

**_Josip Pavlović_** – aspiring Python developer from Novi Sad
🔗 [LinkedIn Profile](https://www.linkedin.com/in/josip-p-151951338)

---

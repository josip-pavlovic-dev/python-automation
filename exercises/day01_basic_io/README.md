# 📘 DAY01_BASIC_IO

![Status](https://img.shields.io/badge/status-completed-brightgreen)
![Level](https://img.shields.io/badge/level-beginner-blue)
![Category](https://img.shields.io/badge/topic-basic--io-lightgrey)
![Python](https://img.shields.io/badge/python-3.11+-blueviolet)

## 📝 Task (English)

**Basic I/O – Reading and writing text files**

📌 Description:  
Write a Python script that performs the following:

1. Reads the file `input.txt` line by line.
2. Prints each line to the terminal.
3. Creates a file `output.txt` with each line prefixed by its line number.

📦 Bonus (interactive):  
Ask the user to input multiple lines. Save them into `output.txt`, with line numbers.

> Example:

```

1: Hello
2: This is a test
3: End of message

```

---

## 📝 Zadatak (Srpski)

**Basic I/O – Čitanje i pisanje tekstualnih fajlova**

📌 Opis:  
Napiši Python skriptu koja:

1. Čita fajl `input.txt` red po red.
2. Ispisuje sadržaj u terminal.
3. Kreira fajl `output.txt` sa rednim brojevima ispred svake linije.

📦 Bonus (interaktivno):  
Korisnik unosi više linija iz terminala. Program ih snima u `output.txt` i numeriše ih.

> Primer:

```

1: Zdravo
2: Ovo je test
3: Kraj poruke

```

---

## 📂 Folder Structure

```

day01\_basic\_io/
├── input.txt
├── output.txt
├── main.py
├── README.md
├── snippets.md
├── docs/
│   └── context_managers_cheatsheet.md
├── assets/
└── .vscode/

```

---

## 🚀 Run Examples

Standard file input:

```bash
python main.py
```

Bonus (user input mode – interactive):

```bash
python main.py --interactive
```

---

## 🧠 Concepts Used

- File I/O
- Context managers (`with`)
- `enumerate()` function
- `f-string` formatting
- Encoding (UTF-8)

---

# 📘 main.py – Basic I/O

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

- Must be executed from the same directory where `main.py` and `input.txt` reside.
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

- Skripta mora biti pokrenuta iz foldera u kojem se nalaze `main.py` i `input.txt`.
- Ako `input.txt` ne postoji, dolazi do greške.

---

## 📂 File Structure | _Struktura fajlova_

```

exercises/
└── day01\_basic\_io/
└── basic\_version/
├── main.py
├── input.txt
├── output.txt
├── README.md
├── snippets.md
└── cheatsheet.md

```

---

## 🚀 Run Instructions | _Instrukcije za pokretanje_

```bash
python main.py
```

---

## 🧠 Concepts Used | _Korišćeni pojmovi_

- `with open(...)` → context manager for working with files | _kontekst menadžer za rad sa fajlovima_
- `enumerate(..., start=1)` → line numbering | _numerisanje linija_
- `print(...), write(...)` → print and write content | _ispis i upis sadržaja_
- `strip()` → removing extra characters (`\n`) | _uklanjanje suvišnih karaktera (`\n`)_

---

### 👤 Author | _Autor_

![GitHub](https://img.shields.io/badge/GitHub-Jole85-black)
![Learning](https://img.shields.io/badge/Path-Career%20Transition-informational)

**_Josip Pavlović_** – aspiring Python developer from Novi Sad
🔗 [LinkedIn Profile](https://www.linkedin.com/in/josip-p-151951338)

---

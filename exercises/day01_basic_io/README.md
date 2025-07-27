# 📘 DAY01*BASIC_IO – Extended Version | \_DAY01_BASIC_IO – Proširena verzija*

![Status](https://img.shields.io/badge/status-completed-brightgreen) | _![Status](https://img.shields.io/badge/status-završeno-brightgreen)_
![Level](https://img.shields.io/badge/level-beginner-blue) | _![Nivo](https://img.shields.io/badge/nivo-početni-blue)_
![Category](https://img.shields.io/badge/topic-basic--io-lightgrey) | _![Kategorija](https://img.shields.io/badge/tema-osnovni--io-lightgrey)_
![Python](https://img.shields.io/badge/python-3.11+-blueviolet) | _![Python](https://img.shields.io/badge/python-3.11+-blueviolet)_

## 📝 Task | _Zadatak_

Create a Python script that supports two modes: | _Napravi Python skriptu koja podržava dva režima:_

1. Read from `input.txt` and write to `output.txt` with line numbers | _Čita iz `input.txt` i piše u `output.txt` sa rednim brojevima_
2. Use interactive mode: user types input manually, which is also saved with line numbers | _Interaktivni režim: korisnik unosi tekst ručno, koji se čuva sa rednim brojevima_

The script uses absolute paths so it can be run from any directory | _Skripta koristi apsolutne putanje, pa može biti pokrenuta iz bilo kog direktorijuma_

### Example Output | _Primer izlaza_

```
1: Hello
2: This is a test
3: End of message
```

| _1: Zdravo_  
| _2: Ovo je test_  
| _3: Kraj poruke_

---

## 📂 File Structure | _Struktura fajlova_

```
day01_basic_io/
├── input.txt
├── output.txt
├── main.py
├── README.md
├── snippets.md
├── cheatsheet.md
├── assets/
├── docs/
└── .vscode/
```

| _Hijerarhijska struktura fajlova u projektu_

---

## 🚀 Run Instructions | _Uputstvo za pokretanje_

### 🔹 Standard mode (read from file) | _Standardni režim (čitanje iz fajla)_

```bash
python main.py
```

### 🔸 Interactive mode (user input) | _Interaktivni režim (unos korisnika)_

```bash
python main.py --interactive
```

---

## 🧠 Concepts Used | _Korišćeni pojmovi_

- `sys.argv` for argument parsing | _`sys.argv` za parsiranje argumenata_
- `pathlib.Path` for file path management | _`pathlib.Path` za rad sa putanjama_
- `enumerate()` for line numbering | _`enumerate()` za numerisanje linija_
- `context manager` using `with` blocks | _kontekst menadžer sa `with` blokovima_
- `f-strings` for formatting strings | _`f-string` za formatiranje teksta_
- `UTF-8` encoding for file I/O | _UTF-8 enkodiranje za čitanje i pisanje fajlova_

---

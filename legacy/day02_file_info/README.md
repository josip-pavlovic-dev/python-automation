# 📂 day02_file_info

[![Status](./assets/day02_status.svg)](./README.md)
[![👤 Developer Profile](../assets/dev_profile_badge.svg)](../docs/developer_profile.md)
[![📘 Career Notes](../assets/career_notes_badge.svg)](../docs/career_notes.md)

**Project type:** Python Automation  
**Date:** 2025-07-14  
**Status:** ✅ Completed

<h3 align="center">🖼️ Preview Images / Pregled slika</h3>

<table align="center">
  <tr>
    <td align="center">
      <img src="assets/day02_file_info-preview-3.png" width="300"/><br/>
      <strong>EN:</strong> Initial folder with files<br/>
      <strong>SR:</strong> Početni folder sa fajlovima
    </td>
    <td align="center">
      <img src="assets/day02_file_info-preview-4.png" width="300"/><br/>
      <strong>EN:</strong> Terminal execution<br/>
      <strong>SR:</strong> Pokretanje skripte u terminalu
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="assets/day02_file_info-preview-2.png" width="300"/><br/>
      <strong>EN:</strong> Extracted file metadata<br/>
      <strong>SR:</strong> Izvučeni metapodaci o fajlovima
    </td>
    <td align="center">
      <img src="assets/day02_file_info-preview-1.png" width="300"/><br/>
      <strong>EN:</strong> Folder content after analysis<br/>
      <strong>SR:</strong> Sadržaj foldera nakon analize
    </td>
  </tr>
</table>

## 🇬🇧: 📌 Description

#### This project analyzes files in a selected folder and logs information about each file, including:

- File name
- Extension
- File size in bytes
- Last modified timestamp

#### It also features:

- Color-coded terminal output using ANSI escape codes
- Log rotation using Python's `RotatingFileHandler`
- Flexible input via `input()`
- Clean error handling and logging using a custom `logger.py` module

#### Goal: Practice Python modules like `os`, `datetime`, `logging`, and improve command-line interaction and logging discipline.

## 🇷🇸:📌 Opis

#### Ovaj projekat analizira fajlove u izabranom folderu i beleži informacije o svakom fajlu, uključujući:

- Ime fajla
- Ekstenziju
- Veličinu u bajtovima
- Datum poslednje izmene

#### Takođe sadrži:

- Boje u terminalu (ANSI escape kodovi)
- Rotaciju log fajla putem `RotatingFileHandler` klase
- Unos foldera putem `input()`
- Robusno logovanje uz sopstveni `logger.py` modul

#### Cilj: Vežbanje rada sa modulima `os`, `datetime`, `logging` i rad u terminalu. Projektom sam dodatno učvrstio rad sa putanjama i logovanjem grešaka.

---

## 🧠 What I Learned | Šta sam naučio

#### 🇬🇧: What I Learned

- How to work with `os.path` and `os.listdir`
- Use of `os.path.getsize` and `os.path.getmtime`
- Parsing file extensions with `os.path.splitext`
- Formatting timestamps using `datetime.fromtimestamp`
- Creating and rotating logs with `RotatingFileHandler`
- Adding terminal colors using ANSI escape codes
- Structuring code into reusable modules (e.g., `logger.py`)
- Accepting user input via `input()` and validating it
- Practicing dynamic folder analysis and command-line interaction

#### 🇷🇸: Šta sam naučio

- Rukovanje fajl sistemom koristeći `os.path` i `os.listdir`
- Dohvatanje veličine fajla (`getsize`) i datuma poslednje izmene (`getmtime`)
- Parsiranje ekstenzije fajla preko `os.path.splitext`
- Formatiranje vremena pomoću `datetime.fromtimestamp`
- Kreiranje i rotacija log fajlova uz `RotatingFileHandler`
- Dodavanje boja u terminal koristeći ANSI escape kodove
- Modularizacija koda – pravljenje sopstvenog `logger.py` modula
- Korišćenje `input()` za unos foldera i validacija unosa
- Analiza sadržaja foldera i logovanje sa modernim CLI pristupom

---

## 🚀 How to Run | Kako pokrenuti

```bash
python main.py
```

#### 🇬🇧: Then enter the name of the folder you want to analyze (e.g., `test_files`)

#### 🇷🇸: Zatim uneti ime foldera koji želite da analizirate (npr., `test_files`)

---

## 📁 Folder Structure | Struktura Projekta

```
day02_file_info/
│
├── main.py
├── logger.py
├── test_files/
│   ├── test1.txt
│   ├── test2.pdf
│   └── ...
├── log.txt
└── README.md
```

## ©️ Author | Autor

#### Josip Pavlović

#### Repository: [python-automation](https://github.com/Jole85/python-automation)

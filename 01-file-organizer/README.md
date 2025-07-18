# 📁 File Organizer Automation | Automatizacija Organizacije Fajlova

[![Status](./assets/day01_status.svg)](./README.md)
[![👤 Developer Profile](../assets/dev_profile_badge.svg)](../docs/developer_profile.md)
[![📘 Career Notes](../assets/career_notes_badge.svg)](../docs/career_notes.md)
## 📌 Description | Opis

#### 🇬🇧: This project automatically organizes files in a selected folder by moving them into subfolders based on file extensions. It simulates a real-life use case where a user downloads or collects various types of files and wants to keep their workspace clean.

#### 🇷🇸: Projekat automatski organizuje fajlove u izabranom folderu tako što ih razvrstava u podfoldere prema tipu ekstenzije. Simulira svakodnevnu situaciju kada korisnik želi da organizuje preuzete fajlove i održi urednost svog sistema.

---

## ⚙️ Features | Funkcionalnosti

#### 🇬🇧: Automatically detects file extensions and creates matching folders

#### 🇷🇸: Automatski detektuje ekstenzije fajlova i kreira odgovarajuće foldere

#### 🇬🇧: Moves files into designated folders based on type (e.g. `.txt`, `.jpg`, `.pdf`)

#### 🇷🇸: Premesta fajlove u pripadajuće foldere na osnovu tipa (npr. `.txt`, `.jpg`, `.pdf`)

#### 🇬🇧: Skips moving files that are already in their correct folder

#### 🇷🇸: Preskače fajlove koji su već u odgovarajućem folderu

#### 🇬🇧: Logs all actions to `log.txt`

#### 🇷🇸: Beleži sve akcije u `log.txt` fajl

---

## 🧠 What I Learned | Šta sam naučio

#### 🇬🇧:
- Working with `os` and `shutil` libraries for file operations
- Creating reusable logging modules
- Using terminal and Git Bash commands
- Modularizing Python code and organizing folders
- Practicing real-world CLI automation

#### 🇷🇸:
- Korišćenje `os` i `shutil` biblioteka za manipulaciju fajlovima
- Kreiranje višekratno upotrebljivih modula za logovanje
- Rad u terminalu i korišćenje Git Bash komandi
- Modularizacija Python koda i organizacija foldera
- Vežbanje automatizacije kroz realne CLI projekte

---

## 📂 Project Structure | Struktura Projekta

```
01-file-organizer/
│
├── assets/                      #Pictures Folder | Folder sa slikama
│   ├── 01-file-organizer-preview-1.png
│   ├── 01-file-organizer-preview-2.png
│   └── 01-file-organizer-preview-3.png
│
├── test_files/                 # Test files for the organization | Test fajlovi za organizaciju
│
├── main.py                     # Main script for file organization | Glavna skripta za organizaciju fajlova
├── logger.py                   # Login module | Modul za logovanje
├── setup_test_files.sh         # Bash script for creating test files | Bash skripta za kreiranje test fajlova
├── README.md                   # Description of the project | Opis projekta
└── log.txt                     # Activity log text file | Tekstalni Log fajl aktivnosti
```


## 🖼️ Preview | Pregled

<h4 align="center"><strong>🇬🇧:</strong> Visual steps of script execution</h4>  
<h4 align="center"><strong>🇷🇸:</strong> Vizuelni koraci izvršavanja skripte</h4>
<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="assets/01-file-organizer-preview-2.png" width="300"/>
        <p><strong>🇬🇧:</strong> Initial folder with mixed files<br/><strong>🇷🇸:</strong> Početni folder sa izmešanim fajlovima</p>
      </td>
      <td align="center">
        <img src="assets/01-file-organizer-preview-4.png" width="300"/>
        <p><strong>🇬🇧:</strong> Organized files after script execution<br/><strong>🇷🇸:</strong> Organizovani fajlovi nakon pokretanja skripte</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <img src="assets/01-file-organizer-preview-3.png" width="300"/>
        <p><strong>🇬🇧:</strong> Script execution in terminal<br/><strong>🇷🇸:</strong> Izvršavanje skripte u terminalu</p>
      </td>
      <td align="center">
        <img src="assets/01-file-organizer-preview-1.png" width="150"/>
        <p><strong>🇬🇧:</strong> Final folder structure<br/><strong>🇷🇸:</strong> Konačna struktura foldera</p>
      </td>
    </tr>
  </table>
</div>


## 🧑‍💻 Author & Learning Goal | Autor i ciljevi učenja

#### 🇬🇧: Josip Pavlović — This project is part of my 6-month plan to transition into a professional software development career. The main objective was to practice file operations, modular coding, and working with real-world directory structures in Python.

#### 🇷🇸: Josip Pavlović — Ovaj projekat je deo mog šestomesečnog plana prelaska u programersku karijeru. Cilj projekta bio je da se kroz praktičan rad savladaju operacije nad fajlovima, modularno programiranje i rad sa realnim strukturom foldera u Pythonu.



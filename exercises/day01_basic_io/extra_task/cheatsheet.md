## 🧪 Cheatsheet – Basic I/O Modes | _Cheatsheet – Osnovni režimi ulaza/izlaza_

## 🧠 Concepts Used | _Korišćeni pojmovi_

| English                                                            | _Serbian_                                                                          |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Use of `Path(__file__).resolve().parent` to get absolute directory | _Upotreba `Path(__file__).resolve().parent` za dobijanje apsolutnog direktorijuma_ |
| Using `input()` and `while` loop to capture multiline input        | _Korišćenje `input()` i `while` petlje za unos više linija_                        |
| Opening multiple files with a single `with` statement using `\`    | _Otvaranje više fajlova pomoću jednog `with` izraza uz `\`_                        |
| Writing output with `enumerate()` to add line numbers              | _Pisanje izlaza pomoću `enumerate()` radi dodavanja rednih brojeva_                |
| Handling mode switching using `sys.argv`                           | _Rukovanje promenom režima rada pomoću `sys.argv`_                                 |
| Using `f-strings` for dynamic output                               | _Korišćenje `f-string` izraza za dinamički izlaz_                                  |

---

## 🔍 Key Syntax | _Ključna sintaksa_

| English                           | _Serbian_                                          |
| --------------------------------- | -------------------------------------------------- |
| `Path(__file__).resolve().parent` | _Apsolutna putanja direktorijuma skripte_          |
| `with open(...) as ...`           | _Korišćenje context menadžera za rad sa fajlovima_ |
| `enumerate(lines, start=1)`       | _Enumeracija linija počevši od 1_                  |
| `input("Prompt: ")`               | _Unos korisnika sa porukom_                        |
| `sys.argv[1] == "--interactive"`  | _Provera CLI argumenta_                            |

---

## 📌 Notes | _Beleške_

| English                                                     | _Serbian_                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| All paths are absolute so script can run from any directory | _Sve putanje su apsolutne pa skripta može da se pokrene iz bilo kog direktorijuma_ |
| Empty line (`""`) is used to break interactive input loop   | _Prazna linija (`""`) se koristi za prekid interaktivne petlje_                    |
| Files are opened with `utf-8` encoding for compatibility    | _Fajlovi se otvaraju sa `utf-8` enkodiranjem radi kompatibilnosti_                 |

---

## 🧠 Cheatsheet – basic_version.py

---

### 🔍 Line-by-line explanation | _Objašnjenje po linijama_

---

### 🔹 Line 1

```python
import os
```

📌 **Explanation: | _Objašnjenje:_**
Imports the `os` module to work with paths. | _Uvozi `os` modul za rad sa putanjama._

---

### 🔹 Line 2

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
```

📌 **Explanation: | _Objašnjenje:_**
Gets the absolute path of the script’s folder. | _Dobija apsolutnu putanju foldera u kom se nalazi skripta._

---

### 🔹 Line 3–4

```python
input_path = os.path.join(script_dir, "input.txt")
output_path = os.path.join(script_dir, "output.txt")
```

📌 **Explanation: | _Objašnjenje:_**
Combines the script folder with file names to create absolute paths. | _Kombinuje folder skripte sa nazivima fajlova da bi dobio apsolutne putanje._

---

### 🔹 Line 5–6

```python
with open(input_path, "r", encoding="utf-8") as input_file, \
     open(output_path, "w", encoding="utf-8") as output_file:
```

📌 **Explanation: | _Objašnjenje:_**
Opens both files using a context manager (`with`). The backslash `\` splits the line for readability. | _Otvara oba fajla pomoću `with` kontekst menadžera. Simbol `\` omogućava podelu linije radi preglednosti._

---

### 🔹 Line 7

```python
    for index, line in enumerate(input_file, start=1):
```

📌 **Explanation: | _Objašnjenje:_**
Loops through each line in the input file and assigns line numbers starting from 1. | _Prolazi kroz svaku liniju u `input.txt` i dodeljuje joj redni broj počevši od 1._

---

### 🔹 Line 8

```python
        output_file.write(f"{index}: {line}")
```

📌 **Explanation: | _Objašnjenje:_**
Writes each line to the output file prefixed by its line number. | _Upisuje svaku liniju u `output.txt`, ispred dodaje njen redni broj._

---

## ✅ Why use absolute paths? | _Zašto koristiti apsolutne putanje?_

- Prevents file not found errors when script is run from another directory. | _Sprečava greške kada se skripta pokrene iz drugog foldera._
- Makes the script portable and robust. | _Omogućava prenosivost i pouzdanost._
- Aids debugging and improves reliability. | _Olakšava debagovanje i povećava stabilnost._

---

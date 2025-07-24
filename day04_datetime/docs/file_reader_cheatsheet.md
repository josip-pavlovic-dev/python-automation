# 📄 file_reader_cheatsheet.md — Read and Write Basics | Čitanje i Pisanje Fajlova

#### 🇬🇧: Demonstrates how to create and read text files in Python using `with open(...)`.

#### 🇷🇸: Prikazuje kako se kreiraju i čitaju tekstualni fajlovi u Python-u koristeći `with open(...)`.

## ✍️ Create a File with Sample Content | Kreiranje fajla sa sadržajem

```python
def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Line 1\n")
        file.write("Line 2\n")
        file.write("Line 3\n")
```

#### 🇬🇧: Creates a text file and writes multiple lines.

#### 🇷🇸: Kreira tekstualni fajl i upisuje više linija.

---

## 📖 Read File Line by Line | Čitanje fajla red po red

```python
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
```

#### 🇬🇧: Returns a list of lines from the file.

#### 🇷🇸: Vraća listu linija iz fajla.

---

## 💡 Tips | Saveti

- Always use `with open(...)` for safe file access.
- Koristi `strip()` da ukloniš `\n` pri prikazu.
- Uvek proveri da li fajl postoji pomoću `os.path.exists()`.

---

#### 📌 **Useful in**: Logging, configuration readers, automation scripts

#### 📌 **Korisno za**: Logovanje, čitanje konfiguracija, skripte za automatizaciju

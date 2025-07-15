# 🧹 Cheatsheet: size_cleaner.py

## 🇷🇸 Opis skripte
Skripta `size_cleaner.py` prolazi kroz dati folder (i njegove podfoldere) i **briše sve fajlove koji su manji od zadate veličine** u bajtovima. Koristi `os` modul i `logger.py` za logovanje svake akcije.

## 🇬🇧 Script Description
The script `size_cleaner.py` recursively scans a folder and **removes all files smaller than a defined byte size**. It uses the `os` module and `logger.py` for logging each action.

---

## 🧩 Funkcija / Function: `clean_by_size`

```python
clean_by_size(folder_path, min_size=100)
```

| Parametar | Tip / Type    | Podrazumevano / By default | Opis (🇷🇸)                                          | Description (🇬🇧)                             |
|-----------|---------|----------------|--------------------------------------------------|----------------------------------------------|
| `folder_path` | `str` | —              | Putanja do foldera za čišćenje                  | Path to the target folder                    |
| `min_size`    | `int` | `100`          | Minimalna veličina fajla (u bajtovima)          | Minimum file size (in bytes)                |

🛠️ Primer / An example:
```python
clean_by_size("test_folder", min_size=150)
```

---

## 🔎 Testiranje skripte / Testing Script: `test_size_cleaner.py`

| Deo testa | Objašnjenje (🇷🇸)                                   | Explanation (🇬🇧)                           |
|-----------|-----------------------------------------------------|---------------------------------------------|
| `bash_path` | Pronalazi putanju do `bash` interpretatora        | Locates path to `bash`                      |
| `setup_test_folder.sh` | Kreira test strukturu foldera         | Creates a test folder structure             |
| `clean_by_size(...)` | Pokreće brisanje fajlova ispod granice   | Runs cleanup for files under min size       |
| `list_files(...)` | Ispisuje preostale fajlove u folderu        | Logs remaining files in the folder          |

---

## 📄 Log poruke / Log Messages

| Nivo | Poruka (🇷🇸)                                   | Message (🇬🇧)                            |
|------|-----------------------------------------------|------------------------------------------|
| INFO | Čišćenje fajlova manjih od X bajtova           | Cleaning files smaller than X bytes      |
| INFO | Obrisani fajl: path (veličina)                 | Deleted file: path (size)                |
| WARNING | Greška pri proveri fajla                    | Error when checking file                 |
| ERROR | Greška pri izvršavanju funkcije               | Error during execution of the function   |

---

## 📦 Logički tok / Execution Flow

1. ✅ Ulazni folder se prosleđuje funkciji / The input folder is passed to the function
2. 🔄 Rekurzivno se obilaze svi fajlovi / All files are traversed recursively
3. ❌ Ako je veličina fajla < `min_size` → fajl se briše / If the file size is < `min_size` → the file is deleted
4. 🧾 Sve radnje se loguju uz odgovarajući nivo (INFO/WARNING/ERROR) / All actions are logged with the appropriate level (INFO/WARNING/ERROR)

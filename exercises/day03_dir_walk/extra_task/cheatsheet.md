# 📄 Cheatsheet | _Pregled komandi_

## ✅ Key Concepts | _Ključni koncepti_

- `os.walk(path)` | _Rekurzivno obilazi sve foldere i fajlove u putanji._
- `foldername, subfolders, filenames` | _Tuple vrednosti koje `os.walk()` vraća po iteraciji._
- `os.getcwd()` | _Vraća trenutni radni direktorijum._
- `print()` | _Koristi se za prikaz rezultata strukture._

## 📌 Example usage | _Primer korišćenja_

```python
for foldername, subfolders, filenames in os.walk("."):
    print("Folder:", foldername)
    for f in filenames:
        print("  File:", f)
```

---

## 📄 Pathlib Cheatsheet | _Pregled pathlib komandi_

### ✅ Key Methods | _Ključne metode_

- `Path(__file__).resolve()` | _Apsolutna putanja do trenutne skripte_
- `path.exists()` | _Proverava da li putanja postoji_
- `path.is_file()` / `path.is_dir()` | _Da li je fajl ili folder_
- `path / "subfolder" / "file.txt"` | _Spajanje putanja pomoću `/` operatora_
- `path.read_text()` / `path.write_text()` | _Čitanje i pisanje fajlova_
- `path.glob("*.txt")` / `path.rglob("*.txt")` | _Pretraga fajlova (rekurzivna i nerekurzivna)_
- `path.stat().st_mtime` | _Vreme poslednje izmene fajla_

---

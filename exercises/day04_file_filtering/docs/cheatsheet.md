# 📄 Cheatsheet | _Pregled najvažnijih izraza_

## ✅ Why use pathlib and filtering? | _Zašto koristiti pathlib i filtriranje?_

- Simple, readable path management | _Jednostavno i čitljivo upravljanje putanjama_
- Easy recursive search with `rglob()` | _Laka rekurzivna pretraga pomoću `rglob()`_
- Cross-platform compatible | _Radi na svim operativnim sistemima_

---

## 📌 Explanation: | _Objašnjenje:_

### `Path(__file__).resolve().parent`

- Returns the folder where the script is located | _Vraća folder u kome se skripta nalazi_

### `.rglob("*.*")`

- Recursively lists all files | _Rekurzivno listanje svih fajlova_

### `stat().st_size`

- Returns the file size in bytes | _Vraća veličinu fajla u bajtovima_

### `datetime.fromtimestamp(file.stat().st_mtime)`

- Converts last modification time to datetime | _Pretvara vreme poslednje izmene u datetime objekat_

### `with open(file, "w", encoding="utf-8")`

- Opens a file for writing, replacing previous content | _Otvara fajl za pisanje, brišući prethodni sadržaj_

---

## 🔍 Key Syntax | _Ključna sintaksa_

```python
py_files = [f for f in filtered_files if f.suffix == ".py"]
md_files = [f for f in filtered_files if f.suffix == ".md"]
```

Filters files by extension. | _Filtrira fajlove po ekstenziji._

---

## 👨‍💻 Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-Josip%20Pavlović-blue?logo=github)](https://github.com/Jole85)

**Josip Pavlović — aspiring Python developer from Novi Sad**

---

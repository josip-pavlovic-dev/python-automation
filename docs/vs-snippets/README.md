# ⚡ VS Code Snippets

## 📘 Description

This folder contains all **custom VS Code snippets** used throughout the `python-automation` project. Snippets help you write code faster by expanding short trigger words into full blocks of code.

---

### 📂 File Structure

| 📄 File Name                         | 🔍 Description                         |
| ------------------------------------ | -------------------------------------- |
| `day01_file_organizer.code-snippets` | Snippets for file organization tasks   |
| `day02_file_info.code-snippets`      | Snippets for file metadata tasks       |
| `day03_file_ops.code-snippets`       | Snippets for reading/writing files     |
| `day04_datetime.code-snippets`       | Snippets for date and time automation  |
| `day05_os_basics.code-snippets`      | Snippets using `os` module basics      |
| `pylance_basics.code-snippets`       | Snippets for type hints and inspection |
| `py_sr-comments.code-snippets`       | Predefined comment snippets in Serbian |
| `snippet_triggers_cheatsheet.md`     | 📌 Cheatsheet of all trigger keywords  |

---

## 🧪 How to Use

1. Open any `.py` file in VS Code.
2. Type a **trigger** word (e.g., `withopen`, `extcheck`, `defhint`).
3. Press `TAB` or `ENTER` to expand the snippet.
4. Modify the generated code as needed.

See [`snippet_triggers_cheatsheet.md`](./snippet_triggers_cheatsheet.md) for a full list of available triggers.

---

## 🔄 Snippet Sync

Snippets are automatically copied into each project's `.vscode` folder by running:

```bash
python scripts/sync_snippets.py
```

Old snippets in target folders are cleaned up before copying.

---

## 🛠 Notes

- If a `.code-snippets` file is not mapped in `sync_snippets.py`, it will be skipped.
- Global snippets (e.g., `pylance_basics`) are synced into the root `.vscode` folder.
- Snippets are visible via IntelliSense or by typing their trigger.

---

# ⚡ VS Code Snippeti

## 📘 Opis

Ovaj folder sadrži sve **prilagođene snippete** korišćene u okviru projekta `python-automation`.
Snippeti ubrzavaju rad tako što omogućavaju da se korišćenjem skraćenih reči (`trigger`) automatski proširi kompletan blok koda.

---

### 📂 Struktura fajlova

| 📄 Naziv fajla                       | 🔍 Opis                                   |
| ------------------------------------ | ----------------------------------------- |
| `day01_file_organizer.code-snippets` | Snippeti za organizaciju fajlova          |
| `day02_file_info.code-snippets`      | Snippeti za prikaz informacija o fajlu    |
| `day03_file_ops.code-snippets`       | Snippeti za rad sa fajlovima              |
| `day04_datetime.code-snippets`       | Snippeti za datum i vreme                 |
| `day05_os_basics.code-snippets`      | Snippeti za rad sa `os` modulom           |
| `pylance_basics.code-snippets`       | Snippeti za type hints i analizu          |
| `py_sr-comments.code-snippets`       | Komentari i objašnjenja na srpskom jeziku |
| `snippet_triggers_cheatsheet.md`     | 📌 Lista svih dostupnih trigger-a         |

---

## 🧪 Kako koristiti

1. Otvori bilo koji `.py` fajl u VS Code-u.
2. Ukucaj **trigger** reč (npr. `withopen`, `extcheck`, `defhint`).
3. Pritisni `TAB` ili `ENTER` da proširiš snippet.
4. Po potrebi izmeni generisani kod.

Pogledaj [`snippet_triggers_cheatsheet.md`](./snippet_triggers_cheatsheet.md) za kompletnu listu `trigger-a`.

---

## 🔄 Sinhronizacija

Snippeti se automatski kopiraju u svaki `.vscode` folder pomoću komande:

```bash
python scripts/sync_snippets.py
```

Stari fajlovi se brišu pre kopiranja.

---

## 🛠 Napomene

- Ako snippet nije mapiran u `sync_snippets.py`, biće preskočen.
- Globalni snippeti (`pylance_basics`) se sinhronizuju u `.vscode` folder na root nivou.
- Snippeti se pozivaju kroz IntelliSense ili kucanjem `trigger` reči.

---

```
Write smarter. Reuse code. Speed up your workflow.
Piši pametnije. Iskoristi gotove blokove. Ubrzaj razvoj. ⚡
```

```

---

```

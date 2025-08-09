# 🧠 Terminology Cheatsheet

📁 Location: `docs/terminology_cheatsheet.md`

## 🇬🇧 Terminology Reference (English)

| Term                 | Meaning / Use                                             |
| -------------------- | --------------------------------------------------------- |
| **task**             | A specific coding assignment or exercise                  |
| **snippet**          | A reusable piece of code                                  |
| **script**           | A full file that can be executed (usually `.py`)          |
| **comment**          | Explanatory text in code (using `#`)                      |
| **trigger**          | Shortcut that expands into a snippet                      |
| **cheatsheet**       | A summary document with quick references                  |
| **project root**     | The main folder of a project                              |
| **subfolder**        | A directory inside another directory                      |
| **README.md**        | Main Markdown documentation file                          |
| **.vscode**          | Folder with configuration files for VS Code               |
| **settings.json**    | VS Code workspace settings file                           |
| **keybindings.json** | File that defines keyboard shortcuts                      |
| **launch.json**      | Configuration for debugging in VS Code                    |
| **terminal**         | Command-line interface used for running scripts           |
| **prompt**           | Text input field in the terminal (e.g., `$` or `PS C:\>`) |
| **log**              | Output text that helps with debugging                     |
| **commit**           | Saving a snapshot in Git                                  |
| **push**             | Sending local Git changes to GitHub                       |

---

## 🇷🇸 Pojmovnik termina (srpski)

| Pojam                | Značenje / Upotreba                          |
| -------------------- | -------------------------------------------- |
| **task**             | Konkretan zadatak ili vežba iz programiranja |
| **snippet**          | Iskoristiv deo koda koji se često ponavlja   |
| **script**           | Izvršni Python fajl (npr. `main.py`)         |
| **komentar**         | Objašnjenje unutar koda (`#`)                |
| **trigger**          | Skraćenica koja aktivira snippet             |
| **cheatsheet**       | Pregledna skripta sa korisnim podsetnicima   |
| **root projekta**    | Glavni folder projekta                       |
| **podfolder**        | Folder unutar drugog foldera                 |
| **README.md**        | Glavni Markdown fajl dokumentacije           |
| **.vscode**          | Folder sa konfiguracijom za VS Code          |
| **settings.json**    | Postavke radnog prostora u VS Code-u         |
| **keybindings.json** | Podešavanja tastaturnih prečica              |
| **launch.json**      | Podešavanje debager okruženja u VS Code-u    |
| **terminal**         | Komandna linija za pokretanje skripti        |
| **prompt**           | Mesto za unos komandi (`$`, `PS C:\>`)       |
| **log**              | Tekstualni zapis dešavanja u skripti         |
| **commit**           | Snimanje promene u Git sistemu               |
| **push**             | Slanje lokalnih promena na GitHub            |

---

## Forma upita za slanje:

🎯 CILJ (kratko):

- Npr. "Generisati README.md za legacy/day01_basic_io"

📂 PRILOZI:

- cheatsheet.md (iz docs/)
- snippets.md (iz docs/)
- main.py (iz root-a projekta)
- structure.txt (celokupna struktura projekta)

🛠️ KORACI:

1. Pročitati priložene fajlove i structure.txt
2. Kreirati README.md po standardu koji smo ranije dogovorili (bilingvalno, badge-ovi itd.)
3. Ne menjati strukturu, samo generisati dokument
4. Poslati ceo fajl u odgovoru

⏱️ HITNOST:

- Odmah (ovo je deo današnjeg plana za legacy)

---

Koristi ovu mini-šemu (kratko, strogo):

ZADATAK: [1–2 rečenice – šta želiš]
KONTEKST: [maks 3 rečenice – zašto, gde]
FAJLOVI: [relativne putanje, opciono opseg linija]
KOMANDE: [ako ima – šta da pokrenem / očekivani output]
DONE KADA: [objektivni kriterijumi – npr. svi testovi prolaze, README ažuriran]
OGRANIČENJA: [npr. bez spoljnjih biblioteka, Python 3.13, Windows]

---

Primer (realan)

ZADATAK: Dovrši logger formattere i proveri JSON izlaz.
KONTEKST: Logger ne hvata traceback kao JSON – sutra radim pytest integraciju.
FAJLOVI: day01_file_organizer/src/logger.py (linije 40–120)
KOMANDE: pytest -q
DONE KADA: test_logger.py prolazi; line_by_line.md dopunjen primerom JSON loga.
OGRANIČENJA: ostati na standardnoj biblioteci; bez spoljnjih handlera.

🗂️ _Ovaj fajl koristi se kao referenca tokom komunikacije sa asistentom i za efikasnije korišćenje profesionalne terminologije tokom učenja._

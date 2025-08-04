# 🎯 Amateur mod

U **Amateur mod** režimu:

- Ja sam istovremeno **senior** koji objašnjava koncepte i **junior** koji postavlja pitanja koja bi ti možda propustio.
- Ti imaš prostor da pitaš sve što ti nije jasno – čak i ono što deluje "glupo".
- Fokus nije samo na učenju kako se nešto piše, već _zašto_ i _kako se o tome razmišlja_.
- Svaki modul (logger, argparse, pathlib...) biće analiziran kroz profesionalnu upotrebu, a tvoja pitanja će biti deo toka.

## 📌 Glavne komponente

- `argparse` → za obradu komandne linije (CLI)
- `pathlib` → rad sa apsolutnim i relativnim putanjama
- `shutil` → kopiranje, premeštanje i brisanje fajlova i foldera
- `logging` → kreiranje log fajlova, hendleri, formati
- `__file__` i `.resolve()` → razumevanje putanja u odnosu na lokaciju skripte

---

## 🎯 Amateur mod | Linija po linija analiza `main.py`

---

### 👨‍💻 `"""Sorts files in the selected directory by their extension..."""`

👶 _Junior_: Zašto odmah pišemo triple-quote docstring iznad fajla?

👴 _Senior_: Ovo je tzv. **module-level docstring**. Profesionalni projekti uvek počinju dokumentacijom na vrhu fajla. Ukazuje šta taj modul radi, koji su ključni moduli u upotrebi (ovde `argparse`, `pathlib`, `shutil`, `logger`), i time omogućava brzi pregled bilo kom developeru koji ulazi u kod. 💡

---

### 👨‍💻 `from pathlib import Path`

👶 _Junior_: Zašto koristimo `pathlib.Path` umesto `os.path`?

👴 _Senior_: Zato što je `pathlib` _moderniji_ i **objektno orijentisan** modul. Radimo sa `Path` objektima koji imaju metode (npr. `.iterdir()`, `.suffix`) i dobijamo čitljiviji i fleksibilniji kod. U industriji se danas favorizuje `pathlib`.

---

### 👨‍💻 `import shutil`

👶 _Junior_: Šta radi `shutil`?

👴 _Senior_: Modul `shutil` se koristi za **rad sa fajlovima i folderima na nivou operativnog sistema**. Najčešće za:

- `move()` – premeštanje fajlova,
- `copy()` – kopiranje,
- `rmtree()` – brisanje celih foldera.

U ovom slučaju `shutil.move()` služi za premeštanje fajlova u podfoldere.

---

### 👨‍💻 `import argparse` i `import sys`

👶 _Junior_: A `argparse` i `sys`?

👴 _Senior_: `argparse` se koristi za parsiranje **komandne linije (CLI)** – korisnik može da unese putanju kao argument. `sys` ovde još ne koristimo, ali obično je prisutan ako treba da npr. `sys.exit()` pozoveš kod greške. Možemo ga za sada i ukloniti ako ga ne koristimo.

---

### 👨‍💻 `from src.logger import setup_logger`

👶 _Junior_: Zašto imamo `setup_logger()`?

👴 _Senior_: Umesto da pišemo logiku logovanja direktno u svaki fajl, napravili smo **poseban fajl `logger.py`** u `src/` koji centralizuje logiku i podešavanja logovanja. Funkcija `setup_logger()` vraća logger objekat koji koristi `FileHandler` i `StreamHandler`. **Profesionalna praksa**.

---

### 👨‍💻 `from src.utils.interactive_folder_browser import select_folder_gui`

👶 _Junior_: Šta je `select_folder_gui()`?

👴 _Senior_: To je funkcija koja otvara **GUI prozor za biranje foldera**, koristi `tkinter.filedialog`. Ako korisnik ne navede putanju kroz CLI, ova funkcija omogućava da je odabere vizuelno. Veoma korisno za automatizaciju.

---

### 👨‍💻 `logger = setup_logger()`

👶 _Junior_: Znači ovde pokrećemo logger?

👴 _Senior_: Da. Pozivamo `setup_logger()` da bismo dobili `logger` objekat koji možemo koristiti kroz ceo fajl sa npr. `logger.info()`, `logger.error()`, itd. Uvek se loguje šta se desilo – profesionalno i korisno za debugging.

---

### 👨‍💻 Funkcija `get_arguments()`

```python
def get_arguments():
    ...
```

👶 _Junior_: Zašto koristimo posebnu funkciju za argumente?

👴 _Senior_: Da bi kod bio modularan. Ova funkcija prvo pokušava da uzme CLI path, a ako nije unet – pada nazad na GUI. Tako korisnik ima **fleksibilnost**: može da koristi CLI ili GUI.

---

### 👨‍💻 `args.path` i `args.path.exists()`

👶 _Junior_: Kako znamo da je `args.path` tipa `Path`?

👴 _Senior_: Zato što smo u `parser.add_argument(... type=Path)` definisali da `argparse` odmah konvertuje string putanju u `Path` objekat. Zato možemo da pišemo `.exists()` direktno.

---

### 👨‍💻 `organize_files_by_extension(folder_path: Path)`

👶 _Junior_: Šta ova funkcija radi?

👴 _Senior_: Prima `folder_path`, prolazi kroz sve fajlove i:

1. čita ekstenziju fajla (`.suffix[1:]`) – skida tačku.
2. kreira folder sa nazivom te ekstenzije (npr. `txt`, `jpg`, `no_extension`)
3. koristi `shutil.move()` da premesti fajl u odgovarajući folder
4. loguje uspeh ili grešku

---

### 👨‍💻 `if __name__ == "__main__":`

👶 _Junior_: Zašto je ovo na kraju?

👴 _Senior_: To je standardni Python idiom – omogućava da se ovaj fajl koristi kao **skripta ili kao modul**. Kad se pokrene kao skripta, aktivira se redosled:

1. pokrene logger
2. uzme folder
3. organizuje fajlove

---

## 📦 Najvažnije metode `Path` objekta (iz `pathlib` modula)

| Metoda                  | Opis                                     | _Prevod / Objašnjenje_                      |
| ----------------------- | ---------------------------------------- | ------------------------------------------- |
| `.exists()`             | Proverava da li fajl/folder postoji      | _Da li fajl/folder postoji na toj putanji?_ |
| `.is_file()`            | Da li je putanja fajl?                   | _Vraća `True` ako je fajl_                  |
| `.is_dir()`             | Da li je folder?                         | _Vraća `True` ako je folder_                |
| `.iterdir()`            | Iterira sadržaj foldera                  | _Za `for` petlju kroz sadržaj foldera_      |
| `.suffix`               | Ekstenzija fajla (`.txt`)                | _Koristi se za sortiranje po tipu_          |
| `.suffixes`             | Lista svih ekstenzija                    | _Korisno za fajlove kao `file.tar.gz`_      |
| `.stem`                 | Ime fajla bez ekstenzije                 | _`file.txt` → `file`_                       |
| `.name`                 | Puno ime fajla sa ekstenzijom            | _`file.txt` → `file.txt`_                   |
| `.parent`               | Roditeljski folder                       | _Putanja iznad trenutnog fajla/foldera_     |
| `.resolve()`            | Vraća apsolutnu putanju                  | _Kao `os.path.abspath()`_                   |
| `.absolute()`           | Takođe vraća apsolutnu putanju           | _Gotovo isto kao `.resolve()`_              |
| `.joinpath("sub")`      | Spaja sa podfolderom/fajlom              | _Umesto `/` operatora_                      |
| `.with_suffix(".md")`   | Menja ekstenziju                         | _`file.txt` → `file.md`_                    |
| `.with_name("new.txt")` | Menja ime fajla                          | _`file.txt` → `new.txt`_                    |
| `.mkdir(parents=True)`  | Pravi folder (rekurzivno)                | _Ako ne postoji – napravi ga_               |
| `.touch()`              | Pravi prazan fajl (kao `touch` u Bash-u) | _Za kreiranje fajla bez sadržaja_           |
| `.unlink()`             | Briše fajl                               | _Obrati pažnju – bez korpe!_                |
| `.rmdir()`              | Briše folder                             | _Ako je prazan_                             |
| `.open()`               | Otvara fajl za čitanje/pisanje           | _Radi sa `with` blokom_                     |
| `.read_text()`          | Čita sadržaj fajla (text)                | _Jedan-liner za čitanje tekst fajla_        |
| `.write_text("Hello")`  | Upisuje sadržaj u fajl                   | _Jedan-liner za pisanje_                    |

---

## ✅ Koje treba da znaš **odmah**?

Kao početnik u automatizaciji i organizaciji fajlova, fokusiraj se na ove:

1. `.exists()`
2. `.is_file()` i `.is_dir()`
3. `.suffix`, `.stem`, `.name`
4. `.parent`
5. `.mkdir(parents=True, exist_ok=True)`
6. `.iterdir()`
7. `.resolve()`
8. `.read_text()` i `.write_text()`

---

## 🧠 Amateur Mod: Analiza `logger.py` liniju po liniju

---

### 🔍 **1–3: Uvoz modula**

```python
import logging
from pathlib import Path
from datetime import datetime
```

👴 **Senior kaže:**

- `logging` je standardni Python modul za logovanje – koristi se umesto `print()` kada želiš ozbiljno da pratiš tok programa, greške i događaje.
- `Path` iz `pathlib` ti olakšava rad sa putanjama – umesto `os.path.join`, koristiš elegantniju sintaksu `Path(...) / "subfolder"`.
- `datetime` ti daje tačno vreme, korisno kada praviš jedinstvene nazive fajlova (npr. log fajlova sa timestamp-om).

👶 **Junior pita:**

- Zašto koristimo `Path(__file__).resolve()` kasnije u kodu?
- Odgovor: Zato što želimo da dobijemo **apsolutnu putanju** do trenutnog fajla, bez obzira odakle se program pokreće.

---

### 🔍 **5–6: Kreiranje i konfiguracija logger-a**

```python
logger = logging.getLogger("file_organizer")
logger.setLevel(logging.INFO)
```

👴 **Senior:**

- Kreiramo logger po imenu `"file_organizer"` – možeš imati više logger-a u većim projektima, pa je ime korisno.
- Nivoi logovanja: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
  Ovde koristimo `INFO` jer nas zanimaju poruke o regularnim događajima.

👶 **Junior:**

- Šta ako želim da pratim i greške i uspešno izvršene operacije?
- `INFO` će pokupiti sve iznad sebe (`INFO`, `WARNING`, `ERROR`, `CRITICAL`). Za sve detalje koristi `DEBUG`.

---

### 🔍 **8–9: Provera postojećih handlera**

```python
if logger.hasHandlers():
    return logger
```

👴 **Senior:**

- `hasHandlers()` proverava da li logger već ima povezane "slušače" (handler-e).
- Ako već postoji – `return` sprečava dupliranje handlera. U suprotnom, imao bi višestruke duplikate istih poruka u fajlu/terminalu!

👶 **Junior:**

- Kako se to dešava?
- Na primer, ako dva puta pozoveš `setup_logger()` bez ove provere, dodaćeš dva `StreamHandler`-a i poruke će se duplirati.

---

### 🔍 **11–12: Kreiranje foldera za logove**

```python
log_dir = Path(__file__).resolve().parent.parent / "log"
log_dir.mkdir(exist_ok=True)
```

👴 **Senior:**

- `Path(__file__).resolve().parent.parent` te vodi iz `src/logger.py` → nazad na root folder.
- Zatim `/ "log"` dodaje folder za čuvanje log fajlova.
- `mkdir(exist_ok=True)` znači: napravi folder ako ne postoji. Ako postoji – ne prijavljuj grešku.

👶 **Junior:**

- Šta ako želim da log folder bude unutar `src/`?
- Samo promeni putanju, npr. `Path(__file__).resolve().parent / "log"` – to je potpuno fleksibilno.

---

### 🔍 **14–15: Naziv fajla sa timestamp-om**

```python
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = log_dir / f"log_{timestamp}.txt"
```

👴 **Senior:**

- Generišemo jedinstveni naziv fajla, npr. `log_2025-08-03_12-15-00.txt`
- Na taj način čuvaš **odvojene logove za svako pokretanje** programa. To olakšava dijagnostiku i pregled starih logova.

👶 **Junior:**

- A šta ako želim **uvek isti fajl** (npr. `latest.log`)?
- Samo koristi: `log_file = log_dir / "latest.log"` i izostavi timestamp.

---

### 🔍 **17–18: Konfigurisanje fajl handlera**

```python
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.INFO)
```

👴 **Senior:**

- `FileHandler` upisuje poruke u fajl.
- `mode="w"` znači: svaki put obriši prethodni sadržaj (overwrite).
- Možeš koristiti `"a"` za **append** ako želiš da dodaješ bez brisanja.

👶 **Junior:**

- Kako da logujem i greške (`ERROR`) i obaveštenja (`INFO`) u fajl?
- Postavi `file_handler.setLevel(logging.DEBUG)` – dobićeš sve nivoe poruka.

---

### 🔍 **20–21: Konfigurisanje terminal handlera**

```python
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
```

👴 **Senior:**

- `StreamHandler` šalje poruke u terminal (stdout).
- Time program korisniku prikazuje šta se dešava uživo – ali sve se i dalje čuva u fajlu (zahvaljujući `FileHandler`).

👶 **Junior:**

- Mogu li da imam različite nivoe za fajl i terminal?
- Da! Npr. u fajl sve (`DEBUG`), a u terminal samo `WARNING` i gore.

---

### 🔍 **23–25: Formatiranje poruka**

```python
formatter = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
```

👴 **Senior:**

- `Formatter` oblikuje svaku poruku: vreme — nivo — poruka.
- Npr. `2025-08-03 12:21:30 — INFO — Starting program...`

👶 **Junior:**

- Mogu li da dodam ime fajla i liniju koda?
- Da, koristi format string kao:
  `"%(asctime)s — %(name)s — %(levelname)s — %(filename)s:%(lineno)d — %(message)s"`

---

### 🔍 **27–28: Dodavanje handlera logger-u**

```python
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
```

👴 **Senior:**

- Logger bez handlera je kao kamera bez objektiva. Moraš dodati gde i kako da snima.
- Ovde snima u fajl + u terminal.

---

### 🔍 **30: Povratak logger objekta**

```python
return logger
```

👴 **Senior:**

- Sad kada je sve podešeno, vraćamo konfigurisani logger nazad u program.
- Možeš ga koristiti bilo gde, samo importuj `setup_logger()` i pozovi `logger = setup_logger()`.

---

## ✅ Zaključak

- Logger modul je jako fleksibilan.
- Možeš istovremeno pratiti događaje u terminalu i u fajlu.
- Možeš filtrirati poruke, menjati nivoe, formatirati ih i pratiti ih kroz vreme.
- `Path` + `__file__` daje čistu, stabilnu kontrolu nad putanjama.

---

## ❓ Pitanja koja su mi se javila tokom rada

- Kada i zašto koristiti `Path(__file__).resolve().parent.parent`?
- Zašto se proverava `if logger.hasHandlers()` i kakve sve hendleri postoje?
- Da li mogu odmah koristiti napredne funkcije ili moram prvo savladati jednostavnije verzije?
- Kako razlikovati osnovne module (`os`, `shutil`, `argparse`) od modernijih (`pathlib`) u praksi?

---

## ✅ Lekcije koje sam naučio

- Ako se ne postavi pravilno `log_path` relativno ka projektu, log se kreira na nepoznatim mestima.
- `logger.hasHandlers()` sprečava višestruko dodavanje istih hendlera.
- `Path.resolve()` daje pravu apsolutnu putanju čak i kada se koristi `__file__`.
- Snaga CLI-ja u kombinaciji sa `argparse` modulom omogućava izuzetno fleksibilne skripte.

---

## 🧩 Ključni snippet-i

- Inicijalizacija logger-a sa fajl i stream handlerom
- Pravljenje apsolutne putanje do `log.txt` fajla
- Korišćenje `argparse.ArgumentParser()` sa različitim `action` i `type`
- Navigacija pomoću `Path(__file__).resolve().parents[2]`

(Detaljno u `docs/snippets.md`)

---

## 📘 Korisni linkovi

- [Python logging — official docs](https://docs.python.org/3/library/logging.html)
- [argparse — CLI parser](https://docs.python.org/3/library/argparse.html)
- [pathlib — objektno orijentisani rad sa fajlovima](https://docs.python.org/3/library/pathlib.html)

---

##### 📆 Period rada: 1–3. avgust 2025 — Sprint blok 3 i 4

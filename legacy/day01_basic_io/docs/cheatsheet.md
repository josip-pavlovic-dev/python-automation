# 📘 Cheatsheet – main.py (day01_basic_io)

## 🔹 What this script does | _Šta radi ova skripta_

- Reads from `input.txt` and writes numbered lines to `output.txt` | _Čita iz `input.txt` i upisuje numerisane redove u `output.txt`_

- Or lets the user type multiple lines and saves them with line numbers | _Ili omogućava korisniku da unese više linija i snima ih sa rednim brojevima_

- Works regardless of the working directory using absolute paths | _Radi nezavisno od trenutnog foldera pomoću apsolutnih putanja_

---

## 🔹 CLI Arguments | _Argumenti komandne linije_

| Argument        | Behavior                             | Ponašanje                                 |
| --------------- | ------------------------------------ | ----------------------------------------- |
| _no argument_   | Reads input.txt and writes to output | Čita `input.txt` i upisuje u `output.txt` |
| `--interactive` | Takes user input and saves to file   | Omogućava unos korisnika i snima u fajl   |

---

## 🔹 Used Concepts | _Korišteni Pojmovi_

| Concept           | Description                         | Opis                                     |
| ----------------- | ----------------------------------- | ---------------------------------------- |
| `sys.argv`        | Command line arguments              | Argumenti komandne linije                |
| `pathlib.Path`    | Safer, cross-platform path handling | Bezbedno upravljanje putanjama           |
| `enumerate()`     | Adds index to each line             | Dodaje indeks svakom redu                |
| `context manager` | `with` block for safe file I/O      | `with` blok za bezbedan rad sa fajlovima |
| `UTF-8 encoding`  | Standard text encoding              | Standardno kodiranje teksta              |
| `input()`         | User terminal input                 | Unos korisnika u terminalu               |

---

## 🔹 Best Practices | _Preporučena praksa_

- Use `Path(__file__).parent` to always calculate base path | _Koristi `Path(__file__).parent` da izračunaš baznu putanju_
- Separate logic into `process_file_input` and `process_user_input` | _Podeli logiku u odvojene funkcije `process_file_input` i `process_user_input`_
- Use list accumulation for multi-line input | _Koristi listu za višelinijski unos_

---

## 🔹 Absolute Path Setup | _Podešavanje apsolutne putanje_

```python
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"
```

🔹 `Path(__file__).parent` | Gets absolute path of script's directory | _Dobija apsolutnu putanju direktorijuma u kome se nalazi skripta_

🔹 `BASE_DIR / "input.txt"` | Builds full path by joining directory with filename | _Formira kompletnu putanju spajanjem foldera i imena fajla_

🔹 Result : Enables the script to run from any working directory | _Skripta se može pokretati iz bilo kog foldera_

---

## 🧠 Šta je _kontekst menadžer_ u Pythonu?

#### **Kontekst menadžer** je mehanizam koji upravlja nekim _resursom_ — i to na sledeći način:

1. Automatski ga **priprema** pre nego što ga koristiš (`__enter__`)
2. Automatski ga **zatvara, oslobađa, čisti** kada si završio (`__exit__`)

#### Najpoznatiji primer u Pythonu je:

```python
with open("neki_fajl.txt", "r") as f:
    sadržaj = f.read()
```

---

## 🧩 Zašto postoji `with`?

#### Da bi izbegao **ručno otvaranje i zatvaranje fajlova** kao u ovome:

```python
f = open("neki_fajl.txt", "r")
sadržaj = f.read()
f.close()  # Ne smeš zaboraviti!
```

Ako se dogodi greška pre `f.close()`, fajl može ostati otvoren – što može dovesti do:

- curenja memorije,
- zaključanih fajlova (na Windowsu naročito),
- gubitka podataka.

---

## ✅ Prednosti kontekst menadžera (`with`)

| Prednost              | Objašnjenje                                         |
| --------------------- | --------------------------------------------------- |
| 📦 Automatizacija     | Fajl se zatvara automatski                          |
| 🔐 Sigurnost          | Greške neće ostaviti fajl u lošem stanju            |
| 🧹 Čist kod           | Više nema potrebe za ručnim `try/finally` blokovima |
| 🔄 Višestruki resursi | Možeš otvoriti više fajlova u jednoj liniji         |

---

## 🧪 Šta se zaista dešava iza kulisa?

Kada napišeš:

```python
with open("file.txt", "r") as f:
    data = f.read()
```

Python poziva ove metode na objektu koji `open()` vraća:

1. `f.__enter__()` → vraća ti otvoreni fajl
2. `f.__exit__()` → automatski poziva `close()` kada `with` blok završi

Zato se kaže da je objekat **file handler** (kao `f`) **kontekst menadžer** – jer implementira `__enter__` i `__exit__`.

---

## 🧠 Šta je kontekst menadžer u Pythonu?:

#### 🗣️ _To je mehanizam koji automatski upravlja resursima kao što su fajlovi, i omogućava da se oni sigurno koriste i zatvore. Najčešće se koristi sa `with` blokom, koji obezbeđuje da se fajl automatski zatvori čak i ako se desi greška._

---

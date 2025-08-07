# 📌 Šta znači `__name__` u Python-u?

```python
__name__
```

* **U svakom Python fajlu**, ova ugrađena promenljiva (`__name__`) sadrži:

  * `"__main__"` ako je fajl **pokrenut direktno** (`python logger.py`)
  * `"ime_modula"` ako je fajl **importovan** u drugi modul

Na primer:

```python
# ako pokrećeš ovaj fajl direktno
print(__name__)  # ispisuje: "__main__"

# ako se importuje kao modul u drugi fajl
# npr. import logger
# onda: print(__name__) => "logger"
```

To ti omogućava da znaš da li se fajl koristi **kao glavni program** ili je deo **veće automatizacije / sistema**.

---

## 🧠 Kako se koristi sa `getLogger(__name__)`

```python
logger = logging.getLogger(__name__)
```

Ova linija **pravi logger** koji:

* nosi **ime modula** u kojem se nalazi (`logger`, `main`, `interactive_folder_browser`, itd.)
* omogućava da loguješ poruke *koje dolaze iz tog konkretnog fajla* (modula)

### ❗ Zašto je ovo bitno?

* Ako koristiš samo `logging.info()`, sve se loguje kao `"root"` — nemaš uvid odakle poruka dolazi.
* Ako koristiš `getLogger(__name__)`, možeš imati **različite log fajlove**, **različite formate**, ili **fino podešene filtere** po modulu.

U većim projektima, ovo je obavezno.

---

## 🛠️ Analogija

Zamisli `__name__` kao **ime pošiljaoca** u e-mailu.
A `getLogger(__name__)` kao **uvođenje tog pošiljaoca u zapisnik**. Umesto da sve piše „poruka iz sistema“, znaćeš da je poruka stigla iz `logger.py`, `main.py` ili `interactive_folder_browser.py`.

---

## ✅ Ukratko

| Element                  | Značenje                                 |
| ------------------------ | ---------------------------------------- |
| `__name__ == "__main__"` | Fajl se pokreće direktno                 |
| `__name__ == "logger"`   | Fajl je importovan kao modul             |
| `getLogger(__name__)`    | Logger se identifikuje po imenu fajla    |
| Prednost                 | Bolje praćenje poruka i modularnost loga |

---


# 🛠 Ruff & Black – mini vodič

## 📌 Svrha

- **Ruff** – veoma brz Python _linter_ i alat za automatsko ispravljanje problema u kodu
- **Black** – strogi Python _formatter_ koji automatski sređuje kod prema unapred definisanom stilu

---

## ✅ Zašto koristiti Ruff & Black?

- Održavaju konzistentan stil koda u celom projektu
- Štede vreme jer eliminišu rasprave o formatiranju koda
- Hvataju greške i lošu praksu još pre pokretanja programa
- Brzi su i dobro funkcionišu zajedno

---

## ⚙ Instalacija

```bash
pip install ruff black
```

---

## 🔍 Ruff – najčešće komande

```bash
ruff check .                  # Proverava sve Python fajlove u trenutnom folderu
ruff check file.py            # Proverava određeni fajl
ruff check . --fix            # Automatski popravlja pronađene probleme
ruff check . --select E,F     # Proverava samo određene tipove grešaka (E = Error, F = Failure)
ruff check . --ignore E501    # Ignoriše pravilo (E501 = predugačke linije)
```

---

## 🖋 Black – najčešće komande

```bash
black .                       # Formatira sve Python fajlove u trenutnom folderu
black file.py                 # Formatira određeni fajl
black . --check                # Samo proverava format bez izmena fajlova
black . --diff                 # Prikazuje razlike bez primene izmena
```

---

## 🔄 Predloženi workflow (Ruff + Black zajedno)

```bash
ruff check . --fix
black .
```

**Logika:**

1. **Ruff** – prvo automatski ispravlja sintaksu i logičke probleme.
2. **Black** – zatim formatira kod prema strogim stilskim pravilima.

---

## 📁 Konfiguracioni fajlovi

- **`.ruff.toml`** – konfiguracija za Ruff (pravila, ignorisanja, selekcije)
- **`pyproject.toml`** – može da čuva podešavanja za Black (širina linija, ignorisani folderi itd.)

**Primer `.ruff.toml`:**

```toml
line-length = 88
target-version = "py310"
select = ["E", "F", "W"]
ignore = ["E501"]
```

**Primer `pyproject.toml` za Black:**

```toml
[tool.black]
line-length = 88
target-version = ['py310']
skip-string-normalization = true
```

---

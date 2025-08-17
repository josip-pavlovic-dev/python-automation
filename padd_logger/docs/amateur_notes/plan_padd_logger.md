# Plan za Dan 1 – `plan_padd_logger.md`

### **🎯 Cilj dana**

Postaviti osnove projekta po TDD-light pristupu:

- Napraviti osnovnu strukturu (`src/`, `tests/`, `docs/`)
- Napisati prve pytest testove za logger
- Implementirati minimalnu verziju loggera koja prolazi te testove
- Postaviti temelje dokumentacije (`cheatsheet.md` + `line_by_line.md`)

---

### **📂 Struktura projekta**

```
padd_logger/
│
├── src/
│   ├── logger.py
│
├── tests/
│   ├── test_logger.py
│
├── docs/
│   ├── README.md
│   ├── cheatsheet.md
│   ├── line_by_line.md
│
├── requirements-dev.txt
└── .gitignore
```

---

### **🕒 Raspored – 18:30 start**

**18:30 – 18:45** → Pregled ciljeva i strukture projekta

- Otvori `structure.txt` i prilagodi ga novom imenu `padd_logger`
- Inicijalni `git commit` sa praznim fajlovima

**18:45 – 19:30** → Pisanje prvih testova (`tests/test_logger.py`)

- Test: kreiranje logger instance
- Test: logovanje u konzolu
- Test: logovanje u fajl

**19:30 – 20:15** → Implementacija minimalnog `logger.py`

- Samo onoliko koda koliko je potrebno da testovi prođu
- Pokretanje `pytest` i ispravke dok sve ne prođe

**20:15 – 20:30** → Pauza (istezanje, hodanje)

**20:30 – 21:00** → Dodavanje novih testova (edge case-ovi)

- Greške, izuzeci, nepostojeći fajl
- Testiranje sa različitim formatima

**21:00 – 21:45** → Refaktor koda

- Čišćenje duplikata
- Formatiranje sa `ruff` i `black`

**21:45 – 22:15** → Dokumentacija

- `cheatsheet.md` – kratak pregled upotrebe loggera
- `line_by_line.md` – objašnjenje ključnih delova koda (Amateur mod)

**22:15 – 22:30** → Commit i push na GitHub

**22:30 – 22:45** → Kratka refleksija i update `daily_log`

---

# Raspoređivanje i pakovanje: Task Scheduler/cron, python -m, struktura projekta (L16)

## Ishodi učenja
- Razumeš osnovne načine zakazivanja i pokretanja skripti.
- Znaš čemu služi `python -m` i organizacija `src/` projekta.
- Znaš kako da pripremiš skriptu za periodično pokretanje.

## Pojmovi
- Task Scheduler/cron, `python -m`, entry point, struktura projekta

## Teorija (sa primerima)

Pokretanje modula:
```bash
python -m package.module
```

Struktura projekta (primer):
```
project/
├── src/
│   └── mytool/
│       ├── __init__.py
│       └── cli.py  # sadrži main()
└── tests/
```

Zakazivanje:
- Windows Task Scheduler: pozovi `python path\to\script.py` u zadato vreme.
- Linux cron: `0 8 * * * /usr/bin/python /path/script.py`


## Napomene — na šta obratiti pažnju
- Loguj svaki periodični job i čuvaj izveštaje sa datumom u nazivu.
- Razdvajaj konfiguraciju od koda (npr. JSON/YAML fajlovi).

## Najčešće greške
- Neodređen radni direktorijum pri zakazanom pokretanju.
- Nepostojanje logova otežava dijagnostiku.

## Mini-zadaci (vezbaj u svom projektu)
- Napraviti dnevni job koji skenira direktorijum i pravi JSON izveštaj sa statistikama.
- Dokumentovati komandu za pokretanje i očekivane izlaze.

## Kviz (L16)
- Čemu služi `python -m`?
- Šta je razlika između Task Scheduler-a i cron-a?
- Zašto je važno logovanje kod periodičnih poslova?


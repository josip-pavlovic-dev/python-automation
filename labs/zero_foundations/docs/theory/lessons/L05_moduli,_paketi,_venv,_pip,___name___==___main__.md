# Moduli, paketi, venv, pip, __name__ == __main__ (L05)

## Ishodi učenja
- Znaš da koristiš `venv` i `pip`.
- Razumeš module i pakete; znaš kako radi `import`.
- Razumeš `__name__ == "__main__"` čuvara.

## Pojmovi
- `venv`, `pip`, modul, paket, `__init__.py`, `PYTHONPATH`, `__name__ == "__main__"`

## Teorija (sa primerima)

Virtuelno okruženje:
```bash
python -m venv .venv
# aktivacija (Win Bash)
source .venv/Scripts/activate
pip install requests
```

Moduli i paketi:
- fajl `mod.py` je modul; folder sa `__init__.py` je paket.
- `import pkg.mod` ili `from pkg.mod import func`.

`__name__ == "__main__"`:
```python
def main():
    print("pokrenuto kao skripta")

if __name__ == "__main__":
    main()
```


## Napomene — na šta obratiti pažnju
- Uvijek koristi `venv` u projektu.
- Jasna struktura `src/` i odvojeni testovi olakšavaju import i održavanje.

## Najčešće greške
- Mešanje sistemskih i projektnog paketa zbog neaktivnog `venv`.
- Relativni importi bez potrebe — preferiraj apsolutne u većim projektima.

## Mini-zadaci (vezbaj u svom projektu)
- Kreiraj `venv`, instaliraj `requests` i napiši kratku skriptu koja ispisuje verziju.
- Napravi paket `tools/` sa modulom `greet.py` i funkcijom `hello(name)`.

## Kviz (L05)
- Čemu služi `venv`?
- Kako sistem zna da je folder paket?
- Zašto koristimo `if __name__ == "__main__":` čuvara?


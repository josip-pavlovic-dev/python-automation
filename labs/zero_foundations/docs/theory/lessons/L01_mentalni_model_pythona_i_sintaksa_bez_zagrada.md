# Mentalni model Pythona i sintaksa bez zagrada (L01)

## Ishodi učenja
- Razumeš da Python koristi uvlaku umesto zagrada za blokove.
- Razumeš dinamičko tipiziranje i koncept „truthiness“ (tačno/lažno vrednovanje).
- Znaš da pokreneš Python REPL i izvršiš skriptu iz komandne linije.

## Pojmovi
- REPL, interpretirani jezik, uvlaka (indentation), `None`, `True/False`, truthy/falsy

## Teorija (sa primerima)

Python za definisanje blokova koristi **dvotačku i uvlaku** (najčešće 4 razmaka):

```python
x = 10
if x > 5:
    print("Veće od 5")  # uvlaka definise blok
```

Promenljive ne zahtevaju eksplicitno navođenje tipa (dinamičko tipiziranje):
```python
x = 3       # int
x = "tri"   # sada str
```

„Truthiness“: sledeće se ponaša kao `False`: `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None`.
Sve ostalo je `True`:
```python
if []:
    print("istina")
else:
    print("prazna lista je falsy")
```

Pokretanje:
- Interaktivno: `python`
- Skripta: `python path/do/skripte.py`


## Napomene — na šta obratiti pažnju
- Standard je uvlaka od 4 razmaka (ne mešaj tabove i razmake).
- Imena varijabli su `snake_case`.
- `None` nije isto što i prazna niska `''`.

## Najčešće greške
- Mešanje tabova i razmaka može izazvati `IndentationError`.
- Zaboravljena dvotačka `:` posle `if`, `for`, `def`.

## Mini-zadaci (vezbaj u svom projektu)
- Napiši skriptu koja proverava da li je korisnički unos prazan (falsy) i ispisuje poruku.
- Pokreni skriptu iz terminala i iz REPL-a (importuj je i pozovi funkciju ako je ima).

## Kviz (L01)
- Šta u Pythonu definiše blok koda?
- Navedi tri vrednosti koje su „falsy“.
- Koja je konvencija imenovanja varijabli u Pythonu?
- Koja je razlika između `None` i `''`?


# Fajlovi i putanje: pathlib, open, enkoding, glob (L06)

## Ishodi učenja
- Čitaš i pišeš fajlove bezbedno uz `with`.
- Radiš sa `pathlib.Path` za putanje i glob obrasce.
- Razumeš enkoding (UTF-8) i meta-podatke fajla.

## Pojmovi
- `pathlib.Path`, `open`, kontekst menadžer, enkoding, `glob`, `stat`

## Teorija (sa primerima)

`pathlib`:
```python
from pathlib import Path
p = Path("docs") / "readme.md"
print(p.exists(), p.is_file(), p.suffix)
```

Čitanje/pisanje uz `with`:
```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Zdravo\n")
```

`glob` uz `pathlib`:
```python
for path in Path(".").glob("**/*.py"):
    print(path)
```


## Napomene — na šta obratiti pažnju
- Uvijek navedi `encoding="utf-8"` za tekst fajlove.
- Koristi `Path` umesto ručnog spajanja stringova putanje.

## Najčešće greške
- Zaboravljen `with` → curenje resursa.
- Mešanje apsolutnih i relativnih putanja bez kontrole radnog direktorijuma.

## Mini-zadaci (vezbaj u svom projektu)
- Napiši skener koji broji redove u svim `.py` fajlovima (rekurzivno).
- Izlistaj sve fajlove veće od 1 MB u datoj putanji.

## Kviz (L06)
- Zašto koristiti `with open(...)`?
- Koja je razlika `Path.is_file()` i `Path.is_dir()`?
- Zašto navodimo `encoding="utf-8"`?


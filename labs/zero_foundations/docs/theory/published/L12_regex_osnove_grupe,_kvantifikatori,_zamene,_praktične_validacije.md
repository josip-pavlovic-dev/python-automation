# Regex osnove: grupe, kvantifikatori, zamene, praktične validacije (L12)

## Ishodi učenja
- Razumeš osnovnu sintaksu regex-a i grupisanje.
- Znaš da koristiš `re.findall` i `re.sub`.
- Možeš validirati i preimenovati fajlove pomoću regex-a.

## Pojmovi
- `re`, grupa, kvantifikator, sidra (`^`, `$`), klase karaktera (`\d`, `\w`), flagovi

## Teorija (sa primerima)

Primeri:
```python
import re
m = re.findall(r"\d+", "abc123def45")  # ['123','45']

# Grupa i zamena
s = re.sub(r"(\d{{4}})-(\d{{2}})-(\d{{2}})", r"\3.\2.\1", "2025-08-16")
# '16.08.2025'
```


## Napomene — na šta obratiti pažnju
- Koristi raw string `r"..."` da izbegneš dupliranje bekslasheva.
- Počni od jednostavnijih obrazaca i postepeno ih proširuj.

## Najčešće greške
- Preopšti regex koji hvata i neželjene podnizove.
- Zaboravljene granice reči/reda (`\b`, `^`, `$`) kada su potrebne.

## Mini-zadaci (vezbaj u svom projektu)
- Validiraj imena fajlova oblika `report_YYYYMMDD.txt`.
- Iz stringa izvući sve email adrese i normalizovati ih na mala slova.

## Kviz (L12)
- Čemu služe sidra `^` i `$`?
- Zašto je koristan `r"..."` oblik stringa u regex izrazima?
- Navedi primer kvantifikatora.


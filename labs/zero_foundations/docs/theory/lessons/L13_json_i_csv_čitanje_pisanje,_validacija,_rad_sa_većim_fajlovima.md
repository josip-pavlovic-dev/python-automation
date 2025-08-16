# JSON i CSV: čitanje/pisanje, validacija, rad sa većim fajlovima (L13)

## Ishodi učenja
- Čitaš i pišeš JSON i CSV u Pythonu.
- Razumeš rad sa većim fajlovima (streaming, linija po linija).
- Možeš validirati ulazne podatke pre obrade.

## Pojmovi
- `json`, `csv`, `DictReader/Writer`, validacija, streaming

## Teorija (sa primerima)

JSON:
```python
import json
data = {"name":"Ana","age":30}
with open("user.json","w",encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

CSV:
```python
import csv
with open("users.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name","age"])
    w.writeheader()
    w.writerow({"name":"Ana","age":30})
```


## Napomene — na šta obratiti pažnju
- Koristi `newline=""` uz `csv` na Windows-u.
- Za velike fajlove čitaj liniju po liniju umesto da sve učitaš u memoriju.

## Najčešće greške
- Zaboravljen `ensure_ascii=False` → loši dijakritici u JSON-u.
- Nepodudaranje `fieldnames` i ključeva u CSV redovima.

## Mini-zadaci (vezbaj u svom projektu)
- Napravi konverter CSV→JSON sa validacijom obaveznih kolona.
- Za JSON listu korisnika generiši CSV izveštaj.

## Kviz (L13)
- Zašto koristiti `newline=""` sa `csv`?
- Kako čuvati Unicode ispravno u JSON-u?
- Koja je uloga `DictWriter.writeheader()`?


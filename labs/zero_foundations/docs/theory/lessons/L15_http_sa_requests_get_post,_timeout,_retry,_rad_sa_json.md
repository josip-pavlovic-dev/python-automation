# HTTP sa requests: GET/POST, timeout, retry, rad sa JSON (L15)

## Ishodi učenja
- Znaš da šalješ GET/POST zahteve sa `requests`.
- Razumeš timeout i osnovni retry obrazac.
- Možeš da obradiš JSON odgovor i greške.

## Pojmovi
- `requests`, GET, POST, status kod, timeout, retry, `response.json()`

## Teorija (sa primerima)

Osnovni GET:
```python
import requests
r = requests.get("https://httpbin.org/get", timeout=5)
r.raise_for_status()
data = r.json()
```

Jednostavan retry:
```python
for _ in range(3):
    try:
        r = requests.get("https://example.com/api", timeout=5)
        r.raise_for_status()
        break
    except requests.RequestException:
        continue
```


## Napomene — na šta obratiti pažnju
- Uvek postavi `timeout`.
- Proveravaj `status_code` ili koristi `raise_for_status()`.

## Najčešće greške
- Nikad bez timeout-a — skripta može „visiti“.
- Nepokriveni izuzeci pri mrežnim greškama.

## Mini-zadaci (vezbaj u svom projektu)
- Napravi skriptu koja preuzima JSON sa javnog API-ja i čuva kao fajl sa datumom.
- Dodaj osnovni retry i logovanje grešaka.

## Kviz (L15)
- Zašto je važno postaviti `timeout`?
- Kako dobijaš Python dict iz JSON odgovora?
- Kako elegantno obradiš HTTP grešku?


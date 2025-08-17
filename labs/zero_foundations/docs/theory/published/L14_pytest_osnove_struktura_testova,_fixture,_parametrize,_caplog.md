# pytest osnove: struktura testova, fixture, parametrize, caplog (L14)

## Ishodi učenja
- Znaš da postaviš i pokreneš `pytest`.
- Razumeš osnovne asertacije i fixture (`tmp_path`, `caplog`).
- Znaš da parametrizuješ testove.

## Pojmovi
- `pytest`, discovery, `assert`, fixture, `parametrize`, `caplog`, `tmp_path`

## Teorija (sa primerima)

Primer testa:
```python
# test_math.py
def add(a,b): return a+b

def test_add_basic():
    assert add(2,3) == 5
```

Parametrizacija:
```python
import pytest

@pytest.mark.parametrize("a,b,exp", [(1,2,3),(0,0,0),(-1,1,0)])
def test_add_param(a,b,exp):
    assert add(a,b) == exp
```


## Napomene — na šta obratiti pažnju
- Ime fajla `test_*.py` i funkcije `test_*`.
- Fixture `tmp_path` za privremene direktorijume, `caplog` za hvatanje logova.

## Najčešće greške
- Test koji zavisi od globalnog stanja ili reda izvršavanja.
- Previše „krhki“ testovi — testiraj ponašanje, ne implementaciju.

## Mini-zadaci (vezbaj u svom projektu)
- Napiši testove za `Timer` klasu (trajanje > 0 posle sleep).
- Testiraj da `AppLogger` ne duplira handler-e (uz `caplog`).

## Kviz (L14)
- Kako `pytest` otkriva testove?
- Za šta služe `tmp_path` i `caplog`?
- Šta radi `@pytest.mark.parametrize`?


# Kolekcije: list/tuple/set/dict, slicing, komprehencije (L04)

## Ishodi učenja
- Razlikuješ list/tuple/set/dict i znaš osnovne operacije.
- Razumeš slicing i komprehencije.
- Znaš kada koristiti koju kolekciju.

## Pojmovi
- lista, torka (tuple), skup (set), rečnik (dict), slicing, comprehensions

## Teorija (sa primerima)

**Liste** su promenljive (mutable):
```python
xs = [1,2,3]; xs.append(4)
```

**Torke** su nepromenljive (immutable):
```python
pt = (10, 20)
```

**Set** uklanja duplikate i nema poredak:
```python
s = {1,2,2,3}  # {1,2,3}
```

**Dict** drži parove ključ→vrednost:
```python
cfg = {"level": "INFO", "file": "app.log"}
```

**Slicing** i **komprehencije**:
```python
xs = [0,1,2,3,4]
print(xs[1:4])      # [1,2,3]
squares = [x*x for x in xs if x%2==0]
```


## Napomene — na šta obratiti pažnju
- Za jedinstvene elemente bez poretka koristi `set`.
- Za mapiranja koristi `dict` (ključ treba da bude hashable).

## Najčešće greške
- Zamena liste tokom iteracije — oprez sa brisanjem unutar `for` petlje.
- Zbunjenost oko slicing granica (desna granica je ekskluzivna).

## Mini-zadaci (vezbaj u svom projektu)
- Iz liste `[1,2,2,3,3,3]` napravi listu jedinstvenih brojeva rastuće.
- Rekonstruši dict rečniku: iz `['a:1','b:2']` napravi `{'a':1,'b':2}`.

## Kviz (L04)
- Koja je razlika između liste i torke?
- Za šta je `set` koristan?
- Šta radi `xs[1:4]` ako je `xs=[0,1,2,3,4]`?


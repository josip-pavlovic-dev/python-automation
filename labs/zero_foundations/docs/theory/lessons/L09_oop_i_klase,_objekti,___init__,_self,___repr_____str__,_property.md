# OOP I: klase, objekti, __init__, self, __repr__/__str__, property (L09)

## Ishodi učenja
- Razumeš klasu, objekat, `__init__`, `self`, atribute.
- Znaš razliku `__repr__` i `__str__`.
- Umeš da dodaš `@property` za kontrolisan pristup.

## Pojmovi
- klasa, objekat, konstruktor, `self`, atributi instance, `__repr__`, `__str__`, `@property`

## Teorija (sa primerima)

Osnovna klasa:
```python
class Timer:
    def __init__(self):
        self._start = None
        self._end = None

    def start(self):
        import time
        self._start = time.time()

    def stop(self):
        import time
        self._end = time.time()

    @property
    def duration(self):
        if self._start is None or self._end is None:
            return 0.0
        return self._end - self._start

    def __repr__(self):
        return f"Timer(start={self._start}, end={self._end})"
```


## Napomene — na šta obratiti pažnju
- Uvek stavi `self` kao prvi parametar metoda instance.
- `__repr__` je za developera (nedvosmislen), `__str__` za korisnički prikaz.

## Najčešće greške
- Zaboravljen `self` u potpisu metoda.
- Korišćenje atributa bez prethodne inicijalizacije u `__init__`.

## Mini-zadaci (vezbaj u svom projektu)
- Dodaj metodu `reset()` koja poništava tajmer.
- Napiši malu klasu `Point(x,y)` sa `distance_to(other)` metodom.

## Kviz (L09)
- Koja je uloga `self`?
- Razlika između `__repr__` i `__str__`?
- Šta vraća `duration` ako tajmer nije pokrenut i zaustavljen?


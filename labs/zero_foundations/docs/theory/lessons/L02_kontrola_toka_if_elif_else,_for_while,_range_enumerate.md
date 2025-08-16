# Kontrola toka: if/elif/else, for/while, range/enumerate (L02)

## Ishodi učenja
- Razlikuješ `if/elif/else`, `for` i `while`.
- Znaš da koristiš `range()` i `enumerate()`.
- Razumeš `break` i `continue`.

## Pojmovi
- `if/elif/else`, `for`, `while`, `range`, `enumerate`, `break`, `continue`, `pass`

## Teorija (sa primerima)

`if/elif/else` primer:
```python
n = 7
if n % 2 == 0:
    print("paran")
elif n % 3 == 0:
    print("deljiv sa 3")
else:
    print("neparan i nije deljiv sa 3")
```

`for` iterira preko **iterabila**:
```python
for ch in "abc":
    print(ch)
```

`range(start, stop, step)`:
```python
for i in range(1, 5):
    print(i)  # 1,2,3,4
```

`enumerate` daje (indeks, vrednost):
```python
xs = ["a","b","c"]
for i, v in enumerate(xs, start=1):
    print(i, v)  # 1 a ...
```


## Napomene — na šta obratiti pažnju
- U Pythonu nema `++/--`; koristi `i += 1`.
- `pass` je „nista“, mesto-držac za prazan blok.

## Najčešće greške
- Beskoonačna `while` petlja bez uslova za izlaz.
- Mešanje `range(5)` (0..4) sa ekskluzivnim `stop`.

## Mini-zadaci (vezbaj u svom projektu)
- Napiši `for` koji ispisuje brojeve 10..1 unazad.
- Upotrebi `enumerate` da odštampaš redne brojeve pored stavki liste.

## Kviz (L02)
- Šta radi `enumerate`?
- Kako dobiti brojeve 0..9 for-petljom bez korišćenja liste?
- Kada je korisno `break`, a kada `continue`?


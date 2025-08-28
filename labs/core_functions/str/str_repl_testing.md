# str() — REPL Testing

## Kako testiram

1. U VS Code terminalu pokreni `python` i testiraj slučajeve ispod.
2. Kopiraj najzanimljivije isečke u _analysis_notes.md_ uz tvoje komentare.

```python
## Osnovni testovi

str(True), str(False)   # 'True', 'False'
str([1,2,3]) # '[1, 2, 3]'


## Dodatni (granice, neobični tipovi, greške)

class P:
    def __str__(self): return "pretty"
    def __repr__(self): return "debug"

p = P()
str(p) # 'pretty'

# Fallback na **repr** ako **str** ne postoji

class Q:
    def **repr**(self): return "Q(...)"

str(Q()) # 'Q(...)'

```

---

## REPL – fokus na razlike str() / repr() / decode()

```bash
>>> str(b"abc")
"b'abc'"       # str(bytes) daje repr bytes-a

>>> (b"abc").decode("utf-8")
'abc'          # decode pretvara bytes -> stvarni tekst

>>> s = "line1\nline2"
>>> print(s)
line1
line2
>>> str(s)
'line1\nline2' # str() čuva stvarne \n karaktere; print renderuje novi red

>>> class A: pass
>>> str(A())             # fallback na <A object at 0x...>
'<__main__.A object at 0x...>'

>>> class B:
...     def __str__(self): return "B::pretty"
...
>>> str(B())
'B::pretty'
```

### Pitanja za razmišljanje

- Kada tačno koristiti `decode()` umesto `str()`?
- Kako da proveriš da li objekat ima smislen **str**?
- Kada koristiti `f"{x:.2f}"` ili `format(x, ".2f")` umesto `str(x)`?
- Zašto je `str(bytes)` često znak da ti treba dekodiranje?

---

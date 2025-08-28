    # len() — Cheatsheet

    **Definicija (kratko):** Vraća dužinu/ukupan broj elemenata sekvence ili kolekcije.

    **Potpis (signature):**
    ```python
    len(obj) -> int  # obj mora imati __len__
    ```

    **Vraća:** int

    ## ✅ Brze činjenice
    - Radi za `str, list, tuple, dict, set, range, bytes, bytearray`, …
- Za custom klase implementirati `__len__` (mora vratiti `int >= 0`).

    ## 🔎 Najčešći primeri
    ```python
    len('abc')      # 3
len([1,2,3])    # 3
len({'a': 1})   # 1

class Bag:
    def __init__(self, items): self.items = items
    def __len__(self): return len(self.items)
len(Bag([1,2,3]))   # 3

    ```

    ## ⚠️ Tipične greške
    - Pogrešan tip argumenta (vidi `help(len)` za očekivane tipove).
    - Mešanje `str` literala i numeričkih vrednosti pri radu sa bazama (za `len()` ovo je česta zamka).
    - Previše oslanjanja na implicitne konverzije — radije testiraj eksplicitno u REPL-u.

    ## 🛠️ Diagnostika u REPL-u
    ```python
    help(len)
    dir(len)
    len.__doc__
    ```

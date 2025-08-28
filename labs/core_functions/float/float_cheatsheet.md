    # float() — Cheatsheet

    **Definicija (kratko):** Konvertuje vrednost u pokretni zarez (IEEE 754).

    **Potpis (signature):**
    ```python
    float(x=0.0) -> float
    ```

    **Vraća:** float

    ## ✅ Brze činjenice
    - `float('inf')`, `float('-inf')`, `float('nan')`
- 0.1 + 0.2 != 0.3 zbog binarne reprezentacije; koristi `math.isclose`.
- Povezano: `__float__`.

    ## 🔎 Najčešći primeri
    ```python
    float(10)      # 10.0
float('3.14')  # 3.14
float('inf'), float('nan')

    ```

    ## ⚠️ Tipične greške
    - Pogrešan tip argumenta (vidi `help(float)` za očekivane tipove).
    - Mešanje `str` literala i numeričkih vrednosti pri radu sa bazama (za `float()` ovo je česta zamka).
    - Previše oslanjanja na implicitne konverzije — radije testiraj eksplicitno u REPL-u.

    ## 🛠️ Diagnostika u REPL-u
    ```python
    help(float)
    dir(float)
    float.__doc__
    ```

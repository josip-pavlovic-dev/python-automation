    # float() — REPL Testing

    ## Kako testiram
    1. U VS Code terminalu pokreni `python` i testiraj slučajeve ispod.
    2. Kopiraj najzanimljivije isečke u *analysis_notes.md* uz tvoje komentare.

    ## Osnovni testovi
    ```py
    float(1), float(True), float(False)  # 1.0, 1.0, 0.0
float('1e-3')                        # 0.001

    ```

    ## Dodatni (granice, neobični tipovi, greške)
    ```py
    import math
math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)   # False
math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-8)   # True (zavisi)

    ```

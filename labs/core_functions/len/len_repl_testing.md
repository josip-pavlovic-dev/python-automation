    # len() — REPL Testing

    ## Kako testiram
    1. U VS Code terminalu pokreni `python` i testiraj slučajeve ispod.
    2. Kopiraj najzanimljivije isečke u *analysis_notes.md* uz tvoje komentare.

    ## Osnovni testovi
    ```py
    len(''), len('hi')          # 0, 2
len([]), len([1,2])         # 0, 2
len({'a':1,'b':2})          # 2

    ```

    ## Dodatni (granice, neobični tipovi, greške)
    ```py
    class Bad:
    def __len__(self): return -1  # loše (treba >= 0)
# len(Bad())  # TypeError u novijim verzijama (ili undefined behavior)

    ```

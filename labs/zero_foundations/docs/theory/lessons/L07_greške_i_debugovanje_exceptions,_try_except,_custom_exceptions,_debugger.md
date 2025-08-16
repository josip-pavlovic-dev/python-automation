# Greške i debugovanje: exceptions, try/except, custom exceptions, debugger (L07)

## Ishodi učenja
- Razumeš mehanizam izuzetaka i kako da ih hvataš/specifično obrađuješ.
- Znaš da podigneš (raise) sopstveni izuzetak.
- Znaš osnovno korišćenje debuggera (VS Code).

## Pojmovi
- exception, `try/except/else/finally`, `raise`, `pdb`, breakpoint

## Teorija (sa primerima)

`try/except`:
```python
try:
    x = int("abc")
except ValueError as e:
    print("Nije broj", e)
else:
    print("Sve ok" )
finally:
    print("All done")
```

Custom izuzetak:
```python
class ConfigError(Exception):
    pass

def load_cfg(path: str):
    if not path.endswith('.json'):
        raise ConfigError("Očekivan .json fajl")
```


## Napomene — na šta obratiti pažnju
- Uvek hvataj **najkonkretniji** izuzetak koji očekuješ.
- Koristi debugger: postavi breakpoint i idi `step over / into`.

## Najčešće greške
- Preširok `except Exception:` bez potrebe – maskira greške.
- „Tihi“ `except` koji ne loguje problem.

## Mini-zadaci (vezbaj u svom projektu)
- Napiši funkciju koja učitava broj iz stringa i vraća `None` ako nije validan (bez bacanja).
- Kreiraj sopstveni izuzetak za nepostojeći fajl konfiguracije i testiraj ga.

## Kviz (L07)
- Koja je razlika `except ValueError` i `except Exception`?
- Čemu služi blok `finally`?
- Kako dodaš breakpoint u VS Code-u?


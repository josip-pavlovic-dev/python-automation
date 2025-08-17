# CLI sa argparse: argumenti, flagovi, validacija, exit kodovi (L11)

## Ishodi učenja
- Znaš da napraviš CLI sa argumentima i flagovima.
- Razumeš validaciju i poruke pomoći.
- Znaš šta je exit kod.

## Pojmovi
- `argparse`, argument (pozicioni/opsioni), flag, `--help`, exit code

## Teorija (sa primerima)

Osnovni CLI:
```python
import argparse

parser = argparse.ArgumentParser(prog="file-reporter", description="Izveštaj o fajlovima")
parser.add_argument("path", help="Putanja do direktorijuma")
parser.add_argument("--pattern", default="*.py", help="Glob obrazac")
parser.add_argument("--verbose", action="store_true", help="Detaljniji izlaz")
args = parser.parse_args()

print(args.path, args.pattern, args.verbose)
```


## Napomene — na šta obratiti pažnju
- Uvijek obezbedi `--help` opis koji je stvarno koristan.
- Koristi exit kodove (`sys.exit(0/1)`) za uspeh/neuspeh.

## Najčešće greške
- Nedovoljna validacija ulaza — bolji error poruke ubrzavaju korišćenje.
- Predugački nazivi bez kratkih aliasa.

## Mini-zadaci (vezbaj u svom projektu)
- Dodaj `--min-size` (u bajtima) i filtriraj fajlove koji su jednaki ili veći.
- Prikaži ukupan broj obrađenih fajlova i zbirnu veličinu.

## Kviz (L11)
- Koja je razlika izmedju pozicionog i opcionog argumenta?
- Kako aktivirati boolean flag `--verbose` u `argparse`?
- Šta znači exit kod 0?


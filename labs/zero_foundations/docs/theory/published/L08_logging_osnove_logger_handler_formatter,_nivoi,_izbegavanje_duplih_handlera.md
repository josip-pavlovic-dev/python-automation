# Logging osnove: logger/handler/formatter, nivoi, izbegavanje duplih handlera (L08)

## Ishodi učenja
- Razumeš hijerarhiju `logging` objekata: logger, handler, formatter.
- Znaš nivoe logovanja i kada koji koristiti.
- Znaš kako da izbegneš dupliranje handlera.

## Pojmovi
- `logging.getLogger`, nivoi (DEBUG/INFO/WARNING/ERROR/CRITICAL), handler, formatter, propagation

## Teorija (sa primerima)

Osnovna konfiguracija:
```python
import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logging.info("Pozdrav")
```

Ručna postavka sa handler-om:
```python
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s")
h.setFormatter(f)

# izbegni dupliranje
if not logger.handlers:
    logger.addHandler(h)

logger.debug("Debug poruka")
```


## Napomene — na šta obratiti pažnju
- Propagation šalje log poruke roditeljskim logger-ima — kontroliši ga po potrebi (`logger.propagate=False`).
- Nemoj dodavati handler-e više puta — proveri `if not logger.handlers:`.

## Najčešće greške
- Korišćenje `basicConfig` i onda ručno dodavanje handler-a bez razumevanja — duplikati.
- Previsok nivo (npr. WARNING) pa „ne vidiš“ INFO poruke.

## Mini-zadaci (vezbaj u svom projektu)
- Napravi `AppLogger` koji kreira stream/file handler po izboru i vraća spreman logger.
- Napiši test koji proverava da nema duplih handlera posle višestrukih poziva `get_logger()`.

## Kviz (L08)
- Koje su standardne vrednosti nivoa logovanja (od najnižeg)?
- Kako izbeći dupliranje handlera?
- Šta radi `logger.propagate=False`?


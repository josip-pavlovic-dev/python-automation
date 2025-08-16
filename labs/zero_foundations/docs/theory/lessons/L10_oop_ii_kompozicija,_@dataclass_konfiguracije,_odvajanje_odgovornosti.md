# OOP II: kompozicija, @dataclass konfiguracije, odvajanje odgovornosti (L10)

## Ishodi učenja
- Razumeš kompoziciju i zašto je često bolja od nasleđivanja.
- Umeš da koristiš `@dataclass` za konfiguracije.
- Umeš da izdvojiš odgovornosti u manje jedinice.

## Pojmovi
- kompozicija, nasleđivanje, `@dataclass`, separacija odgovornosti (SoC), injekcija zavisnosti

## Teorija (sa primerima)

`@dataclass` za konfiguraciju:
```python
from dataclasses import dataclass

@dataclass
class LogConfig:
    level: str = "INFO"
    to_file: bool = False
    filename: str = "app.log"
```

Kompozicija (`AppLogger` koristi `logging.Logger`):
```python
import logging

class AppLogger:
    def __init__(self, cfg: LogConfig):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(getattr(logging, cfg.level))
        if not self.logger.handlers:
            h = logging.FileHandler(cfg.filename) if cfg.to_file else logging.StreamHandler()
            f = logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s")
            h.setFormatter(f)
            self.logger.addHandler(h)
```


## Napomene — na šta obratiti pažnju
- Kompozicija = klasa koristi druge objekte umesto da ih nasleđuje.
- `@dataclass` smanjuje šablonski kod (init/eq/repr).

## Najčešće greške
- Preuranjeno nasleđivanje bez realne potrebe.
- Tvrdo-kodiranje zavisnosti umesto injekcije (npr. handler/factory).

## Mini-zadaci (vezbaj u svom projektu)
- Proširi `LogConfig` sa poljem `fmt` i primeni ga u `AppLogger`.
- Izvedi mali DI: ubaci fabričku funkciju koja pravi handler na osnovu konfiguracije.

## Kviz (L10)
- Zašto često biramo kompoziciju umesto nasleđivanja?
- Šta ti `@dataclass` automatski generiše?
- Kako bi izveo injekciju zavisnosti za `handler`?


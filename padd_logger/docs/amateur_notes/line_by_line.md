# 1) `LogConfig` polje‑po‑polje

## a) `file_path: Optional[Union[str, os.PathLike]]`

**Objašnjenje.**
Ako je zadato (`str` ili `PathLike`), dodaće se **file handler**; inače se fajl ne koristi. Tip je fleksibilan: radi i sa `pathlib.Path`. (L45–L45)&#x20;

**Mikro‑primer.**

```python
from pathlib import Path
cfg = LogConfig(file_path=Path("logs/app.log"))  # prihvata i Path
```

**Tipične greške.**

- Prosleđivanje foldera umesto pune putanje do fajla.
- Oslanjanje na relativni path bez kreiranog foldera (ovde je rešeno, vidi §3).

**Mini‑zadatak.**
Postavi `file_path` na `Path("var/log/my_tool/log.txt")` i objasni šta se dešava ako parent folder ne postoji.

---

## b) `rotating / max_bytes / backup_count`

**Objašnjenje.**
`rotating=True` bira `RotatingFileHandler`; granica po segmentu je `max_bytes`, a broj rezervnih segmenata `backup_count`. Ako je `rotating=False`, ova dva polja se ignorišu. (L46–L48)&#x20;

**Mikro‑primer.**

```python
cfg = LogConfig(file_path="logs/app.log", rotating=True,
                max_bytes=2_000_000, backup_count=5)
```

**Tipične greške.**

- Podešavanje `rotating=True` bez smislenog `max_bytes` (previše malo → stalna rotacija; previše veliko → „naduvan“ fajl).
- Očekivanje da će rotacija obrisati stare fajlove posle `backup_count` ako je sistem „lockovao“ fajl (npr. AV skener).

**Mini‑zadatak.**
Predloži vrednosti `max_bytes` i `backup_count` za CLI alat koji dnevno napravi \~4 MB logova i zadrži istoriju 7 dana.

---

## c) `fmt_console` vs `fmt_file`

**Objašnjenje.**

- `fmt_console`: sažet, „human‑friendly“ raspored (vreme, nivo, ime logera, poruka). (L50–L51)&#x20;
- `fmt_file`: strožiji, delimiter `|`, plus `filename:lineno` za precizno praćenje izvora; pogodniji za mašinsko parsiranje. (L51–L51)&#x20;

**Mikro‑primer.**

```python
cfg = LogConfig(
    fmt_console="[%(asctime)s] %(levelname)s %(name)s: %(message)s",
    fmt_file="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
)
```

**Tipične greške.**

- Korišćenje istog ultra‑detaljnog formata i za konzolu → previše šuma.
- Menjanje redosleda polja u fajlu pa regex/ingest pravila više ne rade.

**Mini‑zadatak.**
Napiši regex koji iz `fmt_file` hvata `timestamp`, `level`, `name`, `fileline` i `message`.

---

## d) `datefmt`

**Objašnjenje.**
Jedan `datefmt` važi za **oba** handlera. Trenutno je `"%Y-%m-%d %H:%M:%S"` — čitljivo, stabilno za sortiranje; po potrebi možeš preći na ISO‑8601 sa milisekundama u **format stringu** (`%(msecs)03d`). (L52–L52)&#x20;

**Mikro‑primer (ISO‑ish, opciono):**

```python
cfg = LogConfig(
    datefmt="%Y-%m-%dT%H:%M:%S",
    fmt_file="%(asctime)s.%(msecs)03d | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
)
```

**Tipične greške.**

- Očekivanje milisekundi iz samog `datefmt` (one dolaze iz `%(msecs)` u **formatu**, ne iz `datefmt`).
- Mešanje lokalnog vremena i UTC bez jasne politike.

**Mini‑zadatak.**
Izmeni formate tako da dobijemo `YYYY‑MM‑DDTHH:MM:SS.mmm` u **oba** handlera, bez prelaska na UTC.

---

# 2) `configure_logger(cfg)` — idempotentnost, propagate, redosled handlera

**Idempotentnost (no‑reset).**
Ako logger već ima handlere i `reset=False`, funkcija **odmah vraća** logger — sprečava dupliranje handlera. (L69–L71)&#x20;

**Reset grana.**
Ako je `reset=True`, svi postojeći handleri se uklanjaju i lista se čisti — „čisto“ stanje za novu konfiguraciju (pytest‑friendly). (L73–L78)&#x20;

**Propagate.**
`logger.propagate = cfg.propagate` sprečava odlazak record‑a ka ancestor loggerima (npr. root) ako je `False` (što je i podrazumevano). (L66–L67, L54) &#x20;

**Redosled dodavanja handlera.**
Prvo se (uslovno) doda **console handler**, zatim (uslovno) **file handler**. Redosled nije kritičan za ispis, ali je pregledan i konsekventan. (L79–L88; L90–L95/101) &#x20;

**Mikro‑primer.**

```python
log = configure_logger(LogConfig(name="x", reset=False))
# drugi poziv bez reset-a neće duplirati handlere
log = configure_logger(LogConfig(name="x", reset=False))
# test reset-a:
log = configure_logger(LogConfig(name="x", reset=True))
```

**Tipične greške.**

- Višestruko pozivanje konfiguracije bez idempotentne zaštite → dupli zapisi.
- Zaboravljen `propagate=False` pa root takođe loguje → duplikati.

**Mini‑zadatak.**
Objasni šta će `configure_logger(...)` uraditi u tri uzastopna poziva: (1) `reset=False`, (2) `reset=False`, (3) `reset=True`.

---

# 3) File handler — folder, `encoding="utf-8"`, bez boja

**Kreiranje foldera.**
Pre otvaranja fajla kreira se parent direktorijum: `os.makedirs(os.path.dirname(file_path_str) or ".", exist_ok=True)`. (L31–L33)&#x20;

**Rotating vs običan i `utf-8`.**

- Ako je `rotating=True`, koristi se `RotatingFileHandler(..., encoding="utf-8")`; inače `FileHandler(..., encoding="utf-8")`. (L34–L39)&#x20;
- Na kraju se postavlja **običan** `Formatter` (bez boja) sa `fmt_file` i `datefmt`. (L41–L43)&#x20;

**Zašto „bez boja“?**
Color sekvence (ANSI) bi kontaminirale .log fajl i otežale parsiranje/gledanje u editorima. Ovde je to ispravno rešeno korišćenjem **standardnog** formattera. (L42–L43)&#x20;

**Mikro‑primer.**

```python
cfg = LogConfig(file_path="logs/run.log", rotating=False)
log = configure_logger(cfg)
log.info("Upis u fajl je UTF-8 i bez boja.")
```

**Tipične greške.**

- Nedostatak `encoding="utf-8"` → problemi sa našim slovima/emoji.
- Deljenje istog `ColorFormatter` i na fajl handleru.
- Nepravljenje foldera → `FileNotFoundError` (ovde pokriveno).

**Mini‑zadatak.**
Dokaži (bez pokretanja) na osnovu koda da file handler **nikad** ne koristi boje.

---

# 4) Console handler — TTY detekcija i `_ColorFormatter`

**Dodavanje console handlera.**
Kreira se `StreamHandler(sys.stdout)`, postavlja nivo i bira formatter:

- ako **i** `console_use_color` **i** `_stream_supports_color(stream)` → koristi se `_ColorFormatter`;
- inače običan `Formatter`. (L80–L88)&#x20;

**Detekcija TTY.**
`_stream_supports_color` proverava da li stream ima `isatty()` i da li vraća `True`; na izuzetak vraća `False`. (L48–L53)&#x20;

**Bojenje samo LEVEL tokena.**
`_ColorFormatter` u `format()` privremeno zameni `record.levelname` obojenom varijantom na osnovu mape nivo→ANSI i **vrati ga** na original u `finally` — zato boja ne „curi“ na druge handlere. (L56–L75, L76–L78) &#x20;

**Mikro‑primer.**

```python
cfg = LogConfig(console=True, console_use_color=True)  # boje ako TTY
log = configure_logger(cfg)
log.warning("Ovo će biti žuto u TTY, bez boje kad je redirect.")
```

**Tipične greške.**

- Forsiranje boja bez TTY provere → ANSI „smeti“ u CI/redirect izlazu.
- Bojenje cele poruke umesto samo `LEVEL` → otežano čitanje/copy‑paste.

**Mini‑zadatak.**
Objasni šta se dešava sa bojama kada pokreneš program kao `python app.py > out.txt` i zašto.

---

## (Opciono) Minimalne, praktične dorade

Samo ako želiš da ih uvedeš; ne menjaju semantiku, poboljšavaju ergonomiju:

```diff
@@ class LogConfig:
-    fmt_console: str = "[%(asctime)s] %(levelname)s %(name)s: %(message)s"
-    fmt_file: str = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
-    datefmt: str = "%Y-%m-%d %H:%M:%S"
+    # ISO-ish timestamp sa milisekundama (lakše parsiranje)
+    fmt_console: str = "[%(asctime)s.%(msecs)03d] %(levelname)s %(name)s: %(message)s"
+    fmt_file: str = "%(asctime)s.%(msecs)03d | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
+    datefmt: str = "%Y-%m-%dT%H:%M:%S"
@@ def configure_logger(cfg: LogConfig) -> logging.Logger:
-        if cfg.console_use_color and _stream_supports_color(ch.stream):
+        # Poštuj NO_COLOR=1 u okruženju (standardna konvencija)
+        if (cfg.console_use_color and _stream_supports_color(ch.stream)
+            and not os.environ.get("NO_COLOR")):
             formatter = _ColorFormatter(fmt=cfg.fmt_console, datefmt=cfg.datefmt)
         else:
             formatter = logging.Formatter(fmt=cfg.fmt_console, datefmt=cfg.datefmt)
@@ if cfg.rotating:
-            fh: logging.Handler = logging.handlers.RotatingFileHandler(
-                file_path_str, maxBytes=cfg.max_bytes, backupCount=cfg.backup_count, encoding="utf-8"
-            )
+            fh: logging.Handler = logging.handlers.RotatingFileHandler(
+                file_path_str, maxBytes=cfg.max_bytes, backupCount=cfg.backup_count,
+                encoding="utf-8", delay=True
+            )
@@ else:
-            fh = logging.FileHandler(file_path_str, encoding="utf-8")
+            fh = logging.FileHandler(file_path_str, encoding="utf-8", delay=True)
```

Ako želiš, mogu da primenim ove sitne izmene i pokažem kratki „smoke“ izlaz.

---

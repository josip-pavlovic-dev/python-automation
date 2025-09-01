(Mentor:) Razumem te i izvinjavam se za raniji ton. Fokus: hoćeš **prostan alat** koji prevodi **bilo koji .txt fajl na srpski** bez printanja “ć/č/ž/đ/š” u terminalu. Idemo direktno na stvar — fajl-to-fajl prevod (bez REPL izlaza), sa DeepL ključem iz `.env`.

# REPL & dizajn (šta pravimo)

- CLI: `translate_txt.py --in input.txt --out output.txt --target SR`
- Ne štampa sadržaj u terminal (izbegavamo encoding probleme), samo kratke ASCII poruke.
- Radi chunking (<= 4500 karaktera po komadu) da free plan ne puca.
- Učitava `DEEPL_AUTH_KEY` iz:

  1. već postavljenog env-a,
  2. `--env` putanje,
  3. automatski traži `.env` “nagore” od CWD (find_dotenv).

- Opcioni `--source` (npr. EN, DE) – obično nije potreban.
- Opcioni `--dry-run` (ne zove DeepL, već samo kopira ulaz u izlaz da testiraš tok).

# Implementacija (MVP)

**Predložena putanja:** `labs/core_functions/tools/translate_text/translate_txt.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prevedi bilo koji .txt fajl na ciljani jezik koristeći DeepL.
Primeri:
  python translate_txt.py --in in.txt --out out.txt --target SR
  python translate_txt.py --in in.txt --out out.txt --target SR --dry-run
  python translate_txt.py --in in.txt --out out.txt --target SR --env ../../.env
"""

from __future__ import annotations
import argparse
import os
from pathlib import Path
from typing import List

# third-party
import deepl
try:
    from dotenv import load_dotenv, find_dotenv
except Exception:
    load_dotenv = None
    find_dotenv = None


def parse_args(argv=None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Prevedi .txt fajl na ciljani jezik (DeepL)."
    )
    ap.add_argument("--in", dest="inp", required=True, help="ulazni .txt fajl (UTF-8)")
    ap.add_argument("--out", dest="out", required=True, help="izlazni .txt fajl (UTF-8)")
    ap.add_argument("--target", default="SR", help="ciljni jezik (npr. SR, EN-US, DE)")
    ap.add_argument("--source", help="izvorni jezik (npr. EN); obično nije potrebno")
    ap.add_argument("--max-chars", type=int, default=4500, help="max dužina chunk-a")
    ap.add_argument("--dry-run", action="store_true", help="ne zove DeepL; kopira ulaz u izlaz (za test)")
    ap.add_argument("--env", dest="env_file", help="putanja do .env (override autodetekcije)")
    return ap.parse_args(argv)


def resolve_auth_key(env_file: str | None) -> str:
    # 1) Već postavljeno u okruženju?
    key = os.getenv("DEEPL_AUTH_KEY")
    if key:
        return key
    # 2) --env
    if env_file and load_dotenv:
        if not os.path.isfile(env_file):
            raise FileNotFoundError(f"--env fajl ne postoji: {env_file}")
        load_dotenv(env_file, override=False)
        key = os.getenv("DEEPL_AUTH_KEY")
        if key:
            return key
    # 3) find_dotenv
    if find_dotenv and load_dotenv:
        found = find_dotenv(filename=".env", usecwd=True)
        if found:
            load_dotenv(found, override=False)
            key = os.getenv("DEEPL_AUTH_KEY")
            if key:
                return key
    raise RuntimeError("DEEPL_AUTH_KEY nije pronađen (env/--env/.env).")


def chunk_text(text: str, max_chars: int) -> List[str]:
    if len(text) <= max_chars:
        return [text]
    parts, cur, size = [], [], 0
    for line in text.splitlines(keepends=True):
        if size + len(line) > max_chars and cur:
            parts.append("".join(cur))
            cur, size = [], 0
        cur.append(line)
        size += len(line)
    if cur:
        parts.append("".join(cur))
    return parts


def translate_file(inp: Path, out: Path, target: str, source: str | None,
                   max_chars: int, dry_run: bool, env_file: str | None) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    text = inp.read_text(encoding="utf-8")

    if dry_run:
        # Bez kontakta sa DeepL – kopija ulaza u izlaz:
        out.write_text(text, encoding="utf-8")
        print(f"[OK] (dry-run) Kopirano {len(text)} karaktera u {out}")
        return

    key = resolve_auth_key(env_file)
    translator = deepl.Translator(key)

    chunks = chunk_text(text, max_chars)
    outputs: List[str] = []
    for c in chunks:
        if source:
            res = translator.translate_text(c, source_lang=source, target_lang=target)
        else:
            res = translator.translate_text(c, target_lang=target)
        outputs.append(res.text if not isinstance(res, list) else "\n".join(x.text for x in res))

    out.write_text("".join(outputs), encoding="utf-8")
    print(f"[OK] Prevedeno i sačuvano: {out} (ulaz {len(text)} chars, delova {len(chunks)})")


def main(argv=None) -> int:
    args = parse_args(argv)
    inp = Path(args.inp)
    out = Path(args.out)
    if not inp.is_file():
        print(f"[ERR] Ulazni fajl ne postoji: {inp}")
        return 2
    try:
        translate_file(inp, out, target=args.target, source=args.source,
                       max_chars=args.max_chars, dry_run=args.dry_run, env_file=args.env_file)
    except Exception as e:
        # ASCII-only poruka, bez srpskih slova -> lakše za terminal
        print(f"[ERR] Translation failed: {type(e).__name__}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

# QA & testovi (brzi check)

1. Dry-run (ne troši kvotu, samo pipeline provera):

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in some_english.txt \
  --out sr_preview.txt \
  --target SR \
  --dry-run
```

2. Stvarni prevod (traži `DEEPL_AUTH_KEY` – u root `.env` ili `--env`):

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in some_english.txt \
  --out sr_output.txt \
  --target SR
```

3. Ako želiš precizno `--env`:

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in some_english.txt \
  --out sr_output.txt \
  --target SR \
  --env ./../../.env
```

# Docs & wrap

- Ovim si **nezavisno** od help() i REPL-a: bilo koji tekst prevedeš copy/paste → `.txt` → fajl-to-fajl prevod.
- Terminal će ispisati samo kratke ASCII poruke (`[OK] ...`, `[ERR] ...`), dok se sadržaj prevoda sigurno snima u **UTF-8** fajl.
- Ako želiš i “capture help(dict)” → dodatna mini alatka može da upiše `help(obj)` u `help_dump.txt`, pa je proslediš gornjoj skripti. Mogu odmah da isporučim i to (10 linija koda).

### Glossary (dopuna)

- **chunking** – sečenje ulaznog teksta na delove da npr. API/kvote ne “puknu”.
- **dry-run** – probni režim bez realnog prevoda; služi da proveriš tok i fajlove.

Ako hoćeš, dodam i drugi skript: `dump_help.py` (snimi `help(obj)` u `.txt`), pa ga koristiš sa `translate_txt.py`.

---

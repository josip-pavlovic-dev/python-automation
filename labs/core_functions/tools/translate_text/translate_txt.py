#!/usr/bin/env python3
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

# third-party
import deepl

try:
    from dotenv import find_dotenv, load_dotenv
except Exception:
    load_dotenv = None
    find_dotenv = None


def parse_args(argv=None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Prevedi .txt fajl na ciljani jezik (DeepL)."
    )
    ap.add_argument("--in", dest="inp", required=True, help="ulazni .txt fajl (UTF-8)")
    ap.add_argument("--out", dest="out", help="izlazni .txt fajl (default: input_sr.txt)")
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


def chunk_text(text: str, max_chars: int) -> list[str]:
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
    outputs: list[str] = []
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

    if not inp.is_file():
        print(f"[ERR] Ulazni fajl ne postoji: {inp}")
        return 2

    # Ako korisnik nije prosledio --out, generiši automatski
    if args.out:
        out = Path(args.out)
    else:
        out = inp.with_name(inp.stem + "_sr.txt")

    try:
        translate_file(
            inp,
            out,
            target=args.target,
            source=args.source,
            max_chars=args.max_chars,
            dry_run=args.dry_run,
            env_file=args.env_file,
        )
    except Exception as e:
        print(f"[ERR] Translation failed: {type(e).__name__}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

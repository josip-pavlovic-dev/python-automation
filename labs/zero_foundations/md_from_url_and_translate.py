#!/usr/bin/env python
"""
Preuzmi HTML sa URL-a -> konvertuj u Markdown -> prevedi na srpsku latinicu (DeepL).
Čuva dva fajla: <base>.md (EN) i <base>.sr.md (SR).

Upotreba:
    python md_from_url_and_translate.py "https://docs.pytest.org/en/stable/how-to/fixtures.html" -o fixtures

Zahtevi:
    pip install requests html2text deepl python-dotenv
    # u .env: DEEPL_AUTH_KEY=...

Napomene:
- Code fence blokovi (``` ... ```) se NE prevode (očuvanje koda).
- Limiti DeepL API-ja: duži tekst se lomi u manje delove (bez prekidanja code blokova).

Autor: ZF-14 · Mentor Central
"""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Iterable, List, Tuple
from urllib.parse import urlparse

import requests
import html2text
from dotenv import load_dotenv

try:
    import deepl  # type: ignore
except Exception:  # pragma: no cover
    deepl = None  # omogućava da skripta pokaže poruku ako paket nije instaliran


def slugify(text: str) -> str:
    """Pretvori tekst u 'Windows-safe' naziv fajla (samo slova, brojevi, ._-)."""
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")
    return text or "index"


def derive_base_from_url(url: str) -> str:
    """Izvuci razuman 'base name' iz URL-a."""
    p = urlparse(url)
    last = Path(p.path).name or Path(p.path).stem
    if not last:
        last = "index"
    return slugify(last.lower())


def fetch_html(url: str, timeout: int = 20) -> str:
    """Preuzmi HTML sa URL-a."""
    headers = {
        "User-Agent": "Mozilla/5.0 (ZF-14/1.0; +https://example.local)"
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def html_to_markdown(html: str) -> str:
    """Konvertuj HTML u Markdown bez prelamanja linija."""
    conv = html2text.HTML2Text()
    conv.body_width = 0  # bez wrap-ovanja linija
    conv.ignore_images = False
    conv.ignore_links = False
    conv.protect_links = True
    return conv.handle(html)


# --- Prevod (sa očuvanjem code blokova) -------------------------------------


_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def split_by_code_fences(md: str) -> List[Tuple[str, bool]]:
    """
    Podeli markdown na segmente: (segment, is_code).
    Code fence blokovi (``` ... ```) se izdvajaju i označavaju is_code=True.
    """
    parts: List[Tuple[str, bool]] = []
    last = 0
    for m in _CODE_FENCE_RE.finditer(md):
        if m.start() > last:
            parts.append((md[last : m.start()], False))
        parts.append((m.group(0), True))
        last = m.end()
    if last < len(md):
        parts.append((md[last:], False))
    return parts


def chunk_text(text: str, max_len: int = 4000) -> List[str]:
    """
    Podeli tekst na manje delove (~4k) po praznim linijama.
    Cilj: ne opterećivati jedan DeepL poziv i izbeći presecanje rečenica.
    """
    paragraphs = text.split("\n\n")
    chunks: List[str] = []
    buf: List[str] = []
    size = 0
    for p in paragraphs:
        p_len = len(p) + 2  # računaj \n\n
        if size + p_len > max_len and buf:
            chunks.append("\n\n".join(buf))
            buf, size = [p], p_len
        else:
            buf.append(p)
            size += p_len
    if buf:
        chunks.append("\n\n".join(buf))
    return chunks


def translate_md_to_sr(md: str, auth_key: str) -> str:
    """
    Prevedi Markdown na srpsku latinicu uz DeepL.
    Ne prevodi code fence delove.
    """
    if deepl is None:
        raise RuntimeError("Paket 'deepl' nije instaliran. Pokreni: pip install deepl")

    translator = deepl.Translator(auth_key)
    segments = split_by_code_fences(md)
    out: List[str] = []

    for text, is_code in segments:
        if is_code or not text.strip():
            out.append(text)
            continue

        # Prevodimo u manjim komadima
        for chunk in chunk_text(text):
            # DeepL vraća objekt (ili listu); uzmi .text
            result = translator.translate_text(chunk, target_lang="SR")
            out.append(result.text)

    return "".join(out)


# --- CLI ---------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Skini URL → HTML→ Markdown → prevod na srpsku latinicu (DeepL)."
    )
    parser.add_argument("url", help="URL do zvanične dokumentacije (npr. pytest stranica)")
    parser.add_argument(
        "-o",
        "--out",
        help="Osnovni naziv izlaznih fajlova (bez ekstenzije). Podrazumevano iz URL-a.",
    )
    parser.add_argument(
        "-d", "--dest", default=".", help="Odredišni folder (default: trenutni)."
    )
    args = parser.parse_args()

    base = args.out or derive_base_from_url(args.url)
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    print(f"[1/4] Preuzimam HTML: {args.url}")
    html = fetch_html(args.url)

    print("[2/4] Konvertujem u Markdown…")
    md_en = html_to_markdown(html)

    md_path = dest / f"{base}.md"
    md_path.write_text(md_en, encoding="utf-8")
    print(f"    Sačuvano: {md_path}")

    # DeepL ključ iz okruženja / .env
    load_dotenv()
    auth_key = os.getenv("DEEPL_AUTH_KEY")
    if not auth_key:
        raise SystemExit("GREŠKA: DEEPL_AUTH_KEY nije podešen u okruženju/.env")

    print("[3/4] Prevodim na srpsku latinicu (DeepL)…")
    md_sr = translate_md_to_sr(md_en, auth_key=auth_key)

    md_sr_path = dest / f"{base}.sr.md"
    md_sr_path.write_text(md_sr, encoding="utf-8")
    print(f"[4/4] Sačuvano: {md_sr_path}")

    print("Gotovo ✅")


if __name__ == "__main__":
    main()

import argparse
import os
from pathlib import Path

import html2text
import requests

try:
    import deepl
except ImportError:
    deepl = None


def fetch_html(url: str) -> str:
    """Skini HTML sa zadatog URL-a."""
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def html_to_md(html: str) -> str:
    """Konvertuj HTML u Markdown string."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    return h.handle(html)


def translate_md(md_text: str, auth_key: str, target_lang: str = "SR") -> str:
    """Prevedi Markdown koristeći DeepL API."""
    if deepl is None:
        raise RuntimeError(
            "deepl paket nije instaliran. Instaliraj ga sa `pip install deepl`."
        )
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(md_text, target_lang=target_lang)
    return result.text


def main():
    parser = argparse.ArgumentParser(
        description="Skini URL → Markdown (+ opcioni prevod na srpski)."
    )
    parser.add_argument("url", help="URL zvanične dokumentacije")
    parser.add_argument(
        "-o", "--output", required=True, help="osnovno ime fajla (bez ekstenzije)"
    )
    parser.add_argument(
        "-d", "--directory", default=".", help="folder gde se čuvaju fajlovi"
    )
    parser.add_argument(
        "--no-translate", action="store_true", help="samo Markdown EN, bez prevoda"
    )
    args = parser.parse_args()

    Path(args.directory).mkdir(parents=True, exist_ok=True)

    print("[1/4] Fetch HTML...")
    html = fetch_html(args.url)

    print("[2/4] Convert HTML → Markdown...")
    md_text = html_to_md(html)

    md_file = Path(args.directory) / f"{args.output}.md"
    md_file.write_text(md_text, encoding="utf-8")
    print(f"   ✓ EN fajl sačuvan: {md_file}")

    if args.no_translate:
        print("[3/4] Preskačem prevod (--no-translate)")
        return

    print("[3/4] Translate Markdown → Serbian...")
    auth_key = os.getenv("DEEPL_AUTH_KEY")
    if not auth_key:
        raise RuntimeError(
            "Nema DEEPL_AUTH_KEY u .env fajlu (ili koristi --no-translate)."
        )

    sr_text = translate_md(md_text, auth_key, target_lang="SR")

    sr_file = Path(args.directory) / f"{args.output}.sr.md"
    sr_file.write_text(sr_text, encoding="utf-8")
    print(f"   ✓ SR fajl sačuvan: {sr_file}")

    print("[4/4] Završeno.")


if __name__ == "__main__":
    main()

"""
Utilities for files and paths. | Pomoćne funkcije za fajlove i putanje.

Focus on `pathlib` and safe I/O. | Fokus na `pathlib` i bezbedan I/O.
"""

from __future__ import annotations

from pathlib import Path


def list_py_files(base: Path, pattern: str = "**/*.py") -> list[Path]:
    """Return a sorted list of .py files under base. | Vrati sortiranu listu .py fajlova ispod baze."""
    # TODO: implement with Path.rglob or glob; sort by name. | TODO: implementiraj uz Path.rglob/glob; sortiraj po imenu.
    raise NotImplementedError

def count_lines(path: Path, encoding: str = "utf-8") -> int:
    """Count lines in a text file. | Prebroj linije u tekst fajlu."""
    # TODO: open with encoding and count newline-separated lines. | TODO: otvori sa encoding i prebroj linije.
    raise NotImplementedError

def files_larger_than(base: Path, min_bytes: int) -> list[Path]:
    """Return files whose size >= min_bytes. | Vrati fajlove čija je veličina >= min_bytes."""
    # TODO: iterate recursively and check p.is_file() and p.stat().st_size. | TODO: rekurzivno iteriraj i proveri p.is_file() i p.stat().st_size.
    raise NotImplementedError

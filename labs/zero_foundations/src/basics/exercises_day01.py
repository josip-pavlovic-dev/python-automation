"""
Dan 1 vežbe (popuni TODO zadatke).

Sve funkcije treba da budu **čiste** (bez print).
Koristi type hints kad možeš.
"""

from collections.abc import Iterable
from typing import Any


def is_empty(value: Any) -> bool:
    """Vrati True ako je vrednost prazna/falsy."""
    # TODO: implementiraj koristeći truthiness.
    return not bool(value)

def countdown(n: int) -> list[int]:
    """Vrati [n, n-1, ..., 1]."""
    # TODO: implementiraj uz range.
    return list(range(n, 0, -1))

def enumerate_1(xs: Iterable[Any]) -> list[tuple[int, Any]]:
    """Enumeracija počev od 1."""
    # TODO: koristi enumerate(xs, start=1).
    return list(enumerate(xs, start=1))


from __future__ import annotations

from collections.abc import Iterable
from typing import Any


def safe_div(a: float, b: float, *, default: float | None = None) -> float | None:
    # TODO: vrati a/b ili default ako je b == 0
    if b == 0:
        return default
    return a / b

def float_equal(a: float, b: float, *, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    # TODO: upotrebi math.isclose
    raise NotImplementedError

def norm(z: complex) -> float:
    # TODO: vrati apsolutnu vrednost (modul) kompleksnog broja
    raise NotImplementedError

def first_non_null(*xs: Any) -> Any | None:
    # TODO: vrati prvu vrednost koja NIJE None (ne „prvi truthy“)
    raise NotImplementedError

def count_truthy(xs: Iterable[Any]) -> int:
    # TODO: prebroj elemente koji su truthy (bool(x) je True)
    raise NotImplementedError

def parse_int(s: str, *, default: int | None = None) -> int | None:
    # TODO: pokušaj int(s.strip()); ako ne može, vrati default
    raise NotImplementedError

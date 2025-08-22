from __future__ import annotations

import math


def safe_div(a: float, b: float, *, default: float | None = None) -> float | None:
    """Vrati a/b, ili default ako je b == 0."""
    return a / b if b != 0 else default


def float_equal(x: float, y: float, *, tol: float = 1e-9) -> bool:
    """Uporedi dva broja sa tolerancijom."""
    return math.isclose(x, y, rel_tol=tol, abs_tol=tol)


def norm(x: float, y: float) -> float:
    """Euklidska norma (dužina vektora)."""
    return math.sqrt(x * x + y * y)


def first_non_null(*values, default=None):
    """Vrati prvu vrednost koja NIJE None, ili default ako je sve None."""
    for v in values:
        if v is not None:
            return v
    return default


def count_truthy(seq) -> int:
    """Prebroj sve elemente u seq koji su truthy."""
    return sum(bool(x) for x in seq)

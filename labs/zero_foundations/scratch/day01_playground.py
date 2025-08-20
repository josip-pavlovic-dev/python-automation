from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path
from typing import Any

# ---------- Zadaci (A, B, C) ----------

def countdown(n: int) -> list[int]:
    """Vrati [n, n-1, ..., 1]."""
    if n < 1:
        return []
    return list(range(n, 0, -1))


def enumerate_1(xs: Iterable[Any]) -> list[tuple[int, Any]]:
    """Enumeriraj xs sa start=1 i vrati listu (i, x) parova."""
    return list(enumerate(xs, start=1))


def safe_first(xs: Iterable[Any]) -> Any | None:
    """Vrati prvi element xs ili None ako je xs prazno."""
    # Koristi next(iter(xs), None) za sve iterables, ne samo indexable.
    return next(iter(xs), None)


# ---------- Demo: truthiness ----------

def truthiness_demo() -> None:
    """Brza provera šta je falsy / truthy u Pythonu."""
    falsy = [[], "", 0, 0.0, set(), {}, tuple(), range(0), None]
    for v in falsy:
        assert not bool(v)

    truthy = [[0], "0", 1, {1}, {"k": 0}, (0,), range(1)]
    for v in truthy:
        assert bool(v)


# ---------- Demo: mutacija vs rebinding ----------

def mutate_vs_rebind_demo() -> None:
    """Pokaži razliku između mutacije i rebinding-a liste."""
    xs = [1, 2, 3]
    ys = xs            # ys pokazuje na ISTI objekat
    xs.append(4)       # MUTACIJA xs
    assert ys is xs and ys[-1] == 4

    xs = xs + [5]      # REBINDING xs (novo telo liste)
    assert ys is not xs and ys[-1] == 4 and xs[-1] == 5


# ---------- Demo: pathlib mini-lister ----------

def list_py(limit: int = 5) -> list[str]:
    """
    Vrati do `limit` relativnih .py putanja (prema trenutnom CWD).
    Cilj je da vežbaš pathlib/glob i razliku CWD-a (skripta vs -m).
    """
    root = Path.cwd()
    found = [p for p in root.rglob("*.py")][:limit]
    return [str(p.relative_to(root)) for p in found]


# ---------- Self-check (mini TDD bez pytest-a) ----------

def _self_check() -> None:
    # Zadaci A/B/C
    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]
    assert enumerate_1(["a", "b"]) == [(1, "a"), (2, "b")]
    assert safe_first([]) is None
    assert safe_first([10]) == 10

    # Demos
    truthiness_demo()
    mutate_vs_rebind_demo()

    # Pathlib – ne testiramo sadržaj, samo da ne puca i da vrati do 'limit' putanja
    paths = list_py(limit=5)
    assert isinstance(paths, list) and len(paths) <= 5

    print("L01 playground: OK ✅")


if __name__ == "__main__":
    print("\n=== L01 • Returns ===")
    print("countdown(3) ->", countdown(3))
    print("enumerate_1(['a','b']) ->", enumerate_1(['a', 'b']))
    print("safe_first([]) ->", safe_first([]))
    print("safe_first([10]) ->", safe_first([10]))

    print("\nlist_py(3):")
    for p in list_py(3):
        print(" •", p)

    print("\n=== L01 • Demos (no return) ===")
    # ove funkcije ne vraćaju ništa; ako nešto nije u redu, izbaciće AssertionError
    truthiness_demo()
    mutate_vs_rebind_demo()
    print("Demos: OK ✅ (nema AssertionError-a)")
    _self_check()  # samo za self-check, ne u produkciji
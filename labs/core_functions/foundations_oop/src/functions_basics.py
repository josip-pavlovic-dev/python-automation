"""
function_basics.py
Prvi primeri Python funkcija: definicija, poziv, parametri, return.
"""

from typing import Any


def greet(name: str = "svete") -> str:
    """Vrati pozdrav za dato ime. Ako nema imena → default 'svete'."""
    return f"Zdravo, {name}!"


def add(a: int, b: int) -> int:
    """Vrati zbir dva broja."""
    return a + b


def add_many(*args: int) -> int:
    """Vrati zbir proizvoljnog broja argumenata (0 ako je prazan)."""
    return sum(args)


def debug_kwargs(**kwargs: Any) -> dict[str, Any]:
    """Vrati prosleđene keyword argumente kao dict (za debug/test)."""
    return kwargs


if __name__ == "__main__":
    print(greet())
    print(greet("Mileva"))
    print(add(2, 3))
    print(add_many(1, 2, 3, 4))
    print(debug_kwargs(a=1, b=2))

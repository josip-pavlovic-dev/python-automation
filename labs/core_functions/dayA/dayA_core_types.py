# src/dayA_core_types.py
from __future__ import annotations

from typing import Any, Optional, Union


def to_int(x: Any, base: Optional[int] = None) -> int:
    """
    Konverzija u int.
    - Ako je x str/bytes i base je zadat -> koristi int(x, base)
    - Ako je x str/bytes i base nije zadat -> int(x)
    - Inače -> int(x) (trunc prema nuli za float)
    Greške: ValueError (loš literal), TypeError (nevalidna kombinacija), OverflowError (npr. inf)
    """
    if base is not None:
        return int(x, base)  # TypeError ako x nije tekst/bytes; to želimo da ispliva
    return int(x)


def str_from_bytes(
    b: Union[bytes, bytearray], encoding: str = "utf-8", errors: str = "strict"
) -> str:
    """Decode bytes/bytearray u tekst (podrazumevano UTF-8)."""
    return bytes(b).decode(encoding, errors)


def str_display(obj: Any) -> str:
    """Čitljiv prikaz objekta; ako klasa ima __str__, koristi se; inače repr fallback."""
    return str(obj)


def to_bool(x: Any) -> bool:
    """Truthiness: koristi __bool__ -> __len__ -> default True."""
    return bool(x)

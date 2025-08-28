from __future__ import annotations

import copy
import json
from typing import Any, Literal

CopyMode = Literal["shallow", "deep"]


def make_copy(obj: Any, mode: CopyMode) -> Any:
    """Vrati kopiju objekta prema modu ('shallow' ili 'deep')."""
    if mode == "shallow":
        return copy.copy(obj)
    elif mode == "deep":
        return copy.deepcopy(obj)
    raise ValueError("mode must be 'shallow' or 'deep'")


def parse_json_structure(payload: str) -> Any:
    """Parse JSON string u Python strukturu (list/dict/ugnježđeno)."""
    return json.loads(payload)



def mutate_nested_sample(x: Any) -> None:
    """
    Demo mutacija (najdublje ulevo gde ima smisla):
    - LIST:
        [[[a]], ...] -> x[0][0][0] = -1
        [[a],  ...]  -> x[0][0]    = -1
    - DICT (gledamo prvu vrednost):
        {"k": [[a]]}  -> v[0][0] = -1
        {"k": [a]}    -> v[0]    = -1
    Ako struktura ne odgovara, funkcija ne radi ništa (no-op).
    """
    # LIST
    if isinstance(x, list) and x:
        first = x[0]
        if isinstance(first, list) and first:
            inner = first[0]
            if isinstance(inner, list) and inner:
                inner[0] = -1      # x[0][0][0] = -1
            else:
                first[0] = -1      # x[0][0] = -1
        return

    # DICT
    if isinstance(x, dict) and x:
        v = next(iter(x.values()))
        if isinstance(v, list) and v:
            inner = v[0]
            if isinstance(inner, list) and inner:
                inner[0] = -1      # v[0][0] = -1
            else:
                v[0] = -1          # v[0]    = -1

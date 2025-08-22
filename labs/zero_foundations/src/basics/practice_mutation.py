from __future__ import annotations

from typing import Any


def append_mutate(lst: list[Any], x: Any):
    # TODO: mutiraj listu .append(x) i vrati (id_pre, id_posle, lst)
    raise NotImplementedError

def add_rebind(lst: list[Any], x: Any):
    # TODO: napravi novu listu bez mutacije originala i vrati (id_pre, id_posle, nova)
    raise NotImplementedError

def add_item_bad(item: Any, bucket: list[Any] = []):
    # TODO: LOŠE: pokazuje deljenje stanja između poziva
    raise NotImplementedError

def add_item_good(item: Any, bucket: list[Any] | None = None):
    # TODO: DOBRO: koristi None sentinel da bi napravio novu listu po potrebi
    raise NotImplementedError

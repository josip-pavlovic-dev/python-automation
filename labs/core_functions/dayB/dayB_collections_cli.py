from __future__ import annotations

import argparse
import logging
import pprint
from typing import Any

from dayB.dayB_collections import (
    make_copy,
    mutate_nested_sample,
    parse_json_structure,
    snapshot_ids_dict,
    snapshot_ids_list,
)

log = logging.getLogger("dayB")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Shallow vs Deep copy demo (JSON input).")
    p.add_argument(
        "--copy",
        choices=["shallow", "deep"],
        required=True,
        help="Tip kopije: shallow ili deep (copy.copy vs copy.deepcopy)",
    )
    p.add_argument(
        "--json",
        required=True,
        help="Ugnježdena struktura kao JSON string, npr: '[[[1,2]], [3]]' ili '{\"a\": [[1,2]], \"b\": 3}'",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    return p.parse_args()


def setup_logging(verb: int) -> None:
    level = logging.WARNING - min(verb, 2) * 10
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def _ids_snapshot(x: Any) -> dict:
    if isinstance(x, list):
        return snapshot_ids_list(x)
    if isinstance(x, dict):
        return snapshot_ids_dict(x)
    return {"id_self": id(x)}


def main() -> int:
    a = parse_args()
    setup_logging(a.verbose)
    original = parse_json_structure(a.json)

    c = make_copy(original, a.copy)
    before = {
        "original": _ids_snapshot(original),
        "copy": _ids_snapshot(c),
    }

    mutate_nested_sample(original)  # menja original (in-place) ako može

    after = {
        "original": _ids_snapshot(original),
        "copy": _ids_snapshot(c),
        "original_value": original,
        "copy_value": c,
    }

    print("=== IDs BEFORE ===")
    pprint.pprint(before, sort_dicts=False)
    print("\n=== IDs AFTER (posle mutate_nested_sample(original)) ===")
    pprint.pprint(after, sort_dicts=False)

    # Hint korisniku
    print("\nNote:")
    print(
        "- Kod shallow kopije očekuj da se PROMENA u ugnježdenoj listi vidi i u kopiji."
    )
    print("- Kod deep kopije očekuj da kopija ostane NEIZMENJENA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Mini CLI: demonstrira core konverzije int/str/bool za zadate ulaze.

Usage:
  python -m src.dayA_core_types_cli --int "0x2A" --base 0 --str-bytes "6869" --str-encoding hex --bool ""
"""

from __future__ import annotations

import argparse
import binascii
import logging

log = logging.getLogger("dayA")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--int", dest="int_val", help="vrednost za int()", default=None)
    p.add_argument(
        "--base", type=int, default=10, help="osnova za int() (2..36 ili 0 auto)"
    )
    p.add_argument(
        "--str-bytes",
        dest="str_bytes",
        help="heks string npr. '6869' (hi)",
        default=None,
    )
    p.add_argument(
        "--str-encoding", dest="str_enc", choices=["utf-8", "hex"], default="utf-8"
    )
    p.add_argument(
        "--bool",
        dest="bool_val",
        help="vrednost za bool() (string se tretira po truthiness)",
    )
    p.add_argument("-v", "--verbose", action="count", default=0)
    return p.parse_args()


def setup_logging(verb: int) -> None:
    level = logging.WARNING - min(verb, 2) * 10
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def demo_int(s: str, base: int) -> int:
    if s is None:
        return 0
    return int(s, base)  # može ValueError/TypeError; to je OK, CLI će prikazati


def demo_str_from_bytes(payload: str | None, mode: str) -> str | None:
    if not payload:
        return None
    if mode == "hex":
        b = binascii.unhexlify(payload)  # "6869" -> b"hi"
        return b.decode("utf-8")  # dekodiraj
    else:
        return str(payload)  # običan str()


def demo_bool(x: str | None) -> bool:
    return bool(x)


def main() -> int:
    a = parse_args()
    setup_logging(a.verbose)
    try:
        iv = demo_int(a.int_val, a.base)
        log.info("int(%r, base=%s) = %r", a.int_val, a.base, iv)
    except Exception as e:
        log.error("int() failure: %s: %s", type(e).__name__, e)

    sv = demo_str_from_bytes(a.str_bytes, a.str_enc)
    log.info("str-from-bytes(%r, %s) -> %r", a.str_bytes, a.str_enc, sv)

    bv = demo_bool(a.bool_val)
    log.info("bool(%r) -> %r", a.bool_val, bv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

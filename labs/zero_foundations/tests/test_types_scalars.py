import math

from src.basics.types_scalars import (
    count_truthy,
    first_non_null,
    float_equal,
    norm,
    parse_int,
    safe_div,
)


def test_safe_div():
    assert safe_div(1, 4) == 0.25
    assert safe_div(1, 0) is None
    assert safe_div(1, 0, default=0.0) == 0.0

def test_float_equal():
    assert float_equal(0.1 + 0.2, 0.3)
    assert not float_equal(1.0, 1.0000001, rel_tol=1e-12)

def test_norm():
    assert math.isclose(norm(3+4j), 5.0)
    assert math.isclose(norm(0+0j), 0.0)

def test_first_non_null():
    assert first_non_null(None, "", 0, "ok") == ""
    assert first_non_null(None, None) is None

def test_count_truthy():
    xs = ["", " ", [], [0], 0, 1, None, True, False]
    assert count_truthy(xs) == 4  # " ", [0], 1, True

def test_parse_int():
    assert parse_int(" 42 ") == 42
    assert parse_int("0042") == 42
    assert parse_int("x42", default=None) is None
    assert parse_int("x42", default=-1) == -1

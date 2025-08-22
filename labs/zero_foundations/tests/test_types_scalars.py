import math

from src.basics.types_scalars import float_equal, norm, safe_div


def test_safe_div_basic():
    assert safe_div(10, 2) == 5
    assert safe_div(10, 0, default=0) == 0
    assert safe_div(10, 0) is None


def test_float_equal():
    assert float_equal(0.1 + 0.2, 0.3)  # floating point issue
    assert not float_equal(0.1, 0.1000001, tol=1e-12)


def test_norm():
    assert norm(3, 4) == 5
    assert math.isclose(norm(1, 1), math.sqrt(2))

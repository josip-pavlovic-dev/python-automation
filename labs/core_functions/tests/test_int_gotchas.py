import pytest


def test_bool_int_key_collision():
    d = {1: "int", True: "bool"}
    assert d[1] == "bool"        # poslednji pobedio

def test_int_from_space_or_float_string():
    import math
    with pytest.raises(ValueError):
        int("   ")
    with pytest.raises(ValueError):
        int("3.14")
    assert int(math.trunc(3.14)) == 3

def test_int_from_bytes():
    assert int(b"123") == 123
    with pytest.raises(ValueError):
        int(b"12 3")

def test_negative_base_not_allowed():
    with pytest.raises(ValueError):
        int("10", -2)

def test_index_vs_int_methods():
    class X:
        def __index__(self): return 11
        def __int__(self):   return 99
    assert int(X()) == 11   # __index__ ima prioritet kao fallback

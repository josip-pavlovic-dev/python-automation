import pytest


def test_int_from_str_decimal():
    assert int("42") == 42
    assert int("+7") == 7
    assert int("-3") == -3
    with pytest.raises(ValueError):
        int("3.5")
    with pytest.raises(ValueError):
        int("")

def test_int_with_base():
    assert int("1010", 2) == 10
    assert int("ff", 16) == 255
    assert int("077", 8) == 0o77 == 63
    with pytest.raises(ValueError):
        int("2", 2)
    with pytest.raises(ValueError):
        int("08", 8)   # '8' nije cifara u oktalnom

def test_int_base_zero_autodetect():
    assert int("0xff", 0) == 255
    assert int("0o77", 0) == 63
    assert int("0b101", 0) == 5
    with pytest.raises(ValueError):
        int("08", 0)  # istorijski: nije validno kao auto oktal

def test_bool_is_subclass_of_int():
    assert issubclass(bool, int)
    assert True + True == 2
    assert int(True) == 1
    assert int(False) == 0

def test_arbitrary_precision_no_overflow():
    big = 10**1000
    assert isinstance(big, int)
    assert big + 1 > big

def test_custom_fallback_index_over_int():
    class A:
        def __index__(self): return 7
    class B:
        def __int__(self): return 9
    assert int(A()) == 7     # int → __index__ fallback prioritet
    assert int(B()) == 9

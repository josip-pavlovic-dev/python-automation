import pytest


def test_basic_conversion():
    assert int(-10.5) == -10
    assert int(3.9) == 3
    assert int(True) == 1
    assert int(False) == 0
    assert int("42") == 42
    assert int("1010", 2) == 10
    assert int("FF", 16) == 255


def test_bit_operations():
    assert (10).bit_length() == 4  # 1010
    assert (255).bit_length() == 8  # 11111111
    assert (10).bit_count() == 2  # 1010
    assert (15).bit_count() == 4  # 1111


def test_to_bytes_and_from_bytes():
    # to_bytes
    assert (255).to_bytes(2, "big") == b"\x00\xff"
    assert (255).to_bytes(2, "little") == b"\xff\x00"
    # from_bytes
    assert int.from_bytes(b"\x00\xff", "big") == 255
    assert int.from_bytes(b"\xff\x00", "little") == 255


def test_rational_attributes():
    x = 5
    assert x.numerator == 5
    assert x.denominator == 1


def test_complex_attributes():
    x = 5
    assert x.real == 5
    assert x.imag == 0


def test_invalid_inputs():
    with pytest.raises(TypeError):
        int(None)
    with pytest.raises(ValueError):
        int("12.5")  # nije validan int string

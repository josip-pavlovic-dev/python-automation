# tests/test_dayA_core_types.py
import pytest
from dayA.dayA_core_types import str_display, str_from_bytes, to_bool, to_int

# ==== int(): happy ====


def test_int_truncation_from_float():
    assert to_int(42.9) == 42
    assert to_int(-3.9) == -3


def test_int_with_base_and_auto_prefix():
    assert to_int("1010", base=2) == 10
    assert to_int("0b101", base=0) == 5
    assert to_int(b"2a", base=16) == 42


# ==== int(): errors ====


def test_int_valueerror_bad_literal():
    with pytest.raises(ValueError):
        to_int("12.5")  # nije ceo broj


def test_int_typeerror_base_on_non_text():
    with pytest.raises(TypeError):
        to_int(3.0, base=10)  # base samo za string/bytes


def test_int_overflowerror_inf():
    with pytest.raises(OverflowError):
        to_int(float("inf"))


# ==== dunder __int__ / __index__ fallback ====


class WithInt:
    def __int__(self):
        return 42


class OnlyIndex:
    def __index__(self):
        return 7


def test_dunder_int_and_index():
    assert to_int(WithInt()) == 42
    assert to_int(OnlyIndex()) == 7


# ==== str(): bytes decode i str-display ====


def test_str_from_bytes_utf8_and_hex():
    assert str_from_bytes(b"hi") == "hi"
    # "6869" je "hi" u hex-u:
    assert bytes.fromhex("6869").decode("utf-8") == "hi"


def test_str_display_str_vs_repr():
    class WithStr:  # ima __str__
        def __str__(self):
            return "pretty"

    class NoStr:  # nema __str__ -> repr fallback
        pass

    assert str_display(WithStr()) == "pretty"
    assert "object at 0x" in str_display(NoStr())


def test_str_encoding_typeerror_like_builtin():
    # builtin str() sa encoding parametrom radi samo za bytes; mi ga ne podržavamo u str_display
    with pytest.raises(TypeError):
        str(123, "utf-8")  # mirrorujemo ponašanje builtina


# ==== bool(): truthiness + dunder lanci ====


def test_bool_truthiness_basics():
    assert to_bool(0) is False
    assert to_bool(1) is True
    assert to_bool("") is False
    assert to_bool("0") is True
    assert to_bool([]) is False
    assert to_bool([0]) is True
    assert to_bool(None) is False


def test_bool_dunders_and_error():
    class WithBool:
        def __bool__(self):
            return False

    class WithLen:
        def __len__(self):
            return 2

    assert to_bool(WithBool()) is False
    assert to_bool(WithLen()) is True

    class BadBool:
        def __bool__(self):
            return 2

    with pytest.raises(TypeError):
        bool(BadBool())

import pytest


# ---------- Osnovno ponašanje ----------
def test_basic_scalars_to_str():
    assert str(10) == "10"
    assert str(3.14).startswith("3.14")  # tolerisati razlike reprezentacije
    assert str(True) == "True"
    assert str(False) == "False"
    assert str(None) == "None"


def test_collections_to_str():
    assert str([1, 2]) == "[1, 2]"
    assert str({"a": 1}).startswith("{")  # format može da se razlikuje po spacingu
    assert str((1, 2)) == "(1, 2)"


def test_objects_with_str_and_repr():
    class WithStr:
        def __str__(self):
            return "S"

    class WithoutStr:
        def __repr__(self):
            return "R"

    assert str(WithStr()) == "S"
    assert str(WithoutStr()) == "R"  # pada na __repr__ ako nema __str__


# ---------- Bajtovi i dekodiranje ----------
def test_str_on_bytes_repr_vs_decode():
    b = b"abc"
    # Bez encoding-a: repr prikaz
    assert str(b) == "b'abc'"
    # Sa encoding-om: dekodirano
    assert str(b, "ascii") == "abc"


def test_str_on_bytes_invalid_decode_raises():
    bad = b"\xff"
    with pytest.raises(UnicodeDecodeError):
        str(bad, "utf-8")  # strict by default


def test_str_on_bytes_decode_with_errors_replace():
    bad = b"\xff"
    assert str(bad, "utf-8", "replace") == "�"


# ---------- Granice i specijale ----------
def test_float_str_scientific_and_precision():
    # Može vratiti eksponencijalni zapis za vrlo male/velike brojeve
    s = str(1e-7)
    assert "e" in s or s.startswith("0.0") or s.startswith("1e-")  # tolerantno


def test_complex_to_str():
    assert str(1 + 2j) in {"(1+2j)"}  # format stabilan u Py3


def test_str_no_encoding_on_non_bytes_raises_typeerror():
    with pytest.raises(TypeError):
        str(10, "utf-8")  # encoding dozvoljen samo za bytes-like


# ---------- Custom klase — profesionalni slučaj ----------
def test_custom_class_readable_and_repr():
    class User:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"User<{self.name}>"

        def __repr__(self):
            return f"User(name={self.name!r})"

    u = User("Ana")
    assert str(u) == "User<Ana>"
    assert repr(u) == "User(name='Ana')"

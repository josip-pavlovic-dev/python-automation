import pytest


# ---------- Skalari ----------
def test_bool_on_numbers():
    assert bool(0) is False
    assert bool(0.0) is False
    assert bool(0j) is False
    assert bool(1) is True
    assert bool(-1) is True
    assert bool(2.7) is True


def test_bool_on_none_and_object():
    assert bool(None) is False
    assert bool(object()) is True  # default je True ako nema __bool__/__len__


# ---------- Stringovi ----------
def test_bool_on_strings():
    assert bool("") is False
    assert bool(" ") is True  # whitespace je neprazan
    assert bool("0") is True  # neprazan string -> True
    assert bool("False") is True  # neprazan string -> True


# ---------- Kolekcije ----------
def test_bool_on_collections():
    assert bool([]) is False
    assert bool([[]]) is True
    assert bool(()) is False
    assert bool((0,)) is True
    assert bool({}) is False
    assert bool({"a": 1}) is True
    assert bool(set()) is False
    assert bool({0}) is True
    assert bool(range(0)) is False
    assert bool(range(1)) is True


# ---------- Custom tipovi: __len__ fallback ----------
def test_bool_custom_class_len_fallback():
    class Box:
        def __init__(self, items):
            self.items = items

        def __len__(self):
            return len(self.items)

    assert bool(Box([])) is False
    assert bool(Box([1])) is True


# ---------- Custom tipovi: __bool__ ima prioritet ----------
def test_bool_custom_class_bool_priority_over_len():
    class Weird:
        def __len__(self):
            return 0  # sugeriše False...

        def __bool__(self):
            return True  # ...ali __bool__ pobeđuje

    assert bool(Weird()) is True


# ---------- Custom tip: bez __bool__/__len__ -> True ----------
def test_bool_custom_class_default_true():
    class Plain:
        pass

    assert bool(Plain()) is True


# ---------- Edge slučajevi za “zbunjujuće stringove” ----------
@pytest.mark.parametrize("value", ["0", "False", "None", "No"])
def test_confusing_strings_are_truthy(value):
    # Neprazni stringovi su True bez obzira na "semantiku" sadržaja
    assert bool(value) is True

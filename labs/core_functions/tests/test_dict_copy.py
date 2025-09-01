import copy

import pytest


def test_assignment_is_same_reference():
    d1 = {"x": [1, 2], "y": 3}
    d2 = d1  # samo nova referenca, nije kopija
    assert d1 is d2
    d2["x"][0] = 99
    assert d1["x"][0] == 99  # promena se vidi i u d1


def test_shallow_copy_dict_copy_new_outer_same_inner_refs():
    d1 = {"x": [1, 2], "y": 3}
    d2 = d1.copy()  # shallow
    assert d1 is not d2
    assert d1 == d2

    # Izmena skroz spolja:
    d2["y"] = 100
    assert d1["y"] == 3  # d1 ostaje isto po kljucu 'y'

    # Izmena unutrašnje mutable vrednosti:
    d2["x"][0] = 99
    assert d1["x"][0] == 99  # DELI se lista između d1 i d2 (shallow copy)


def test_shallow_copy_copy_copy_equivalent_to_dict_copy():
    d1 = {"x": [1, 2], "y": {"z": 0}}
    d2 = copy.copy(d1)  # isto kao d1.copy()
    assert d1 is not d2
    # Unutrašnje reference su iste (shallow)
    assert d1["x"] is d2["x"]
    assert d1["y"] is d2["y"]


def test_deepcopy_isolated_nested_mutables():
    d1 = {"x": [1, 2], "y": {"z": 0}}
    d2 = copy.deepcopy(d1)
    assert d1 is not d2
    assert d1["x"] is not d2["x"]
    assert d1["y"] is not d2["y"]

    # Menjamo d2; d1 ostaje netaknut
    d2["x"][0] = 99
    d2["y"]["z"] = 42
    assert d1["x"][0] == 1
    assert d1["y"]["z"] == 0


@pytest.mark.parametrize(
    "factory",
    [
        lambda: {"a": 1, "b": 2},                    # prost dict (samo immutable vrednosti)
        lambda: {"a": (1, 2), "b": ("x", "y")},      # tuple vrednosti (immutable)
    ],
)
def test_shallow_copy_ok_when_values_are_immutable(factory):
    d1 = factory()
    d2 = d1.copy()  # shallow je OK jer su vrednosti immutable
    assert d1 is not d2
    assert d1 == d2
    # Promena vrednosti u d2 NE utiče na d1 (jer zamenjujemo referencu)
    d2["a"] = 999
    assert d1["a"] != d2["a"]


def test_common_pitfall_list_inside_dict():
    d1 = {"xs": [1, 2, 3]}
    d2 = d1.copy()  # shallow
    d3 = copy.deepcopy(d1)

    # Mutacija elementa liste utiče na d1 i d2, ne i na d3
    d2["xs"].append(4)
    assert d1["xs"] == [1, 2, 3, 4]
    assert d2["xs"] == [1, 2, 3, 4]
    assert d3["xs"] == [1, 2, 3]


def test_overwriting_inner_reference_breaks_sharing():
    d1 = {"xs": [1, 2]}
    d2 = d1.copy()  # shallow -> dele listu

    # Ako potpuno zamenimo referencu u d2, prekidamo deljenje
    d2["xs"] = [999]
    assert d1["xs"] == [1, 2]
    assert d2["xs"] == [999]


def test_error_example_unhashable_key_in_dict_creation():
    with pytest.raises(TypeError):
        _ = {[1, 2]: "nope"}  # list nije hashable -> ne može kao ključ


def test_deepcopy_mixed_levels():
    d1 = {"a": [{"k": 1}, {"k": 2}], "b": 5}
    d2 = copy.deepcopy(d1)

    # Menjamo duboko u d2
    d2["a"][0]["k"] = 999
    assert d1["a"][0]["k"] == 1  # d1 netaknut
    # Menjamo plitko u d2
    d2["b"] = 100
    assert d1["b"] == 5

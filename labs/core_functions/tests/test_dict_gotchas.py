import pytest


def test_bool_and_int_keys():
    d = {1: "int", True: "bool"}
    assert d[1] == "bool"   # poslednji ključ pobedio

def test_false_and_zero_keys():
    d = {0: "zero", False: "false"}
    assert d[0] == "false"

def test_unhashable_key_list():
    with pytest.raises(TypeError):
        { [1, 2]: "ne radi" }

def test_tuple_with_list_inside():
    with pytest.raises(TypeError):
        { (1, [2, 3]): "ne radi" }

def test_tuple_with_only_hashable():
    d = {(1, 2): "ok"}
    assert d[(1, 2)] == "ok"

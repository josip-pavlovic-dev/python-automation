import pytest


def test_hashable_keys_ok():
    d = {1: "int", (1, 2): "tuple", "s": "str"}
    assert d[1] == "int"
    assert d[(1, 2)] == "tuple"
    assert d["s"] == "str"

def test_unhashable_keys_fail():
    with pytest.raises(TypeError):
        {["a", "b"]: "lista nije hashable"}

    with pytest.raises(TypeError):
        {{1: 2}: "dict nije hashable"}  # dict kao ključ

import pytest


def test_hashable_key_ok():
    # int je hashable
    d = {1: "a"}
    assert d[1] == "a"

    # tuple je hashable AKO su svi elementi hashable
    d2 = {(1, 2): "ok"}
    assert d2[(1, 2)] == "ok"

    # string je hashable
    d3 = {"x": 42}
    assert d3["x"] == 42


def test_unhashable_key_fail():
    # list nije hashable → TypeError
    with pytest.raises(TypeError):
        {["a", "b"]: "oops"}

    # dict nije hashable → TypeError
    with pytest.raises(TypeError):
        {{1: 2}: "bad"}

    # tuple sa listom unutra → TypeError
    with pytest.raises(TypeError):
        {(1, [2, 3]): "also bad"}

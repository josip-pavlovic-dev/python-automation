import copy

import pytest


def test_get_vs_indexing():
    d = {"x": 1}
    with pytest.raises(KeyError):
        _ = d["y"]
    assert d.get("y") is None
    assert d.get("y", 99) == 99

def test_membership_is_on_keys():
    d = {"a": 1, "b": 2}
    assert "a" in d
    assert 1 not in d
    assert 1 in d.values()

def test_hashable_keys():
    k = (1, 2)
    d = {k: "ok"}
    assert d[k] == "ok"

def test_unhashable_keys_raise():
    with pytest.raises(TypeError):
        {[]: 1}
    with pytest.raises(TypeError):
        {([1], 2): "no"}

def test_shallow_vs_deep_copy_on_values():
    d = {"x": [1, 2]}
    sh = d.copy()
    dp = copy.deepcopy(d)
    d["x"][0] = 99
    assert sh["x"][0] == 99   # deli unutrašnjost
    assert dp["x"][0] == 1    # deep je nezavisan

def test_setdefault_builds_container_once():
    d = {}
    d.setdefault("items", []).append("x")
    d.setdefault("items", []).append("y")
    assert d["items"] == ["x", "y"]

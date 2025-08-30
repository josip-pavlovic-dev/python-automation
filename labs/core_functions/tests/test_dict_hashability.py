import builtins
import math

import pytest


def is_hashable(x) -> bool:
    try:
        hash(x)
        return True
    except TypeError:
        return False


# === Happy: dozvoljeni (hashable) ključevi ===

def test_hashable_simple_keys():
    d = {
        1: "int",
        "x": "str",
        (1, 2): "tuple_of_hashables",
        frozenset({1, 2}): "frozenset",
        None: "none",
        True: "bool",
    }
    # sanity
    assert d[1] == "int"
    assert d["x"] == "str"
    assert d[(1, 2)] == "tuple_of_hashables"
    assert d[frozenset({1, 2})] == "frozenset"
    assert d[None] == "none"
    assert d[True] == "bool"
    # svi navedeni zaista jesu hashable
    for k in d.keys():
        assert is_hashable(k)


# === Error: nedozvoljeni (unhashable) ključevi ===

def test_unhashable_basic_types_raise():
    with pytest.raises(TypeError):
        {[]: 1}                 # list
    with pytest.raises(TypeError):
        {{1, 2}: "set"}         # set
    with pytest.raises(TypeError):
        {{1: 2}: "dict"}        # dict kao ključ

def test_tuple_containing_unhashable_is_unhashable():
    # tuple je hashable SAMO ako su SVI njegovi elementi hashable
    with pytest.raises(TypeError):
        {([1], 2): "no"}        # lista unutra kvari stvar
    with pytest.raises(TypeError):
        {( {1}, 2 ): "no"}      # set unutra kvari stvar

def test_custom_object_without_hash_is_hashable_by_identity():
    class A:
        # nema __eq__/__hash__ → nasleđuje object.__hash__ → hashable po identitetu
        pass
    a1, a2 = A(), A()
    d = {a1: "one", a2: "two"}
    assert d[a1] == "one" and d[a2] == "two"
    assert is_hashable(a1) and is_hashable(a2)

def test_custom_object_explicitly_unhashable():
    class B:
        __hash__ = None      # standardna konvencija: instanca NIJE hashable
    with pytest.raises(TypeError):
        {B(): "x"}

def test_is_hashable_helper_spot_checks():
    # brzi sanity za helper
    samples_true  = [0, 1.5, "s", (1, 2), frozenset({1}), builtins, math]
    samples_false = [[], {}, set(), [1, 2]]
    assert all(is_hashable(x) for x in samples_true)
    assert all(not is_hashable(x) for x in samples_false)

import copy

import pytest
from dayB.dayB_collections import make_copy, mutate_nested_sample

# ==== LIST kopije (shallow vs deep) ====

def test_list_slice_is_shallow():
    a = [[1, 2], [3]]
    a2 = a[:]  # shallow
    a[0][0] = -1
    assert a2[0][0] == -1  # deli ugnježdeni objekat

def test_list_deepcopy_is_independent():
    a = [[1, 2], [3]]
    a3 = copy.deepcopy(a)
    a[0][0] = -1
    assert a3[0][0] == 1  # deep kopija ostaje nezavisna

def test_make_copy_modes():
    a = [[1], [2]]
    s = make_copy(a, "shallow")
    d = make_copy(a, "deep")
    assert s is not a and d is not a
    a[0][0] = 99
    assert s[0][0] == 99  # shallow deli unutrašnjost
    assert d[0][0] == 1   # deep ne deli

# ==== DICT ključevi i .get vs [] ====

def test_dict_keyerror_vs_get():
    d = {"x": 1}
    with pytest.raises(KeyError):
        _ = d["y"]
    assert d.get("y") is None
    assert d.get("y", 99) == 99

def test_unhashable_list_key_raises():
    with pytest.raises(TypeError):
        {[]: 1}  # list nije hashable

def test_tuple_key_ok():
    k = (1, 2)
    d = {k: "ok"}
    assert d[k] == "ok"

def test_tuple_with_list_inside_is_unhashable():
    lst = [1]
    k = (lst, 2)
    with pytest.raises(TypeError):
        {k: "nope"}

# ==== len() ponašanje i custom __len__ ====

def test_len_on_collections():
    assert len([]) == 0
    assert len([1, 2]) == 2
    assert len({"a": 1}) == 1

class BadLen:
    def __len__(self): return -1

def test_len_negative_raises_valueerror():
    b = BadLen()
    with pytest.raises(ValueError):
        len(b)

# ==== membership 'in' (list vs dict) ====

def test_membership_list_and_dict():
    xs = [10, 20]
    d = {"a": 1, "b": 2}
    assert 10 in xs
    assert "a" in d          # membership u dict gleda KLJUČEVE
    assert 1 not in d        # vrednosti nisu članstvo (sem preko d.values())

# ==== mutate_nested_sample demonstracija ====

def test_mutate_nested_sample_list():
    a = [[[1, 2]], [3]]
    mutate_nested_sample(a)
    assert a[0][0][0] == -1

def test_mutate_nested_sample_dict():
    a = {"x": [[1, 2]], "y": 3}
    mutate_nested_sample(a)
    assert a["x"][0][0] == -1

import pytest


def test_literal_creation_happy():
    d = {"a": 1, "b": 2}
    assert d == {"a": 1, "b": 2}
    assert isinstance(d, dict)

def test_from_pairs_happy():
    pairs = [("a", 1), ("b", 2)]
    d = dict(pairs)
    assert d["a"] == 1 and d["b"] == 2

def test_named_args_happy():
    d = dict(a=1, b=2)  # kljucevi su stringovi-validni identifikatori
    assert d == {"a": 1, "b": 2}

def test_tuple_key_literal_happy():
    d = {(1, 2): "x"}
    assert d[(1, 2)] == "x"

def test_tuple_key_from_pairs_happy():
    d = dict([((1, 2), "x")])   # tuple kljuc preko iterabla parova
    assert d[(1, 2)] == "x"

def test_named_args_invalid_identifier_syntax_error():
    code = 'dict((1,2)="x")'  # nevalidna sintaksa
    with pytest.raises(SyntaxError):
        compile(code, "<str>", "exec")

def test_unhashable_key_type_error():
    with pytest.raises(TypeError):
        # list nije hashable -> ne moze biti kljuc
        _ = {[1, 2]: "x"}  # noqa: F601

def test_duplicate_keys_last_wins():
    d = {"a": 1, "a": 2}
    assert d["a"] == 2

def test_merge_operator_pipe_creates_new():
    a = {"x": 1}
    b = {"y": 2}
    c = a | b
    assert c == {"x": 1, "y": 2}
    assert a == {"x": 1}  # a ostaje isto

def test_merge_operator_ior_in_place():
    a = {"x": 1}
    b = {"y": 2}
    a |= b
    assert a == {"x": 1, "y": 2}  # a je izmenjen in-place

def test_get_vs_indexing_default_and_keyerror():
    d = {"user": "ana"}
    assert d.get("user", "guest") == "ana"
    assert d.get("missing", "guest") == "guest"
    with pytest.raises(KeyError):
        _ = d["missing"]

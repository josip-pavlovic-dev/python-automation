import pytest


def test_get_returns_default_when_missing():
    d = {"a": 1}
    assert d.get("a") == 1
    assert d.get("x") is None
    assert d.get("x", 99) == 99          # bez KeyError-a

def test_indexing_raises_keyerror_when_missing():
    d = {"a": 1}
    with pytest.raises(KeyError):
        _ = d["x"]                       # [] traži da ključ postoji

def test_no_side_effects_for_get():
    d = {}
    _ = d.get("items", [])               # ne menja dict
    assert d == {}                       # i dalje prazan

def test_setdefault_has_side_effects_once():
    d = {}
    # kreira 'items' ako ne postoji, vrati listu, pa se mutira append-om
    d.setdefault("items", []).append("x")
    assert d == {"items": ["x"]}

    # drugi put se ključ već nalazi – koristi istu listu
    d.setdefault("items", []).append("y")
    assert d["items"] == ["x", "y"]

def test_pop_with_default_is_safe():
    d = {"a": 1}
    assert d.pop("a", None) == 1         # vrati i ukloni
    assert d == {}
    assert d.pop("a", None) is None      # umesto KeyError-a

def test_keyerror_message_contains_key():
    d = {}
    with pytest.raises(KeyError) as ei:
        _ = d["user"]
    # Lenja, ali korisna provera: poruka sadrži repr ključa
    assert "'user'" in str(ei.value)

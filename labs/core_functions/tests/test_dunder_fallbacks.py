import pytest

# ---------- BOOL: __bool__ > __len__ > default True ----------


def test_bool_prefers___bool__():
    class X:
        def __len__(self):
            return 0  # ovo bi dalo False...

        def __bool__(self):
            return True  # ...ali __bool__ ima prioritet

    assert bool(X()) is True


def test_bool_fallback_to___len__():
    class Box:
        def __init__(self, items):
            self.items = items

        def __len__(self):
            return len(self.items)

    assert bool(Box([])) is False  # len == 0
    assert bool(Box([1])) is True  # len > 0


def test_bool_default_true_without_both():
    class Plain:  # nema ni __bool__ ni __len__
        pass

    assert bool(Plain()) is True


# ---------- INT: __int__ > __index__ > TypeError ----------


def test_int_uses___int__():
    class N:
        def __int__(self):
            return 42

    assert int(N()) == 42


def test_int_fallback_to___index__():
    class Ix:
        def __index__(self):
            return 7

    assert int(Ix()) == 7


def test_int_typeerror_without_both():
    class Bad:
        pass

    with pytest.raises(TypeError):
        int(Bad())


# ---------- STR: __str__ > __repr__ (fallback) ----------


def test_str_prefers___str__():
    class S:
        def __str__(self):
            return "pretty"

        def __repr__(self):
            return "debug"

    assert str(S()) == "pretty"
    assert repr(S()) == "debug"


def test_str_fallback_to___repr__():
    class R:
        def __repr__(self):
            return "debug-only"

    # nema __str__, pa se koristi __repr__ kao fallback
    assert str(R()) == "debug-only"


def test_str_default_object_repr_shape():
    class P:  # nema ni __str__ ni __repr__
        pass

    s = str(P())
    # Ne proveravamo tačnu adresu, samo da je formata <... object at 0x...>
    assert s.startswith("<") and "object at 0x" in s and s.endswith(">")


# ----------- __call__ "pažljivo" poziva -----------


def test_call_makes_instance_callable():
    class R:
        def __call__(self, n):
            return n * 2

    r = R()
    assert callable(r)
    assert r(5) == 10


# ------------ __getitem__/__contains__ interplay ------------


def test_getitem_and_contains_contract():
    class Bag:
        def __init__(self):
            self._d = {}

        def __setitem__(self, k, v):
            self._d[k] = v

        def __getitem__(self, k):
            return self._d[k]

        def __contains__(self, k):
            return k in self._d

    b = Bag()
    b["x"] = 1
    assert "x" in b and b["x"] == 1
    with pytest.raises(KeyError):
        _ = b["nope"]


# --------- __enter__/__exit__ za context manager ---------


def test_context_manager_protocol_is_called():
    calls = []

    class CM:
        def __enter__(self):
            calls.append("enter")
            return 123

        def __exit__(self, exc_type, exc, tb):
            calls.append("exit")
            return False

    with CM() as v:
        assert v == 123
    assert calls == ["enter", "exit"]

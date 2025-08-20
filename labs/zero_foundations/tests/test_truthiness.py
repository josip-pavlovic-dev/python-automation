from src.basics.practice_truthiness import coalesce, is_truthy


def test_is_truthy_core():
    assert is_truthy([0]) is True
    assert is_truthy([]) is False
    assert is_truthy("") is False
    assert is_truthy("a") is True
    assert is_truthy(range(0)) is False
    assert is_truthy(range(1)) is True
    assert is_truthy(0) is False
    assert is_truthy(1) is True
    assert is_truthy(None) is False

def test_coalesce_basic():
    assert coalesce("", 0, None, "ok") == "ok"
    assert coalesce(False, None, 0.0, [1]) == [1]
    assert coalesce("x") == "x"

def test_coalesce_default():
    sentinel = object()
    assert coalesce("", 0, None, default=sentinel) is sentinel

from src.basics.types_scalars import count_truthy, first_non_null


def test_first_non_null_basic():
    assert first_non_null(None, None, "ok") == "ok"
    assert first_non_null(None, "", 0, "x") == ""
    assert first_non_null(None, None, 0) == 0
    assert first_non_null(None) is None


def test_count_truthy():
    assert count_truthy([]) == 0
    assert count_truthy(["", 0, None]) == 0
    assert count_truthy([" ", 0, []]) == 1
    assert count_truthy([0, 1, 2, "", "x"]) == 3

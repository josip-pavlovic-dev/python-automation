def test_int_casting():
    assert int(3.9) == 3
    assert int(-3.9) == -3


def test_str_casting():
    assert str(42) == "42"
    assert str(True) == "True"


def test_bool_casting():
    assert bool(0) is False
    assert bool(1) is True

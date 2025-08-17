import pytest
from src.basics.exercises_day01 import is_empty, countdown, enumerate_1

def test_is_empty_basic():
    assert is_empty(0) is True
    assert is_empty("") is True
    assert is_empty([]) is True
    assert is_empty("x") is False

@pytest.mark.parametrize("n, expected", [(3, [3,2,1]), (1, [1])])
def test_countdown(n, expected):
    assert countdown(n) == expected

def test_enumerate_1():
    xs = ["a", "b", "c"]
    assert enumerate_1(xs) == [(1,"a"), (2,"b"), (3,"c")]

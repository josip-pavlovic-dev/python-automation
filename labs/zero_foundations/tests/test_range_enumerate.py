from src.basics.practice_range_enumerate import (
    countdown,
    enumerate_with_index,
    odd_numbers,
)


def test_countdown():
    assert countdown(5) == [5,4,3,2,1]
    assert countdown(1) == [1]

def test_odd_numbers():
    assert odd_numbers(2, 10) == [3,5,7,9]
    assert odd_numbers(3, 4) == [3]
    assert odd_numbers(4, 5) == []

def test_enumerate_with_index():
    names = ["Ana", "Marko", "Iva"]
    assert enumerate_with_index(names, start=1) == [(1,"Ana"), (2,"Marko"), (3,"Iva")]
    assert enumerate_with_index([], start=10) == []

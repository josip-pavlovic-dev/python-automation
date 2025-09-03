import pytest
from foundations_oop.src.functions_basics import add, add_many, debug_kwargs, greet


def test_greet_default_and_custom():
    assert greet() == "Zdravo, svete!"
    assert greet("Tesla") == "Zdravo, Tesla!"


def test_add_happy_path():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


@pytest.mark.parametrize("nums, expected", [
    ((), 0),
    ((1,), 1),
    ((1, 2, 3), 6),
])
def test_add_many_various(nums, expected):
    assert add_many(*nums) == expected


def test_debug_kwargs_returns_dict():
    d = debug_kwargs(x=1, y=2)
    assert d == {"x": 1, "y": 2}
    assert isinstance(d, dict)

def test_add_with_non_int_arguments_raises_typeerror():
    with pytest.raises(TypeError):
        add("2", 3)

def test_add_many_with_non_int_arguments_raises_typeerror():
    with pytest.raises(TypeError):
        add_many(1, "2", 3)

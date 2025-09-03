from functools import reduce

import pytest

# =====================
# Generators & Iterators
# =====================

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def test_countdown_generator_yields_in_reverse():
    assert list(countdown(3)) == [3, 2, 1]
    assert list(countdown(0)) == []

def test_iter_and_next_protocol():
    it = iter([1, 2, 3])
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    with pytest.raises(StopIteration):
        next(it)

# =====================
# Functional tools
# =====================

def test_map_filter_reduce_workflow():
    nums = [1, 2, 3]
    doubled = list(map(lambda x: x * 2, nums))
    odds = list(filter(lambda x: x % 2, nums))
    total = reduce(lambda a, b: a + b, nums)

    assert doubled == [2, 4, 6]
    assert odds == [1, 3]
    assert total == 6

# =====================
# Docstring & type hints
# =====================

def greet(name: str) -> str:
    """Vrati pozdrav za dato ime."""
    return f"Zdravo, {name}!"

def test_greet_docstring_and_return_type():
    assert greet("Ana") == "Zdravo, Ana!"
    assert isinstance(greet.__doc__, str)
    assert greet.__annotations__ == {"name": str, "return": str}

# =====================
# OOP: property & classmethod
# =====================

class Circle:
    def __init__(self, r): self.r = r
    @property
    def area(self): return 3.14 * self.r**2

def test_property_area_works_like_attribute():
    c = Circle(3)
    assert pytest.approx(c.area, 0.01) == 28.26
    # provera da je property (ne callable method)
    assert not callable(c.area)

class User:
    def __init__(self, name): self.name = name
    @classmethod
    def from_name(cls, n): return cls(n)

def test_classmethod_creates_instance():
    u = User.from_name("Mileva")
    assert isinstance(u, User)
    assert u.name == "Mileva"

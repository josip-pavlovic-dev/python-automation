from foundations_oop.src.counter import Counter

def test_counter_basic():
    c = Counter()
    assert c.count == 0
    assert c.inc() == 1
    assert c.dec() == 0

def test_counter_custom_start_and_step():
    c = Counter(start=10)
    assert c.inc(5) == 15
    assert c.dec(3) == 12

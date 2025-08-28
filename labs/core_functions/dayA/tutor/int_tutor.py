# int_tutor.py — trunc, base, bytes, __int__/__index__
print(int(42.9), int(-3.9))  # 42 -3
print(int("0b101", 0))  # 5 (auto baza)
print(int(b"2a", 16))  # 42


class WithInt:
    def __int__(self):
        return 42


class OnlyIndex:
    def __index__(self):
        return 7


print(int(WithInt()), int(OnlyIndex()))  # 42 7
for bad in ["12.5", (3.0, 10), float("inf")]:
    try:
        if bad == (3.0, 10):
            int(*bad)
        else:
            int(bad)
    except Exception as e:
        print(type(e).__name__)

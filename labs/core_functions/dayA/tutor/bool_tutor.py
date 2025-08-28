# bool_tutor.py — truthiness, __bool__ / __len__ i greška
print(bool(0), bool(1), bool(""), bool("0"), bool([]), bool([0]), bool(None))


class WithBool:
    def __bool__(self):
        return False


class WithLen:
    def __len__(self):
        return 2


print(bool(WithBool()), bool(WithLen()))  # False True


class BadBool:
    def __bool__(self):
        return 2


try:
    bool(BadBool())
except Exception as e:
    print(type(e).__name__)  # TypeError

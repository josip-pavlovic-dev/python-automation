import inspect


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def default_op(*_, **__):
    raise ValueError("Nepoznata operacija")


OPS = {"plus": add, "times": mul}

name = "plus"
func = OPS.get(name, default_op)
print(func(2, 3))  # 5


def f(x: int) -> str:
    """demo doc."""
    return str(x)


print(f.__name__, f.__doc__, f.__annotations__)


def greet(name: str) -> str:
    """Vrati pozdrav za dato ime."""
    return f"Zdravo, {name}!"


print(help(greet), greet.doc__)


def add(a: int, b: int = 0) -> int:
    return a + b


print(help(add), add.__doc__)


class Repeater:
    def __init__(self, word):
        self.word = word

    def __call__(self, n):
        return " ".join([self.word] * n)


def format_kv_amateur(**kwargs):
    result = ""
    for k, v in kwargs.items():
        # konkatenacija stringova sa +=
        result += str(k) + "=" + str(v) + ", "
    return result[:-2]  # skini poslednji zarez i razmak


print(format_kv_amateur(key1=2, key2=4))
# key1=2, key2=4

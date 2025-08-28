# str_tutor.py — str vs repr, decode, __str__ fallback
b = b"abc"
print(str(b))  # "b'abc'" (repr, ne tekst)
print(b.decode())  # 'abc' (tekst)


class NoStr:
    pass


class WithStr:
    def __str__(self):
        return "WithStr::pretty"


print(str(NoStr()))  # repr fallback
print(str(WithStr()))  # WithStr::pretty
try:
    print(str(123, "utf-8"))
except Exception as e:
    print(type(e).__name__)  # TypeError

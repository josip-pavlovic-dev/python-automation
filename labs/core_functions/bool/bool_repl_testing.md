# bool() — REPL plan

```python
help(bool)
print(bool.__doc__)

print(bool(0), bool(1), bool(-1))
print(bool(""), bool("0"))
print(bool([]), bool([0]))
print(bool({}), bool({"k": 1}))
print(bool(None), bool(object()))

class WithBool:
    def __bool__(self): return False
print(bool(WithBool()))   # False

class WithLen:
    def __len__(self): return 2
print(bool(WithLen()))    # True

class BadBool:
    def __bool__(self): return 2
try:
    print(bool(BadBool()))
except Exception as e:
    print(type(e).__name__)  # TypeError
```

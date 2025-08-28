# int() — REPL Testing (copy/paste blokovi)

## Osnovni testovi

```python
int(0), int(1), int(-1)
int(3.9), int(-3.9)           # 3, -3  (trunc prema nuli)
int(True), int(False)         # 1, 0
```

## Strings + base

```python
int("10")                      # 10
int("10", 2)                   # 2
int("0b101", 0)                # 5 (auto-detekcija prefiksa)
int("0x10", 0), int("0o10", 0) # 16, 8

# underscores (ispravno)
int("1_000")                   # 1000
# underscores (neispravno)
try: print(int("1__0"))
except Exception as e: print(type(e).__name__)  # ValueError
```

## Bytes / bytearray

```python
int(b"2a", 16)                 # 42
int(bytearray(b"10"), 2)       # 2
# base samo za tekst/bytes-like
try: print(int(3.0, 10))
except Exception as e: print(type(e).__name__)  # TypeError
```

## Specijalne float vrednosti

```python
import math
try: print(int(float("nan")))
except Exception as e: print(type(e).__name__)  # ValueError

try: print(int(float("inf")))
except Exception as e: print(type(e).__name__)  # OverflowError

int(-0.0)                      # 0
```

## Dunder protokol

```python
class WithInt:
    def __int__(self): return 42

class OnlyIndex:
    def __index__(self): return 7

print(int(WithInt()))          # 42
print(int(OnlyIndex()))        # 7
```

## Negativni primeri (greške)

```python
for bad in ["12.3", "++10", "1_", "_1", "  ", "10a"]:
    try:
        print(bad, "->", int(bad))
    except Exception as e:
        print(bad, "->", type(e).__name__)

try: print(int(None))
except Exception as e: print(type(e).__name__)   # TypeError
```

# Edge-case testovi koje treba probati

```python
# 1) Whitespace i newline – validno parsiranje
print(int("  42\n"))   # 42

# 2) Različite osnove
print(int("1010", 2))  # 10
print(int("FF", 16))   # 255

# 3) Bool vrednosti
print(int(True))       # 1
print(int(False))      # 0

# 4) Greške
try:
    print(int("12.5"))
except Exception as e:
    print(type(e).__name__)   # ValueError
```

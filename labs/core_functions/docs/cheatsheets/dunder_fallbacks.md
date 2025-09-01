# Dunder fallback mapa (brzi podsetnik)

## Pravila (ko zove koga)

- bool(x) → **bool** → **len** → default True
- int(x) → **int** → **index** → TypeError
- str(x) → **str** → **repr** → default object.**repr**
- repr(x) → **repr** (nema fallbacka osim default object.**repr**)
- len(x) → **len** → TypeError (nema fallbacka)
- iter(x) → **iter** → legacy **getitem**(0..)
- x[i] → **getitem**
- x in y → **contains** → fallback na iteraciju (**iter**/**getitem**)
- a + b → **add** → **radd** → TypeError (ako obu strane ne znaju)

## Mini primeri

### bool → len → default

```py
class A: pass
class B:
    def __len__(self): return 0
class C:
    def __bool__(self): return False

bool(A())  # True (default)
bool(B())  # False (len==0)
bool(C())  # False (__bool__ ima prioritet)
```

### int → index

```py
class N:
    def __index__(self): return 7
int(N())  # 7 (fallback na __index__)
```

### str → repr

```py
class S:
    def __repr__(self): return "debug"
str(S())   # "debug" (nema __str__, pa pada na __repr__)
```

---

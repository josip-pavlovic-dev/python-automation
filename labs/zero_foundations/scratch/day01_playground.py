from src.basics.types_scalars import (
    count_truthy,
    first_non_null,
    float_equal,
    norm,
    safe_div,
)

print("safe_div(10, 2) =", safe_div(10, 2))
print("safe_div(10, 0, default=0) =", safe_div(10, 0, default=0))
print("float_equal(0.1+0.2, 0.3) =", float_equal(0.1 + 0.2, 0.3))
print("norm(3,4) =", norm(3, 4))
print("first_non_null(None, None, 'x') =", first_non_null(None, None, "x"))
print("count_truthy([0, '', None, 'ok']) =", count_truthy([0, "", None, "ok"]))


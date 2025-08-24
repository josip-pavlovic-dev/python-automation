from src.basics.exercises_day01 import float_equal

print("\n=== abs() ===")
x = -7
abs_x = abs(x)
print("abs(-7) =", abs_x)
print("type(abs_x) =", type(abs_x))
print("id(x) =", id(x))

print("id(abs_x) =", id(abs_x))  # isti ID ako je broj isti
print("abs(3 + 4j) =", abs(3 + 4j))  # kompleksan broj
print("type(abs(3 + 4j)) =", type(abs(3 + 4j)))

print("\n=== round() ===")
print("round(2.5) =", round(2.5))
print("round(3.5) =", round(3.5))
print("round(2.675, 2) =", round(2.675, 2))
print("bool(round(2.5) == round(3.5)) =", bool(round(2.5) == round(3.5)))

print("\n=== bool() ===")
print("bool('') =", bool(""))
print("bool(0) =", bool(0))
print("bool(123) =", bool(123))
print("bool([]) =", bool([]))

print("\n=== float_equal() ===")
print("float_equal(0.1 + 0.2, 0.3) =", float_equal(0.1 + 0.2, 0.3))
print("float_equal(1.0000001, 1.0) =", float_equal(1.0000001, 1.0))
print("float_equal(1.1, 1.0) =", float_equal(1.1, 1.0))

print("\n=== type() & id() tracking ===")
a = 10
b = float(a)
print("a =", a, "| type =", type(a), "| id =", id(a))
print("b = float(a) =", b, "| type =", type(b), "| id =", id(b))

print("\n=== hasattr() ===")
print("hasattr(5, '__abs__') =", hasattr(5, "__abs__"))  # True
print("hasattr('text', '__abs__') =", hasattr("text", "__abs__"))  # False
print("hasattr(None, '__abs__') =", hasattr(None, "__abs__"))  # False

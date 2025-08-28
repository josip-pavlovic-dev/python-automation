# int_tutor_template.py — fokusirani Python Tutor primeri
# 1) Otvori https://pythontutor.com/python-visualize.html
# 2) Nalepi kod i klikni RUN; pomiči korak-po-korak i prati promene.

print("1) Brojevi i trunc prema nuli")
x1 = 3.9
x2 = -3.9
print(int(x1))  # 3  -> float -> int (trunc prema 0)
print(int(x2))  # -3 -> negativan trunc

print("\n2) Bool vrednosti")
print(int(True), int(False))  # 1 0

print("\n3) Strings sa base")
s_bin = "0b101"
s_hex = "0x10"
print(int(s_bin, 0))  # 5  -> base=0 auto-detekcija prefiksa 0b
print(int(s_hex, 0))  # 16 -> base=0 auto-detekcija prefiksa 0x

print("\n4) Underscores u stringu")
s_u = "1_000"
print(int(s_u))  # 1000 -> underscores dozvoljeni u pravilnim pozicijama

print("\n5) Bytes/bytearray parsing")
b = b"2a"
ba = bytearray(b"10")
print(int(b, 16))  # 42 -> bytes interpretiran kao ASCII cifre u osnovi 16
print(int(ba, 2))  # 2  -> bytearray kao ASCII cifre u osnovi 2

print("\n6) Dunder protokol: __int__ i __index__")


class WithInt:
    def __int__(self):  # Python poziva __int__ pri int(obj)
        return 42


class OnlyIndex:
    def __index__(self):  # Fallback za celobrojni prikaz
        return 7


w = WithInt()
oi = OnlyIndex()
print(int(w))  # 42
print(int(oi))  # 7

print("\n7) Greške: ValueError, TypeError, OverflowError")
try:
    print(int("12.3"))  # nije ceo broj u stringu
except Exception as e:
    print(type(e).__name__)  # ValueError

try:
    print(int(3.0, 10))  # base uz ne-string ulaz
except Exception as e:
    print(type(e).__name__)  # TypeError

try:
    print(int(float("inf")))  # beskonačnost -> ne može u int
except Exception as e:
    print(type(e).__name__)  # OverflowError

print("\n8) Edge detalji")
print(int(-0.0))  # 0 -> -0.0 kao float postaje 0 int

print("\n9) Edge-case testovi (razmaci, base, bool, greške)")

print(int("  42\n"))  # 42 -> dozvoljeni whitespace
print(int("1010", 2))  # 10 -> binarni string
print(int("FF", 16))  # 255 -> heksadecimalni string

print(int(True))  # 1
print(int(False))  # 0

try:
    print(int("12.5"))  # nije ceo broj
except Exception as e:
    print(type(e).__name__)  # ValueError

# str() — Python Tutor template

# 1) Otvori https://pythontutor.com/python-visualize.html, nalepi kod i klikni RUN.
# 2) Pomiči korak-po-korak i prati kako vrednosti teku.
# 3) Zabeleži opažanja u *_analysis_notes.md.


print(str(123))
print(str(None))
print(str(b"ćao", "utf-8"))


class User:
    def __repr__(self):
        return "User(id=1)"

    def __str__(self):
        return "User: #1"


u = User()
print(str(u))  # Koji se metod poziva?
# --- str(): dodatni, fokusirani testovi (edge-cases + praksa) ---

# 1) Brojevi i bool
print(str(0), "# '0'")
print(str(-42), "# '-42'")
print(str(3.1400), "# '3.14'")
print(str(True), str(False), "# 'True' 'False'")

# 2) None i praznine
print(str(None), "# 'None'")
print(str(""), "# '' (prazan string ostaje prazan)")

# 3) Sekvence i kolekcije (str() poziva __str__/__repr__ svakog elementa)
print(str([1, 2, 3]), "# '[1, 2, 3]'")
print(str((1, "a", None)), "# '(1, 'a', None)'")
print(str({}), "# '{}' (prazan dict)")

# 4) bytes / bytearray – razlika str() vs decode()
b = b"hello"
print(str(b), "# \"b'hello'\"  (repr bytes-a)")
print(b.decode(), "# 'hello'      (pravi tekst)")

ba = bytearray(b"hi")
print(str(ba), "# \"bytearray(b'hi')\"")
print(ba.decode(), "# 'hi'")

# 5) encoding/ errors parametri: dozvoljeno SAMO uz bytes-like
print(str(b"\xe2\x9c\x93", "utf-8"), "# '✓'")
# Sledeće DIŽE TypeError jer nije bytes:
try:
    print(str(123, "utf-8"))
except Exception as e:
    print(type(e).__name__, "# očekivano: TypeError")


# 6) Custom objekat bez __str__ -> preuzima se __repr__ iz object-a
class NoStr:
    pass


print(
    type(str(NoStr())) is str, "# True, ali format je <__main__.NoStr object at 0x...>"
)


# 7) Custom objekat sa __str__
class WithStr:
    def __str__(self):
        return "WithStr::pretty"


print(str(WithStr()), "# 'WithStr::pretty'")

# 8) Unicode i escapovi
print(str("šĐćžč ✓"), "# unicode ostaje")
print(str("\n\t"), "# '\n\t' ostaju stvarni kontrolni karakteri, ne \\n literal")

# 9) formatiranje vs str()
x = 12.3456
print(str(x), "# '12.3456'  – bez zaokruživanja")
print(f"{x:.2f}", "# '12.35'    – formatiranje, namerno zaokruži")
print(format(x, ".3f"), "# '12.346'   – isto kao gore ali preko format()")

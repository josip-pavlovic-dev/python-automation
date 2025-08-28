print("1) Truthy / falsy osnove")
print(bool(0), bool(1), bool(-1))
print(bool(""), bool("0"))
print(bool([]), bool([0]))
print(bool(None), bool(object()))

print("\n2) __bool__ ima prioritet")
class WithBool:
    def __bool__(self): return False
print(bool(WithBool()))

print("\n3) __len__ kao fallback")
class WithLen:
    def __len__(self): return 2
print(bool(WithLen()))

print("\n4) Pogrešan povratni tip iz __bool__")
class BadBool:
    def __bool__(self): return 2
try:
    print(bool(BadBool()))
except Exception as e:
    print(type(e).__name__)

print("\n5) Idiomski primer")
xs = []
if xs:
    print("Ima elemenata")
else:
    print("Prazno -> False")

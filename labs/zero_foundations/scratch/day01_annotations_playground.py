def demo_annotations_basics():
    print("=" * 40)
    print("ANNOTATIONS: variable vs runtime")


# 1) Varijabilna anotacija + dodela
xs: list[int] = [10, 20, 20, 30]
print("xs =", xs)

# 2) Runtime je isti kao i bez tipa (anotacija ide u __annotations__)
# Ovo ne baca grešku u runtime-u:
xs = ["a", "b"]  # "pogrešan" tip vs hint
print("xs reassigned to strings:", xs)

# 3) Pogledaj kako Python pamti anotacije na nivou funkcije/scope-a
#    Napomena: u modulu vidiš __annotations__ na globalnom nivou;
#    ovde demonstriramo ideju preko lokalnog prostora imena:
local_annotations = locals().get("__annotations__", {})
print("__annotations__ in this scope:", local_annotations)


def demo_function_hints():
    print("=" * 40)
    print("FUNCTION HINTS: params and return")


def add_one(n: int) -> int:
    return n + 1


# "Namerno pogrešno" u runtime-u (nema greške!):
print("add_one('7') =", add_one("7"))

# konkatenacija stringa i int će dići TypeError tek kad proba da sabere
# zapravo ovde će baciti TypeError pri izvršenju, ali ne zbog hint-a,
# već jer '+' ne radi za str i int

# Pokaži da hint-ovi postoje (alatima korisno, runtime ih ne koristi za enforce):
print("add_one.__annotations__ =", add_one.__annotations__)

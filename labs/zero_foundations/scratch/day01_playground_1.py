#ENG: Run with "python -m scratch.day01_playground" from project root
#SR : Pokreni sa "python -m scratch.day01_playground" iz korena projekta

from src.basics.exercises_day01 import countdown, enumerate_1, is_empty

#ENG: Truthiness demo
#SR : Truthiness demo
print(bool([]))     # False
print(bool(""))     # False
print(bool(0))      # False
print(bool(None))   # False
print(bool(set()))  # False
print(bool([1]))    # True

#ENG: range() examples (stop is exclusive)
#SR : range() primeri (desna granica je ekskluzivna)
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(3, 0, -1)))   # [3, 2, 1]

#ENG: enumerate() examples
#SR : enumerate() primeri
print(list(enumerate(["a","b","c"])))                 # [(0,'a'), (1,'b'), (2,'c')]
print(list(enumerate(["a","b","c"], start=1)))        # [(1,'a'), (2,'b'), (3,'c')]


def demo_truthiness():
    print("=" * 40)
    print("TRUTHINESS DEMO")
    values = [0, 0.0, "", [], {}, set(), None, [1], "tekst", 42]
    for v in values:
        print(f"Value={repr(v):>8} | bool(v)={bool(v)} | is_empty(v)={is_empty(v)}")
    #ENG: empty/falsy → bool(v)=False, is_empty(v)=True
    #SR : prazno/falsy → bool(v)=False, is_empty(v)=True


def demo_countdown():
    print("=" * 40)
    print("COUNTDOWN DEMO")
    for n in [5, 3, 1]:
        print(f"countdown({n}) -> {countdown(n)}")
    #ENG: range(n,0,-1) stops before 0
    #SR : range(n,0,-1) staje pre 0

    # Edge cases
    try:
        print("countdown(0):", countdown(0))
    except Exception as e:
        print("Error with countdown(0):", e)

    try:
        print("countdown(-3):", countdown(-3))
    except Exception as e:
        print("Error with countdown(-3):", e)


def demo_enumerate_1():
    print("=" * 40)
    print("ENUMERATE_1 DEMO")
    xs = ["a", "b", "c"]
    print("Input:", xs)
    print("enumerate_1(xs):", enumerate_1(xs))

    # Nested enumerate
    words = ["Python", "Automation", "Day01"]
    for idx, word in enumerate_1(words):
        print(f"{idx}: {word}")

    # Empty list
    print("enumerate_1([]):", enumerate_1([]))

    # Enumerating over range
    print("enumerate_1(range(3)):", enumerate_1(range(3)))


def demo_combinations():
    print("=" * 40)
    print("COMBINED USAGE DEMO")

    # Filter non-empty values with enumerate_1
    items = ["", "X", [], [1, 2], None, "ok"]
    print("Original items:", items)
    filtered = [(i, x) for i, x in enumerate_1(items) if not is_empty(x)]
    print("Filtered (non-empty):", filtered)

    # Countdown + enumerate
    n = 5
    cd = countdown(n)
    print(f"Countdown list for n={n}:", cd)
    indexed = enumerate_1(cd)
    print("Enumerated countdown:", indexed)

    # Realistic: validate fields
    user_inputs = {"name": "Ana", "email": "", "age": 0}
    print("User inputs:", user_inputs)
    empties = [k for k, v in user_inputs.items() if is_empty(v)]
    print("Empty fields:", empties)


def demo_matrix_enumeration():
    print("=" * 40)
    print("MATRIX ENUMERATION DEMO")
    matrix = [
        [1, 2, 3],
        [4, 5],
        [],
        [6]
    ]
    for row_idx, row in enumerate_1(matrix):
        if is_empty(row):
            print(f"Row {row_idx} is empty")
            continue
        for col_idx, value in enumerate_1(row):
            print(f"Row {row_idx}, Col {col_idx}: {value}")


def demo_identity_vs_equality():
    print("=" * 40)
    print("IDENTITY vs EQUALITY")
    a = [1, 2]
    b = a          # b pokazuje na isti objekat kao a
    c = [1, 2]     # novi objekat sa istim sadržajem

    print("a == b:", a == b)   # True (jednakost po vrednosti)
    print("a is b:", a is b)   # True (identitet: isti objekat)
    print("a == c:", a == c)   # True
    print("a is c:", a is c)   # False (drugi objekat)
    print("ids:", id(a), id(b), id(c))

    # Imutabilni tipovi (str, int)
    s1 = "py"; s2 = "py"
    print("s1 == s2:", s1 == s2)   # True
    print("s1 is s2:", s1 is s2)   # CPython često interniše kratke stringove, ne oslanjaj se na ovo u logici

def demo_mutation_vs_rebinding():
    print("=" * 40)
    print("MUTATION vs REBINDING (+=)")

    # List (mutable): += mutira listu
    xs = [1]
    ys = xs
    xs += [2]   # MUTATION: ys vidi promenu
    print("list xs, ys:", xs, ys)

    # String (immutable): += kreira NOVI objekat (rebinding)
    s = "ab"
    before = id(s)
    s += "c"    # REBINDING
    after = id(s)
    print("str s:", s, "id(before)->id(after):", before, "->", after)

    # Int (immutable): += kreira NOVI objekat
    n = 41
    before_n = id(n)
    n += 1
    after_n = id(n)
    print("int n:", n, "id(before)->id(after):", before_n, "->", after_n)

g = "module-level"

def demo_LEGB_nonlocal_global():
    print("=" * 40)
    print("LEGB / nonlocal / global")

    x = "E"  # Enclosing for outer()

    def outer():
        x = "L"  # Local to outer

        def inner():
            nonlocal x       # menja x iz outer()
            x = "I->changed outer's x"
        inner()
        print("outer.x =", x)

    outer()

    # global primer
    def set_global():
        global g
        g = "changed by set_global"

    print("g BEFORE:", g)
    set_global()
    print("g AFTER :", g)


def demo_mutable_default_args():
    print("=" * 40)
    print("MUTABLE DEFAULT ARGS")

    def bad_add(x, bucket=[]):
        bucket.append(x)
        return bucket

    a1 = bad_add(1)
    a2 = bad_add(2)   # iznenađenje: deli isti 'bucket'
    print("bad_add(1), bad_add(2):", a1, a2)

    def good_add(x, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(x)
        return bucket

    g1 = good_add(1)
    g2 = good_add(2)
    print("good_add(1), good_add(2):", g1, g2)


def main():
    demo_truthiness()
    demo_countdown()
    demo_enumerate_1()
    demo_combinations()
    demo_matrix_enumeration()

    # NEW for L01 mental model:
    demo_identity_vs_equality()
    demo_mutation_vs_rebinding()
    demo_LEGB_nonlocal_global()
    demo_mutable_default_args()

if __name__ == "__main__":
    main()

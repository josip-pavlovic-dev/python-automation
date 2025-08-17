#ENG: Run with "python -m scratch.day01_playground" from project root
#SR : Pokreni sa "python -m scratch.day01_playground" iz korena projekta

from src.basics.exercises_day01 import is_empty, countdown, enumerate_1

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

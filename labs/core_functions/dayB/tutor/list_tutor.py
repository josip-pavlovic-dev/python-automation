# list_tutor.py — fokus: mutabilnost, slicing, shallow vs deep
import copy

a = [[1, 2], [3]]
print("orig ids:", id(a), id(a[0]))
a2 = a[:]
a3 = copy.deepcopy(a)
print("a2 ids:", id(a2), id(a2[0]))
print("a3 ids:", id(a3), id(a3[0]))
a[0][0] = -1
print("after:", "a=", a, "a2=", a2, "a3=", a3)

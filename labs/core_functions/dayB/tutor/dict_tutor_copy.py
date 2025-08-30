import copy

d = {"x": [1,2]}
sh = d.copy()
dp = copy.deepcopy(d)
d["x"][0] = 99
print(d, sh, dp)

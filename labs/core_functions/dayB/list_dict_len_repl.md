Hej! Idemo odmah, Dan B (F0) — vodiću te kroz 4 bloka rada, sa REPL-om, implementacijom (CLI), pytest setom (≥12 testova), i dokumentacijom + glossary dopunama. (Ritam i format su po našem dnevnom driveru i kickoff materijalima. )

# 1) REPL & dizajn (list, dict, len) — mini set za labs/dayB/list_dict_len_repl.md

**Predlog fajla:** `labs/dayB/list_dict_len_repl.md`

```python
# === LIST: mutabilnost, slicing, kopije ===
a = [[1, 2], [3]]
print("a id:", id(a), "a[0] id:", id(a[0]))
a2 = a[:]               # shallow copy (slicing)
print("a2 id:", id(a2), "a2[0] id:", id(a2[0]))  # a2[0] je isti objekat kao a[0]!

import copy
a3 = copy.deepcopy(a)   # deep copy
print("a3 id:", id(a3), "a3[0] id:", id(a3[0]))

# Mutacija ugnježdenog elementa
a[0][0] = -1
print("posle:", a, a2, a3)  # a2 je pogođen, a3 nije

# extend vs append
b = [1, 2]; c = [3, 4]
b_append = b.copy(); b_append.append(c)     # [1,2,[3,4]]
b_extend = b.copy(); b_extend.extend(c)     # [1,2,3,4]
print("append:", b_append, "extend:", b_extend)

# Slicing gotchas
s = [0,1,2,3,4]
print(s[1:4], s[:], s[::-1])  # podlista, plitka kopija, reverse

# === DICT: ključevi, get vs [] ===
d = {"x": 1}
print("d['x']:", d["x"])
print("d.get('y'):", d.get("y"), "sa default:", d.get("y", 99))
try:
    print(d["y"])       # KeyError
except Exception as e:
    print(type(e).__name__)

# hashability
try:
    k = []
    dd = {k: "nece proci"}  # list nije hashable
except Exception as e:
    print("unhashable key:", type(e).__name__)

t = (1,2)   # tuple je hashable (ako su svi elementi hashable)
dd2 = {t: "ok"}
print("tuple key radi:", dd2[t])

# === len: __len__ i greške ===
class BadLen:
    def __len__(self): return -1

try:
    len(BadLen())   # len mora vratiti nenegativan int -> ValueError
except Exception as e:
    print("len() negative:", type(e).__name__)

# truthiness uz len (prazne kolekcije su falsy)
print(bool([]), bool([0]), bool({}), bool({"a":1}))
```

Brzi “decision tree” (mentalna mapa):

- Treba mi kopija liste?

  - Plitka (struktura ista, unutrašnji objekti deljeni) → `a[:]` ili `list(a)` ili `copy.copy(a)`
  - Duboka (nezavisni unutrašnji objekti) → `copy.deepcopy(a)`

- Treba mi ključ u dict?

  - Da izbacim grešku ako ne postoji → `d[key]`
  - Da vratim default/None ako ne postoji → `d.get(key, default)`

- `len(x)` mora vratiti **nenegativan int**; negativno → `ValueError`. (Ujedno utiče na truthiness; vidi i pravila bool/len protokola. )

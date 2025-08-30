# list — Cheatsheet

- Mutabilna sekvenca; slicing (`a[:]`) pravi **plitku** kopiju.
- `append(x)` dodaje 1 element; `extend(iter)` razvlači elemente iterabla.
- Plitka vs duboka: `copy.copy(a)` vs `copy.deepcopy(a)` (nezavisnost unutrašnjih objekata).
- Idiomi: reverse `a[::-1]`, kopija `a[:]` ili `a.copy()`.

---

## 1. Kreiranje

```python
xs = []                   # prazna lista
ys = [1, 2, 3]            # sa elementima
zs = list("abc")          # ['a', 'b', 'c']
```

## 2. Indeksiranje

```python
xs = [10, 20, 30]
xs[0]    # 10  (prvi)
xs[-1]   # 30  (poslednji)
```

## 3. Mutabilnost

```python
xs = [1, 2, 3]
xs[0] = 99
print(xs)   # [99, 2, 3]
```

## 4. Dodavanje i brisanje

```python
xs = [1, 2]
xs.append(3)       # [1, 2, 3]
xs.extend([4, 5])  # [1, 2, 3, 4, 5]
xs.insert(1, 99)   # [1, 99, 2, 3, 4, 5]
xs.pop()           # vrati i ukloni poslednji → 5
xs.remove(99)      # ukloni prvi 99
```

## 5. Slicing (uvek nova lista)

```python
xs = [0,1,2,3,4,5]
xs[1:4]    # [1,2,3]
xs[:3]     # [0,1,2]
xs[::2]    # [0,2,4]
xs[::-1]   # [5,4,3,2,1,0] (reversed)
```

## 6. Kopije

```python
import copy

a = [[1,2],[3]]

alias   = a                # nema kopije
shallow = a[:]              # nova spolja, deli unutra
deep    = copy.deepcopy(a)  # sve novo

a[0][0] = -1
print(alias[0][0])   # -1 (isti objekat)
print(shallow[0][0]) # -1 (dele unutrašnjost)
print(deep[0][0])    # 1  (nezavisno)
```

## 7. Multiplication gotcha

```python
grid = [[0]*3]*2
grid[0][0] = 1
print(grid)   # [[1,0,0],[1,0,0]] → deli unutrašnje liste

# Rešenje:
grid_ok = [[0]*3 for _ in range(2)]
grid_ok[0][0] = 1
print(grid_ok)  # [[1,0,0],[0,0,0]]
```

## 8. Korisne metode

```python
xs = [3,1,2]
xs.sort()             # [1,2,3] (in-place)
xs.reverse()          # [3,2,1] (in-place)
ys = sorted(xs)       # [1,2,3] (nova lista)
zs = xs[::-1]         # reversed kopija
```

## 9. Membership i dužina

```python
xs = [10,20,30]
10 in xs      # True
99 in xs      # False
len(xs)       # 3
```

## 10. Iteracija

```python
for x in [1,2,3]:
    print(x)
# 1
# 2
# 3
```

---

## 🧠 Pojmovi

- **mutabilna**: možeš menjati sadržaj bez novog objekta (`id` ostaje isti).
- **shallow copy**: kopira spolja, deli unutrašnjost.
- **deep copy**: rekurzivno kopira i unutrašnje objekte.
- **alias**: drugo ime za isti objekat (`b = a`).
- **slicing**: presecanje liste; uvek daje novu listu.

---

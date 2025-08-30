# 🐍 REPL sesija: alias vs shallow vs deep (10 koraka)

## 1) Početna struktura + identitet

```python
a = [[1, 2], [3]]
print(a, type(a))           # [[1, 2], [3]] <class 'list'>
print(id(a))                # npr. 1407...  (tvoj će biti drugačiji)
```

## 2) Alias (drugo ime za isti objekat)

```python
alias = a
print(alias is a)           # True  (isti objekat)
print(id(alias), id(a))     # isti ID
```

## 3) Shallow (kopija spoljne liste)

```python
shallow = a[:]              # isto bi radilo: list(a) ili a.copy()
print(shallow is a)         # False (nova spoljna lista)
print(id(shallow), id(a))   # različiti ID-ovi (spolja)
print(id(shallow[0]) == id(a[0]))  # True  (dele unutrašnju listu!)
```

## 4) Deep (kopija i spolja i unutra)

```python
import copy
deep = copy.deepcopy(a)
print(deep is a)            # False
print(id(deep), id(a))      # različito (spolja)
print(id(deep[0]) == id(a[0]))  # False (unutrašnja lista je nova)
```

## 5) Promena duboko – efekat na alias

```python
a[0][0] = 99
print("a   :", a)           # [[99, 2], [3]]
print("alias:", alias)      # [[99, 2], [3]]  (isti objekat)
```

## 6) Promena curi na shallow (deli unutrašnjost)

```python
print("shallow:", shallow)  # [[99, 2], [3]]  (curi jer deli unutrašnjost)
```

## 7) Deep je nezavisan (nema curenja)

```python
print("deep:", deep)        # [[1, 2], [3]]  (ostaje isto)
```

## 8) Dokaz identitetom (ID-ovi)

```python
print("id a[0]     =", id(a[0]))
print("id shallow[0] =", id(shallow[0]))  # isti kao a[0]
print("id deep[0]    =", id(deep[0]))     # drugačiji
```

## 9) “Multiply gotcha” – reference se ponavljaju

```python
grid = [[0]*3]*2
print(grid)                 # [[0,0,0],[0,0,0]]
print(id(grid[0]), id(grid[1]))  # isti ID -> ista unutrašnja lista
grid[0][0] = 1
print(grid)                 # [[1,0,0],[1,0,0]]  (curi)
```

## 10) Ispravno pravljenje matrice (nezavisne unutrašnje liste)

```python
grid_ok = [[0]*3 for _ in range(2)]
print(id(grid_ok[0]), id(grid_ok[1]))  # različiti ID-ovi
grid_ok[0][0] = 1
print(grid_ok)              # [[1,0,0],[0,0,0]]
```

---

## Mini-cheatsheet (za pamćenje)

- **alias**: `b = a` → sve isto (spolja i unutra).
- **shallow**: `a[:]`, `list(a)`, `a.copy()` → nova spoljna lista, **deli** unutrašnje.
- **deep**: `copy.deepcopy(a)` → sve novo (spolja + unutra).
- **množenje listi**: `[[0]*M]*N` → **ponavlja reference** (gotcha).
  Ispravno: `[[0]*M for _ in range(N)]`.

---

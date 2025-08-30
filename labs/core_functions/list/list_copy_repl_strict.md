# 🐍 REPL sesija (strict varijanta sa assert-ima)

Ovo je ista logika kao prethodno, ali ovde svaki korak proveravaš `assert`-om – odmah vidiš ako nešto ne važi.

---

## 1) Alias = isto ime

```python
a = [1, 2]
alias = a
assert alias is a
a[0] = 99
assert alias[0] == 99
```

---

## 2) Shallow = nova spoljna lista

```python
a = [[1, 2], [3]]
shallow = a[:]
assert shallow is not a
assert shallow[0] is a[0]   # dele unutrašnju listu
a[0][0] = 42
assert shallow[0][0] == 42  # curi unutra
```

---

## 3) Deep = sve nove kopije

```python
import copy
a = [[1, 2], [3]]
deep = copy.deepcopy(a)
assert deep is not a
assert deep[0] is not a[0]  # nova unutrašnja lista
a[0][0] = 99
assert deep[0][0] != 99
```

---

## 4) Multiply gotcha

```python
grid = [[0]*3]*2
assert id(grid[0]) == id(grid[1])  # iste reference
grid[0][0] = 1
assert grid == [[1,0,0],[1,0,0]]
```

---

## 5) Multiply fix

```python
grid_ok = [[0]*3 for _ in range(2)]
assert id(grid_ok[0]) != id(grid_ok[1])
grid_ok[0][0] = 1
assert grid_ok == [[1,0,0],[0,0,0]]
```

---

📌 Ideja: sve što si radio “mentalno” sad ima i **proveru** – ako `assert` ne uspe, odmah pukne i znaš da nisi dobro shvatio ponašanje.

---

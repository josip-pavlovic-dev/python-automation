# 📊 Poster: Alias vs Shallow vs Deep copy

Zamisli listu `a = [[1,2],[3]]`.

## Alias

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

alias ──────────────────────────────┘
```

👉 `alias = a` → oba imena pokazuju na ISTU spoljnu listu i iste unutrašnje objekte.

---

## Shallow copy

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

shallow ─► [ ┌──► [1,2] (ista lista kao u a)
             └──► [3]   (ista lista kao u a) ]
```

👉 `shallow = a[:]` → nova spoljna lista, ali unutrašnje su iste.

---

## Deep copy

```text
a ───► [ ┌──► [1,2]
         └──► [3] ]

deep ─► [ ┌──► [1,2] (NOVA kopija!)
          └──► [3]   (NOVA kopija!) ]
```

👉 `deep = copy.deepcopy(a)` → sve kopirano, spoljno i unutrašnje.

---

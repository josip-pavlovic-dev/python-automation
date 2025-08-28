# list — Cheatsheet

- Mutabilna sekvenca; slicing (`a[:]`) pravi **plitku** kopiju.
- `append(x)` dodaje 1 element; `extend(iter)` razvlači elemente iterabla.
- Plitka vs duboka: `copy.copy(a)` vs `copy.deepcopy(a)` (nezavisnost unutrašnjih objekata).
- Idiomi: reverse `a[::-1]`, kopija `a[:]` ili `a.copy()`.

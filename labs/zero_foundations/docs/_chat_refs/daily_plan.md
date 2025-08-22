# Daily Plan

## 1. Početak – intuicija

- Imaš funkciju `float_equal(a, b, eps=1e-9)` → odmah vidiš da upoređuje `float` vrednosti.
- Ali znaš da `float` ume da vara (`0.1 + 0.2 != 0.3`), pa te zanima: _šta koristi unutra?_ → `math.isclose`.

---

## 2. Pylance (intellisense u VS Code-u)

- **Hover** mišem preko `math.isclose` → Pylance ti prikaže **potpis** i kratak docstring.
  Primer:

  ```python
  isclose(a: float, b: float, *, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> bool
  ```

- Ako ti hover nije dovoljan, koristi **Ctrl+Shift+Space** (Signature Help) dok kucaš `math.isclose(`.
- Ako želiš ceo opis: **Go to Definition (F12)** ili **Peek Definition (Alt+F12)** → videćeš kod ili C-extension stub.

👉 Ovo je prvi sloj: brzo saznaješ potpis i koje argumente ima.

---

## 3. Ruff

- Ruff proverava stil i potencijalne greške.
- Na primer, ako napišeš `a == b` za float, Ruff ti može prijaviti upozorenje (`PLR0133`) i sugerisati `math.isclose`.
- Ruff takođe proverava neiskorišćene promenljive, import-ove, preduge linije…
- Poenta: **Ruff ti signalizira da tvoj pristup poređenju float-a može biti loš**.

---

## 4. REPL (interaktivno ispitivanje)

Pokreneš Python (`python` ili `ipython`) i kucaš:

```python
import math
help(math.isclose)
```

Dobićeš celokupnu dokumentaciju direktno iz standardne biblioteke (isto kao što bi ChatGPT rekao, ali provereno 100%).
Ako želiš samo docstring:

```python
print(math.isclose.__doc__)
```

Ako želiš da testiraš:

```python
math.isclose(0.1 + 0.2, 0.3)
math.isclose(1000, 1001, rel_tol=0.001)
math.isclose(1e-9, 0.0, abs_tol=1e-8)
```

👉 Tako eksperimentišeš i dobijaš osećaj _kako funkcija reaguje_.

---

## 5. Sklapanje slike

- **Pylance** ti kaže: kako se funkcija koristi (potpis, tipovi).
- **Ruff** ti sugeriše ako radiš nešto loše (npr. `a == b` umesto `isclose`).
- **REPL** ti daje dokumentaciju i interaktivno igralište da probaš edge slučajeve.
- Ako želiš i korak dalje: otvori zvaničnu dokumentaciju u browseru (F1 → “Python: Search Online Docs”).

---

## 6. „Amateur mod“ mindset

Pitanja koja bi postavio sam sebi:

- Šta znači `rel_tol` a šta `abs_tol`?
- Kada bih koristio jedno, a kada drugo?
- Šta je default? (rel_tol=1e-9 → vrlo stroga tolerancija)
- Koji su edge slučajevi? (`NaN`, `inf`, brojevi različitih magnituda)
- Da li mi moja `float_equal` funkcija samo prepisuje `math.isclose`, ili dodaje neku vrednost (npr. default eps)?

---

💡 Ukratko:

- **Pylance** → potpis i kratak opis odmah dok kucaš.
- **Ruff** → upozorenje da običan `==` nije dobar, predlog da koristiš `math.isclose`.
- **REPL (help, dir, **doc**)** → ceo opis i eksperimentisanje.
- **Eksperimenti** → sami testovi daju ti osećaj šta radi.

---

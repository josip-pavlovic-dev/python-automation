# 🧭 dict: `get()` vs `[]` i `KeyError`

Cilj: bezbedan pristup vrednosti kada ključ možda ne postoji.

---

## A) Indexing: d[k]

Semantika:

- PRETPOSTAVLJA da ključ POSTOJI.
- Ako ne postoji → baca KeyError.

ASCII:
d = {"a": 1}

         +-------------+
    "a"  |     1       |   d["a"] → 1
         +-------------+

         +-------------+
    "x"  |    nema     |   d["x"] → KeyError: 'x'
         +-------------+

---

## B) get: d.get(k, default=None)

Semantika:

- Ako ključ postoji → vrati vrednost.
- Ako ne postoji → vrati default (po difoltu None).
- NIKAD ne baca KeyError.

ASCII tok:
postoji? ──► DA ──► vrati d[k]
└► NE ──► vrati default (npr. 99 ili None)

---

## C) setdefault: d.setdefault(k, default)

Semantika:

- Ako ključ ne postoji → d[k] = default i VRATI default.
- Ako postoji → VRATI postojeću vrednost (bez zamene).

ASCII:
d = {}
d.setdefault("items", []) ──► d = {"items": []}
d.setdefault("items", []).append("x") ──► {"items": ["x"]}

⚠ Gotcha:
d.setdefault("k", []).append(v) # vraća None jer append mutira listu in-place

---

## D) pop: d.pop(k, default=MISSING)

- Ukloni i vrati d[k].
- Ako ne postoji i default NIJE dat → KeyError.
- Ako default JESTE dat → vrati default (bez greške).

---

## E) Najčešći obrasci

- Bezbedno čitanje: v = d.get("user", "guest")
- Uklanjanje bez greške: v = d.pop("user", None)
- Gradnja liste u mapi: d.setdefault("items", []).append(x)
- Tvrdi zahtev: v = d["user"] # ako ključ mora postojati

Kratko pravilo:

- Nisi siguran da ključ postoji? → `get`
- Želiš da padne fail fast? → `[]`
- Želiš da kreiraš pa koristiš? → `setdefault`
- Želiš da ukloniš bezbolno? → `pop(..., default)`

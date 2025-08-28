# dict — Cheatsheet

- Mapping: ključevi moraju biti **hashable** (npr. tuple, int, str).
- Pristup: `d[key]` → **KeyError** ako nema; `d.get(key, default)` → bez greške.
- Membership: `k in d` proverava **ključeve**.

# `int()` – Cheatsheet (Mentor + Junior)

> Cilj: sigurna konverzija u celobrojni tip, razumevanje **trunc prema nuli**, `base` parametra i dunder protokola (`__int__`, `__index__`).
> Radi paralelno u REPL-u i zapisuj opažanja.

## 1) Brzi mentalni model

**Mentor:** `int(x)` pretvara `x` u **celi broj**. Ako je `x` broj (npr. `float`), rezultat je **trunc prema nuli**. Ako je `x` tekst ili bytes-like, parsira cifre uz zadatu osnovu (`base`).
**Junior:** Znači `int(-1.9)` je `-1`, ne `-2`?
**Mentor:** Tačno. To je trunc, a ne floor.

## 2) Potpis i ograničenja

```python
int(x=0) -> int
int(x: str | bytes | bytearray, base=10) -> int
```

- `base` je u opsegu **2..36** ili **0** (auto-detekcija prefiksa `0x/0o/0b`). Drugačije → `ValueError`.
- `base` **ne sme** da se koristi ako `x` nije `str`/`bytes`/`bytearray` → `TypeError`.
- Whitespace i znak `+`/`-` u stringu su dozvoljeni; podržani su i **underscores** (`"1_000"` → `1000`) ako su ispravno postavljeni.
- `bytes`/`bytearray` se tumače kao **ASCII** cifre; **nema** `encoding` parametra (za razliku od `str()`).

## 3) Tipični primeri

```python
int(42.9)        # 42  (trunc prema 0)
int(-1.9)        # -1
int(True), int(False)     # 1, 0
int("10")        # 10
int("10", 2)     # 2
int("0b101", 0)  # 5 (auto baziranje)
int("1_000")     # 1000 (underscores OK)
int(b"2a", 16)   # 42
```

**Mini-pravilo:** Brojevi → `int(x)`. Tekst/bytes → `int(x, base)` ili `base=0` za auto.

## 4) Dunder protokol

- Ako objekat ima `__int__`, `int(x)` poziva to.
- Ako nema `__int__`, ali ima **`__index__`** (tačan celobrojni prikaz), `int(x)` može iskoristiti to kao fallback (korisno za tipove koji reprezentuju celobrojnu veličinu).
- Za `float` i slične, primenjuje se trunc prema nuli.

**Junior:** A `__trunc__`?
**Mentor:** `math.trunc(x)` koristi trunc protokol; `int(x)` se u praksi oslanja na `__int__`/`__index__` za objekte i na “trunc” za numeričke tipove.

## 5) Tipične greške

- `int("12.3")` → `ValueError` (string mora biti ceo broj, bez decimalne tačke).
- `int("1__0")` ili `int("_100")` → `ValueError` (loš underscore).
- `int(float("nan"))` → `ValueError`; `int(float("inf"))` → `OverflowError`.
- `int(3.0, 10)` → `TypeError` (zato što je `base` dozvoljen samo uz `str/bytes/bytearray`).

## 6) Brzi REPL check-list

- [ ] `int()` na `bool`, `float` (pozitivni/negativni), `None` (očekuj `TypeError`).
- [ ] `int()` na `str` sa `base`, uključujući `base=0` i prefikse `0b/0o/0x`.
- [ ] `int()` na `bytes` i `bytearray`.
- [ ] `int()` na custom klasu sa `__int__` i drugu sa samo `__index__`.

## 7) Profesionalni moment (QA / logika / testovi)

- Kada parsiraš korisnički unos ili fajl → uvek očekuj `ValueError` i hvataj ga.
- Za protokole i low-level API-je → razmisli o implementaciji `__index__` ako tip predstavlja prirodno celobrojnu veličinu (npr. veličina u bajtima).
- U izveštajima: `int()` nije formatiranje – to je konverzija. Za formatiranje koristi `f"{x:d}"` ili `format(x, "d")`.

## 8) Decision tree

1. Da li je `x` već broj? → **Da** → `int(x)` (trunc).
2. `x` je `str`/`bytes`/`bytearray`? → **Da** → `int(x, base)` ili `base=0` (auto).
3. Custom tip? → Implementiraj `__int__` ili bar `__index__`.
4. Očekuješ nevalidan unos? → Okruži `try/except` (`ValueError`/`TypeError`).

---

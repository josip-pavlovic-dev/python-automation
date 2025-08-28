# str_analysis_notes.md — vodič za popunjavanje analysis

> Cilj: da samostalno _dokažeš_ razumevanje `str()` kroz REPL i Python Tutor.

## 0) Potpis i intuicija

- Zapiši potpis `str()` (oba oblika).
- Ukratko: “pretvara objekt u _čitljiv_ string; za bytes koristim decode”.

## 1) Ulazi i izlazi (REPL)

- Napravi tabelu: ulaz → izlaz (int/float/bool/None/list/tuple/dict).
- Dodaj bytes/bytearray + _razliku_ `str(x)` vs `x.decode()`.

## 2) Dunder metode

- Napravi dve klase: `NoStr` (bez `__str__`), `WithStr` (sa `__str__`).
- REPL: `str(NoStr())` i `str(WithStr())` → zapiši zaključak “fallback na **repr**”.

## 3) Greške

- `str(123, "utf-8")` → očekivano: `TypeError`
- `str(b"\xff", "utf-8", "strict")` → `UnicodeDecodeError` (što je OK, pokaži “errors='ignore'”)

## 4) str vs repr vs format

- REPL blok: `str(12.3456)`, `repr(12.3456)`, `f"{12.3456:.2f}"`.
- Napiši **pravilo kada šta** koristiš u praksi (log, korisnički ispis, debug).

## 5) Python Tutor mini-skripta

- 8–10 linija iz `str_tutor_template.py` (conversions + custom tipovi).
- Zabeleži _šta se menja u frame-ovima_ i **zašto**.

## 6) Zaključci & “što sa posla”

- Šta ćeš proveravati PRVO kad vidiš `b'...'` u logu?
- Kako izbeći `TypeError` kod `str(..., encoding=...)`?
- Koje 2–3 format pravila ćeš uvek koristiti (npr. dve decimale u izveštajima).

> Kad popuniš, pošalji mi dokument na brzi senior review.

---

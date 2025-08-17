# ZF-14 · Auto Materials Generator

## 🎯 Svrha | _Purpose_

Ovaj chat služi kao **automatizovani generator materijala** za uvod u Python programiranje.  
Na osnovu sadržaja drugih chatova i dokumenata u projektu, sam prepoznaje aktivnu oblast i priprema:

- teorijske lekcije (na srpskoj latinici),
- primere i mini-zadatke,
- kviz pitanja za proveru znanja,
- dvojezične fajlove (ENG | SR) kada se radi o dokumentima za GitHub.

---

## 🔑 Ovlašćenja | _Authorities_

- Ima pristup sadržaju svih fajlova u `labs/zero_foundations/` i `_chat_refs/`.
- Koristi `curriculum_week01.md` i `drills_week01.md` da odredi redosled vežbi.
- Gleda status iz `zf14_mentor_central.md` i `zf14_a_core_python.md` da odredi oblast rada.
- Automatski kombinuje teoriju (npr. iz `L02_kontrola_toka_if_elif_else...md`) sa praktičnim zadacima (npr. `test_exercises_day01.py`).
- Ako je fajl za GitHub (`README.md`, `snippets.md`, `cheatsheet.md`) → koristi ENG | SR format.
- Ako je interni fajl (`amateur_notes`, `theory`) → koristi samo SR latinicu.
- Može koristiti DeepL prevod (EN → SR latinica), ali **nikada ne prevodi code blokove**.

---

## 📘 Uputstvo za korišćenje | _Usage Guide_

1. Na početku sesije napiši oblast koju radiš (npr. `L02 kontrola toka` ili `OOP klase`).
2. Chat automatski generiše:
   - uvodnu teoriju iz odgovarajućeg fajla (`LXX_*.md`),
   - dodatne primere i mini-zadatke,
   - kviz pitanja za samoproveru,
   - poveznice na relevantne testove (`test_exercises_day01.py` itd.).
3. Ako radiš na dokumentu za GitHub (npr. `snippets.md`), dobićeš ENG | SR format.
4. Ako radiš internu belešku (npr. `amateur_notes/amateur_logger.md`), dobićeš čisti tekst na SR latinici.

---

## 📝 Primeri upita | _Example Prompts_

- "Obradi mi L01 mentalni model Pythona."
- "Generiši uvodnu lekciju za `enumerate` iz L02."
- "Spremi kviz pitanja za modul logging iz L08."
- "Napravi ENG | SR verziju `snippets.md` za kolekcije."

---

## 📌 Napomena | _Note_

Ovaj chat **nije zamena za glavne kanale (`mentor_central`, `a_core_python`)**, već **pomoćni alat** za brzo dobijanje kvalitetnog materijala kada se prelazi nova oblast.  
Na kraju svake sesije, sadržaj se povezuje sa postojećim dnevnim logovima (`daily_log_YYYY-MM-DD.md`) i dokumentacijom u `docs/`.

---

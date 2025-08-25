# 🔍 Daily Function Analysis Template | _Dnevna analiza funkcije_

## 🧠 1. Intuitivni pregled | _Intuitivno razumevanje_

- ✅ Ime funkcije: `...`
- ✅ Prva pretpostavka: Šta funkcija radi na osnovu imena i potpisa?
- ✅ Da li podrazumeva transformaciju, validaciju, IO ili pomoćnu logiku?
- ✅ Koji tipovi su u pitanju (`int`, `float`, `list`, ...)?
- ✅ Ima li `default` vrednosti? Keyword-only parametara?

---

## 🧭 2. Pylance i Ruff alati | _Korišćenje VS Code alata_

- 🧩 **Hover**: da li prikazuje potpuni potpis i kratak opis?
- 🧩 **Ctrl+Shift+Space (Signature Help)**: prikazuje li korisne informacije tokom poziva?
- 🧩 **F12 / Alt+F12**: `Go to` ili `Peek Definition` — da li vidim internu logiku?
- 🧩 **Ruff upozorenja**: da li se pojavio neki `PLR`, `F`, `E`, `B` warning?
  - Ako da: _Koji warning? Šta on znači?_
- 🧩 **Lint info**: da li mi sugeriše poboljšanja stila, tipova ili logike?

---

## 🔬 3. REPL istraživanje | _Eksperimenti u terminalu_

- 📥 Import funkcije: `from src.basics.exercises_day01 import ...`
- 🧪 `help(...)`: Šta prikazuje?
- 📘 `print(....__doc__)`: Kratak docstring?
- 🧠 Direktno testiranje:
  - Primer 1: ...
  - Primer 2: ...
  - Edge case: ...
- 🌀 Da li sam primetio ponašanje koje nisam očekivao?

---

## 🧪 4. Mini test plan | _Test primeri koje bih napisao_

| Ulaz | Očekivani izlaz | Napomena                      |
| ---- | --------------- | ----------------------------- |
| ...  | ...             | normalni slučaj               |
| ...  | ...             | ivica (npr. `None`, `0`)      |
| ...  | ...             | ekstrem (npr. `float("inf")`) |

---

## 🧭 5. Python Tutor (vizuelna analiza) | _Za složenije funkcije_

- 🔗 Link: https://pythontutor.com/render.html#mode=edit
- 📌 Koraci:
  - Kopiraj funkciju u editor
  - Pokreni `Visualize Execution`
  - Klikći `Next` i posmatraj:
    - Promene u memoriji
    - Tok kontrole (`if`, `for`, `return`)
    - Povratne vrednosti
- 📍 Zaključak iz vizuelizacije:
  - ...
  - ...

---

## ❗ 6. Zaključci i pitanja za Seniora | _Refleksija i nedoumice_

- ❓ Da li su mi svi parametri jasni?
- ❓ Da li funkcija mutira ili vraća novu vrednost?
- ❓ Da li koristi `float`, `None`, `set`, `dict` – treba li paziti na nešto specifično?
- ❓ Da li bih znao da je implementiram sam?
- ❓ Da li bih znao da napišem bar 2 pytest testa?

---

## ✅ 7. Checklist | _Mentalni pregled_

- [ ] Potpuno razumem ugovor funkcije (input → output).
- [ ] Razumem kako bih testirao funkciju (pozitivni i edge slučajevi).
- [ ] Znam kako bih modifikovao ponašanje (npr. da menjam default).
- [ ] Znam gde bih pogledao dodatnu dokumentaciju (`math`, `pathlib`, itd.).
- [ ] Imam bar 2 primera za dnevnu vežbu.

---

## 🗂 8. Fajl u kom se nalazi + povezana vežba

- 📄 Fajl: `src/basics/exercises_day01.py`
- 🧪 Test fajl: `tests/test_exercises_day01.py`
- 📘 Vezba: `L01_L016_plan.md` → Dan X

---

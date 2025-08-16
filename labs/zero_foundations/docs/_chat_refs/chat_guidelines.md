# 📘 ZF-14 • Chat Guidelines

> Ovaj dokument je „ustav“ za rad u chatovima tokom **Zero Foundations (ZF-14)** sprinta.
> Cilj je da svaki chat ima jasan _scope_, definiciju završetka (DoD), i predvidljiv ritam rada.
> Jezik: srpska latinica. Stil: formalan, profesionalan i praktičan; „senior + junior“ mod.

---

## 1) Principi

- **Jedan chat = jedna tema (scope).** Pitanja i kod ostaju u granicama tog chata.
- **DoD pre prelaska dalje.** Ne prelazimo na sledeću temu dok DoD nije ispunjen.
- **Male iteracije.** Kratke poruke, konkretni koraci, brzi feedback loop.
- **Uvek merenje.** Svaki dan: šta je zeleni test, koji je commit, koja je lekcija zatvorena.
- **Repo je „source of truth“.** Ključni sadržaji iz chatova čuvaju se kao `.md` fajlovi u repou.
- **Bez rupa u znanju.** Ako nešto ne razumeš, pauziramo i „spuštamo nivo“ do kristalnog razumevanja.

---

## 2) Hijerarhija i scope chatova

> Nazive drži dosledno da bi pretraga i navigacija bile lake.

- **`ZF-14 | Mentor Central (hub)`**  
  **Scope:** plan dana/nedelje, DoD, blokade, hand-off, retro.  
  **Nije za kod**, već za organizaciju i odluke.  
  **DoD:** dnevni plan postavljen i zatvoren; nedeljni rezime upisan.

- **`ZF-14 | A — Core Python (L01–L06)`**  
  **Scope:** sintaksa, kontrola toka, funkcije, kolekcije, moduli/venv, fajlovi (`pathlib`).  
  **DoD:** zeleni testovi za `exercises_day01.py` i `paths_utils.py` (Week 1).

- **`ZF-14 | B — Debug & Logging (L07–L08)`**  
  **Scope:** izuzeci, debugger workflow, `logging` model (logger/handler/formatter).  
  **DoD:** minimalni primeri sa `caplog`, bez duplih handlera.

- **`ZF-14 | C — OOP Foundations (L09–L10)`**  
  **Scope:** klase/objekti, `__init__/self`, `__repr__/__str__`, `@dataclass`, **kompozicija > nasleđivanje**.  
  **DoD:** `Timer` klasa sa testovima; `AppLogger` sa injekcijom handler fabrike.

- **`ZF-14 | D — CLI & Regex (L11–L12)`**  
  **Scope:** `argparse` (argumenti/flagovi/exit kodovi), regex validacije/zamene.  
  **DoD:** mali CLI sa `--verbose` i validacijama; 2 regex zadatka.

- **`ZF-14 | E — Data & Testing (L13–L14)`**  
  **Scope:** JSON/CSV (streaming, validacija), `pytest` osnove (fixture `tmp_path`, `caplog`, `parametrize`).  
  **DoD:** konverter CSV→JSON sa testovima; parametrize primer.

- **`ZF-14 | F — HTTP & Scheduling (L15–L16)`**  
  **Scope:** `requests` (timeout, retry), `python -m`, Task Scheduler/cron, struktura projekta.  
  **DoD:** skripta sa retry i logovanjem + uputstvo za zakazivanje.

- **`ZF-14 | Literatura (ref)`**  
  **Scope:** sažeci čitanja, pitanja za razumevanje, link na `_chat_refs/`.  
  **DoD:** 2–3 kratka sažetka nedeljno, po 3 pitanja/lekciji.

---

## 3) Mapiranje chat ⇄ repo

- **Vault za referentne chatove:** `labs/zero_foundations/docs/_chat_refs/`  
  Primeri: `chat_oop_foundations.md`, `zf14_A_core_python.md` (sažeci i instrukcije).
- **Operativni kod i testovi:** `labs/zero_foundations/src/` i `labs/zero_foundations/tests/`.
- **Teorija i plan:** `labs/zero_foundations/docs/` (`curriculum_week01.md`, `drills_week01.md`, `README.md`).

**Pravilo:** Kad se u chatu donese odluka ili rešenje koje je „zrelo“, prebacuje se u odgovarajući `.md` u repou (kratak commit).

---

## 4) Dnevni ritam (16:00 start)

- **Blok A (Prep, 60–90 min):** teorija + mikro-vežbe → odmah 1–2 testa.
- **Pauza (15–30 min).**
- **Blok B (Build, 60–90 min):** primena na kodu i testovima iz `tests/`.
- **Wrap-up (10–15 min):** `daily_log` + kratka refleksija (šta je kliknulo / šta zapinje).

**DoD dana:** makar jedan _zeleni_ test + commit sa jasnom porukom.

---

## 5) Amateur mod: pravila komunikacije

- **Kada tražiš objašnjenje:** navedi _konkretne_ linije/funkcije i očekivanje („zašto se ovde koristi `enumerate`?“).
- **Kada lepiš kod:** koristi code fence ```python i kratak kontekst (putanja fajla, test koji pada).
- **Kada si blokiran > 15 min:** stavi **BLOCKER** u Mentor Central, priloži minimalan primer.

---

## 6) Kvalitet (što očekujemo od koda)

- PEP 8, **type hints**, i kratak **docstring** na srpskom.
- Zabranjeno: **mutable default** vrednosti, dupliranje handlera u logovanju, „tiha“ `except Exception`.
- Fajlovi: `pathlib`, uvek `encoding="utf-8"` za tekst.
- Testovi: ponašanje, ne implementacija; `pytest -q`; fixture `tmp_path` za I/O.
- Commit poruke: `type(scope): kratko objašnjenje` (npr. `feat(zf-14): implement countdown (day01)`).

---

## 7) Eskalacija i merila

- **Blokada:** 15 min samostalno → 1 pokušaj pretrage → postavi **BLOCKER** u Mentor Central.
- **Nedeljni sync:** `weekly_sync.md` — šta je naučeno, rizici, sledeći fokus.
- **Merenje:** broj zelenih testova, broj dovršenih lekcija (Lxx), mali CLI demo do kraja sprinta.

---

## 8) Kada otvarati nove chatove

- Odmah kada menjaš domen (A→B, B→C…), ili kada stari chat postaje predugačak.
- Naslov uvek sa prefiksom: `[ZF-14]`.
- Prva poruka u novom chatu: **Scope**, **DoD**, aktuelni **task** i linkovi ka testovima.

---

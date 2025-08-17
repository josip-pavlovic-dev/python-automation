# 🗂️ Daily Logs — Vodič, pravila i indeks

Ovaj folder sadrži **dnevne zapise rada** (daily logs). Cilj je jednostavno i proverljivo praćenje napretka:

- svaki dan: rezime, konkretne isporuke, naučeno, blokade (ako ih ima), i kratke komande (ACP);
- jezik: **srpska latinica** (primarno); po potrebi kratka EN napomena u zagradi;
- izvor istine: sve “zrele” odluke i dogovori iz chatova završavaju u ovim `.md` zapisima.

> **Veze na ostale dokumente (relativno):**
>
> - Standup/Wrap-up: `../amateur_notes/chatGPT/daily_standups_&_wrap_ups.md`
> - Navigacija chatova: `../amateur_notes/chatGPT/chats_navigation.md`
> - Chat Guidelines: `../amateur_notes/chatGPT/junior_developer_chatGPT.md`

---

## 📐 Imenovanje i struktura fajla

- **Ime fajla:** `daily_log_YYYY-MM-DD.md` (npr. `daily_log_2025-08-17.md`)
- **Agregatni period:** kada se spaja više dana u jedan dokument, koristi:  
  `daily_log_YYYY-MM-DD_to_YYYY-MM-DD.md`  
  (npr. `daily_log_2025-08-04_to_2025-08-12.md`)

**Obavezne sekcije u svakom dnevniku:**

1. `## Rezime dana` — 2–4 rečenice: šta je bio fokus i zašto.
2. `## Šta je urađeno` — tačno šta je isporučeno (testovi, kod, dokumentacija).
3. `## Naučeno / uvidi` — kratke lekcije/aha-momenti.
4. `## Problemi / blokade` — što pre zabeležiti (ili “nema”).
5. `## Komande / fajlovi dana` — par bitnih komandi (pytest, git ACP, alati).

> **Minimalni dnevni cilj:** ≥1 **zeleni test** + ≥1 **smislen commit**.

---

## 🧩 Template (kopiraj pri kreiranju novog dana)

````md
# daily_log_YYYY-MM-DD

**Project:** (npr. PADD, ZF-14, Foundations)

## Rezime dana

- …

## Šta je urađeno

- …

## Naučeno / uvidi

- …

## Problemi / blokade

- …

## Komande / fajlovi dana

```bash
# primeri
pytest -q
git add -A
git commit -m "docs(log): add daily_log_YYYY-MM-DD (kratak opis)"
git push

```
````

---

## 🧾 Avgust 2025 — indeks

- 2025-08-04 → 2025-08-12: agregatni log → `./daily_log_2025-08-04_to_2025-08-12.md`
- 2025-08-13: PADD → `./daily_log_2025-08-13.md`
- 2025-08-14: PADD → `./daily_log_2025-08-14.md`
- 2025-08-15: ZF-14 (kickoff) → `./daily_log_2025-08-15.md`
- 2025-08-16: ZF-14 → `./daily_log_2025-08-16.md`
- 2025-08-17: ZF-14 → `./daily_log_2025-08-17.md`

> Napomena: Indeks je ručno održavan (namera: čist Git dif i lak pregled).
> Drži **jedan fajl po datumu** (izbegni duplikate za isti dan).

---

## ♻️ Održavanje kvaliteta

- **Doslednost sekcija:** koristi isti redosled naslova svaki dan.
- **Relativne putanje:** ne stavljaj apsolutne GitHub URL-ove.
- **Kratko, operativno:** dnevnik je trag isporuke, ne roman.
- **Backfill:** ako popunjavaš raniji dan, dodaj napomenu “(unos naknadno dopunjen)”.

---

## 🔁 Brzi workflow (preporuka)

1. U **Standup** dokumentu zapiši 3 fokusa dana.
2. Radi po planu; čim završiš komad posla → **upiši u dnevnik** i uradi **ACP**.
3. Na kraju dana uradi **Wrap-up** (3–5 rečenica) i čekiraj da je dnevnik potpun.

---

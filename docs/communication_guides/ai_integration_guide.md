# 🤖 AI Integration & Productivity Guide (Copilot + ChatGPT + VS Code)

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 📌 Purpose | Svrha

- 🇬🇧 This guide summarizes how to effectively integrate and use AI tools (GitHub Copilot, Copilot Chat, ChatGPT, GitHub + CLI) in a Python automation project.
- 🇷🇸 Ovaj vodič objedinjuje upotrebu alata (Copilot, Copilot Chat, ChatGPT, GitHub, CLI) u Python projektima za automatizaciju.

---

## 🧠 Copilot Configuration Overview | Pregled Copilot podešavanja

### 📄 `.github/copilot.yaml`

| Podešavanje           | Vrednost                        | Opis                                     |
| --------------------- | ------------------------------- | ---------------------------------------- |
| `default_language`    | `python`                        | Podrazumevani jezik predloga             |
| `documentation_style` | `bilingual`                     | Svi README fajlovi su dvojezični (EN/SR) |
| `code_tone`           | `professional`                  | Stil generisanog koda i komentara        |
| `focus`               | `automation, CLI, modular code` | Fokus kod predloga                       |

---

### 📁 `about_copilot_instructions.md`

- Definiše konvencije korišćenja Copilot-a u ovom repozitorijumu
- Nema eksternih API-ja, sve se radi u okviru Python standardne biblioteke
- Automatizovani skriptovi su modularni, jednostavni i komentarisani

---

## 🤖 Kada koristiti koji AI alat?

| Alat                           | Kada koristiti                                         | Za šta je najbolji                          |
| ------------------------------ | ------------------------------------------------------ | ------------------------------------------- |
| **GitHub Copilot**             | Tokom kucanja koda                                     | Inline predlozi: `for`, `if`, funkcije      |
| **Copilot Chat (u VS Code-u)** | Kada debaguješ ili tražiš pomoć za kod                 | Objašnjenje koda, `bash`, `regex`, greške   |
| **ChatGPT (web)**              | Za dublje razumevanje koncepata i analizu više fajlova | Arhitektura, struktura projekta, roadmap    |
| **Copilot CLI (beta)**         | U komandnoj liniji (ako je podržan)                    | Bash automatizacija, brisanje fajlova, grep |
| **GitHub + ChatGPT**           | Kada želiš da ChatGPT direktno čita repozitorijum      | Analiza README, foldera, koda               |

---

## 🧩 Tastaturne prečice (VS Code)

### 📂 Osnovne prečice

| Akcija                 | Windows/Linux      | Mac                  |
| ---------------------- | ------------------ | -------------------- |
| Otvori terminal        | `Ctrl + ~`         | `Cmd + ~`            |
| Komentariši liniju     | `Ctrl + /`         | `Cmd + /`            |
| Formatiraj kod         | `Shift + Alt + F`  | `Shift + Option + F` |
| Otvori pretragu        | `Ctrl + F`         | `Cmd + F`            |
| Otvori komandnu paletu | `Ctrl + Shift + P` | `Cmd + Shift + P`    |
| Idi na fajl            | `Ctrl + P`         | `Cmd + P`            |
| Idi na definiciju      | `F12`              | `F12`                |
| IntelliSense predlog   | `Ctrl + Space`     | `Ctrl + Space`       |

### 🔄 Navigacija između panela

| Akcija             | Prečica           |
| ------------------ | ----------------- |
| Fokus na editor    | `Ctrl + 1`        |
| Fokus na terminal  | `Ctrl + ~`        |
| Sledeći terminal   | `Ctrl + PageDown` |
| Prethodni terminal | `Ctrl + PageUp`   |

---

## 🔧 Copilot Chat Setup (Shortcut)

> Kako otvoriti Copilot Chat brzo:

1. `Ctrl + K` → zatim `Ctrl + S` (otvori Keyboard Shortcuts)
2. Traži: `View: Toggle Chat`
3. Uveri se da komanda ima ID:

```
workbench.panel.chat.view\.copilot.active
```

4. Dodeli prečicu, npr. `Ctrl + Alt + C`
5. Pritisni **Enter** i testiraj

---

## 🧠 Bash komande (minimalni podsetnik)

| Komanda          | Objašnjenje                   |
| ---------------- | ----------------------------- |
| `cd folder`      | Uđi u folder                  |
| `cd ..`          | Nazad jedan nivo              |
| `ls`             | Prikaži sadržaj foldera       |
| `mkdir naziv`    | Napravi novi folder           |
| `touch fajl.py`  | Kreiraj fajl                  |
| `code .`         | Otvori VS Code u ovom folderu |
| `python fajl.py` | Pokreni Python skriptu        |
| `clear`          | Očisti terminal               |

---

## 📘 Preporučeni stil i praksa

- ✅ Koristiti `type hints` u svim funkcijama (`param: str -> int`, itd.)
- ✅ Pisati sve README fajlove dvojezično (🇬🇧 / 🇷🇸)
- ✅ Koristiti Copilot kao asistenta, ne kao zamenu za razumevanje
- ✅ Svaki projekat ima:
  - `README.md`
  - `docs/` folder (cheatsheet + opis modula)
  - `logger.py`, `main.py`, `tests/`

---

## 🔚 Zaključak

> 🇷🇸: Ova stranica je centralizovana pomoć za sve buduće projekte koji koriste veštačku inteligenciju u razvoju i automatizaciji.
>
> 🇬🇧: This page serves as the central reference for all future AI-assisted automation and scripting projects.

📌 _Autor: Josip Pavlović — Prelazak iz građevine u profesionalni razvoj softvera._

📆 _Ažurirano: 2025-07-21_

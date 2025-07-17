## 🤖 AI Workflow Cheatsheet + Tastaturne Prečice (EN/SR)

> **Copilot + ChatGPT + GitHub** – kako koristiti AI profesionalno u VS Code-u i terminalu  
> **Kako da znaš koji alat kada da koristiš + najvažnije prečice i komande koje svaki programer treba da zna.**

---

## 🔹 1. ChatGPT (web interfejs)

**Use when:**
- You want to learn deeply about a concept (e.g. `datetime`, `OOP`, `logging`, `Git`)
- You need help with structure, roadmap, README.md, architecture
- You want analysis across multiple files/projects

**Koristi kada:**
- Želiš dubinsko objašnjenje koncepta
- Potrebna ti je pomoć oko strukture projekta, README, plana rada
- Analiziraš više fajlova odjednom (repozitorijum)

---

## 🔹 2. GitHub Copilot (inline predlozi u VS Code-u)

**Use when:**
- You want quick autocomplete suggestions as you type
- You're writing a simple function, loop, condition

**Koristi kada:**
- Pišeš funkciju i želiš da ti predloži nastavak linije
- Automatizuješ osnovni kod (for, if-else, dict...)

**Keyboard shortcut / Prečica:**  
`Tab` → prihvati predlog

---

## 🔹 3. Copilot Chat (u okviru VS Code-a)

**Use when:**
- You want code explanation or refactoring
- You need help debugging errors
- You want help with shell/bash commands

**Koristi kada:**
- Treba ti objašnjenje koda ili refaktorisanje
- Imaš grešku i tražiš lokalnu pomoć
- Pišeš `bash`, `regex`, `json`, `yaml` i želiš pomoć

**Keyboard shortcuts / Tastaturne prečice:**
- `Ctrl + I` → Otvori Copilot Chat
- `Ctrl + Enter` → Pošalji pitanje
- `Alt + \`` → Prebaci na Copilot tab

---

## 🔹 4. GitHub integracija sa ChatGPT

**Use when:**
- You want ChatGPT to read or analyze a public/private repo
- You’re writing/validating a professional README

**Koristi kada:**
- Želiš da ChatGPT direktno čita kod iz tvog repozitorijuma
- Pišeš profesionalnu dokumentaciju (README.md)

**Koraci:**
1. Otvori `Settings → Konektori → GitHub`
2. Poveži autorizaciju
3. Koristi `Explore files` iz ChatGPT-a

---

## 🔹 5. Copilot CLI (beta – ako podržan)

**Use when:**
- You want AI to suggest Bash/Zsh commands

**Koristi kada:**
- Automatizuješ komandnu liniju (npr. brisanje fajlova, grep, rename)

**Primer:**
```bash
copilot suggest "find all .log files older than 30 days"
```


## ⌨️ OSNOVNE TASTATURNE PREČICE KOJE MORAJU DA SE ZNAJU

| Akcija / Action                             | Prečica Windows/Linux | Prečica Mac          |
| ------------------------------------------- | --------------------- | -------------------- |
| Otvori VS Code terminal                     | `Ctrl + ~`            | `Cmd + ~`            |
| Komentar linije koda                        | `Ctrl + /`            | `Cmd + /`            |
| Formatiranje fajla                          | `Shift + Alt + F`     | `Shift + Option + F` |
| Pretraga unutar fajla                       | `Ctrl + F`            | `Cmd + F`            |
| Globalna pretraga u projektu                | `Ctrl + Shift + F`    | `Cmd + Shift + F`    |
| Brza navigacija po fajlovima                | `Ctrl + P`            | `Cmd + P`            |
| Prelazak na definiciju (`Go to definition`) | `F12`                 | `F12`                |
| IntelliSense predlozi                       | `Ctrl + Space`        | `Ctrl + Space`       |
| Otvori komandnu paletu                      | `Ctrl + Shift + P`    | `Cmd + Shift + P`    |

---

## 🔧 OSNOVNE BASH KOMANDE ZA RAD

| Komanda                 | Objašnjenje                        |
| ----------------------- | ---------------------------------- |
| `cd naziv_foldera`      | Uđi u folder                       |
| `cd ..`                 | Vrati se jedan nivo                |
| `ls`                    | Prikaži sadržaj foldera            |
| `mkdir naziv_foldera`   | Napravi folder                     |
| `touch fajl.py`         | Napravi novi fajl                  |
| `code .`                | Otvori trenutni folder u VS Code-u |
| `rm fajl.txt`           | Obriši fajl                        |
| `clear`                 | Očisti terminal                    |
| `python ime_skripte.py` | Pokreni Python skriptu             |

---
## 🧭 VS Code Navigation Cheatsheet (EN/SR)

> **Navigacija, fokus, tabovi, fajlovi, editor i terminal**  
> Kratak vodič za efikasno kretanje unutar Visual Studio Code-a

---

## 🔹 1. Navigacija između panela / Navigating Panels

| Akcija / Action                         | Prečica (Win/Linux) | Prečica (Mac)      |
|----------------------------------------|----------------------|---------------------|
| Otvori Explorer panel (File Browser)   | `Ctrl + Shift + E`   | `Cmd + Shift + E`   |
| Otvori Source Control (Git)            | `Ctrl + Shift + G`   | `Cmd + Shift + G`   |
| Otvori Extensions                      | `Ctrl + Shift + X`   | `Cmd + Shift + X`   |
| Otvori Terminal                        | `Ctrl + ~`           | `Cmd + ~`           |
| Otvori Command Palette                 | `Ctrl + Shift + P`   | `Cmd + Shift + P`   |

---

## 🔹 2. Prebacivanje fokusa / Switching Focus

| Akcija / Action                                 | Prečica                    |
|--------------------------------------------------|-----------------------------|
| Fokus iz Editora u Explorer                     | `Ctrl + 0`, zatim `Ctrl + Shift + E` |
| Fokus iz Explorera u Editor                     | `Enter` na označenom fajlu |
| Kretanje kroz Sidebar sekcije                   | `F1` → `View: Focus on...` |
| Promena tabova otvorenih fajlova                | `Ctrl + Tab` / `Ctrl + Shift + Tab` |
| Navigacija po već otvorenim panelima            | `Ctrl + 1`, `Ctrl + 2`, `Ctrl + 3` (levi, centralni, desni panel) |

---

## 🔹 3. Navigacija po fajlovima / Navigating Files

| Akcija / Action                     | Prečica (Win/Linux) | Prečica (Mac)    |
|------------------------------------|----------------------|-------------------|
| Otvori bilo koji fajl (po imenu)   | `Ctrl + P`           | `Cmd + P`         |
| Idi na liniju                      | `Ctrl + G`           | `Cmd + G`         |
| Pretraga unutar fajla              | `Ctrl + F`           | `Cmd + F`         |
| Globalna pretraga u projektu       | `Ctrl + Shift + F`   | `Cmd + Shift + F` |
| Idi na definiciju simbola          | `F12`                | `F12`             |
| Prikaži sve definicije simbola     | `Ctrl + Shift + O`   | `Cmd + Shift + O` |

---

## 🔹 4. Navigacija kroz kod / Code Navigation

| Akcija / Action                              | Prečica            |
|---------------------------------------------|---------------------|
| IntelliSense predlozi                       | `Ctrl + Space`      |
| Jump to matching bracket (skok na zagradu)  | `Ctrl + Shift + \\` |
| Otvori/minimiziraj outline prikaz           | `Ctrl + Shift + O`  |
| Refaktorisanje (rename simbola)             | `F2`                |
| Komentar linije                             | `Ctrl + /`          |

---

## 🔹 5. Terminal i Editor navigacija

| Akcija / Action                       | Prečica              |
|--------------------------------------|-----------------------|
| Otvori ili sakrij terminal           | `Ctrl + ~`            |
| Novi terminal                        | `Ctrl + Shift + ö` ili `+` u terminalu |
| Fokus terminal → editor              | `Ctrl + 1`            |
| Fokus editor → terminal              | `Ctrl + ` (tilde)     |
| Fokus na sledeći terminal            | `Ctrl + PageDown`     |
| Fokus na prethodni terminal          | `Ctrl + PageUp`       |

---


## 🔧 Copilot Chat Shortcut Setup – Cheatsheet

## 🇬🇧 ENGLISH

### ✅ Step-by-step Instructions

1. Press `Ctrl + K` then `Ctrl + S` to open **Keyboard Shortcuts**.
2. Search for:  
```

View: Toggle Chat

```
3. Confirm that the command has this ID:  
```

workbench.panel.chat.view\.copilot.active

```
4. Right-click the entry → `Change Keybinding`.
5. Set your desired shortcut, for example:  
```

Ctrl + Alt + C

```
6. Press **Enter** to confirm.
7. Test it! Your chat panel should toggle open/closed.

---

### 🧪 Tip for Testing

To confirm it works:
- Close all panels.
- Press your shortcut.
- You should see the Copilot Chat panel appear at the bottom.

---

### 💡 Additional Notes

- You can change the model (e.g., GPT-4.1 or GPT-4o) in the dropdown.
- Use `Ctrl + Shift + P` and search:  
```

> Copilot: Open Copilot Chat

```

---

## 🇷🇸 SRPSKI (latinica)

Ovaj cheatsheet objašnjava kako da podesiš tastaturnu prečicu za **otvaranje Copilot Chat panela** u VS Code-u.

---

### ✅ Koraci za podešavanje

1. Pritisni `Ctrl + K` pa zatim `Ctrl + S` da otvoriš **Keyboard Shortcuts**.
2. U pretrazi ukucaj:  
```

View: Toggle Chat

```
3. Uveri se da komanda ima sledeći ID:  
```

workbench.panel.chat.view\.copilot.active

```
4. Desni klik → `Change Keybinding`.
5. Postavi željenu prečicu, npr:  
```

Ctrl + Alt + C

```
6. Pritisni **Enter** da potvrdiš.
7. Testiraj! Panel bi trebalo da se pojavi/deselektuje.

---

### 🧪 Savet za testiranje

Da proveriš da li radi:
- Zatvori sve donje panele.
- Pritisni svoju prečicu.
- Ako se pojavi Copilot Chat – sve je ispravno podešeno.

---

### 💡 Dodatne napomene

- Možeš da biraš model (npr. GPT-4.1 ili GPT-4o) u padajućem meniju.
- Koristi `Ctrl + Shift + P` i ukucaj:  
```

> Copilot: Open Copilot Chat
```
---

📍 *Autor: Jole – Vizuelna efikasnost u VS Code-u*  
📆 *Ažurirano: 2025-07-17*



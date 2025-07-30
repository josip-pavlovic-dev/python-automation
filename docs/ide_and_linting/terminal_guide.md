# 🖥️ Terminal Setup & Navigation | _Podešavanje i navigacija u terminalu_

## ✅ Terminal profiles in VS Code | _Profili terminala u VS Code-u_

### 1️⃣ Add profiles in `settings.json` | _Dodaj profile u `settings.json`_

```json
"terminal.integrated.profiles": {
    "PowerShell": {
        "path": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    },
    "Command Prompt": {
        "path": "C:\\Windows\\System32\\cmd.exe"
    },
    "Git Bash": {
        "path": "C:\\Program Files\\Git\\bin\\bash.exe"
    }
},
"terminal.integrated.defaultProfile.windows": "PowerShell"
```

- Sets up **PowerShell**, **Command Prompt (cmd)** and **Git Bash** profiles.
  \| _Podesi profile za **PowerShell**, **Command Prompt (cmd)** i **Git Bash**._

### 2️⃣ Switching terminals | _Menjanje terminala_

- **Ctrl + Shift + P** → `Terminal: Select Default Profile`
  \| _Menja default terminal._
- **Ctrl + \`** (backtick) → otvori/zatvori terminal.
- Klik na strelicu pored `+` u terminalu za biranje drugog profila.
  \| _Klikni strelicu pored `+` za izbor drugog profila._

---

## 🔀 Navigation shortcuts | _Prečice za navigaciju_

- `Ctrl + ↑ / ↓` → pomeri gore/dole u terminalu
- `Shift + PgUp / PgDn` → skrol po stranici
- `Ctrl + Shift + [` i `Ctrl + Shift + ]` → promena terminal tabova
- `Ctrl + Shift + C` → kopiraj tekst iz terminala
- `Ctrl + Shift + V` → nalepi tekst u terminal

---

## 🎨 Customize appearance | _Prilagodi izgled_

### 1️⃣ Font & boje | _Font i boje_

```json
"terminal.integrated.fontFamily": "Fira Code, Cascadia Code, monospace",
"terminal.integrated.fontSize": 14,
"terminal.integrated.cursorBlinking": true
```

- Install **Fira Code** ([https://github.com/tonsky/FiraCode](https://github.com/tonsky/FiraCode)) for ligatures.
  \| _Instaliraj **Fira Code** za lepši prikaz znakova._

### 2️⃣ Prompt styling (PowerShell) | _Stilizovanje prompta (PowerShell)_

1. Instaliraj **oh-my-posh**:

   ```powershell
   winget install JanDeDobbeleer.OhMyPosh -s winget
   ```

2. Otvori profil:

   ```powershell
   notepad $PROFILE
   ```

3. Dodaj:

   ```powershell
   oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\paradox.omp.json" | Invoke-Expression
   ```

➡ Kada ponovo otvoriš PowerShell, prompt će biti šaren i pokazivaće **Git grane i trenutni folder**.

---

## 🧹 Useful commands | _Korisne komande_

- **Clear screen**:

  - Bash: `clear`
  - PowerShell/CMD: `cls`

- **Change directory**:

  - `cd folder_name`

- **List files**:

  - Bash: `ls`
  - CMD/PowerShell: `dir`

---

## 👨‍💻 Author | _Autor_

[![GitHub](https://img.shields.io/badge/GitHub-Josip%20Pavlović-blue?logo=github)](https://github.com/Jole85)

**Josip Pavlović — aspiring Python developer from Novi Sad**

---

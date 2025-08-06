# ⚙️ VS Code Configuration | _Podešavanja VS Code okruženja_

Ova datoteka sadrži sve relevantne `.json` fajlove, preporučene ekstenzije i objašnjenja za optimalno podešeno Python razvojno okruženje u Visual Studio Code-u.

---

## ✅ settings.json – Finalna verzija

```jsonc
{
  // FONT & TEMA
  "editor.fontFamily": "Fira Code, Consolas, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "workbench.colorTheme": "Default Dark Modern",

  // FORMATIRANJE KODA
  "editor.formatOnSave": true,
  "editor.formatOnType": true,
  "python.formatting.provider": "black",

  // LINTERI
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,

  // PYLANCE (INTELLISENSE)
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.analysis.autoSearchPaths": true,
  "python.analysis.useLibraryCodeForTypes": true,

  // VIRTUALNO OKRUŽENJE
  "python.venvPath": "${workspaceFolder}/.venv",
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",

  // TERMINAL
  "terminal.integrated.defaultProfile.windows": "PowerShell 7",
  "terminal.integrated.profiles.windows": {
    "PowerShell 7": {
      "path": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
      "icon": "terminal-powershell"
    }
  },

  // NOTEBOOK
  "jupyter.askForKernelRestart": false,
  "jupyter.sendSelectionToInteractiveWindow": true
}
```

---

### 📘 Objašnjenja po sekcijama

#### 🎨 Font & Tema

- `"editor.fontFamily"` → Redosled fontova; koristi se _Fira Code_ zbog podrške za ligature.
- `"editor.fontLigatures"` → Spaja operatore kao `!=`, `=>`, `==` u estetski prijatne simbole.

#### 🧹 Formatiranje

- `"editor.formatOnSave"` → Automatski poziva `black` svaki put kad sačuvaš fajl.
- `"editor.formatOnType"` → Formatira dok kucaš (opciono korisno).

#### 🔍 Pylance & IntelliSense

- `"python.analysis.*"` → Kontrola inteligentnog koda, predlozi, uvoz, tipovi i sl.

#### 🐍 Virtualno okruženje

- `"python.venvPath"` → Mesto gde VS Code traži `venv` folder.
- `"python.defaultInterpreterPath"` → Putanja do `python.exe` unutar projekta.

#### 🖥 Terminal

- `"terminal.integrated.*"` → Definiše da je PowerShell 7 tvoj podrazumevani terminal.

#### 📓 Notebook

- `"jupyter.askForKernelRestart"` → Ne pita svaki put da restartuje kernel.
- `"jupyter.sendSelectionToInteractiveWindow"` → Omogućava Jupyter-style rad unutar VS Code-a.

---

## ▶️ launch.json – Debug podešavanje

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "▶️ Launch: Python file",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

- Pokreće trenutno otvoreni `.py` fajl pomoću `F5` ili iz `"Run"` menija.
- `integratedTerminal` koristi VS Code terminal, a ne zaseban prozor.

---

## 🔄 tasks.json – Automatizovane radnje

Primer taskova:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "▶️ Run: current file",
      "type": "shell",
      "command": "python",
      "args": ["${file}"],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "focus": true
      },
      "problemMatcher": []
    }
  ]
}
```

- Možeš ih proširiti da pokreću npr. `day03_file_management/scanner.py` ili `sync_snippets.py`.

---

## ⌨️ keybindings.json – Prečice

Primer:

```json
[
  {
    "key": "alt+r",
    "command": "workbench.action.tasks.runTask",
    "args": "▶️ Run: current file"
  }
]
```

- `Alt + R` pokreće trenutno aktivan Python fajl pomoću taska.
- Možeš dodati više prečica za različite radnje.

---

## 📦 extensions.json – Preporučene ekstenzije

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "ms-vscode.powershell",
    "ms-azuretools.vscode-docker",
    "esbenp.prettier-vscode",
    "ms-vscode.cpptools",
    "donjayamanne.python-environment-manager",
    "ms-vscode.live-server",
    "batisteo.vscode-django",
    "njpwerner.autodocstring",
    "ms-python.black-formatter",
    "charliermarsh.ruff",
    "deepl-translator.deepl"
  ]
}
```

📌 Kada VS Code otvori projekat, automatski predlaže instalaciju svih ekstenzija iz ovog fajla.

---

## 📁 Lokacija svih fajlova

| Fajl             | Lokacija u projektu                  |
| ---------------- | ------------------------------------ |
| settings.json    | `.vscode/settings.json`              |
| launch.json      | `.vscode/launch.json`                |
| tasks.json       | `.vscode/tasks.json`                 |
| keybindings.json | _(user level)_ `AppData/Roaming/...` |
| extensions.json  | `.vscode/extensions.json`            |

---

## 🧠 Napomena

Ova konfiguracija je deo većeg razvojnog sistema i u potpunosti je kompatibilna sa sledećim alatima:

- `venv` + `direnv` + `.envrc`
- GitHub + Git + GitLens
- Python Black + Flake8 + Ruff
- PowerShell 7
- Jupyter Notebooks

---

## 📌 Author | _Autor_

![GitHub](https://img.shields.io/badge/GitHub-josip--pavlovic--dev-blue?logo=github)
![Learning Path](https://img.shields.io/badge/Learning_Path-Python_Automation_and_Data_Engineering-critical)

Josip Pavlović – aspiring Python developer from Novi Sad

[LinkedIn profil](https://www.linkedin.com/in/josip-p-151951338/)

---

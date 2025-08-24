# 🛠️ final_settings.md

_Referentni fajl za VS Code podešavanja — profil: `python-automation`_
_(Korisno za reinstalaciju, migraciju, kloniranje projekata, i proveru podešavanja)_

---

## ✅ 1. Globalni `settings.json`

_Lokacija: `C:\Users\JoleDev\AppData\Roaming\Code\User\settings.json`_
**Opis:** Postavke koje se primenjuju u okviru _profila_ `python-automation`.

```json
{
  "workbench.colorTheme": "Default Dark Modern",
  "workbench.iconTheme": "material-icon-theme",
  "editor.fontSize": 15,
  "editor.lineHeight": 22,
  "editor.tabSize": 4,
  "editor.renderWhitespace": "boundary",
  "editor.rulers": [80, 100],
  "editor.wordWrap": "on",
  "editor.stickyScroll.enabled": false,
  "editor.minimap.enabled": false,

  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,

  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.autoSave": "onWindowChange",

  "terminal.integrated.fontSize": 14,
  "terminal.integrated.cursorStyle": "underline",
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.cwd": "${workspaceFolder}",
  "terminal.integrated.defaultProfile.windows": "Git Bash",

  "explorer.confirmDelete": false,
  "breadcrumbs.enabled": true,

  "python.defaultInterpreterPath": "c:\\Program Files\\Python313\\python.exe",
  "python.analysis.typeCheckingMode": "basic",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.ruffArgs": ["--select=E,F,W,I,N"],
  "ruff.enable": true,

  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll.ruff": "explicit"
  },

  "markdown.preview.breaks": true,
  "markdown.preview.fontSize": 14,

  "github.copilot.enable": {
    "": false,
    "python": false,
    "markdown": false
  },

  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  }
}
```

---

## ✅ 2. Lokalni `settings.json`

_Lokacija: `python-automation/.vscode/settings.json`_
**Opis:** Projektna podešavanja — definišu testiranje, formatiranje, lintovanje i putanje.

```json
{
  "python.testing.pytestArgs": ["labs/zero_foundations/tests"],
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true,

  "python.analysis.extraPaths": [
    "${workspaceFolder}/labs/zero_foundations/src"
  ],
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.envFile": "${workspaceFolder}/.env",

  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },

  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll.ruff": "explicit"
  },

  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,

  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.linting.pylintEnabled": false,

  "ruff.lint.config": {
    "select": ["E", "F", "W", "I", "C90", "N"],
    "ignore": ["E501"]
  },

  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  },

  "explorer.confirmDelete": false,
  "explorer.confirmDragAndDrop": false,
  "explorer.compactFolders": false,

  "workbench.sideBar.location": "left",
  "workbench.statusBar.visible": true,

  "editor.hover.enabled": true,
  "editor.scrollbar.vertical": "auto",
  "editor.scrollbar.horizontal": "auto",
  "editor.renderWhitespace": "boundary",
  "editor.guides.indentation": true,

  "files.autoSave": "onWindowChange",
  "files.hotExit": "onExitAndWindowClose",

  "security.workspace.trust.untrustedFiles": "open",

  "terminal.integrated.env.windows": {
    "PYTHONPATH": "${workspaceFolder}/labs/zero_foundations/src"
  },

  "workbench.colorTheme": "Default Dark Modern",
  "workbench.editor.highlightModifiedTabs": true,
  "workbench.editor.enablePreview": false
}
```

---

## 📦 Extensions (najvažnije)

- `ms-python.python`
- `charliermarsh.ruff`
- `esbenp.prettier-vscode`
- `bierner.markdown-preview-github-styles`
- `eamodio.gitlens`
- `PKief.material-icon-theme`

---

## ⌨️ Preporučene prečice

- **Format on save**: `Ctrl + S`
- **Run Python file**: `Ctrl + Alt + N` (ako koristiš Code Runner)
- **Open Terminal**: `Ctrl + ` \`
- **Organize imports**: automatski na save (`explicit`)
- **Prebacivanje profila**: `F1` → “Profiles: Switch Profile”

---

## 🧠 Napomena

Ova konfiguracija je **optimizovana za tvoj stil učenja**, kao i za posao koji planiraš da radiš (automatizacija + Markdown dokumentacija).

---

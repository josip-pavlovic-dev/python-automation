# Skaliranje ekrana vs VS Code podešavanja

### Šta bih ja uradio (stabilno za PowerToys):

- **Drži oba ekrana na istom Windows skalingu** (125% je često najbolji kompromis za čitljivost).
- **Ne diraj OS skaling svaki čas**; umesto toga podesi **VS Code User Settings** da ti sve stane i bude čitko.

Ubaci u **User** `settings.json` (ne Workspace), ili prilagodi vrednosti po ukusu:

```json
{
  // Globalni zum samo za VS Code (ne menja Windows scaling)
  "window.zoomLevel": 0, // probaj -0.5, 0 ili +0.5

  // Editor
  "editor.fontSize": 14, // npr. 13–16
  "editor.lineHeight": 1.4,
  "editor.wordWrap": "on", // dugačke linije se lome
  "editor.minimap.enabled": false,

  // Terminal
  "terminal.integrated.fontSize": 13, // teraj da dve linije stanu
  "terminal.integrated.lineHeight": 1.2,
  "terminal.integrated.scrollback": 5000,

  // Panel i layout
  "workbench.panel.defaultLocation": "bottom", // više širine za terminal
  "workbench.editor.enablePreview": false
}
```

**Kada birati 125% vs 100%?**

- Ako sediš malo dalje ili želiš manje zamaranje očiju → **125%** na oba ekrana + smanji `window.zoomLevel` za 0.5 koraka u VS Code-u.
- Ako voliš ultra-kompaktan prikaz i sediš blizu → **100%** na oba, a u VS Code podigni fontove za editor/terminal.

---

---

(Mentor🙂) Super — dopunio sam tvoj **User `settings.json`** i pripremio komplet **`bool()` paket** (cheatsheet, analysis notes, REPL, tutor template).

---

### ✅ User `settings.json` (konačna varijanta)

```json
{
  "editor.fontSize": 16,
  "editor.lineHeight": 24,
  "editor.fontFamily": "Fira Code, Consolas, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.cursorSmoothCaretAnimation": "explicit",
  "editor.cursorBlinking": "phase",
  "editor.cursorStyle": "line",
  "editor.smoothScrolling": true,
  "editor.inlineSuggest.enabled": true,
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": "active",
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll": "explicit",
    "source.fixAll.ruff": "explicit"
  },
  "editor.minimap.enabled": false,
  "editor.wordWrap": "on",

  "explorer.confirmDragAndDrop": false,
  "explorer.confirmDelete": false,

  "files.autoSave": "off",
  "files.autoSaveWhenIdle": true,
  "files.autoGuessEncoding": true,
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.associations": {
    "*.code-snippets": "jsonc"
  },

  "terminal.integrated.defaultProfile.windows": "Git Bash",
  "terminal.integrated.fontSize": 15,
  "terminal.integrated.cursorStyle": "underline",
  "terminal.integrated.cursorBlinking": true,
  "terminal.integrated.scrollback": 10000,

  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
  "python.analysis.typeCheckingMode": "basic",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.linting.mypyEnabled": false,
  "python.analysis.diagnosticMode": "workspace",
  "python.analysis.autoSearchPaths": true,
  "python.analysis.useLibraryCodeForTypes": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,

  "workbench.colorTheme": "Default Dark Modern",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.startupEditor": "newUntitledFile",
  "workbench.editor.enablePreview": false,
  "workbench.statusBar.visible": true,

  "breadcrumbs.enabled": false,

  "workbench.editor.showTabs": true,
  "workbench.editor.tabCloseButton": "right",
  "workbench.editor.labelFormat": "short",
  "workbench.editor.tabSizing": "shrink",
  "workbench.editor.pinnedTabSizing": "compact",
  "workbench.editor.wrapTabs": true,
  "workbench.editor.pinnedTabsOnSeparateRow": true,

  "workbench.colorCustomizations": {
    "statusBar.background": "#2f3542",
    "statusBar.noFolderBackground": "#2f3542",
    "statusBar.debuggingBackground": "#ffa502",
    "titleBar.activeBackground": "#1f2937",
    "titleBar.activeForeground": "#e5e7eb"
  },

  "security.workspace.trust.untrustedFiles": "open",
  "window.menuBarVisibility": "compact"
}
```

---

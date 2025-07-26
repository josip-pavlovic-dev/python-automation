# 🛠️ scripts – Automation and Configuration Tools / Alati za automatizaciju i konfiguraciju

![Status](https://img.shields.io/badge/status-maintained-brightgreen)![Scope](https://img.shields.io/badge/scope-internal--tools-blue)![Language](https://img.shields.io/badge/python-3.12%2B-blue)

## 📁 Structure / Struktura

```

scripts/
│
├── sync\_snippets/
│   ├── sync\_snippets.md         ← Dokumentacija za rad skripti
│   ├── sync\_snippets.py         ← Python skripta za sinhronizaciju snippeta
│   ├── sync\_snippets.bat        ← Windows batch fajl
│   └── sync\_snippets.ps1        ← PowerShell verzija

```

---

## 🔍 Description / Opis

This folder contains internal automation tools that enhance productivity and help maintain consistent workflows across the `python-automation` repository.  
Ova fascikla sadrži interne alate za automatizaciju koji poboljšavaju produktivnost i olakšavaju održavanje doslednog toka rada u okviru `python-automation` repozitorijuma.

### 🔄 `sync_snippets/` – Snippet Synchronization / Sinhronizacija snippeta

- Synchronizes `.code-snippets` files from `docs/vs-snippets/` to project-specific `.vscode/` folders.
- Maintains exceptions (e.g. `pylance_basics`, `commenting_basics`) for global `.vscode/`.
- Čisti stari sadržaj i prepisuje samo relevantne fajlove.

---

## 📄 Documentation / Dokumentacija

- [sync_snippets.md](./sync_snippets.md) – Usage instructions and logic overview  
  – Uputstvo za upotrebu i opis logike

---

## ✅ Usage Tips / Saveti za korišćenje

- Run the script via terminal or double-click `.bat`/`.ps1` if on Windows.
- Pokreni skriptu iz terminala ili dvostrukim klikom na `.bat`/`.ps1` fajl na Windows sistemu.

---

## 📌 Note / Napomena

These scripts are internal utilities and not intended for standalone deployment.  
Ove skripte su interne pomoćne alatke i nisu namenjene za samostalno pokretanje van projekta.

---

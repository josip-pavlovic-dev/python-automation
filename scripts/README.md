# 🛠 Scripts – Developer Utilities / Razvojne skripte

This folder contains developer utilities used to automate repetitive tasks across the `python-automation` project.  
_Ovaj folder sadrži razvojne skripte koje automatizuju ponavljajuće zadatke u okviru `python-automation` projekta._

---

## 📄 Included Scripts / Uključene skripte

| Script                | Description (EN)                                            | Opis (SR)                                                  |
|-----------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| `sync_snippets.py`    | Python script to copy `.code-snippets` into `.vscode` folders | Python skripta koja kopira `.code-snippets` fajlove u `.vscode` foldere |
| `sync_snippets.bat`   | Batch wrapper to run the Python sync script on Windows      | Batch fajl za pokretanje Python skripte na Windows-u       |
| `sync_snippets.ps1`   | PowerShell wrapper for the same purpose                     | PowerShell verzija za istu svrhu                           |

---

## 🧰 Usage Instructions / Uputstvo za korišćenje

### ▶️ Python
```bash
python scripts/sync_snippets.py
```

### ▶️ Batch
```cmd
scripts\sync_snippets.bat
```

### ▶️ PowerShell
```powershell
.\scripts\sync_snippets.ps1
```

---

## 🔄 Purpose / Svrha

These scripts automate the process of synchronizing `.code-snippets` files from the central `docs/vs-snippets/` folder into each project's `.vscode` folder.  
_Skripte automatski sinhronizuju `.code-snippets` fajlove iz centralnog foldera `docs/vs-snippets/` u `.vscode` foldere svakog projekta._

- Ensures consistent snippet availability  
  _Osigurava dostupnost istih snippeta u svim projektima_

- Simplifies updates across all environments  
  _Pojednostavljuje ažuriranja u svim okruženjima_

- Helps maintain cleaner documentation and workflow  
  _Pomaže u održavanju urednog toka rada i dokumentacije_

---

## 🧠 Notes / Napomene

- Update `sync_snippets.py` if new projects are added  
  _Ažuriraj `sync_snippets.py` ukoliko se dodaju novi projekti_

- Serbian snippets (`py-sr-comments.code-snippets`) are available only in `vs-snippets`, not synced automatically  
  _Srpski snippet-i (`py-sr-comments.code-snippets`) dostupni su samo u `vs-snippets` i ne sinhronizuju se automatski_


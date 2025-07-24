# 🛠 Scripts – Developer Utilities / Razvojne skripte

This folder contains developer utilities used to automate repetitive tasks across the `python-automation` project.  
_Ovaj folder sadrži razvojne skripte koje automatizuju ponavljajuće zadatke u okviru `python-automation` projekta._

---

## 📄 Included Scripts / Uključene skripte

| Script              | Description (EN)                                              | Opis (SR)                                                               |
| ------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `sync_snippets.py`  | Python script to copy `.code-snippets` into `.vscode` folders | Python skripta koja kopira `.code-snippets` fajlove u `.vscode` foldere |
| `sync_snippets.bat` | Batch wrapper to run the Python sync script on Windows        | Batch fajl za pokretanje Python skripte na Windows-u                    |
| `sync_snippets.ps1` | PowerShell wrapper for the same purpose                       | PowerShell verzija za istu svrhu                                        |
| `git_push.bat`      | Batch script for Git add/commit/push with custom message      | Batch skripta za `git add/commit/push` sa porukom                       |
| `git_push.sh`       | Bash script for Git push operations (Linux/Mac)               | Bash skripta za Git push (Linux/Mac okruženja)                          |

---

## ▶️ Usage Instructions / Uputstvo za korišćenje

### 🔁 Python (manual sync)

```bash
python scripts/sync_snippets.py
```

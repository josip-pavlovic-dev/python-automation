# 🧰 Cheatsheet — pokretanje skripti, modula i testova (Win + VS Code)

> Repo struktura (bitno za `-m`):
> `python-automation/`
> └─ `labs/core_functions/`
>     ├─ `dayB/` (sadrži npr. `try_code.py`, idealno i `__init__.py`)
>     └─ `tests/` (pytest fajlovi)

## 1) Provera gde si (CWD) i koji Python koristiš

```bash
# Git Bash
pwd
python -c "import sys,os;print('PY=',sys.executable);print('CWD=',os.getcwd())"
```

Ako `CWD` ≠ folder iz kog očekuješ da se sve pokreće → `cd` do njega.

---

## 2) Aktivacija venv-a (Windows)

### PowerShell

```powershell
# iz foldera gde je .venv/
.\.venv\Scripts\Activate.ps1
# ako Execution Policy koči:
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### Git Bash

```bash
source .venv/Scripts/activate
# (Alternativa, ako radiš iz root-a repoa)
source labs/core_functions/.venv/Scripts/activate
```

Brza provera:

```bash
python -V
python -c "import sys; print(sys.executable)"
```

---

## 3) Pokretanje **skripte** (putanja do .py fajla)

### Opcija A — iz repo root-a

```bash
python labs/core_functions/dayB/try_code.py
```

### Opcija B — uđeš u radni folder pa pokreneš

```bash
cd labs/core_functions
python dayB/try_code.py
```

> Ovo radi bez `__init__.py`. Najjednostavnije za vežbu.

---

## 4) Pokretanje kao **modul** (`-m`)

Za `-m` moraš biti **u folderu iznad paketa** i paket mora imati `__init__.py`.

```bash
# iz repo root-a, ako dayB ima __init__.py
python -m labs.core_functions.dayB.try_code

# ili iz labs/core_functions
cd labs/core_functions
python -m dayB.try_code
```

Tipične greške i lek:

- `ModuleNotFoundError: No module named 'dayB'` → nisi u folderu iznad `dayB` ili nema `__init__.py`.
- Rešenje: kreiraj prazan `labs/core_functions/dayB/__init__.py`.

---

## 5) Pytest — pokretanje testova

```bash
# iz labs/core_functions
pytest -q
pytest -q labs/core_functions/tests/test_list_grid.py
pytest -q labs/core_functions/tests/test_dict_hashability.py

# verbose + stop on first fail
pytest -v -x
```

Ako dobiješ upozorenje od Ruff-a “unused import pytest”:

- ili **ukloni** `import pytest` u testu gde ga ne koristiš,
- ili dodaj komentar: `import pytest  # noqa: F401`,
- ili u `.ruff.toml` (oprezno) dozvoli u test folderu:

  ```toml
  [tool.ruff.per-file-ignores]
  "labs/core_functions/tests/*" = ["F401"]
  ```

---

## 6) VS Code — brze postavke (User/Workspace)

### 6.1. Odabir interpretera (obavezno)

Command Palette → “Python: Select Interpreter” → izaberi **tačan** `.venv`:

- za `labs/core_functions`: `.../python-automation/labs/core_functions/.venv/Scripts/python.exe`

### 6.2. Workspace `settings.json` (predlog)

`.vscode/settings.json` u **repo root-u** ili u `labs/core_functions/.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/labs/core_functions/.venv/Scripts/python.exe",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["labs/core_functions/tests"],
  "python.terminal.activateEnvironment": true,
  "terminal.integrated.defaultProfile.windows": "Git Bash",
  "editor.formatOnSave": true
}
```

> Ako koristiš zasebne venv-ove po labs-ovima, stavi **poseban** `.vscode/settings.json` u svaki labs folder.

### 6.3. Debug (launch.json)

Ako ti VS Code traži _debugpy_, instaliraj **Python** ekstenziju. Minimalan `launch.json` za skriptu iz `dayB`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run dayB/try_code.py",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/labs/core_functions/dayB/try_code.py",
      "console": "integratedTerminal",
      "justMyCode": true
    }
  ]
}
```

### 6.4 Zašto Ruff briše `import pytest`?

- Ruff javlja **F401: imported but unused** → u tvom testu `test_grid_gotcha` **ne koristiš** `pytest` (nema `pytest.raises` itd.), pa predlaže da obrišeš `import pytest`.
- U testovima gde **koristiš** `pytest.raises(...)`, `import pytest` je potreban i Ruff neće prigovarati.
- Ako ipak želiš da zadržiš import (npr. zbog šablona), dodaj komentare:

  - u tom fajlu: `import pytest  # noqa: F401`
  - ili u **.ruff.toml** (preporuka samo ako želiš šire pravilo):

    ```toml
    [tool.ruff.per-file-ignores]
    "labs/core_functions/tests/*" = ["F401"]  # dozvoli neiskorišćen import u testovima
    ```

> Ukratko: test bez `pytest.raises` → ukloni `import pytest`. Test sa `raises` → ostavi import.

---

## 7) Tipični simptomi i instant dijagnostika

| Poruka/Simptom                                       | Uzrok                                                   | Rešenje                                                               |
| ---------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'dayB'`        | `-m` pokrenut iz pogrešnog CWD-a ili nema `__init__.py` | `cd` u folder iznad paketa; dodaj `__init__.py`                       |
| `Configured debug type 'debugpy' is not supported`   | Nema Python ekstenzije/debugpy                          | Instaliraj VS Code **Python** ekstenziju                              |
| Testovi ne vide import iz `labs/core_functions/dayB` | Pytest CWD/`sys.path`                                   | Pokreni pytest iz `labs/core_functions`; koristi putanju do fajla     |
| `import pytest` označen kao unused                   | Ruff F401                                               | ukloni import, ili `# noqa: F401`, ili per-file-ignore u `.ruff.toml` |
| Aktivacija venv ne radi u Git Bash                   | putanja/komanda                                         | `source .venv/Scripts/activate` (ne `activate.ps1`)                   |

---

## 8) Dnevni workflow (minimal friction)

1. Otvori **VS Code** u **repo root-u**.
2. ` Ctrl+`` → terminal →  `cd labs/core_functions`→`source .venv/Scripts/activate\`
3. Provera: `python -V` i `which python` (ili `python -c "import sys;print(sys.executable)"`).
4. Pokreni skriptu: `python dayB/try_code.py`
   (ili `python -m dayB.try_code` ako ima `__init__.py`)
5. Testovi: `pytest -q` ili `pytest -q labs/core_functions/tests/test_*.py`

---

## 9) “Zaboravio sam sve — brz reset”

```bash
# Gde sam i koji python koristim?
pwd
python -c "import sys,os;print(sys.executable);print(os.getcwd())"

# Aktivacija venv-a (Git Bash)
source .venv/Scripts/activate

# Pokretanje skripte
python labs/core_functions/dayB/try_code.py

# Pokretanje modula
python -m labs.core_functions.dayB.try_code

# Testovi
pytest -q labs/core_functions/tests
```

---

## 10) Opciona finese

- **Paketi po labs-ovima**: u svaki `dayX/` stavi prazan `__init__.py` → lakše `-m`.
- **Više venv-ova** u istom repo-u: drži **po jedan `.vscode/settings.json`** u svakom labs-u sa odgovarajućim interpreterom.
- **PYTHONPATH** ne diraj dok ne bude stvarno potrebno; radije koristi ispravne CWD i `-m`.

---

Ako želiš, pošalji mi **tvoj User i Workspace `settings.json`** (i `launch.json` ako postoji) — dopuniću ih da 1:1 prate ovaj cheat-path i tvoje venv-ove, da više ne “proklizavaš” na setup-u.

---

bravo — sve si poslao što nam treba. Evo **jednog lista-za-rad (cheatsheet)** + konkretnih **ispravki** da globalno i lokalno ne ulaze u konflikt.

---

# 🧰 VS Code + Python pokretanje: “jedan ekran za sve”

## 0) Trenutno stanje (kratak audit)

- **Globalni `settings.json`** ti fiksira interpreter na **system Python 3.13**
  (`python.defaultInterpreterPath: "c:\\Program Files\\Python313\\python.exe"`)&#x20;
  → Ako u projektu želiš `.venv`, ovo zna da preglasa lokalno.
- **Globalni `keybindings.json`** ima prečice vezane za **Zero Foundations** (CWD i PYTHONPATH) .
- **Lokalni `.vscode/launch.json`** i **`.vscode/tasks.json`** u tvom projektu takođe su **vezani za `labs/zero_foundations`** (CWD/PYTHONPATH) .
- **Lokalni `settings.json`** u projektu je mnogo bliži onome što hoćemo (pytest na `labs/core_functions/tests`, interpreter iz repo `.venv`), ali još uvek dodaje `extraPaths` i PYTHONPATH za `zero_foundations/src` (to nam ne treba za `core_functions`) .
- **Globalne preporučene ekstenzije** su OK (Python, Pylance, Jupyter, Ruff, Docker…) .
- Instalirane ekstenzije (Python, Pylance, Jupyter, Ruff, GitLens, Black…) — fino 👌 .

---

## 1) Cilj

1 repo, **više laboratorija**:

- `labs/zero_foundations/` → ima **svoj** `.venv` i **svoje** VS Code fajlove.
- `labs/core_functions/` → ima **svoj** `.venv` i **svoje** VS Code fajlove.

> Praksa: **ne** oslanjati se na globalni interpreter. Svaki labs ima **lokalni** interpreter i zaseban `settings.json/launch.json/tasks.json`.

---

## 2) Minimalne ispravke (copy/paste)

### 2.1. U `python-automation/labs/core_functions/.vscode/settings.json`

Zameni sadržaj ovim (čisto, bez ZF referenci):

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/labs/core_functions/.venv/Scripts/python.exe",

  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": ["labs/core_functions/tests"],

  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": "explicit",
    "source.fixAll.ruff": "explicit"
  },

  "terminal.integrated.defaultProfile.windows": "Git Bash",
  "python.analysis.typeCheckingMode": "basic",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true
}
```

> Zašto: Lokalni interpreter + lokalni test path (preseca globalno).
> (Globalni settings fiksira system Python 3.13 — zato ovo radimo lokalno.)&#x20;

---

### 2.2. U `python-automation/labs/core_functions/.vscode/launch.json`

Čisto pokretanje bilo kog **otvorenog fajla** iz `core_functions`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Run file (No Debug)",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "noDebug": true,
      "cwd": "${workspaceFolder}/labs/core_functions"
    },
    {
      "name": "Python: Debug file",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "noDebug": false,
      "cwd": "${workspaceFolder}/labs/core_functions"
    }
  ]
}
```

> Pre je CWD bio usmeren na **Zero Foundations**; čistimo da ne “beži” u pogrešan labs .

---

### 2.3. U `python-automation/labs/core_functions/.vscode/tasks.json`

Pytest taskovi za **core_functions** (bez ZF CWD/PYTHONPATH):

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Pytest -q (core_functions root)",
      "type": "shell",
      "options": { "cwd": "${workspaceFolder}/labs/core_functions" },
      "command": "python",
      "args": ["-m", "pytest", "-q"],
      "group": { "kind": "test", "isDefault": true },
      "presentation": {
        "reveal": "always",
        "panel": "dedicated",
        "clear": true
      }
    },
    {
      "label": "Pytest current file",
      "type": "shell",
      "options": { "cwd": "${workspaceFolder}/labs/core_functions" },
      "command": "python",
      "args": ["-m", "pytest", "-q", "${relativeFile}"],
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated",
        "clear": true
      }
    },
    {
      "label": "Pytest -k pattern…",
      "type": "shell",
      "options": { "cwd": "${workspaceFolder}/labs/core_functions" },
      "command": "python",
      "args": ["-m", "pytest", "-q", "-k", "${input:pytestPattern}"],
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "dedicated",
        "clear": true
      }
    }
  ],
  "inputs": [
    {
      "id": "pytestPattern",
      "type": "promptString",
      "description": "Unesi -k pattern (npr. dict or list or grid)",
      "default": "dict"
    }
  ]
}
```

> Prethodni `tasks.json` ciljao je **Zero Foundations** kao CWD – zato su `Alt+P` i ostalo išli na pogrešno mesto .

---

### 2.4. (Opciona) lokalna `keybindings.json` za **core_functions**

Ako želiš iste prečice ali za ovaj labs, napravi
`python-automation/labs/core_functions/.vscode/keybindings.json`:

```json
[
  {
    "key": "alt+r",
    "command": "workbench.action.terminal.sendSequence",
    "args": { "text": "python \"${file}\"\u000D" },
    "when": "editorTextFocus"
  },
  {
    "key": "alt+p",
    "command": "workbench.action.tasks.runTask",
    "args": "Pytest current file",
    "when": "resourceExtname == .py"
  },
  {
    "key": "alt+k",
    "command": "workbench.action.tasks.runTask",
    "args": "Pytest -k pattern…"
  }
]
```

> Globalni keybindings trenutačno startuju debug i pytest iz **Zero Foundations** (CWD + PYTHONPATH) — zato odvajamo lokalno za **core_functions** .

---

## 3) “Kako da pokrenem?” — 6 komandi koje ne smeš zaboraviti

```bash
# 1) Uđi u labs
cd python-automation/labs/core_functions

# 2) Aktiviraj lokalni venv (Git Bash)
source .venv/Scripts/activate

# 3) Pokreni trenutni fajl (najjednostavnije)
python dayB/try_code.py

# 4) Kao modul (ako dayB ima __init__.py)
python -m dayB.try_code

# 5) Testovi (svi / ovaj fajl / pattern)
pytest -q
pytest -q labs/core_functions/tests/test_dict_hashability.py
pytest -q -k dict

# 6) Sanity – gde sam i koji Python koristim
python -c "import sys,os;print(sys.executable);print(os.getcwd())"
```

---

## 4) Šta ostaje globalno, šta lokalno?

**Globalno** (User):

- Ekstenzije i UI (tema, font, brzine kursora…) — OK. &#x20;
- Ne fiksirati globalni `python.defaultInterpreterPath` (ili prihvati ali **lokalno preglasi** kao gore).

**Lokalno** (Workspace/Folder):

- `settings.json` sa **lokalnim interpreterom** i **pytestArgs** za taj labs.&#x20;
- `launch.json` i `tasks.json` sa **CWD = labs/core_functions** (ne ZF). &#x20;
- (opciono) `keybindings.json` ako želiš prečice vezane samo za ovaj labs.

---

## 5) Brzi checklist (pre nego što kreneš da radiš)

- [ ] U VS Code komandna paleta → **Python: Select Interpreter** → odaberi `labs/core_functions/.venv/...`
- [ ] Otvori terminal (integrisani) → vidi `which python` / `sys.executable` pokazuje na `labs/core_functions/.venv`
- [ ] `pytest -q` u **labs/core_functions** radi bez greške
- [ ] Alt+R/Alt+P rade u **core_functions** (ako si dodao lokalni `keybindings.json`)

---

Ako želiš, mogu i **da preradim tvoje postojeće fajlove 1-na-1** (globalne i lokalne) na tačno ove vrednosti i da ti samo prelepiš sadržaj — reci koji labs još treba (npr. `zero_foundations` ostaje kakav jeste).

---

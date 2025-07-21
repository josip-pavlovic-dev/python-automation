# 🧠 Pylance u VS Code-u – Detaljno objašnjenje (ENG + SRB)

---

## 🇬🇧 Pylance – What It Is and Why It Matters

**Pylance** is a high-performance language server extension for Python in Visual Studio Code. It provides fast and accurate IntelliSense, type checking, code navigation, and more.

### ✅ Key Features:

- **IntelliSense** (auto-complete, suggestions)
- **Type checking** via `pyright`
- **Hover tooltips** with function signatures and documentation
- **Code navigation**: jump to definition, symbol search
- **Error detection** in real time

> 🧠 Pylance is built on [Pyright](https://github.com/microsoft/pyright), a fast type checker.

### 📁 Pylance works best when:

- You use a `venv` environment
- Your project folder has a clean structure
- You add this to `settings.json`:

```json
"python.analysis.extraPaths": ["./"],
"python.analysis.typeCheckingMode": "basic"
```

---

## 🇷🇸 Pylance – šta je i zašto je važan

**Pylance** je dodatak za Visual Studio Code koji omogućava **inteligentno pisanje Python koda**:

- predloge (`IntelliSense`),
- upozorenja o greškama u realnom vremenu,
- prikaz funkcija i dokumentacije,
- brzo kretanje kroz kod,
- i proveru tipova (tipizaciju)!

### ✅ Glavne funkcionalnosti:

- **Automatski predlozi dok kucaš** (IntelliSense)
- **Hover info**: kada zadržiš miša iznad metode/funkcije
- **Pretraga definicija** (`F12`, `Ctrl+Click`)
- **Linting + type checking**: otkriva greške dok kucaš
- **Brzina**: sve radi trenutno jer koristi `Pyright`

---

## 🔍 Prepoznavanje ikonica u IntelliSense listi

| Ikonica | Značenje           | Primer                 |
| ------- | ------------------ | ---------------------- |
| 🟦 `f`  | Funkcija           | `now()`, `strftime()`  |
| 🟪 `C`  | Klasa              | `datetime`, `date`     |
| 🟫 `a`  | Atribut/Property   | `year`, `month`        |
| 📄      | Dokumentacija      | `__doc__`              |
| 🔧      | Sistem/metapodatak | `__class__`, `__dir__` |

> 📌 Ako ne vidiš predloge: pritisni `Ctrl + Space`

---

## ⚙️ Podesi `settings.json` kao profesionalac

```json
{
  "python.analysis.extraPaths": ["./"],
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.autoImportCompletions": true,
  "python.linting.enabled": true,
  "editor.formatOnSave": true
}
```

Ovo omogućava:

- bolji rad sa uvoženim modulima (`import`),
- da VS Code prepoznaje tvoju strukturu projekta,
- automatsko formatiranje i linting.

---

## 💡 Refleksi i trikovi

- `Ctrl + Hover`: vidiš dokumentaciju odmah
- `Ctrl + Click`: skok na definiciju
- `F12`: isto kao iznad
- `Shift + Alt + F`: formatira ceo fajl (ako je `formatOnSave` isključen)
- `Alt + Enter`: quick fix opcije (ako Pylance predloži refaktor)

---

## 🔄 Kada Pylance „ne vidi“ modul

Najčešći uzroci:

- `settings.json` nema `extraPaths`
- Pokušavaš `import` iz foldera koji nije u root-u
- Fali `__init__.py` (ako koristiš stariji Python)
- Nisi pokrenuo VS Code iz foldera projekta (reši sa `code .` iz Bash-a)

---

## 🧠 Zaključak

- Pylance ti je lični mentor u pozadini — uči te dok kucaš
- Ne ignoriši crvene linije — one su besplatni code review
- Ako ga ispravno podesiš, kod pišeš **brže, sigurnije i tačnije**

---

> 📎 Beleška: koristi `Pylance` svaki dan da ti sugestije postanu refleks. Kao inženjer – koristi alat koji ti povećava sigurnost i brzinu.


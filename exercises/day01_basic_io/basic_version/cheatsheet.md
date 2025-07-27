# 🧠 Cheatsheet – main.py

## 🔍 Line-by-line explanation (English + Serbian)

---

### 🔹 Line 1

```python
with open("input.txt", "r", encoding="utf-8") as input_file, \
```

📌 Explanation:

- `with` is a **context manager** – it ensures the file is automatically closed.
- `"r"` means we open the file in **read mode**.
- `as input_file` binds the file object to a variable.
- `\` is a **line continuation symbol**, allows splitting long statements.

📌 Objašnjenje:

- `with` je **kontekst menadžer** – fajl se automatski zatvara.
- `"r"` označava režim **čitanja**.
- `as input_file` dodeljuje fajl promenljivoj.
- `\` omogućava da se linija koda nastavi u sledećem redu.

---

### 🔹 Line 2

```python
     open("output.txt", "w", encoding="utf-8") as output_file:
```

📌 Explanation:

- Opens a new file in **write mode** (`"w"`).
- If the file exists, it is **overwritten**.
- If not, it's **created**.

📌 Objašnjenje:

- Otvara novi fajl u **režimu pisanja**.
- Ako fajl postoji → **biće prepisan**.
- Ako ne postoji → **biće kreiran**.

---

### 🔹 Line 3

```python
    for index, line in enumerate(input_file, start=1):
```

📌 Explanation:

- `enumerate()` returns `(index, line)` pairs.
- Starts indexing from `1`.

📌 Objašnjenje:

- `enumerate()` daje parove `(index, line)`.
- Indeksiranje počinje od `1`.

---

### 🔹 Line 4

```python
        output_file.write(f"{index}: {line}")
```

📌 Explanation:

- Formats and writes each line with its number.
- Uses **f-string** syntax: `f"{index}: {line}"`.

📌 Objašnjenje:

- Formatira i upisuje svaku liniju sa rednim brojem.
- Koristi **f-string**: `f"{index}: {line}"`.

---

## ✅ Why use a context manager with multiple files? | Šta `with` blok sa više fajlova postiže?

- Clean and compact code | Čist i kompaktan kod
- Automatically closes all files | Automatski `close()` za oba fajla – čak i ako se desi greška unutar petlje
- Handles errors safely | Sigurno rukovanje fajlovima
- Follows professional practices | Profesionalna praksa

---

## ⚠️ Tip: Newline handling | Savet: Rukovanje novim redom

##### `line` already includes `\n`, so you usually **don't need to add it manually** when writing.

##### `line` već uključuje `\n`, tako da ga obično **ne morate ručno dodavati** prilikom pisanja.

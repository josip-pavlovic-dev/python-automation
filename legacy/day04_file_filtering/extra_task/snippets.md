# ✂️ Snippets | _Isečci koda_

## 🔹 Find all `.py` and `.md` files | _Pronađi sve `.py` i `.md` fajlove_

```python
md_files = [p for p in base_dir.rglob("*.md") if p.is_file()]
py_files = [p for p in base_dir.rglob("*.py") if p.is_file()]
```

- Uses `rglob()` to search recursively | _Koristi `rglob()` za rekurzivnu pretragu_

---

## 🔹 Write results with headers | _Upiši rezultate sa zaglavljima_

```python
f.write(f"=== PYTHON FILES ({len(py_files)}) ===\n")
for p in py_files:
    f.write(f"{p.relative_to(base_dir)}\n")
```

- Adds a header and relative paths for `.py` files | _Dodaje zaglavlje i relativne putanje za `.py` fajlove_

---

## 🔹 Timestamp header | _Zaglavlje sa vremenom_

```python
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

- Adds date/time of execution | _Dodaje datum/vreme izvršavanja_

---

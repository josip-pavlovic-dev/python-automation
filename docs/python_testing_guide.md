# 🧪 Python Testing Guide — unittest + Mocking (EN + SR)

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 🧰 1. `unittest` Framework – Basics

### 🇬🇧 What is `unittest`?

- Python's built-in testing framework
- Tests are written as **classes** inheriting from `unittest.TestCase`
- Test methods must start with `test_`

```python
import unittest
from my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(my_function(2), 4)

if __name__ == '__main__':
    unittest.main()
```

### 🇷🇸 Šta je `unittest`?

- Ugrađeni Python framework za testiranje
- Testovi su klase koje nasleđuju `unittest.TestCase`
- Metode moraju počinjati sa `test_`

---

## ✅ 2. Ključne `assert` metode

| Metoda                   | Opis EN             | Opis SR              |
| ------------------------ | ------------------- | -------------------- |
| `assertEqual(a, b)`      | a == b              | da li su jednaki     |
| `assertTrue(x)`          | bool(x) is True     | da li je istinito    |
| `assertFalse(x)`         | bool(x) is False    | da li je lažno       |
| `assertRaises()`         | exception is raised | da li se baca greška |
| `assertRegex(s, r)`      | regex match         | da li regex odgovara |
| `assertIn(a, b)`         | a in b              | da li je sadržano    |
| `assertIsInstance(x, t)` | isinstance check    | tip podatka          |

---

## 🧱 3. Test Fixtures: `setUp()` i `tearDown()`

```python
class MyTest(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
```

- 🇬🇧 These methods run **before/after each test**
- 🇷🇸 Izvršavaju se pre i posle svakog testa

---

## 🎭 4. Mocking – `unittest.mock`

### 🇬🇧 What is mocking?

- Replace real functions or objects during testing

### 🇷🇸 Šta je mocking?

- Zamenjuješ stvarne funkcije sa lažnima radi kontrole testa

```python
from unittest.mock import patch

@patch("module.function")
def test_func(mock_func):
    mock_func.return_value = "fake result"
    assert module.function() == "fake result"
```

Use when:

- Testing APIs
- Avoiding file operations
- Controlling unpredictable outputs

---

## 🧪 5. Test folder structure (project-specific)

```
python-automation/
├── day04_datetime/
│   └── timestamp_generator.py
├── tests/
│   └── test_day04_datetime/
│       └── test_timestamp_generator.py
```

- Fajlovi uvek imaju prefiks `test_`
- `tests/` folder odražava strukturu glavnih skripti

---

## 🚀 6. Pokretanje testova

### 1. Terminal (svi testovi):

```bash
python -m unittest discover -s tests
```

### 2. Terminal (pojedinačni fajl):

```bash
python -m unittest tests/test_day04_datetime/test_timestamp_generator.py
```

### 3. VS Code launch config:

```json
{
  "name": "🧪 Run all tests",
  "type": "python",
  "request": "launch",
  "module": "unittest",
  "args": ["discover", "-s", "tests"],
  "console": "integratedTerminal"
}
```

---

## ❗ 7. Tipične greške u testiranju

| Greška                | Objašnjenje                      |
| --------------------- | -------------------------------- |
| `ModuleNotFoundError` | loš import, fali `__init__.py`   |
| Test nije vidljiv     | ime metode ne počinje sa `test_` |
| Test ne startuje      | fali `unittest.main()`           |
| Ne detektuje fajl     | fajl ne počinje sa `test_`       |

---

## 🧠 8. Zaključak

- ✅ Pisanje testova = profesionalni razvoj
- ✅ Koristi `setUp` + `tearDown` za pripremu test okruženja
- ✅ Mockuj sve što zove API, piše u fajl ili briše podatke
- ✅ Pokreći testove svakodnevno, ne samo kad sumnjaš

---

📁 Lokacija: `docs/python_testing_guide.md`
✍️ Autor: Josip Pavlović
📅 Ažurirano: 2025-07-21

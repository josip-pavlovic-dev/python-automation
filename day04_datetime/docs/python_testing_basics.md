# 🧪 Vodič kroz Testiranje u Pythonu (unittest sistem)

---

## 📌 Osnovna svrha testiranja

**Testiranje = sigurnost.** Osnovni cilj je da se automatizovano proveri:

- da li funkcije rade kako treba,
- da li vraćaju tačne vrednosti,
- da li se greške detektuju i hendlaju,
- da li sistem radi posle izmene (tzv. *regresija*).

> 🧠 **Pravilo koje moraš zapamtiti:** Svaka funkcionalnost koja može da pukne, mora imati test koji puca pre nje.

---

## 🧰 Šta je `unittest`

To je Python-ov ugrađeni framework za testiranje (nije potreban dodatni install).

Test se piše kao **klasa** koja nasleđuje `unittest.TestCase`, i u njoj imaš metode koje počinju sa `test_`.

```python
import unittest
from my_module import my_function

class TestMyFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(my_function(2), 4)

if __name__ == '__main__':
    unittest.main()
```

> 📌 Svaki `assert` proverava jedno pravilo.

---

## ✅ Ključne `assert` metode koje moraš znati

| Metoda                   | Čemu služi                                 |
| ------------------------ | ------------------------------------------ |
| `assertEqual(a, b)`      | Da li su `a == b`                          |
| `assertTrue(x)`          | Da li je `bool(x) == True`                 |
| `assertFalse(x)`         | Da li je `bool(x) == False`                |
| `assertRaises()`         | Da li se izuzetak baca                     |
| `assertRegex(s, r)`      | Da li string `s` odgovara regex izrazu `r` |
| `assertIn(a, b)`         | Da li je `a` u `b`                         |
| `assertIsInstance(x, t)` | Da li je `x` instanca tipa `t`             |

> 🧠 Reflex: kad pišeš funkciju, automatski razmisli: "Šta bi moglo da pođe naopako i kako da to testiram?"

---

## 🗂️ Struktura testova po folderima (kao u tvom projektu)

```
python-automation/
├── day04_datetime/
│   └── timestamp_generator.py
├── tests/
│   └── test_day04_datetime/
│       └── test_timestamp_generator.py
```

Test fajl uvek nosi prefiks `test_` i nalazi se u odgovarajućem potfolderu `tests/`.

---

## 🚀 Pokretanje testova

1. **Iz terminala**:

```bash
python -m unittest discover -s tests
```

2. **Iz VS Code launch.json**: Dodaj:

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

3. **Pojedinačni fajl:**

```bash
python -m unittest tests/test_day04_datetime/test_timestamp_generator.py
```

---

## ❗ Tipične greške

| Greška                | Uzrok                                             |
| --------------------- | ------------------------------------------------- |
| `ModuleNotFoundError` | loš import, ne vidi folder ako nema `__init__.py` |
| Test se ne vidi       | metoda se ne zove `test_*`                        |
| Test ne startuje      | nema `unittest.main()`                            |
| Ne detektuje fajl     | `test_` nije prefiks fajla                        |

> 📌 Reflex: kad ti test "ne postoji" ili "ne radi", **uvek prvo proveri** da li si ga imenovao kako treba i da li ima `test_` prefiks.

---

## 🧠 Zaključak za danas:

- `unittest` je **osnova automatizovanog testiranja** u Pythonu.
- Uvek razdvajaj testove u poseban `tests/` folder.
- Pokreći testove svaki dan, ne samo kad sumnjaš.
- Pisanje testova uči te **jasnoći razmišljanja i organizaciji koda**.
- Testovi su kao kaciga — koristi ih i kad "samo ideš do prodavnice".

---

Ako želiš, mogu ti generisati PDF verziju ovog vodiča, kao i sledeći deo: `unittest.mock`, koji se koristi za simulaciju API poziva, logger-a i fajlova bez da stvarno pozivaš spoljne sisteme.

Tvoj profa 🙌


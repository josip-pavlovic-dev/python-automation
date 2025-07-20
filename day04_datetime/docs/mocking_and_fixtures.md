# 🧪 Mocking and Fixtures in Python `unittest` – ENG + SRB

---

## 🇬🇧 Mocking and Fixtures – Core Concepts

Testing in real-world scenarios often requires:

- **Replacing real functions** (like file I/O or APIs)
- **Creating test environments** before tests
- **Cleaning up afterward**

We use:

- `unittest.mock.patch`, `Mock`, `MagicMock`
- `setUp()` and `tearDown()` fixture methods

---

### 🔁 What is Mocking?

Mocking means **replacing a real object/function with a fake one** during testing.

```python
from unittest.mock import patch

@patch("module.function")
def test_something(mock_func):
    mock_func.return_value = "fake result"
    assert module.function() == "fake result"
```

Use cases:

- Avoid hitting real APIs
- Avoid writing to disk
- Control unpredictable outputs

---

### 🧱 Fixtures: setUp and tearDown

```python
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        # prepare env before each test
        self.test_file = "test.txt"

    def tearDown(self):
        # cleanup after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
```

Fixtures run **before and after each test method**.

---

## 🇷🇸 Mocking i Fixtures – Osnovni Koncepti

U realnim testovima često želimo da:

- **Zamenimo prave funkcije** (npr. koje brišu fajlove)
- **Napravimo test okruženje** pre testa
- **Očistimo okruženje** posle testa

Koristimo:

- `unittest.mock.patch`, `Mock`, `MagicMock`
- `setUp()` i `tearDown()` metode u klasama testova

---

### 🔁 Šta je Mocking?

Mocking znači da **umesto prave funkcije koristiš lažnu** tokom testa.

```python
from unittest.mock import patch

@patch("module.function")
def test_nesto(mock_func):
    mock_func.return_value = "lažni rezultat"
    assert module.function() == "lažni rezultat"
```

Primeri upotrebe:

- Da test ne zove pravi API
- Da test ne piše na disk
- Da test ima predvidiv ishod

---

### 🧱 Fixtures: setUp i tearDown

```python
import unittest

class MojTest(unittest.TestCase):
    def setUp(self):
        # priprema pre svakog testa
        self.test_fajl = "test.txt"

    def tearDown(self):
        # čišćenje posle svakog testa
        if os.path.exists(self.test_fajl):
            os.remove(self.test_fajl)
```

`setUp()` i `tearDown()` se izvršavaju pre i posle SVAKOG testa.

---

## ✅ Kada koristiš mocking i fixtures?

- Kada koristiš `logger.log()` → mockuj upis u fajl
- Kada testiraš funkcije koje brišu fajlove → koristi `setUp()` da ih napraviš, `tearDown()` da ih obrišeš
- Kada testiraš API pozive → koristi `@patch("requests.get")`

---

## 🧠 Zaključak

- Mock je kontrolisana zamena za stvarnu funkciju
- Fixtures ti omogućavaju da praviš i brišeš fajlove, foldere, konekcije itd. tokom testa
- Profesionalni testovi uvek uključuju `setUp()` i `tearDown()`
- Nikad ne koristi pravi `open()`, `os.remove()` itd. bez kontrole u testu

> 🧪 Kombinuj `@patch` + `setUp` i `tearDown` za stabilne, predvidive testove


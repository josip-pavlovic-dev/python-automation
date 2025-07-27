# 🧠 Šta je _kontekst menadžer_ u Pythonu?

#### **Kontekst menadžer** je mehanizam koji upravlja nekim _resursom_ — i to na sledeći način:

1. Automatski ga **priprema** pre nego što ga koristiš (`__enter__`)
2. Automatski ga **zatvara, oslobađa, čisti** kada si završio (`__exit__`)

#### Najpoznatiji primer u Pythonu je:

```python
with open("neki_fajl.txt", "r") as f:
    sadržaj = f.read()
```

---

## 🧩 Zašto postoji `with`?

#### Da bi izbegao **ručno otvaranje i zatvaranje fajlova** kao u ovome:

```python
f = open("neki_fajl.txt", "r")
sadržaj = f.read()
f.close()  # Ne smeš zaboraviti!
```

Ako se dogodi greška pre `f.close()`, fajl može ostati otvoren – što može dovesti do:

- curenja memorije,
- zaključanih fajlova (na Windowsu naročito),
- gubitka podataka.

---

## ✅ Prednosti kontekst menadžera (`with`)

| Prednost              | Objašnjenje                                         |
| --------------------- | --------------------------------------------------- |
| 📦 Automatizacija     | Fajl se zatvara automatski                          |
| 🔐 Sigurnost          | Greške neće ostaviti fajl u lošem stanju            |
| 🧹 Čist kod           | Više nema potrebe za ručnim `try/finally` blokovima |
| 🔄 Višestruki resursi | Možeš otvoriti više fajlova u jednoj liniji         |

---

## 🧪 Šta se zaista dešava iza kulisa?

Kada napišeš:

```python
with open("file.txt", "r") as f:
    data = f.read()
```

Python poziva ove metode na objektu koji `open()` vraća:

1. `f.__enter__()` → vraća ti otvoreni fajl
2. `f.__exit__()` → automatski poziva `close()` kada `with` blok završi

Zato se kaže da je objekat **file handler** (kao `f`) **kontekst menadžer** – jer implementira `__enter__` i `__exit__`.

---

## 🧠 Šta je kontekst menadžer u Pythonu?:

#### 🗣️ _To je mehanizam koji automatski upravlja resursima kao što su fajlovi, i omogućava da se oni sigurno koriste i zatvore. Najčešće se koristi sa `with` blokom, koji obezbeđuje da se fajl automatski zatvori čak i ako se desi greška._

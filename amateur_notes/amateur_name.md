# 📌 `__name__` u Python-u | _Specijalna promenljiva u Python-u_

## 🛠️ Osnovna ideja | _Basic idea_

`__name__` je **ugrađena promenljiva** u svakom Python fajlu koja pokazuje **kontekst izvršavanja** tog fajla.

- Ako je fajl **pokrenut direktno**, `__name__` će biti `"__main__"`.
- Ako je fajl **importovan** u drugi fajl (kao modul), `__name__` će biti **ime tog modula**.

```python
# primer: pokretanje direktno
print(__name__)
# izlaz: "__main__"

# primer: importovanje
# u drugom fajlu:
# import logger
# print(__name__) → "logger"
```

---

## 📌 Kako se koristi sa `if __name__ == "__main__":` | _Kontrola toka programa_

Ovaj uslov znači: **izvrši sledeći blok koda samo ako se fajl pokreće direktno**.
Ako se fajl importuje — kod unutar ovog bloka se **neće pokrenuti**.

Tipičan primer:

```python
if __name__ == "__main__":
    main()
```

Ovo je **standard Python prakse** i koristi se u svim ozbiljnim projektima.

---

## 🧠 Povezanost sa `getLogger(__name__)`

```python
import logging
logger = logging.getLogger(__name__)
```

- Logger dobija ime modula iz kog se poziva (`logger`, `main`, `interactive_folder_browser`, itd.).
- Time se omogućava **precizno praćenje izvora log poruka**.

📌 **Zašto je ovo bitno?**
Ako koristiš `logging.info()` bez imena loggera, sve se beleži kao `"root"`, bez informacije iz kog modula potiče poruka.

---

## 🛠️ Analogija | _Analogy_

- `__name__` = **ime pošiljaoca** (da znaš ko je poslao poruku)
- `getLogger(__name__)` = **uvođenje tog pošiljaoca u knjigu evidencije**

---

## ✅ Kratak pregled | _Quick summary_

| Element                  | Značenje                                             |
| ------------------------ | ---------------------------------------------------- |
| `__name__ == "__main__"` | Fajl se pokreće direktno                             |
| `__name__ == "logger"`   | Fajl je importovan kao modul                         |
| `getLogger(__name__)`    | Logger dobija ime modula (izvor poruke)              |
| Prednost                 | Modularno praćenje i filtriranje logova po fajlovima |

---

💡 **Napomena za dalje učenje:**
`__name__` je temelj za razumevanje **Python modula, paketa** i **testiranja**.
U Pytest-u, ovaj koncept omogućava da test fajlovi ne izvršavaju test kod pri importovanju, već samo kad ih pokrene pytest.

---

# 📚 OOP Foundations – Lekcije 1–3

## 🎯 Cilj

Postepeno izgraditi razumevanje osnovnih OOP pojmova u Python-u:

- Klase i objekti
- Nasleđivanje
- Polimorfizam i apstraktne klase

Svi primeri su u **Amateur modu**: jasno, ali sa dovoljno tehničke dubine za ozbiljan početak.

---

# 🏗 Lekcija 1 – Klase i objekti

## 📌 Pojam

- **Klasa** – plan (šablon) prema kojem pravimo objekte.
- **Objekat** – konkretna instanca klase, sa sopstvenim podacima i ponašanjem.
- **Zašto OOP?** – omogućava grupisanje podataka (atributa) i funkcija (metoda) u jednu celinu.

💡 **Analogija**: Plan kuće (klasa) i izgrađena kuća (objekat).

---

## 🛠 Minimalni primer

```python
class Logger:
    def __init__(self, name):
        self.name = name  # atribut instance

    def log(self, message):
        print(f"[{self.name}] {message}")  # metoda

app_logger = Logger("AppLogger")
error_logger = Logger("ErrorLogger")

app_logger.log("Aplikacija pokrenuta.")
error_logger.log("Došlo je do greške.")
```

---

## 📌 Ključne tačke

1. `class Logger:` – definiše klasu.
2. `__init__` – konstruktor, pokreće se pri kreiranju objekta.
3. `self.name` – atribut instance.
4. Metode definišu ponašanje objekata.
5. Više objekata može poticati iz iste klase, ali sa različitim vrednostima atributa.

---

## 🧪 Mini vežba

Napravi klasu `FileLogger` koja:

- ima atribut `filename`
- ima metodu `log_to_file(message)` koja dodaje poruku u fajl.

Testiraj sa dva različita fajla.

---

# 🏗 Lekcija 2 – Nasleđivanje

## 📌 Pojam

- **Nasleđivanje** omogućava child klasi da preuzme osobine i ponašanje parent klase.
- Cilj: ponovna upotreba koda i proširenje funkcionalnosti.

💡 **Analogija**: Plan “vozilo” iz koga nastaju planovi “auto” ili “kamion”.

---

## 🛠 Primer

```python
class Vozilo:
    def __init__(self, boja, brzina):
        self.boja = boja
        self.brzina = brzina

    def vozi(self):
        print(f"Vozilo se kreće brzinom {self.brzina} km/h.")

class Auto(Vozilo):
    def __init__(self, boja, brzina, marka):
        super().__init__(boja, brzina)
        self.marka = marka

    def predstavi(self):
        print(f"Ovo je {self.marka}, boja {self.boja}, brzina {self.brzina} km/h.")
```

---

## 📌 Ključne tačke

- `super().__init__()` poziva konstruktor parent klase.
- Child klasa može **koristiti**, **menjati** ili **dodavati** metode.
- Višestruko nasleđivanje postoji, ali koristi se oprezno.

---

## 🧪 Mini vežba

1. Napravi klasu `Osoba` sa atributima `ime` i `prezime`.
2. Napravi klasu `Zaposleni` koja nasleđuje `Osoba` i dodaje `pozicija`.
3. Prepiši metodu `predstavi_se()` tako da prikazuje i poziciju.

---

# 🏗 Lekcija 3 – Polimorfizam i apstraktne klase

## 📌 Polimorfizam

Sposobnost objekata različitih klasa da odgovore na isti poziv metode na svoj način.

💡 **Primer**: `sviraj()` za gitaru, bubanj i violinu – isti poziv, različita izvedba.

---

## 🛠 Primer nasleđivanja

```python
class Zivotinja:
    def glas(self):
        print("Neka životinja pravi zvuk.")

class Pas(Zivotinja):
    def glas(self):
        print("Av, av!")

class Macka(Zivotinja):
    def glas(self):
        print("Mjau!")

def pusti_da_prica(zivotinja):
    zivotinja.glas()

pusti_da_prica(Pas())
pusti_da_prica(Macka())
```

---

## 📌 Duck typing

Python ne zahteva nasleđivanje za polimorfizam – ako objekat ima traženu metodu, može da se koristi.

```python
class Gitara:
    def sviraj(self):
        print("Gitara svira akorde.")

class Bubanj:
    def sviraj(self):
        print("Bubanj udara ritam.")

def nastup(instr):
    instr.sviraj()

nastup(Gitara())
nastup(Bubanj())
```

---

## 📌 Apstraktne klase

Koriste se da definišu obavezan interfejs za child klase.

```python
from abc import ABC, abstractmethod

class LoggerBase(ABC):
    @abstractmethod
    def log(self, poruka):
        pass

class ConsoleLogger(LoggerBase):
    def log(self, poruka):
        print(f"[Console] {poruka}")
```

---

## 📌 Ključne tačke

- Polimorfizam omogućava fleksibilan rad sa različitim objektima.
- Duck typing čini Python posebno prilagodljivim.
- Apstraktne klase osiguravaju da child klase implementiraju ključne metode.

---

## 🧪 Mini vežba

1. Napravi apstraktnu klasu `Oblik` sa metodom `povrsina()`.
2. Implementiraj `Pravougaonik` i `Krug` sa konkretnim formulama.
3. Testiraj polimorfizam pozivom `povrsina()` nad listom objekata različitih tipova.

---

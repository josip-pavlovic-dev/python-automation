# OOP Foundations — chat reference
> Chat reference • Source: OOP Foundations chat (zajednički folder)
> Scope: teorijska referenca za Zero Foundations (nije deliverable)
> Version: v1.0 • Last updated: 2025-08-16

## Table of Contents | _Sadržaj_
- [📚 OOP Foundations – Lekcija 1](#-oop-foundations-lekcija-1)
- [1️⃣ Zašto uopšte OOP?](#1-zasto-uopste-oop)
- [2️⃣ Klasa – plan, šablon, nacrt](#2-klasa-plan-sablon-nacrt)
- [3️⃣ Objekat – konkretna instanca](#3-objekat-konkretna-instanca)
- [4️⃣ Više primera iz realnog sveta](#4-vise-primera-iz-realnog-sveta)
- [Primer 1 – Korisnici sistema](#primer-1-korisnici-sistema)
- [Primer 2 – Logger (već povezano sa tvojim projektom)](#primer-2-logger-vec-povezano-sa-tvojim-projektom)
- [5️⃣ Analizirajmo `self` – ključ OOP-a u Pythonu](#5-analizirajmo-self-kljuc-oop-a-u-pythonu)

> Chat reference • Izvor: OOP Foundations chat (zajednički folder)
> Uloga: teorijska referenca za Zero Foundations; nije deliverable projekta.

📢 Novi chat — OOP Foundations serija
"Uvod u objektno-orijentisano programiranje kroz praktične primere, sa tehničkim i logičkim objašnjenjima."

🎯 Cilj:

Postepeno graditi razumevanje OOP koncepta (klase, objekti, atributi, metode, nasleđivanje, polimorfizam)

Koristiti Amateur mod: tehničko + logičko objašnjenje + mini demonstracija na svakom primeru

Direktno povezivati teoriju sa aktuelnim projektima (logger.py, budući formatter moduli itd.)

🗂 Struktura:

Uvod u OOP – Zašto postoji, šta rešava i gde se koristi u Python automatizaciji

Osnovni pojmovi – klase, objekti, **init**, atributi i metode

Principi OOP-a – enkapsulacija, nasleđivanje, polimorfizam

Napredne teme – magic methods, apstraktne klase, interfejsi

Primena u praksi – kreiranje OOP verzije logger-a i drugih modula

🛠 Način rada:

Jedan novi koncept dnevno — uz pauze za mini vežbe

Kroz realne primere povezane sa trenutnim repozitorijumom

Bilingvalna dokumentacija (EN + SR), sa badge-ovima i istim standardima kao i sadašnji repo

📌 Prva lekcija:
"Šta je klasa i kako se iz nje pravi objekat?" — uz poređenje sa realnim svetom i jednostavnim kod primerom.

Razumem — želiš **30 minuta fokusiranog materijala** na srpskoj latinici, koji ide u dubinu i sa što više primera, tako da ti ostane čvrsta osnova bez koje nijedan junior programer ne može reći da zna OOP.
Pripremiću ti **celu lekciju 1** u **Amateur modu**, ali proširenu:

- biće puno primera, objašnjenja korak-po-korak, analogija i mikro-vežbi,
- ići ćemo od najosnovnijeg do nivoa na kojem već možeš da povezuješ sa budućim projektima (logger, formatter moduli).

---

# 📚 OOP Foundations – Lekcija 1

**Tema:** Šta je klasa i kako se iz nje pravi objekat?
**Cilj:** Razumeti osnovu OOP-a u Pythonu i biti sposoban da samostalno definišeš klase i kreiraš objekte.

---

### 1️⃣ Zašto uopšte OOP?

U proceduralnom programiranju (ono što si radio do sada), imaš:

- promenljive (podatke)
- funkcije (operacije nad tim podacima)

Problem: kod brzo postaje **rasut**, teško ga je održavati i ponovo koristiti.

**OOP (Objektno-Orijentisano Programiranje)** omogućava da podatke i funkcije **spakujemo u jednu celinu** – objekat.
Taj objekat ima svoje **atribute** (podatke) i **metode** (funkcije), i ponaša se kao **“mali program”** unutar većeg sistema.

💡 **Primer iz prakse:**
Zamišljaj Python skriptu kao gradilište. U proceduralnom pristupu, svi radnici i alat su pomešani u jednom velikom skladištu. U OOP-u, svaki “tim” (klasa) ima svoj prostor, alat i pravila rada.

---

### 2️⃣ Klasa – plan, šablon, nacrt

```python
class Auto:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def predstavi(self):
        print(f"Ovo je {self.marka} {self.model}.")
```

- `class Auto:` → definiše novu klasu.
- `__init__` → konstruktor, automatski se pokreće kad pravimo objekat.
- `self` → pokazuje na **taj** konkretni objekat (bez njega Python ne zna na kome radimo).
- `self.marka` i `self.model` → **atributi instance**.

---

### 3️⃣ Objekat – konkretna instanca

```python
auto1 = Auto("Toyota", "Corolla")
auto2 = Auto("BMW", "X5")

auto1.predstavi()
auto2.predstavi()
```

**Izlaz:**

```
Ovo je Toyota Corolla.
Ovo je BMW X5.
```

Svaki objekat ima **svoje vrednosti atributa**, iako potiče iz iste klase.

---

### 4️⃣ Više primera iz realnog sveta

### Primer 1 – Korisnici sistema

```python
class Korisnik:
    def __init__(self, ime, email):
        self.ime = ime
        self.email = email

    def predstavi(self):
        print(f"Korisnik: {self.ime} ({self.email})")

k1 = Korisnik("Milan", "milan@example.com")
k2 = Korisnik("Ana", "ana@example.com")

k1.predstavi()
k2.predstavi()
```

---

### Primer 2 – Logger (već povezano sa tvojim projektom)
> Napomena: U ovim primerima naglašavamo **kompozicija > nasleđivanje** (fleksibilnije testiranje i manja sprega).

```python
class Logger:
    def __init__(self, ime):
        self.ime = ime

    def log(self, poruka):
        print(f"[{self.ime}] {poruka}")

app_logger = Logger("AppLogger")
error_logger = Logger("ErrorLogger")

app_logger.log("Aplikacija pokrenuta.")
error_logger.log("Došlo je do greške.")
```

Ovaj primer lako kasnije proširujemo da logger piše u fajl, filtrira tipove poruka itd.

---

### 5️⃣ Analizirajmo `self` – ključ OOP-a u Pythonu

`self` je **referenca na objekat koji se trenutno koristi**.
Ako napraviš dva objekta, `self` u jednom pokazuje na jedan skup podataka, a u drugom na drugi.

```python
class Test:
    def __init__(self, x):
        self.x = x

t1 = Test(5)
t2 = Test(10)

print(t1.x)  # 5
print(t2.x)  # 10
```

Bez `self`, svi bi delili istu vrednost – izgubili bismo nezavisnost objekata.

---

### 6️⃣ Instance atributi vs. Class atributi

```python
class Auto:
    broj_tockova = 4  # Class atribut

    def __init__(self, marka):
        self.marka = marka  # Instance atribut

a1 = Auto("Toyota")
a2 = Auto("BMW")

print(a1.broj_tockova)  # 4
print(a2.broj_tockova)  # 4

Auto.broj_tockova = 6  # menja za sve instance
print(a1.broj_tockova)  # 6
```

- **Instance atribut** → specifičan za svaki objekat.
- **Class atribut** → zajednički za sve objekte.

---

### 7️⃣ Metode – ponašanje objekata

### Instance metoda

Radi sa podacima iz **konkretnog** objekta.

```python
class BankovniRacun:
    def __init__(self, vlasnik, stanje):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplata(self, iznos):
        self.stanje += iznos
        print(f"Uplaćeno: {iznos}. Novo stanje: {self.stanje}")
```

### Class metoda

Radi sa klasom kao celinom (retko se koristi u osnovama).

```python
@classmethod
def info_o_klasi(cls):
    print("Ovo je bankovni račun.")
```

### Static metoda

Ne zavisi od objekta, samo logički pripada klasi.

```python
@staticmethod
def konvertuj_valutu(iznos, kurs):
    return iznos * kurs
```

---

### 8️⃣ Mikro-vežbe (uradi odmah)

1. Napravi klasu `Knjiga` sa atributima `naslov` i `autor` i metodom `prikazi_info`.
2. Napravi dva objekta i pozovi metod na oba.
3. Dodaj **class atribut** `biblioteka = "Gradska biblioteka"`.
4. Napravi **static metodu** `broj_stranica_u_satu(br_strana, sati)` koja vraća rezultat `br_strana * sati`.

---

### 9️⃣ Povezivanje sa tvojim projektima

- Logger može biti **osnovna klasa** koju kasnije nasleđuju `FileLogger`, `ConsoleLogger`, `FormatterLogger`.
- Formatter moduli mogu biti posebne klase koje logger koristi (kompozicija).
- Umesto da funkcije stoje razbacane po fajlu, biće **organizovane** unutar odgovarajućih klasa.

---

### 🔑 Ključne tačke za pamćenje

- **Klasa** = plan, **objekat** = konkretna instanca.
- **self** uvek ide kao prvi argument metoda instance.
- Atributi = podaci, metode = ponašanje.
- Instance atributi su privatni podaci objekta, class atributi su zajednički.
- OOP = modularnost + ponovna upotreba + lakše održavanje.

---

Odlično ✅
Spremiću ti **Lesson 2** tako da dobiješ još **30 minuta** materijala, sa fokusom na **nasleđivanje u OOP-u**, jer je to prva “ozbiljna” nadogradnja na osnove iz Lesson 1.
Ići ćemo **Amateur mod** pristupom: čvrsta logika, realni primeri, kod, vežbe i povezivanje sa tvojim projektima.

---

# 📚 OOP Foundations – Lesson 2

**Tema:** Nasleđivanje (Inheritance)
**Cilj:** Razumeti kako jedna klasa može da koristi i proširuje kod iz druge klase.

---

### 1️⃣ Šta je nasleđivanje?

**Definicija:**
Nasleđivanje je mehanizam u OOP-u koji omogućava da jedna klasa (**child** ili **subclass**) preuzme osobine i ponašanje druge klase (**parent** ili **superclass**).

💡 Prednost:

- **Ponovna upotreba koda** – pišemo ga jednom, koristimo više puta.
- **Proširivanje funkcionalnosti** bez menjanja originalne klase.

**Analogy:**
Ako imaš osnovni plan “vozilo” (sa brzinom, bojom, brojem točkova), iz njega možeš praviti specijalizovane planove za auto, motor, kamion – svi nasleđuju osnovne osobine, ali dodaju svoje.

---

### 2️⃣ Osnovni primer

```python
# Parent class
class Vozilo:
    def __init__(self, boja, brzina):
        self.boja = boja
        self.brzina = brzina

    def vozi(self):
        print(f"Vozilo se kreće brzinom {self.brzina} km/h.")

# Child class
class Auto(Vozilo):
    def __init__(self, boja, brzina, marka):
        super().__init__(boja, brzina)  # poziv konstruktora parent klase
        self.marka = marka

    def predstavi(self):
        print(f"Ovo je {self.marka}, boja {self.boja}, brzina {self.brzina} km/h.")

auto1 = Auto("crvena", 120, "Toyota")
auto1.vozi()       # metoda iz parent klase
auto1.predstavi()  # metoda iz child klase
```

**Ključne tačke:**

- `class Auto(Vozilo)` → Auto nasleđuje Vozilo.
- `super().__init__()` → poziva konstruktor parent klase.
- Child klasa može da koristi **sve metode i atribute** parent klase.

---

### 3️⃣ Overriding metoda (prepisivanje ponašanja)

Child klasa može da **zameni** metodu iz parent klase ako joj treba drugačije ponašanje.

```python
class Vozilo:
    def vozi(self):
        print("Vozilo se kreće.")

class Bicikl(Vozilo):
    def vozi(self):
        print("Bicikl se vozi pedaliranjem.")

v = Vozilo()
b = Bicikl()

v.vozi()  # Vozilo se kreće.
b.vozi()  # Bicikl se vozi pedaliranjem.
```

**Kada koristiti?**
Kad osnovna funkcionalnost postoji, ali treba prilagoditi specifičnim potrebama podklase.

---

### 4️⃣ Dodavanje novih metoda u child klasu

Child klasa ne mora samo da menja stare metode – može da dodaje nove.

```python
class Logger:
    def log(self, poruka):
        print(f"[LOG] {poruka}")

class FileLogger(Logger):
    def log_to_file(self, poruka, filename):
        with open(filename, "a") as f:
            f.write(f"[LOG] {poruka}\n")

fl = FileLogger()
fl.log("Ovo ide u konzolu.")
fl.log_to_file("Ovo ide u fajl.", "log.txt")
```

---

### 5️⃣ Višestruko nasleđivanje

Python dozvoljava da child klasa nasledi više parent klasa.
Koristi se retko, ali može biti moćno.

```python
class A:
    def pozdrav(self):
        print("Pozdrav iz A")

class B:
    def zdravo(self):
        print("Zdravo iz B")

class C(A, B):
    pass

c = C()
c.pozdrav()
c.zdravo()
```

⚠️ U praksi – koristi pažljivo, može zakomplikovati kod.

---

### 6️⃣ Praktičan primer za tvoje projekte – Logger hijerarhija
> Napomena: U ovim primerima naglašavamo **kompozicija > nasleđivanje** (fleksibilnije testiranje i manja sprega).

```python
class BaseLogger:
    def log(self, poruka):
        print(f"[LOG] {poruka}")

class FileLogger(BaseLogger):
    def log(self, poruka):
        super().log(poruka)  # poziv originalne log metode
        with open("app.log", "a") as f:
            f.write(f"[LOG] {poruka}\n")

class ErrorLogger(FileLogger):
    def log_error(self, poruka):
        self.log(f"[ERROR] {poruka}")

# Korišćenje
log = ErrorLogger()
log.log("Normalna poruka")
log.log_error("Ovo je greška")
```

**Zašto je ovo dobro?**

- `BaseLogger` → definisan samo jednom.
- `FileLogger` → proširuje funkcionalnost pisanjem u fajl.
- `ErrorLogger` → dodaje specifične metode za greške.
- Kada sutra dodaš `FormatterLogger`, nećeš menjati postojeće klase, samo dodati novu.

---

### 7️⃣ Mikro-vežbe

1. Napravi klasu `Osoba` sa atributima `ime` i `prezime` i metodom `predstavi_se()`.
2. Napravi child klasu `Zaposleni` koja ima i `pozicija` i metod `prikazi_posao()`.
3. Dodaj metodu u child klasu koja prepisuje `predstavi_se()` tako da ispisuje i poziciju.
4. Testiraj sa nekoliko primera.

---

### 8️⃣ Gde greše početnici?

- Zaborave da pozovu `super().__init__()` pa izgube inicijalizaciju parent klase.
- Prepisuju metode kad to nije potrebno.
- Previše duboko prave hijerarhiju (teško za održavanje).
- Mešaju instance i class atribute u nasleđivanju.

---

### 🔑 Ključne tačke

- Nasleđivanje omogućava **ponovnu upotrebu i proširenje** koda.
- `super()` služi za pozivanje metoda iz parent klase.
- Možemo **dodati** nove metode ili **prepisati** postojeće.
- Oprezno sa višestrukim nasleđivanjem – razmisli o čitljivosti.

---

Razumem 👍
Završićemo današnji blok sa **Lesson 3 – Polimorfizam i apstraktne klase**, tako da imaš **tri osnovna stuba OOP-a** kompletna.
Zadržaćemo **Amateur mod** pristup – jednostavno, ali dubinski, sa dovoljno primera da možeš odmah da primeniš.

---

# 📚 OOP Foundations – Lesson 3

**Tema:** Polimorfizam i apstraktne klase
**Cilj:** Razumeti kako objekti različitih klasa mogu da se koriste na isti način i kako apstraktne klase pomažu u definisanju zajedničkog interfejsa.

---

### 1️⃣ Šta je polimorfizam?

**Definicija:**
Polimorfizam znači **“više oblika”** – sposobnost različitih objekata da odgovore na isti poziv metode na svoj način.

💡 Primer iz života:
Ako različiti muzički instrumenti imaju metod `sviraj()`, violina, gitara i bubanj će ga izvesti potpuno drugačije, ali kod koji ih koristi ne mora da zna detalje.

---

### 2️⃣ Polimorfizam kroz nasleđivanje

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

**Izlaz:**

```
Av, av!
Mjau!
```

Kod `pusti_da_prica` ne zna da li je dobio psa ili mačku – samo poziva `glas()`.

---

### 3️⃣ Polimorfizam bez nasleđivanja (duck typing)

Python ne zahteva nasleđivanje da bi primenio polimorfizam.
Ako objekat ima metodu određenog imena, Python će je pozvati – bez obzira na tip.

```python
class Gitara:
    def sviraj(self):
        print("Gitara svira akorde.")

class Bubanj:
    def sviraj(self):
        print("Bubanj udara ritam.")

def nastup(instrument):
    instrument.sviraj()

nastup(Gitara())
nastup(Bubanj())
```

**Duck typing** → “Ako hoda kao patka i kvace kao patka, ponašamo se prema njemu kao prema patki.”

---

### 4️⃣ Apstraktne klase – obavezan interfejs

Ponekad želimo da **nateramo** sve child klase da implementiraju određene metode.
Za to koristimo **`abc` modul** i apstraktne klase.

```python
from abc import ABC, abstractmethod

class LoggerBase(ABC):
    @abstractmethod
    def log(self, poruka):
        pass

class ConsoleLogger(LoggerBase):
    def log(self, poruka):
        print(f"[Console] {poruka}")

class FileLogger(LoggerBase):
    def log(self, poruka):
        with open("log.txt", "a") as f:
            f.write(f"[File] {poruka}\n")

loggers = [ConsoleLogger(), FileLogger()]
for logger in loggers:
    logger.log("Ovo je test poruka.")
```

**Ključne tačke:**

- `class LoggerBase(ABC)` → nasleđuje od `ABC` (Abstract Base Class).
- `@abstractmethod` → mora biti implementiran u child klasi.
- Ne možeš napraviti objekat od apstraktne klase direktno.

---

### 5️⃣ Praktičan primer za tvoje projekte

Zamisli da praviš **formatters** module za logger.
Apstraktna klasa `FormatterBase` može zahtevati da svaka podklasa ima metod `format(poruka)`, ali implementacija zavisi od tipa formattera.

```python
from abc import ABC, abstractmethod

class FormatterBase(ABC):
    @abstractmethod
    def format(self, poruka):
        pass

class SimpleFormatter(FormatterBase):
    def format(self, poruka):
        return f"[SIMPLE] {poruka}"

class JSONFormatter(FormatterBase):
    def format(self, poruka):
        import json
        return json.dumps({"log": poruka})

formatters = [SimpleFormatter(), JSONFormatter()]
for f in formatters:
    print(f.format("Test poruka"))
```

---

### 6️⃣ Mikro-vežbe

1. Napravi apstraktnu klasu `Oblik` sa metodom `povrsina()`.
2. Napravi podklase `Pravougaonik` i `Krug` koje implementiraju `povrsina()`.
3. Kreiraj listu različitih oblika i izračunaj površinu za svaki.
4. Testiraj da vidiš da li Python odbija kreiranje objekta direktno iz `Oblik`.

---

### 🔑 Ključne tačke

- **Polimorfizam** omogućava da isti kod radi sa različitim tipovima objekata.
- **Duck typing** u Pythonu čini polimorfizam fleksibilnim.
- **Apstraktne klase** definišu obavezan interfejs koji child klase moraju da implementiraju.
- Kombinovanjem nasleđivanja, polimorfizma i apstraktnih klasa dobijaš osnovu za **čist, proširiv kod**.

---

📌 Ovime imaš kompletirana **prva tri stuba OOP-a**:

1. **Klase i objekti**
2. **Nasleđivanje**
3. **Polimorfizam + apstraktne klase**

---

OOP – Dan 1: Kickoff plan
1️⃣ Uvod: Šta je OOP?
Definicija klase i instance.

Razlika između objekta i varijable koja na njega pokazuje.

Kratko o 4 glavna principa OOP-a (samo imena, bez detalja sada):

Encapsulation

Abstraction

Inheritance

Polymorphism

2️⃣ Klasa i instanca – prvi primer
Pisanje minimalne klase sa **init** metodom.

Kreiranje dve instance iste klase i poređenje (id(), is, ==).

3️⃣ Atributi i metode
Razlika atribut (podatak) vs metod (funkcija koja pripada klasi).

Primer sa atributima i metodama koje manipulišu tim atributima.

4️⃣ Veza sa logger.py
Kako se logging.Logger kreira kao instanca klase Logger.

Zašto getLogger() uvek vraća istu instancu za isto ime (singleton logika).

5️⃣ Mini-vežbe
Napraviti klasu Car sa par atributa i metodom za ispis.

Napraviti dve instance i izmeniti podatke u jednoj da vidiš nezavisnost instanci.

Bonus: Napraviti klasu LoggerLite sa samo jednim atributom level.

---

Evo ti **OOP – Dan 1: Kickoff plan** u obliku radne lekcije koju možeš čitati i pratiti tokom dana, sa primerima koda i mini-vežbama.
Sve je u **Amateur modu** i prilagođeno našem šestomesečnom planu.

---

# 📚 OOP – Dan 1: Kickoff plan

### 1️⃣ Uvod: Šta je OOP?

### Definicija

- **OOP** (objektno-orijentisano programiranje) je pristup gde kod organizujemo u **klase** i **objekte**.
- **Klasa**: definicija strukture i ponašanja.
- **Instanca (objekat)**: konkretna realizacija klase.

---

### Objekat vs. varijabla koja na njega pokazuje

U Pythonu, promenljiva **ne sadrži objekat**, već referencu (adresu u memoriji) na objekat.

```python
class Test:
    pass

a = Test()
b = a  # b pokazuje na isti objekat kao a

print(id(a), id(b))  # isti ID = ista memorijska lokacija
print(a is b)        # True
```

---

### 4 glavna principa OOP-a (samo imena)

1. **Encapsulation**
2. **Abstraction**
3. **Inheritance**
4. **Polymorphism**

---

### 2️⃣ Klasa i instanca – prvi primer

```python
class Pozdrav:
    def __init__(self, ime):
        self.ime = ime

    def pozdravi(self):
        print(f"Zdravo, {self.ime}!")

p1 = Pozdrav("Milan")
p2 = Pozdrav("Ana")

print(id(p1), id(p2))
print(p1 is p2)       # False – različiti objekti
print(p1 == p2)       # False – po default-u == poredi po referenci

p1.pozdravi()
p2.pozdravi()
```

---

### 3️⃣ Atributi i metode

- **Atribut** – podatak vezan za objekat (npr. `self.ime`).
- **Metod** – funkcija definisana unutar klase, koja po pravilu ima `self` kao prvi argument.

```python
class Racun:
    def __init__(self, vlasnik, stanje):
        self.vlasnik = vlasnik
        self.stanje = stanje

    def uplata(self, iznos):
        self.stanje += iznos
        print(f"Uplaćeno: {iznos}, novo stanje: {self.stanje}")

    def isplata(self, iznos):
        if iznos <= self.stanje:
            self.stanje -= iznos
            print(f"Isplaćeno: {iznos}, novo stanje: {self.stanje}")
        else:
            print("Nedovoljno sredstava.")
```

---

### 4️⃣ Veza sa `logger.py`
> Napomena: U ovim primerima naglašavamo **kompozicija > nasleđivanje** (fleksibilnije testiranje i manja sprega).

U Python-ovom `logging` modulu:

- `logging.Logger` je **klasa**.
- Kada pozoveš `logging.getLogger("ime")`, dobijaš **instancu Logger-a**.
- Ako ponovo pozoveš sa istim imenom, dobijaš **istu instancu** (singleton obrazac) – ovo sprečava da se kreira više logger-a za isti kontekst.

```python
import logging

logger1 = logging.getLogger("app")
logger2 = logging.getLogger("app")

print(logger1 is logger2)  # True
```

---

### 5️⃣ Mini-vežbe

### Vežba 1 – `Car`

```python
class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def info(self):
        print(f"Auto: {self.marka} {self.model}")
```

- Kreiraj dve instance.
- Izmeni `model` u jednoj instanci.
- Proveri da druga ostaje nepromenjena.

---

### Vežba 2 – `LoggerLite`

```python
class LoggerLite:
    def __init__(self, level):
        self.level = level

    def log(self, msg):
        print(f"[{self.level}] {msg}")
```

- Testiraj sa različitim `level` vrednostima (`INFO`, `ERROR`).

---

📌 Ako hoćeš, mogu ti sutra odmah posle uvoda u **Day 2** dodati i **prvu pravu OOP verziju `LoggerLite`** koja piše u fajl i ima dinamičke levele – to će već biti mini-projekat.
Želiš da ti to pripremim kao nastavak?

---

Treba mi fokusirana OOP osnova za logger kontekst:

- klase, **init**, **repr** (za debug), i dataclass (imutabilnost kada ima smisla)
- kompozicija vs. nasleđivanje (zašto logger konfiguracija ≈ kompozicija)
- male jedinice odgovornosti (SRP) i dependency injection (npr. prosleđivanje Path-a)
- kako OOP odluke olakšavaju testiranje (pytest)
  Daj primere koji se mogu direktno preslikati na moj logger modul.

---

Odlično pitanje i odličan fokus. Ispod je **koncizan, ali dubinski** set primera za OOP odluke u kontekstu tvog `logger` modula. Sve je pisano tako da možeš direktno da iskoristiš i/ili proširiš.

---

# OOP osnove za logger: praktični vodič

### 1) Klase, `__init__`, `__repr__` i `@dataclass` (imutabilnost kad ima smisla)

**Kada koristiti šta**

- `__init__`: inicijalizuje stanje objekta (zavisnosti, obavezni parametri).
- `__repr__`: vraća **debug-friendly** string; fokus na bitne atribute i identitet.
- `@dataclass(frozen=True)`: odličan za **konfiguracije** i **vrednosne objekte** (immutability sprečava nenamerno menjanje).

```python
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Callable

# -------------- Vrednosni objekat: konfiguracija (immutabilna) --------------
@dataclass(frozen=True)
class LoggerConfig:
    name: str
    level: str  # npr. "DEBUG" | "INFO" | "ERROR"
    file_path: Path | None = None

# -------------- Protokoli (interfejsi) za kompoziciju --------------
class Formatter(Protocol):
    def format(self, level: str, msg: str) -> str: ...

class Sink(Protocol):
    def write(self, text: str) -> None: ...

# -------------- Konkretne implementacije --------------
class SimpleFormatter:
    def __init__(self, time_provider: Callable[[], str]):
        self._now = time_provider

    def format(self, level: str, msg: str) -> str:
        return f"{self._now()} [{level}] {msg}"

class ConsoleSink:
    def write(self, text: str) -> None:
        print(text)

class FileSink:
    def __init__(self, path: Path):
        self._path = path
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, text: str) -> None:
        self._path.write_text(
            (self._path.read_text() if self._path.exists() else "") + text + "\n",
            encoding="utf-8"
        )

# -------------- Logger orkestrira (komponuje) formatter + sink --------------
class Logger:
    _ORDER = {"DEBUG": 10, "INFO": 20, "ERROR": 40}

    def __init__(self, config: LoggerConfig, formatter: Formatter, sink: Sink):
        self._cfg = config
        self._fmt = formatter
        self._sink = sink

    def __repr__(self) -> str:
        # Debug-friendly: ime, nivo, gde piše (sink klasa) i file (ako ga ima)
        location = getattr(self._sink, "_path", None)
        return (f"Logger(name={self._cfg.name!r}, level={self._cfg.level!r}, "
                f"sink={self._sink.__class__.__name__}, file={str(location) if location else None})")

    # --- javne metode ---
    def debug(self, msg: str) -> None: self._log("DEBUG", msg)
    def info(self, msg: str)  -> None: self._log("INFO", msg)
    def error(self, msg: str) -> None: self._log("ERROR", msg)

    # --- privatno ---
    def _enabled(self, level: str) -> bool:
        return self._ORDER[level] >= self._ORDER[self._cfg.level]

    def _log(self, level: str, msg: str) -> None:
        if not self._enabled(level):
            return
        self._sink.write(self._fmt.format(level, f"{self._cfg.name}: {msg}"))

# -------------- Sastavljanje instanci (DI u praksi) --------------
def now_iso() -> str:
    from datetime import datetime
    return datetime.now().isoformat(timespec="seconds")

cfg = LoggerConfig(name="app", level="INFO", file_path=Path("logs/app.log"))
formatter = SimpleFormatter(time_provider=now_iso)
sink = FileSink(cfg.file_path) if cfg.file_path else ConsoleSink()
logger = Logger(cfg, formatter, sink)

# Debug ispis celog objekta:
# print(repr(logger))
```

**Zašto je ovo dobro:**

- `LoggerConfig` je _frozen_ → stabilna konfiguracija (ne menja se “u letu”).
- `__repr__` ti na debugu odmah kaže _ko je logger_ i _gde piše_.
- DI: Logger ne kreira sam zavisnosti — dobija ih **spolja** (formatter, sink, time provider).

---

### 2) Kompozicija vs. nasleđivanje (zašto je konfiguracija ≈ kompozicija)

**Česta greška**: praviti `FileLogger(Logger)` ili `DbLogger(Logger)` hijerarhiju.
**Bolje**: jedan `Logger` + ubacuješ različite **Sinks** i **Formatters** (kompozicija).

**Zašto kompozicija:**

- Manje krhko: menjaš deo (sink/formatter), ne celu hijerarhiju.
- Fleksibilno: isti logger danas piše u fajl, sutra u konzolu ili mrežu — bez subclass eksplozije.
- Testabilno: možeš ubrizgati “lažni” sink u testu.

**Antipattern (nasleđivanje):**

```python
# class FileLogger(Logger): ...  # brzo završiš sa ConsoleLogger, JsonFileLogger, RotatingFileLogger...
# Problem: naduvana hijerarhija i spajanje odgovornosti u baznoj klasi.
```

**Poenta**: Logger _orkestrira_ — ne _nasleđuje_.

---

### 3) SRP (Single Responsibility Principle) i Dependency Injection

**Male jedinice odgovornosti:**

- `Logger` – samo odlučuje _kada_ i _kako_ da pozove formatter/sink uz minimalnu logiku nivoa.
- `Formatter` – isključivo zadužen za pretvaranje poruke u tekstualni zapis.
- `Sink` – isključivo zadužen za krajnje odredište (fajl, konzola, mreža).
- `LoggerConfig` – nosi konfiguraciju (immutabilnu).

**Dependency Injection (DI):**

- Umesto da `Logger` **kreira** `FileSink(Path(...))`, _prosleđuješ_ gotov `Sink`.
- Umesto da `Formatter` sam zove `datetime.now()`, _prosleđuješ_ `time_provider`.
- Umesto da `FileSink` sam traži direktorijum, _prosleđuješ_ `Path`.

Time dobijaš:

- **Predvidljivo ponašanje**,
- **Jednostavne testove** (ubrizgaš “fake” varijante),
- \*_Laku zamenu_ delova bez menjanja koda logera.

---

### 4) Kako OOP odluke olakšavaju testiranje (pytest)

**Ciljevi u testu**:

- Bez I/O kada nije neophodno (ili ga kontrolišemo).
- Determinističko vreme (fake `time_provider`).
- Lako hvatanje izlaza (fake `Sink`).

### 4.1. Fake sink za test

```python
class MemorySink:
    def __init__(self):
        self.lines: list[str] = []

    def write(self, text: str) -> None:
        self.lines.append(text)
```

### 4.2. Test sa `pytest` (primer)

```python
# test_logger.py
from pathlib import Path
from dataclasses import dataclass

def fixed_time() -> str:
    return "2025-08-11T10:00:00"

def test_info_logs_when_level_allows(tmp_path):
    cfg = LoggerConfig(name="app", level="INFO", file_path=None)
    sink = MemorySink()
    fmt = SimpleFormatter(time_provider=fixed_time)
    log = Logger(cfg, fmt, sink)

    log.debug("hidden")      # ne sme proći (INFO > DEBUG)
    log.info("visible info")
    log.error("visible error")

    assert len(sink.lines) == 2
    assert sink.lines[0].endswith("app: visible info")
    assert sink.lines[1].endswith("app: visible error")

def test_file_sink_writes(tmp_path):
    log_path = tmp_path / "app.log"
    sink = FileSink(log_path)
    fmt = SimpleFormatter(time_provider=fixed_time)
    cfg = LoggerConfig(name="app", level="DEBUG", file_path=log_path)
    log = Logger(cfg, fmt, sink)

    log.debug("hello")
    assert "hello" in log_path.read_text(encoding="utf-8")

def test_repr_contains_key_fields():
    cfg = LoggerConfig(name="svc", level="ERROR")
    sink = ConsoleSink()
    fmt = SimpleFormatter(time_provider=lambda: "X")
    log = Logger(cfg, fmt, sink)
    r = repr(log)
    assert "svc" in r and "ERROR" in r and "ConsoleSink" in r
```

**Šta je testirano i zašto je lako:**

- Nema slučajnog I/O (osim kada **namerno** testiramo `FileSink`).
- Vreme je determinističko (fiksna funkcija).
- `repr` pomaže da _odmah_ vidiš suštinu instance.

---

### Kratka mapa odluka (za tvoj `logger`)
> Napomena: U ovim primerima naglašavamo **kompozicija > nasleđivanje** (fleksibilnije testiranje i manja sprega).

- **Konfiguracija**: `@dataclass(frozen=True)` → `LoggerConfig`.
- **Ulazi**: `Formatter`, `Sink`, `time_provider` (DI).
- **Logger**: drži minimalnu logiku nivoa + orkestraciju (SRP).
- **Kompozicija umesto nasleđivanja**: menjaš delove bez promena baze.
- **Testovi**: fake sink + fiksno vreme + `tmp_path` za file testove.

Ako želiš, mogu iz ovoga da ti izvedem:

- varijantu sa **JSON formatter-om**,
- **RotatingFileSink** (split po datumu/veličini),
- i kratku **factory** funkciju (npr. `build_logger(env_cfg: dict) -> Logger`) — sve ostaje u istim OOP okvirima i testabilno.

---

[OOP Foundations — start, Amateur mod]

Pravila rada:

- Objašnjavaj pojmove kao da ih prvi put vidim (Amateur mod).
- Daj najmanje moguće difove koda (ne celu skriptu).
- Posle svake izmene: napiši kratko “Zašto je ovo tačno”, i komandu pytest koju da pokrenem.
- Po završetku: preusmeri me u Terminology (3 nova pojma) i nazad u Junior Developer radi wrap-up-a.

---

1. Mini-zadatak 1 (Counter): otvoriti foundations_oop/src/counter.py i implementirati inc(), dec(), reset() + **repr**/**str** (jednostavno).
2. Testovi: kreirati nove testove u tests/ (možeš da se osloniš na ideje iz legacy_tests/test_foundations_oop/\*).
3. Mini-zadatak 2 (PathWalker): skica funkcije/klase za brojanje fajlova po ekstenziji (pathlib) + 1–2 testa.

Cilj dana (DoD): Counter minimalne operacije + novi testovi prolaze; PathWalker skica + bar 1 test.

---

Fenomenalno — idemo striktno po pravilima **Amateur moda**: mikro‑koraci, najmanji mogući difovi, kratko “zašto je ovo tačno”, i odmah pytest komanda.
Putanje koristim kako si definisao.

---

# 1) Mini‑zadatak 1 — `Counter`

### 1.1 Otvori `foundations_oop/src/counter.py` i ubaci minimalnu implementaciju

```diff
*** foundations_oop/src/counter.py
+from __future__ import annotations
+
+
+class Counter:
+    def __init__(self, start: int = 0) -> None:
+        self._value = int(start)
+
+    def inc(self, step: int = 1) -> int:
+        self._value += int(step)
+        return self._value
+
+    def dec(self, step: int = 1) -> int:
+        self._value -= int(step)
+        return self._value
+
+    def reset(self) -> None:
+        self._value = 0
+
+    def __repr__(self) -> str:
+        return f"Counter(value={self._value})"
+
+    def __str__(self) -> str:
+        return str(self._value)
```

**Zašto je ovo tačno (kratko):**

- `_value` je jedini izvor istine; `inc/dec` vraćaju **novu** vrednost posle promene (lakše za test).
- `reset()` vraća stanje na nulu bez povratne vrednosti (signal da je “akcija” izvršena).
- `__repr__` je debug‑friendly, `__str__` je “user‑friendly”.

**Pytest komanda (još nemamo testove, samo sanity check):**

```
pytest -q
```

---

### 1.2 Kreiraj testove za Counter: `tests/test_counter.py`

```diff
*** tests/test_counter.py
+from foundations_oop.src.counter import Counter
+
+
+def test_counter_inc_dec_and_reset():
+    c = Counter()
+    assert str(c) == "0"
+    assert c.inc() == 1
+    assert c.inc(2) == 3
+    assert c.dec() == 2
+    c.reset()
+    assert str(c) == "0"
+
+
+def test_counter_repr_is_debug_friendly():
+    c = Counter(5)
+    assert "Counter(value=5)" == repr(c)
```

**Zašto je ovo tačno (kratko):**

- Test pokriva osnovne operacije i očekivane povratne vrednosti.
- `repr` mora sadržati klasu i ključno stanje da bismo ga koristili u debugu/regresiji.

**Pytest komanda:**

```
pytest -q tests/test_counter.py
```

---

# 2) Mini‑zadatak 2 — `PathWalker` (skica) + 1–2 testa

> Fokus: **pathlib**, brojanje fajlova po ekstenziji. Pravila: case‑insensitive ekstenzije, tačka opciona (`"txt"` == `".txt"`). Ovo je skica minimalne odgovornosti (SRP).

### 2.1 Dodaj skicu u `foundations_oop/src/pathwalker.py`

```diff
*** foundations_oop/src/pathwalker.py
+from __future__ import annotations
+from pathlib import Path
+from collections import Counter as _Counter
+from typing import Dict
+
+
+class PathWalker:
+    """Broji fajlove po ekstenziji (case-insensitive)."""
+
+    def __init__(self, root: Path) -> None:
+        self._root = Path(root)
+
+    @staticmethod
+    def _norm_ext(ext: str) -> str:
+        ext = ext.lower()
+        return ext if ext.startswith(".") else f".{ext}"
+
+    def count_by_ext(self, ext: str) -> int:
+        """Vrati broj fajlova za jednu ekstenziju (npr. 'txt' ili '.txt')."""
+        target = self._norm_ext(ext)
+        return sum(1 for p in self._root.rglob("*") if p.is_file() and p.suffix.lower() == target)
+
+    def count_all(self) -> Dict[str, int]:
+        """Vrati mapu {'.ext': count} za sve nadjene fajlove."""
+        bag = _Counter()
+        for p in self._root.rglob("*"):
+            if p.is_file():
+                bag[p.suffix.lower()] += 1
+        return dict(bag)
```

**Zašto je ovo tačno (kratko):**

- SRP: klasa ima **jednu odgovornost** — prebrojavanje (bez I/O van čitanja strukture).
- Normalizacija ekstenzije rešava “`.TXT` vs `.txt` vs `txt`”.
- `rglob("*")` pretražuje rekurzivno; `suffix` je standardni API `pathlib.Path`.

**Pytest komanda (testove dodajemo odmah ispod):**

```
pytest -q tests/test_pathwalker.py
```

---

### 2.2 Testovi za PathWalker: `tests/test_pathwalker.py`

```diff
*** tests/test_pathwalker.py
+from pathlib import Path
+from foundations_oop.src.pathwalker import PathWalker
+
+
+def _touch(p: Path) -> None:
+    p.parent.mkdir(parents=True, exist_ok=True)
+    p.write_text("x", encoding="utf-8")
+
+
+def test_count_by_ext_is_case_insensitive(tmp_path):
+    _touch(tmp_path / "a.TXT")
+    _touch(tmp_path / "b.txt")
+    _touch(tmp_path / "sub" / "c.TxT")
+
+    pw = PathWalker(tmp_path)
+    assert pw.count_by_ext("txt") == 3
+    assert pw.count_by_ext(".TXT") == 3
+
+
+def test_count_all_returns_map_of_extensions(tmp_path):
+    _touch(tmp_path / "a.py")
+    _touch(tmp_path / "b.py")
+    _touch(tmp_path / "c.md")
+
+    pw = PathWalker(tmp_path)
+    counts = pw.count_all()
+    assert counts.get(".py", 0) == 2
+    assert counts.get(".md", 0) == 1
```

**Zašto je ovo tačno (kratko):**

- `tmp_path` izoluje testni fajl‑sistem; nema side‑effects.
- Proveravamo i **pojedinačnu** i **agregatnu** putanju (po ekstenziji i ukupno).

**Pytest komanda:**

```
pytest -q tests/test_pathwalker.py
```

---

# 3) BONUS — veza sa logger kontekstom (kompozicija, SRP, DI, testiranje)

Minimalni “hintovi” (bez kompletnog koda):

```diff
*** foundations_oop/src/logger_config.py
+from dataclasses import dataclass
+from pathlib import Path
+
+@dataclass(frozen=True)
+class LoggerConfig:
+    name: str
+    level: str
+    file_path: Path | None = None
```

```diff
*** foundations_oop/src/sinks.py
+from pathlib import Path
+
+class ConsoleSink:
+    def write(self, text: str) -> None:
+        print(text)
+
+class FileSink:
+    def __init__(self, path: Path) -> None:
+        self._path = path
+        self._path.parent.mkdir(parents=True, exist_ok=True)
+    def write(self, text: str) -> None:
+        self._path.write_text(
+            (self._path.read_text(encoding="utf-8") if self._path.exists() else "") + text + "\n",
+            encoding="utf-8"
+        )
```

```diff
*** foundations_oop/src/formatters.py
+from typing import Callable
+
+class SimpleFormatter:
+    def __init__(self, now: Callable[[], str]) -> None:
+        self._now = now
+    def format(self, level: str, msg: str) -> str:
+        return f"{self._now()} [{level}] {msg}"
```

```diff
*** foundations_oop/src/logger.py
+from foundations_oop.src.logger_config import LoggerConfig
+
+class Logger:
+    _ORDER = {"DEBUG": 10, "INFO": 20, "ERROR": 40}
+    def __init__(self, cfg: LoggerConfig, formatter, sink) -> None:
+        self._cfg, self._fmt, self._sink = cfg, formatter, sink
+    def __repr__(self) -> str:
+        dest = getattr(self._sink, "_path", None)
+        return f"Logger(name={self._cfg.name!r}, level={self._cfg.level!r}, sink={self._sink.__class__.__name__}, file={str(dest) if dest else None})"
+    def _enabled(self, level: str) -> bool:
+        return self._ORDER[level] >= self._ORDER[self._cfg.level]
+    def _log(self, level: str, msg: str) -> None:
+        if self._enabled(level):
+            self._sink.write(self._fmt.format(level, f"{self._cfg.name}: {msg}"))
+    def info(self, msg: str) -> None: self._log("INFO", msg)
+    def error(self, msg: str) -> None: self._log("ERROR", msg)
```

**Zašto je ovo tačno (kratko):**

- **Kompozicija** (formatter + sink) → nema eksplozije podklasa.
- **SRP**: svako ima minimalnu odgovornost.
- **DI**: sve zavisnosti su ubrizgane → testovi su trivijalni (fake sink, fiksno vreme).

**Pytest komanda (primer fokus testa):**

```
pytest -q tests/test_counter.py tests/test_pathwalker.py
```

> (Za logger testove koristi isti princip kao kod `MemorySink` iz prethodne poruke; drži I/O pod kontrolom.)

---

### ✅ Definition of Done (DoD) za današnji cilj

- `Counter`: minimalne operacije + repr/str testirani i prolaze.
- `PathWalker`: skica sa `count_by_ext` i `count_all` + bar 1 test prolazi.

---

### ➡️ Terminology (dodaj u tvoj Terminology Cheatsheet)

1. **SRP (Single Responsibility Principle)** – svaka klasa ima _jednu_ odgovornost; lakše menjanje i testiranje.
2. **Dependency Injection (DI)** – zavisnosti (npr. `Path`, `formatter`, `sink`, `now()`) se prosleđuju spolja; kod je predvidljiv i testabilan.
3. **`__repr__` vs `__str__`** – `__repr__` za debug (nedvosmislen prikaz stanja), `__str__` za user‑friendly ispis.

---

### 🔁 Povratak u “Junior Developer” wrap‑up

- Napravi branch `feat/oop-foundations-day1`.
- Dodaj/izvrši gore navedene difove i testove.
- Pokreni:

  ```
  pytest -q
  ```

- Commit poruke (primeri):

  - `feat(counter): implement inc/dec/reset and add repr/str`
  - `test(counter): cover operations and debug repr`
  - `feat(pathwalker): add sketch for count_by_ext/count_all`
  - `test(pathwalker): case-insensitive ext counting`

Kada sve prođe, otvori PR i napiši kratak opis šta je urađeno i šta sutra planiraš (Enkapsulacija + `__str__/__repr__` fine‑tuning + prvi logger test sa fake sink‑om).

---

Odlično — ulazim u **Amateur mod** i držim se tvog repo-konteksta. Krenuću kratko od ideje (OOP pogled), pa **linija-po-linija** objašnjenja za `logger.py`, i posebno ću rastumačiti **anotacije** (uključujući `from __future__ import annotations`). Na kraju dobijaš mini-zadatak i brzu pytest proveru.

---

# Šta `logger.py` radi (OOP pogled)

- Modul je **mala fabrika** za kreiranje/konfigurisanje logger-a po imenu. U OOP smislu, to je “konstruktorska” funkcija koja vraća objekat klase `logging.Logger`, ali uz **invarijante**: tačno **jedan** `StreamHandler`, standardni `Formatter`, i **idempotentnost** (ponovni poziv ne duplira hendler). Ova pravila su “zaključana” u tvojim materijalima i testovima. &#x20;
- Konstante `DEFAULT_FMT` i `DEFAULT_DATEFMT` centralizuju format i datum – formatter se pravi iz jedne funkcije i testovi proveravaju baš te vrednosti. &#x20;

---

# Linija-po-linija: `src/logger.py` (trenutni inkrement)

> Napomena: ne lepim ceo fajl — pokazujem minimalne isečke, pa objašnjenje “kao prvi put”.

### 1) Hejder i importi

```py
from __future__ import annotations
import logging
from pathlib import Path
from typing import Optional, Union
```

**Šta znači:**

- `from __future__ import annotations` odlaže evaluaciju anotacija — one se čuvaju kao **stringovi** i po potrebi se razrešavaju npr. preko `typing.get_type_hints`. To olakšava “forward reference” i smanjuje rizik cikličnih importa. **Baš tako je predloženo za ceo tvoj `src/`**. &#x20;
- `Path` je već pripremljen za sledeći inkrement (dodavanje `FileHandler`), ali u ovom koraku je samo “parkiran”. To je u skladu s dnevnim planom/DoD.&#x20;

**Zašto je ovo tačno (mini-logika):** odložene anotacije = manji coupling pri importu; kod se i dalje tip-čekuje u alatima, a runtime ostaje jednostavan.&#x20;

---

### 2) Konstante formata

```py
DEFAULT_FMT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
DEFAULT_DATEFMT = "%Y-%m-%d %H:%M:%S"
```

**Šta znači:** Jedno mesto istine za formatiranje poruke i vremena; testovi očekuju baš ove vrednosti na postojećem `StreamHandler`-u.&#x20;

**Zašto je ovo tačno:** centralizacija formata → lakše održavanje; u “Line Explainer” vodiču formatter se pravi iz fabričke funkcije sa istim konstantama.&#x20;

---

### 3) Normalizacija nivoa: `_coerce_level(...) -> int`

```py
def _coerce_level(level: Optional[Union[int, str]],
                  fallback: int = logging.INFO) -> int:
    ...
```

**Šta znači:** Helper prima `int` ili `"INFO"`/`"DEBUG"`… i vraća **int** nivo (`logging.INFO`, `logging.DEBUG` itd.). Za nepoznat string treba da digne `ValueError` — to je i predmet testa.&#x20;

**Zašto je ovo tačno:** test „invalid level” upravo to traži; vodiči naglašavaju jasne greške umesto tihog „kastovanja“. &#x20;

---

### 4) Osiguranje jednog `StreamHandler`-a

U fajlu se poziva:

```py
_ensure_stream_handler(lg)
```

**Šta znači:** Funkcija prolazi kroz `logger.handlers`; ako već postoji odgovarajući **konzolni** handler, **samo** mu osigura pravilan `Formatter`. Ako ne postoji, doda tačno **jedan** novi `StreamHandler` i namesti formatter na `DEFAULT_*`.&#x20;

**Zašto je ovo tačno:** time se obezbeđuje **idempotentnost** — ponovni poziv fabrike za isto ime ne duplira hendler, što takođe proveravaju testovi.&#x20;

---

### 5) Sama “fabrika”: `get_logger(...) -> logging.Logger`
> Napomena: U ovim primerima naglašavamo **kompozicija > nasleđivanje** (fleksibilnije testiranje i manja sprega).

```py
def get_logger(
    name: str,
    level: Union[int, str] = "INFO",
    log_file: Optional[Path] = None,
) -> logging.Logger:
    lg = logging.getLogger(name)
    lg.setLevel(_coerce_level(level))
    lg.propagate = False
    _ensure_stream_handler(lg)
    return lg
```

**Parametri (zašto baš ovako):**

- `name: str` — ključ za **istog** `Logger` objekta između poziva; `logging.getLogger(name)` vraća istu instancu pod tim imenom → lakše deljenje konfiguracije. (Tu invarijantu oslanjaš na testove “isti logger, bez duplih handlera”.)&#x20;
- `level: Union[int, str]="INFO"` — **stabilan API** i za ljude (“INFO”) i za program (“20”); `_coerce_level` obezbeđuje validaciju.&#x20;
- `log_file: Optional[Path]=None` — rezervisano za sledeći inkrement (dodavanje `FileHandler` sa `utf-8`). Dizajnerski, to je **kompozicija** (logger + handleri), ne nasleđivanje.&#x20;

**Telo (ključne odluke):**

- `lg.setLevel(...)` — postavlja ugovoreni nivo.
- `lg.propagate = False` — sprečava dupli ispis preko root loggera (česta početnička zamka).&#x20;
- `_ensure_stream_handler(lg)` — vidi tačku 4; čuva **jedan** `StreamHandler` sa našim `DEFAULT_*`.&#x20;

**Zašto je ovo tačno:** sve ovo je direktno povezano sa DoD/tetsovima: 1 handler, standardni format, INFO kao podrazumevani nivo, idempotentnost.&#x20;

---

### Anotacije (tip-hintovi) — “kao prvi put”

- **Gde ih vidiš:** u potpisima funkcija (`name: str`, `level: Union[int, str]`, `-> logging.Logger`) i parametara.

- **Šta znače:** signaliziraju očekivane tipove _statističkim_ alatima (IDE, linters, mypy), a u runtime-u su **meta-podatak**, ne proveravaju se automatski.

- **Zašto `from __future__ import annotations`:** čuva anotacije kao **stringove** do trenutka kada su potrebne; time:

  1. radi **forward reference** bez navodnika,
  2. smanjuje rizik od cikličnih importa,
  3. čini potpis čistijim. &#x20;

- **Kako to pomaže u OOP dizajnu loggera:** čitljiviji ugovori funkcija, lakše refaktorisanje (npr. izdvajanje tip-aliasa), manje “import buke” i jasnija izolacija odgovornosti (SRP). Tvoj “Learning Boost” upravo to preporučuje za ceo `src/`.&#x20;

---

### Povezivanje sa testovima (brzi sanity)

- Test 1 očekuje: **INFO** nivo, tačno **1** `StreamHandler`, i da je formatter postavljen na `DEFAULT_FMT/DEFAULT_DATEFMT`.&#x20;
- Test 2 očekuje: **idempotentnost** (isti logger, bez duplih handlera).&#x20;

**Pokreni:**

```bash
pytest -q -k "logger and (api_defaults or idempotent)"
```

---

### Mini-zadaci (5–7 min)

1. **Introspekcija anotacija:** u REPL-u uključi `from typing import get_type_hints` pa `get_type_hints(get_logger)` — videćeš da se string-anotacije razrešavaju u stvarne tipove (zahvaljujući future-annotations konceptu). (Objašnjenje koncepta: )
2. **Namerno pokvari formatter** na postojećem `StreamHandler`-u i ponovo pozovi `get_logger(...)` — `_ensure_stream_handler` treba da ga vrati na `DEFAULT_*`. (Vodič “Line Explainer” opisuje tu zaštitu.)&#x20;

---

### Kratko “zašto je sve ovo OOP-tačno”

- **SRP (jedna odgovornost):** `get_logger` orkestrira konfiguraciju, a pomoćne funkcije obavljaju mikro-zadate (nivelacija, formatter, handler).&#x20;
- **Kompozicija, ne nasleđivanje:** logger sastavljamo iz handlera/formatter-a (dodavanjem komponenti), što je prirodni model u `logging` ekosistemu. Plan sledećeg inkrementa (`FileHandler`) je isto kompozicija.&#x20;
- **Idempotentnost kao invarijanta API-ja:** višestruki pozivi ne menjaju broj handlera; to je temelj testova i sprečava “dupli ispis”.&#x20;

---

### Handoff (po tvom toku)

- **Terminology Cheatsheet (3 pojma danas):** _idempotent_, _StreamHandler_, _Formatter/datefmt_ (spremno u dnevnim beleškama).&#x20;
- **Nazad u Junior Developer**: upiši wrap-up i “sutra: FileHandler + validacija nivoa preko CLI”, kako je već predviđeno.&#x20;

Ako želiš, sledeći put možemo da dopunimo liniju-po-liniju baš za `_coerce_level`, `_make_formatter` i `_ensure_stream_handler` uz mikro-testove iz “Line Explainer” vodiča (tu su već gotovi zadaci i rešenja). &#x20;

---

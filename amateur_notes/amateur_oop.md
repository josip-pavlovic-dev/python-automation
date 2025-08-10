Razumem — želiš **30 minuta fokusiranog materijala** na srpskoj latinici, koji ide u dubinu i sa što više primera, tako da ti ostane čvrsta osnova bez koje nijedan junior programer ne može reći da zna OOP.
Pripremiću ti **celu lekciju 1** u **Amateur modu**, ali proširenu:

- biće puno primera, objašnjenja korak-po-korak, analogija i mikro-vežbi,
- ići ćemo od najosnovnijeg do nivoa na kojem već možeš da povezuješ sa budućim projektima (logger, formatter moduli).

---

# 📚 OOP Foundations – Lekcija 1

**Tema:** Šta je klasa i kako se iz nje pravi objekat?
**Cilj:** Razumeti osnovu OOP-a u Pythonu i biti sposoban da samostalno definišeš klase i kreiraš objekte.

---

## 1️⃣ Zašto uopšte OOP?

U proceduralnom programiranju (ono što si radio do sada), imaš:

- promenljive (podatke)
- funkcije (operacije nad tim podacima)

Problem: kod brzo postaje **rasut**, teško ga je održavati i ponovo koristiti.

**OOP (Objektno-Orijentisano Programiranje)** omogućava da podatke i funkcije **spakujemo u jednu celinu** – objekat.
Taj objekat ima svoje **atribute** (podatke) i **metode** (funkcije), i ponaša se kao **“mali program”** unutar većeg sistema.

💡 **Primer iz prakse:**
Zamišljaj Python skriptu kao gradilište. U proceduralnom pristupu, svi radnici i alat su pomešani u jednom velikom skladištu. U OOP-u, svaki “tim” (klasa) ima svoj prostor, alat i pravila rada.

---

## 2️⃣ Klasa – plan, šablon, nacrt

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

## 3️⃣ Objekat – konkretna instanca

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

## 4️⃣ Više primera iz realnog sveta

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

## 5️⃣ Analizirajmo `self` – ključ OOP-a u Pythonu

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

## 6️⃣ Instance atributi vs. Class atributi

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

## 7️⃣ Metode – ponašanje objekata

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

## 8️⃣ Mikro-vežbe (uradi odmah)

1. Napravi klasu `Knjiga` sa atributima `naslov` i `autor` i metodom `prikazi_info`.
2. Napravi dva objekta i pozovi metod na oba.
3. Dodaj **class atribut** `biblioteka = "Gradska biblioteka"`.
4. Napravi **static metodu** `broj_stranica_u_satu(br_strana, sati)` koja vraća rezultat `br_strana * sati`.

---

## 9️⃣ Povezivanje sa tvojim projektima

- Logger može biti **osnovna klasa** koju kasnije nasleđuju `FileLogger`, `ConsoleLogger`, `FormatterLogger`.
- Formatter moduli mogu biti posebne klase koje logger koristi (kompozicija).
- Umesto da funkcije stoje razbacane po fajlu, biće **organizovane** unutar odgovarajućih klasa.

---

## 🔑 Ključne tačke za pamćenje

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

## 1️⃣ Šta je nasleđivanje?

**Definicija:**
Nasleđivanje je mehanizam u OOP-u koji omogućava da jedna klasa (**child** ili **subclass**) preuzme osobine i ponašanje druge klase (**parent** ili **superclass**).

💡 Prednost:

- **Ponovna upotreba koda** – pišemo ga jednom, koristimo više puta.
- **Proširivanje funkcionalnosti** bez menjanja originalne klase.

**Analogy:**
Ako imaš osnovni plan “vozilo” (sa brzinom, bojom, brojem točkova), iz njega možeš praviti specijalizovane planove za auto, motor, kamion – svi nasleđuju osnovne osobine, ali dodaju svoje.

---

## 2️⃣ Osnovni primer

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

## 3️⃣ Overriding metoda (prepisivanje ponašanja)

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

## 4️⃣ Dodavanje novih metoda u child klasu

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

## 5️⃣ Višestruko nasleđivanje

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

## 6️⃣ Praktičan primer za tvoje projekte – Logger hijerarhija

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

## 7️⃣ Mikro-vežbe

1. Napravi klasu `Osoba` sa atributima `ime` i `prezime` i metodom `predstavi_se()`.
2. Napravi child klasu `Zaposleni` koja ima i `pozicija` i metod `prikazi_posao()`.
3. Dodaj metodu u child klasu koja prepisuje `predstavi_se()` tako da ispisuje i poziciju.
4. Testiraj sa nekoliko primera.

---

## 8️⃣ Gde greše početnici?

- Zaborave da pozovu `super().__init__()` pa izgube inicijalizaciju parent klase.
- Prepisuju metode kad to nije potrebno.
- Previše duboko prave hijerarhiju (teško za održavanje).
- Mešaju instance i class atribute u nasleđivanju.

---

## 🔑 Ključne tačke

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

## 1️⃣ Šta je polimorfizam?

**Definicija:**
Polimorfizam znači **“više oblika”** – sposobnost različitih objekata da odgovore na isti poziv metode na svoj način.

💡 Primer iz života:
Ako različiti muzički instrumenti imaju metod `sviraj()`, violina, gitara i bubanj će ga izvesti potpuno drugačije, ali kod koji ih koristi ne mora da zna detalje.

---

## 2️⃣ Polimorfizam kroz nasleđivanje

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

## 3️⃣ Polimorfizam bez nasleđivanja (duck typing)

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

## 4️⃣ Apstraktne klase – obavezan interfejs

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

## 5️⃣ Praktičan primer za tvoje projekte

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

## 6️⃣ Mikro-vežbe

1. Napravi apstraktnu klasu `Oblik` sa metodom `povrsina()`.
2. Napravi podklase `Pravougaonik` i `Krug` koje implementiraju `povrsina()`.
3. Kreiraj listu različitih oblika i izračunaj površinu za svaki.
4. Testiraj da vidiš da li Python odbija kreiranje objekta direktno iz `Oblik`.

---

## 🔑 Ključne tačke

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

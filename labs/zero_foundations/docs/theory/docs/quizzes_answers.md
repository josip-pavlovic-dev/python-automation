# Odgovori na kviz pitanja


## L01

1. Uvlaka (indentation) posle dvotačke `:`.
2. `0`, `''`, `[]` (i još: `{}`, `set()`, `None`).
3. `snake_case`.
4. `None` je posebna vrednost koja označava „nema vrednosti“, dok je `''` prazna niska (string).

## L02

1. Dodaje indeks uz svaku vrednost tokom iteracije.
2. Koristi `for i in range(10):`.
3. `break` prekida petlju; `continue` preskače ostatak trenutne iteracije i nastavlja.

## L03

1. Parametar je ime u definiciji funkcije; argument je konkretna vrednost pri pozivu.
2. Zato što se dele između poziva — evaluiraju se jednom pri definiciji.
3. Da dokumentuje namenu, parametre i povratnu vrednost funkcije.

## L04

1. Lista je mutable; torka je immutable.
2. Uklanjanje duplikata i test pripadnosti bez poretka.
3. Vraća podlistu `[1,2,3]` (desna granica ekskluzivna).

## L05

1. Izoluje zavisnosti projekta.
2. Po prisustvu `__init__.py` (u klasičnom modelu paketa).
3. Da razlikujemo pokretanje kao skripta od importovanja kao modula.

## L06

1. Automatski zatvara fajl i čuva resurse čak i kod izuzetaka.
2. Proveravaju da li je putanja fajl ili direktorijum.
3. Da bismo izbegli probleme sa podrazumevanim enkodingom i znakovima.

## L07

1. Prvi hvata samo `ValueError`; drugi hvata praktično sve izuzetke (preširoko).
2. Blok koji se uvek izvrši (čistka resursa).
3. Klik na marginu uz liniju koda (ili F9), pa `Start Debugging`.

## L08

1. DEBUG, INFO, WARNING, ERROR, CRITICAL.
2. Proveriti `if not logger.handlers:` pre dodavanja; ili ukloniti postojeće pre ponovnog dodavanja.
3. Zaustavlja prosleđivanje log poruka roditeljskim logger-ima.

## L09

1. Referenca na konkretnu instancu preko koje pristupaš atributima/metodama.
2. `__repr__` — nedvosmislen prikaz za developera; `__str__` — lepši, korisnički prikaz.
3. 0.0 (ili neku definisanu vrednost dok nema obe vremenske tačke).

## L10

1. Manje sprega, veća fleksibilnost i lakše testiranje.
2. Automatski `__init__`, `__repr__`, `__eq__` (i drugo po potrebi).
3. Prosledi fabričku funkciju/objekat u konstruktor umesto da ga gradiš unutra.

## L11

1. Pozicioni je obavezan i identifikovan redosledom; opcioni ima prefiks `--` i najčešće podrazumevanu vrednost.
2. `action="store_true"` (prisustvo flaga postavlja `True`).
3. Uspešan završetak programa.

## L12

1. Početak i kraj stringa (reda).
2. Da ne moramo duplo da bekslash-ujemo karaktere (lakše pisanje).
3. `+`, `*`, `{m,n}` su primeri kvantifikatora.

## L13

1. Da `csv` modul ispravno upravlja novim redovima na Windows-u.
2. `ensure_ascii=False` i `encoding="utf-8"`.
3. Upisuje zaglavlje sa imenima kolona u CSV.

## L14

1. Prema obrascima imena `test_*.py` i `test_*` funkcijama/klasama.
2. `tmp_path` daje privremenu radnu putanju; `caplog` hvata log zapise.
3. Pokreće isti test više puta sa različitim skupovima podataka.

## L15

1. Da se poziv ne blokira neograničeno u slučaju mrežnog problema.
2. Pozivom `response.json()`.
3. Korišćenjem `raise_for_status()` i `try/except` oko mrežnog poziva.

## L16

1. Pokreće modul kao skriptu (respektuje import puteve paketa).
2. Task Scheduler je Windows alat; cron je Linux/Unix mehanizam.
3. Da bi se kasnije mogla dijagnostikovati greška i pratiti istorija izvršavanja.
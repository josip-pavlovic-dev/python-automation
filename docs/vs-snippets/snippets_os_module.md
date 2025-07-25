# 🧠 os module - test log & notes

## ✅ Summary

Interaktivno testiranje funkcija `os` i `os.path` modula kroz `snippets_os.py`.

---

## 🧪 Ispitane funkcije

### 1. `os.getcwd()`

Vraca trenutni radni direktorijum.

### 2. `os.listdir()`

Lista sve fajlove i foldere u trenutnom direktorijumu.

### 3. `os.mkdir()`

Kreira folder ako ne postoji.

### 4. `os.rename()`

Menja ime foldera ili fajla.

### 5. `os.path.isdir()` i `os.path.isfile()`

Proverava da li je data putanja folder ili fajl.

### 6. `os.path.abspath()`

Vraca apsolutnu putanju fajla.

### 7. `os.path.split()`

Razdvaja putanju na folder i fajl.

### 8. `os.path.join()`

Bezbedno spaja delove putanje.

### 9. `os.environ['PATH']`

Vraca sistemsku promenljivu PATH.

### 10. `os.path.getsize()`

Vraca velicinu fajla u bajtovima.

---

## 💡 Napomene

- Ako folder vec postoji, `os.mkdir()` ce baciti `FileExistsError`.
- `os.environ` se ponasa kao rečnik (`dict`).
- Ova skripta je idealna za razumevanje putanja, radnog direktorijuma i sistemskih funkcija.

---

## 🗂️ Lokacija

Smešteno u `docs/vs-snippets/`

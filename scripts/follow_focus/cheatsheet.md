# 🧠 Cheatsheet: `follow_focus.ahk`  
_Advanced AHK script for intelligent cursor focus across windows_  
_Cheatsheet za pametno pomeranje kursora pomoću AutoHotkey_

---

## 📌 Explanation: | _Objašnjenje:_

| Line | Code | _Objašnjenje_ |
|------|------|----------------|
| 1 | `#Persistent` | Keeps the script running in background. | _Drži skriptu aktivnom u pozadini._ |
| 2 | `#SingleInstance force` | Prevents duplicate script instances. | _Onemogućava pokretanje više instanci skripte._ |
| 3 | `SetTimer, CheckFocus, 100` | Calls `CheckFocus` every 100ms. | _Poziva funkciju `CheckFocus` na svakih 100 milisekundi._ |
| 4 | `return` | Ends auto-execute section. | _Zatvara deo koji se izvršava automatski pri startu._ |

---

## 🔁 Function: `CheckFocus` | _Funkcija koja prati promenu prozora_

```ahk
CheckFocus:
    WinGet, id, ID, A
    if (id != lastWin)
    {
        lastWin := id
        WinGetPos, X, Y, W, H, ahk_id %id%
        MouseMove, X + (W // 2), Y + (H // 2), 0
    }
return
````

### 📌 Explanation: | *Objašnjenje:*

| Code                                       | *Objašnjenje*                                           |                                                                     |
| ------------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------- |
| `WinGet, id, ID, A`                        | Gets the window ID of the currently active window.      | *Dobija ID trenutno aktivnog prozora.*                              |
| `if (id != lastWin)`                       | Proverava da li se promenio fokusirani prozor.          | *Ako je novi prozor drugačiji od prethodnog...*                     |
| `lastWin := id`                            | Ažurira ID trenutno aktivnog prozora.                   | *Pamti novi prozor kao trenutno fokusirani.*                        |
| `WinGetPos, X, Y, W, H, ahk_id %id%`       | Dobija poziciju i veličinu aktivnog prozora.            | *X i Y su koordinate gornjeg levog ugla; W i H su širina i visina.* |
| `MouseMove, X + (W // 2), Y + (H // 2), 0` | Pomera miš u **centar prozora** trenutno aktivnog taba. | *Računa centar i odmah premesti miš bez animacije (`0`).*           |

---

## 📦 Variables | *Promenljive u skripti*

| Name      | Purpose                            | *Opis*                                  |
| --------- | ---------------------------------- | --------------------------------------- |
| `id`      | ID currently focused window        | *Trenutni aktivni prozor*               |
| `lastWin` | Stores previously active window ID | *Pamti prethodni fokus za poređenje*    |
| `X, Y`    | Position of top-left corner        | *Koordinata gornjeg levog ugla prozora* |
| `W, H`    | Width and height of window         | *Dimenzije prozora u pikselima*         |

---

## 💡 Tips | *Saveti za korišćenje*

* Ako primetiš kašnjenje, smanji interval `SetTimer` (npr. `50ms`)
* Ako koristiš više monitora sa različitim rezolucijama, proveri da `MouseMove` ne ide van ekrana
* Ako koristiš kompajlirani `.exe`, možeš ga lako dodati u `shell:startup`

---

## ✏️ Customization | *Prilagođavanje ponašanja*

| Želiš...                                                 | Izmena u kodu                                 |
| -------------------------------------------------------- | --------------------------------------------- |
| ...da miš ide u **donji desni ugao** prozora?            | `MouseMove, X + W - 10, Y + H - 10, 0`        |
| ...da koristi **poslednju poziciju kursora** po prozoru? | Dodaj mapiranje ID → pozicija (napredno)      |
| ...da se miš ne pomera ako je prozor fullscreen?         | Dodaj `WinGet, Style...` i proveru `0xC40000` |

---

## 🧭 Author | *Autor*

* 👨‍💻 Josip Pavlović
* 🌐 [GitHub](https://github.com/josip-pavlovic-dev)
* 🎯 Aspiring Python Developer from Novi Sad
* 🔗 [LinkedIn](https://www.linkedin.com/in/josip-p-151951338/)

---

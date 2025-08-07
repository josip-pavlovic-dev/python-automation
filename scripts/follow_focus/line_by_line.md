# 📌 Line-by-line explanation | _Objašnjenje liniju po liniju_

```
#Requires AutoHotkey v2.0
```

Specifies that the script must use AutoHotkey v2.0. | _Definiše da skripta koristi AutoHotkey verziju 2.0._

```
Persistent
```

Keeps the script running in the background. | _Drži skriptu aktivnom u pozadini._

```
SetTimer, CheckWindowFocus, 50
```

Calls the function `CheckWindowFocus` every 50 milliseconds. | _Poziva funkciju `CheckWindowFocus` svakih 50 milisekundi._

```
global lastWinID := 0
```

Stores the ID of the last active window. | _Pamti ID poslednjeg aktivnog prozora._

```
global cursorMemory := Map()
```

Creates a dictionary (`Map`) to store cursor positions by window ID. | _Kreira mapu za pamćenje pozicija kursora po ID-u prozora._

---

### 🔄 `CheckWindowFocus` funkcija

```
CheckWindowFocus() {
    static prevWinID := 0
```

Defines a static variable that retains value between function calls. | _Definiše statičku promenljivu koja zadržava vrednost između poziva funkcije._

```
    thisWinID := WinActive("A")
```

Gets the currently active window ID. | _Dobija ID trenutno aktivnog prozora._

```
    if (thisWinID != prevWinID) {
```

Checks if the active window has changed. | _Proverava da li se aktivni prozor promenio._

```
        if (cursorMemory.Has(thisWinID)) {
            coords := cursorMemory[thisWinID]
            MouseMove(coords.x, coords.y, 0)
        }
```

If there is stored cursor position for the new window, move the mouse there. | _Ako postoji pozicija za novi prozor, pomeri miš tamo._

```
        MouseGetPos(&x, &y)
        cursorMemory[prevWinID] := { x: x, y: y }
```

Stores current cursor position for the previous window. | _Pamti trenutnu poziciju miša za prethodni prozor._

```
        prevWinID := thisWinID
    }
}
```

Updates the stored window ID for next iteration. | _Ažurira ID prozora za narednu proveru._

---

## ✅ Behavior Summary | _Opis ponašanja_

- Detektuje kada promeniš aktivni prozor (tab)
- Ako si već bio u tom prozoru ranije, vratiće kursor na mesto gde si poslednji put kliknuo
- Radi sa više monitora
- Izbegava centriranje koje je davalo loše rezultate na eksternom TV-u

---

## 🛠️ Podešavanja i preporuke | _Settings & Recommendations_

- 🖥️ _Radi idealno kada su monitore podešeni sa pravim razmerama i orijentacijom (npr. 1920x1080)._
- 🔁 _Interval od 50ms je brz ali ne agresivan – može se prilagoditi ako želiš veću efikasnost._
- 🪟 _Ne reaguje na prozore bez fokusa (minimizovani itd.)._

---

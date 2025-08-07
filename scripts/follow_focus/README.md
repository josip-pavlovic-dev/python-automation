# 🎯 follow_focus.ahk

![Automation](https://img.shields.io/badge/type-AHK%20Script-blue)
![Category](https://img.shields.io/badge/category-Productivity-lightgrey)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

> Automatically moves the mouse pointer to the active window when switching tabs (`Alt + Tab`), maintaining natural flow across dual-monitor setups.

> _Automatski pomera kursor miša ka aktivnom prozoru pri promeni taba (`Alt + Tab`) – korisno za rad sa više ekrana._

---

## ✅ Features | _Karakteristike_

- Moves the mouse cursor to the **center of the currently active window**
- Ignores taskbars and screen edges
- **Remembers last mouse position per window**, restoring it upon return
- Optimized for **dual-monitor setups** (e.g. laptop + TV)
- Lightning fast response time (reaction delay reduced)

---

## 🖥️ Use Case | _Kada koristiti ovu skriptu_

- Kod rada sa više monitora, kada VS Code, browser i terminal rade na različitim ekranima
- Pri čestom korišćenju `Alt + Tab` za prebacivanje fokusa
- Kada miš ostaje na pogrešnom ekranu i prekida tok rada

---

## ⚙️ Requirements | _Zahtevi_

- [AutoHotkey v1.1+](https://www.autohotkey.com/) (tested on v1.1.36.02)
- Windows 10 / 11
- Dual-monitor setup (laptop + eksterni ekran – npr. TV)

---

## 🚀 How to Use | _Kako pokrenuti skriptu_

1. Kopiraj fajl `follow_focus.ahk` u željeni folder (npr. `scripts/follow_focus/`)
2. Desni klik na fajl → **Compile Script** _(ili direktno pokreni ako imaš AHK instaliran)_
3. (Opcionalno) Dodaj prečicu `.lnk` u `shell:startup` folder:
   - `Win + R` → upiši `shell:startup`
   - Nalepi prečicu do `follow_focus.ahk`
   - Tako se skripta automatski pokreće pri startovanju sistema

---

## 🧪 Behavior | _Kako funkcioniše_

- Kada pritisneš `Alt + Tab`, skripta:
  - registruje novi prozor u fokusu
  - izračuna njegov centar (ili pamti prethodnu poziciju kursora)
  - pomeri miš u sredinu ili prethodnu tačku
- Reakcija je **trenutna** i **ne zavisi od taskbara**

---

## 🧭 Author | _Autor_

- 👨‍💻 Josip Pavlović
- 🌐 [GitHub](https://github.com/josip-pavlovic-dev)
- 🎯 Aspiring Python Developer from Novi Sad
- 🔗 [LinkedIn](https://www.linkedin.com/in/josip-p-151951338/)

---

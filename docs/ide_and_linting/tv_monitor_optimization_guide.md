# 🛠️ TV Monitor Optimization Guide

## Samsung UE55NU7093 + Windows + VS Code

> 🎯 Designed for developers using a TV as a monitor  
> 🧠 Focus: Text clarity · Reduced eye strain · Professional ergonomics

---

## 1. 📺 Samsung TV – Enable “PC” HDMI Mode

### Why?

- Ensures 4:4:4 Chroma for pixel-perfect text
- Disables unnecessary post-processing
- Reduces input lag

### How?

1. Press `Home` on the remote.
2. Go to **Source/Input**.
3. Highlight the HDMI port your PC uses.
4. Press `Up` or `≡` (Options).
5. Choose **Edit Name** → Select ✅ **PC**.

---

## 2. 🖥️ Windows Settings (for Text Clarity)

| Setting             | Recommended Value       |
| ------------------- | ----------------------- |
| Resolution          | 1920 x 1080 (Full HD)   |
| Scaling             | 100%                    |
| HDR                 | OFF (if text looks dim) |
| ClearType Text      | ON                      |
| Night Light / f.lux | ON (reduce eye fatigue) |
| Refresh Rate        | 60Hz                    |

To adjust:

- Open **Settings → Display**
- Search “ClearType” and follow the text tuner wizard
- Use f.lux (or Windows Night Light) to reduce blue light

---

## 3. ⚙️ VS Code `settings.json` (Ergonomic Setup)

```jsonc
{
  "editor.fontFamily": "'Fira Code', Consolas, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.fontSize": 16,
  "editor.lineHeight": 26,
  "editor.cursorSmoothCaretAnimation": true,
  "editor.cursorBlinking": "phase",
  "workbench.colorTheme": "Default Dark Modern",
  "workbench.startupEditor": "none",
  "editor.minimap.enabled": false,
  "editor.renderWhitespace": "boundary",
  "editor.wordWrap": "on",
  "editor.smoothScrolling": true,
  "terminal.integrated.fontSize": 15
}
```

---

# 🛠️ Vodič za Optimizaciju TV-a kao Monitora

## Samsung UE55NU7093 + Windows + VS Code

> 🎯 Namenjeno programerima koji koriste TV kao monitor
> 🧠 Fokus: Jasnoća teksta · Manji zamor očiju · Profesionalna ergonomija

---

## 1. 📺 Samsung TV – Aktiviranje “PC” moda na HDMI ulazu

### Zašto?

- Aktivira 4:4:4 Chroma → jasniji tekst
- Isključuje obradu slike (oštrina, interpolacija)
- Smanjuje input lag

### Kako?

1. Pritisni dugme `Home` na daljinskom.
2. Idi na **Source / Izvori**.
3. Označi HDMI ulaz gde je računar.
4. Pritisni `Strelicu gore` ili `≡` dugme.
5. Izaberi **Edit Name / Izmeni naziv** → ✅ **PC**

---

## 2. 🖥️ Windows podešavanja (za jasnoću teksta)

| Podešavanje         | Preporučena vrednost            |
| ------------------- | ------------------------------- |
| Rezolucija          | 1920 x 1080 (Full HD)           |
| Skaliranje          | 100%                            |
| HDR                 | ISKLJUČENO (ako je slika tamna) |
| ClearType Text      | UKLJUČEN                        |
| Noćni režim / f.lux | UKLJUČEN                        |
| Refresh Rate        | 60Hz                            |

Gde se podešava:

- Otvori **Settings → Display / Ekran**
- U pretrazi kucaj “ClearType” i prati čarobnjak
- Instaliraj f.lux ili koristi Windows Night Light

---

## 3. ⚙️ Podešavanje `settings.json` u VS Code-u

```jsonc
{
  "editor.fontFamily": "'Fira Code', Consolas, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.fontSize": 16,
  "editor.lineHeight": 26,
  "editor.cursorSmoothCaretAnimation": true,
  "editor.cursorBlinking": "phase",
  "workbench.colorTheme": "Default Dark Modern",
  "workbench.startupEditor": "none",
  "editor.minimap.enabled": false,
  "editor.renderWhitespace": "boundary",
  "editor.wordWrap": "on",
  "editor.smoothScrolling": true,
  "terminal.integrated.fontSize": 15
}
```

---

## ✅ Završni saveti:

- Redovno proveravaj HDMI labelu – neki Samsung modeli resetuju naziv nakon ažuriranja.
- Drži osvetljenje u prostoriji stabilnim (bez direktne svetlosti iza TV-a).
- Ako koristiš više monitora, uvek sinhronizuj skalu i osvežavanje ekrana.

---

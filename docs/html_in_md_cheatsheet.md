---

# 📝 HTML in Markdown Cheatsheet / HTML u Markdown-u (EN/SR)

Kratak vodič za korišćenje HTML tagova unutar `.md` fajlova.

---

## 🔤 Basic Formatting / Osnovno formatiranje

**EN:** These HTML tags are useful for styling text in Markdown files.
**SR:** Ovi HTML tagovi se koriste za stilizaciju teksta u Markdown fajlovima.

```html
<b>bold</b>                <!-- podebljan tekst -->
<i>italic</i>              <!-- iskošen tekst -->
<sup>superscript</sup>     <!-- indeks gore -->
<sub>subscript</sub>       <!-- indeks dole -->
<br>                        <!-- novi red (line break) -->
<hr>                        <!-- horizontalna linija -->
```

---

## 🖼️ Images / Slike

**EN:** You can control image size and alignment using HTML.
**SR:** Možeš kontrolisati veličinu slike i poravnanje pomoću HTML-a.

```html
<!-- Slika sa dimenzijom -->
<img src="https://github.com/user/repo/blob/main/assets/folder/image.png?raw=true" width="400" />

<!-- Slika u dva reda po dve -->
<p>
  <img src="img1.png" width="300" />
  <img src="img2.png" width="300" />
</p>
<p>
  <img src="img3.png" width="300" />
  <img src="img4.png" width="300" />
</p>

<!-- Opis slike -->
<p>
  <em>EN: Before running the script<br>SR: Pre pokretanja skripte</em>
</p>
```

---

## 📊 Tables with Images / Tabele sa slikama

```html
<table>
<tr>
  <td><img src="img1.png" width="250"></td>
  <td><img src="img2.png" width="250"></td>
</tr>
<tr>
  <td><em>EN: Before<br>SR: Pre</em></td>
  <td><em>EN: After<br>SR: Posle</em></td>
</tr>
</table>
```

---

## 📎 Notes / Napomene

* ✅ Radi u GitHub `.md` fajlovima
* ⚠️ HTML mora biti zatvoren i validan (npr. `<img />`)
* ❌ Ne koristi `<style>` i kompleksni CSS – nije podržan u GitHub renderovanju
* ✅ Kombinuj Markdown i HTML po potrebi

---

## 📘 Useful HTML Tags / Korisni HTML tagovi

| Tag       | Opis / Description            |
| --------- | ----------------------------- |
| `<b>`     | Bold / Podebljan tekst        |
| `<i>`     | Italic / Iskošen tekst        |
| `<br>`    | Line break / Novi red         |
| `<hr>`    | Horizontal rule / Linija      |
| `<img>`   | Slika sa atributima           |
| `<p>`     | Paragraf                      |
| `<em>`    | Emphasis (naglasak, iskošeno) |
| `<sup>`   | Superscript / Indeks gore     |
| `<sub>`   | Subscript / Indeks dole       |
| `<table>` | Tabela                        |
| `<td>`    | Ćelija tabele                 |
| `<tr>`    | Red tabele                    |

---

## 🧠 Bonus Tips / Dodatni saveti

* Slike iz GitHub repoa moraju koristiti `?raw=true` da bi se prikazale u `.md` fajlu
* HTML se koristi kada Markdown nije dovoljno fleksibilan
* Idealno za layout slika, tabele, kombinacije teksta/slike

---

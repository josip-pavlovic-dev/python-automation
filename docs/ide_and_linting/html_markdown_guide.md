# 📝 HTML in Markdown — Guide (EN + SR)

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 📌 Purpose / Svrha

- 🇬🇧 This cheatsheet explains how to embed HTML inside `.md` files for more control over formatting.
- 🇷🇸 Ovaj vodič objašnjava kako koristiti HTML unutar Markdown fajlova za dodatnu fleksibilnost.

---

## 🔤 Basic Formatting / Osnovno formatiranje

```html
<b>bold</b>
<!-- Podebljan tekst -->
<i>italic</i>
<!-- Iskošen tekst -->
<sup>superscript</sup>
<!-- Indeks gore -->
<sub>subscript</sub>
<!-- Indeks dole -->
<br />
<!-- Novi red -->
<hr />
<!-- Horizontalna linija -->
```

---

## 🖼️ Images / Slike

```html
<!-- Slika sa dimenzijom -->
<img
  src="https://github.com/user/repo/blob/main/assets/img.png?raw=true"
  width="400"
/>

<!-- Slike u mreži -->
<p>
  <img src="img1.png" width="300" />
  <img src="img2.png" width="300" />
</p>

<!-- Opis slike -->
<p>
  <em>EN: Before<br />SR: Pre</em>
</p>
```

---

## 📊 Tables with Images / Tabele sa slikama

```html
<table>
  <tr>
    <td><img src="img1.png" width="250" /></td>
    <td><img src="img2.png" width="250" /></td>
  </tr>
  <tr>
    <td>
      <em>EN: Before<br />SR: Pre</em>
    </td>
    <td>
      <em>EN: After<br />SR: Posle</em>
    </td>
  </tr>
</table>
```

---

## 📘 Supported HTML Tags in Markdown

| Tag       | Description EN        | Opis SR             |
| --------- | --------------------- | ------------------- |
| `<b>`     | Bold text             | Podebljan tekst     |
| `<i>`     | Italic text           | Iskošen tekst       |
| `<br>`    | Line break            | Novi red            |
| `<hr>`    | Horizontal rule       | Horizontalna linija |
| `<img>`   | Image with attributes | Slika sa atributima |
| `<p>`     | Paragraph block       | Paragraf            |
| `<em>`    | Emphasis              | Naglasak            |
| `<sup>`   | Superscript           | Indeks gore         |
| `<sub>`   | Subscript             | Indeks dole         |
| `<table>` | Table container       | Tabela              |
| `<td>`    | Table cell            | Ćelija              |
| `<tr>`    | Table row             | Red                 |

---

## ⚠️ HTML Limitations in Markdown (GitHub)

- ❌ Cannot use `<style>` or full CSS
- ❌ JavaScript not allowed
- ✅ HTML must be **valid and closed** (`<img />` not `<img>`)
- ✅ Best for: layout, images, alignment, mixed text/images

---

## 🧠 Bonus Tips

- Slike iz GitHub repoa moraju imati `?raw=true` da bi se prikazale
- Koristi HTML samo kada Markdown ne zadovoljava potrebe
- Kombinuj HTML i Markdown po potrebi

---

📁 Lokacija: `docs/html_markdown_guide.md`
✍️ Autor: Josip Pavlović
📅 Ažurirano: 2025-07-21

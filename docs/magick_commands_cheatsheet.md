
# 🧙‍♂️ ImageMagick Cheatsheet (magick CLI komande)

Ova skripta prikazuje najčešće korišćene `magick` komande u radu sa slikama.  
Komande funkcionišu u okviru terminala na sistemima sa instaliranim [ImageMagick](https://imagemagick.org).

---

## 🏁 1. Kreiranje praznih slika različitih boja i veličina

```bash
magick convert -size 100x100 xc:white test1.png
magick convert -size 200x150 xc:lightblue test2.jpg
magick convert -size 50x50 xc:gray test3.jpeg
magick convert -size 120x60 xc:yellow test4.png
````

---

## 🧩 2. Promena dimenzija slike (Resize)

```bash
magick input.jpg -resize 300x300 output.jpg
```

> Automatski čuva format slike i prilagođava dimenzije.

---

## 🔪 3. Sečenje slike (Crop)

```bash
magick input.png -crop 100x100+10+10 output.png
```

> Seče pravougaonik 100x100 piksela sa početkom na koordinatama (10,10).

---

## 🔁 4. Konvertovanje između formata

```bash
magick input.png output.jpg
```

> Konverzija formata bez dodatnih parametara.

---

## 🖼️ 5. Dodavanje teksta na sliku

```bash
magick input.png -pointsize 20 -draw "text 10,50 'Hello World'" output.png
```

> Dodaje tekst "Hello World" na poziciju (10,50) piksela.

---

## 🧪 6. Provera verzije ImageMagick-a

```bash
magick -version
```

> Proverava instalaciju i verziju ImageMagick alata.

---

## ℹ️ Napomena

* Na sistemima sa verzijom IMv7+ **uvek koristi `magick` ili `magick convert`**, a ne samo `convert`.
* Na Windowsu komanda `convert` može pozvati Windows alat za konverziju diskova.

---

📁 **Lokacija**: `docs/magick_commands_cheatsheet.md`
✍️ Autor: Josip Pavlović


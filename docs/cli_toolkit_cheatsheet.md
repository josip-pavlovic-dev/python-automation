# 🛠️ CLI Toolkit Cheatsheet — Bash, ImageMagick, FFmpeg (EN + SR)

> 🇬🇧 English + 🇷🇸 Srpski (latinica)

---

## 🧱 1. Bash komande (osnovno)

| Komanda             | Objašnjenje EN          | Objašnjenje SR                |
| ------------------- | ----------------------- | ----------------------------- |
| `ls`                | List files in directory | Prikaži sadržaj direktorijuma |
| `cd folder`         | Change directory        | Uđi u folder                  |
| `cd ..`             | Go one level up         | Vrati se jedan nivo           |
| `pwd`               | Print working directory | Trenutna putanja              |
| `mkdir ime`         | Make directory          | Kreiraj novi folder           |
| `touch fajl.py`     | Create empty file       | Kreiraj prazan fajl           |
| `code .`            | Open VS Code            | Otvori folder u VS Code-u     |
| `python skripta.py` | Run Python file         | Pokreni Python fajl           |
| `clear`             | Clear terminal          | Očisti ekran                  |
| `rm fajl.txt`       | Remove file             | Obriši fajl                   |
| `rm -r folder`      | Remove folder           | Obriši folder i sve u njemu   |

---

## 🖼️ 2. ImageMagick — `magick` komande

### ✅ Osnovne komande:

```bash
magick input.jpg -resize 200x200 output.jpg
magick input.png -rotate 90 output.png
magick input.jpg -crop 100x100+20+20 output.jpg
```

### 📋 Objašnjenja:

| Komanda         | Opis EN                  | Opis SR                        |
| --------------- | ------------------------ | ------------------------------ |
| `-resize WxH`   | Resize to width/height   | Promeni dimenzije slike        |
| `-rotate angle` | Rotate image             | Rotiraj sliku za određeni ugao |
| `-crop WxH+X+Y` | Crop image               | Iseci sliku                    |
| `-quality 85`   | JPEG compression quality | Kvalitet JPEG slike            |
| `-strip`        | Remove metadata          | Ukloni Exif/metapodatke        |

### 📦 Generisanje test slika:

```bash
magick -size 300x200 canvas:gray output.png
magick -size 400x300 xc:skyblue label:'Test' -gravity center -append output.jpg
```

---

## 🎞️ 3. FFmpeg — video/audio obrada

### 🎬 Osnovne komande:

```bash
ffmpeg -i input.mp4 output.avi
ffmpeg -i input.mov -c:v libx264 -preset slow -crf 22 output.mp4
```

### 🔇 Izdvajanje zvuka:

```bash
ffmpeg -i input.mp4 -q:a 0 -map a output.mp3
```

### 🔪 Sečenje i spajanje:

```bash
ffmpeg -i input.mp4 -ss 00:00:10 -to 00:00:20 -c copy cut.mp4
ffmpeg -f concat -safe 0 -i files.txt -c copy merged.mp4
```

### 📝 Primer `files.txt` za spajanje:

```
file 'deo1.mp4'
file 'deo2.mp4'
```

### 📋 Objašnjenja:

| Parametar | Opis EN        | Opis SR                          |
| --------- | -------------- | -------------------------------- |
| `-i`      | Input file     | Ulazni fajl                      |
| `-ss`     | Start time     | Vreme početka                    |
| `-to`     | End time       | Vreme završetka                  |
| `-c copy` | No re-encoding | Bez ponovne kompresije           |
| `-crf`    | Quality factor | Faktor kvaliteta (niže je bolje) |
| `-preset` | Encoding speed | Brzina enkodiranja               |

---

## 🧠 Saveti za CLI rad

- ✅ Piši komande u `.sh` fajlove kada su kompleksnije
- ✅ Koristi `echo`, `cat`, `grep`, `find` za rad sa tekstom
- ✅ Ako zaboraviš opciju: koristi `--help`, npr. `ffmpeg --help`
- ✅ Redovno briši nepotrebne fajlove komandama: `rm`, `find`, `shred`

---

## 🧾 Lokacija fajla

📁 `docs/cli_toolkit_cheatsheet.md`
✍️ Autor: Josip Pavlović
📅 Ažurirano: 2025-07-21

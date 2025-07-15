# 🧾 setup_test_folder.sh Cheatsheet

## 📌 Description / Opis

**EN:**  
Shell script to automatically create test folder structure and files for verifying file management functions.  
**SR:**  
Shell skripta za automatsko kreiranje strukture foldera i fajlova radi testiranja skripti za upravljanje fajlovima.

---

## 🧱 Structure Created / Kreirana struktura

**EN:**
- `test_folder/`
  - `document.txt`
  - `image.png`
  - `archive.zip`
  - `old_file.log` (modified 10 days ago)

**SR:**
- `test_folder/`
  - `document.txt`
  - `image.png`
  - `archive.zip`
  - `old_file.log` (izmenjen pre 10 dana)

---

## ▶️ How to Use / Kako koristiti

**EN:**
```bash
bash setup_test_folder.sh
```

**SR:**
```bash
bash setup_test_folder.sh
```

This will generate all necessary files for testing. / Ovo će generisati sve neophodne fajlove za testiranje.

---

## 📎 Notes / Napomene

- Make sure the script has execution permission (`chmod +x setup_test_folder.sh`) / Uveriti se da li skripta ima dozvolu za izvršenje (`chmod +x setup_test_folder.sh`)
- Files will be overwritten if they already exist! / Fajlovi će biti prekopirani ako već postoje!


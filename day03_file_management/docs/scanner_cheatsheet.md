# 🧪 Scanner Cheatsheet | Vodič za Scanner skriptu

##### 🇬🇧: A bilingual guide for understanding and using the `scanner.py' script within the **Day 03 – File Management Suite** project.
##### 🇷🇸: Dvojezični vodič za razumevanje i upotrebu `scanner.py` skripte u okviru projekta **Day 03 – File Management Suite**.

## 📌 Purpose | Svrha

### 🇬🇧: The `scanner.py` script recursively traverses a target directory and lists all files and subdirectories, capturing key attributes.

### 🇷🇸: Skripta `scanner.py` rekurzivno prolazi kroz ciljni direktorijum i prikazuje sve fajlove i poddirektorijume sa ključnim informacijama.

---

## ⚙️ Usage | Korišćenje

```bash
python scanner.py test_folder
```

##### 🇬🇧`test_folder`: Path to the directory you want to scan.
##### 🇷🇸 `test_folder`: Putanja do direktorijuma koji želite da skenirate.

---

## 📁 Output | Izlaz

### 🇬🇧: Prints the folder structure, listing each file and subfolder with indentation to reflect hierarchy.

### 🇷🇸: Prikazuje strukturu direktorijuma, navodeći svaki fajl i podfolder sa uvlačenjem koje odražava hijerarhiju.

---

## 🧠 Key Concepts | Ključni koncepti

| Concept                     | Python Modules/Functions      | Objašnjenje (🇷🇸/🇬🇧) |
|----------------------------|-------------------------------|---------------------|
| Directory Traversal        | `os.walk()`                   | Šeta kroz strukturu direktorijuma / Traverses directories |
| Indented Output            | `level * "  "`                | Vizuelno prikazuje hijerarhiju foldera / Shows folder depth |
| Argument Handling          | `sys.argv`, `len(sys.argv)`   | Čita argumente iz komandne linije / Parses command-line args |
| Path Manipulation          | `os.path.join()`              | Spaja putanje bez grešaka / Joins paths safely |
| Basic Validation           | `if not os.path.isdir()`      | Proverava da li je putanja validan direktorijum / Validates input path |

---

## 🧩 Sample Output | Primer izlaza

```
📁 test_folder
  📄 file1.txt
  📄 file2.txt
  📁 subfolder
    📄 image.png
```

---

## ✍️ Author Note | Napomena autora

### 🇬🇧: This script was created as a practice in recursive directory exploration and argument validation, aiming to understand how directory trees can be visualized in terminal.

### 🇷🇸: Skripta je nastala kao vežba u rekurzivnom pretraživanju direktorijuma i validaciji argumenata. Cilj je bio vizualizovati strukturu direktorijuma u terminalu.


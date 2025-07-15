# 🧪 Scanner Cheatsheet / Vodič za Scanner skriptu

Dvojezični vodič za razumevanje i upotrebu `scanner.py` skripte u okviru projekta **Day 03 – File Management Suite**.

---

## 📌 Purpose / Svrha

**EN:**  
The `scanner.py` script recursively traverses a target directory and lists all files and subdirectories, capturing key attributes.

**SR:**  
Skripta `scanner.py` rekurzivno prolazi kroz ciljni direktorijum i prikazuje sve fajlove i poddirektorijume sa ključnim informacijama.

---

## ⚙️ Usage / Korišćenje

```bash
python scanner.py test_folder
```

- `test_folder`: Path to the directory you want to scan. / Putanja do direktorijuma koji želite da skenirate.

---

## 📁 Output / Izlaz

**EN:**  
Prints the folder structure, listing each file and subfolder with indentation to reflect hierarchy.

**SR:**  
Prikazuje strukturu direktorijuma, navodeći svaki fajl i podfolder sa uvlačenjem koje odražava hijerarhiju.

---

## 🧠 Key Concepts / Ključni koncepti

| Concept                     | Python Modules/Functions      | Objašnjenje (SR/EN) |
|----------------------------|-------------------------------|---------------------|
| Directory Traversal        | `os.walk()`                   | Šeta kroz strukturu direktorijuma / Traverses directories |
| Indented Output            | `level * "  "`                | Vizuelno prikazuje hijerarhiju foldera / Shows folder depth |
| Argument Handling          | `sys.argv`, `len(sys.argv)`   | Čita argumente iz komandne linije / Parses command-line args |
| Path Manipulation          | `os.path.join()`              | Spaja putanje bez grešaka / Joins paths safely |
| Basic Validation           | `if not os.path.isdir()`      | Proverava da li je putanja validan direktorijum / Validates input path |

---

## 🧩 Sample Output / Primer izlaza

```
📁 test_folder
  📄 file1.txt
  📄 file2.txt
  📁 subfolder
    📄 image.png
```

---

## ✍️ Author Note / Napomena autora

**EN:**  
This script was created as a practice in recursive directory exploration and argument validation, aiming to understand how directory trees can be visualized in terminal.

**SR:**  
Skripta je nastala kao vežba u rekurzivnom pretraživanju direktorijuma i validaciji argumenata. Cilj je bio vizualizovati strukturu direktorijuma u terminalu.


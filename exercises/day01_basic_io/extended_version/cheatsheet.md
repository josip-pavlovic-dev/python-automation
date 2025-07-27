# 🧪 Cheatsheet – Basic I/O Modes | _Cheatsheet – Osnovni režimi ulaza/izlaza_

## 🧠 Concepts Used | _Korišćeni pojmovi_

| English                                                            | _Serbian_                                                                          |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Use of `Path(__file__).resolve().parent` to get absolute directory | _Upotreba `Path(__file__).resolve().parent` za dobijanje apsolutnog direktorijuma_ |
| Using `input()` and `while` loop to capture multiline input        | _Korišćenje `input()` i `while` petlje za unos više linija_                        |
| Opening multiple files with a single `with` statement using `\`    | _Otvaranje više fajlova pomoću jednog `with` izraza uz `\`_                        |
| Writing output with `enumerate()` to add line numbers              | _Pisanje izlaza pomoću `enumerate()` radi dodavanja rednih brojeva_                |
| Handling mode switching using `sys.argv`                           | _Rukovanje promenom režima rada pomoću `sys.argv`_                                 |
| Using `f-strings` for dynamic output                               | _Korišćenje `f-string` izraza za dinamički izlaz_                                  |

---

## 🔍 Key Syntax | _Ključna sintaksa_

| English                           | _Serbian_                                          |
| --------------------------------- | -------------------------------------------------- |
| `Path(__file__).resolve().parent` | _Apsolutna putanja direktorijuma skripte_          |
| `with open(...) as ...`           | _Korišćenje context menadžera za rad sa fajlovima_ |
| `enumerate(lines, start=1)`       | _Enumeracija linija počevši od 1_                  |
| `input("Prompt: ")`               | _Unos korisnika sa porukom_                        |
| `sys.argv[1] == "--interactive"`  | _Provera CLI argumenta_                            |

---

## 📌 Notes | _Beleške_

| English                                                     | _Serbian_                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| All paths are absolute so script can run from any directory | _Sve putanje su apsolutne pa skripta može da se pokrene iz bilo kog direktorijuma_ |
| Empty line (`""`) is used to break interactive input loop   | _Prazna linija (`""`) se koristi za prekid interaktivne petlje_                    |
| Files are opened with `utf-8` encoding for compatibility    | _Fajlovi se otvaraju sa `utf-8` enkodiranjem radi kompatibilnosti_                 |

---

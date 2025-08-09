#!/bin/bash

# ------------------------------------------
# Bash skripta za kreiranje test strukture
# Koristi se za testiranje skripti scanner.py i cleaner.py
# ------------------------------------------

# Ako već postoji stari test_folder, brišemo ga da počnemo "čisto"
rm -rf test_folder

# Kreiramo glavne podfoldere koji simuliraju realnu strukturu
mkdir -p test_folder/scripts      # Folder za skripte
mkdir -p test_folder/images       # Folder za slike

# Kreiramo testne fajlove sa sadržajem (tekstualni podaci)
echo "Ovo je info fajl za testiranje." > test_folder/info.txt
echo "README za test folder." > test_folder/readme.txt

# Kreiramo prazne fajlove bez sadržaja (za simulaciju postojanja fajlova)
touch test_folder/data.csv                        # Prazan CSV fajl
touch test_folder/images/img1.jpg                 # Simulacija slike
touch test_folder/images/img2.png                 # Simulacija druge slike
touch test_folder/scripts/script.py               # Prazna Python skripta
touch test_folder/temp.tmp                        # Fajl sa .tmp ekstenzijom (za testiranje cleaner.py)

# ------------------------------------------
# Kraj skripte
# ------------------------------------------

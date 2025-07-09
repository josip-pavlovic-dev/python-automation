import os
import shutil

# Putanja do foldera koji želiš da organizuješ
# Po defaultu, koristi test_files koji je u istom folderu kao skripta

# Umesto da koristimo relativnu putanju: target_folder = "test_files" mi ćemo koristiti apsolutnu putanju baziranu na lokaciji skripte:

script_dir = os.path.dirname(os.path.abspath(__file__))
target_folder = os.path.join(script_dir, "test_files")


# Listanje svih fajlova u folderu

files = os.listdir(target_folder)

# Prolazak kroz sve fajlove

for file in files:
    # Kreira punu putanju
    file_path = os.path.join(target_folder, file)

    # Preskoči ako nije fajl
    if not os.path.isfile(file_path):
        continue

    # Izdvajanje ekstenzije
    _, extension = os.path.splitext(file)

    # Uklanjanje tačke (npr. ".jpg" -> "jpg")
    extension = extension[1:]

    # Formiranje putanje do foldera za tu ekstenziju
    new_folder = os.path.join(target_folder, extension)

    # Kreiranje foldera ako ne postoji
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Novi put za fajl
    new_path = os.path.join(new_folder, file)

    # Premestanje fajla
    shutil.move(file_path, new_path)


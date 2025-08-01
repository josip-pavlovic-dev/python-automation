import os

def get_current_working_directory() -> str:
    """
    ✅ Funkcija: get_current_working_directory

    🟠 Opis (SR): Vraća apsolutnu putanju trenutnog radnog direktorijuma.
    🟢 Description (EN): Returns the absolute path of the current working directory.

    🔹 Povratna vrednost / Returns:
        str: Putanja radnog direktorijuma. / The working directory path.

    🧪 Primer / Example:
        >>> get_current_working_directory()
        'C:\\Users\\JoleDev\\dev-learning\\python-automation'
    """
    return os.getcwd()

def move_to_directory(path: str) -> None:
    """
    ✅ Funkcija: move_to_directory

    🟠 Opis (SR): Menja trenutni radni direktorijum na zadatu putanju.
    🟢 Description (EN): Changes the current working directory to the specified path.

            
    🔸 Parametri / Parameters:
        path (str): Putanja do novog direktorijuma. / Path to the new directory.
    🔹 Povratna vrednost / Returns:
        str: Poruka o uspešnom pomeranju. / Message indicating successful move.

    🧪 Primer / Example:
        >>> move_to_directory('C:\\Users\\JoleDev\\Documents')
        '✅ Moved to C:\\Users\\JoleDev\\Documents'
    """
    try:
        os.chdir(path)
        print(f"✅ Moved to {path}")
    except FileNotFoundError:
        print(f"⚠️ Directory {path} not found.")
    except PermissionError:
        print(f"⚠️ Permission denied to access {path}.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")




def list_directory_contents(path: str = ".") -> list[str]:
    """
    ✅ Funkcija: list_directory_contents

    🟠 Opis (SR): Vraća listu fajlova i foldera u zadatom direktorijumu.
    🟢 Description (EN): Returns a list of files and folders in the given directory.

    🔸 Parametri / Parameters:
        path (str): Putanja do direktorijuma (podrazumevano trenutni). /
                    Path to the directory (defaults to current).

    🔹 Povratna vrednost / Returns:
        list[str]: Lista imena fajlova i foldera. /
                   List of filenames and folders.

    🧪 Primer / Example:
        >>> list_directory_contents()
        ['README.md', 'scripts', 'main.py']
    """
    return os.listdir(path)

def create_new_directory(name: str) -> None:
    """
    ✅ Funkcija: create_new_directory

    🟠 Opis (SR): Kreira novi direktorijum sa zadatim imenom.
    🟢 Description (EN): Creates a new directory with the given name.

    🔸 Parametri / Parameters:
        name (str): Ime novog direktorijuma. / Name of the new directory.

    🧪 Primer / Example:
        >>> create_new_directory('test_dir')
        '✅ test_dir created.'
    """
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"✅ {name} created.")
    else:
        print(f"⚠️ {name} already exists.")

def create_a_new_file(file_name: str) -> None:
    """
    ✅ Funkcija: create_a_new_file

    🟠 Opis (SR): Kreira novi fajl sa zadatim imenom.
    🟢 Description (EN): Creates a new file with the given name.

    🔸 Parametri / Parameters:
        file_name (str): Ime novog fajla. / Name of the new file.

    🧪 Primer / Example:
        >>> create_a_new_file('example.txt')
        '✅ example.txt created.'
    """
    with open(file_name, 'w') as f:
        f.write("")  # Create an empty file
    print(f"✅ {file_name} created.")


def rename_directory(old_name: str, new_name: str) -> None:
    """
    ✅ Funkcija: rename_directory

    🟠 Opis (SR): Preimenuje postojeći direktorijum.
    🟢 Description (EN): Renames an existing directory.

    🔸 Parametri / Parameters:
        old_name (str): Staro ime direktorijuma. / Old directory name.
        new_name (str): Novo ime direktorijuma. / New directory name.

    🧪 Primer / Example:
        >>> rename_directory('test_dir', 'renamed_dir')
        '✅ Directory renamed.'
    """
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("✅ Directory renamed.")
    else:
        print(f"⚠️ {old_name} not found.")
def delete_directory(name: str) -> None:
    """
    ✅ Funkcija: delete_directory

    🟠 Opis (SR): Briše direktorijum sa zadatim imenom.
    🟢 Description (EN): Deletes the directory with the given name.

    🔸 Parametri / Parameters:
        name (str): Ime direktorijuma za brisanje. / Name of the directory to delete.

    🧪 Primer / Example:
        >>> delete_directory('test_dir')
        '✅ Directory deleted.'
    """
    if os.path.exists(name):
        os.rmdir(name)
        print(f"✅ {name} deleted.")
    else:
        print(f"⚠️ {name} not found.")

def delete_file(file_name: str) -> None:
    """
    ✅ Funkcija: delete_file

    🟠 Opis (SR): Briše fajl sa zadatim imenom.
    🟢 Description (EN): Deletes the file with the given name.

    🔸 Parametri / Parameters:
        file_name (str): Ime fajla za brisanje. / Name of the file to delete.

    🧪 Primer / Example:
        >>> delete_file('example.txt')
        '✅ example.txt deleted.'
    """
    if os.path.isfile(file_name):
        os.remove(file_name)
        print(f"✅ {file_name} deleted.")
    else:
        print(f"⚠️ {file_name} not found.")


# Testiranje funkcija

print("Testiranje funkcija iz modula os:")

# Prikaz trenutnog radnog direktorijuma
print("📁 Trenutni radni direktorijum: ", get_current_working_directory())

# Prikaz sadržaja trenutnog direktorijuma
print("📂 Sadržaj direktorijuma: ", list_directory_contents())

# Korisnik unosi ime novog foldera
folder_name = input("🆕 Unesite ime novog direktorijuma za kreiranje: ").strip()
create_new_directory(folder_name)

# Korisnik unosi ime za novi fajl unutar tog foldera
file_name = input("📝 Unesite ime fajla koji želite da kreirate unutar tog direktorijuma: ").strip()
create_a_new_file(os.path.join(folder_name, file_name))

# Prikaz sadržaja foldera nakon kreiranja fajla
print(f"📂 Sadržaj direktorijuma '{folder_name}': ", list_directory_contents(folder_name))

# Korisnik unosi novo ime foldera (pre nego što se uđe u njega!)
folder_new_name = input("✏️ Unesite novo ime za preimenovanje direktorijuma: ").strip()
rename_directory(folder_name, folder_new_name)

# Ulazak u preimenovani folder
move_to_directory(folder_new_name)

# Prikaz konačne putanje i sadržaja
print("📁 Novi radni direktorijum: ", get_current_working_directory())
print("📂 Sadržaj novog direktorijuma: ", list_directory_contents())

# Brisanje fajla primer.txt iz trenutno aktivnog direktorijuma
print("Brišem fajl 'primer.txt': ", delete_file("primer.txt"))

# Vraćanje u naddirektorijum
print("Vraćam se u naddirektorijum: ", move_to_directory(".."))
print("Trenutni direktorijum: ", get_current_working_directory())

# Brisanje preimenovanog direktorijuma
print(f"Brišem direktorijum '{folder_new_name}': ", delete_directory(folder_new_name))

# Prikaz sadržaja trenutnog direktorijuma da se potvrdi da folder više ne postoji
print("Lista sadržaja nakon brisanja foldera: ", list_directory_contents())

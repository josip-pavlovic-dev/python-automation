"""
🧪 trening.py – Utility Functions for File Operations (os module)
Author: Josip Pavlović
"""

import os


def get_current_working_directory() -> str:
    """
    ✅ Funkcija: get_current_working_directory

    🟠 Opis (SR): Vraća apsolutnu putanju trenutnog radnog direktorijuma.
    🟢 Description (EN): Returns the absolute path of the current working directory.
    """
    return os.getcwd()


def move_to_directory(path: str) -> None:
    """
    ✅ Funkcija: move_to_directory

    🟠 Opis (SR): Menja trenutni radni direktorijum na zadatu putanju.
    🟢 Description (EN): Changes the current working directory to the specified path.

    🔸 Parametri / Parameters:
        path (str): Putanja do direktorijuma. / Path to the target directory.
    """
    try:
        os.chdir(path)
        print(f"✅ Moved to {path} | _Prebačeno u {path}_")
    except FileNotFoundError:
        print(f"⚠️ Directory {path} not found. | _Direktorijum {path} nije pronađen._")
    except PermissionError:
        print(f"⚠️ Permission denied for {path}. | _Pristup odbijen za {path}_")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e} | _Neočekivana greška: {e}_")


def list_directory_contents(path: str = ".") -> list[str]:
    """
    ✅ Funkcija: list_directory_contents

    🟠 Opis (SR): Vraća listu fajlova i foldera u zadatom direktorijumu.
    🟢 Description (EN): Returns a list of files and folders in the given directory.
    """
    return os.listdir(path)


def create_new_directory(name: str) -> None:
    """
    ✅ Funkcija: create_new_directory

    🟠 Opis (SR): Kreira novi direktorijum ako već ne postoji.
    🟢 Description (EN): Creates a new directory if it doesn't already exist.
    """
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"✅ {name} created.")
    else:
        print(f"⚠️ {name} already exists.")


def create_a_new_file(file_name: str) -> None:
    """
    ✅ Funkcija: create_a_new_file

    🟠 Opis (SR): Kreira novi prazan fajl.
    🟢 Description (EN): Creates a new empty file.
    """
    with open(file_name, "w") as f:
        f.write("")
    print(f"✅ {file_name} created.")


def rename_directory(old_name: str, new_name: str) -> None:
    """
    ✅ Funkcija: rename_directory

    🟠 Opis (SR): Preimenuje direktorijum ako postoji.
    🟢 Description (EN): Renames a directory if it exists.
    """
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print("✅ Directory renamed.")
    else:
        print(f"⚠️ {old_name} not found.")


def delete_directory(name: str) -> None:
    """
    ✅ Funkcija: delete_directory

    🟠 Opis (SR): Briše direktorijum ako postoji.
    🟢 Description (EN): Deletes a directory if it exists.
    """
    if os.path.exists(name):
        os.rmdir(name)
        print(f"✅ {name} deleted.")
    else:
        print(f"⚠️ {name} not found.")


def delete_file(file_name: str) -> None:
    """
    ✅ Funkcija: delete_file

    🟠 Opis (SR): Briše fajl ako postoji.
    🟢 Description (EN): Deletes a file if it exists.
    """
    if os.path.isfile(file_name):
        os.remove(file_name)
        print(f"✅ {file_name} deleted.")
    else:
        print(f"⚠️ {file_name} not found.")

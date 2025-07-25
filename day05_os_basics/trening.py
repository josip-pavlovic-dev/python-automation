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


# Testiranje funkcija

print("Testiranje funkcija iz modula os:")
print("Trenutni radni direktorijum: ", get_current_working_directory())
print("Lista fajlova i foldera iz direktorijuma: ", list_directory_contents())
import os

def get_full_path(filename: str) -> str:
    """
    Vraća punu putanju do fajla u trenutnom radnom direktorijumu.
    """
    current_dir = os.getcwd()
    return os.path.join(current_dir, filename)


if __name__ == "__main__":
    filename = "primer.txt"
    full_path = get_full_path(filename)
    print(f"Puna putanja: {full_path}")
    # Očekivani ispis: "Puna putanja: /putanja/do/trenutnog/direktorijuma/primer.txt"
    # Napomena: Putanja će zavisiti od trenutnog radnog direktorijuma



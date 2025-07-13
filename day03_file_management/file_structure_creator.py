import os

# Kreiranje osnovnog foldera

base_folder = "test_folder"

# Lista podfoldera
subfolders = ["docs", "images", "scripts"]

# Kreiranje podfoldera unutar 'test_folder'

for folder in subfolders:
    path = os.path.join(base_folder, folder)
    os.makedirs(path, exist_ok=True)
    print(f"Kreiran folder: {path}")
    
    # Kreiranje fajla unutar svakog podfoldera

    file_path = os.path.join(path, "info.txt")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Ovo je fajl unutar '{folder}' foldera.\n")
        print(f"Kreiran fajl: {file_path}")

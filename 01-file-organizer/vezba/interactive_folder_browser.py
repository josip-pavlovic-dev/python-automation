import os

def get_available_drives():
    drives = []
    for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

# Prikaz dostupnih diskova
drives = get_available_drives()

if not drives:
    print("[ERROR] Nema dostupnih diskova.")
    exit()

print("\n💽 Dostupni diskovi:")
for i, d in enumerate(drives, 1):
    print(f"  {i}. {d}")

# Unos diska sa liste
while True:
    choice = input("\nUnesi broj diska koji želiš da pregledaš: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(drives):
        disk = drives[int(choice) - 1]
        break
    else:
        print("[ERROR] Neispravan izbor. Pokušaj ponovo.")
print(f"\n📂 Pregledanje diska: {disk}")


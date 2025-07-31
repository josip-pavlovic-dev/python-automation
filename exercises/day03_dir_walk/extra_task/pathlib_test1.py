from pathlib import Path

print("Testiranje pathlib modula")

# 1) Osnovne putanje
working_dir = Path.cwd()
print(f"Trenutni radni direktorijum (cwd): {working_dir}")

script_path = Path(__file__).resolve()
print(f"Apsolutna putanja do skripte:      {script_path}")

script_dir = script_path.parent
print(f"Direktorijum skripte:              {script_dir}")

# 2) Roditeljske putanje uz proveru dubine
parents = script_path.parents  # sequence-like
if len(parents) > 1:
    print(f"Drugi roditeljski dir:             {parents[1]}")
else:
    print("Nema dovoljno nivoa za parents[1].")

if len(parents) > 2:
    print(f"Treći roditeljski dir:             {parents[2]}")
else:
    print("Nema dovoljno nivoa za parents[2].")

# 3) Rad sa fajlom u istom folderu kao i skripta
test_file = script_dir / "test.txt"
print(f"Putanja do test.txt:               {test_file}")

if test_file.exists():
    print(f"Fajl postoji:                      {test_file.name}")
else:
    print("Fajl ne postoji — biće kreiran.")

# 4) Upis (overwrite) ili dopuna (append)
# Overwrite:

test_file.write_text(
    "Ovo je testni fajl kreiran pomoću pathlib modula.\n",
    encoding="utf-8"
)

# Ako želimo append umesto overwrite, koristimo ovo umesto write_text:
with test_file.open("a", encoding="utf-8") as f:
    f.write("Dodat red (append).\n")

# 5) Čitanje sadržaja
content = test_file.read_text(encoding="utf-8")
print(f"Sadržaj test.txt:\n{content}")






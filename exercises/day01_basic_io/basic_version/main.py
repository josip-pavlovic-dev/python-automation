"""
day01_basic_io – Basic I/O – Čitanje i pisanje fajlova

Zadatak:
1. Pročitati fajl `input.txt` red po red.
2. Ispisati sadržaj u terminal.
3. Kreirati fajl `output.txt` u kome je svaka linija numerisana.
"""

# Otvaramo dva fajla istovremeno:
# - input.txt za čitanje ("r")
# - output.txt za pisanje ("w")
# Znak \ koristi se da se linija nastavi u sledećem redu
with open("input.txt", "r", encoding="utf-8") as input_file, \
     open("output.txt", "w", encoding="utf-8") as output_file:

    # enumerate nam daje redni broj (index) i sadržaj linije (line)
    # start=1 znači da brojanje kreće od 1
    for index, line in enumerate(input_file, start=1):
        # Ispisujemo liniju u terminal (uklanjamo \n sa kraja)
        print(line.strip())

        # Upisujemo red u novi fajl, uz redni broj ispred sadržaja
        output_file.write(f"{index}: {line}")

# Nakon izlaska iz with-bloka fajlovi se automatski zatvaraju
print("\n✅ File processed successfully and written to output.txt")

""" 
Važno: Ovu skriptu morate pokrenuti iz istog direktorijumu gde se nalaze fajlovi input.txt i output.txt. U terminalu se mora iz radnog foldera preći u folder gde je smeštena basic_main.py skripta a zatim se iz tog foldera pokreće skripta komandom "python basic_main.py". Proverite da su fajlovi input.txt i output.txt prisutni u tom folderu.
Ukoliko fajl input.txt ne postoji, skripta će baciti grešku.

"""
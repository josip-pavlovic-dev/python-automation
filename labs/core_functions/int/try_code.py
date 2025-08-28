print("📝 Mini-eksperiment za tebe u REPL-u")

x = int(-10.5)  # -10
print(x)
print(x.bit_count())
print(x.to_bytes(2, "big", signed=True))

print("👉 Ovako testiraš neke od metoda koje si video.")
print("👉 Koliko bitova treba za binarni zapis broja.")

(10).bit_length()  # 4, jer 10 je 1010 u binarnom zapisu
(255).bit_length()  # 8

print("👉 Koliko jedinica (1) ima u binarnom zapisu.")

(10).bit_count()  # 2, jer 1010 ima dve jedinice
(15).bit_count()  # 4, jer 1111

print("👉 Pretvara broj u sekvencu bajtova.")

# to_bytes(length, byteorder, signed=False)
(255).to_bytes(2, "big")  # b'\\x00\\xff'
(255).to_bytes(2, "little")  # b'\\xff\\x00'

print("👉 Obrnut proces: bajtovi → int.")
# from_bytes(b, byteorder, signed=False)
# (klasna metoda, pozivaš je kao int.from_bytes)

int.from_bytes(b"\\x00\\xff", "big")  # 255
int.from_bytes(b"\\xff\\x00", "little")  # 255

# numerator, denominator
# 👉 jer se int ponaša i kao “rational number” (specijalizovan Fraction).
x = 5
(x).numerator  # 5
(x).denominator  # 1

# real, imag
# 👉 jer se int ponaša i kao kompleksan broj gde su imaginarni deo = 0.
(5).real  # 5
(5).imag  # 0

import os

print(__file__)
# __file__ je posebna promenljiva koja sadrži putanju do trenutne skripte.
# Vraća apsolutnu putanju skripte koju pokrećeš.
# Koristiš je kada želiš da kod zna gde se on sam nalazi.

print(os.path.abspath("../assets/agent_mode_active.svg"))
# Prikazuje apsolutnu putanju do datoteke

print(os.path.dirname(__file__))
# Prikazuje dirktorijum u kojem se nalazi skripta.

print(os.path.basename(__file__))
# Prikazuje ime skripte


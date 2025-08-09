"""
🧪 path_debugger.py – Debugging absolute and relative paths in Python
Author: Josip Pavlović
"""

import os

# Print the relative path to this file
# Ispis relativne putanje do ove skripte
print("📍 __file__ variable:")
print(__file__)

# Print the absolute path to a file located one level up in assets/
# Ispis apsolutne putanje do fajla u folderu assets/ jedan nivo iznad
print("\n📍 Absolute path of '../assets/agent_mode_active.svg':")
print(os.path.abspath("../assets/agent_mode_active.svg"))

# Print the directory where this script is located
# Ispis direktorijuma u kojem se nalazi ova skripta
print("\n📍 Directory of this script:")
print(os.path.dirname(__file__))

# Print only the filename of the current script
# Ispis samo imena ove skripte
print("\n📍 Filename of this script:")
print(os.path.basename(__file__))

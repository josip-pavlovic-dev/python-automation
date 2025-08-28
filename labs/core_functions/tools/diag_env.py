import glob
import importlib.util
import os
import sys

print("Python:", sys.version)
print("Exe:", sys.executable)
print("CWD:", os.getcwd())
print("pytest.ini here?:", glob.glob("pytest.ini"))
print("Top sys.path:", *sys.path[:5], sep="\n - ")
for mod in ["pytest", "coverage", "ruff"]:
    print(mod, "->", "OK" if importlib.util.find_spec(mod) else "MISSING")
print("-----")

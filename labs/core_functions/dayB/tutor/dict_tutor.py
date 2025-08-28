# dict_tutor.py — fokus: KeyError vs get, hashability
d = {"x": 1}
print(d.get("y"), d.get("y", 99))
try:
    print(d["y"])
except Exception as e:
    print("Key access error:", type(e).__name__)
try:
    _ = {[]: 1}
except Exception as e:
    print("Unhashable key:", type(e).__name__)
t = (1, 2)
print({t: "ok"}[t])

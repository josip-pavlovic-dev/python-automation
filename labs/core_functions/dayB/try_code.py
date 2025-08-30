d = {}
print(d.setdefault("items", []).append("x"))     # {'items': ['x']}
v = d.get("user", "guest")                # 'guest'
v = d.pop("missing", None)                # None (bez KeyError)
print("RADI!")

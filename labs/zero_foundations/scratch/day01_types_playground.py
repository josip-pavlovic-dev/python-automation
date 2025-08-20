from pathlib import Path


def title(msg: str) -> None:
    print("\n" + "=" * 10, msg)

#ENG: Scalars and truthiness
#SR : Skalari i truthiness
title("SCALARS & TRUTHINESS")
print(bool([]))      # False
print(bool(""))      # False
print(bool(0))       # False
print(bool(None))    # False
print(bool(set()))   # False
print(bool([1]))     # True

#ENG: LIST — order + duplicates + mutation
#SR : LISTA — redosled + duplikati + mutacija
title("LIST")
xs = [10, 20, 20, 30]
xs.append(40)
xs += [50]           # mutacija na mestu
print(xs)            # [10, 20, 20, 30, 40, 50]
print(xs[1:4])       # [20, 20, 30]

#ENG: TUPLE — fixed record; hashable; single-element tuple note
#SR : TAPL — fiksni rekord; hashable; napomena za jednoelementnu
title("TUPLE")
pt = (10, 20)
single = (1,)        # bez zareza ovo je samo int sa zagradama!
print(pt, single)    # (10, 20) (1,)

#ENG: DICT — mapping; safe access with get; iteration preserves order
#SR : REČNIK — mapiranje; bezbedan pristup get; čuva redosled
title("DICT")
cfg = {"level": "INFO", "file": "app.log"}
print(cfg["level"])              # INFO
print(cfg.get("mode", "w"))      # w (default)
for k, v in cfg.items():
    print(k, "->", v)

#ENG: SET — unique elements; fast membership
#SR : SET — jedinstveni elementi; brzo članstvo
title("SET")
s = {1, 2, 2, 3}
s.add(3); s.add(4)
print(s)             # {1, 2, 3, 4}
print(2 in s)        # True

#ENG: STR vs BYTES — encode/decode
#SR : STR vs BYTES — enkodiranje/dekodiranje
title("STR vs BYTES")
s = "Ćevap"; b = s.encode("utf-8")
print(b)             # b'...'
print(b.decode("utf-8"))  # Ćevap

#ENG: PATHLIB — glob .py files (first 5)
#SR : PATHLIB — pronađi .py fajlove (prvih 5)
title("PATHLIB")
py_files = list(Path(".").glob("**/*.py"))[:5]
print([p.as_posix() for p in py_files])

#ENG: PREDICT EXERCISE — what prints?
#SR : VEŽBA PREDVIĐANJA — šta se ispisuje?
title("PREDICT")
a = [1,2]; b = a; a += [3]
print(a, b)          # [1,2,3] [1,2,3]  (deli isti objekat; mutacija)
c = (1,2); d = c + (3,)
print(c, d)          # (1,2) (1,2,3)    (novi tuple; imutabilno)
print({1,1,2,3} == {1,2,3})  # True

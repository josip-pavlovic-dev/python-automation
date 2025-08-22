#ENG: Run with "python -m scratch.day00_playground" from project root
#SR : Pokreni sa "python -m scratch.day00_playground" iz korena projekta

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


#ENG: Helpers
#SR : Pomoćne funkcije
def title(msg: str) -> None:
    print("\n" + "=" * 12, msg)


#ENG: Scalars: int, float, bool, str, None
#SR : Skalari: int, float, bool, str, None
def demo_scalars() -> None:
    title("SCALARS")
    n: int = 42
    x: float = 3.14
    ok: bool = True
    s: str = "Zdravo"
    nothing = None

    print(type(n), n)
    print(type(x), x)
    print(type(ok), ok)
    print(type(s), s)
    print(type(nothing), nothing)

    #ENG: f-string formatting
    #SR : f-string formatiranje
    print(f"n={n} x={x:.2f} ok={ok} s='{s}' none={nothing}")


#ENG: Truthiness for basic values
#SR : Truthiness za osnovne vrednosti
def demo_truthiness() -> None:
    title("TRUTHINESS")
    values = [0, 0.0, "", [], {}, set(), None, [1], "tekst", 1]
    for v in values:
        print(f"value={repr(v):>8} -> bool={bool(v)}")


#ENG: Sequences: list & tuple; indexing, slicing, copying
#SR : Sekvence: list i tuple; indeksiranje, sečenje, kopiranje
def demo_sequences() -> None:
    title("SEQUENCES (list/tuple)")
    xs: list[int] = [10, 20, 30, 40, 50]
    tp: tuple[int, int, int] = (1, 2, 3)
    print("xs:", xs, "len:", len(xs))
    print("tp:", tp, "len:", len(tp))

    print("xs[0], xs[-1]:", xs[0], xs[-1])
    print("xs[1:4] (stop exclusive):", xs[1:4])
    print("xs[:3], xs[3:]:", xs[:3], xs[3:])

    #ENG: list is mutable; tuple is immutable
    #SR : list je mutabilan; tuple je imutabilan
    before_id = id(xs)
    xs += [60]          # mutation in-place
    after_id = id(xs)
    print("xs mutated:", xs, "same_object:", before_id == after_id)
    print("tuple + (4,) creates new object:", tp + (4,))

    #ENG: unpacking + starred
    #SR : raspakivanje + zvezdica
    a, b, *rest = xs
    print("unpack -> a,b,*rest:", a, b, rest)


#ENG: Sets (unique, no order) and set ops
#SR : Setovi (jedinstveno, bez poretka) i operacije
def demo_sets() -> None:
    title("SETS")
    s1 = {1, 2, 2, 3}
    s2 = {3, 4}
    print("s1 (dedup):", s1)
    print("union:", s1 | s2)
    print("intersection:", s1 & s2)
    print("difference:", s1 - s2)
    print("membership 2 in s1:", 2 in s1)


#ENG: Dicts (mapping) + safe access + comprehensions
#SR : Rečnici (mapiranja) + bezbedan pristup + komprehencije
def demo_dicts() -> None:
    title("DICTS")
    cfg: dict[str, Any] = {"level": "INFO", "file": "app.log"}
    print("cfg:", cfg)
    print("get existing:", cfg.get("level"))
    print("get missing with default:", cfg.get("mode", "w"))
    cfg.setdefault("retries", 3)
    print("after setdefault:", cfg)

    #ENG: dict comprehension
    #SR : dict komprehencija
    nums = [1, 2, 3, 4]
    sq = {n: n * n for n in nums}
    print("squares:", sq)

    #ENG: iterate items
    #SR : iteracija preko items
    for k, v in cfg.items():
        print(f"  {k} -> {v}")


#ENG: Bytes vs str; encode/decode
#SR : Bajtovi vs string; enkodiranje/dekodiranje
def demo_bytes() -> None:
    title("BYTES vs STR")
    s = "Ćevap"
    b = s.encode("utf-8")
    print("str:", s, "| bytes:", b)
    print("decode:", b.decode("utf-8"))


#ENG: File I/O – text
#SR : Rad sa fajlovima – tekst
def demo_file_io_text(base: Path) -> None:
    title("FILE I/O (TEXT)")
    txt = base / "hello.txt"
    with open(txt, "w", encoding="utf-8") as f:
        f.write("Zdravo, fajl!\n")
        f.write("Druga linija\n")
    with open(txt, encoding="utf-8") as f:
        print("read:", f.read().strip())


#ENG: File I/O – JSON
#SR : Rad sa fajlovima – JSON
def demo_file_io_json(base: Path) -> None:
    title("FILE I/O (JSON)")
    data = {"user": "Ana", "age": 28, "tags": ["py", "automation"]}
    js = base / "user.json"
    with open(js, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(js, encoding="utf-8") as f:
        loaded = json.load(f)
    print("json loaded:", loaded)


#ENG: File I/O – CSV (DictWriter/DictReader)
#SR : Rad sa fajlovima – CSV (DictWriter/DictReader)
def demo_file_io_csv(base: Path) -> None:
    title("FILE I/O (CSV)")
    rows = [
        {"name": "Ana", "score": 91},
        {"name": "Boris", "score": 85},
        {"name": "Ceca", "score": 100},
    ]
    csv_path = base / "scores.csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "score"])
        w.writeheader()
        w.writerows(rows)

    with open(csv_path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        loaded = list(r)
    print("csv loaded:", loaded)


#ENG: Iteration helpers: range & enumerate
#SR : Pomoćnici za iteraciju: range i enumerate
def demo_range_enumerate() -> None:
    title("RANGE & ENUMERATE")
    print("range(5):", list(range(5)))
    print("range(3, 0, -1):", list(range(3, 0, -1)))  # stop je ekskluzivan
    for i, ch in enumerate(["a", "b", "c"], start=1):
        print(f"{i}: {ch}")


#ENG: Small validation use-case combining pieces
#SR : Mali primer validacije koji kombinuje sve gore
def demo_validation_case() -> None:
    title("MINI VALIDATION CASE")
    form = {"name": "Ana", "email": "", "age": 0}
    empties = [k for k, v in form.items() if not v]
    if empties:
        print("Empty fields:", empties)
    else:
        print("All good.")


def main() -> None:
    #ENG: Create a temp workspace next to this file
    #SR : Napravi privremeni radni folder pored ovog fajla
    base = Path(__file__).resolve().parent / "_tmp_day00"
    base.mkdir(parents=True, exist_ok=True)
    print(f"Workspace: {base}")

    demo_scalars()
    demo_truthiness()
    demo_sequences()
    demo_sets()
    demo_dicts()
    demo_bytes()
    demo_range_enumerate()
    demo_file_io_text(base)
    demo_file_io_json(base)
    demo_file_io_csv(base)
    demo_validation_case()

    print("\nDone. Pogledaj generisane fajlove u:", base)


if __name__ == "__main__":
    main()

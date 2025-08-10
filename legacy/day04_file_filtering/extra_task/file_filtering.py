from pathlib import Path
from datetime import datetime


def main() -> None:
    print("📂 Polazni direktorijum je jedan nivo iznad skripte: \n")
    base_dir = (Path(__file__).parents[1]).resolve()
    print(f"[🔍] Skeniram: {base_dir}")

    # ========== 1) SVI FAJLOVI iz base_dir (rekurzivno) ==========
    all_files = [p for p in base_dir.rglob("*") if p.is_file()]
    print("📂 Svi fajlovi (rekurzivno):")
    for p in all_files:
        print(p)
    print(f"Ukupno fajlova: {len(all_files)}")

    # ========== 2) Fajlovi samo iz base_dir (bez rekurzije) ==========
    top_level_files = [p for p in base_dir.glob("*") if p.is_file()]
    print("\n📁 Fajlovi samo iz trenutnog foldera (bez rekurzije):")
    for p in top_level_files:
        print(p)
    print(f"Ukupno fajlova u trenutnom folderu: {len(top_level_files)}")

    # ========== Upis u tekstualni fajl ==========
    out_path = (Path(__file__).parents[0] / "file_filtering_output.txt").resolve()
    print(f"\n✅ Rezultat će biti sačuvan u: {out_path}")
    with out_path.open("w", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"# Rezultat filtriranja fajlova\n")
        f.write(f"# Baza: {base_dir}\n")
        f.write(f"# Generisano: {timestamp}\n\n")

        f.write("📂 Svi fajlovi (rekurzivno):\n")
        for p in all_files:
            f.write(f"{p}\n")
        f.write(f"\nUkupno fajlova: {len(all_files)}\n\n")
        f.write("\n📁 Fajlovi samo iz trenutnog foldera (bez rekurzije):\n")
        for p in top_level_files:
            f.write(f"{p}\n")
        f.write(f"\nUkupno fajlova u trenutnom folderu: {len(top_level_files)}\n")

    print(f"\n✅ Rezultat sačuvan u: {out_path}")


if __name__ == "__main__":
    main()
# file_filtering.py
# Ovaj skript filtrira fajlove u direktorijumu jedan nivo iznad skripte i njegovim poddirektorijumima.
# Prikazuje sve fajlove, .py fajlove, .md fajlove i fajlove drugih tipova.
# Rezultat se upisuje u file_filtering_output.txt u istom direktorijumu kao skript.

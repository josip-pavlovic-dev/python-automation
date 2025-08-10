from pathlib import Path
from datetime import datetime


def main() -> None:
    # Polazni direktorijum jedan nivo iznad skripta
    base_dir = (Path(__file__).resolve().parent / "..").resolve()
    print(f"[🔍] Skeniram: {base_dir}")

    # 1) Pronađi .md i .py fajlove (rekurzivno)
    md_files = [p for p in base_dir.rglob("*.md") if p.is_file()]
    py_files = [p for p in base_dir.rglob("*.py") if p.is_file()]

    # 2) Upis rezultata
    out_path = (Path(__file__).resolve().parent / "file_filtering_output.txt").resolve()
    print(f"[💾] Upisujem rezultate u: {out_path}")
    with out_path.open("w", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("# Rezultat filtriranja fajlova\n")
        f.write(f"# Baza: {base_dir}\n")
        f.write(f"# Generisano: {timestamp}\n\n")

        # PY fajlovi
        f.write(f"=== PYTHON FILES ({len(py_files)}) ===\n")
        if py_files:
            for p in py_files:
                f.write(f"{p.relative_to(base_dir)}\n")
        else:
            f.write("Nema pronađenih .py fajlova.\n")

        # MD fajlovi
        f.write(f"\n=== MARKDOWN FILES ({len(md_files)}) ===\n")
        if md_files:
            for p in md_files:
                f.write(f"{p.relative_to(base_dir)}\n")
        else:
            f.write("Nema pronađenih .md fajlova.\n")

        f.write("\n" + "=" * 40 + "\n")

    print(f"\n✅ Rezultat sačuvan u: {out_path}")


if __name__ == "__main__":
    main()

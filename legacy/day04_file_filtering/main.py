from datetime import datetime
from pathlib import Path

# 🗂️ Podešavanje osnovnih putanja
base_dir = Path(__file__).resolve().parent
output_file = base_dir / "file_filtering_output.txt"

# 🎯 Filteri
size_threshold = 1_000  # minimalna veličina u bajtovima (1 KB)
days_threshold = 7  # stariji fajlovi od 7 dana se ignorišu


# 📝 Funkcija za formatiranje informacija o fajlu
def file_info(file_path: Path) -> str:
    size = file_path.stat().st_size
    modified_time = datetime.fromtimestamp(file_path.stat().st_mtime)
    return f"{file_path.name} | {size} B | Last modified: {modified_time.strftime('%Y-%m-%d %H:%M:%S')}"


# 🔍 Pretraga svih fajlova
all_files = list(base_dir.rglob("*.*"))

# 🧹 Filtriranje fajlova po veličini i datumu
filtered_files = [
    f
    for f in all_files
    if f.stat().st_size >= size_threshold
    and (datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)).days
    <= days_threshold
]

# 📑 Razdvajanje po tipu fajla
py_files = [f for f in filtered_files if f.suffix == ".py"]
md_files = [f for f in filtered_files if f.suffix == ".md"]
other_files = [f for f in filtered_files if f.suffix not in [".py", ".md"]]

# 💾 Upis u fajl
with open(output_file, "w", encoding="utf-8") as out:
    out.write("=== 📄 Python files (.py) ===\n")
    for f in py_files:
        out.write(file_info(f) + "\n")

    out.write("\n=== 📝 Markdown files (.md) ===\n")
    for f in md_files:
        out.write(file_info(f) + "\n")

    out.write("\n=== 📦 Other files ===\n")
    for f in other_files:
        out.write(file_info(f) + "\n")

print(f"✅ File filtering complete! Results saved to: {output_file}")
# ✅ Kraj koda

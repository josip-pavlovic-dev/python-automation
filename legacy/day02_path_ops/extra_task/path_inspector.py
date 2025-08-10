import os

# ℹ️ Absolute path to this script | _Apsolutna putanja do ove skripte_
script_path = os.path.abspath(__file__)
print(f"Script absolute path: {script_path}")

# ℹ️ Script name | _Ime skripte_
script_name = os.path.basename(script_path)
print(f"Script name: {script_name}")

# ℹ️ Directory containing this script | _Folder u kom se nalazi ova skripta_
base_dir = os.path.dirname(script_path)
print(f"Script directory: {base_dir}")

# ℹ️ Going 3 levels up to reach the project root | _Idemo tri nivoa iznad do root foldera projekta_
project_root = os.path.abspath(os.path.join(base_dir, "..", "..", ".."))
print(f"Project root path: {project_root}")

# ℹ️ Construct absolute path to SVG image inside assets/ | _Kreiramo apsolutnu putanju do slike u assets/ folderu_
svg_filename = "agent_mode_active.svg"
svg_path_abs = os.path.join(project_root, "assets", svg_filename)
print(f"Absolute path to SVG: {svg_path_abs}")

# ℹ️ Calculate relative path from current script to target file | _Relativna putanja od skripte do SVG fajla_
svg_path_rel = os.path.relpath(svg_path_abs, start=base_dir)
print(f"Relative path to SVG: {svg_path_rel}")

# ✅ Check if file exists | _Provera da li fajl postoji_
if os.path.exists(svg_path_abs):
    print("✅ File exists.")
else:
    print("❌ File not found!")

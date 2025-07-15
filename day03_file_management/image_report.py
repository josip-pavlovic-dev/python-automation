import os
from PIL import Image
import csv

# 📂 Putanja do foldera sa slikama / Path to the image folder
IMAGE_FOLDER = os.path.join("test_folder", "images")

# 📝 Putanja do CSV fajla izveštaja / Path to the output CSV report file
REPORT_FILE = os.path.join("test_folder", "image_report.csv")


# 🔍 Ekstrahuje informacije iz jedne slike / Extracts metadata from a single image
def get_image_info(image_path):
    with Image.open(image_path) as img:
        return {
            "filename": os.path.basename(image_path),
            "format": img.format,
            "size": os.path.getsize(image_path),
            "dimensions": f"{img.width}x{img.height}"
        }


# 📸 Skenira sve slike u datom folderu / Scans all images in the given folder
def scan_images(folder_path):
    image_data = []

    if not os.path.exists(folder_path):
        print(f"[WARN] Folder ne postoji / Folder does not exist: {folder_path}")
        return image_data

    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)

        # Filtrira slike po ekstenzijama / Filters images by extension
        if os.path.isfile(path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                image_data.append(get_image_info(path))
                print(f"[OK] {filename} obrađen / processed.")
            except Exception as e:
                print(f"[ERROR] {filename}: {e}")
    return image_data


# 💾 Upisuje podatke u CSV fajl / Writes metadata to a CSV file
def write_csv(report_data, output_path):
    with open(output_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["filename", "format", "size", "dimensions"])
        writer.writeheader()
        writer.writerows(report_data)


# 🚀 Glavni deo programa / Entry point
if __name__ == "__main__":
    print(f"[INFO] Skeniram folder: {IMAGE_FOLDER}")
    images = scan_images(IMAGE_FOLDER)
    write_csv(images, REPORT_FILE)
    print(f"[INFO] Izveštaj sačuvan u / Report saved to: {REPORT_FILE}")
# 📊 Izveštaj o slikama uspešno generisan! / Image report successfully generated!

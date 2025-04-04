"""Views"""

import csv
import numpy as np
from PIL import Image

# pip install numpy


def main():
    """Main code"""
    with open("views.csv", "r", encoding="utf-8") as file, \
         open("analysis.scv", "w", encoding="utf-8", newline="") as analysis:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])  # type: ignore
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)

        # for row in reader:
        #     brightness = calculate_brightness(f"6shorts/{row['id']}.jpeg")
        #     writer.writerow(
        #         {
        #             "id": row["id"],
        #             "english_title": row["english_title"],
        #             "japanese_title": row["japanese_title"],
        #             "brightness": round(brightness, 2),
        #         }
        #     )


def calculate_brightness(filename):
    """Returns overall brightness"""
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()

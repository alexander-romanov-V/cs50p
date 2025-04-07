"""CS50 P-Shirt"""

import os
import sys
from PIL import Image
from PIL import ImageOps


def main():
    """Main code"""
    shirt_f_name = "shirt.png"
    in_f_name, out_f_name = check_arguments(sys.argv)
    try:
        try_tshirt(shirt_f_name, in_f_name, out_f_name)
    except (FileNotFoundError, TypeError):
        sys.exit("Input does not exist")


def check_arguments(argv):
    """Checks arguments - must be exactly two different *.jpg|jpeg|png files"""
    extentions = [".jpg", ".jpeg", ".png"]
    argc = len(argv)
    if argc < 3:
        sys.exit("Too few command-line argumens")
    if argc > 3:
        sys.exit("Too many command-line argumens")
    ext = ["", ""]
    for i in range(1, 3):
        ext[i - 1] = os.path.splitext(argv[i])[1].lower()
        if ext[i - 1] not in extentions:
            sys.exit("Invalid Input")
    if ext[0] != ext[1]:
        sys.exit("Input and output have different extensions")
    return argv[1], argv[2]


def try_tshirt(shirt_f_name, in_f_name, out_f_name):
    """Combine shirt_f_name and in_f_name into out_f_name (jpg|jpeg|png)"""
    with Image.open(shirt_f_name) as shirt_img, \
         Image.open(in_f_name) as in_img:
        in_img = ImageOps.fit(in_img, shirt_img.size)
        in_img.paste(shirt_img, shirt_img)
        in_img.save(out_f_name)


if __name__ == "__main__":
    main()

from PIL import Image
import os, sys
import glob

root_dir = "D:/sample/folder/"
resize_ratio = 0.5  # where 0.5 is half size, 2 is double size

for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    image = Image.open(filename)

    new_image_height = int(image.size[0] / (1 / resize_ratio))
    new_image_length = int(image.size[1] / (1 / resize_ratio))

    image = image.resize((new_image_height, new_image_length), Image.ANTIALIAS)
    image.save(filename , 'JPEG', quality=80)

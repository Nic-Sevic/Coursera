#!/usr/bin/env python3

import os
from PIL import Image

path = "supplier-data/images"

for image in os.listdir(path):
  print(image)
  if image == "LICENSE" or image == "README":
    continue  
  # Size: Change image resolution from 3000x2000 to 600x400 pixel
  with Image.open(os.path.join(path, image)) as img:
    img = img.resize((600, 400))

    # Change image format from .TIFF to .JPEG
    img = img.convert("RGB")
    # Save with new extension name
    img.save(os.path.join(path, image.split(".")[0] + ".jpeg"), "JPEG")

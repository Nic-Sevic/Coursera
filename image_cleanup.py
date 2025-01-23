#!/usr/bin/env python3
# This script will take an image file, rotate it 90 degrees counter-clockwise, resize it to 128x128 pixels, and convert it to .jpeg format.
# The script will then save the image to the /opt/icons/ directory.
# To run this script, you will need to have the Python Imaging Library installed. You can install it with the following command: pip3 install pillow
# You can run the script with the following command: ls <image dir> | xargs -I {} ./image_cleanup.py {} 

import os, sys
import traceback
from PIL import Image

# make sure the directory exists
if not os.path.exists("/opt/icons/"):
    os.makedirs("/opt/icons/")

for infile in sys.argv[1:]: 
    im = Image.open(infile)
    
    # Rotate an image from -90%
    try:
        im = im.rotate(-90) # degrees counter-clockwise
    except OSError:
        print(f"Unable to rotate file {infile}")
        traceback.print_exc()
    
    # Resize from 192x192 to 128x128
    try: 
        im = im.resize((128, 128))
    except OSError:
        print(f"Unable to resize file {infile}")
        traceback.print_exc()

    # Convert from .tiff to .jpeg 
    # outfile = os.path.basename(infile) + ".jpeg"
    try:
      im = im.convert('RGB')
      im.save("/opt/icons/" + os.path.basename(infile), "JPEG")
    except OSError:
        print(f"Unable to convert file {infile}")
        traceback.print_exc()

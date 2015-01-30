# -*- coding: utf-8 -*-

import os.path
import glob
from PIL import Image

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(file + ".gif")

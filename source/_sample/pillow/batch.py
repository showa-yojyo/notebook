# -*- coding: utf-8 -*-
import os.path
import glob
from PIL import Image

for infile in glob.glob("*.gif"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(file + ".png")

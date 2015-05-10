#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gradient3.py: Demonstrate drawing linear gradient on an image.
"""
from PIL import Image, ImageColor
import os.path

WORK_SIZE = 0x100
SOURCE_PATH = os.path.join(
    os.path.dirname(__file__), '../../_static/illvelo.png')

img = Image.open(source_path)
assert img.mode == 'RGBA'

gradient = Image.new('L', (1, WORK_SIZE))
for i in range(WORK_SIZE):
    gradient.putpixel((0, i), i)

alpha = gradient.resize(img.size, Image.ANTIALIAS)

final = Image.new('RGBA', img.size, (0, 0, 0, 0))
final.paste(img, None, mask=alpha)

# -*- coding: utf-8 -*-
"""gradient3.py: Demonstrate drawing linear gradient on an image.
"""
from PIL import Image, ImageColor

WORK_SIZE = 0x100

img = Image.open('illvelo.png')
assert img.mode == 'RGBA'

gradient = Image.new('L', (1, WORK_SIZE))
for i in range(WORK_SIZE):
    gradient.putpixel((0, i), i)

alpha = gradient.resize(img.size, Image.ANTIALIAS)

final = Image.new('RGBA', img.size, (0, 0, 0, 0))
final.paste(img, None, mask=alpha)

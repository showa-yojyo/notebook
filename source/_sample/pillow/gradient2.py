# -*- coding: utf-8 -*-
"""gradient2.py: Demonstrate drawing linear gradient.
"""
from PIL import Image

BASE_COLOR = 'red'
IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
WORK_SIZE = 0x100

img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), BASE_COLOR)
gradient = Image.new('L', (1, WORK_SIZE))

for i in range(WORK_SIZE):
    gradient.putpixel((0, i), WORK_SIZE - i)

img.putalpha(gradient.resize(img.size))

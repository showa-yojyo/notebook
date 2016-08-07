#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""text1.py: Demonstrate how to draw a text with PIL.
"""
from PIL import (Image, ImageDraw)

IMAGE_SIZE = (96, 24)
BKGND_COLOR = 'black'
TEXT_COLOR = 'white'

img = Image.new('RGBA', IMAGE_SIZE, BKGND_COLOR)
draw = ImageDraw.Draw(img)
draw.text((0, 0), 'Hello, world', fill=TEXT_COLOR)
img.show()

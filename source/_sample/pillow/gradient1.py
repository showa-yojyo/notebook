#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""gradient1.py: Demonstrate drawing linear gradient.
"""
from PIL import (Image, ImageColor)
import numpy as np

COLOR_START = ImageColor.getrgb('antiquewhite')
COLOR_STOP = ImageColor.getrgb('deeppink')
IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
WORK_SIZE = 0x100

img = Image.new('RGB', (1, WORK_SIZE))
gradient = np.array(
    [np.linspace(i, j, WORK_SIZE) for i, j in zip(COLOR_START, COLOR_STOP)],
    dtype=int)

for i, rgb in enumerate(gradient.T):
    img.putpixel((0, i), tuple(rgb))

img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
img.show()

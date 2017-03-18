#!/usr/bin/env python
"""gradient4.py: Demonstrate drawing radial gradient.
"""
from PIL import (Image, ImageColor, ImageDraw)
import numpy as np

COLOR_START = ImageColor.getrgb('antiquewhite')
COLOR_STOP = ImageColor.getrgb('deeppink')
WORK_SIZE = 0x100

img = Image.new('RGB', (WORK_SIZE, WORK_SIZE), color='white')
draw = ImageDraw.Draw(img)

gradient = np.array(
    [np.linspace(i, j, WORK_SIZE) for i, j in zip(COLOR_START, COLOR_STOP)],
    dtype=int)
for i, rgb in enumerate(gradient.T):
    draw.ellipse([i, i, WORK_SIZE - i, WORK_SIZE - i], fill=tuple(rgb))

img.show()

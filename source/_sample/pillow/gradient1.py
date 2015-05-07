# -*- coding: utf-8 -*-
from PIL import Image, ImageColor
import numpy as np

COLOR_START = ImageColor.getrgb('antiquewhite')
COLOR_STOP = ImageColor.getrgb('deeppink')
IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
WORK_SIZE = 0x100
R, G, B = 0, 1, 2

img = Image.new('RGB', (1, WORK_SIZE))
colors = np.dstack(
    (np.linspace(COLOR_START[i], COLOR_STOP[i], num=WORK_SIZE) for i in (R, G, B)))[0]

for i, color in enumerate(colors):
    img.putpixel((0, i), tuple(color.astype(int).tolist()))

img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))

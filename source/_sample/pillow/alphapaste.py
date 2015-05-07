# -*- coding: utf-8 -*-
from PIL import Image

# Photoshop で言うところのレイヤー 1 に置く画像。
img = Image.open('illvelo.png')
bands = img.split()

# R, G, B, A の A だけが要る。
alpha = bands[3]

# Photoshop で言うところの背景レイヤーになる画像。
bkgnd = Image.new('RGBA', img.size, 'blue')

# これではダメ。
#bkgnd.paste(img, None)
# これが正解。
bkgnd.paste(img, None, mask=alpha)

# -*- coding: utf-8 -*-

from PIL import Image

img = Image.open('illvelo.png')
assert img.mode == 'RGBA'

bands = img.getbands()
assert bands[0] == 'R'
assert bands[1] == 'G'
assert bands[2] == 'B'
assert bands[3] == 'A'

# R, G, B, A チャンネルを抽出する。
data = img.split()

#data[0].save('illvelo-r.png')
#data[1].save('illvelo-g.png')
#data[2].save('illvelo-b.png')

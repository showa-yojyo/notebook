# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (1024, 256), 'black')
dr = ImageDraw.Draw(img)
fnt = ImageFont.truetype('hgrme.ttc', 24, encoding='utf-8')

text = '''どうしても会ってもらえませんか？
私はこんなにあなたに会いたいのに…。
お金には余裕があるので心配しないで
ください。
コード780の1102番で、
あなたを待っています。
'''

width = 0
height = 0
for line in text.splitlines():
    ext = dr.textsize(line, fnt)
    dr.text((0, height), line, font=fnt, fill='white')
    width = max(ext[0], width)
    height += ext[1]

# 余白をトリムする。
img = img.crop((0, 0, width, height))
img.show()
#img.save('karous-paradise.png')

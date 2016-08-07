#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""text2.py: Demonstrate how to draw multi-line text using ImageFont.
"""
from PIL import (Image, ImageDraw, ImageFont)

TEXT = '''どうしても会ってもらえませんか？
私はこんなにあなたに会いたいのに…。
お金には余裕があるので心配しないで
ください。
コード780の1102番で、
あなたを待っています。
'''

TEXT_COLOR = 'white'
BKGND_COLOR = 'black'
FONT = ImageFont.truetype('HGRME.TTC', 24, encoding='utf-8')

img = Image.new('RGB', (1024, 256), BKGND_COLOR)
draw = ImageDraw.Draw(img)

width = 0
height = 0
for line in TEXT.splitlines():
    draw.text((0, height), line, font=FONT, fill=TEXT_COLOR)

    ext = draw.textsize(line, FONT)
    width = max(ext[0], width)
    height += ext[1]

# Trim extra margin of right and bottom.
final = img.crop((0, 0, width, height))
final.show()

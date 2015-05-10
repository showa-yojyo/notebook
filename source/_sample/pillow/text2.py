#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""text2.py: Demonstrate how to draw multi-line text using ImageFont.
"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.new('RGB', (1024, 256), 'black')
dr = ImageDraw.Draw(img)
fnt = ImageFont.truetype('HGRME.TTC', 24, encoding='utf-8')

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
    dr.text((0, height), line, font=fnt, fill='white')

    ext = dr.textsize(line, fnt)
    width = max(ext[0], width)
    height += ext[1]

# Trim extra margin of right and bottom.
img = img.crop((0, 0, width, height))

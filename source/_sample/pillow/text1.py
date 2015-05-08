# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

IMAGE_WIDTH, IMAGE_HEIGHT = 96, 24
TEXT_COLOR = 'white'

# デフォルト背景色のキャンヴァスを用意する。
img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT), 'black')

# Draw 関数でオブジェクトを作成。
draw = ImageDraw.Draw(img)

# 画面の左上隅にテキストを描画する。
draw.text((0, 0), 'Hello, world', fill=TEXT_COLOR)

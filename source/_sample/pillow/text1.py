# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

IMAGE_WIDTH, IMAGE_HEIGHT = 320, 240
TEXT_COLOR = 'red'

# デフォルト背景色のキャンヴァスを用意する。
img = Image.new('RGBA', (IMAGE_WIDTH, IMAGE_HEIGHT))

# Draw 関数でオブジェクトを作成。
draw = ImageDraw.Draw(img)

# 画面の左上隅にテキストを赤く描画する。
draw.text((0, 0), 'Hello, world', fill=TEXT_COLOR)

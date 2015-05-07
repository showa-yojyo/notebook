# -*- coding: utf-8 -*-
from PIL import Image, ImageGrab

# スクリーンショットをキャプチャーして
img = ImageGrab.grab()
# テキトーに縮小、表示する。
img.thumbnail((256, 256), Image.ANTIALIAS)

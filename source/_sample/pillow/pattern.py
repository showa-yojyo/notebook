# -*- coding: utf-8 -*-
import sys
from PIL import Image

def run():
    src = Image.open('illvelo.png')
    #print("format, size, mode: %r %r %r" % (src.format, src.size, src.mode))

    newsize = src.size[:]
    #newsize = [i // 3 for i in src.size]
    src = src.resize(newsize, Image.ANTIALIAS)

    target = swap_quadrants(src)

    # 最後にオリジナル画像を重ねがけ。
    #target.paste(src, (0, 0, src.size[0], src.size[1]), mask=src.split()[3])
    mypaste(src, (0, 0, src.size[0], src.size[1]), target, 0x10)

    target.save('illvelo-wallpaper.png')

def swap_quadrants(img):
    """オリジナル画像を縦横に四分割する。
    オリジナル画像と同サイズのキャンバスを用意し、
    対角線上の region[i] を入れ替えた上でコピーする。
    """
    # (L, U, R, B), LU = (0, 0)
    W = img.size[0] // 2
    H = img.size[1] // 2

    boxes = list()
    boxes.append((0, 0, W, H))
    boxes.append((W, 0, img.size[0], H))
    boxes.append((0, H, W, img.size[1]))
    boxes.append((W, H, img.size[0], img.size[1]))

    regions = [img.crop(box) for box in boxes]

    target = Image.new(img.mode, img.size)

    wc = img.size[0] - W
    hc = img.size[1] - H
    opacity = 0x80
    mypaste(regions[3], (0, 0, wc, hc), target, opacity)
    mypaste(regions[2], (wc, 0, img.size[0], hc), target, opacity)
    mypaste(regions[1], (0, hc, wc, img.size[1]), target, opacity)
    mypaste(regions[0], (wc, hc, img.size[0], img.size[1]), target, opacity)

    return target

def mypaste(region, box, target, opacity):
    mask = Image.new('L', (box[2] - box[0], box[3] - box[1]), 0x80)
    target.paste(region, box, mask=mask)

if __name__ == '__main__':
    run()

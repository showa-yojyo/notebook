# -*- coding: utf-8 -*-
from PIL import Image

def run(filepath):
    """TBW"""

    src = Image.open(filepath)
    target = swap_quadrants(src)
    paste_with_alpha(target, src, (0, 0, src.size[0], src.size[1]), 0x10)
    return target

def swap_quadrants(img):
    """オリジナル画像を縦横に四分割する。
    オリジナル画像と同サイズのキャンバスを用意し、
    対角線上の region[i] を入れ替えた上でコピーする。
    """

    W = img.size[0] // 2
    H = img.size[1] // 2

    # box := (L, U, R, B)
    boxes = make_boxes(img, W, H)

    regions = [img.crop(box) for box in boxes]

    target = img.copy()
    region_boxes = make_boxes(
        img, img.size[0] - W, img.size[1] - H)

    for i in range(4):
        paste_with_alpha(target, regions[3 - i], region_boxes[i], 0x80)

    return target

def paste_with_alpha(target, source, box, opacity):
    """TBW"""

    mask = Image.new('L', (box[2] - box[0], box[3] - box[1]), 0x80)
    target.paste(source, box, mask=mask)

def make_boxes(img, width, height):
    """TBW"""

    return [
        (0, 0, width, height),
        (width, 0, img.size[0], height),
        (0, height, width, img.size[1]),
        (width, height, img.size[0], img.size[1]),]

if __name__ == '__main__':
    run('illvelo.png')

#!/usr/bin/env python
"""pattern.py: An example like <Rolling an image> in Pillow document.
"""
import os.path
from PIL import Image

def run(filepath):
    """Create a wallpaper image from a PNG file."""

    src = Image.open(filepath)
    target = swap_quadrants(src)
    paste_with_alpha(target, src, (0, 0), 0x10)
    return target

def swap_quadrants(img):
    """Quarter the image and swap two diagonal quadrant pairs."""

    boxes = quarter_bbox(img)
    regions = [img.crop(box) for box in boxes]

    target = img.copy()
    paste_with_alpha(target, regions[3], (0, 0), 0x80)
    paste_with_alpha(target, regions[2], (regions[3].size[0], 0), 0x80)
    paste_with_alpha(target, regions[1], (0, regions[3].size[1]), 0x80)
    paste_with_alpha(target, regions[0], regions[3].size, 0x80)

    return target

def paste_with_alpha(target, source, left_upper, opacity):
    """An alpha_composite-like operation."""

    mask = Image.new('L', source.size, opacity)
    target.paste(source, left_upper, mask=mask)

def quarter_bbox(img):
    """Quarter the bounding box of an image."""

    (left, upper, right, bottom) = img.getbbox()
    xmid = (left + right - 1) // 2
    ymid = (upper + bottom - 1) // 2

    # Z
    return [
        (left, upper, xmid, ymid),
        (xmid + 1, upper, right, ymid),
        (left, ymid + 1, xmid, bottom),
        (xmid + 1, ymid + 1, right, bottom),]

if __name__ == '__main__':
    result = run(os.path.join(
        os.path.dirname(__file__), '../../_images/illvelo.png'))
    result.show()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def draw_text(text, initsize=256, point=144, bgcolor='black', forecolor='white'):
    """Helper function."""

    # Create a larger canvas.
    img = Image.new('RGBA', (initsize, initsize), bgcolor)
    dr = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('HGRME.TTC', point)

    ext = dr.textsize(text, font=fnt)
    dr.text((0, 0), text, font=fnt, fill=forecolor)

    # (left, upper, right, lower)-tuple
    img = img.crop(
        (0, 0,
         ext[0], ext[1] + 16))

    # TODO: Use the power of two value that is the closest
    # to each component of img.size.
    return img.resize((initsize, initsize), Image.ANTIALIAS)

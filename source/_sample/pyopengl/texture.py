#!/usr/bin/env python
"""texture.py: Provide a helper function.
"""
from PIL import (Image, ImageDraw, ImageFont)

def draw_text(text, initsize=256, point=144, bgcolor='black', forecolor='white'):
    """Helper function."""

    # Create a larger canvas.
    img = Image.new('RGBA', (initsize, initsize), bgcolor)
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('HGRME.TTC', point)

    ext = draw.textsize(text, font=fnt)
    draw.text((0, 0), text, font=fnt, fill=forecolor)

    # (left, upper, right, lower)-tuple
    imgcr = img.crop(
        (0, 0,
         ext[0], ext[1] + 16))

    # TODO: Use the power of two value that is the closest
    # to each component of img.size.
    return imgcr.resize((initsize, initsize), Image.ANTIALIAS)

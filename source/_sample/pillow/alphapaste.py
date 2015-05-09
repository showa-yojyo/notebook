# -*- coding: utf-8 -*-
"""alphapaste.py: Demonstrate how to composite two images with alpha values.
"""
from PIL import Image

# Layer 1 in Photoshop.
img = Image.open('illvelo.png')

# Background layer in Photoshop.
bkgnd = Image.new('RGBA', img.size, 'blue')

# Blend images with the transparency mask from img.split()[3].
result = Image.alpha_composite(bkgnd, img)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""alphapaste.py: Demonstrate how to composite two images with alpha values.
"""
import os.path
from PIL import Image

SOURCE_PATH = os.path.join(
    os.path.dirname(__file__), '../../_static/illvelo.png')

# Layer 1 in Photoshop.
img = Image.open(SOURCE_PATH)

# Background layer in Photoshop.
bkgnd = Image.new('RGBA', img.size, 'blue')

# Blend images with the transparency mask from img.split()[3].
result = Image.alpha_composite(bkgnd, img)
result.show()

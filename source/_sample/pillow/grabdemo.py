#!/usr/bin/env python
"""grabdemo.py: Demonstrate how to use function ImageGrab.grab.
"""
from PIL import (Image, ImageGrab)

# Take a snapshot of the whole screen.
img = ImageGrab.grab()

# For the purpose of display, make it to a thumbnail.
img.thumbnail((256, 256), Image.ANTIALIAS)

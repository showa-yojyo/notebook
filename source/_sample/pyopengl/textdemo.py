#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""textdemo.py: Demonstrate how to use OpenGL texture (text)."""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
from texturedemo import TextureDemoApp
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image, ImageDraw, ImageFont

def draw_text(text, initsize=256, point=144, margin=4):
    """Helper function."""

    # Create a larger canvas.
    img = Image.new('RGBA', (initsize, initsize), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)

    fnt = ImageFont.truetype('hgrme.ttc', point)
    ext = dr.textsize(text, font=fnt)
    dr.text((margin, margin), text, font=fnt, fill='white')

    # TODO: Use the power of two value that is the closest
    # to each component of img.size.
    return img.crop(
        (margin, margin,
         ext[0] + margin * 3, ext[1] + margin * 3)
        ).resize((initsize, initsize), Image.ANTIALIAS)

class TextDemoApp(TextureDemoApp):
    """Demonstrate how to use OpenGL texture (text)."""

    def init_object(self):
        """Initialize the object to be displayed."""

        img = draw_text('潔')

        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1],
            0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        vx, vy = 5.0, 5.0

        vertices = (
            -vx, vy, 0.0,
            -vx, -vy, 0.0,
            vx, -vy, 0.0,
            vx, vy, 0.0,)

        texcoords = (
            0, 0,
            0, 1,
            1, 1,
            1, 0)

        colors = (
            1, 1, 1, 1,
            0.5, 0.5, 0.5, 1,
            0.5, 0.5, 0.5, 1,
            1, 1, 1, 1,)

        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glTexCoordPointer(2, GL_FLOAT, 0, texcoords)
        glColorPointer(4, GL_FLOAT, 0, colors)

    def do_render(self):
        """Render the object."""

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        gluLookAt(0.5, -9.5, 1.58,
                  0.5, 10.0, 1.58,
                  0, 0, 1)

        glPushAttrib(GL_ALL_ATTRIB_BITS)
        glPushClientAttrib(GL_CLIENT_ALL_ATTRIB_BITS)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glDrawArrays(GL_QUADS, 0, 4)

        glPopClientAttrib()
        glPopAttrib()
        glPopMatrix()

def main(args):
    """The main function."""

    app = TextDemoApp(
        window_title=b"Build texture from text",
        window_size=(320, 240))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

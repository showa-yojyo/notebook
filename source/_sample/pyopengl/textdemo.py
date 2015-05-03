#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""textdemo.py: Demonstrate how to use OpenGL texture with PIL."""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=invalid-name
import sys
from texturedemo import TextureDemoApp
import OpenGL.GL as GL
from texture import draw_text

class TextDemoApp(TextureDemoApp):
    """Demonstrate how to use OpenGL texture with PIL."""

    def init_object(self):
        """Initialize the object to be displayed."""

        vx, vy = (5.0, 5.0)

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

        GL.glVertexPointer(3, GL.GL_FLOAT, 0, vertices)
        GL.glTexCoordPointer(2, GL.GL_FLOAT, 0, texcoords)
        GL.glColorPointer(4, GL.GL_FLOAT, 0, colors)

    def init_texture(self):
        """Initialize textures."""

        img = draw_text('潔')

        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL.GL_RGBA,
            img.size[0], img.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img.tostring())

        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_CLAMP)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_CLAMP)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)

def main(args):
    """The main function."""

    app = TextDemoApp(
        window_title=b"Build texture from text",
        window_size=(320, 240),
        camera_eye=(0.5, -9.5, 1.58,),
        camera_center=(0.5, 10.0, 1.58,),
        camera_up=(0., 0., 1.))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

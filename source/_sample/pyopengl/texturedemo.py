#!/usr/bin/env python
"""texturedemo.py: Demonstrate how to use OpenGL texture with PIL."""
# pylint: disable=unused-argument, no-self-use, invalid-name
import sys
import os
import OpenGL.GL as GL
from PIL import Image
from deprecatedapp import DeprecatedApp

class TextureDemoApp(DeprecatedApp):
    """Demonstrate how to use OpenGL texture (bitmap)."""

    def __init__(self, **kwargs):
        """Initialize an instance of class TextureDemoApp."""

        kwargs['context_version'] = (1, 5)
        super(TextureDemoApp, self).__init__(**kwargs)

    def init_gl(self):
        """Initialize the OpenGL state."""

        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_TEXTURE_2D)

    def init_object(self):
        """Initialize the object to be displayed."""

        vx, vy = (40.0, 40.0)
        tx, ty = (6.0, 6.0)

        vertices = (
            -vx, -vy, 0.0,
            vx, -vy, 0.0,
            vx, vy, 0.0,
            -vx, vy, 0.0,)

        texcoords = (
            -tx, -ty,
            tx, -ty,
            tx, ty,
            -tx, ty,)

        colors = (
            0, 0, 0, 0.75,
            0, 0, 0, 0.75,
            1, 1, 1, 0.75,
            0, 0, 0, 0.75,)

        GL.glVertexPointer(3, GL.GL_FLOAT, 0, vertices)
        GL.glTexCoordPointer(2, GL.GL_FLOAT, 0, texcoords)
        GL.glColorPointer(4, GL.GL_FLOAT, 0, colors)

    def init_texture(self):
        """Initialize textures."""

        source_path = os.path.join(
            os.path.dirname(__file__), '../../_static/illvelo.png')
        img = Image.open(source_path).resize((256, 256))
        assert img.mode == 'RGBA'

        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL.GL_RGBA,
            img.size[0], img.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img.tobytes())

        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_NEAREST)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_NEAREST)
        GL.glTexEnvf(
            GL.GL_TEXTURE_ENV, GL.GL_TEXTURE_ENV_MODE, GL.GL_DECAL)

    def do_render(self):
        """Render the object."""

        GL.glPushAttrib(GL.GL_CURRENT_BIT)
        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glPushMatrix()
        self.set_modelview_matrix()

        GL.glPushClientAttrib(GL.GL_CLIENT_VERTEX_ARRAY_BIT)
        GL.glEnableClientState(GL.GL_VERTEX_ARRAY)
        GL.glEnableClientState(GL.GL_TEXTURE_COORD_ARRAY)
        GL.glEnableClientState(GL.GL_COLOR_ARRAY)

        GL.glDrawArrays(GL.GL_POLYGON, 0, 4)

        GL.glPopClientAttrib()
        GL.glPopAttrib()
        GL.glPopMatrix()

def main(args):
    """The main function."""

    app = TextureDemoApp(
        window_title=b"Build texture from a PNG file",
        window_size=(320, 240),
        camera_eye=(14, 14, 1.58,),
        camera_up=(0, 0, 1))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

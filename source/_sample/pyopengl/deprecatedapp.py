#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""deprecatedapp.py: Do not use.

References:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
  * OpenGLBook.com
    <http://openglbook.com/chapter-4-entering-the-third-dimension.html>
  * Tutorials for modern OpenGL (3.3+)
    <http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/>
"""
# pylint: disable=unused-argument, no-self-use
import sys
import numpy as np
import OpenGL.GL as GL
import OpenGL.GLU as GLU
from appbase import AppBase

class DeprecatedApp(AppBase):
    """The base class for classes that use some deprecated features
    of OpenGL 3.0.
    """

    def __init__(self, **kwargs):
        """Initialize an instance of class DeprecatedApp."""

        kwargs.setdefault('context_version', (2, 1))
        super(DeprecatedApp, self).__init__(**kwargs)

        self.rotation_matrix = np.identity(4)

    def init_program(self):
        """Setup shaders."""
        self.program_manager = None

    def get_shader_sources(self):
        """Return shader sources."""
        return {}

    def update_projection(self, fovy, width, height):
        """Update the projection matrix."""

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GLU.gluPerspective(fovy, width / height, self.znear, self.zfar)
        self.fovy = fovy

    def update_rotation(self, quat=None):
        """Update the model transform."""

        if quat is None:
            # Initial update.
            self.rotation_matrix = np.identity(4)
        else:
            self.quat = quat
            self.rotation_matrix[:3, :3] = quat.transform.transpose()

    def set_modelview_matrix(self):
        """Set the modelview matrix with deprecated GL commands."""

        GL.glLoadIdentity()
        GLU.gluLookAt(
            self.camera_eye[0], self.camera_eye[1], self.camera_eye[2],
            self.camera_center[0], self.camera_center[1], self.camera_center[2],
            self.camera_up[0], self.camera_up[1], self.camera_up[2])
        GL.glMultMatrixf(self.rotation_matrix)

def main(args):
    """The main function."""

    app = DeprecatedApp()
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

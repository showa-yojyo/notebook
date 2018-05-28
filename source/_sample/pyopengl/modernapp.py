#!/usr/bin/env python
"""glmodernapp.py: For OpenGL 3.x applications.

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
from appbase import AppBase
from program_manager import ProgramManager
from transform import (lookat, perspective)

class ModernApp(AppBase):
    """The base class for classes that never use deprecated features
    of OpenGL.
    """

    def __init__(self, **kwargs):
        """Initialize an instance of class ModernApp."""

        super(ModernApp, self).__init__(**kwargs)

    def init_program(self):
        """Setup shaders."""

        shader_sources = self.get_shader_sources()
        if not shader_sources:
            return

        self.program_manager = ProgramManager()
        self.program_manager.setup(shader_sources)

    def init_transform(self):
        """Initialize VM transforms."""

        self.update_rotation()

        camera_matrix = lookat(
            self.camera_eye, self.camera_center, self.camera_up)

        GL.glUniformMatrix4fv(
            GL.glGetUniformLocation(
                self.program_manager.program_id, b"camera"),
            1, GL.GL_TRUE,
            camera_matrix)

    def get_shader_sources(self):
        """Return shader sources."""
        return {}

    def update_projection(self, fovy, width, height):
        """Update the projection matrix."""

        if not self.program_manager:
            return

        if self.program_manager.program_id:
            GL.glUniformMatrix4fv(
                GL.glGetUniformLocation(
                    self.program_manager.program_id, b"projection"),
                1, GL.GL_TRUE,
                perspective(
                    fovy, width / height, self.znear, self.zfar))

        self.fovy = fovy

    def update_rotation(self, quat=None):
        """Update the model transform."""

        if not self.program_manager or not self.program_manager.program_id:
            return

        rotation_matrix = np.identity(4)
        if quat is not None:
            self.quat = quat
            rotation_matrix[:3, :3] = quat.transform

        GL.glUniformMatrix4fv(
            GL.glGetUniformLocation(
                self.program_manager.program_id, b"rotation"),
            1, GL.GL_TRUE,
            rotation_matrix)

    def cleanup(self):
        """The clean up callback function."""

        if self.program_manager:
            self.program_manager.cleanup()

def main(args):
    """The main function."""

    app = ModernApp()
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

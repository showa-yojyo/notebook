#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""viewnavigationdemo.py: Demonstrate zooming and rotation.

References:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
"""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from shaderdemo import ShaderDemoApp
from Quaternion import Quat
from transform import perspective
from viewnavigation import ViewRotate
from viewnavigation import ViewZoom

FRAG_SHADER_SOURCE = """
#version 330 core

in vec4 ex_Color;
out vec4 out_Color;

void main(void)
{
    out_Color = ex_Color;
}
"""

VERT_SHADER_SOURCE = """
#version 330 core

uniform mat4 camera;
uniform mat4 projection;
uniform mat4 rotation;

layout(location=0) in vec4 in_Position;
layout(location=1) in vec4 in_Color;

out vec4 ex_Color;

void main(void)
{
    gl_Position = projection * camera * rotation * in_Position;
    ex_Color = in_Color;
}
"""

class ViewNavigationDemoApp(ShaderDemoApp):
    """Implement zooming and rotation."""

    def __init__(self, **kwargs):
        """Initialize an instance of class ViewNavigationDemoApp."""

        super(ViewNavigationDemoApp, self).__init__(**kwargs)

        self.zoom_handler = None
        self.rotate_handler = None
        self.quat = Quat([0., 0., 0., 1.])
        self.fovy = 45.0

    def init_shader_source(self):
        """Initialize shader source."""

        self.shader_sources = {
            GL_VERTEX_SHADER: VERT_SHADER_SOURCE,
            GL_FRAGMENT_SHADER: FRAG_SHADER_SOURCE,}
        self.shader_ids = {}

    def init_object(self):
        """Initialize the object to be displayed."""

        super(ViewNavigationDemoApp, self).init_object()
        self.update_rotation()

    def mouse(self, button, state, x, y):
        """The mouse callback function."""

        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                self.rotate_handler = ViewRotate(self, x, y)
            elif state == GLUT_UP:
                self.rotate_handler = None

        if button == GLUT_RIGHT_BUTTON:
            if state == GLUT_DOWN:
                self.zoom_handler = ViewZoom(self, x, y)
            elif state == GLUT_UP:
                self.zoom_handler = None

    def motion(self, x, y):
        """The motion callback function."""

        update_scene = False
        for handler in (self.rotate_handler, self.zoom_handler):
            if handler and handler.update_mouse_position(x, y):
                update_scene = True

        if update_scene:
            glutPostRedisplay()

    def resize(self, width, height):
        """The reshape callback function."""
        if height == 0:
            return

        glViewport(0, 0, width, height)
        self.update_perspective(width, height)

    def update_perspective(self, width, height):
        """Set the projection matrix."""

        projection = perspective(self.fovy, width / height, 1.0, 100.0)
        proj_id = glGetUniformLocation(self.program_id, b"projection")
        glUniformMatrix4fv(proj_id, 1, GL_TRUE, projection)

    def update_rotation(self):
        """Update the model transform of shader object."""

        rotation_id = glGetUniformLocation(self.program_id, b"rotation")
        rotation_matrix = np.identity(4)
        rotation_matrix[:3, :3] = self.quat.transform
        glUniformMatrix4fv(rotation_id, 1, GL_TRUE, rotation_matrix)

def main(args):
    """The main function."""

    app = ViewNavigationDemoApp(window_title=b'View Navigation Demo')
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

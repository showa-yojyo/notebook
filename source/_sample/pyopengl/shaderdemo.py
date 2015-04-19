#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""shaderdemo.py: Demonstrate GLSL.

References:
  * rndblnch / opengl-programmable
    <http://bitbucket.org/rndblnch/opengl-programmable>
  * OpenGLBook.com
    <http://openglbook.com/chapter-4-entering-the-third-dimension.html>
  * Tutorials for modern OpenGL (3.3+)
    <http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/>
"""
# pylint: disable=unused-argument,no-self-use
# pylint: disable=wildcard-import,unused-wildcard-import
# pylint: disable=invalid-name
import sys
import colorsys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from ctypes import c_void_p
from glshaderappbase import GLShaderAppBase
from transform import lookat
from transform import perspective

VERT_SHADER_SOURCE = """
#version 330 core

uniform mat4 camera;
uniform mat4 projection;

layout(location=0) in vec4 in_Position;
layout(location=1) in vec4 in_Color;

out vec4 ex_Color;

void main(void)
{
    gl_Position = projection * camera * in_Position;
    ex_Color = in_Color;
}
"""

FRAG_SHADER_SOURCE = """
#version 330 core

in vec4 ex_Color;
out vec4 out_Color;

void main(void)
{
    out_Color = ex_Color;
}
"""

class ShaderDemoApp(GLShaderAppBase):
    """A GLSL demonstration."""

    def __init__(self, **kwargs):
        """Initialize an instance of class ShaderDemoApp."""

        kwargs.setdefault('context_version', (3, 1))
        super(ShaderDemoApp, self).__init__(**kwargs)

        self.buffer_id = 0
        self.index_buffer_id = 0
        self.num_triangles = 24

        self.vao_id = 0

    def init_shader_source(self):
        """Initialize shader source."""

        self.shader_sources = {
            GL_VERTEX_SHADER: VERT_SHADER_SOURCE,
            GL_FRAGMENT_SHADER: FRAG_SHADER_SOURCE,}
        self.shader_ids = {}

    def init_camera(self):
        """Initialize viewing transformation."""

        camera_matrix = lookat(
            np.array([2., 2., 2.]),
            np.array([0., 0., 0.]),
            np.array([0., 0., 1.]))

        camera_id = glGetUniformLocation(self.program_id, b"camera")
        glUniformMatrix4fv(camera_id, 1, GL_TRUE, camera_matrix)

    def init_object(self):
        """Initialize the object to be displayed."""

        self.init_camera()

        num_triangles = self.num_triangles
        vertices = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        for i in range(num_triangles):
            theta = 2 * np.pi * i / num_triangles
            pos = np.array([np.cos(theta), np.sin(theta), 1.0, 1.0])
            color = colorsys.hsv_to_rgb(i / num_triangles, 1.0, 1.0)
            vertices = np.hstack((vertices, pos, color, [1.0]))

        vertices = vertices.astype(np.float32)
        indices = np.hstack((range(num_triangles + 1), 1)).astype(np.uint8)

        self.vao_id = glGenVertexArrays(1)
        glBindVertexArray(self.vao_id)

        # Create buffer objects data.
        self.buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_id)
        glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)

        self.index_buffer_id = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.index_buffer_id)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

        # xyzwrgba := [float32] * 4 + [float32] * 4
        vsize = np.nbytes[np.float32] * 4
        csize = np.nbytes[np.float32] * 4
        unit_size = vsize + csize
        glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, unit_size, None)
        glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, unit_size, c_void_p(vsize))
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)

    def resize(self, width, height):
        """The reshape callback function."""
        if height == 0:
            return

        glViewport(0, 0, width, height)

        # Set the projection matrix.
        projection = perspective(45.0, width / height, 1.0, 100.0)
        proj_id = glGetUniformLocation(self.program_id, b"projection")
        glUniformMatrix4fv(proj_id, 1, GL_TRUE, projection)

    def do_render(self):
        """Render the object."""

        glDrawElements(GL_TRIANGLE_FAN, self.num_triangles + 2, GL_UNSIGNED_BYTE, None)

    def cleanup(self):
        """The clean up callback function."""

        super(ShaderDemoApp, self).cleanup()
        self.destroy_vbo()

    def destroy_vbo(self):
        """Clean up VAO and VBO."""

        glDisableVertexAttribArray(1)
        glDisableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.buffer_id])

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, [self.index_buffer_id])

        glBindVertexArray(0)
        glDeleteVertexArrays(1, [self.vao_id])

def main(args):
    """The main function."""

    app = ShaderDemoApp(
        window_title=b'Shader Demo',
        window_size=(300, 300))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

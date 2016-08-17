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
# pylint: disable=unused-argument, no-self-use, invalid-name, no-member
import sys
import os
import colorsys
from ctypes import c_void_p

import numpy as np
from PIL import Image
import OpenGL.GL as GL

from modernapp import ModernApp

VERT_SHADER_SOURCE = """
#version 330 core

uniform mat4 camera;
uniform mat4 projection;
uniform mat4 rotation;

layout(location=0) in vec4 in_Position;
layout(location=1) in vec4 in_Color;
layout(location=2) in vec2 in_TexCoord;

out vec4 ex_Color;
out vec2 ex_TexCoord;

void main(void)
{
    gl_Position = projection * camera * rotation * in_Position;
    ex_Color = in_Color;
    ex_TexCoord = in_TexCoord;
}
"""

FRAG_SHADER_SOURCE = """
#version 330 core

uniform sampler2D texture_sampler;

in vec4 ex_Color;
in vec2 ex_TexCoord;
out vec4 out_Color;

void main(void)
{
    out_Color = texture(texture_sampler, ex_TexCoord).rgba;
    if(out_Color.a < 0.9){
        out_Color = ex_Color;
    }
}
"""

class ShaderDemoApp(ModernApp):
    """A GLSL demonstration."""

    def __init__(self, **kwargs):
        """Initialize an instance of class ShaderDemoApp."""

        kwargs.setdefault('context_version', (3, 1))
        super(ShaderDemoApp, self).__init__(**kwargs)

        self.buffer_id = 0
        self.index_buffer_id = 0
        self.num_triangles = 24
        self.texture = 0

        self.vao_id = 0

    def get_shader_sources(self):
        """Initialize shader source."""

        return {
            GL.GL_VERTEX_SHADER: VERT_SHADER_SOURCE,
            GL.GL_FRAGMENT_SHADER: FRAG_SHADER_SOURCE,}

    def init_object(self):
        """Initialize the object to be displayed."""

        num_triangles = self.num_triangles
        vertices = np.array(
            [0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0])
        for i in range(num_triangles):
            theta = 2 * np.pi * i / num_triangles
            pos = np.array([np.cos(theta), np.sin(theta), 1.0, 1.0])
            color = colorsys.hsv_to_rgb(i / num_triangles, 1.0, 1.0)
            tex = pos[0:2]
            vertices = np.hstack((vertices, pos, color, [1.0], tex))

        vertices = vertices.astype(np.float32)
        indices = np.hstack(
            (range(num_triangles + 1), 1)).astype(np.uint8)

        self.vao_id = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_id)

        # Create buffer objects data.
        self.buffer_id = GL.glGenBuffers(1)
        GL.glBindBuffer(
            GL.GL_ARRAY_BUFFER, self.buffer_id)
        GL.glBufferData(
            GL.GL_ARRAY_BUFFER, vertices, GL.GL_STATIC_DRAW)

        self.index_buffer_id = GL.glGenBuffers(1)
        GL.glBindBuffer(
            GL.GL_ELEMENT_ARRAY_BUFFER, self.index_buffer_id)
        GL.glBufferData(
            GL.GL_ELEMENT_ARRAY_BUFFER, indices, GL.GL_STATIC_DRAW)

        # xyzwrgbauv := [float32] * 4 + [float32] * 4 + [float32] * 2
        vsize = np.nbytes[np.float32] * 4
        csize = np.nbytes[np.float32] * 4
        tsize = np.nbytes[np.float32] * 2
        unit_size = vsize + csize + tsize
        GL.glVertexAttribPointer(
            0, 4, GL.GL_FLOAT, GL.GL_FALSE, unit_size, None)
        GL.glVertexAttribPointer(
            1, 4, GL.GL_FLOAT, GL.GL_FALSE, unit_size, c_void_p(vsize))
        if self.texture:
            GL.glVertexAttribPointer(
                2, 2, GL.GL_FLOAT, GL.GL_FALSE,
                unit_size, c_void_p(vsize + csize))
        GL.glEnableVertexAttribArray(0)
        GL.glEnableVertexAttribArray(1)
        if self.texture:
            GL.glEnableVertexAttribArray(2)

    def init_texture(self):
        """Initialize textures."""

        source_path = os.path.join(
            os.path.dirname(__file__), '../../_static/illvelo.png')
        img = Image.open(source_path).resize((256, 256))
        assert img.mode == 'RGBA'

        tex_id = GL.glGetUniformLocation(
            self.program_manager.program_id, b"texture_sampler")
        GL.glUniform1i(tex_id, 0)

        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.texture = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture)

        GL.glTexImage2D(
            GL.GL_TEXTURE_2D, 0, GL.GL_RGBA,
            img.size[0], img.size[1],
            0, GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img.tobytes())

        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameterf(
            GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)

    def do_render(self):
        """Render the object."""

        GL.glDrawElements(
            GL.GL_TRIANGLE_FAN, self.num_triangles + 2,
            GL.GL_UNSIGNED_BYTE, None)

    def cleanup(self):
        """The clean up callback function."""

        super(ShaderDemoApp, self).cleanup()
        self.destroy_vbo()

        GL.glDeleteTextures(1, [self.texture])

    def destroy_vbo(self):
        """Clean up VAO and VBO."""

        if self.texture:
            GL.glDisableVertexAttribArray(2)

        GL.glDisableVertexAttribArray(1)
        GL.glDisableVertexAttribArray(0)

        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, 0)
        GL.glDeleteBuffers(1, [self.buffer_id])

        GL.glBindBuffer(GL.GL_ELEMENT_ARRAY_BUFFER, 0)
        GL.glDeleteBuffers(1, [self.index_buffer_id])

        GL.glBindVertexArray(0)
        GL.glDeleteVertexArrays(1, [self.vao_id])

def main(args):
    """The main function."""

    app = ShaderDemoApp(
        window_title=b'Shader Demo',
        window_size=(300, 300),
        camera_eye=(2., 2., 2.),
        camera_center=(0., 0., 0.),
        camera_up=(0., 0., 1.))
    app.run(sys.argv)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

# -*- coding: utf-8 -*-
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# NumPy
from numpy import array

# PIL
from PIL import Image

# main 等で使う変数
window_title=b"Generating textures from PNG files"
window_sx,window_sy = 320,240
window_x,window_y = 100,100

def init():
    """OpenGL ステートを初期化する"""

    glClearColor(0., 0., 0., 1.)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_BLEND)

    img = Image.open('../pillow/illvelo.png').resize((256, 256))
    assert img.mode == 'RGBA'

    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_BLEND)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

vx, vy = 40.0, 40.0
tx, ty = 6.0, 6.0

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

def display():
    """シーンレンダリング"""

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    gluLookAt(14, 14, 1.58,
              0, 0, 0,
              0, 0, 1)

    # プリミティブを描画する。
    glPushAttrib(GL_CURRENT_BIT)
    glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glTexCoordPointer(2, GL_FLOAT, 0, texcoords)
    glColorPointer(4, GL_FLOAT, 0, colors)
    glDrawArrays(GL_POLYGON, 0, 4)

    glPopClientAttrib()
    glPopAttrib()
    glPopMatrix()

    # バッファスワップ
    glutSwapBuffers()

################################################################################
# callback

def reshape(width, height):
    """ウィンドウリサイズイベントをハンドルする。"""
    if height == 0:
        return

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #if width <= height:
    #    # 縦長ビューポートのケース
    #    aspect = float(height) / width
    #    glOrtho(-2, 2, -2 * aspect, 2 * aspect, -5.0, 20.0)
    #else:
    #    # 横長ビューポートのケース
    #    aspect = float(width) / height
    #    glOrtho(-2 * aspect, 2 * aspect, -2, 2, -5.0, 20.0)
    ## もしくは
    gluPerspective(45.0, float(width)/height, 1.0, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard(key, x, y):
    """キーボードイベントをハンドルする。"""

    if ord(key) == 0o33:
        # ESC
        print('ESC pressed', file=sys.stderr)
        sys.exit()

def mouse(button, state, x, y):
    """マウスのクリックイベントをハンドルする。"""
    pass

def motion(x, y):
    """マウスのモーションイベントをハンドルする。"""
    pass

################################################################################
# main

def main():
    # GLUT を初期化する。
    glutInit(sys.argv)

    # ウィンドウを設定する。
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_sx, window_sy)
    glutInitWindowPosition(window_x, window_y)
    glutCreateWindow(window_title)

    # OpenGL ステートを初期化する。
    init()

    # コールバック関数を登録する。
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    #glutMotionFunc(motion)

    # イベントハンドルスタート。
    glutMainLoop()

if __name__ == '__main__':
    main()

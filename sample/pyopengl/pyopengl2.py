# -*- coding: utf-8 -*-
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Pillow
from PIL import Image, ImageDraw, ImageFont

# main 等で使う変数
window_title=b"The Clean Room"
window_sx,window_sy = 320,240
window_x,window_y = 100,100

def init():
    """OpenGL ステートを初期化する"""

    glClearColor(0., 0., 0., 1.)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    img = drawtext('潔')

    glTexImage2D(GL_TEXTURE_2D, 0, 4, img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

def drawtext(text, initsize=256, point=144, margin=4):
     # 大きめのキャンヴァスを用意しておく。
     img = Image.new('RGBA', (initsize, initsize), (0, 0, 0, 0))
     dr = ImageDraw.Draw(img)

     fnt = ImageFont.truetype('hgrme.ttc', point)
     ext = dr.textsize(text, font=fnt)
     dr.text((margin, margin), text, font=fnt, fill='white')

     # TODO: img.size の各成分に最も近い最小の 2 のべき乗の値を使う。
     return img.crop(
         (margin, margin, ext[0]+margin*3, ext[1]+margin*3)
         ).resize((initsize, initsize), Image.ANTIALIAS)

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
   
def display():
    """シーンレンダリング"""

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

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
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glTexCoordPointer(2, GL_FLOAT, 0, texcoords)
    glColorPointer(4, GL_FLOAT, 0, colors)
    glDrawArrays(GL_QUADS, 0, 4)

    glPopClientAttrib()

    glPopAttrib()
    glPopMatrix()

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
    gluPerspective(45.0, float(width)/height, 1.0, 20.0)

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

    glutMainLoop()

if __name__ == '__main__':
    main()

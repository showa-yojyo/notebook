# -*- coding: utf-8 -*-
# OpenGL の演習スクリプト用テンプレ
"""%prog
A study program of OpenGL
Example: %prog"""
import sys

# 三角関数等を利用するならばコメントアウトを解除する。
#import math
from optparse import OptionParser

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# NumPy
#from numpy import array

# Pillow
#from PIL import Image

# main 等で使う変数
window_title=b"OpenGL Study"
window_sx,window_sy = 320,240
window_x,window_y = 100,100

def init():
    """OpenGL ステートを初期化する"""

    glClearColor(0., 0., 0., 1.)
    glEnable(GL_DEPTH_TEST)

def display():
    """シーンレンダリング"""

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # プリミティブを描画する。
    glPushAttrib(GL_CURRENT_BIT)

    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glEnd()

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
    if width <= height:
        # 縦長ビューポートのケース
        aspect = float(height) / width
        glOrtho(-2, 2, -2 * aspect, 2 * aspect, -5.0, 20.0)
    else:
        # 横長ビューポートのケース
        aspect = float(width) / height
        glOrtho(-2 * aspect, 2 * aspect, -2, 2, -5.0, 20.0)
    # もしくは
    #gluPerspective(45.0, float(width)/height, 1.0, 100.0)

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

def main(options, args):
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
    parser = OptionParser(__doc__)

    options, args = parser.parse_args()
    #if len(args) < 1:
    #    print(parser.print_help(), file=sys.stderr)
    #    sys.exit(1)

    main(options, args)

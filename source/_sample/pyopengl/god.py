# -*- coding: utf-8 -*-
import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# NumPy
from numpy import array

# PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# main 等で使う変数
window_title=b"God"
window_sx,window_sy = 320,240
window_x,window_y = 100,100

def init():
    """OpenGL ステートを初期化する"""

    glClearColor(0., 0., 0., 1.)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    #glLightfv(GL_LIGHT0, GL_POSITION, array( (5, 5, 10, 0.0),'f') );

    #glMaterialfv(GL_FRONT, GL_SPECULAR, array((1.0, 1.0, 1.0, 0.15),'f') );
    #glMaterialfv(GL_FRONT, GL_SHININESS, array((100.0, ),'f') );
    
    #glEnable(GL_BLEND)

    textwidth, textheight = 64, 64
    img = drawtext(textwidth, textheight)

    glEnable(GL_TEXTURE_2D)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, textwidth, textheight, 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

def drawtext(textwidth, textheight):
    # 大きめのキャンヴァスを用意しておく。
    img = Image.new('RGBA', (textwidth, textheight), 'white')
    #return img

    dr = ImageDraw.Draw(img)
    # HG 明朝体を使ってみる。
    fnt = ImageFont.truetype('hgrme.ttc', 48, encoding='utf-8')

    # テキストを用意する。
    text = u'神'
    
    width = 6
    height = 10
    for line in text.splitlines():
        ext = dr.textsize(line, fnt)
        dr.text((width, height), line, font=fnt, fill='black')
        width = max(ext[0], width)
        height += ext[1]
    
    # 余白をトリムする。
    #img = img.crop((0, 0, width, height))
    return img

vertices = [[-1.0, -1.0,  1.0],
            [-1.0,  1.0,  1.0],
            [1.0,  1.0,  1.0],
            [1.0, -1.0,  1.0],
            [-1.0, -1.0, -1.0],
            [-1.0,  1.0,  -1.0],
            [1.0,  1.0,  -1.0],
            [1.0, -1.0,  -1.0]]

colors = [[1.0, 0.0, 0.0],
          [0.0, 1.0, 1.0],
          [1.0, 1.0, 0.0],
          [0.0, 1.0, 0.0],
          [0.0, 0.0, 1.0],
          [1.0, 0.0, 1.0],
          [0.0, 0.0, 0.0],
          [1.0, 1.0, 1.0]]

def polygon(a, b, c, d):
    glBegin(GL_POLYGON)
    #glColor3fv(colors[a])
    glTexCoord2f(0.0, 0.0)
    glVertex3fv(vertices[a])

    #glColor3fv(colors[b])
    glTexCoord2f(0.0, 1.0)
    glVertex3fv(vertices[b])

    #glColor3fv(colors[c])
    glTexCoord2f(1.0, 1.0)
    glVertex3fv(vertices[c])

    #glColor3fv(colors[d])
    glTexCoord2f(1.0, 0.0)
    glVertex3fv(vertices[d])
    glEnd()

def display():
    """シーンレンダリング"""

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    gluLookAt(4, 4, 3,
              0, 0, 0,
              0, 0, 1)

    # プリミティブを描画する。
    glPushAttrib(GL_CURRENT_BIT)

    polygon(0, 3, 2, 1)
    polygon(2, 3, 7, 6)
    polygon(3, 0, 4, 7)
    polygon(1, 2, 6, 5)
    polygon(4, 5, 6, 7)
    polygon(5, 4, 0, 1)

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

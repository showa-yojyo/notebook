======================================================================
画像ファイルを扱う
======================================================================
本稿では PyOpenGL_ と Pillow_ との連携技についていくつか述べる。
プログラムの全体は、前述のスケルトンの上に構築していることを前提としている。

.. contents::

PNG ファイルからテクスチャーを生成する
======================================================================
ポイントは Pillow の ``Image`` インスタンスの ``tostring`` 戻り値を ``glTexImage2D`` に渡すことだ。
ここではアルファチャンネルを含む PNG ファイルからテクスチャーデータを作成する例を示す。

関数 init を定義する
----------------------------------------------------------------------
まずはテクスチャー設定から。

.. code-block:: python3

   def init():
      glClearColor(1., 1., 1., 1.)
      glEnable(GL_DEPTH_TEST)
      glEnable(GL_TEXTURE_2D)

      # Comment 1
      img = Image.open('illvelo.png').resize((256, 256))
      assert img.mode == 'RGBA'

      # Comment 2
      glTexImage2D(GL_TEXTURE_2D, 0, 4, img.size[0], img.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
      glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

Comment 1
  :doc:`/python-pillow` で利用した PNG ファイルからテクスチャーを作成している。
  ファイルのピクセルサイズがやや中途半端なので、決め打ちだが 256 ピクセル四方にリサイズする。

Comment 2
  ``glTexImage2D`` 呼び出しにより、テクスチャーデータを OpenGL に渡している。
  後半の実引数群に注目したい。

  残りの関数呼び出しは、アプリケーションの目的に応じてパラメーターを指定すること。

関数 display を定義する
----------------------------------------------------------------------
次に描画ロジックを示す。明らかに手抜きコードだが、説明にはこれで十分だろう。
これを ``display`` の主要部分に加える。

.. code-block:: python3

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
       """The display callback function."""

       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

       glMatrixMode(GL_MODELVIEW)
       glPushMatrix()
       glLoadIdentity()

       gluLookAt(14, 14, 1.58,
                 0, 0, 0,
                 0, 0, 1)

       # Render primitives.
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

       # Swap rendering buffers to repaint the screen.
       glutSwapBuffers()

実行すると以下のようなイメージ (320x240) を得るだろう。

.. image:: /_static/illvelo-texture.png
   :scale: 50%

日本語テキストを描画する
======================================================================
Pillow のテキスト描画機能と PyOpenGL のテクスチャー機能を活用したプログラム例。
要所のみを説明する。

関数 init を定義する
----------------------------------------------------------------------
``init`` のテクスチャー初期化コードに以下を含める。

.. code-block:: python3

   img = drawtext('潔')

   # 残りは前項を参照。

関数 drawtext を定義する
----------------------------------------------------------------------
フォントファイルは別途用意すること。ここではシステムに既存のものを利用している。

.. code-block:: python3

   def drawtext(text, initsize=256, point=144, margin=4):
       # Set up a larger canvas.
       img = Image.new('RGBA', (initsize, initsize), (0, 0, 0, 0))
       dr = ImageDraw.Draw(img)

       fnt = ImageFont.truetype('hgrme.ttc', point)
       ext = dr.textsize(text, font=fnt)
       dr.text((margin, margin), text, font=fnt, fill='white')
       img = img.crop((margin, margin, ext[0] + margin * 3, ext[1] + margin * 3))

       # TODO: use the least power of 2 values closest to each img.size component.
       img = img.resize((initsize, initsize), Image.ANTIALIAS)

       return img

関数 display を定義する
----------------------------------------------------------------------
.. code-block:: python3

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

関数 reshape を定義する
----------------------------------------------------------------------
.. code-block:: python3

   def reshape(width, height):

       # ... 略 ...

       gluPerspective(45.0, width / height, 1.0, 20.0)

以上を実行すると、実行結果のスクリーンショットはだいたい次のようなものになる。

.. image:: /_static/pyopengl-text.png
   :scale: 50%

Pillow + glReadPixels によるスクリーンショット取得
======================================================================
ウィンドウに描画されているイメージをファイルに保存できるとたいへん便利なので、次のような関数を定義しておくとよい。
この関数をキーボードイベントコールバックあたりから呼び出すようにしておくと便利。

.. code-block:: python3

   def capture_screen():
      sx = glutGet(GLUT_WINDOW_WIDTH)
      sy = glutGet(GLUT_WINDOW_HEIGHT)

      pixels = glReadPixels(0, 0, sx, sy, GL_RGBA, GL_UNSIGNED_BYTE)
      img = Image.fromstring("RGBA", (sx, sy), pixels)
      img = img.transpose(Image.FLIP_TOP_BOTTOM)

      filename = input('filename: ')
      img.save(filename)
      print('{} saved'.format(filename))

.. include:: /_include/pyopengl-refs.txt

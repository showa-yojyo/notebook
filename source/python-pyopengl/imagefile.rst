======================================================================
画像ファイルを扱う
======================================================================
本稿では PyOpenGL_ と Pillow_ との連携技についていくつか述べる。

ここに示すプログラムは、いずれも前述のクラスを派生することで構築している。

.. contents::

PNG ファイルからテクスチャーを生成する
======================================================================
既存の PNG ファイルから 2 次元テクスチャーデータを生成する方法の一例を示す。

ポイントは Pillow の ``Image`` インスタンスのメソッド ``tostring`` の戻り値を関数 ``glTexImage2D`` に渡すことだ。
アルファチャンネルを含む PNG ファイルからテクスチャーデータを作成する例の、コード全景を示す。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3

以下、ポイントを絞って解説する。

各種初期設定をする
----------------------------------------------------------------------
スケルトンクラス ``GLAppBase`` のサブクラスを定義する。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3
   :lines: 12-26

* 新しいサンプルコードを書くのが面倒なので、レガシー API を使うのだが、その都合上、コンテキストバージョンを 1.5 にしたい。それ以外はスーパークラスの既定値に従う。
* メソッド ``init_gl`` で ``GL_TEXTURE_2D`` 機能を有効にしておくことを忘れずに。

描画オブジェクトを定義する
----------------------------------------------------------------------
メソッド ``init_object`` をオーバーライドすることで、描画オブジェクトを定義する。ここではテクスチャー、図形の順に処理する。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3
   :lines: 28-34

PNG ファイルからテクスチャーを作成している（:doc:`/python-pillow` 参照）。メソッド
``tostring`` で矩形イメージの RGBA バイト列を得られるということが本質的だ。
イメージのピクセルサイズが OpenGL 的に中途半端なので、決め打ちだが 256 ピクセル四方にリサイズする。

ファイルパスが私のノート環境から決まる値に決め打ちになっているが、あくまでも本稿はテクスチャー描画の実現方法に主眼があるので気にしない。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3
   :lines: 36-43

関数 ``glTexImage2D`` 呼び出しにより、テクスチャーデータを OpenGL に渡している。
残りのテクスチャーオプションは、アプリケーションの目的に応じてパラメーターを指定すればよい。

最後に空間座標・テクスチャー座標・色からなる頂点データをレガシー API で定義する。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3
   :lines: 45-68

これで描画の準備がほぼ整った。残りは描画メソッド本体で行う。

描画する
----------------------------------------------------------------------
メソッド ``do_render`` をオーバーライドすることで描画処理の中心部分を定義する。レガシー API のオンパレードなので、説明は省く。

.. literalinclude:: /_sample/pyopengl/legacy-texture.py
   :language: python3
   :lines: 81-102

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

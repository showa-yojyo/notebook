======================================================================
PyOpenGL 3.x 利用ノート
======================================================================

.. contents:: ノート目次

.. note::

   * OS: Windows XP Home Edition SP 3
   * 本稿執筆にあたり利用した各パッケージのバージョンは次のとおり。

     * Python_: 2.6.6
     * PyOpenGL_: 3.0.2a5
     * NumPy_: 1.6.1
     * PIL_: 1.1.7 (unofficial)

関連リンク
======================================================================
PyOpenGL_ (The Python OpenGL Binding)
  本パッケージ総本山サイト。インストール方法やドキュメント等。

GLUT_ (Nate Robins - OpenGL - GLUT for Win32)
  OpenGL Utility Toolkit (GLUT) の Windows 版バイナリーを配布しているウェブページ。

関連ノート
======================================================================
* :doc:`python-numpy`
* :doc:`python-pil`

インストール
======================================================================
* 経験則として PyOpenGL の依存パッケージ的なものを先にインストールしておくのがコツ。
  もちろん本来の意味では PyOpenGL が依存するパッケージというものはない。
  しかし、グラフィックのプログラムを書くのならば、
  普通はインストールしていないとマズいというものは存在する。

  * 基礎的なベクトル演算のために NumPy_ を利用したいので、インストールしておく。関連ノート参照。
  * 画像ファイルからテクスチャーを読み込むために PIL_ をインストールしておく。これも関連ノート参照。

* GLUT_ をインストールしておく。ただし、システムに存在しない場合に限る。

  * :file:`glut32.dll` が環境変数 ``PATH`` の含むどこかにいれば十分。
  * ない場合は関連リンク先から :file:`glut-3.7.6-bin.zip` をダウンロードする。
    解凍して DLL ファイルを ``C:\WINDOWS\System32`` にぶち込む。
    残りのファイルは処分する。

* PyOpenGL 本体のインストールは `easy_install`_
  またはそれに準じた方法で行えばよい。
  `pip`_ 推奨。

  .. code-block:: console
  
     $ pip install PyOpenGL

ドキュメント
======================================================================
PyOpenGL は Python のラッパーに過ぎない。
OpenGL が一通り使える腕があれば、
必要な勉強は C 言語でのプログラミングとの差分を確認するだけということになる。

* 公式サイトの "PyOpenGL for OpenGL Programmers" という章を読む。

  * PyOpenGL は実行速度については期待できない。

    * プログラミングの柔軟性、利便性、堅牢性を重視しているらしい。
    * 頂点毎の各種演算はアホみたいに遅い。
      よって、せめて配列ベースの演算でコードを書くようにする。

  * PyOpenGL は SIWG ではなく ctypes を利用して実装されている。

  * 一部関数シグニチャーが C 言語版と PyOpenGL 版とで異なる。
    といっても、配列モノの API が Python 風に表現されているだけ。

  * PyOpenGL は OpenGL 操作中でのエラー発生時に例外を送出する。
    プログラマーが手で ``glCheckError`` を書かずにすむというわけだ。

    * デバッグが終わったら ``OpenGL.ERROR_CHECKING = False`` すればよい。

  * PyOpenGL はエラーをログ出力する。
    ``OpenGL.ERROR_LOGING = False`` で無効化。

  * PyOpenGL では、関数の型別サフィックスが省略できる。
    例えば ``glDrawElements{ub|us|ui}`` はいずれも ``glDrawElements`` とできる。

コード
======================================================================
C ではなく Python を利用して OpenGL プログラムを書く利点は、
PyOpenGL_ の API を NumPy_ や PIL_ といった、高品質なサードパーティ製パッケージの
部品と簡単に組み合わせて利用できる点に尽きる。

欠点は何度も言うように実行が遅いことだ。悲しいくらい遅い。
しかし、グラフィックの初学者には遅い方が学習の上ではむしろ好都合ということもあるだろう。

GLUT ベースのスケルトンを自作しておく
----------------------------------------------------------------------
簡単な PyOpenGL プログラムの構造は次のようなものになる。
次のようなテキストファイルをテンプレートとして保存しておき、
新しいスクリプトを作成する際には、このテンプレートからコードを「増築」していくようにする。

.. literalinclude:: glut-skeleton.py
   :language: python

仮に実行すると、黒い画面に赤い三角形が描画されているのが確認できるはずだ。
以降の各デモコードでは、このスケルトンの差分部分・修正部分を記述する。

C 言語で配列に相当する型の実引数を与える
----------------------------------------------------------------------
* 何度も言うが型を示すサフィックスが省略できる。
  例えば ``glLightfv`` ではなく ``glLight`` でよい。

* 値の与え方もかなり柔軟になっている。
  ``list``, ``tuple``, ``numpy.ndarray``, etc. を直接与えることが許される。

.. code-block:: python

   from OpenGL.GL import *
   from OpenGL.GLU import *
   from OpenGL.GLUT import *
   import numpy as np

   SPECULAR_VALUE = np.ones(4)
   DIFFUSE_VALUE = SPECULAR_VALUE * .9
   DIFFUSE_VALUE[3] = 1.0
   AMBIENT_VALUE = SPECULAR_VALUE * .1
   AMBIENT_VALUE[3] = 1.0

   def init_lighting():
       glEnable(GL_LIGHTING)
       glEnable(GL_LIGHT0)
       glLight(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 1.0, 0.0))
       glLight(GL_LIGHT0, GL_AMBIENT, AMBIENT_VALUE)
       glLight(GL_LIGHT0, GL_DIFFUSE, DIFFUSE_VALUE)
       glLight(GL_LIGHT0, GL_SPECULAR, SPECULAR_VALUE)

       glEnable(GL_COLOR_MATERIAL)
       glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

       glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, SPECULAR_VALUE)
       glMaterial(GL_FRONT_AND_BACK, GL_EMISSION, (0.0, 0.0, 0.0, 1.0))

PNG ファイルからテクスチャーを生成する
----------------------------------------------------------------------
ポイントは PIL の ``Image`` インスタンスの ``tostring`` 戻り値を ``glTexImage2D`` に渡すことだ。
ここではアルファチャンネルを含む PNG ファイルからテクスチャーデータを作成する例を示す。

まずはテクスチャー設定から。

.. code-block:: python

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
  :doc:`python-pil` で利用した PNG ファイルからテクスチャーを作成している。
  ファイルのピクセルサイズがやや中途半端なので、決め打ちだが 256 ピクセル四方にリサイズする。

Comment 2
  ``glTexImage2D`` 呼び出しにより、テクスチャーデータを OpenGL に渡している。
  後半の実引数群に注目したい。
  
  残りの関数呼び出しは、アプリケーションの目的に応じてパラメーターを指定すること。

次に描画ロジックを示す。明らかに手抜きコードだが、説明にはこれで十分だろう。
これを ``display`` の主要部分に加える。

.. code-block:: python

   vx, vy = 20.0, 20.0
   tx, ty = 4.0, 4.0
   
   # ...

   gluLookAt(4, 4, 4,
             0, 0, 0,
             0, 0, 1)

   # ...

   glBegin(GL_POLYGON)
   glColor3f(0, 0, 0)
   glTexCoord2d(-tx, -ty)
   glVertex3f(-vx, -vy, 0.0)

   glTexCoord2d(tx, -ty)
   glVertex3f(vx, -vy, 0.0)

   glTexCoord2d(tx, ty)
   glColor3f(1, 1, 1)
   glVertex3f(vx, vy, 0.0)

   glTexCoord2d(-tx, ty)
   glVertex3f(-vx, vy, 0.0)
   glEnd()

実行すると以下のようなイメージ (320x240) を得るだろう。

.. image:: /_static/illvelo-texture.png
   :scale: 50%

日本語テキストを描画する
----------------------------------------------------------------------
PIL のテキスト描画機能と PyOpenGL のテクスチャー機能を活用したプログラム例。
要所のみを説明する。

.. code-block:: python

   def drawtext(text, initsize=256, point=144, margin = 4):
       # 大きめのキャンヴァスを用意しておく。
       img = Image.new('RGBA', (initsize, initsize), (0, 0, 0, 0))
       dr = ImageDraw.Draw(img)

       fnt = ImageFont.truetype('hgrme.ttc', point)
       ext = dr.textsize(text, font=fnt)
       dr.text((margin, margin), text, font=fnt, fill='white')
       img = img.crop((margin, margin, ext[0]+margin, ext[1]+margin))

       # TODO: img.size の各成分に最も近い最小の 2 のべき乗の値を使う。
       img = img.resize((initsize, initsize), Image.ANTIALIAS)

       return img

``init`` のテクスチャー初期化コードに以下を含める。

.. code-block:: python

   img = drawtext(u'潔')

   # 残りは前項を参照。

``display`` 関連は前項を参照に適宜パラメーターを調整。

.. code-block:: python

   vx, vy = 15.0, 15.0
   tx, ty = 5.0, 5.0
   
   vertices = (
       -vx, -vy, 0.0,
        vx, -vy, 0.0,
        vx, vy, 0.0,
       -vx, vy, 0.0)
   
   texcoords = (
       0, ty,
       tx, ty,
       tx, 0,
       0, 0)
   
   colors = (
       1, 1, 1, 1.0,
       1, 1, 1, 1.0,
       0, 0, 0, 0.75,
       0, 0, 0, 0.75)

   def display():
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

       glMatrixMode(GL_MODELVIEW)
       glPushMatrix()
       glLoadIdentity()

       gluLookAt(0.5, -1.0, 1.58,
                 0.5, 10.0, 1.5,
                 0, 0, 1)

       glPushAttrib(GL_CURRENT_BIT)
       glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)

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

実行結果のスクリーンショットは次のようなものになる。

.. image:: /_static/pyopengl-text.png
   :scale: 50%


.. _Python: http://www.python.org/
.. _PyOpenGL: http://pyopengl.sourceforge.net

.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pypi.python.org/pypi/pip
.. _Python Extension Packages for Windows - Christoph Gohlke: http://www.lfd.uci.edu/~gohlke/pythonlibs/

.. _Numpy: http://scipy.org/NumPy/
.. _PIL: http://www.pythonware.com/products/pil

.. _PyQt: http://www.riverbankcomputing.com/software/pyqt/intro

.. _GLUT: http://user.xmission.com/~nate/glut.html

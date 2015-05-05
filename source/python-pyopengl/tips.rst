======================================================================
PyOpenGL プログラムに頻出する技法・注意点
======================================================================
本稿では PyOpenGL プログラムに頻出する技法と注意点を記す。

.. contents::

文字列が ``bytes`` 型になっている
======================================================================
PyOpenGL がなぜこういう仕様にしたのかわからないが、
関数 ``glGetString`` 等の文字列を返す関数ほとんどすべてが
``str`` オブジェクトではなく ``bytes`` オブジェクトを返すようだ。
よって、OpenGL から受け取る戻り値を確認するときはメソッド ``decode`` で読めるようにする。

.. code-block:: python3

   print("Version: ", GL.glGetString(GL.GL_VERSION).decode())

関数 ``glutCreateWindow`` 等、引数に文字列を取るものについても、
``str`` オブジェクトではなく ``bytes`` オブジェクトを受け付けると思っていたほうがよい。

.. code-block:: python3

   GLUT.glutCreateWindow(b"Texture Demo")
   # or
   GLUT.glutCreateWindow("テクスチャーデモ".encode('sjis'))

日本語文字列は ``sjis`` というエンコーディングで（私の環境では）うまくいく。

GLUT の引数コールバックに、自作クラスのメソッドを渡せる
======================================================================
例えば関数 ``glutReshapeFunc`` のシグニチャーは、オリジナルではこうだった。

.. code-block:: c

   void glutReshapeFunc(void (*func)(int width, int height));

PyOpenGL では次のようなコードが有効だ。

.. code-block:: python3

   def reshape(width, height):
       """the reshape callback for the current window"""
       ...

   # in global scope
   ...
   glutReshapeFunc(reshape)
   
そして、次のようなコードも有効だ。

.. code-block:: python3

   class MyPyOpenGLApp(object):

       def reshape(self, width, height):
           """the reshape callback for the current window"""
           ...

   # in global scope
   ...
   app = MyPyOpenGLApp()
   ...
   glutReshapeFunc(app.reshape)

複数形の名前を持つ関数が単数の値を返す場合は注意
======================================================================
例えば関数 ``glGenBuffers`` を考える。これはオリジナルとはシグニチャーが異なり、
引数が「生成するバッファーの個数」だけで、
戻り値が「指定した個数分の生成バッファーの名前」となっている。
問題は指定した個数が 1 のときに起こる。

まず ``buffer = glGenBuffers(1)`` とすると、
オブジェクト ``buffer`` の型はおそらく単なる ``int`` である。
ところがこれを ``buffer = glGenBuffers(2)`` とすると、
今度は要素数 2 の ``list`` が返ってくる。

これを破棄するときを考えると、頭が痛いわけだ。

.. code-block:: python3

   glDeleteBuffers(1, [buffer])
   # or
   glDeleteBuffers(len(buffer), buffer)

多分 PyOpenGL 側の設計ミスではないかと思う。

こういう問題が他にも関数 ``glDeleteFramebuffers``, ``glDeleteRenderbuffers``,
``glDeleteTextures``, ``glDeleteQueries``, etc. にありそうだ
（半分想像で書いているので、なかったら申し訳ない）。

配列を受け取る関数全般
======================================================================
一般に、OpenGL で配列を入力として受け取るある関数に対応する
PyOpenGL のそれは、オリジナルのものとは関数シグニチャーが若干異なる。
オリジナルでは「配列の要素数」「配列の先頭」の両方が引数リストにあるが、
PyOpenGL では「配列そのもの」に統合している傾向がある。

また、最初に言うべきだったが「配列」としては次のものが有効である。

* ``list`` オブジェクト
* ``tuple`` オブジェクト
* ``np.array`` オブジェクト

NumPy の ``np.array`` を配列として扱う
======================================================================
細かく考えると、C/C++ で ``GL_FLOAT`` の配列として表現するものは
Python ではどうすればよいのかという、配列要素型の問題がある。
正直に言うと、私の中ではここが完全には解決していない。
テキトーにやってうまくいくケースがあるのが気に食わない
（おそらく PyOpenGL の実装が気を利かせて型変換等の下処理をしてくれているはずだ）。

厳密にやりたい場合は、やはりオブジェクト ``np.array`` の生成時にコンストラクターで
``dtype`` を明示するのがベストであろう。

.. code-block:: python3

   # for GL_FLOAT interface
   vertex = np.array([0, 0, 0, 1], dtype=np.float32)

オブジェクトを生成した後からでも、メソッド ``astype`` で配列要素型の変換が可能だ。

``sizeof`` 問題
======================================================================
組み込み型のバイトサイズをハードコードしたくない人は次のようにする。

.. code-block:: python3

   # GL_FLOAT, float
   assert np.nbytes[np.float32] == 4

ポインター系統の関数のためにモジュール ``ctypes`` の機能を併用する
======================================================================
オリジナル OpenGL の関数で引数の型が ``const GLvoid*`` であるものについて、
これを PyOpenGL 版で実引数をどのように表現するかという問題があった。
今のところ 3 通り発見している。

* 実引数がゼロの場合は、単に ``None`` または標準モジュール ``ctypes`` から
  ``c_void_p`` をインポートして ``c_void_p(0)`` を指定する。
  単に ``0`` と指定するのでは、何も描画されない。
  ここが C/C++ と決定的に異なる。

* 実引数が非ゼロの場合は、次のどちらかになる。

  * 配列データを直接渡す場合は Python の ``list`` なり ``np.array`` なりのオブジェクトを直接指定する。
  * オフセット量を指定する場合は ``c_void_p(n)`` を指定する。
    ここで ``n`` はバイト数である。

「オフセット量を指定する場合」の例を挙げておく。
関数 ``glVertexAttribPointer`` の引数 ``pointer`` が、
「VBO ターゲット ``GL_ARRAY_BUFFER`` に結びついたアドレスからのバイトオフセット」を指定する場合だ。
このアドレスが ``GL_FLOAT`` or ``np.float32`` 配列のそれだとすれば、
``pointer`` としては ``c_void_p(4 * n)`` の形になるだろう。
具体例は :doc:`shader` の ``init_object`` を参照。

NumPy の ``np.array`` を行列として扱う
======================================================================
#. ``m.shape == (4, 4)`` となるように ``np.array`` オブジェクト ``m`` を生成する。
#. 各成分を適宜セットする。
#. 次のいずれかの方法で OpenGL に ``m`` を渡す。

   * ``m.transpose()`` を関数の実引数とする。
   * ``m`` そのものを転置行列系の GL 関数の実引数とする。
   * ``m`` そのものを GL 関数の実引数とし、かつ転置フラグ引数を ``GL_TRUE`` にする。
   * ``m.transpose()`` を関数の実引数とし、かつ転置フラグ引数を ``GL_FALSE`` にする。

本テキストでは旧式 OpenGL に準拠して、
行列は列ベクトルの左から作用するものとして設計している。

PIL 経由でテクスチャーを生成する
======================================================================
:doc:`imagefile` に記した。

.. include:: /_include/pyopengl-refs.txt

======================================================================
バッファーオブジェクトを扱う
======================================================================
本稿では PyOpenGL_ のバッファーオブジェクト機能を、特に NumPy_ のオブジェクトと連携して利用する方法について記す。

オリジナルの OpenGL では C 言語の配列データとのやりとりを規定しているので、これを Python の流儀でどのように表現するのかを考慮することになる。

.. contents::

サンプルコード全体
======================================================================
最初にバッファーオブジェクトを利用するコードの全体を示す。

.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3

これは単にカラフルな正多角形を描画するだけのプログラムで、バッファーオブジェクトを利用できることを示すことのみを目的としている。
このため、シェーダープログラム、テクスチャー、ライティング、座標変換といった機能は排除してある。

表示されるグラフィックは次のようなものだ。

.. image:: /_static/pyopengl-vbo.png
   :scale: 100%

ポイント解説
======================================================================
本節では上記コードを要所に絞って解説していく。解説するポイントの順序はプログラムの実行順とするが、重要なのはバッファーデータの取り扱い方法だ。

インポート部分
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 14-21

* 後述するバッファーデータのオフセット指定のために、どうしても謎のクラス ``ctypes.c_void_p`` をインポートする必要がある。
* 頂点の RGB を指定するのを間接的に行う予定で、標準モジュールの ``colorsys`` をインポートしてある。
* 例によって、自作クラス ``GLAppBase`` をインポートする。

クラス ``BufferObjectDemoApp``
----------------------------------------------------------------------
スケルトンクラス ``GLAppBase`` のサブクラスを定義する。
今回のプログラムではバッファーオブジェクトの適切なタイミングでの生成・削除という、オブジェクト指向プログラミングにうってつけな問題の解決を必要とする。
つまり、クラスの実装という方針は今回は適切なように思える。

.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 23-33

* またしてもレガシー API を用いるので、コンテキストバージョンを差し当たり 2.1 にしておく。

  ちなみに仮にこれを 3.1 などの「高め」のバージョンに指定すると、プログラムが一気に動作しなくなる。

  .. code-block:: text

     File "errorchecker.pyx", line 53, in OpenGL_accelerate.errorchecker._ErrorChecker.glCheckError (D:\Build\PyOpenGL\pyopengl-bzr\OpenGL_accelerate\src\errorchecker.c:1221)
     OpenGL.error.GLError: GLError(
             err = 1282,
             description = b'\x96\xb3\x8c\xf8\x82\xc8\x91\x80\x8d\xec',
             baseOperation = glEnableClientState,
             cArguments = (GL_VERTEX_ARRAY,)
     )

  「無効な操作」と言っているのだが、関数 ``glEnableClientState`` の呼び出しが高位バージョンの OpenGL だとアウトらしい。

* ``buffer_id`` および ``index_buffer_id`` を、関数 ``glGenBuffers`` 系の ID を管理するためのメンバーデータとする。
  プログラムがそれらの生成時と削除時に参照するメンバーデータだ。
* ``num_triangles`` は描画する多角形の頂点数を示すものだ。扱いとしては定数である。

メソッド ``init_object``
----------------------------------------------------------------------
バッファーオブジェクトを定義するため、メソッド ``init_object`` をオーバーライドする。

.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 35-47

次の段階を踏んでバッファーオブジェクトを構築していく。

#. NumPy の配列を活用して、描画するべき頂点の各種属性を定義する。
#. 定義した頂点データのアドレス的なものを PyOpenGL を用いて指定する。

まずは ``vertices`` の「メモリレイアウト」について説明する。

例えば三角形を *N* 個描くものとする。このとき、座標と色のペアが *N* 個あることになる。サンプルコードにおける想定はこのようなものだ。

* 点の座標と色の表現をそれぞれ (x, y, z, w) および (R, G, B, A) で表現することにした。そして、ひとつの頂点データを
  (x, y, z, w, R, G, B, A) で表現することにした。
* 点・色の各成分の型を OpenGL の ``GL_FLOAT`` に相当する、NumPy の ``np.float32`` で表現することにした。
* 頂点データ全体を (x0, y0, z0, w0, R0, G0, B0, A0, ..., ) のように直列して表現することにした。

結局は ``GL_FLOAT`` 型の 4 * 8 * *N* 要素からなる配列を作成することになるが、プログラムでは

* ``np.array`` を配列バッファーとして、
* ``np.array.hstack`` を配列の単純連結操作として、
* ``np.array.astype`` を高精度の型 (e.g. ``float64``) から低精度の型 (e.g. ``float32``) へキャストするための操作として

適宜応用した。

描画するイメージ自体についてのプランはこうだ。

* 単位円周上に正 24 角形を描く。
* ``GL_TRIANGLE_FAN`` で原点を中心としてファンとして描く。
* 頂点の色は配列のインデックスをベースに HSV で決める。中心は白にしておく。

.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 49-56

* 関数 ``glGenBuffers`` での実引数に注意。1 の場合はリストではなく、単なる整数が戻る。
* 関数 ``glBufferData`` の第 2 引数には NumPy の配列オブジェクトを直接指定できる。便利。

.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 58-62

バッファーオブジェクトのバインドの他に、ポインターの指定も必要となる。関数
``glVertexPointer`` および ``glColorPointer`` の最終実引数に要注意。

一般に、オリジナル OpenGL の関数でパラメーターの型が ``const GLvoid*`` であるものについて、これを
Python で表現する状況・方法は今のところ 3 通り発見している。

* 実引数がゼロの場合は、単に ``None`` または ``c_void_p(0)`` を指定する。単に ``0`` では何も描画されないことに注意。
* 実引数が非ゼロの場合は、次のどちらかになる。

  * 配列データを直接渡す場合は Python の ``list`` なり ``np.array`` なりのオブジェクトを直接指定する。
  * オフセット量を指定する場合は ``c_void_p(n)`` を指定する。ここで ``n`` はバイト数である。

メソッド ``do_render``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 64-71

最大のポイントは ``glDrawElements`` の最後の引数の型にある。直前の解説を参照。

メソッド ``cleanup``
----------------------------------------------------------------------
.. literalinclude:: /_sample/pyopengl/buffer-object.py
   :language: python3
   :lines: 73-81

関数 ``glDeleteBuffers`` の第 2 引数にはこのように配列的なオブジェクトを渡す。
``glGenBuffers(1)`` がスカラーを戻すので、このように ``list`` 化してやるのが面倒だが必要だ。
ちなみに ``glGenBuffers(2)`` なら ``list`` を戻すので、そのまま削除関数に引き渡せる。

.. include:: /_include/pyopengl-refs.txt

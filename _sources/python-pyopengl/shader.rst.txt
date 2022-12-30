======================================================================
単純なシェーダープログラムの作成
======================================================================

今までのサンプルは古い OpenGL の仕様に基づいたコードなので、いずれ無用の存在にな
る（私のノートはこういうパターンがけっこう多い）。全てを忘れて最新バージョンの
OpenGL が推奨する様式でコードを書くことにしたい。残念ながら私の環境は OpenGL 3.1
までの機能しかサポートしていないので、今後ここに記すコードはせいぜい 3.1 程度の
新しさとなる。

私の OpenGL の知識はバージョン 1.4 程度で止まっており、ましてやシェーダーなどは
触ったこともない。ゆえに、ここでは初歩的な事項の確認にとどまる。

.. contents::

.. warning::

   私の環境でプログラムが適切なグラフィックドライバーを取得できない不具合が発生
   しており、本稿のスクリプトを実行すると、次のエラーメッセージが生じて異常終了
   する。ちなみに description のテキストは「無効な列挙」だ。

   .. code:: console

      bash$ ./shaderdemo.py
      freeglut (./shaderdemo.py): OpenGL >2.1 context requested but wglCreateContextAttribsARB is not available! Falling back to legacycontext creation
      freeglut (./shaderdemo.py): fgInitGL2: fghGenBuffers is NULL
      Vendor: Microsoft Corporation
      Renderer: GDI Generic
      Version: 1.1.0
      Traceback (most recent call last):
        File "./shaderdemo.py", line 214, in <module>
          sys.exit(main(sys.argv))
        File "./shaderdemo.py", line 211, in main
          app.run(sys.argv)
        File "D:\home\yojyo\devel\all-note\notebook\source\_sample\pyopengl\appbase.py", line 69, in run
          self.init_glut(args)
        File "D:\home\yojyo\devel\all-note\notebook\source\_sample\pyopengl\appbase.py", line 120, in init_glut
          GL.glGetString(i[1]).decode()),
        File "errorchecker.pyx", line 53, in OpenGL_accelerate.errorchecker._ErrorChecker.glCheckError (src\errorchecker.c:1218)
      OpenGL.error.GLError: GLError(
              err = 1280,
              description = b'\x96\xb3\x8c\xf8\x82\xc8\x97\xf1\x8b\x93',
              baseOperation = glGetString,
              cArguments = (GL_SHADING_LANGUAGE_VERSION,)
      )

サンプルプログラムを探す
======================================================================

なにぶん知識がないものだから Google で GLSL 等の単語を検索して、色々と漁ってみる
しかない。次のようなサイトが取っ掛かりになる。

`GLSL 1.2 Tutorial <http://www.lighthouse3d.com/tutorials/glsl-tutorial/>`_
  バージョンが 1.2 と古いが、参考になった。
`rndblnch / opengl-programmable <https://bitbucket.org/rndblnch/opengl-programmable/src>`_
  話が早いことに PyOpenGL で書かれたプログラムも発見できた。

サンプルコード全体
======================================================================

プログラムをスクリプトファイルの形で構成する。全体を以下に示す：

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3

これはイルベロの描かれた正多角形を描画するだけのプログラムである。シェーダープロ
グラム、テクスチャー、座標変換機能はベースクラスで実装済みである。残念ながら、照
光処理は実装していない。

ポイント解説
======================================================================

本節では上記コードを要所に絞って解説していく。解説するポイントの順序は、スクリプ
トの先頭から末尾に向かってとする。

インポート
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 14-23

* 頂点の RGB を指定するのを間接的に行う予定で、標準モジュールの ``colorsys`` を
  インポートする。
* 後述するバッファーデータのオフセット指定のために、どうしても謎のクラス
  ``ctypes.c_void_p`` をインポートする必要がある。
* OpenGL 3.1 を志向しているので、GLU は決してインポートしない。
* クラス ``ModenApp`` のサブクラスをつくるため、当然インポートする。

シェーダーコード
----------------------------------------------------------------------

シェーダーコード自身については、OpenGL でも PyOpenGL でも何ら変わらない。Python
の場合はトリプルクォート記法が便利だ。

頂点シェーダーコード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: glsl
   :lines: 25-43

* OpenGL コンテキストバージョンを 3.1 以上に上げると、シェーダーコードの先頭行を
  ``#version 330`` のようにバージョンの宣言をするのがほぼ必須となる。明示的に指
  定しないと、コンパイラーはかなり古いシェーダーコードとみなす。結果、コンパイル
  エラーを引き起こす。
* ``layout(location=0) in vec4 ...`` の行の宣言により、Python コードからシェー
  ダーに何らかの四次元ベクトルデータを引き渡すこと示す。

  * 関数呼び出し ``glVertexAttribPointer(0, 4, ...)`` で、頂点シェーダー内
    ``location = 0`` のデータに四次元ベクトルデータをセットする。
  * 関数呼び出し ``glEnableVertexAttribArray(0)`` で、このやりとりを有効にすると
    いう手続きになるのだろう。

フラグメントシェーダーコード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: glsl
   :lines: 47-61

* 頂点シェーダーの出力がフラグメントシェーダーの入力となる。
* 最新バージョンの GLSL では ``gl_FragColor`` が廃止されたらしいので、本シェー
  ダーの出力を ``out ...`` の行で別途宣言する。

クラス ``ShaderDemoApp``
----------------------------------------------------------------------

OpenGL 3.0 以降準拠の PyOpenGL スクリプトのためのベースクラス ``ModenApp`` のサ
ブクラスを定義する。

メソッド ``__init__``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 68-79

* コンテキストバージョンは、コンストラクターに明示的に指示のない限り、本稿の意図
  通りに 3.1 とする。
* メンバーデータ ``buffer_id`` および ``index_buffer_id`` を、関数
  ``glGenBuffers`` 系の ID を管理するために宣言する。プログラムがそれらの生成時
  と削除時に参照する。
* メンバーデータ ``num_triangles`` は描画する多角形の頂点数を示すものだ。扱いと
  しては定数である。
* メンバーデータ ``texture`` は関数 ``glGenTextures`` の戻り値をキープしておくた
  めのものだ。
* メンバーデータ ``vao_id`` は頂点配列オブジェクト用だ。

メソッド ``get_shader_sources``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 81-86

メソッド ``get_shader_source`` は前述のシェーダープログラム初期化メソッドから呼
び出すためのテンプレートメソッドとする。頂点シェーダーやフラグメントシェーダーの
ソースコードをメンバーデータの辞書に設定する。

メソッド ``init_object``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 88-137

主に頂点バッファーオブジェクトを定義する。

次の段階を踏んでバッファーオブジェクトを構築していく。

#. NumPy の配列を活用して、描画するべき頂点の各種属性を定義する。
#. 定義した頂点データのアドレス的なものを PyOpenGL を用いて指定する。

まずは本コードで想定している ``vertices`` の「メモリレイアウト」について説明する。

例えば三角形を *N* 個描くものとする。このとき、座標と色のペアが *N* 個あることに
なる。サンプルコードにおける想定はこのようなものだ。

* 点の座標と色の表現をそれぞれ ``(x, y, z, w)`` および ``(R, G, B, A)`` で表現す
  ることにした。そして、一つの頂点データを ``(x, y, z, w, R, G, B, A)`` で表現す
  ることにした。
* 点・色の各成分の型を OpenGL の ``GL_FLOAT`` に相当する、NumPy の
  ``np.float32`` で表現することにした。
* 頂点データ全体を ``(x0, y0, z0, w0, R0, G0, B0, A0, ..., )`` のように直列して
  表現することにした。

結局は ``GL_FLOAT`` 型の 4 * 8 * *N* 要素からなる配列を作成することになるが、プ
ログラムでは

* ``np.array`` を配列バッファーとして、
* ``np.array.hstack`` を配列の単純連結操作として、
* ``np.array.astype`` を高精度の型 (e.g. ``float64``) から低精度の型 (e.g.
  ``float32``) へキャストするための操作として

適宜応用した。

描画するイメージ自体についてのプランはこうだ。

* 平面 z = 1 上の単位円周上に正 24 角形を描く。
* ``GL_TRIANGLE_FAN`` で原点 ``(0, 0)`` を中心としてファンとして描く。
* 頂点の色は配列のインデックスをベースに HSV で決める。中心は白にしておく。
* 頂点配列オブジェクトを新たに導入する。関数 ``glGenVertexArrays``,
  ``glBindVertexArray`` を用いる。
* 関数 ``glGenBuffers`` での実引数に注意。1 の場合はリストではなく、単なる整数が
  戻る。
* 関数 ``glBufferData`` の第二引数には NumPy の配列オブジェクトを直接指定でき
  る。便利。
* 旧式の関数 ``glVertexPointer``, ``glColorPointer`` に代え、現代的な
  ``glVertexAttribPointer`` を用いる。

  細かい説明は :doc:`tips` の ``ctypes`` の説明を参照。

* 以前メソッド ``do_render`` で呼び出していた ``glEnableClientState`` の代わるも
  のとして、関数 ``glEnableVertexAttribArray`` を導入する。

書かずもがなだが、本コードでは VBO を動的に切り替えるようなことはしないため、
VertexAttrib 系関数の呼び出しを初期化メソッドで済ませている。仮に複数種類の VAO
なり VBO なりを用意して、何か動的に切り替えるのであれば、バインド関数の呼び出し
を伴った上で、VertexAttrib 系関数の呼び出しをメソッド ``do_render`` に配置するか
もしれない。

メソッド ``init_texture``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 139-167

前半部では、ファイルシステムにある PNG ファイルからテクスチャーパターンを生成し
ている。これをフラグメントシェーダーの ``texture_sampler`` に送る。

後半部、関数 ``glTexImage2D`` 呼び出し以降は従来の OpenGL での手続き様式と同じで
ある。

メソッド ``do_render``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 169-174

上述のメソッドでがんばったおかげで、関数 ``glDrawElements`` の最後の引数は
``None`` で済むようになった。

メソッド ``cleanup``, ``destroy_vbo``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 176-200

* 関数 ``glDisableVertexAttribArray`` により、VBO を効かなくする。
* 関数 ``glBindBuffer`` で ``0`` を指定して VBO を効かなくしてから、関数
  ``glDeleteBuffers`` により、VBO を片付ける。
* 関数 ``glBindVertexArray`` で ``0`` を指定して VAO を効かなくしてから、関数
  ``glDeleteVertexArrays`` を用いて VAO を片付ける。
* 関数 ``glDeleteTextures`` でテクスチャーを片付ける。

一点注意。関数 ``glDeleteXXXs`` の第二引数は array-like を要求するので、困ったこ
とに関数 ``glGenXXXs`` で「一個だけ」名前を生成したときには、ここに示したように
利用したモノが一個だけでも、無理矢理それを含む array-like オブジェクトを作る必要
がある。

関数 ``main``
----------------------------------------------------------------------

.. literalinclude:: /_sample/pyopengl/shaderdemo.py
   :language: python3
   :lines: 202-211

このように各種パラメーターを指定して、クラス ``ShaderDemoApp`` のオブジェクトを
生成、実行をする。

実行する
======================================================================

スクリプトを実行すると、いつものように描画ウィンドウが出現する。それに加えて
Python 関数 ``print`` による情報がコンソールウィンドウに出力する。

表示されるグラフィックは次のようなものだ。マウスドラッグでズームや回転を試すこと
もできる。

.. figure:: /_images/pyopengl-shader-demo.png
   :alt: 初期状態
   :width: 308px
   :height: 327px
   :scale: 100%

.. figure:: /_images/pyopengl-shader-transform.png
   :alt: ズームと回転
   :width: 308px
   :height: 327px
   :scale: 100%

.. include:: /_include/python-refs-vision.txt

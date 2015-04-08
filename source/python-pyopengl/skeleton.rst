======================================================================
GLUT ベースのスケルトンを自作する
======================================================================
本稿では PyOpenGL_ のプログラムを書く際の「型」となるコードを考える。

.. contents::

スケルトン概要
======================================================================
しばらく PyOpenGL のデモコードを色々と書いていくことになる。単純な構造のプログラムを何本か書くという意味であり、それにはコードの重複を避けることが重要だ。

そこで、プログラム全体を一つのクラスにカプセル化した。それを次に示す。

.. literalinclude:: /_sample/pyopengl/glappbase.py
   :language: python3

このクラスの目的は次のとおりだ。

* 新しいサンプルコードを書くときは、このクラスのサブクラスを定義する形にすることで、コードの重複を積極的に少なくする。
  特にメソッドのオーバーライドにより、描画や操作の「差分」の実装だけで済むようにする。
* レガシーな API も最新のそれも、サブクラスでコンテキストバージョンを指定することで、利用可能とする。
* コンテキスト情報の出力や FPS の表示等、全サンプルコードが利用しがちな機能を提供する。

このクラスの利用方法は後述のページで見ていくことになるので、このページの残りでは、このクラス自体のポイントを記す。

機能概要
----------------------------------------------------------------------
* OpenGL のコンテキストバージョンをクラスのコンストラクターで指定できる。
* ウィンドウの初期サイズ、初期表示位置をクラスのコンストラクターで指定できる。
* ウィンドウ表示までに、次のような情報をコンソールに出力する。

  .. code-block:: console

     $ python34 glappbase.py
     Vendor: Intel
     Renderer: Intel(R) HD Graphics
     Version: 3.1.0 - Build 9.17.10.4101
     GLSL: 1.40 - Intel Build 9.17.10.4101

* ウィンドウリサイズ時に常に OpenGL のビューポートをウィンドウ全域に更新する。
* ウィンドウタイトルに FPS を 0.25 秒ごとに表示する。
* Esc キーを押すとウィンドウを閉じてアプリケーションを終了する。
* 各種コールバック関数群はサブクラスでオーバーライドできる。

補足
======================================================================
本節ではスケルトンのコードに出てくる PyOpenGL 固有の問題を言及する。

文字列の型について
----------------------------------------------------------------------
Python 3 では ``glutCreateWindow`` の実引数となる文字列 ``window_title`` の型に注意して欲しい。
素の文字列ではエラーが起こるのを避けるべく、接頭辞 ``b`` を付けている。

* 外部から文字列を受け取って、PyOpenGL の API に引数として渡す場合は ``.encode()`` する必要があるだろう。
* 関数 ``glGetString`` の戻り値の型も ``bytes`` のようなものになっている。
  関数 ``print`` で文字列をコンソールに出力したい等の場合は、戻り値を ``.decode()`` するとよい。

C 言語で配列に相当する型の実引数を与える
----------------------------------------------------------------------
何度も言うが型を示すサフィックスが省略できる。例えば ``glLightfv`` ではなく ``glLight`` でよい。

オリジナル版のインターフェイスと比べ、実引数の与え方がかなり柔軟になっている。
特に ``list``, ``tuple``, ``numpy.ndarray``, etc. を直接与えることが許されるので、存分に活用したい。

.. code-block:: python3

   from OpenGL.GL import *
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

.. include:: /_include/pyopengl-refs.txt

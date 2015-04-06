======================================================================
GLUT ベースのスケルトンを自作する
======================================================================
本稿では PyOpenGL_ のプログラムを書く際の「型」となるコードを考える。

.. todo::

   本稿を全面的に改訂する。内容が時代遅れになっている。

   * コードが取り扱う OpenGL のバージョンを明示する態度をとる。具体的に言うと関数
     ``glutInitContextVersion`` がスケルトン内になければならない。
   * ``glBegin`` 等のレガシー関数がスケルトン内に現れるのは当世風でないようだ。
     バージョン 3.x のコードとして通じない関数を排除したコードを改訂版スケルトンの条件としたい。

.. contents::

スケルトン概要
======================================================================
簡単な PyOpenGL プログラムの構造は次のようなものになる。
次のようなテキストファイルをテンプレートとして保存しておき、
新しいスクリプトを作成する際には、このテンプレートからコードを「増築」していくようにする。

.. literalinclude:: /_sample/pyopengl/skeleton.py
   :language: python3

仮に実行すると、黒い画面に赤い三角形が描画されているのが確認できるはずだ。
以降の各デモコードでは、このスケルトンの差分部分・修正部分を記述する。

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

.. include:: /_include/pyopengl-refs.txt

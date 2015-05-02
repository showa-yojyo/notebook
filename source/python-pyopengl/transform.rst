======================================================================
ベクトル・行列・座標変換
======================================================================
本稿では、ベクトル・行列・座標の変換を PyOpenGL 利用プログラムでどのように実現するかについて記す。

.. contents::

基本方針
======================================================================
* プログラムが採用するコンテキストバージョンによらず、
  ベクトル・行列を取り扱うのに ``np.array`` を積極的に用いる。
  ただし、単なる ``list`` や ``tuple`` で済む場合は、もちろんそれで間に合わせる。

  * ベクトルは shape が (n,) なインスタンスで表現する。
    ここで n は 2 か 3 か 4 になる。

  * 行列は shape が (4, 4) なインスタンスで表現する。

* プログラムは、行列の成分を「教科書の順序」で取り扱うものとする。
  つまり、普段は通常の ``np.array`` の形で保持しておく。
  そして、OpenGL のインターフェイスとアクセスする際に、
  内部配列のメモリレイアウトを NumPy 形式または
  OpenGL 形式 (column-major) に並び替えるものとする。

* 3.0 以上のコンテキストバージョンでは、OpenGL の行列の機能が全滅しているので、
  必要に応じて対応する機能を自作する。

``np.array`` の使いこなし方については、
:doc:`/python-numpy/index` で述べる。

OpenGL インターフェイスとアクセスする行列データについて
======================================================================
OpenGL は新旧共通で行列データを 16 要素の浮動小数点型数の配列として扱うことが圧倒的に多い。

旧式インターフェイスに行列データを設定する
----------------------------------------------------------------------
主に PyOpenGL 関数 ``glLoadMatrix`` および ``glMultMatrix`` に関しての話となる。
これらのインターフェイスに対して ``np.array`` を行列として引き渡す方法が 2 通り考えられる。

ひとつは次の擬似コードのように ``np.array.transpose`` を用いて、
内部配列を column-major に並び替えることによるものだ。

.. code-block:: python3

   matrix = np.identity(4)
   # Set matrix elements...

   glMatrixMode(GL_MODELVIEW)
   glLoadMatrixf(matrix.transpose())

もうひとつは、配列はそのままにして OpenGL の「転置バージョン」の行列関数、
つまり ``glLoadTransposeMatrix`` および ``glMultTransposeMatrix`` を利用するものだ。

.. code-block:: python3

   matrix = np.identity(4)
   # Set matrix elements...

   glMatrixMode(GL_MODELVIEW)
   glLoadTransposeMatrixf(matrix)

旧式インターフェイスから行列データを取得する
----------------------------------------------------------------------
OpenGL 側から行列データを受け取る方法について述べる。
いつものようにデータ取得には関数 ``glGetFloatv`` か ``glGetDoublev`` を用いるのだが、
PyOpenGL の場合はオリジナルとは異なり戻り値として配列を得ることに注意を要する。

そして、配列自体のメモリレイアウトの問題も設定時と同様に存在する。
ここでもメソッド ``.transpose`` を用いてかつシンボル ``GL_*_MATRIX`` を用いるか、
またはメソッド ``.transpose`` を用いずにシンボル ``GL_TRANSPOSE_*_MATRIX`` を用いるかの選択肢がある。

シェーダーオブジェクトに行列データを設定する
----------------------------------------------------------------------
頂点シェーダーのコードをこのように書くとする。

.. code-block:: glsl

   #version 330 core

   uniform mat4 camera;
   uniform mat4 projection;
   uniform mat4 rotation;

   ...

* 例えば ``uniform mat4 camera;`` という表現が「4 次正方行列 ``camera`` を扱う」ということを宣言するものだ。
  このオブジェクトの内容を設定するには、「外側」から OpenGL の関数を用いる必要がある。

   .. code-block:: python3

      def init_transform(self):
          # ...

          location = glGetUniformLocation(self.program_manager.program_id, b"camera"),
          glUniformMatrix4fv(
              location,
              1, GL_TRUE,
              self.camera_matrix)

* 関数 ``glUniformMatrix4fv`` の呼び出しが、行列データをシェーダープログラムに渡す処理である。

  * 関数 ``glGetUniformLocation`` にシェーダーにおける識別子を与えて、
    行列オブジェクトの「場所」を得る。アドレスのようなものだろう。
  * ``GL_TRUE`` は引数の行列を転置する、すなわち OpenGL 側に column-major 化してもらうことを意味する。
  * ``self.camera_matrix`` は別のところで設定済みの ``np.array`` オブジェクトという仮定である。

シェーダーオブジェクトから行列データを取得する
----------------------------------------------------------------------
先の例に対応する、行列データの取得コードは次のようなものになる。
受け取った後に ``.transpose`` をしないと、数学の教科書通りの並びにならない。

.. code-block:: python3

   camera_matrix = np.empty(4, dtype=np.float32)
   glGetUniformfv(
       self.program_manager.program_id,
       location,
       camera_matrix)
   assert np.allclose(camera_matrix.transpose(), self.camera_matrix)

座標変換を実装する
======================================================================
基本的には、変換を表現する行列を返す関数を実装し、
Python コードではそのオブジェクトを GLSL に渡したり、
その場で頂点座標を変換したりという利用を想定する。

自作する変換処理は別モジュール ``transform.py`` で定義することにする。
このモジュールが提供するいずれの自作関数も、返す行列 ``m`` が次の条件を満たすものとする。

* ``m`` は数学的には、同次座標系で表現された列ベクトルに左から作用する行列を表現する。
* ``m`` は ``np.array`` オブジェクトである。
* ``m.shape == (4, 4)``
* ``m.dtype == np.float64``

自作対象関数
----------------------------------------------------------------------
OpenGL 3.0 で deprecated にされた行列関連の関数と、自作するかどうかの対応表を記す。
ここで言う「自作」がどういう作業を意味するのかは、関数によって異なってくる。

===========================  ==============================================
関数                         対応
===========================  ==============================================
``glFrustum``                ``gluPerspective`` の対応をもって代える。
``glLoadIdentity``           ``glUniformMatrix4fv`` に単位行列 ``np.identity(4)`` を渡す。
``glLoadMatrix``             ``glUniformMatrix4fv`` に任意の (4, 4) 型 ``np.array`` を渡す。
``glLoadTransposeMatrix``    ``glUniformMatrix4fv`` に転置フラグ引数があるので、対応しない。
``glMatrixMode``             GLSL にこの概念がないので、対応しない。
``glMultMatrix``             ``np.array`` および GLSL に同等機能があるため、対応しない。
``glMultTransposeMatrix``    ``glUniformMatrix4fv`` に転置フラグ引数があるので、対応しない。
``glOrtho``                  平行投影は当分利用しないので、必要になるまで対応しない。
``glPopMatrix``              スタックの概念が不要なので対応しない。
``glPushMatrix``             スタックの概念が不要なので対応しない。
``glRotate``                 ``glUniformMatrix4fv`` と Quaternion を併用する。
``glScale``                  対応する。
``glTranslate``              対応する。
``gluLookAt``                是非対応する。
``gluOrtho2D``               平行投影は当分利用しないので、必要になるまで対応しない。
``gluPerspective``           是非対応する。
``gluPickMatrix``            当分利用しないので、必要になるまで対応しない。
``gluProject``               当分利用しないので、必要になるまで対応しない。
``gluUnproject``             当分利用しないので、必要になるまで対応しない。
===========================  ==============================================

そのモジュールでのインポート部一覧を示す。

.. literalinclude:: /_sample/pyopengl/transform.py
   :language: python3
   :lines: 17-18

いつものモジュール ``numpy`` だけではなく、
サブモジュールである ``numpy.linalg`` の機能も用いる。

関数 ``gluLookAt`` を真似る
----------------------------------------------------------------------
OpenGL のリファレンスをそのまま実装すればよい。

まず、与えられたカメラの位置、観測目標点、カメラの姿勢から正規直交基底を計算する。
それから、座標系原点を観測者の位置に移すような変換を加味する。

.. literalinclude:: /_sample/pyopengl/transform.py
   :language: python3
   :lines: 40-64

関数 ``gluPerspective`` を真似る
----------------------------------------------------------------------
OpenGL のリファレンスをそのまま実装すればよい。

コツは先述の基本方針に沿うべく -1 の成分が最下行にあるということだ。

.. literalinclude:: /_sample/pyopengl/rc/transform.py
   :language: python3
   :lines: 68-82

.. include:: /_include/pyopengl-refs.txt

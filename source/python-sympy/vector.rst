======================================================================
ベクトル
======================================================================
モジュール ``sympy.vector`` に関するメモを記す。
ベクトル代数というよりもベクトル解析寄りの機能が目立つという印象を受ける。

.. contents:: ノート目次

.. note::

   紙幅の都合上、出力を一部手で改行した。

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      init_printing(use_unicode=False, pretty_print=False)

基本編
======================================================================

座標系およびベクトル
----------------------------------------------------------------------
* 座標系としては現在は 3 次元直交座標系を表現するクラス ``CoordSysCartesian`` だけがある。
* オブジェクトの生成はコンストラクターでの直接生成でよい。
  その際には簡単な名前をつける。

以下 ``N`` をクラス ``CoordSysCartesian`` のオブジェクトとする。

* 座標系の基底ベクトルに次の方法でアクセスできる。

  * プロパティー ``N.i``, ``N.j``, ``N.k``
  * メソッド ``N.base_vectors``

* 一応記すが、各基底ベクトルは対応する座標軸に沿う長さ 1 のものである。
* 基底ベクトルはクラス ``BaseVector`` のオブジェクトである。
  これの「線形結合」を表現しようとすると、SymPy 的には
  ``BaseVector``, ``VectorAdd``, ``VectorMul`` オブジェクトの composite になる。

* 名前が紛らわしいので要注意だが、これらのベクトル関連クラスの基底クラスが ``Vector`` である。

* 零ベクトルは ``Vector.zero`` オブジェクトで表現されている。

以下 ``u`` および ``v`` をベクトルオブジェクトとする。

* ベクトルのドット積は次のどちらかで表現する。

  * ``u.dot(v)``
  * ``u & v``

* ベクトルのクロス積は次のどちらかで表現する。

  * ``u.cross(v)``
  * ``u ^ v``

ベクトルに対する SymPy 演算
----------------------------------------------------------------------
``Vector`` オブジェクトに対して、次の関数およびクラスによる SymPy 演算を適用することができる。
ベクトルの各要素ごと、つまり各基底ベクトルの係数に演算がそれぞれ作用する。

* ``simplify``
* ``trigsimp``
* ``factor``
* ``diff``, ``Derivative``
* ``integrate``, ``Integral``

点
----------------------------------------------------------------------
ある座標系に点を生成することができるのだが、少し特徴的な方法による。

* プロパティー ``origin`` が座標系原点を表現する。
  すなわち ``N.origin`` は座標系 ``N`` の原点を意味する。
  このオブジェクトの型がクラス ``Point`` である。

* 新しく点を生成するには、この原点なり既存の点なりのメソッド ``locate_new`` を用いる。
  引数にはその点から生成したい点への変位をベクトルで指定する。

以下 ``P``, ``Q`` をクラス ``Point`` のオブジェクトとする。

* メソッド ``position_wrt`` を用いて位置ベクトルを得られる。
  点 ``P`` の ``Q`` に対する位置ベクトルは ``P.position_wrt(Q)`` である。

* メソッド ``express_coordinates`` により、点の座標を得られる。
  引数は座標系を指定する。

設計は常識的なのだが、実際使うときにはクセがあるように感じられる。
点を生成するのも、その位置を確認するのも、
基本的な操作のはずなのだが、その割には手間がかかる。

二項テンソル
----------------------------------------------------------------------
ベクトル同士の二項テンソルをオブジェクトとして表現するクラス ``Dyadic`` がある。

* オブジェクトをコンストラクターで直接生成することはまれであり、
  通常は ``Vector`` のメソッド ``outer`` もしくは演算子 ``|`` により生成する。

  .. code-block:: ipython

     In [1]: from sympy.vector import CoordSysCartesian

     In [2]: N = CoordSysCartesian('N')

     In [3]: a = sum((i * j for i, j in zip(symbols('a0:3'), N.base_vectors())), Vector.zero)

     In [4]: b = sum((i * j for i, j in zip(symbols('b0:3'), N.base_vectors())), Vector.zero)

     In [5]: a | b # i.e. a.outer(b)
     Out[5]: a0*b0*(N.i|N.i) + a0*b1*(N.i|N.j) + a0*b2*(N.i|N.k)
           + a1*b0*(N.j|N.i) + a1*b1*(N.j|N.j) + a1*b2*(N.j|N.k)
           + a2*b0*(N.k|N.i) + a2*b1*(N.k|N.j) + a2*b2*(N.k|N.k)

* ``Dyadic`` の関連クラスは ``Vector`` のそれと酷似している。
  すなわち ``BaseDyadic``, ``DyadicAdd``, ``DyadicMul``, etc. である。

* 零元はオブジェクト ``Dyaric.zero`` で表現している。

* ベクトルのスカラー積、クロス積とも混ぜて利用可能。

  .. code-block:: ipython

     In [6]: c = sum((i * j for i, j in zip(symbols('c0:3'), N.base_vectors())), Vector.zero)

     In [7]: a.dot(b.outer(vc))
     Out[7]: (a0*b0*c0 + a1*b1*c0 + a2*b2*c0)*N.i
           + (a0*b0*c1 + a1*b1*c1 + a2*b2*c1)*N.j
           + (a0*b0*c2 + a1*b1*c2 + a2*b2*c2)*N.k

複数座標系
======================================================================
既存の座標系オブジェクト ``N`` から、新たに別の座標系オブジェクト ``M`` を生成することができる。

並進のみ
----------------------------------------------------------------------
メソッド ``CoordSysCartesian.locate_new`` を呼ぶと新しく ``CoordSysCartesian`` オブジェクトを生成できる。

* 引数には座標系の名前と、基準となる座標系の原点からの変位をベクトルで指定する。
* ``N`` に対する ``M`` の変位を得るには、次のどちらかを行う。

  * ``M.position_wrt(N)``
  * ``M.origin.express_coordinates(N)``

回転のみ
----------------------------------------------------------------------
次は新たな座標系に回転（だけ）を施す。

* ``M = N.orient_new_axis('M', theta, v)`` のようにすれば、
  座標系 ``M`` に対してベクトル ``v`` 周りに角度 ``theta`` だけ回転して得られる座標系 ``N`` を生成する。

  ``v`` に関しては細かい条件が不明。

その他にも次のようなメソッドにより、新しい座標系を生成できる。

* ``orient_new_body``
* ``orient_new_space``
* ``orient_new_quaternion``

より一般的には、メソッド ``orient_new`` および以下のクラスのオブジェクトを用いる。

* ``AxisOrienter``
* ``BodyOrienter``
* ``SpaceOrienter``
* ``QuaternionOrienter``

生成手順は ``M = N.orient_new(name, (orienter1, orienter2, ...))`` である。

* 以上の 4 つの座標変換について、新旧座標系の原点は一致している。
* ``N.rotation_matrix(M)`` にて、回転変換を表現する 3 次正則行列を得られる。
  すべての上記 4 つの座標変換について、行列式の絶対値が 1 になると思われる。

並進と回転
----------------------------------------------------------------------
最後に並進と回転を組み合わせる方法を記す。

* メソッド ``orient_new`` およびその仲間たちには、キーワード引数 ``locate`` が指定できる。
  これを用いて変位量をベクトルで与えれば、
  新しい座標系は、原点の周りに指定の回転を施された後、指定の変位だけ移動したものになる。

* 関数 ``express`` を用いて、一方の座標系の座標を他方の座標系のそれで表現できる。
  呼び出し形式は ``express(point, coord_sys)`` である。

スカラー場とベクトル場
======================================================================
内容が若干 :doc:`./diffgeom` で見てきた微分形式と外積周りの話題と重複する。

* 座標系 ``R`` でのスカラー場やベクトル場を構成するには、
  クラス ``BaseScalar`` のオブジェクトである
  ``R.x``, ``R.y``, ``R.z`` を用いる。

ナブラ
----------------------------------------------------------------------
クラス ``CoordSysCartesian`` のプロパティー ``delop`` がナブラを表現する。

例を示す。

.. code-block:: ipython

   In [1]: from sympy.vector import CoordSysCartesian

   In [2]: N = CoordSysCartesian('N')

   In [3]: f = Function('f')(N.x, N.y, N.z); f
   Out[3]: f(N.x, N.y, N.z)

   In [4]: N.delop(p)
   Out[4]: (Derivative(f(N.x, N.y, N.z), N.x))*N.i
         + (Derivative(f(N.x, N.y, N.z), N.y))*N.j
         + (Derivative(f(N.x, N.y, N.z), N.z))*N.k

回転 curl, rot
----------------------------------------------------------------------
3 次元空間のベクトルの回転を計算する方法がふたつある。

* メソッド ``delop.cross`` を用いる。
* 関数 ``curl`` を用いる。

例を示す。

.. code-block:: ipython

   In [1]: from sympy.vector import CoordSysCartesian, curl

   In [2]: N = CoordSysCartesian('N')

   In [3]: fx, fy, fz = [i(N.x, N.y, N.z) for i in symbols('fx fy fz', type=Function)]

   In [4]: curl(fx * N.i + fy * N.j + fz * N.k, N)
   Out[4]: (-Derivative(fy(N.x, N.y, N.z), N.z) + Derivative(fz(N.x, N.y, N.z), N.y))*N.i
         + (Derivative(fx(N.x, N.y, N.z), N.z) - Derivative(fz(N.x, N.y, N.z), N.x))*N.j
         + (-Derivative(fx(N.x, N.y, N.z), N.y) + Derivative(fy(N.x, N.y, N.z), N.x))*N.k

   In [5]: N.delop.cross(fx * N.i + fy * N.j + fz * N.k) == _
   Out[5]: True

発散 div
----------------------------------------------------------------------
3 次元空間のベクトルの発散を計算する方法がふたつある。

* メソッド ``delop.dot`` を用いる。
* 関数 ``divergence`` を用いる。

例を示す。

.. code-block:: ipython

   In [1]: from sympy.vector import CoordSysCartesian, divergence

   In [2]: # Create N, fx, fy, and fz...

   In [3]: divergence(fx * N.i + fy * N.j + fz * N.k, N)
   Out[3]: Derivative(fx(N.x, N.y, N.z), N.x)
         + Derivative(fy(N.x, N.y, N.z), N.y)
         + Derivative(fz(N.x, N.y, N.z), N.z)

   In [4]: N.delop.dot(fx * N.i + fy * N.j + fz * N.k) == _
   Out[4]: True

勾配 grad
----------------------------------------------------------------------
* メソッド ``delop.gradient`` を用いる。
* 関数 ``gradient`` を用いる。

例を示す。

.. code-block:: ipython

   In [1]: from sympy.vector import CoordSysCartesian, gradient

   In [2]: # Create N, and f(x, y, z).

   In [3]: gradient(f, N)
   Out[3]: (Derivative(f(N.x, N.y, N.z), N.x))*N.i
         + (Derivative(f(N.x, N.y, N.z), N.y))*N.j
         + (Derivative(f(N.x, N.y, N.z), N.z))*N.k

   In [4]: N.delop.gradient(f) == _
   Out[4]: True

方向微分
----------------------------------------------------------------------
方向微分は ``(v.dot(coord_sys.delop))(field)`` のようにする。ここで、

* ``coord_sys`` はクラス ``CoordSysCartesian`` オブジェクト、
* ``v`` は ``coord_sys`` 上のクラス ``Vector`` オブジェクト、
* ``field`` は ``coord_sys.base_scalars()`` で表現されているスカラー場なりベクトル場である。

例を示す。

.. code-block:: ipython

   In [1]: # Create N, a, b, f(x, y, z), fx, fy, and fz.

   In [2]: (a.dot(N.delop))(f)
   Out[2]: a0*Derivative(f(N.x, N.y, N.z), N.x)
         + a1*Derivative(f(N.x, N.y, N.z), N.y)
         + a2*Derivative(f(N.x, N.y, N.z), N.z)

   In [3]: (b.dot(N.delop))(fx * N.i + fy * N.j + fz * N.k)
   Out[3]: (b0*Derivative(fx(N.x, N.y, N.z), N.x) + b1*Derivative(fx(N.x, N.y, N.z), N.y) + b2*Derivative(fx(N.x, N.y, N.z), N.z))*N.i
         + (b0*Derivative(fy(N.x, N.y, N.z), N.x) + b1*Derivative(fy(N.x, N.y, N.z), N.y) + b2*Derivative(fy(N.x, N.y, N.z), N.z))*N.j
         + (b0*Derivative(fz(N.x, N.y, N.z), N.x) + b1*Derivative(fz(N.x, N.y, N.z), N.y) + b2*Derivative(fz(N.x, N.y, N.z), N.z))*N.k

演習
======================================================================

.. todo:: 何かやる。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt

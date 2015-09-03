======================================================================
ベクトル
======================================================================
モジュール ``sympy.vector`` に関するメモを記す。
ベクトル解析寄りの機能が目立つという印象を受ける。
もっと言うと 3 次元空間用の座標系だけを利用の対象と想定している節がある。

.. contents:: ノート目次

.. note::

   紙幅の都合上、出力を一部手で改行した。

   本文中のすべての IPython セッション中のサンプルコードで、
   以下の出力書式設定が済んでいるものとする。

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

* 一応記すが、各基底ベクトルは対応する座標軸に沿う長さ 1 のものである。正規直交基底。
* 基底ベクトルはクラス ``BaseVector`` のオブジェクトである。
  これの「線形結合」を表現しようとすると、SymPy 的には
  ``BaseVector``, ``VectorAdd``, ``VectorMul`` オブジェクトの composite になる。

* 名前が紛らわしいので要注意だが、これらのベクトル関連クラスの基底クラスが ``Vector`` である。

* 零ベクトルは ``Vector.zero`` オブジェクトで表現されている。

以下 ``u`` および ``v`` をベクトルオブジェクトとする。

* ベクトルのドット積 :math:`\mathbf{u} \cdot \mathbf{v}` は次のどちらかで表現する。

  * ``u.dot(v)``
  * ``u & v``

* ベクトルのクロス積 :math:`\mathbf{u} \times \mathbf{v}` は次のどちらかで表現する。

  * ``u.cross(v)``
  * ``u ^ v``

オブジェクト指向プログラミング言語のコードでベクトルをクラスとして表現することはしばしばある。
演算子オーバーロードをサポートする言語では、
このふたつの積を計算する処理を演算子として実装することが多い。
その時は常にプログラマーは演算子の優先順位に注意することになる。

* ベクトルの長さはメソッド ``magnitude()`` を用いる。
* ベクトルの長さを単位化するメソッドは ``normalize()`` である。
  新しいベクトルを返し、自分自身は変わらない。
* ベクトルの成分はプロパティー ``components`` で確認できる。
  ただし型が ``dict`` で使い勝手に疑問点がある。
  キーが ``BaseVector`` オブジェクトで、値が係数すなわち成分である。
  こういう設計になっている理由は、
  「関連のない別々の座標系からとってきたベクトルの和」のようなオブジェクトが許されることから来るものと思う。

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
モデリングソフト等でお馴染みの方法論でもある。

並進のみによる指定
----------------------------------------------------------------------

メソッド ``locate_new(name, position, vector_names=None, variable_names=None)``
  新しく ``CoordSysCartesian`` オブジェクトを生成できる。

  * 引数 ``name`` は座標系の名前を指定する。主にデバッグ作業用？
  * 引数 ``position`` にはその点から生成したい点への変位をベクトルで指定する。
  * 残りのキーワード引数は ``base_vectors`` と ``base_scalars`` の名前のためのもの。

* ``N`` に対する ``M`` の変位を得るには、次のどちらかを行う。

  * ``M.position_wrt(N)``
  * ``M.origin.express_coordinates(N)``

回転のみによる指定
----------------------------------------------------------------------
次は新たな座標系に回転（だけ）を施す。

メソッド ``orient_new_axis(name, angle, axis, location=None, vector_names=None, variable_names=None)``
  座標系 ``M`` に対してベクトル ``axis`` 周りに角度 ``angle`` だけ回転して得られる座標系 ``N`` を生成する。

  * ``axis`` に関しては細かい条件が不明。零ベクトルだとアウトなことは想像できる。
  * ``location`` にベクトルを指定すると、回転プラス並進となるが、後述。

その他にも次のようなメソッドにより、新しい座標系を生成できる。

メソッド ``orient_new_body(name, angle1, angle2, angle3, rotation_order, ...)``
  座標系を 3 回の座標軸周りの回転により生成する。

  * 引数 ``angle1``, ``angle2``, ``angle3`` が各座標軸に関する回転角を表す。
  * 引数 ``rotation_order`` が回転を施す座標軸の順序を示す文字列。
    例えば x, z, y 軸の順に回転する場合は ``'132'`` または ``'XZY'`` を指定する。
  * 回転軸が新座標系のそれを基準とすることに注意。
    最初の回転は新旧一致しているが、次の回転は前の回転の影響を受けている。

メソッド ``orient_new_space(name, angle1, angle2, angle3, rotation_order, ...)``
  上のものと似ているが、回転の基準が 3 回転とも ``M`` の座標軸に沿う。

メソッド ``orient_new_quaternion(name, q0, q1, q2, q3, ...)``
  Hamilton の四元数による回転を与えて新たな座標系を生成する。

  単位ベクトル :math:`(n_x, n_y, n_z)` の周りに角度 :math:`\theta` だけの回転を表す四元数は

  .. math::
     :nowrap:

     \left(\cos \frac{\theta}{2},\,
           n_x \sin \frac{\theta}{2},\,
           n_y \sin \frac{\theta}{2},\,
           n_z \sin \frac{\theta}{2}\right)

  となる。この各成分を ``q0`` から ``q3`` までこの順序で指定する。

より一般的には、メソッド ``orient_new`` および以下のクラスのオブジェクトを用いる。

* ``AxisOrienter``
* ``BodyOrienter``
* ``SpaceOrienter``
* ``QuaternionOrienter``

生成手順は ``M = N.orient_new(name, (orienter1, orienter2, ...))`` である。

* 以上の 4 つの座標変換について、新旧座標系の原点は一致している。
* ``N.rotation_matrix(M)`` にて、回転変換を表現する 3 次正則行列を得られる。
  すべての上記 4 つの座標変換について、行列式の絶対値が 1 になると思われる。

  ここでは控えめに絶対値と言ったが、
  座標系の向きがどの変換でも右手系（オリジナルの向き）を保つならば真に 1 になる。
  現在確認中。

並進と回転による指定
----------------------------------------------------------------------
最後に並進と回転を組み合わせる方法を記す。

* メソッド ``orient_new`` およびその仲間たちには、キーワード引数 ``locate`` が指定できる。
  これを用いて変位量をベクトルで与えれば、
  新しい座標系は、原点の周りに指定の回転を施された後、指定の変位だけ移動したものになる。

* 関数 ``express`` を用いて、一方の座標系の座標を他方の座標系のそれで表現できる。
  呼び出し形式は ``express(point, coord_sys)`` である。

関数 ``express``
----------------------------------------------------------------------
関数 ``express`` が指定の座標系の表現に書き直せるのは点やベクトルだけではない。

* ベクトルを含む SymPy 式
* ``Dyaric`` オブジェクト

  * 座標系オブジェクトを 2 個引数として渡せる。
    特に、引数の二項テンソルがふたつの座標系にまたがるようなものに対して有効。

* ``BaseScalar`` オブジェクト

  * ポイントはキーワード引数 ``variables=True`` を指定すること。
    例えば座標系 ``N`` で定義したスカラー場を ``M`` での表現に書き直せる。

スカラー場とベクトル場
======================================================================
内容が若干 :doc:`./diffgeom` で見てきた微分形式と外積周りの話題と重複する。

* 座標系 ``R`` でのスカラー場やベクトル場を構成するには、
  クラス ``BaseScalar`` のオブジェクトである
  ``R.x``, ``R.y``, ``R.z`` を用いる。

ナブラ
----------------------------------------------------------------------
クラス ``CoordSysCartesian`` のプロパティー ``delop`` がナブラ :math:`\nabla` を表現する。
英語圏の人はこれをデルと呼ぶことが多い。
そしてみんなが知っているが、小文字の ``del`` は Python の予約語である。

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

回転
----------------------------------------------------------------------
3 次元空間のベクトルの回転 :math:`\nabla \times \mathbf{F}` を計算する方法がふたつある。

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

発散
----------------------------------------------------------------------
3 次元空間のベクトルの発散 :math:`\nabla \cdot \mathbf{F}` を計算する方法がふたつある。

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

勾配
----------------------------------------------------------------------
3 次元空間上の実数値関数の勾配 :math:`\nabla f` を計算する方法がふたつある。

* メソッド ``delop.gradient`` を用いる。
* 関数 ``gradient`` を用いる。

例を示す。
または関数メソッド ``gradient`` を呼ぶことで、
スカラー関数から勾配ベクトル場オブジェクトが生成できている。

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

ポテンシャル
----------------------------------------------------------------------
関数 ``is_conservative(field)``
  ベクトル場が保存場であるかどうかをテストする。

  * 実装は ``curl(field, coord_sys) == Vector.zero`` を丁寧に調べている。

関数 ``is_solenoidal(field)``
  ベクトル場がソレノイド場であるかどうかをテストする。

  * 実装は ``divergence(field, coord_sys) == 0`` を丁寧に調べている。

関数 ``scalar_potential(field, coord_sys)``
  保存場に関するスカラーポテンシャルを（積分定数を除いて）求める。

  * 実装では実際に各座標軸の区間ごとに積分を一度ずつ都合 3 回計算している。

関数 ``scalar_potential_difference(field, coord_sys, point1, point2)``
  保存場に関する指定 2 点間のポテンシャルの差を計算する。
  引数は保存ベクトル場でも、そのスカラーポテンシャルでもよい。

  * ``point2`` でのポテンシャルと ``point1`` でのそれとの差。

演習
======================================================================
3 次元空間上のベクトル場
:math:`\mathbf{F} = 2 x y^3 z^4 \mathbf{i} + 3 x^2 y^2 z^4 \mathbf{j} + 4 x^2 y^3 z^3 \mathbf{k}`
が保存場であることを確認し、そのスカラーポテンシャルを先述の関数で求める。
また、このベクトル場の始点と終点をそれぞれ :math:`P_0(0, 0, 0)` と :math:`P_1(10, 10, 10)` とする、
何らかの経路上の線積分を関数 ``scalar_potential_difference`` を利用して求める手続きの例を示す。

.. code-block:: ipython

   In [1]: from sympy.vector import *

   In [2]: N = CoordSysCartesian('N')

   In [3]: F = (2 * N.x * N.y**3 * N.z **4) * N.i\
      ....: + (3 * N.x**2 * N.y**2 * N.z**4) * N.j\
      ....: + (4 * N.x**2 * N.y**3 * N.z** 3) * N.k

   In [4]: is_conservative(F)
   Out[4]: True

   In [5]: f = scalar_potential(F, N); f
   Out[5]: N.x**2*N.y**3*N.z**4

   In [6]: p0 = N.origin

   In [7]: p1 = N.origin.locate_new(10 * N.i + 10 * N.j + 10 * N.k)

   In [8]: scalar_potential_difference(f, N, p0, p1)
   Out[8]: 1000000000

* [1] 面倒なので全てをインポートする。
* [3] この保存ベクトル場は `Paul's Online Math Notes <http://tutorial.math.lamar.edu/Classes/CalcIII/ConservativeVectorField.aspx>`_ から拝借した。
* [5] 求めたスカラーポテンシャルには定数項が表現されていないので注意。
* [7] どう考えても点の座標の指定が面倒だ。
* [8] ここでは上品に求めたばかりのスカラーポテンシャルを引数として指定したが、
  先述のように ``F`` を直接渡してよい。その場合は上における [5] が不要になる。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt

======================================================================
微分幾何
======================================================================
微分幾何に関係する機能を提供するモジュール ``sympy.diffgeom`` に関するメモを記す。

これはふたつのサブモジュール ``diffgeom`` と ``rn`` から構成されている。
理解の都合上、まず ``diffgeom`` に定義されている基礎的な諸クラスを見ていく。
次にサブモジュール ``rn`` で定義されているすべてのオブジェクトを見ていく。
最後に再度 ``diffgeom`` に戻り、残りの（さらに複雑な概念を表現する）諸機能を見ていく。

.. contents:: ノート目次

.. note::

   本文中のすべての IPython セッション中のサンプルコードで、
   以下のインポートおよび出力書式設定が済んでいるものとする。

   .. code-block:: python3

      from sympy.diffgeom import *
      from sympy.diffgeom.rn import *
      init_printing(pretty_print=False)

多様体
======================================================================
本節ではサブモジュール ``sympy.diffgeom.diffgeom`` で定義されている、
多様体を表現するための一連のクラス群について記す。

クラス Manifold
----------------------------------------------------------------------
クラス Manifold は多様体をオブジェクトとして表現する。

* オブジェクトをコンストラクターから直接生成する。
  名前と多様体次元さえ用意すればよい。
  生成後にそれぞれをメンバーデータ :code:`name` および :code:`dim` で参照できる。

* メンバーデータ :code:`patches` から構成パッチオブジェクトにアクセスできる。
  これは後述する Patch オブジェクトの list オブジェクトである。

クラス Patch
----------------------------------------------------------------------
クラス Patch は多様体オブジェクトの構成要素をオブジェクトとして表現する。

* オブジェクトをコンストラクターから直接生成する。
  この際、名前と自身が所属する Manifold オブジェクトが必要となる。
  生成後にそれぞれをメンバーデータ :code:`name` および :code:`manifold` で参照できる。

* メンバーデータ :code:`coord_systems` から座標系オブジェクトにアクセスできる。
  これは後述する CoordSystem オブジェクトの list オブジェクトである。

* 多様体次元はプロパティー :code:`dim` を用いて参照可能。

クラス CoordSystem
----------------------------------------------------------------------
クラス CoordSystem は多様体パッチのひとつの座標系をオブジェクトとして表現する。

* オブジェクトをコンストラクターから直接生成する。
  座標系の名前と関連付けるパッチオブジェクトが要る。

  * 他にもオプションで :code:`names` というのがある。
    これは座標成分の名称を list で指定することができる。

* 多様体次元はプロパティー :code:`dim` を用いて参照可能。

このクラスは特に重要なメソッドが多い。
強いて言えば、座標情報と座標変換に関係するものに分類したい。

座標情報にアクセスするメソッドは次のようなものがある。

:code:`coord_function(coord_index)`, :code:`coord_functions()`
  点を取り、その点の特定の座標を返す関数オブジェクトを返す。

  * 後述のクラス BaseScalarField を参照。

  * 単数形の方は :code:`coord_index` 番目の座標成分のものに関するそれを返す。
    例えば直交座標系で ``0``, ``1`` はそれぞれ x, y 座標。

  * 複数形の方は全成分を list で返す。

:code:`base_vector(coord_index)`, :code:`base_vectors()`
  基底ベクトルを返す。
  後述のクラス BaseVectorField を参照。

:code:`base_oneform(coord_index)`, :code:`base_oneforms()`
  基底微分 1-形式を返す。
  外積代数の生成元である。
  後述のクラス Differential を参照。

座標変換メソッドは次のようなものがある。

:code:`connect_to(to_sys, from_coords, to_exprs, inverse=True, fill_in_gaps=False)`
  当座標系から座標系 :code:`to_sys` への座標変換を定義する。

  * 利用例を知るならモジュール ``rn`` を見るのが最良。

:code:`coord_tuple_transform_to(to_sys, coords)`
  この座標系における座標 :code:`coords` を
  指定座標系 :code:`to_sys` でのそれに変換する。

  * 戻り値は Matrix オブジェクトとなる。
    座標を表現するために便宜上この型を用いている。

:code:`point_to_coords(point)`
  既存の（おそらくは別座標系にある）点オブジェクトから、
  この座標系での座標を得る。

  * 戻り値は Matrix オブジェクトとなる。

:code:`jacobian(to_sys, coords)`
  当座標系から座標系 :code:`to_sys` に関する Jacobi 行列を求める。
  先程から Matrix 型が頻出しているのは、このメソッドとの相性のためだろう。

利用例は後述する。

クラス Point
----------------------------------------------------------------------
多様体パッチ上の一点をオブジェクトとして表現する。

* オブジェクトの生成方法はふたつある。
  このクラスのコンストラクターから直接生成する方法と、
  クラス CoordSystem のメソッド :code:`point` を呼ぶ方法だ。

  * 直接生成の場合、座標系オブジェクトと座標を要する。
    前者はもちろん CoordSystem オブジェクトであり、
    後者は単に座標成分を list で渡せばよい。

  * メソッド :code:`CoordSystem.point` の場合は座標成分だけあればよい。

* メソッド :code:`coords` を用いれば、この点の座標系が得られる。

  * オプションとして別の座標系 :code:`to_sys` を与えると、
    座標変換後の座標を得ることも可能だ。
    これには前述のクラス CoordSystem のメソッド :code:`coord_tuple_transform_to` が用いられる。

スカラー場、ベクトル場、外微分
======================================================================
こちらも利用例は後述することにする。

クラス BaseScalarField
----------------------------------------------------------------------
多様体上のスカラー場をオブジェクトとして表現するための基になるクラス。

* コンストラクターでオブジェクトを生成する場合、
  CoordSystem オブジェクトと座標成分番号 `i` を指定する。

  例えば 3 次元直交座標系の y 成分 (:code:`i = 1`) スカラー場を生成する、
  というような構成をする。

* 丸括弧で評価するときの引数は Point オブジェクトである。
  点オブジェクトは任意の座標系で表現されていて構わない。
  戻り値はスカラーだが、座標系の第 `i` 成分に相当する値を示す。

* BaseScalarField オブジェクトを（算術演算等で）組み合わせて、
  単に座標成分を返すだけでない、より一般的なスカラー場を構成することもできる。

クラス BaseVectorField
----------------------------------------------------------------------
このクラスが表現するのは接ベクトルの基底だと思われる。
つまり接ベクトル :math:`\displaystyle \sum_{i=0} a_i \left(\frac{\partial}{\partial x_i}\right)_p` の
:math:`\frac{\partial}{\partial x_i}` の部分を表現している。

このクラスはベクトル場を表現するための素材に過ぎない。
ベクトル場自体を表現するものではない。

* コンストラクターでオブジェクトを生成する方法は BaseScalarField と同じだ。
  座標系とどの座標成分に関するものなのかを指定する。

* 丸括弧で評価するときの引数と戻り値の型は両方ともスカラー的な値である。
  ある点 :code:`p` における座標成分 `i` に関する方向微分を得るには、
  基底接ベクトル :code:`vi` を生成した後、結果的に二段階評価を行う。
  すなわち :code:`vi(f).rcall(p)` である。

  * 見慣れぬ :code:`rcall` は丸括弧のようなものなので、気にしないでよい。

  * このクラスのオブジェクトを「線形結合」することはできでも、
    その型が単なる SymPy の Add オブジェクトに過ぎないので、
    「接ベクトル」に丸括弧をつけて評価することができない。
    丸括弧の代わりに :code:`rcall()` を用いる。

クラス Commutator
----------------------------------------------------------------------
ふたつのベクトル場の交換子を表現する。

* :code:`Commutator(v1, v2)` は
  :math:`v_1(v_2(f)) - v_2(v_1(f))` で定義されるベクトル場を意味する。
  :code:`f` は多様体上のスカラー場。

  * 丸括弧で :code:`f` を評価する前に、交換子オブジェクトがゼロでないことを確認する必要がある。

* ドキュメントにあるように、現行の実装は少々弱いようだ。
  展開し切れないケースがままある。

クラス Differential
----------------------------------------------------------------------
クラス Differential は外微分を意味する。
スカラー関数を含む微分形式の外微分をオブジェクトとして表現する。

* コンストラクターには k-形式として扱えるオブジェクトを渡す。
  ここで k はゼロ以上。

  * 既存の Differential オブジェクトでもかまわないが、結果的にゼロが返る。

  * 先述したメソッド :code:`CoordSystem.base_oneforms` が返すのは
    0-形式 :code:`f_i = BaseScalarField(coord, i)` の外微分となる
    1-形式 :code:`Differential(f_i)` をすべての `i` 成分について生成したものに他ならない。

  * 実数値関数 :code:`f` からは全微分 :code:`df` が得られる。
    任意のベクトル :code:`v` について :code:`df(v) == v(f)` が成り立つ。

* 丸括弧で評価する際のオペランドはスカラー関数オブジェクトまたは「接ベクトル」でよい。
  今度は BaseVectorField オブジェクトの線形結合で通じるし、
  オブジェクトを次元個分カンマ区切りで可変個引数的に渡してもよい。
  同じ結果が得られると期待してよろしい。

* 実装に Commutator を用いる。

クラス TensorProduct
----------------------------------------------------------------------
クラス TensorProduct は k-形式のテンソル積を表現するクラス。

* コンストラクターの引数は k-形式オブジェクトである。複数個渡してよい。

  * 言い忘れたが、k-形式として認められる型はだいたい次のような感じらしい。

    * 定数
    * Function オブジェクト
    * BaseScalarField オブジェクト
    * Differential オブジェクト

* 丸括弧の引数はベクトル場オブジェクトである。
* 戻り値の型もまた TensorProduct であるのだが、
  状況により Mul になったり、あるいは定数になったりする。
  このときは丸括弧は使えない。

クラス WedgeProduct
----------------------------------------------------------------------
クラス WedgeProduct は微分形式オブジェクト同士の wedge 積を表現するクラス。

* スーパークラスは TensorProduct だが、混ぜて使わないこと。
  前項で注意した点がそのまま当クラスの注意点でもある。

* 積分の文脈上に限り、反対称性がまともに扱われるとのこと。
  この注意は、例えば

  * :code:`WedgeProduct(X, X)` のようなオブジェクトを生成しても、
    直ちにゼロと評価されたりしない

  * :code:`WedgeProduct(X, Y)` と :code:`-WedgeProduct(Y, X)` が等しくならない

  という現象を説明するものだろうか。

定義済み多様体オブジェクト
======================================================================
本節ではサブモジュール ``sympy.diffgeom.rn`` に定義されているオブジェクトを見ていく。

前節で述べた一連の機能をすぐに試したいが、オブジェクト生成が面倒で困る。
そこで、ここにある定義済みオブジェクトをインポートすることが考えられる。
それらのオブジェクトを試して、感触を確かめるのがよいだろう。

.. csv-table::
   :delim: @
   :header: オブジェクト, クラス, 名前, 意味
   :widths: 8, 10, 10, 16

   :code:`R2`@Manifold@``'R^2'``@:math:`\RR^2`
   :code:`R2_origin`@Patch@``'origin'``@:code:`R2` のパッチ
   :code:`R2_r`@CoordSystem@``'rectangular'``@:code:`R2_origin` の直交座標系
   :code:`R2_p`@CoordSystem@``'polar'``@:code:`R2_origin` の極座標系
   :code:`R3`@Manifold@``'R^3'``@:math:`\RR^3`
   :code:`R3_origin`@Patch@``'origin'``@:code:`R3` のパッチ
   :code:`R3_r`@CoordSystem@``'rectangular'``@:code:`R3_origin` の直交座標系
   :code:`R3_c`@CoordSystem@``'cylindrical'``@:code:`R3_origin` の円柱座標系
   :code:`R3_s`@CoordSystem@``'spherical'``@:code:`R3_origin` の球座標系

2 次元オブジェクト
----------------------------------------------------------------------
:code:`R2`, :code:`R2_origin`, :code:`R2_r`, :code:`R2_p` には
可能な限り次に示すメンバーデータが付与されている。
可能な限りというのは「座標系 A 由来のデータは座標系 B には付与しない」という意味だ。

:code:`x`, :code:`y`
  :code:`R2_r.coord_functions()` から値を設定。

:code:`e_x`, :code:`e_y`
  :code:`R2_r.base_vectors()` から値を設定。

:code:`dx`, :code:`dy`
  :code:`R2_r.base_oneforms()` から値を設定。

:code:`r`, :code:`theta`
  :code:`R2_p.coord_functions()` から値を設定。

:code:`e_r`, :code:`e_theta`
  :code:`R2_p.base_vectors()` から値を設定。

:code:`dr`, :code:`dtheta`
  :code:`R2_p.base_oneforms()` から値を設定。

座標成分 :code:`x`, :code:`y`, :code:`r`, :code:`theta` は次の座標変換が（微妙な点もあるが）
成り立つように相互に :code:`connect_to` している。
数式中の逆三角正接関数は SymPy では関数 :code:`atan2` である。

.. math::

   \begin{align*}
   T_{rp}: (x, y) & \mapsto & (\sqrt{x^2 + y^2}, \tan^{-1} \frac{y}{x})\\
   T_{pr}: (r, \theta) & \mapsto & (r \cos \theta, r \sin \theta)
   \end{align*}

3 次元オブジェクト
----------------------------------------------------------------------
:code:`R3` 側でも同様の考えの下に、
各オブジェクトに座標成分、基底ベクトル、微分 1-形式のメンバーデータが付与されて、
関連する 3 座標系の間に相互に座標変換が定義されている。

以下、座標変換だけ記す。
直交座標系と円柱座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   T_{rc}: (x, y, z) & \mapsto & (\sqrt{x^2 + y^2}, \tan^{-1} \frac{y}{x}, z)\\
   T_{cr}: (\rho, \psi, z) & \mapsto & (\rho \cos \psi, \rho \sin \psi, z)
   \end{align*}

直交座標系と球座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   T_{rs}: (x, y, z) & \mapsto & (\sqrt{x^2 + y^2 + z^2}, \cos^{-1} \frac{z}{\sqrt{x^2 + y^2 + z^2}}, \tan^{-1} \frac{y}{x})\\
   T_{sr}: (r, \theta, \phi) & \mapsto & (r \sin \theta \cos \phi, r \sin \theta \sin \phi, r \cos \theta)
   \end{align*}

円柱座標系と球座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   T_{cs}: (\rho, \psi, z) & \mapsto & (\sqrt{\rho^2 + z^2}, \cos^{-1} \frac{z}{\sqrt{\rho^2 + z^2}}, \psi)\\
   T_{sc}: (r, \theta, \phi) & \mapsto & (r \sin \theta, \phi, r \cos \theta)
   \end{align*}

コード例（基本編）
======================================================================
コード例を書けるだけのクラスとオブジェクトの説明が終わったところで、
基本的な用例を示したい。

以下に示す例では、出来合いの :code:`R2_r` 等のオブジェクトを多用する。

局所座標系
----------------------------------------------------------------------
クラス CoordSystem, Point, BaseScalarField の
座標成分に関係するメソッドの簡単な例を示す。

.. code-block:: ipython

   In [1]: r, th = symbols('r th')

   In [2]: polar_coords = R2_p.point([r, th])

   In [3]: R2_r.x(polar_coords), R2_r.y(polar_coords)
   Out[3]: (r*cos(th), r*sin(th))

   In [4]: R2_r.point_to_coords(polar_coords)
   Out[4]:
   Matrix([
   [r*cos(th)],
   [r*sin(th)]])

   In [5]: R2_p.coord_tuple_transform_to(R2_r, [r, th])
   Out[5]:
   Matrix([
   [r*cos(th)],
   [r*sin(th)]])

* [1][2] 記号により 2 次元極座標系の座標 :code:`(r, th)` を定義する。
* [3] BaseScalarField オブジェクト
  :code:`R2_r.x` および :code:`R2r.y` による座標 :code:`point` の x 座標と y 座標成分の取得。
* [4] 同じことをメソッド :code:`CoordSystem.point_to_coords` で。
* [5] 同じことをメソッド :code:`CoordSystem.coord_tuple_transform_to` で。
  これがあるので [2] の前処理なしで済むことがある。

ドキュメントのそれとたいして変わらないが、Jacobi 行列の例を示す。

.. code-block:: ipython

   In [1]: x, y, r, th = symbols('x y r th')

   In [2]: R2_r.jacobian(R2_r, [x, y])
   Out[2]:
   Matrix([
   [1, 0],
   [0, 1]])

   In [3]: R2_r.jacobian(R2_p, [x, y])
   Out[3]:
   Matrix([
   [x/sqrt(x**2 + y**2), y/sqrt(x**2 + y**2)],
   [   -y/(x**2 + y**2),     x/(x**2 + y**2)]])

   In [4]: R2_p.jacobian(R2_r, [r, th])
   Out[4]:
   Matrix([
   [cos(th), -r*sin(th)],
   [sin(th),  r*cos(th)]])

* [2] 一応見ておくだけだが、
  自分自身の座標系で Jacobi 行列を求めると、恒等行列が得られる。
* [3] 2 次元直交座標から系極座標系への変換の Jacobi 行列。
* [4] 2 次元極座標系から直交座標系への変換の Jacobi 行列。

ベクトル場
----------------------------------------------------------------------
クラス BaseVectorField の例を示す。3 次元空間に何か適当な、
例えば原点からの距離の平方に反比例する値を返すスカラー場 :code:`f` を定義し、
各座標成分について適用させて、方向微分を見よう。

.. code-block:: ipython

   In [1]: k = symbols('k')

   In [2]: f = -k * R3_s.r ** -2

   In [3]: R3_s.e_r(f), R3_s.e_theta(f), R3_s.e_phi(f)
   Out[3]: (2*k/r**3, 0, 0)

   In [4]: R3_r.e_x(f), R3_r.e_y(f), R3_r.e_z(f)
   Out[4]: (2*k*x/(sqrt(x**2 + y**2 + z**2)*r**3), 2*k*y/(sqrt(x**2 + y**2 + z**2)*r**3), 2*k*z/(sqrt(x**2 + y**2 + z**2)*r**3))

   In [5]: R3_c.e_rho(f), R3_c.e_psi(f), R3_c.e_z(f)
   Out[5]: (2*k*rho/(sqrt(rho**2 + z**2)*r**3), 0, 2*k*z/(sqrt(rho**2 + z**2)*r**3))

* [2] 球座標系でスカラー場 :math:`f(r, \theta, \phi) = -\frac{k}{r^2}` を定義する。

* [3] まず球座標系 :code:`R3_s` の BaseVectorField オブジェクト
  :code:`e_r`, :code:`e_theta`, :code:`e_psi` の丸括弧演算を全成分で評価する。
  つまり単に勾配を手動で求めることになる。
  前述したとおり :math:`\frac{\partial f}{\partial r}` 等が得られている。

* [4][5] 直交座標系 :code:`R3_r` と 円柱座標系 :code:`R3_s` で同じことをする。
  例えば :code:`R3_r.e_x(f)` を見ると、
  例示したスカラー場がゼロ成分ばかりで検証しにくいが、
  これは一応次の式に合致した結果である。

  .. math::
     :nowrap:

     \begin{align*}
     \frac{\partial f}{\partial x} =
     \frac{\partial f}{\partial r}\frac{\partial r}{\partial x} +
     \frac{\partial f}{\partial \theta}\frac{\partial \theta}{\partial x} +
     \frac{\partial f}{\partial \phi}\frac{\partial \phi}{\partial x}
     \end{align*}

微分形式と外微分
----------------------------------------------------------------------
クラス Differential と WedgeProduct の基本動作を見たい。
例えば次の微分形式とその外微分をこれらのクラスを用いて再現したい。
上側の数式（出典はネットで拾ってきたどこかのベクトル解析の演習問題）のほうをオブジェクトとして表現して、
それをうまく処理して下側の数式に相当するオブジェクトを得たい。

.. math::
   :nowrap:

   \begin{align*}
   \omega &=& a x y z \,\dx + b x^2 z \,\dy -3 x^2 y \,\dz\\
   \dd{\omega} &=& (-bx^2 - 3x^2) \,\dy \wedge \dz + (axy + 6xy) \,\dz \wedge \dx + (2bxz - axz) \,\dx \wedge \dy.
   \end{align*}

しかし考えられる二通りの方法を試したところ、どうも所望の出力にならない。
まずは Differential だけでがんばる。

.. code-block:: ipython

   In [1]: a, b, c = symbols('a b c')

   In [2]: fx = a * R3_r.x * R3_r.y * R3_r.z

   In [3]: fy = b * R3_r.x ** 2 * R3_r.z

   In [4]: fz = -3 * R3_r.x**2 * R3_r.y

   In [5]: omega = fx * R3_r.dx + fy * R3_r.dy + fz * R3_r.dz; omega
   Out[5]: a*x*y*z*dx + b*x**2*z*dy - 3*x**2*y*dz

   In [6]: domega = Differential(omega); domega
   Out[6]: d(a*x*y*z*dx + b*x**2*z*dy - 3*x**2*y*dz)

   In [7]: domega(R3_r.e_x, R3_r.e_y, R3_r.e_z)
   Out[7]: a*x*y - a*x*z - b*x**2 + 2*b*x*z - 3*x**2 + 6*x*y

* [1]-[4] :math:`\RR^3` 上の 1-形式 :code:`omega` のセットアップ。
* [5] 内容の確認。ちなみに各単項式の次数が一致していることに気付いて欲しい。
* [6] 外微分オブジェクト :code:`domega` を生成する。
* [7] 丸括弧評価。ここが期待通りにならない。

期待通りにならない理由は :code:`Differential()` の計算ロジックが
Commutator に基づくため wedge 積が出現しないことによる。
そこで手動で WedgeProduct を適用することで :code:`omega` の外微分を求めることを考える。

.. code-block:: ipython

   In [8]: domega2 = sum(WedgeProduct(Differential(f), oneform)\
      ...: for (f, oneform) in zip((fx, fy, fz), R3_r.base_oneforms()))
   Out[8]: WedgeProduct(d(-3*x**2*y), dz) + WedgeProduct(d(b*x**2*z), dy) + WedgeProduct(d(a*x*y*z), dx)

   In [9]: domega2.rcall(R3_r.e_x, R3_r.e_y, R3_r.e_z)
   Out[9]: 2*a*x*y - 2*a*x*z - 2*b*x**2 + 4*b*x*z - 6*x**2 + 12*x*y

しかし期待は外れた。

* [8] :code:`omega` と同じものを表すハズの :code:`omega2` をセットアップ。
* [9] 今度は素の丸括弧は効かないので（式全体が単なる Add オブジェクトだから）、
  代わりに :code:`rcall` したものの、結果は悪化している。

  * またも wedge 積オブジェクトが見当たらない。
  * 出力が本来の倍？になっている。おそらく wedge 積の反対称性が加味されていないことによる。

余談だが、テストモジュール :code:`test_function_diffgeom_book` の
関数 :code:`test_functional_diffgeom_ch6` を参考にして、
:code:`omega` と :code:`omega2` が同じらしいことを確認するにはこうする。

.. code-block:: ipython

   In [10]: from itertools import permutations

   In [11]: all((domega - domega2).rcall(u, v) == 0 for u, v in permutations(R3_r.base_vectors(), 2))
   Out[11]: True

* [11] xyz のうちの順序を込めた任意ふたつの方向について
  :code:`domega` と :code:`domega2` が同じことがわかる。
  理論がわからないが、全方向で評価すると先程述べたように変な値が出てくる。

積分曲線
======================================================================
再びサブモジュール ``sympy.diffgeom.diffgeom`` に戻り、残りの機能を調べる。

ベクトル場の積分曲線を計算するための関数が定義されている。
級数版と微分方程式版のふたつの関数がある。
仕様を順に記してから、例を示す。

関数 :code:`intcurve_series(vector_field, param, start_point, n=6, coord_sys=None, coeffs=False)`
  ベクトル場の積分曲線を級数展開の形で返す。

  * 引数 :code:`vector_field` はベクトル場。
  * 引数 :code:`param` は積分曲線のパラメーター記号。
    差し当たり :code:`symbols('t')` などを渡せば十分。
  * 引数 :code:`start_point` は積分曲線の :code:`param=0` に対応する M 上の点。
    ここでは Point オブジェクトを渡す。
  * キーワード引数 `n` は級数展開の次数。
    デフォルトの ``6`` ならば :math:`O(n^6)` の項はカットされる。
  * キーワード引数 :code:`coord_sys` は級数展開を行う座標系を指定する。
    他の引数で示されるものとは異なる座標系を用いる場合にこれを用いる。
  * キーワード引数 :code:`coeffs` を True にすると、
    戻り値を級数展開の要素のリストとして返すようになる。

  * 戻り値はデフォルトでは Matrix オブジェクト。
    各行が積分曲線の座標成分に対応していて、
    内容は変数 :code:`param` に関する多項式である。

関数 :code:`intcurve_diffequ(vector_field, param, start_point, coord_sys=None)`
  ベクトル場の積分曲線を微分方程式の形で返す。
  各引数の意味は級数版と同じ。

  * 戻り値は 2 要素 tuple オブジェクトである。

    * [0]: 各座標成分で積分曲線の微分方程式オブジェクトからなる list オブジェクト。
    * [1]: それらに対応する、初期条件オブジェクトからなる list オブジェクト。

例を示す。

ベクトル場 :math:`\displaystyle X = -y \frac{\partial}{\partial x} + x \frac{\partial}{\partial y}` の
積分曲線 :math:`\gamma: (t_0, t_1) \longto M\ (M \subset \RR^2)` をそれぞれの関数を用いて求める。

.. code-block:: ipython

   In [1]: x0, y0, t = symbols('x0 y0 t', real=True)

   In [2]: X = -R2.y * R2.e_x + R2.x * R2.e_y

   In [3]: p0 = R2_r.point([x0, y0])

   In [4]: intcurve_series(X, t, p0)
   Out[4]:
   Matrix([
   [-t**5*y0/120 + t**4*x0/24 + t**3*y0/6 - t**2*x0/2 - t*y0 + x0],
   [ t**5*x0/120 + t**4*y0/24 - t**3*x0/6 - t**2*y0/2 + t*x0 + y0]])

   In [5]: eq, ini = intcurve_diffequ(X, t, p0)

   In [6]: eq
   Out[6]: [f_1(t) + Derivative(f_0(t), t), -f_0(t) + Derivative(f_1(t), t)]

   In [7]: ini
   Out[7]: [-x0 + f_0(0), -y0 + f_1(0)]

* [1]-[3] ベクトル場 :code:`X` と多様体上の点 :code:`p0` をセットする。
* [4] 関数 :code:`intcurve_series` を必要最低限の情報だけで呼び出す。
  戻り値には積分曲線 :math:`\gamma(t) = (\gamma_0(t), \gamma_1(t))` の級数展開が見える。
  パッと見は cos と sin の一次結合のようだ。
* [5] 関数 :code:`intcurve_diffequ` を呼び出す。戻り値は次を意味する。

  .. math::
     :nowrap:

     \begin{align*}
     \gamma_1(t) + \diff{}{t} \gamma_0(t) = 0\\
     - \gamma_0(t) + \diff{}{t} \gamma_1(t) = 0\\
     -x_0 + \gamma_0(0) = 0\\
     -y_0 + \gamma_1(0) = 0\\
     \end{align*}

  これを何らかの手段で解けば次の積分曲線が求まる。

  .. math::
     :nowrap:

     \begin{align*}
     \gamma(t) = (\gamma_0(t), \gamma_1(t)) = (x_0 \cos t - y_0 \sin t, y_0 \cos t + x_0 \sin t)
     \end{align*}

  SymPy の関数 :code:`dsolve` をそのまま用いてもよいが、
  この状況での初期値 :code:`ics` の指定方法が不明。

補助関数
======================================================================

基底ベクトルの変換
----------------------------------------------------------------------
座標の変換は各種メソッドで行えるが、ベクトル場のそれは次の関数を用いる。

関数 :code:`vectors_in_basis(expr, to_sys)`
  式 :code:`expr` に含まれる BaseVectorField オブジェクトを
  座標系 :code:`to_sys` での表現に変換する。

  * 引数 :code:`expr` は任意の SymPy 式。
  * 引数 :code:`to_sys` は座標変換先の CoordSystem オブジェクト。
  * 戻り値は SymPy 式。

  * 基底は変換されるが、変換後の基底の係数は変換前の CoordSystem の
    BaseScalarField で表現されている。

  ロジックの概要は次のとおり。

  #. 式 :code:`expr` に含まれるすべての BaseVectorField オブジェクトに対して、
     座標値の変換メソッドで見たのと同様に Jacobi 行列を評価する。

  #. 線形代数の要領でベクトルの基底変換を行う。

  #. 次にそれらをメソッド :code:`expr.subs` で一括置換する。

それほど面白い関数ではないので、サンプルコードの記載を省略する。

微分形式から行列を生成する
----------------------------------------------------------------------
この関数は後ほど記す関数群の実装のためにあるようだ。

関数 :code:`twoform_to_matrix(omega)`
  2-形式を表現する :code:`omega` から次の性質を持つ行列を生成する。

  .. math::
     :nowrap:

     \begin{align*}
     M_{ij} = \omega\left(\frac{\partial}{\partial x_j}, \frac{\partial}{\partial x_i}\right)
     \end{align*}

添字の順序については、実装を正とするならばドキュメントの記述が誤りだと思う。
例として、先ほどうまくいかなかった外微分 :math:`\dd{\omega}` がちょうど 2-形式なので、
ここで試そう。

.. code-block:: ipython

   In [1]: # See [1]-[6] in section Differential Form and Exterior Derivative

   In [2]: m = twoform_to_matrix(domega); m
   Out[2]:
   Matrix([
   [               0,  a*x*z - 2*b*x*z,   a*x*y + 6*x*y],
   [-a*x*z + 2*b*x*z,                0, b*x**2 + 3*x**2],
   [  -a*x*y - 6*x*y, -b*x**2 - 3*x**2,               0]])

   In [3]: all(m[i, j] == domega.rcall(R3_r.base_vector(j), R3_r.base_vector(i))\
      ...: for i in range(3) for j in range(3))
   Out[3]: True

* [2] 関数 :code:`twoform_to_matrix` を呼び出す。
  対角成分がゼロの 3 次交代行列が返るが、これは wedge 積の性質による。
* [3] この行列からは先ほどの :math:`\dd{\omega}` の各基底 2-form の係数が得られるようだ。
  こちらを用いればよかったのだ。

計量テンソル
======================================================================

Christoffel 記号
----------------------------------------------------------------------
第一種と第二種の Christoffel 記号を求める関数がそれぞれ存在する。
ただし、どちらも戻り値の型が記号の概念そのものではなく、
和をとる対象の数式を入れ子の tuple オブジェクトとして表現するようだ。
テンソルが関係するので入れ子が多用される。

関数 :code:`metric_to_Christoffel_1st(expr)`
  計量テンソル :code:`expr` から第一種 Christoffel 記号
  :math:`\Gamma_{c a b}` を求める。

  * 引数 :code:`expr` は、これから基本計量テンソルを得られる、
    何らかの TensorProduct オブジェクトの式でなければならない。
    この関数の実装に :code:`twoform_to_matrix` を利用しており、
    これが生成する行列が対称行列となるような :code:`expr` を与えなければならない。

  * 戻り値は第一種 Christoffel 記号の、いわばシグマ記号の中身。

関数 :code:`metric_to_Christoffel_2nd(expr)`
  計量テンソル :code:`expr` から第二種 Christoffel 記号
  :math:`\Gamma_{ij}^k` を求める。

  * 引数と戻り値の型の意味は上述の関数と同じ。
  * この関数の実装に :code:`twoform_to_matrix` と、
    当然ながら関数 :code:`metric_to_Christoffel_1st` を用いている。

  第二種の記号が曲面の第一基本形式の E, F, G と関係があるので、
  私はいつか利用するかもしれない。

Riemman-Christoffel 曲率テンソル
----------------------------------------------------------------------
関数 :code:`metric_to_Riemann_components(expr)`
  計量テンソル :code:`expr` から Riemman-Christoffel 曲率テンソルを求める。

  * 引数の意味は関連関数のそれに準じる。
  * 戻り値は、次の数式の右辺（縮約表現）を tuple の入れ子で表現したもの。

    .. math::
       :nowrap:

       \begin{align*}
       R^\rho{}_{\sigma \mu \nu} = 
       \Gamma_{\sigma \nu, \mu}^\rho
       - \Gamma_{\sigma \mu, \nu}^\rho
       + \Gamma_{\sigma \nu}^l \Gamma_{l \mu}^\rho
       - \Gamma_{\sigma \mu}^l \Gamma_{l \nu}^\rho
       \end{align*}

   * 実装では当然ながら関数 :code:`metric_to_Christoffel_2nd` を用いている。

Ricci 曲率テンソル
----------------------------------------------------------------------
関数 :code:`metric_to_Ricci_components(expr)`
  計量テンソル :code:`expr` から Ricci 曲率テンソルを求める。

  * 引数の意味は関連関数のそれに準じる。
  * 戻り値は、次の数式の右辺の Riemman-Christoffel 曲率テンソルを tuple の入れ子で表現したもの。

    .. math::
       :nowrap:

       \begin{align*}
       R_{ij} = R^k {}_{i k j}
       \end{align*}

  * 実装では当然ながら関数 :code:`metric_to_Riemann_components` を用いている。

.. include:: /_include/python-refs-core.txt
.. include:: /_include/python-refs-sci.txt

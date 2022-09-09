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

   .. code:: python3

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
ここで言う多様体とは、微分可能多様体を意味するものとして話をすすめる。

* オブジェクトをコンストラクターから直接生成する。
  名前と多様体次元さえ用意すればよい。
  生成後にそれぞれをメンバーデータ :code:`name` および :code:`dim` で参照できる。

  * あまり凝った名前は付けられない。
    例えば ``S^1`` のような文字列を指定すれば、コンストラクター呼び出し中に例外が送出する
    （あえてやるなら ``S**1`` とする）。

  * なお :code:`name` の型は文字列ではなく Symbol であるので注意。

* メンバーデータ :code:`patches` を介してこの多様体の座標近傍系を表現するオブジェクトにアクセスできる。
  このデータの型は後述する Patch オブジェクトの list である。

クラス Patch
----------------------------------------------------------------------
クラス Patch は多様体上の座標近傍となる開集合一つを表現する型だ。

例えば多様体 :math:`M` とその座標近傍系が :math:`\set{(U_\alpha, \varphi_\alpha)}_{\alpha \in I}` のように
与えられているとする。この座標近傍 :math:`U_\alpha` に相当する概念だと解釈できる。

* オブジェクトをコンストラクターから直接生成する。
  この際、この座標近傍自身の名前と、これが含まれる Manifold オブジェクトが必要だ。
  生成後にそれぞれをメンバーデータ :code:`name` および :code:`manifold` で参照できる。

* メンバーデータ :code:`coord_systems` から関連する局所座標系オブジェクトにアクセスできる。
  これは後述する CoordSystem オブジェクトの list オブジェクトである。

* 多様体次元はプロパティー :code:`dim` を用いて参照可能。
  この多様体のある座標近傍と微分同相な開集合を含むユークリッド空間の次元に他ならない。

クラス CoordSystem
----------------------------------------------------------------------
クラス CoordSystem は多様体の座標近傍ひとつの局所座標系を表現する型だ。

先ほどのモデルで言うと、一つの座標近傍 :math:`(U_\alpha, \varphi_\alpha)` の
局所座標系 :math:`\fn{\varphi_\alpha}{U_\alpha}\RR^n` に相当する概念だと解釈できる。

* オブジェクトをコンストラクターから直接生成する。
  局所座標系の名前と関連付ける座標近傍に対応する Patch オブジェクトが要る。

  * 他にもオプションで :code:`names` というのがある。
    これは局所座標成分の名称を list で指定することができる。

このクラスは特に重要なメソッドが多い。
強いて言えば、座標情報と座標変換に関係するものに分類したい。

座標情報にアクセスするメソッドは次のようなものがある。

:code:`coord_function(coord_index)`, :code:`coord_functions()`
  多様体上の点を取り、その点の局所座標を関数オブジェクトとして返す。
  後述のクラス BaseScalarField を参照。

  * 単数形の方は :code:`coord_index` 番目の座標成分のものに関するそれを返す。
    先ほどのモデルで言うと、座標近傍が :math:`(U_i, \varphi_i = (x_1, \dotsc, x_n))`
    で表されているとするならば、
    :math:`x_{\text{coord_index}}` を参照する。

  * 複数形の方は全成分を list で返す。

:code:`base_vector(coord_index)`, :code:`base_vectors()`
  接空間の基底を返す。
  微分幾何の教科書で言う :math:`\dfrac{\partial}{\partial x_1}, \dotsc, \dfrac{\partial}{\partial x_n}` に相当する。

  * 単数形の場合、オブジェクトの型は後述のクラス BaseVectorField だ。

:code:`base_oneform(coord_index)`, :code:`base_oneforms()`
  余接空間の基底を返す。
  微分幾何の教科書で言う :math:`\dd x_1, \dotsc, \dd x_n` に相当する。

  * 単数形の場合、オブジェクトの型は後述のクラス Differential

座標変換メソッドは次のようなものがある。

:code:`connect_to(to_sys, from_coords, to_exprs, inverse=True, fill_in_gaps=False)`
  この局所座標系から別の局所座標系 :code:`to_sys` への座標変換を指定する。
  数式で言うと :math:`(U_\alpha, \varphi_\alpha)` と :math:`(U_\beta, \varphi_\beta)`
  の二つの座標近傍について、例えば :math:`\varphi_\beta \circ \varphi_\alpha\inv` を表現するメソッドだと言える。

  * 利用例を知るならモジュール ``rn`` を見るのが最良。
    または後述する例題を参照して欲しい。
  * :code:`inverse=True` の指定により、逆写像まで自動的に計算してくれる。
  * 引数 :code:`to_exprs` で具体的な座標変換式を指定する。

  多様体論では、この座標変換が滑らかであることが死活的に重要なのだが、
  困ったことに使い勝手が妙に悪い。後述する例題を見て欲しい。

:code:`coord_tuple_transform_to(to_sys, coords)`
  この局所座標系における局所座標 :code:`coords` を
  別の局所座標系 :code:`to_sys` におけるそれに変換する。

  * 戻り値は Matrix オブジェクトとなる。
    座標を表現するために便宜上この型を用いている。

:code:`point_to_coords(point)`
  既存の（おそらくは別座標系にある）点オブジェクトから、
  この座標系での座標を得る。

  * 戻り値は Matrix オブジェクトとなる。

:code:`jacobian(to_sys, coords)`
  当座標系から座標系 :code:`to_sys` に関するヤコビアンを求める。
  先程から Matrix 型が頻出しているのは、このメソッドとの相性のためだろう。

利用例は後述する。

クラス Point
----------------------------------------------------------------------
多様体の一点を表現する型だ。

* オブジェクトの生成方法はふたつある。
  このクラスのコンストラクターから直接生成する方法と、
  クラス CoordSystem のメソッド :code:`point` を呼ぶ方法だ。

  * 直接生成の場合、局所座標系オブジェクトと座標を要する。
    前者はもちろん CoordSystem オブジェクトであり、
    後者は単に局所座標成分を list で渡せばよい。

  * メソッド :code:`CoordSystem.point` の場合は座標成分だけあればよい。
    対応する局所座標を指定する。

* メソッド :code:`coords` を用いれば、この点の局所座標系が得られる。

  * オプションとして別の局所座標系 :code:`to_sys` を与えると、
    座標変換後の座標を得ることも可能だ。
    これには前述のクラス CoordSystem のメソッド :code:`coord_tuple_transform_to` が用いられる。

多様体の場および微分演算各種
======================================================================
こちらも利用例は後述することにする。

クラス BaseScalarField
----------------------------------------------------------------------
多様体上で定義された関数 :math:`\fn{f}{M}\RR` を構成するための型だ。

* コンストラクターでオブジェクトを生成する場合、
  CoordSystem オブジェクトと座標成分番号 `i` を指定する。
  つまり多様体の局所座標系を一つ指定することになる。

  例えば 3 次元直交座標系の y 成分 (:code:`i = 1`) スカラー場を生成する、
  というような構成をする。

* 丸括弧で評価するときの引数は Point オブジェクトである。
  点オブジェクトは任意の座標系で表現されていて構わない。
  戻り値はスカラーだが、座標系の第 `i` 成分に相当する値を示す。

* BaseScalarField オブジェクトを（算術演算等で）組み合わせて、
  より一般的なスカラー場、つまり多様体上で定義された関数を構成することもできる。

クラス BaseVectorField
----------------------------------------------------------------------
このクラスが表現するのは多様体上のベクトル場の基底の一つだと思われる。
つまりベクトル場 :math:`\displaystyle \sum_{i=0}^n a_i \frac{\partial}{\partial x_i}` の
:math:`\dfrac{\partial}{\partial x_i}` の部分を表現している。

このクラスはベクトル場を表現するための素材に過ぎない。

* コンストラクターでオブジェクトを生成する方法は BaseScalarField と同じだ。

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
ふたつのベクトル場の交換子、括弧積を表現する。

* :code:`Commutator(X, Y)` は
  :math:`[X, Y]f \coloneqq X(Yf) - Y(Xf)` で定義されるベクトル場を意味する。
  ここで :code:`f` は多様体上で定義される関数を意味する。

  * 丸括弧で :code:`f` を評価する前に、交換子オブジェクトがゼロでないことを確認する必要がある。

* ドキュメントにあるように、現行の実装は少々弱いようだ。
  展開し切れないケースがままある。

:math:`[X, Y] = -[Y, X]` や :math:`[X, Y] = XY - YX` を実感してみよう。
次の例では、適当な次元の多様体とその上の適当なベクトル場二つを定義し、
この数式の左辺と右辺それぞれに対応する SymPy オブジェクトを生成して、
さらに多様体上で定義された適当な関数を評価することによって、
間接的に両辺を比較する：

.. code:: ipython

   In [1]: M = Manifold('R^5', 5)

   In [2]: U = CoordSystem('x', Patch('U', M))

   In [3]: x_0, x_1, x_2, x_3, x_4 = U.coord_functions()
      ...: X_0, X_1, X_2, X_3, X_4 = U.base_vectors()
      ...: dx0, dx_1, dx_2, dx_3, dx_4 = U.base_oneforms()
      ...:

   In [4]: X = x2**2 * X0 + exp(x3) * X1 - X4

   In [5]: Y = (x1 ** 3 + x0 ** 2) * X3

   In [6]: Commutator(X, Y) + Commutator(Y, X)
   Out[6]: 0

   In [7]: f = x0 ** 2 + x1 ** 2 + x2 ** 4 + x3 ** 4

   In [8]: Commutator(X, Y).rcall(f) - (X.rcall(Y.rcall(f)) - Y.rcall(X.rcall(f)))
   Out[8]: 0

クラス Differential
----------------------------------------------------------------------
クラス Differential は外微分を意味する。
スカラー関数を含む微分形式の外微分をオブジェクトとして表現する。

* コンストラクターには k-形式として扱えるオブジェクトを渡す。
  ここで k はゼロ以上。

  * 既存の Differential オブジェクトでもかまわないが、結果的にゼロが返る。
    :math:`\dd \circ \dd = 0` による。

  * 先述したメソッド :code:`CoordSystem.base_oneforms` が返すのは
    0-形式 :code:`f_i = BaseScalarField(coord, i)` の外微分となる
    1-形式 :code:`Differential(f_i)` をすべての `i` 成分について生成したものに他ならない。

  * 多様体上の関数 :code:`f` からは全微分 :code:`df` が得られる。
  * 任意のベクトル場 :code:`X` について :code:`df(X) == X(f)` が成り立つ。

* 丸括弧で評価する際のオペランドはスカラー関数オブジェクトまたはベクトル場でよい。
  今度は BaseVectorField オブジェクトの線形結合で通じるし、
  オブジェクトを次元個分カンマ区切りで可変個引数的に渡してもよい。
  同じ結果が得られると期待してよろしい。

* 実装に Commutator を用いる。

クラス TensorProduct
----------------------------------------------------------------------
クラス TensorProduct は多様体の座標近傍における（ふつうは一次の）微分形式とベクトル場からなる
テンソルを表現することができる。

次の例ではある 5 次元多様体で簡単な (2, 3) テンソルを定義する：

.. code:: ipython

   In [1]: M = Manifold('R^5', 5)

   In [2]: U = CoordSystem('x', Patch('U', M))

   In [3]: x_0, x_1, x_2, x_3, x_4 = U.coord_functions()
      ...: X_0, X_1, X_2, X_3, X_4 = U.base_vectors()
      ...: dx_0, dx_1, dx_2, dx_3, dx_4 = U.base_oneforms()
      ...:

   In [4]: T = TensorProduct(X_1, X_4, dx_0, dx_2, dx_3)

   In [5]: assert covariant_order(T) == 3

   In [6]: assert contravariant_order(T) == 2

TensorProduct 型オブジェクトに対して丸括弧演算子を呼び出すことで、
テンソルの多重線形写像としての評価を行うことができる。引数として

* 微分形式に対応する引数にはベクトル場を、
* ベクトル場に対応する引数には局所座標からなるスカラー場を

それぞれ指定する必要がある。
テンソルの各成分ごとの演算結果の積を計算するものと考えるのがわかりやすい：

.. code:: ipython

   In [7]: from sympy import var

   In [8]: var('k0:5')
   Out[8]: (k0, k1, k2, k3, k4)

   In [9]: T(k0*x_1, k1*x_4, k2*X_0, k3*X_2, k4*X_3)
   Out[9]: k0*k1*k2*k3*k4

   In [10]: T(x1 ** -2, x4, X0, X0 + X1 + X2 + X3 + X4, X3)
   Out[10]: -2/x_1**3

空の TensorProduct オブジェクトは 1 と評価される。

.. code:: ipython

   In [11]: TensorProduct()
   Out[11]: 1

TensorProduct オブジェクトの :code:`rcall` 呼び出しで計量縮約を行なうことができる。
次の例は 3 次元ユークリッド空間にテキトーな計量 :math:`g` を定義して、
接空間の各基底（当然テンソルの一種とみなせる）と ``None`` を引数として呼び出すものだ：

.. code:: ipython

   In [12]: TP = TensorProduct

   In [13]: g = k0*TP(R3_r.dx, R3_r.dx) + k1*TP(R3_r.dy, R3_r.dy) + k2*TP(R3_r.dz, R3_r.dz)

   In [14]: g.rcall(R3_r.e_x, None)
   Out[14]: k0*dx

   In [15]: g.rcall(R3_r.e_y, None)
   Out[15]: k1*dy

   In [16]: g.rcall(R3_r.e_z, None)
   Out[16]: k2*dz

クラス WedgeProduct
----------------------------------------------------------------------
クラス WedgeProduct は微分形式オブジェクト同士の外積を表現する。

* スーパークラスは TensorProduct だが、混ぜて使わないこと。
  前項で注意した点がそのまま当クラスの注意点でもある。

* 積分の文脈上に限り、反対称性がまともに扱われるとのこと。
  この注意は、例えば

  * :code:`WedgeProduct(X, X)` のようなオブジェクトを生成しても、
    直ちにゼロと評価されたりしない

  * :code:`WedgeProduct(X, Y)` と :code:`-WedgeProduct(Y, X)` が等しくならない

  という現象を説明するものだろうか。

クラス LieDerivative
----------------------------------------------------------------------
クラス LieDerivative はリー微分を表現する。
あるベクトル場が生成するフローに沿う何かの微分を計算するのに利用できるはずだ。

次の設定で簡単なテンソル場のリー微分を試すことにする：

.. code:: ipython

   In [1]: U = CoordSystem('x', Patch('U', Manifold('R^5', 5)))

   In [2]: x_0, x_1, x_2, x_3, x_4 = U.coord_functions()
      ...: X_0, X_1, X_2, X_3, X_4 = U.base_vectors()
      ...: dx_0, dx_1, dx_2, dx_3, dx_4 = U.base_oneforms()
      ...:

   In [3]: X = sum(ci * Xi for ci, Xi in zip(var('c0:5'), U.base_vectors()))

   In [4]: L, C = LieDerivative, Commutator

最初に :math:`\mathcal L_xf = X(f)` と :math:`\mathcal L_XY = [X, Y]` を試してみよう：

.. code:: ipython

   In [5]: f = x0 ** 2 + x1 ** 2

   In [6]: assert L(X, f) == X.rcall(f)

   In [7]: Y = 8 * x_3 * X_0 + 9 * x_1 * X_2 + 3 * x_0 * X_4

   In [8]: assert L(X, Y) == C(X, Y)

次にライプニッツ則スカラー場バージョンを試す：

.. code:: ipython

   In [9]: g = x_3 ** 2 + x_4 ** 2

   In [10]: assert L(X, f * g).expand() == (f * L(X, g) + L(X, f) * g).expand()

SymPy の FAQ にあるように、こういう複雑な等式のテストには
メソッド :code:`expand()` を適用したり、左辺マイナス右辺をゼロと比較したりする必要があることが多い。

.. todo::

   :math:`f, g \in C^\infty(M)`, :math:`X, Y \in \mathfrak X(M)`,
   :math:`\omega \in \varOmega^1(M)`,
   :math:`\xi \in \varGamma(T(a, b)),\ \eta \in \varGamma(T(a', b'))` に対して、
   例えば次に挙げるリー微分の性質が成り立っているかどうかを試したい：

   .. math::

      \begin{align*}
      &(\mathcal L_X \omega)(Y) = X(\omega(Y)) - \omega([X, Y])\\
      &(\mathcal L_X \omega)(fY) = f(\mathcal L_X\omega)(Y)\\
      &\mathcal L_X(fY) = f \mathcal L_X(Y) + (\mathcal L_Xf) Y\\
      &\mathcal L_X(f\omega) = f \mathcal L_X(\omega) + (\mathcal L_Xf) \omega\\
      &\mathcal L_{[X, Y]} = \mathcal L_X \circ \mathcal L_Y - \mathcal L_Y \circ \mathcal L_X\\
      &\mathcal L_X(\xi \otimes \eta) = \mathcal L_X\xi \otimes \eta + \xi \otimes \mathcal L_X\eta
      \end{align*}

   今のところ与えるテンソルが平凡過ぎて処理中にスカラーになるのがまずいのか、
   ``TypeError: 'Add' object is not callable`` というエラーが頻出する。

定義済み多様体オブジェクト
======================================================================
本節ではサブモジュール ``sympy.diffgeom.rn`` に定義されているオブジェクトを見ていく。

前節で述べた一連の機能をすぐに試したいが、後で見るように比較的簡単な多様体を構成することすら面倒で困る。
そこで、ここにある定義済みオブジェクトをインポートすることが考えられる。
それらのオブジェクトを試して、感触を確かめるのがよいだろう。

.. csv-table::
   :delim: @
   :header: オブジェクト, クラス, 名前, 意味
   :widths: 8, 10, 10, 16

   :code:`R2`@Manifold@``'R^2'``@ユークリッド空間 :math:`\RR^2` を多様体としてみたもの
   :code:`R2_origin`@Patch@``'origin'``@:code:`R2` の局所（というか大域）座標近傍
   :code:`R2_r`@CoordSystem@``'rectangular'``@:code:`R2_origin` の局所座標を直交座標系で表現したもの
   :code:`R2_p`@CoordSystem@``'polar'``@:code:`R2_origin` の極座標系
   :code:`R3`@Manifold@``'R^3'``@ユークリッド空間 :math:`\RR^3` を多様体としてみたもの
   :code:`R3_origin`@Patch@``'origin'``@:code:`R3` の局所（というか大域）座標近傍
   :code:`R3_r`@CoordSystem@``'rectangular'``@:code:`R3_origin` の局所座標を直交座標系で表現したもの
   :code:`R3_c`@CoordSystem@``'cylindrical'``@:code:`R3_origin` の局所座標を円柱座標系で表現したもの
   :code:`R3_s`@CoordSystem@``'spherical'``@:code:`R3_origin` の局所座標を球座標系で表現したもの

どちらの次元の多様体にも開集合としての座標近傍は一つしか定義されていないが、
それに対して複数の局所座標系が与えられていて、それらの間の座標変換も定義済みだ。

2 次元オブジェクト
----------------------------------------------------------------------
:code:`R2`, :code:`R2_origin`, :code:`R2_r`, :code:`R2_p` には
可能な限り次に示すメンバーデータが付与されている。
可能な限りというのは「局所座標系 A 由来のデータは局所座標系 B には付与しない」という意味だ。

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
   \varphi_{pr}: (x, y) & \longmapsto (\sqrt{x^2 + y^2}, \tan\inv \frac{y}{x})\\
   \varphi_{rp}: (r, \theta) & \longmapsto (r \cos \theta, r \sin \theta)
   \end{align*}

ただし :math:`\varphi_{rp} = \varphi_r \circ \varphi_p\inv` 等と記した。
以下同様。

3 次元オブジェクト
----------------------------------------------------------------------
:code:`R3` 側でも同様の考えの下に、
各オブジェクトに局所座標成分、接ベクトル基底、1-形式基底のメンバーデータが付与されて、
関連する 3 座標系の間に相互に座標変換が定義されている。

以下、座標変換だけ記す。
直交座標系と円柱座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   \varphi_{cr}: (x, y, z) & \longmapsto (\sqrt{x^2 + y^2}, \tan\inv \frac{y}{x}, z)\\
   \varphi_{rc}: (\rho, \psi, z) & \longmapsto (\rho \cos \psi, \rho \sin \psi, z)
   \end{align*}

直交座標系と球座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   \varphi_{sr}: (x, y, z) & \longmapsto (\sqrt{x^2 + y^2 + z^2}, \cos\inv \frac{z}{\sqrt{x^2 + y^2 + z^2}}, \tan\inv \frac{y}{x})\\
   \varphi_{rs}: (r, \theta, \varphi) & \longmapsto (r \sin \theta \cos \varphi, r \sin \theta \sin \varphi, r \cos \theta)
   \end{align*}

円柱座標系と球座標系間の座標変換は次のように与えられている。

.. math::

   \begin{align*}
   \varphi_{sc}: (\rho, \psi, z) & \longmapsto (\sqrt{\rho^2 + z^2}, \cos\inv \frac{z}{\sqrt{\rho^2 + z^2}}, \psi)\\
   \varphi_{cs}: (r, \theta, \varphi) & \longmapsto (r \sin \theta, \varphi, r \cos \theta)
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

.. code:: ipython

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
  :code:`R2_r.x` および :code:`R2r.y` による局所座標系表示 :code:`point` の x 座標と y 座標成分の取得。
* [4] 同じことをメソッド :code:`CoordSystem.point_to_coords` で。
* [5] 同じことをメソッド :code:`CoordSystem.coord_tuple_transform_to` で。
  これがあるので [2] の前処理なしで済むことがある。

ドキュメントのそれとたいして変わらないが、ヤコビアンの例を示す。

.. code:: ipython

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
  自分自身の座標系でヤコビアンを求めると、恒等行列が得られる。
* [3] 2 次元直交座標系から極座標系への変換のヤコビアン。
* [4] 2 次元極座標系から直交座標系への変換のヤコビアン。

単位円 :math:`S^1`
----------------------------------------------------------------------
ユークリッド空間 :math:`\RR^2` の部分集合 :math:`S^1 = \set{\bm x \in \RR^2 \sth \norm{\bm x} = 1}` を
1 次元多様体として表現してみよう（わかりやすさを優先して、変数を冗長に使い分けている）：

.. literalinclude:: /_sample/sympy/s1.py
   :language: python3

* 序盤の CoordSystem および Patch オブジェクトのペア 4 個は単位円と

  * :code:`phip0`: 半平面 :math:`x_0 > 0` との共通部分、
  * :code:`phim0`: 半平面 :math:`x_0 < 0` との共通部分、
  * :code:`phip1`: 半平面 :math:`x_1 > 0` との共通部分、
  * :code:`phim1`: 半平面 :math:`x_1 < 0` との共通部分を

  それぞれ表現するためのものだ。

* 次に各座標変換 :math:`\varphi_j^\pm \circ \varphi_i^\pm{}\inv` を指定する。
  ここでは :code:`inverse=False` として逆写像を自動で計算させる機能を無効化する。

  * こうしないとなぜか :code:`-sqrt(1 - x0**2)` の逆写像の評価に失敗するのでそうしているに過ぎない。
    可能な限り SymPy に逆写像を求めさせるのが楽に決まっている。

* 次にオーバーラップする座標近傍における座標変換のヤコビアンを出力する。
  多様体次元が 1 であるため、一次正方行列として評価される。

  * 余裕があればヤコビアンから多様体の臨界点を求める処理を考えてみよう。

* 最後に適当な座標近傍上の点について座標変換を見る。
  :math:`\pm\dfrac{1}{2}` は :math:`\pm\dfrac{\sqrt{3}}{2}` または
  :math:`\mp\dfrac{\sqrt{3}}{2}` に変換されるはずだ。

実行結果は次のようになる：

.. code:: text

   Jacobian phip0 -> phip1: Matrix([[-x1/sqrt(-x1**2 + 1)]])
   Jacobian phip1 -> phip0: Matrix([[-x0/sqrt(-x0**2 + 1)]])
   Jacobian phip0 -> phim1: Matrix([[-x1/sqrt(-x1**2 + 1)]])
   Jacobian phim1 -> phip0: Matrix([[x0/sqrt(-x0**2 + 1)]])
   Jacobian phim0 -> phip1: Matrix([[x1/sqrt(-x1**2 + 1)]])
   Jacobian phip1 -> phim0: Matrix([[-x0/sqrt(-x0**2 + 1)]])
   Jacobian phim0 -> phim1: Matrix([[x1/sqrt(-x1**2 + 1)]])
   Jacobian phim1 -> phim0: Matrix([[x0/sqrt(-x0**2 + 1)]])
   phip0( 0.5000) = phip1( 0.8660)
   phip0(-0.5000) = phim1( 0.8660)
   phim0( 0.5000) = phip1(-0.8660)
   phim0(-0.5000) = phim1(-0.8660)
   phip1( 0.5000) = phip0( 0.8660)
   phip1(-0.5000) = phim0( 0.8660)
   phim1( 0.5000) = phip0(-0.8660)
   phim1(-0.5000) = phim0(-0.8660)

ベクトル場
----------------------------------------------------------------------
クラス BaseVectorField の例を示す。3 次元空間に何か適当な、
例えば原点からの距離の平方に反比例する値を返すスカラー場

.. math::

   \fnm{f}{\RR^2}{\RR}{(r, \theta, \varphi)}-\frac{k}{r^2}.

を :code:`f` として定義し、各座標成分について適用させて方向微分を見よう。

.. code:: ipython

   In [1]: k = symbols('k')

   In [2]: f = -k * R3_s.r ** -2

   In [3]: R3_s.e_r(f), R3_s.e_theta(f), R3_s.e_phi(f)
   Out[3]: (2*k/r**3, 0, 0)

   In [4]: R3_r.e_x(f), R3_r.e_y(f), R3_r.e_z(f)
   Out[4]: (2*k*x/(sqrt(x**2 + y**2 + z**2)*r**3), 2*k*y/(sqrt(x**2 + y**2 + z**2)*r**3), 2*k*z/(sqrt(x**2 + y**2 + z**2)*r**3))

   In [5]: R3_c.e_rho(f), R3_c.e_psi(f), R3_c.e_z(f)
   Out[5]: (2*k*rho/(sqrt(rho**2 + z**2)*r**3), 0, 2*k*z/(sqrt(rho**2 + z**2)*r**3))

* [2] 球座標系でスカラー場 :math:`f(r, \theta, \varphi) = -\dfrac{k}{r^2}` を定義する。

* [3] まず球座標系 :code:`R3_s` の BaseVectorField オブジェクト
  :code:`e_r`, :code:`e_theta`, :code:`e_psi` の丸括弧演算を全成分で評価する。
  つまり単に勾配ベクトルを手動で求めることになる。
  前述したとおり :math:`\dfrac{\partial f}{\partial r}` 等が得られている。

* [4][5] 直交座標系 :code:`R3_r` と 円柱座標系 :code:`R3_s` で同じことをする。
  例えば :code:`R3_r.e_x(f)` を見ると、
  例示したスカラー場がゼロ成分ばかりで検証しにくいが、
  これは一応次の式に合致した結果である。

  .. math::

     \begin{align*}
     \frac{\partial f}{\partial x} =
     \frac{\partial f}{\partial r}\frac{\partial r}{\partial x} +
     \frac{\partial f}{\partial \theta}\frac{\partial \theta}{\partial x} +
     \frac{\partial f}{\partial \varphi}\frac{\partial \varphi}{\partial x}
     \end{align*}

微分形式と外微分
----------------------------------------------------------------------
クラス Differential と WedgeProduct の基本動作を見たい。
例えば次の微分形式 :math:`\omega` とその外微分 :math:`\dd \omega` をこれらのクラスを用いて再現したい。
上側の数式（出典はネットで拾ってきたどこかのベクトル解析の演習問題）のほうをオブジェクトとして表現して、
それをうまく処理して下側の数式に相当するオブジェクトを得たい。

.. math::

   \begin{align*}
   \omega &= axyz \,\dx + bx^2z\,\dd y -3x^2y\,\dd z\\
   \dd{\omega} &= (-bx^2 - 3x^2)\,\dd y \wedge \dd z + (axy + 6xy)\,\dd z \wedge \dd x + (2bxz - axz)\,\dd x \wedge \dd y.
   \end{align*}

まずは Differential だけでがんばる：

.. code:: ipython

   In [1]: a, b, c = symbols('a b c')

   In [2]: fx = a * R3_r.x * R3_r.y * R3_r.z

   In [3]: fy = b * R3_r.x ** 2 * R3_r.z

   In [4]: fz = -3 * R3_r.x**2 * R3_r.y

   In [5]: omega = fx * R3_r.dx + fy * R3_r.dy + fz * R3_r.dz; omega
   Out[5]: a*x*y*z*dx + b*x**2*z*dy - 3*x**2*y*dz

   In [6]: domega = Differential(omega); domega
   Out[6]: d(a*x*y*z*dx + b*x**2*z*dy - 3*x**2*y*dz)

   In [7]: domega(ey, ez), domega(ez, ex), domega(ex, ey)
   Out[7]: (-b*x**2 - 3*x**2, a*x*y + 6*x*y, -a*x*z + 2*b*x*z)

* [1]-[4] :math:`\RR^3` 上の 1-形式 :code:`omega` のセットアップ。
* [5] 内容の確認。ちなみに各単項式の次数が一致していることに気付いて欲しい。
* [6] 外微分オブジェクト :code:`domega` を生成する。
* [7] 丸括弧評価。ここでは
  :math:`\dd y \wedge \dd z` 等の :math:`\extp^2(\RR^3)` の基底ごとに係数を得ている。

  * 先ほどの数式の :math:`\dd \omega` 全体を一度に得られる方法はないのか？

  * なぜ :math:`\omega\left(\dfrac{\partial}{\partial y}, \dfrac{\partial}{\partial z}\right)` で
    それが得られるのか、考えてみよう。

次に手動で WedgeProduct を適用することで :math:`\dd \omega` を求めるやり方をとる。

.. code:: ipython

   In [8]: domega2 = sum(WedgeProduct(Differential(f), oneform)\
      ...: for (f, oneform) in zip((fx, fy, fz), R3_r.base_oneforms()))
   Out[8]: WedgeProduct(d(-3*x**2*y), dz) + WedgeProduct(d(b*x**2*z), dy) + WedgeProduct(d(a*x*y*z), dx)

   In [9]: domega2.rcall(ey, ez), domega2.rcall(ez, ex), domega2.rcall(ex, ey)
   Out[9]: (-b*x**2 - 3*x**2, a*x*y + 6*x*y, -a*x*z + 2*b*x*z)

* [8] :code:`omega` と同じものを表すハズの :code:`omega2` をセットアップ。
  外積代数における次の関係式を意識している：

  .. math::

     \dd \left(\sum_{i = 1}^n f_i\,\dd x_i\right) = \sum_{i = 1}^n \dd f_i\,\wedge \dd x_i

* [9] 今度は素の丸括弧は効かないので（式全体が単なる Add オブジェクトだから）、
  代わりに :code:`rcall` を適用する。

余談だが、テストモジュール :code:`test_function_diffgeom_book` の
関数 :code:`test_functional_diffgeom_ch6` を参考にして、
:code:`omega` と :code:`omega2` が同じらしいことを確認するにはこうする。

.. code:: ipython

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
ベクトル場を :math:`X` とし、局所的に対応する積分曲線を :math:`\gamma(t)` とする
常微分方程式 :math:`\displaystyle \diff{\gamma(t)}{t} = X(\gamma(t))` の一般解を求めるための関数だ。
級数版と微分方程式版のふたつがある。
仕様を順に記してから、例を示す。

関数 :code:`intcurve_series(vector_field, param, start_point, n=6, coord_sys=None, coeffs=False)`
  ベクトル場が満たす積分曲線を級数展開の形で返す。

  * 引数 :code:`vector_field` は（何らかのフローを生成するような）ベクトル場。
  * 引数 :code:`param` は積分曲線のパラメーター記号。
    差し当たり :code:`symbols('t')` などを渡せば十分。
  * 引数 :code:`start_point` は積分曲線の :code:`param=0` に対応する多様体上の点。
    ここでは Point オブジェクトを渡す。
  * キーワード引数 `n` は級数展開の次数。
    デフォルトの ``6`` ならば :math:`O(n^6)` の部分はカットされる。
  * キーワード引数 :code:`coord_sys` は級数展開を行う局所座標系を指定する。
    他の引数で示されるものとは異なる座標系を用いる場合にこれを用いる。
  * キーワード引数 :code:`coeffs` を True にすると、
    戻り値を級数展開の要素のリストとして返すようになる。

  * 戻り値はデフォルトでは Matrix オブジェクト。
    各行が積分曲線の座標成分に対応していて、
    内容は変数 :code:`param` に関する多項式である。

関数 :code:`intcurve_diffequ(vector_field, param, start_point, coord_sys=None)`
  ベクトル場が満たす積分曲線を常微分方程式の形で返す。
  各引数の意味は級数版と同じ。

  * 戻り値は 2 要素 tuple オブジェクトである。

    * [0]: 各座標成分で積分曲線の微分方程式オブジェクトからなる list オブジェクト。
    * [1]: それらに対応する、初期条件オブジェクトからなる list オブジェクト。

例を示す。
ユークリッド空間 :math:`\RR^2` 上の各点で定義される次のベクトル場 :math:`X` が
生成するフロー :math:`\fn{\gamma}{\RR^2}\RR^2` で、点 :math:`(x_0, y_0)` を通るようなものを、
上述のそれぞれの関数を用いて求める。

.. math::

   X = -y \frac{\partial}{\partial x} + x \frac{\partial}{\partial y}.

.. code:: ipython

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
  パッと見は :math:`\cos` と :math:`\sin` の一次結合のようだ。
* [5] 関数 :code:`intcurve_diffequ` を呼び出す。戻り値は次を意味する：

  .. math::

     \begin{align*}
     \gamma_1(t) + \diff{\gamma_0(t)}{t}  = 0\\
     - \gamma_0(t) + \diff{\gamma_1(t)}{t} = 0\\
     -x_0 + \gamma_0(0) = 0\\
     -y_0 + \gamma_1(0) = 0\\
     \end{align*}

  この常微分方程式の解曲線が積分曲線であり、具体的には次のものである：

  .. math::

     \gamma(t) = (\gamma_0(t), \gamma_1(t)) = (x_0 \cos t - y_0 \sin t, x_0 \sin t + y_0 \cos t).

  :math:`\displaystyle X(0) = \left.\diff{\gamma(t)}{t}\right|_{t = 0} = (x_0, y_0)` が成り立つ。

  .. todo::

     上の常微分方程式は簡単なので SymPy に頼らずに解を求めて書いたが、
     もちろん SymPy で解きたい。

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
     座標値の変換メソッドで見たのと同様にヤコビアンを評価する。

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
例として、先ほどの外微分 :math:`\dd{\omega}` がちょうど 2-形式なので、
ここで試そう。

.. code:: ipython

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
  :math:`\varGamma_{c a b}` を求める。

  * 引数 :code:`expr` は、これから基本計量テンソルを得られる、
    何らかの TensorProduct オブジェクトの式でなければならない。
    この関数の実装に :code:`twoform_to_matrix` を利用しており、
    これが生成する行列が対称行列となるような :code:`expr` を与えなければならない。

  * 戻り値は第一種 Christoffel 記号の、いわばシグマ記号の中身。

関数 :code:`metric_to_Christoffel_2nd(expr)`
  計量テンソル :code:`expr` から第二種 Christoffel 記号
  :math:`\varGamma_{ij}^k` を求める。

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
       \varGamma_{\sigma \nu, \mu}^\rho
       - \varGamma_{\sigma \mu, \nu}^\rho
       + \varGamma_{\sigma \nu}^l \varGamma_{l \mu}^\rho
       - \varGamma_{\sigma \mu}^l \varGamma_{l \nu}^\rho
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

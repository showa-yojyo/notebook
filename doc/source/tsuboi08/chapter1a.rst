======================================================================
第 1 章 ユークリッド空間上の微分形式 1/2
======================================================================

.. contents:: ノート目次

1.1 微積分学の基本定理（基礎）
======================================================================

* 定義 1.1.1: 原始関数

  * 区間上の連続関数 :math:`f(t)` に対して関数 :math:`F(t)` の導関数が
    :math:`f(t)` であるとき、:math:`F` は :math:`f` の原始関数であるという。この
    用語は高校数学で聞いているはず。
  * 相異なる原始関数が常に存在するが、その違いは定数分でしかない。

    * `平均値の定理 <http://mathworld.wolfram.com/Mean-ValueTheorem.html>`__ に
      よる。
    * あとで微分形式の積分を考えるときにこの性質の類比をも考える。

.. _tsuboi08.1.1.2:

* 定理 1.1.2: 定積分の存在

  * 閉区間上の連続関数には定積分が定まる。ここでは「閉」区間と限定していることに
    注意。

.. _tsuboi08.1.1.3:

* 定理 1.1.3: `微積分学の基本定理
  <http://mathworld.wolfram.com/FundamentalTheoremsofCalculus.html>`__

(pp. 2-3) の「余談」がとてもいい。面積を求めることと接線を求めることの関係が
1.1.3 として述べられた。

1.2 微積分学の基本定理の多変数化（基礎）
======================================================================

.. _tsuboi08.1.2.1:

* 定義 1.2.1: 微分 1 形式、`線積分
  <http://mathworld.wolfram.com/LineIntegral.html>`__

  まず次のような状況において「関数の値の差」を考察する：

  * :math:`{U \subset \RR^n}` を弧状連結開集合とする。
  * 関数 :math:`\fn{f}{U}{\RR}` および写像 :math:`\fn{\gamma}{[a, b]}U` を微分可
    能とする。さらに次の対応があるとする：

    * :math:`{\gamma(a) = \bm y, \gamma(b) = \bm z,}`
    * :math:`{\bm y, \bm z \in U.}`

  差を次のように表現する：

  .. math::

     \begin{align*}
     f(\bm z) - f(\bm y) &= f \circ \gamma(b) - f \circ \gamma(a)\\
     &= \int_a^b\! \diff{(f \circ \gamma(t))}{t}\,\dd{t}\\
     &= \int_a^b\! \sum_{i = 1}^n \frac{\partial f}{\partial x_i}(\gamma(t))\diff{\gamma_i}{t}(t)\,\dd{t}\\
     &= \int_\gamma\sum_{i = 1}^n \frac{\partial f}{\partial x_i}\dd{x}_i.
     \end{align*}

  * :math:`{\displaystyle \sum_{i = 1}^n f_i \dd{x}_i}` を :math:`U` 上の微分 1
    形式 or 1 次微分形式 or 1 形式という。
  * :math:`{\displaystyle \int_\gamma\sum_{i = 1}^n f_i\dd{x}_i}` を上述の式のよ
    うに定義し、これを線積分という。
  * 各 :math:`\dd{x_i}` を 何らかの :math:`n` 次元線形空間の :math:`x_i` 方向の
    基底のようなものという解釈を今のところはとることにする。

.. _tsuboi08.1.2.2:

* 定義 1.2.2: 全微分

  先ほどの式の最後の線積分の被積分部を :math:`f` の全微分と言う：

  .. math::

     \dd{f} = \sum_{i = 0}^n \frac{\partial f}{\partial x_i}\dd{x}_i.

.. _tsuboi08.1.2.3:

* 定理 1.2.3: :ref:`定理 1.1.3<tsuboi08.1.1.3>` の一般化

  1 形式についての線積分は先ほどの式と整合する：

  .. math::

     \int_\gamma df = f \circ \gamma(b) - f \circ \gamma(a).

* 積分可能条件とは :math:`{\dfrac{\partial f_i}{\partial x_j} = \dfrac{\partial
  f_j}{\partial x_i}}` がすべての :math:`{1 \le i, j \le n}` について成り立つこ
  とを言う。
* 積分可能条件を満たす :math:`f` について、次の等式が成り立つような :math:`U` 上
  の関数 :math:`F` は存在するだろうかということを以下考察する：

  .. math::

     \dd{F} = \sum_{i = 1}^n f_i \dd{x_i}.

.. _tsuboi08.1.2.4:

* 例 1.2.4: 二次元のある例

  .. math::

     F(x_1, x_2) = \int_0^{x_1}\!f_1(s, 0)\,\dd{s} + \int_0^{x_2}\!f_2(x_1, t)\,\dd{t}
     \implies
     \dd{F} = f_1 \dd{x_1} + f_2 \dd{x_2}.

  なぜならば二つ目の定積分を :math:`x_1` について偏微分して、積分可能条件が使え
  るから。

.. _tsuboi08.1.2.5:

* 例 1.2.5: 積分可能条件を満たすが、:math:`F` が存在しない例

  次の :math:`{\RR^2\minuszero}` 上で定義されている 1 形式は積分可能条件を満た
  す。しかし、:math:`\dd{F}` がこの 1 形式になるような :math:`F` は存在しない
  （曲線として原点を内部に含む円周をとる）：

  .. math::

     -\frac{x_2}{x_1^2 + x_2^2}\dd{x_1} + \frac{x_1}{x_1^2 + x_2^2}\dd{x_2}.

.. _tsuboi08.1.2.6:

* 注意 1.2.6: これは円周上の関数が何か存在していて、それが微分になる関数を求める
  ときの問題である。

.. _tsuboi08.1.2.7:

* 定義 1.2.7: `星型 <http://mathworld.wolfram.com/StarConvex.html>`__

  ユークリッド空間の部分集合 :math:`{U \subset \RR^n}` が星型であるとは、次の条
  件をいう：

  .. math::

     \forall \bm x \in U, \exists \bm y \in U, \quad\text{s.t }
     l_{\bm x} \coloneqq \set{(1 -t)\bm y + t\bm x \sth 0 \le t \le 1} \subset U.

.. _tsuboi08.1.2.8:

* 問題 1.2.8

  * 仮定

    * :math:`{U \subset \RR^n}` が星型である。
    * そこで定義されている各関数 :math:`\fn{f_i}{U}\RR` が積分可能条件を満たす。

  * 結論

    * :math:`{\displaystyle F(\bm x) = \int_{l_{\bm x}}\! \sum_{i = 1}^n f_i\,\dd{x_i}}`
      が :math:`{\displaystyle \dd{F} = \sum_{i = 1}^n f_i \dd{x_i}}` を満たす。

  * 証明

    .. math::

       \begin{align*}
       \frac{\partial F}{\partial x_i}
       &= \frac{\partial}{\partial x_i}\int_{l_{\bm x}}\! \sum_{j = 1}^n f_j\,\dd{x_j}\\
       &= \frac{\partial}{\partial x_i}\int_0^1\! \sum_{j = 1}^n f_j((1 - t)\bm y + t\bm x)(x_j - y_j)\,\dd{x_j}\\
       &= \int_0^1\! \sum_{j = 1}^n \frac{\partial f_j}{\partial x_i}((1 - t)\bm y + t\bm x)(x_j - y_j)t\,\dd{x_j}
          + \int_0^1\! f_i((1 - t)\bm y + t\bm x)\,\dd{t}\\
       &= \Bigl[ f_i((1 - t)\bm y + t\bm x)t\Bigr]_0^1
          - \int_0^1\! \dots \,\dd{t}
          + \int_0^1\! \dots \,\dd{t}\\
       &= f_i(\bm x).
       \end{align*}

    式の変形では chain rule や積分可能条件（上の書き方はわかりにくいか）、および
    部分積分の公式を使う。

1.3 微分 2 形式（基礎）
======================================================================

* 二次元の場合には :math:`{\dfrac{\partial f_2}{\partial x_1} - \dfrac{\partial
  f_1}{\partial x_2}}` は「:math:`{\sum f_i \dd{x_i}}` が :math:`\dd{F}` の形に
  書かれない度合い」を示していると考えられる。
* ここで外積と呼ばれる二項演算 :math:`\wedge` を導入する。計算規則は次の二つしか
  ない：

  * :math:`{x \wedge x = 0}`
  * :math:`{x \wedge y = y \wedge x}`

  あとで一般の場合の定義を与えるので、すぐに忘れてよい。特に上記の反対称性の定義
  は要注意。あくまでも一次同士の外積演算では符号が入れ替わるというだけだ。

  * ライプニッツ則を満たす。

* さらに 1 形式に対して外微分という演算 :math:`\dd{}` を次のように定義する：

  .. math::

     \begin{align*}
     \dd{(f_1 \dd{x1} + f_2 \dd{x_2})}
     &= \dd{f_1} \wedge \dd{x1} + \dd{f_2} \wedge \dd{x2}\\
     &= \left(\dfrac{\partial f_2}{\partial x_1} - \dfrac{\partial f_1}{\partial x_2}\right)\dd{x_1} \wedge \dd{x_2}.
     \end{align*}

  * 1 形式に 2 形式が対応する。
  * この演算を微分であると考える。
  * 平面上の :math:`C^2` 級関数に対して :math:`{\dd{(\dd{f})} = 0}` という性質が
    ある。
  * 一般の場合は後ほど定義する。

.. _tsuboi08.1.3.1:

* 命題 1.3.1: 矩形上の 1 形式の線積分

  :math:`{[a_1, b_1] \times [a_2, b_2]}` 上で定義されている 1 形式
  :math:`\alpha` に対して次の等式が成り立つ（直接計算で示せる）：

  .. math::

     \int_{[a_1, b_1]\times\set{a_2}}\!\alpha
     + \int_{\set{b_1}\times[a_1, b_1]}\!\alpha
     - \int_{[a_1, b_1]\times\set{b_2}}\!\alpha
     - \int_{\set{a_1}\times[a_2, b_2]}\!\alpha
     = \int_{[a_1, b_1]\times[a_2, b_2]}\!\dd{\alpha}.

.. _tsuboi08.1.3.2:

* 定義 1.3.2: 微分 2 形式

  :math:`{U \subset \RR^n}` を開集合とする。微分可能関数
  :math:`\fn{f_{ij}}{U}\RR` に対して次の形式を :math:`U` 上の 2 形式という：

  .. math::

     \sum_{1 \le i \le j \le n}f_{ij}\dd{x_i}\wedge\dd{x_j}.

.. _tsuboi08.1.3.3:

* 定義 1.3.3: 1 形式同士の外積

  .. math::

     \begin{align*}
     \left(\sum_{i = 1}^n f_i \dd{x_i}\right) \wedge \left(\sum_{j = 1}^n g_j \dd{x_j}\right)
     &= \sum_{i, j = 1}^n f_i g_j \dd{x_i} \wedge \dd{x_j}\\
     &= \sum_{1 \le i < j \le n} (f_i g_j - f_j g_i) \dd{x_i} \wedge \dd{x_j}.
     \end{align*}

.. _tsuboi08.1.3.4:

* 定義 1.3.4: 1 形式の外微分

  .. math::

     \begin{align*}
     \dd{\left(\sum_{i = 1}^n f_i \dd{x_i}\right)}
     &= \sum \dd{f_i} \wedge \dd{x_i}\\
     &= \sum_{i, j = 1}^n \frac{\partial f_i}{\partial x_j} \dd{x_j} \wedge \dd{x_i}\\
     &= \sum_{j < i}\left(\frac{\partial f_i}{\partial x_j} - \frac{\partial f_j}{\partial x_i}\right)\dd{x_j} \wedge \dd{x_i}.
     \end{align*}

  ここで各 :math:`\dd{f_i}` は全微分の意味であるとする。

* `閉形式 <http://mathworld.wolfram.com/ClosedForm.html>`__

.. _tsuboi08.1.3.5:

* 定理 1.3.5: :ref:`定理 1.1.3<tsuboi08.1.1.3>` の多変数バージョン

  :math:`{U \subset \RR^n}` が星型であれば、この集合上の閉 1 形式は :math:`U` 上
  で定義された関数の全微分になっている。

  * :ref:`問題 1.2.8<tsuboi08.1.2.8>` を利用する。
  * 本書のあとの方に出てくる記号を用いれば次のように覚えられる：

    .. math::

       \forall \alpha \in Z^1(U),\ \exists f \in \varOmega^0(U)\text{ s.t. }\dd f = \alpha.

.. _tsuboi08.1.3.6:

* 問題 1.3.6: 開集合 :math:`{U \subset \RR^n}` 上の閉 1 形式 :math:`\alpha` は
  :math:`{\alpha \wedge \alpha = 0}`

  * :math:`{\alpha = \sum f_i \dd{x_i}}` とおくと :math:`{\dd{\alpha} = 0.}`
  * (p. 12) の「:ref:`定義 1.3.2<tsuboi08.1.3.2>` の形で書けば……」の展開式を利用
    する。

    .. math::

       \begin{align*}
       \alpha \wedge \alpha
       &= \left(\sum_{i = 1}^n f_i\,\dd x_i\right) \wedge \left(\sum_{i = 1}^n f_i\,\dd x_i\right)\\
       &= \sum_{i, j = 1}^n f_i f_j\,\dd x_i \wedge \dd x_j\\
       &= \sum_{i < j}(f_i f_j - f_j f_i)\,\dd x_i \wedge \dd x_j\\
       &= 0.
       \end{align*}

    * 三番目の等号は :math:`{\dd x_i \wedge \dd x_j = -\dd x_j \wedge \dd x_i}`
      による。特に :math:`{i = j}` の項はキャンセルし合う。
    * 最後の等号は :math:`{f_i f_j = f_j f_i}` による。

.. _tsuboi08.1.3.7:

* 問題 1.3.7: 開集合 :math:`{U \subset \RR^n}` 上の :math:`C^2` 級関数の全微分は
  閉形式である

  * これは単純に次のように展開できることによる：

    .. math::

       \dd{(\dd{f})} = \sum\left(\dfrac{\partial^2 f}{\partial x_i \partial x_j}
                                -\dfrac{\partial^2 f}{\partial x_i \partial x_j}
                           \right)\dd{x_j} \wedge \dd{x_i}

1.4 面積分（基礎）
======================================================================

* 一般の :math:`n` 次元ユークリッド空間上の開集合 :math:`U` 上の 2 形式を微分可
  能な写像 :math:`\fn{\kappa}{\text{(rectangle)}}U` に沿って積分することができ
  る。

  .. math::

     \int_\kappa\!\sum_{i < j} f_{ij}\,\dd{x_i} \wedge \dd{x_j}
     = \int_{a_1}^{b_1}\int_{b_1}^{b_2}\!\sum_{i < j} f_{ij}(\kappa(t_1, t_2))
     \det{D\kappa}\,\dd{t_1}\dd{t_2}.

  * 上の式の :math:`D` はヤコビアンのつもり。実際は二次の行列。
  * また、シグマ記号の添字は :math:`{i, j = 1}` バージョンも考えられる。

.. _tsuboi08.1.4.1:

* 問題 1.4.1: 1 形式の外微分に対する、長方形から開集合 :math:`U` への微分可能写
  像に沿う積分は線積分の和として表される。

  * :math:`{\alpha = \left(\sum_{i = 1}^n f_i\,\dd x_i\right) \in
    \varOmega^1(\RR^n)}`
  * :math:`{\fn{[a_1, b_1] \times [a_2, b_2]}U}` を :math:`C^\infty` 級である写
    像

  とする。このとき次の等式が成り立つ：

  .. math::

     \int_\kappa\!\dd{\left(\sum f_i\,\dd{x_i}\right)} =
     -\int_{\kappa(\cdot,\ b_2)}\alpha
     +\int_{\kappa(\cdot,\ a_2)}\alpha
     +\int_{\kappa(b_1,\ \cdot)}\alpha
     -\int_{\kappa(a_1,\ \cdot)}\alpha.

  * 面積分を線積分で表している。pp. 16-17 も参照。

  .. math::

     \begin{align*}
     \int_\kappa\!\dd\alpha
     &= \int_\kappa\!\sum_{i = 1}^n \dd f_i \wedge \dd x_i\\
     &= \int_\kappa\!\sum_{i < j} \left(
         \frac{\partial f_i}{\partial x_j} - \frac{\partial f_j}{\partial x_i}\right)
         \,\dd x_i \wedge \dd x_j\\
     &= \int_{a_1}^{b_1}\!\int_{a_2}^{b_2}\!\sum_{i < j} \left(
         \frac{\partial f_i}{\partial x_j} - \frac{\partial f_j}{\partial x_i}\right)
         \det{\frac{\partial(\kappa_i, \kappa_j)}{\partial(t_1, t_2)}}\,\dd t_1\dd t_2\\
     &= -\int_{a_1}^{b_1}\!\int_{a_2}^{b_2}\!\sum_{i, j = 1}^n
         \frac{\partial f_i}{\partial x_j}
         \det{\frac{\partial(\kappa_i, \kappa_j)}{\partial(t_1, t_2)}}\,\dd t_1\dd t_2\\
     &= -\int_{a_1}^{b_1}\!\int_{a_2}^{b_2}\!\sum_{i, j = 1}^n\left(
         \frac{\partial f_i}{\partial x_j} \frac{\partial \kappa_j}{\partial t_2} \frac{\partial \kappa_1}{\partial t_1}
             - \frac{\partial f_i}{\partial x_j} \frac{\partial \kappa_j}{\partial t_1} \frac{\partial \kappa_1}{\partial t_2}\right)
         \,\dd t_1\dd t_2\\
     &= -\int_{a_1}^{b_1}\!\int_{a_2}^{b_2}\!\sum_{i, j = 1}^n\left(
         \sum_{i = 1}^n \frac{\partial f_i(\kappa)}{\partial t_2}\frac{\partial \kappa_i}{\partial t_1}
             - \sum_{i = 1}^n \frac{\partial f_i(\kappa)}{\partial t_1}\frac{\partial \kappa_i}{\partial t_2}\right)
         \,\dd t_1\dd t_2\\
     \end{align*}

  * 最初の等号は外微分を微分形式に適用した。
  * 二番目の等号は p. 12 の式による。
  * 三番目の等号は p. 13 の式による。
  * 四番目の等号は :math:`{i = j}` のときには行列式がゼロであることによる。
  * 以降の式変形では :math:`{[a_1, b_1]}` 側は :math:`t_2` で、:math:`{[a_2,
    b_2]}` 側は :math:`t_1` でそれぞれ積分する。

  式を書くのが面倒なので :math:`{[a_1, b_1]}` 側のみ展開する：

  .. math::

     \begin{align*}
     -\int_{a_1}^{b_1}\!\int_{a_2}^{b_2}\!\sum_{i, j = 1}^n\left(
         \sum_{i = 1}^n \frac{\partial f_i(\kappa)}{\partial t_2}\frac{\partial \kappa_i}{\partial t_1}\right)
         \,\dd t_1\dd t_2
     &= -\int_{a_1}^{b_1}\!\left[\sum_{i = 1}^n f_i(\kappa(t))\right]_{a_2}^{b_2}
         \frac{\partial \kappa_i}{\partial t_i}\,\dd t_1\\
     &= -\int_{a_1}^{b_1}\!\sum_{i = 1}^n (f_i(\kappa(t_1, b_2)) - f_i(\kappa(t_1, a_2)))
         \frac{\partial \kappa_i}{\partial t_i}\,\dd t_1\\
     &= -\int_{\kappa(\cdot,\ b_2)}\alpha
        +\int_{\kappa(\cdot,\ a_2)}\alpha.
     \end{align*}

  :math:`{[a_2, b_2]}` 側も同様にして示せる。

箱の表面で面積分を考えると 2 形式の長方形と 1 形式との関係とよく似ている。

1.5 3 次元ユークリッド空間上のベクトル解析（基礎）
======================================================================

* 微分形式の理論の起源はベクトル解析にある。
* この節では微分形式とナブラ記号を使う方式との記法の関係を整理する。

  * :math:`\grad f,\ \nabla f` と :math:`\dd{f}` との関係。:math:`\dd{f}` の係数
    の縦ベクトルが :math:`\grad f` だ。
  * :math:`{\rot \vec f,}\ {\curl \vec f,}\ {\nabla\times \vec f}` と三次元 1 形
    式 :math:`\alpha` との関係。:math:`\dd{\alpha}` の係数が :math:`{\rot \vec
    f}` だ。
  * :math:`{\div \vec g},\ {\nabla \cdot \vec g}` と三次元 2 形式 :math:`\beta`
    との関係。:math:`\dd{\beta}` の係数が :math:`\div` だ。
  * :math:`{\rot \circ \grad = 0,}\ {\div \circ \rot = 0}` と :math:`{\dd{}
    \circ \dd{} = 0}` との関係
  * ガウスの定理
  * ベクトルとポテンシャル
  * :math:`{\vec g = \rot \vec f}` なる :math:`\vec f` とは？
  * :math:`{\div \vec g = 0 \iff \dd{\beta} = 0}`
  * etc.

.. _tsuboi08.1.5.1:

* 問題 1.5.1: :math:`{\rot \circ \grad = 0,\ \div \circ \rot = 0}`

  * :math:`{\rot(\grad(f)) = 0}` を SymPy で確かめるとこのような感じになる：

    .. code:: ipython

       In [1]: from sympy import Function, symbols

       In [2]: from sympy.vector import CoordSys3D

       In [3]: R = CoordSys3D('R')

       In [4]: f = Function('f')(R.x, R.y, R.z)

       In [5]: from sympy.vector import gradient, curl, divergence

       In [6]: curl(gradient(f)).doit()
       Out[6]: (Derivative(f(R.x, R.y, R.z), R.y, R.z) - Derivative(f(R.x, R.y, R.z), R.z, R.y))*R.i
       + (-Derivative(f(R.x, R.y, R.z), R.x, R.z) + Derivative(f(R.x, R.y, R.z), R.z, R.x))*R.j
       + (Derivative(f(R.x, R.y, R.z), R.x, R.y) - Derivative(f(R.x, R.y, R.z), R.y, R.x))*R.k

  * :math:`{\div(\rot(f)) = 0}` はこのような感じになる：

    .. code:: ipython

       In [7]: f1, f2, f3 = symbols('f1:4', cls=Function)

       In [8]: divergence(curl(f1(R.x, R.y, R.z)*R.i + f2(R.x, R.y, R.z)*R.y + f3(R.x, R.y, R.z) * R.k))
       Out[8]: -Derivative(f1(R.x, R.y, R.z), R.y, R.z)
       + Derivative(f1(R.x, R.y, R.z), R.z, R.y)
       + Derivative(f2(R.x, R.y, R.z), R.x, R.z)
       - Derivative(f2(R.x, R.y, R.z), R.z, R.x)
       - Derivative(f3(R.x, R.y, R.z), R.x, R.y)
       + Derivative(f3(R.x, R.y, R.z), R.y, R.x)

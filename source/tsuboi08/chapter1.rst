======================================================================
第 1 章 ユークリッド空間上の微分形式
======================================================================

.. contents:: ノート目次

1.1 微積分学の基本定理（基礎）
======================================================================
* 定義 1.1.1: 原始関数

.. _tsuboi08.1.1.2:

* 定理 1.1.2: 定積分の存在

.. _tsuboi08.1.1.3:

* 定理 1.1.3: `微積分学の基本定理 <http://mathworld.wolfram.com/FundamentalTheoremsofCalculus.html>`__

(pp. 2-3) の「余談」がとてもいい。
面積を求めることと接線を求めることの関係が 1.1.3 として述べられた。

1.2 微積分学の基本定理の多変数化（基礎）
======================================================================

.. _tsuboi08.1.2.1:

* 定義 1.2.1: 微分 1 形式、
  `線積分 <http://mathworld.wolfram.com/LineIntegral.html>`__

  まず次のような状況において「関数の値の差」を考察する：

  * :math:`U \subset \RR^n` を弧状連結開集合とする。
  * 関数 :math:`\fn{f}{U}{\RR}` および写像 :math:`\fn{\gamma}{[a, b]}U` を微分可能とする。
    さらに次の対応があるとする： 

    * :math:`\gamma(a) = \bm y, \gamma(b) = \bm z,`
    * :math:`\bm y, \bm z \in U.`

  差を次のように表現する：

  .. math::

     \begin{align*}
     f(\bm z) - f(\bm y) &= f \circ \gamma(b) - f \circ \gamma(a)\\
     &= \int_a^b\! \diff{(f \circ \gamma(t))}{t}\,\dd{t}\\
     &= \int_a^b\! \sum_{i = 1}^n \frac{\partial f}{\partial x_i}(\gamma(t))\diff{\gamma_i}{t}(t)\,\dd{t}\\
     &= \int_\gamma\sum_{i = 1}^n \frac{\partial f}{\partial x_i}\dd{x}_i.
     \end{align*}

  * :math:`\displaystyle \sum_{i = 1}^n f_i \dd{x}_i` を :math:`U` 上の
    微分 1 形式 or 1 次微分形式 or 1 形式という。

  * :math:`\displaystyle \int_\gamma\sum_{i = 1}^n f_i\dd{x}_i` を上述の式のように定義し、
    これを線積分という。

  * 各 :math:`\dd{x_i}` を 何らかの n 次元線形空間の
    :math:`x_i` 方向の基底のようなものという解釈を今のところはとることにする。

.. _tsuboi08.1.2.2:

* 定義 1.2.2: 全微分

  先ほどの式の最後の線積分の被積分部を :math:`f` の全微分と言う：

  .. math::

     \dd{f} = \sum_{i = 0}^n \frac{\partial f}{\partial x_i}\dd{x}_i.

.. _tsuboi08.1.2.3:

* 定理 1.2.3: :ref:`定理 1.1.3 <tsuboi08.1.1.3>` の一般化

  1 形式についての線積分は先ほどの式と整合する：

  .. math::

     \int_\gamma df = f \circ \gamma(b) - f \circ \gamma(a).

* 積分可能条件とは :math:`\dfrac{\partial f_i}{\partial x_j} = \dfrac{\partial f_j}{\partial x_i}`
  がすべての :math:`1 \le i, j \le n` について成り立つことを言う。

* 積分可能条件を満たす :math:`f` について、次の等式が成り立つような
  :math:`U` 上の関数 :math:`F` は存在するだろうかということを以下考察する：

  .. math::

     \dd{F} = \sum_{i = 1}^n f_i \dd{x_i}.

.. _tsuboi08.1.2.4:

* 例 1.2.4: 2 次元のある例

  .. math::

     F(x_1, x_2) = \int_0^{x_1}\!f_1(s, 0)\,\dd{s} + \int_0^{x_2}\!f_2(x_1, t)\,\dd{t}
     \implies
     \dd{F} = f_1 \dd{x_1} + f_2 \dd{x_2}.

  なぜならば二つ目の定積分を :math:`x_1` について偏微分して、積分可能条件が使えるから。

.. _tsuboi08.1.2.5:

* 例 1.2.5: 積分可能条件を満たすが、:math:`F` が存在しない例

  次の :math:`\RR^2\minuszero` 上で定義されている 1 形式は積分可能条件を満たす。
  しかし、:math:`\dd{F}` がこの 1 形式になるような :math:`F` は存在しない
  （曲線として原点を内部に含む円周をとる）：

  .. math::

     -\frac{x_2}{x_1^2 + x_2^2}\dd{x_1} + \frac{x_1}{x_1^2 + x_2^2}\dd{x_2}.

.. _tsuboi08.1.2.6:

* 注意 1.2.6: これは円周上の関数が何か存在していて、
  それが微分になる関数を求めるときの問題である。

.. _tsuboi08.1.2.7:

* 定義 1.2.7: `星型 <http://mathworld.wolfram.com/StarConvex.html>`__

  ユークリッド空間の部分集合 :math:`U \subset \RR^n` が星型であるとは、
  次の条件をいう：

  .. math::

     \forall \bm x \in U, \exists \bm y \in U, \quad\text{s.t }
     l_{\bm x} := \set{(1 -t)\bm y + t\bm x \sth 0 \le t \le 1} \subset U.

.. _tsuboi08.1.2.8:

* 問題 1.2.8

  * 仮定

    * :math:`U \subset \RR^n` が星型である。
    * そこで定義されている各関数 :math:`\fn{f_i}{U}\RR` が積分可能条件を満たす。

  * 結論

    * :math:`\displaystyle F(\bm x) = \int_{l_{\bm x}}\! \sum_{i = 1}^n f_i\,\dd{x_i}`
      が :math:`\displaystyle \dd{F} = \sum_{i = 1}^n f_i \dd{x_i}` を満たす。

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

    式の変形では chain rule や積分可能条件（上の書き方はわかりにくいか）、
    および部分積分の公式を使う。

1.3 微分 2 形式（基礎）
======================================================================
* 2 次元の場合には :math:`\dfrac{\partial f_2}{\partial x_1} - \dfrac{\partial f_1}{\partial x_2}` は
  「:math:`\sum f_i \dd{x_i}` が :math:`\dd{F}` の形に書かれない度合い」を示していると考えられる。

* ここで外積と呼ばれる二項演算 :math:`\wedge` を導入する。
  計算規則は次の二つしかない：

  * :math:`x \wedge x = 0`
  * :math:`x \wedge y = y \wedge x`

  あとで一般の場合の定義を与えるので、すぐに忘れてよい。
  特に上記の反対称性の定義は要注意。
  あくまでも 1 次同士の外積演算では符号が入れ替わるというだけだ。

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
  * 平面上の :math:`C^2` 級関数に対して :math:`\dd{(\dd{f})} = 0` という性質がある。
  * 一般の場合は後ほど定義する。

.. _tsuboi08.1.3.1:

* 命題 1.3.1: 矩形上の 1 形式の線積分

  :math:`[a_1, b_1] \times [a_2, b_2]` 上で定義されている 1 形式 :math:`\alpha` に対して
  次の等式が成り立つ（直接計算で示せる）：

  .. math::

     \int_{[a_1, b_1]\times\set{a_2}}\!\alpha
     + \int_{\set{b_1}\times[a_1, b_1]}\!\alpha
     - \int_{[a_1, b_1]\times\set{b_2}}\!\alpha
     - \int_{\set{a_1}\times[a_2, b_2]}\!\alpha
     = \int_{[a_1, b_1]\times[a_2, b_2]}\!\dd{\alpha}.

.. _tsuboi08.1.3.2:

* 定義 1.3.2: 微分 2 形式

  :math:`U \subset \RR^n` を開集合とする。
  微分可能関数 :math:`\fn{f_{ij}}{U}\RR` に対して次の形式を :math:`U` 上の 2 形式という：

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

* 定理 1.3.5: :ref:`定理 1.1.3 <tsuboi08.1.1.3>` の多変数バージョン

  :math:`U \subset \RR^n` が星型であれば、この集合上の閉 1 形式は
  :math:`U` 上で定義された関数の全微分になっている。

.. _tsuboi08.1.3.6:

* 問題 1.3.6: 開集合 :math:`U \subset \RR^n` 上の閉 1 形式 :math:`\alpha` は
  :math:`\alpha \wedge \alpha = 0`

  * :math:`\alpha = \sum f_i \dd{x_i}` とおくと :math:`\dd{\alpha} = 0.`
  * (p. 12) の「:ref:`定義 1.3.2 <tsuboi08.1.3.2>` の形で書けば……」の展開式を利用する。

.. _tsuboi08.1.3.7:

* 問題 1.3.7: 開集合 :math:`U \subset \RR^n` 上の :math:`C^2` 級関数の全微分は閉形式である

  * これは単純に次のように展開できることによる：

    .. math::

       \dd{(\dd{f})} = \sum\left(\dfrac{\partial^2 f}{\partial x_i \partial x_j}
                                -\dfrac{\partial^2 f}{\partial x_i \partial x_j}
                           \right)\dd{x_j} \wedge \dd{x_i}

1.4 面積分（基礎）
======================================================================
* 一般の n 次元ユークリッド空間上の開集合 :math:`U` 上の 2 形式を
  微分可能な写像 :math:`\fn{\kappa}{\text{(rectangle)}}U` に沿って積分することができる。

  .. math::

     \int_\kappa\!\sum_{i < j} f_{ij}\,\dd{x_i} \wedge \dd{x_j}
     = \int_{a_1}^{b_1}\int_{b_1}^{b_2}\!\sum_{i < j} f_{ij}(\kappa(t_1, t_2))
     \det{D\kappa}\,\dd{t_1}\dd{t_2}.

  * 上の式の :math:`D` はヤコビアンのつもり。実際は 2 次の行列。
  * また、シグマ記号の添字は :math:`i, j = 1` バージョンも考えられる。

.. _tsuboi08.1.4.1:

* 問題 1.4.1: 1 形式の外微分に対する、長方形から開集合 :math:`U` への微分可能写像に沿う積分は
  線積分の和として表される。

  .. math::

     \int_\kappa\!\dd{\left(\sum f_i\,\dd{x_i}\right)} =
     -\int_{\kappa(\cdot,\ b_2)}\cdot
     +\int_{\kappa(\cdot,\ a_2)}\cdot
     +\int_{\kappa(b_1,\ \cdot)}\cdot
     -\int_{\kappa(a_1,\ \cdot)}\cdot.

  * 面積分を線積分で表している。pp. 16-17 も参照。

箱の表面で面積分を考えると 2 形式の長方形と 1 形式との関係とよく似ている。

1.5 3 次元ユークリッド空間上のベクトル解析（基礎）
======================================================================
* 微分形式の理論の起源はベクトル解析にある。
* この節では微分形式とナブラ記号を使う方式との記法の関係を整理する。

  * :math:`\grad f,\ \nabla f` と :math:`\dd{f}` との関係。
    :math:`\dd{f}` の係数の縦ベクトルが :math:`\grad f` だ。

  * :math:`\rot \vec f,\ \curl \vec f,\ \nabla\times \vec f` と 3 次元 1 形式 :math:`\alpha` との関係。
    :math:`\dd{\alpha}` の係数が :math:`\rot \vec f` だ。

  * :math:`\div \vec g,\ \nabla \cdot \vec g` と 3 次元 2 形式 :math:`\beta` との関係。
    :math:`\dd{\beta}` の係数が :math:`\div` だ。

  * :math:`\rot \circ \grad = 0,\ \div \circ \rot = 0` と :math:`\dd{} \circ \dd{} = 0` との関係
  * ガウスの定理
  * ベクトルとポテンシャル
  * :math:`\vec g = \rot \vec f` なる :math:`\vec f` とは？
  * :math:`\div \vec g = 0 \iff \dd{\beta} = 0`
  * etc.

.. _tsuboi08.1.5.1:

* 問題 1.5.1: :math:`\rot \circ \grad = 0,\ \div \circ \rot = 0`

  * 完全に直接計算だけの証明となるので、あとで SymPy にやらせたい。

1.6 一般の微分形式
======================================================================
冒頭の番号が付いていない図式にある「グラフ」がいい。

* 一般の次元のユークリッド空間の開集合上に p 形式を定義したいので、
  :math:`\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}` をすべて定義する。

.. _tsuboi08.1.6.1:

* 定義 1.6.1: `p 形式 <http://mathworld.wolfram.com/Differentialk-Form.html>`__

  * 各 :math:`f_{x_{i_1}} \dots f_{x_{i_p}}` を連続関数とする。
  * この p を微分形式の次数という。

.. _tsuboi08.1.6.2:

* 定義 1.6.2: `外積 <http://mathworld.wolfram.com/WedgeProduct.html>`__

  * 同じ添字が一つでもあれば :math:`\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}} = 0.`
  * 添字の集合が同じだが配列が異なる場合は、それらの置換の符号を外積の違いとする。
    これは数式で表現したほうがわかりにくいので、あえてこのように書き残しておく。

    * あとで出てくる :ref:`定義 1.6.8 <tsuboi08.1.6.8>` のほうが見やすい。

  * 結合則は普通に使える。

.. _tsuboi08.1.6.3:

* 例 1.6.3: 標準的 `シンプレクティック形式 <http://mathworld.wolfram.com/SymplecticForm.html>`__

  * 2 形式 :math:`\displaystyle \omega = \sum_{i = 1}^n \dd{x_{2i - 1}} \wedge \dd{x_{2i}}`
    の n 個の外積は次の 2n 形式になる：

    .. math::

       \overbrace{\omega \wedge \dotsb \wedge \omega}^\text{n}
       = n\,! \dd{x_1} \wedge \dotsb \wedge \dd{x_{2n}}.

.. _tsuboi08.1.6.4:

* 例題 1.6.4: 次数付き可換性

  .. math::

     \beta \wedge \alpha = (-1)^{\alpha\beta}\alpha \wedge \beta.

  * :math:`pq` 回の隣接ペアの swap で一方が他方に移るから。
  * これをしっかり意識しないとたいていの計算を間違うことになる。

.. _tsuboi08.1.6.5:

* 定義 1.6.5: `外微分 <http://mathworld.wolfram.com/ExteriorDerivative.html>`__

  .. math::

     \dd{\left(\sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p}\, \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}\right)}
     = \sum_{i_1 < \dotsb < i_p} \dd{f_{i_1 \dots i_p}} \wedge \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}.

  .. TeX コードをタイプするのがたいへん面倒なので、マクロを定義しないとダメか？

.. _tsuboi08.1.6.6:

* 例 1.6.6: 標準的接触形式

  .. math::

     \begin{align*}
     \alpha &= \dd{x_{2n + 1}} + \sum_{i = 1}^n x_{2i - 1}\dd{x_{2i}},\\
     \dd{\alpha} &= \sum_{i = 1}^n \dd{x_{2i - 1}} \wedge \dd{x_{2i}},\\
     \alpha \wedge \overbrace{\dd{\alpha} \wedge \dotsb \wedge \dd{\alpha}}^\text{n} &=
       n\,! \dd{x_1} \wedge \dotsb \wedge \dd{x_{2n + 1}}.
     \end{align*}

.. _tsuboi08.1.6.7:

* 例題 1.6.7

  .. math::

     \dd(\alpha \wedge \beta) = \dd\alpha \wedge \beta + (-1)^p\alpha \wedge \beta.

  * 例によって符号が次数に依ることに注意。
  * 証明方法は具体的に微分形式を定義して計算すればよい。

.. _tsuboi08.1.6.8:

* 定義 1.6.8: 微分形式の積分

  * 開集合 :math:`U \subset \RR^n` 上の写像 :math:`\fn{\kappa}{[a_1, b_1] \times \dotsb \times [a_p, b_p]}U`
    に沿う積分を次の式で定義する：

    .. math::

       \int_\kappa\!\sum_{i_1 < \dotsb < i_p}f_{i_1 \dots i_p}\,\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}
       = \int_{a_1}^{b_1}\dots\int_{a_p}^{b_p}\!\sum_{i_1 < \dotsb < i_p}f_{i_1 \dots i_p}(
         \kappa(t_1, \dotsc, t_p))\det(D\kappa)\,\dd{t_1}\dots\dd{t_p}.

    ただし :math:`D\kappa` と書いたのは :math:`\kappa_{i_1}, \dotsc, \kappa_{i_p}` を
    :math:`t_1, \dotsc, t_p` でヤコビアンにしたもの。スペースの都合でこう書いた。

  * シグマ記号は別の添字の付け方も採用する。
  * ここで各添字が相異なる場合は次の関係式が成り立つ：

    .. math::

       \dd{x_{j_1}} \wedge \dotsb \wedge \dd{x_{j_p}} = \operatorname{sign}
       \begin{pmatrix}j_1 & \dots & j_p\\i_1 & \dots & i_p\end{pmatrix}
       \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}.

  * 実は次のように書け、以降でこれを利用する：

    .. math::

       \int_\kappa\!\alpha = \int_\id\!\kappa\alpha.

.. _tsuboi08.1.6.9:

* 例題 1.6.9: 直方体版ストークスの定理

  * 開集合 :math:`U` に沿う積分が :math:`p + 1` 次元直方体から :math:`U` への
    写像 :math:`\kappa` に沿う積分の和となる：

    .. math::

       \int_\kappa\,\dd{\alpha} = \sum_{q = 1}^{p + 1}(-1)^{q - 1}
       \left(
       \int_{\kappa(\dots b_q \dots)}\,\alpha - \int_{\kappa(\dots a_q \dots)}\,\alpha
       \right).

  * 今のところ証明方法は腕力による。あとで別バージョンが紹介される。

1.7 ユークリッド空間の開集合上の微分形式の空間
======================================================================
以下 :math:`C^\infty` 級関数、微分形式のみを考える。

* 約束として 0 形式とは関数全体とする。
* 記号 :math:`\Omega^p(U)` で :math:`U` 上の p 形式全体を表す。

  * :math:`\Omega^p(U)` は（集合が空集合でなければ）無限次元ベクトル空間である。
  * :math:`p < 0 \text{ or } n < p \implies \Omega^p(U) = \zeroset` とする。
  * 演算 :math:`\fn{\dd{}}{\Omega^p(U)}\Omega^{p + 1}(U)` は線形写像である。

.. todo:: `コチェイン複体 <http://mathworld.wolfram.com/CochainComplex.html>`__ の定義。

.. _tsuboi08.1.7.1:

* 定理 1.7.1: :math:`\fn{\dd \circ \dd}{\Omega^p(U)}\Omega^{p + 2}(U)` は 0 準同型である

  * 基底に対しては :math:`\dd{(\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}})} = 0.`
  * 一般には次のようになってやはりゼロだ：

    .. math::

       \begin{align*}
       \dd{(\dd{(f_{i_1 \dots i_p}\, \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}})})}
       &= \dd{(\dd{f_{i_1 \dots i_p}}\, \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}})}\\
       &= \underbrace{\dd{(\dd{f_{i_1 \dots i_p}})}}_\text{0}\, \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}} + \dd{f_{i_1 \dots i_p}} \wedge 
          \underbrace{\dd{(\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}})}}_\text{0}\\
       &= 0.
       \end{align*}

.. _tsuboi08.1.7.2:

* 定理 1.7.2: `ポアンカレの補題 <http://mathworld.wolfram.com/PoincaresLemma.html>`__

  * 星型 :math:`U` 上の p 形式 :math:`\alpha` が :math:`\dd{\alpha} = 0` ならば
    :math:`\dd{\beta} = \alpha` なる p - 1 形式 :math:`\beta` が存在する。

  * cf. :ref:`問題 1.2.8 <tsuboi08.1.2.8>`
  * 証明は後ほど行なう。

1.8 微分形式の引き戻し
======================================================================
図 1.6 の状況をいつでも思い浮かべられるようにしておきたい。
当分の間、次の記号を用いる：

* :math:`V \subset \RR^m,\ W \subset \RR^n` を開集合とする。
* :math:`\fn{\varphi}{V}W` を :math:`C^\infty` 級写像とする。
* 座標表示を :math:`\varphi(\bm x) = \bm y,\ y_i = \varphi_i(x_1, \dotsc, x_m)` とする。
* :math:`\fn{f}{W}\RR` を :math:`C^1` 級写像とする。

* 定義 1.8.1: 1 形式の引き戻し

  .. math::

     \begin{align*}
     \varphi^*\left(\sum_{i = 1}^n f_i\,\dd{y_i}\right) &=
     \sum_{i = 1}^n\sum_{j = 1}^m f_i \circ \varphi \frac{\partial \varphi_i}{\partial x_j}\,\dd{x_j}\\
     &= \sum_{i = 1}^n(\varphi^* f_i)(\varphi^* \,\dd{y_i})\\
     &= \sum_{i = 1}^n \varphi^* f_i\,\dd{\varphi_i}.
     \end{align*}

  * 最後の等式は形式的なものだ。
  * 関数の引き戻しを :math:`\varphi^* f = f \circ \varphi` で定義する。

.. _tsuboi08.1.8.2:

* 命題 1.8.2: :math:`\dd{(\varphi^* f)} = \varphi^* \dd{f}`

..

* 1 形式 :math:`\alpha` に対して次が成り立つ：

  .. math::

     \int_\gamma\!\varphi^*\alpha = \int_{\varphi \circ \gamma}\!\alpha.

.. _tsuboi08.1.8.3:

* 定義 1.8.3: p 形式の引き戻し

  .. math::

     \alpha = \sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p}\,\dd{y_{i_1}} \wedge \dotsb \wedge \dd{y_{i_p}}
     \implies\\
     \varphi^* \alpha = \sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p} \circ \varphi\,\dd{\varphi_{i_1}} \wedge \dotsb \wedge \dd{\varphi_{i_p}}.

  ここで各 :math:`\dd{\varphi_{i_j}}` は全微分の意味にとること。

.. _tsuboi08.1.8.4:

* 例 1.8.4: いろいろ

  * :math:`V \subset W` という状況における包含写像 :math:`\fn{\iota}{V}W` と
    :math:`\iota^* \alpha = \alpha|V` の関係（説明のみ）。

  * :math:`m < n` とすれば :math:`\fnm{\iota}{\RR^m}{\RR^n}{(x_1, \dotsc, x_m)}(x_1, \dotsc, x_m, 0, \dotsc, 0)` である。
    このとき :math:`\alpha \in \Omega^p(\RR^n)` に対する次の値を :math:`\alpha|\RR^n` と書くことがある：

    .. math::

       \iota^*\alpha = \sum_{i_1 < \dotsb < i_p \le m} f_{i_1 \dots i_p} \circ \iota\,\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}.

  * :math:`\fnm{\pi}{\RR^n}{\RR^m}{(x_1, \dotsc, x_m, \dotsc, x_n)}(x_1, \dotsc, x_m)` とする。
    このとき :math:`\alpha \in \Omega^p(\RR^m)` に対して次の式が成り立つ：

    .. math::

       \pi^*\alpha = \sum_{i_1 < \dotsb < i_p \le m} f_{i_1 \dots i_p} \circ \pi\,\dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}.

    添字が :math:`m + 1` 以上の項はない。

.. _tsuboi08.1.8.5:

* 問題 1.8.5: 線形写像の引き戻し？

  * 仮定

    * :math:`\omega = \dd{x_1} \wedge \dotsb \wedge \dd{x_n}`
    * 線形写像 :math:`\fn{L}{\RR^n}\RR^n` の表現行列を :math:`A = (a_{ij})` とする。

  * 結論

    * :math:`L^*\omega = \det A.`
    * 式変形の途中で出てくる :math:`\dd{x_{j_1}} \wedge \dotsb \wedge \dd{x_{j_n}}` が
      ゼロでない値となるには、この添字の配列が n 次の permutation である必要がある。
    * 与式は次のようになる：

      .. math::

         \sum_{\sigma \in \mathfrak S^n} \operatorname{sign} \sigma(
           a_{1\sigma(1)}\dots a_{n\sigma(n)})
           \dd{x_1} \wedge \dotsb \wedge \dd{x_n}.

.. _tsuboi08.1.8.6:

* 問題 1.8.6: :math:`\omega = \dd{x_1} \wedge \dd{x_2} + \dd{x_3} \wedge \dd{x_4}`

  * :math:`\fnm{L}{\RR^2}{\RR^4}{(u_1, u_2)}\left(\sum_{j = 1, 2}a_{ij}u_j\right)_{i = 1, \dotsc, 4}`
  * :math:`L^*\omega = 0` の条件は何か。

    * これは素直に計算すればわかる。
      結局 :math:`\dd{u_1} \wedge \dd{u_2}` の係数がゼロになる条件を求めることになる。

.. _tsuboi08.1.8.7:

* 問題 1.8.7: 引き戻しと外微分の計算 :math:`\alpha = \dd{z} + x\dd{y}`

  .. todo:: 自力でも計算したが、数式は SymPy で生成したい。

  * :math:`\fnm{F}{\RR^3}{\RR^3}{(x, y, z)}\left(x, y, z - \frac{xy}{2}\right)`
    に対する :math:`F^*\alpha` の値？

  * :math:`F` のヤコビアンと :math:`\alpha \wedge \dd{\alpha}` と
    :math:`F^*\alpha \wedge \dd{F^*\alpha}` の値？

  * :math:`\varphi_t(x, y, z) = (x\cos t - y \sin t, x \sin t + y \cos t, z)` に対する
    :math:`\varphi_t^* F^* \alpha` の値？

  * :math:`\fnm{G}{\RR^3}{\RR^3}{(x, y, z)}(x, y, z - xy)` および
    :math:`\fnm{H}{\RR^3}{\RR^3}{(x, y, z)}(x, y \cos x - z \sin x, y \sin x + z \cos x)` に対して
    :math:`H^* G^* \alpha` の値？

  * :math:`\det D(G \circ H)` および :math:`H^* G^* \alpha \wedge \dd{H^* G^* \alpha}` の値？

    * ヤコビアンの行列式は 1 となるが、途中 chain rule に注意。
    * 後半は三角関数の simplify に注意。

* 微分形式の引き戻しの外積は外積の引き戻しである。

.. _tsuboi08.1.8.8:

* 例題 1.8.8: :math:`\varphi^*(\alpha \wedge \beta) = \varphi^*\alpha \wedge \varphi^* \beta`

  * :math:`\alpha = \sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p}\,\dd{y_{i_1}} \wedge \dotsb \wedge \dd{y_{i_p}}` などと置いて
    直接計算により示せる。

  * :math:`\varphi^*(f_{i_1 \dots i_p} g_{j_1 \dots j_q}) = (f \circ \varphi)(g \circ \varphi)` を利用する。

.. _tsuboi08.1.8.9:

* 例題 1.8.9: :math:`\psi^* \varphi^*\alpha = (\varphi \circ \psi)^*\alpha`

  * :math:`\alpha` を上の例題のようにとり、与式の右辺を展開していく。

    .. math::

       (\varphi \circ \psi)^*\alpha = \sum_{j_1 < \dotsb < j_p} f_{j_1 \dots j_p} \circ \varphi \circ \psi\,
         \dd{(\varphi_{j_1} \circ \psi)} \wedge \dotsb \wedge
         \dd{(\varphi_{j_p} \circ \psi)}.

  * 次に :math:`\displaystyle \varphi_{j_i} \circ \psi = \sum_{k = 1}^m \frac{\partial \varphi_{j_i}}{\partial x_k}\,\dd{\psi_k}` か。

  * この次の式変形が思いつかない。
    :math:`\dd{\psi_?}` を :math:`\dd{x_?}` と書き換えたい。
    全体を :math:`\psi^*(\quad)` で囲むような。

.. _tsuboi08.1.8.10:

* 定理 1.8.10: 積分の変形？

  * :math:`C^\infty` 級写像 :math:`\fn{\varphi}{V}W` および
  * :math:`C^\infty` 級写像 :math:`\fn{\kappa}{[a_1, b_1] \times \dotsb \times [a_p, b_p]}V` と
  * :math:`W \subset \RR^n` 上の p 形式 :math:`\alpha`

  に対して次が成り立つ：

  .. math::

     \int_\kappa\!\varphi^*\alpha = \int_{\varphi \circ \kappa}\!\alpha.

  * 証明中の式変形では p. 31 の文章中の等式（下に書く）と
    :ref:`例題 1.8.9 <tsuboi08.1.8.9>` の結果を利用する。

    .. math::

       \int_\kappa\!\varphi^*\alpha = \int_{\id}\!\kappa^*\varphi^*\alpha.

  * :math:`\id` が出てくるのがミソか。

.. _tsuboi08.1.8.11:

* 定理 1.8.11: 外微分と引き戻しは可換 :math:`\dd{\varphi^*\alpha} = \varphi^*\dd{\alpha}`

  * 外微分と引き戻しはどちらも直方体からの写像に沿う積分と整合するように定義されたものだった。
  * 証明はいつものように :math:`\alpha` をおいて、順次展開する：

    .. math::

       \begin{align*}
       \dd{(\varphi^*\alpha)}
       &= \dd{\left(\varphi^* \sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p}\,\dd{y_{i_1}} \wedge \dotsb \wedge \dd{y_{i_p}}\right)}\\
       &= \dd{\left(\sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p} \circ \varphi\,\dd{\varphi_{i_1}} \wedge \dotsb \wedge \dd{\varphi_{i_p}}\right)}\\
       &= \sum_{i_1 < \dotsb < i_p} \dd{(f_{i_1 \dots i_p} \circ \varphi)} \wedge \dd{\varphi_{i_1}} \wedge \dotsb \wedge \dd{\varphi_{i_p}}\\
       &= \varphi^*\left(\sum_{i_1 < \dotsb < i_p} \dd{f_{i_1 \dots i_p}} \wedge \dd{y_{i_1}} \wedge \dotsb \wedge \dd{y_{i_p}}\right)\\
       &= \varphi^*\dd{\alpha}.
       \end{align*}

..

* :ref:`例題 1.6.9 <tsuboi08.1.6.9>` の別解を紹介している。

  * :math:`\alpha` が p 形式であれば :math:`\kappa^*\alpha` もそうなので、
    トリッキーだと思うが次の式のようにおく：
    
    .. math::
    
       \kappa^*\alpha = \sum_{q = 1}^{p + 1} f_q\,\dd{t_1} \wedge \dotsb \wedge
       \dd{t_{q - 1}} \wedge \dd{t_{q + 1}}
       \wedge \dotsb \wedge \dd{t_{p + 1}}.

  * 次に :math:`\kappa^*(\dd{\alpha})` を計算すると、次に示す微分形式の和である：
  
    .. math::
    
       \sum_{q = 1}^{p + 1} (-1)^{q - 1} \frac{\partial f_q}{\partial t_q}
       \dd{t_1} \wedge \dotsb \wedge \dd{t_{p + 1}}.

  * あとは :math:`\dd\alpha` を :math:`\kappa` に沿って積分していくと
    :ref:`例題 1.6.9 <tsuboi08.1.6.9>` の右辺が得られる。

    * この過程で :ref:`定義 1.8.11 <tsuboi08.1.8.11>`, 部分積分、
      :ref:`定理 1.8.10 <tsuboi08.1.8.10>` を利用するようだ。
      途中で行列式が一切出て来ないのが特徴か？

1.9 ポアンカレの補題の証明
======================================================================
.. _tsuboi08.1.9.1:

* 命題 1.9.1 :math:`\dd{I(\alpha)} + I(\dd{\alpha}) = \alpha - \pi^*(\iota_0^*\alpha)`

  * :math:`U \subset \RR^n` を開集合、
  * :math:`\alpha` を直積 :math:`[0, 1] \times U` 上の p 形式、
  * :math:`\fnm{\iota_0}{V}{[0, 1] \times U}{\bm x}(0, \bm x)`
  * :math:`\fnm{\pi}{[0, 1] \times U}{U}{(x_0, \bm x)}x_0\bm x`

  このとき :math:`I(\alpha)` を次のようにおくと表題の等式が成り立つ
  （ただし :math:`\alpha` をいつもようにおいたものとする）：

  .. math::

     I(\alpha) = \sum_{0 < i_2 < \dotsb < i_p}\left(
     \int_0^{x_0}\! f_{0 i_2 \dots i_p}\,\dd{x_0}
     \right)
     \dd{x_{i_2}} \wedge \dotsb \wedge \dd{x_{i_p}}.

  * これは :math:`[0, 1] \times U` 上の p - 1 形式である。
  * :math:`\dd{I(\alpha)} + I(\dd{\alpha}) = \alpha - \alpha_0` の形になる。
    ここで :math:`\alpha_0` は次のようなものだ：

    .. math::

       \alpha_0 = \sum_{0 < i_1 < \dotsb < i_p} f_{i_1\dots i_p}
       (0, x_1, \dotsc, x_n)\,
       \dd{x_{i_1}} \wedge \dotsb \wedge \dd{x_{i_p}}.

  * :ref:`例 1.8.4 <tsuboi08.1.8.4>` より :math:`\alpha_0 = \pi^*(\iota_0^*\alpha).`

  証明手順は次のとおり：

  #. :math:`[0, 1] \times U` 上の p 形式 :math:`\beta` を次のようにおく。
     意味はこの微分形式が :math:`\varphi(x_0, \bm x) = x_0(\bm x - \bm y) + \bm y)` による
     :math:`\alpha` の引き戻しとなることにある：

     .. math::

        \beta = \sum_{i_1 < \dotsb < i_p} f_{i_1 \dots i_p}(x_0(\bm x - \bm y) + \bm y)
        (x_0\,\dd{x_{i_1}} + (x_{i_1} - y_{i_1})\,\dd{x_0}) \wedge
        \dotsb
        (x_0\,\dd{x_{i_p}} + (x_{i_p} - y_{i_p})\,\dd{x_0}).

  #. :math:`\varphi` は :math:`x_0 = 0` において定数写像 :math:`\bm y` であり、
     :math:`x_0 = 1` において恒等写像 :math:`\id_U` である。

     本書図 1.7 のちくわぶが直積 :math:`[0, 1] \times U` を表している。

  #. :math:`\dd{\alpha} = 0 \implies \dd{\beta} = \dd{(\varphi^* \alpha)} = \varphi^*(\dd{\alpha}) = 0.`

     この等式変形で :ref:`定理 1.8.11 <tsuboi08.1.8.11>` (p. 31) を利用した。

  #. ゆえに :math:`\dd{I(\beta)} = \beta - \beta_0` である。
     前ページ :ref:`命題 1.9.1 <tsuboi08.1.9.1>` による。

  #. :math:`p > 0` としたのだから :math:`\beta_0 = \pi^*(\iota_0^*\beta) = \pi^*0 = 0`
     により :math:`\dd{I(\beta)} = \beta.`

  #. :math:`x_0 = 1` とすると写像 :math:`\fn{\iota_1}{U}[0, 1] \times U` による引き戻しによって
     :math:`\alpha = \iota_1^*\beta = \iota_1^* \dd{(I(\beta))} = \dd{(\iota_1^* I(\beta))}.`

.. _tsuboi08.1.9.2:

* 注意 1.9.2

  特に :math:`a \in [0, 1]` に対して :math:`I_a(\alpha)` を上に倣って定義し、
  :math:`\iota_a(\bm x) = (a, \bm x)` と定義すると下の式が成り立つ：

  .. math::

     \dd I_a(\alpha) + I_a(\dd \alpha) = \alpha - \pi^*(\iota_a^*\alpha).

1.10 第 1 章の問題の解答
======================================================================
ノートは既に残した。

----

:doc:`chapter2a` へ。

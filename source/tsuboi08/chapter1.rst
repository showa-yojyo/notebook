======================================================================
幾何学 III 微分形式 読書ノート 1/6
======================================================================

.. contents:: ノート目次

第 1 章 ユークリッド空間上の微分形式
======================================================================

1.1 微積分学の基本定理（基礎）
----------------------------------------------------------------------
* 定義 1.1.1: 原始関数
* 定理 1.1.2: 定積分の存在
* 定理 1.1.3: `微積分学の基本定理 <http://mathworld.wolfram.com/FundamentalTheoremsofCalculus.html>`__

(pp. 2-3) の「余談」がとてもいい。
面積を求めることと接線を求めることの関係が 1.1.3 として述べられた。

1.2 微積分学の基本定理の多変数化（基礎）
----------------------------------------------------------------------
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

* 定義 1.2.2: 全微分

  先ほどの式の最後の線積分の被積分部を :math:`f` の全微分と言う：

  .. math::
  
     \dd{f} = \sum_{i = 0}^n \frac{\partial f}{\partial x_i}\dd{x}_i.

* 定理 1.2.3: 1.1.3 の一般化

  1 形式についての線積分は先ほどの式と整合する：

  .. math::

     \int_\gamma df = f \circ \gamma(b) - f \circ \gamma(a).

* 積分可能条件とは :math:`\dfrac{\partial f_i}{\partial x_j} = \dfrac{\partial f_j}{\partial x_i}`
  がすべての :math:`1 \le i, j \le n` について成り立つことを言う。

* 積分可能条件を満たす :math:`f` について、次の等式が成り立つような
  :math:`U` 上の関数 :math:`F` は存在するだろうかということを以下考察する：
  
  .. math::
  
     \dd{F} = \sum_{i = 1}^n f_i \dd{x_i}.

* 例 1.2.4: 2 次元のある例

  .. math::
  
     F(x_1, x_2) = \int_0^{x_1}\!f_1(s, 0)\,\dd{s} + \int_0^{x_2}\!f_2(x_1, t)\,\dd{t}
     \implies
     \dd{F} = f_1 \dd{x_1} + f_2 \dd{x_2}.

  なぜならば二つ目の定積分を :math:`x_1` について偏微分して、積分可能条件が使えるから。

* 例 1.2.5: 積分可能条件を満たすが、:math:`F` が存在しない例

  次の :math:`\RR^2\minuszero` 上で定義されている 1 形式は積分可能条件を満たす。
  しかし、:math:`\dd{F}` がこの 1 形式になるような :math:`F` は存在しない
  （曲線として原点を内部に含む円周をとる）：

  .. math::
  
     -\frac{x_2}{x_1^2 + x_2^2}\dd{x_1} + \frac{x_1}{x_1^2 + x_2^2}\dd{x_2}.

* 注意 1.2.6: これは円周上の関数が何か存在していて、
  それが微分になる関数を求めるときの問題である。

* 定義 1.2.7: `星型 <http://mathworld.wolfram.com/StarConvex.html>`__

  ユークリッド空間の部分集合 :math:`U \subset \RR^n` が星型であるとは、
  次の条件をいう：
  
  .. math::
  
     \forall \bm x \in U, \exists \bm y \in U, \quad\text{s.t }
     l_{\bm x} := \set{(1 -t)\bm y + t\bm x \sth 0 \le t \le 1} \subset U.

* 問題 1.2.8

  * 仮定

    * :math:`U \subset \RR^n` が星型である。
    * そこで定義されている各関数 :math:`\fn{f_i}{U}\RR` が積分可能条件を満たす。

  * 結論
  
    * :math:`\displaystyle F(\bm x) = \int_{l_{\bm x}}\! \sum_{i = 1}^n f_i\,\dd{x_i}`
      が :math:`\dd{F} = \sum_{i = 1}^n f_i \dd{x_i}` を満たす。

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

----

:doc:`chapter2` へ。

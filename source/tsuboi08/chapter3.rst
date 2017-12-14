======================================================================
第 3 章 微分形式の積分
======================================================================

.. contents:: ノート目次

* コンパクト多様体 :math:`M` の :math:`\H^p(M)` が有限次元であるならば：

  .. math::

     \dd \alpha = 0 \quad\text{and } \H^p(M) \owns [\alpha] = 0
     \iff
     \exists \beta \in \Omega^{p - 1}(M) \quad\text{s.t. } \dd \beta = \alpha.

* :math:`\H^p(M)` が自明でないときには、今のところは自力で判定するしかない。
  マイヤー・ビエトリス完全系列やチェック・ドラーム完全系列を調べることになる。

* :math:`[\alpha] = 0` であるかどうかは、有限個の積分により判定が可能となる。

3.1 閉微分 1 形式の積分
======================================================================
連結多様体 :math:`M` 上の曲線 :math:`\fn{\gamma_x}{[0, 1]}\RR` 上で積分を定義する。

* これは :math:`x_0, x \in M` を結ぶ曲線であり、
  :math:`\gamma_x(0) = x_0,\ \gamma_x(1) = x` を満たすものとしておく。

* 関数 :math:`\fn{f}{M}\RR` について閉 1 形式 :math:`\alpha` を
  :math:`\alpha = \dd f` で定義する。

* 下の左のふたつの意味が同じ積分を、右のふたつの意味が同じ積分で定義する：

  .. math::

     \int_{\gamma_x}\!\alpha = \int_{\gamma_x}\!\dd f =
     \int_0^1\!\gamma_x^* \alpha = \int_0^1\!\gamma_x^*\,\dd f.

  これの根拠は次の式が成り立つことによる：

  .. math::

     f(x) - f(x_0) = f(\gamma_x(1)) - f(\gamma_x(0))
     = \int_0^1\!\diff{f\circ \gamma_x}{t}\,\dd t.

  積分記号の中身全部は :math:`\gamma_x \dd f` である。
  これは :ref:`定義 2.1.7 <tsuboi08.2.1.7>` と :ref:`命題 2.3.6 <tsuboi08.2.3.6>` による。

* この閉 1 形式に対して積分の値が経路のとり方に依らなければ、
  :math:`\displaystyle f(x) = \int_{\gamma_x}\!\alpha` と定義すれば
  :math:`\alpha = \dd f` となる。

* :math:`\alpha = \dd f` なる :math:`f` が存在することと、
  すべての閉曲線 :math:`\gamma` について :math:`\displaystyle \int_\gamma\!\alpha = 0` であることは
  同値である。

* :math:`\H^p(M) \owns [\alpha] \ne 0` ならば、
  :math:`\displaystyle \int_\gamma\!\alpha \ne 0` なる :math:`f` が存在する。

.. _tsuboi08.3.1.1:

* 例題 3.3.1: 全微分すると与えられた微分形式に一致する関数の存在する十分条件

  * :math:`M` をコンパクト多様体、
  * :math:`\H^1(M) \cong \RR^k,`
  * 次の条件を満たす多様体上の閉曲線 :math:`\gamma_1, \dotsc, \gamma_k` が存在する：

    .. math::

       \int_{\gamma_i}\!\alpha = 0\quad\text{for }i = 1, \dotsc, k.

  このとき :math:`\alpha = \dd f` を満たす多様体上の関数 :math:`f` が存在する。

  * :math:`\H^1(M)` の基底を :math:`[\alpha_1], \dotsc, [\alpha_k]` とおく。
  * 線形代数の各種命題の証明にありがちなアルゴリズムにより、
    次の正方行列が正則であるように閉曲線 :math:`\gamma_1, \dotsc, \gamma_k` がとれる：

    .. math::

       \left(\int_{\gamma_j}\!\alpha_i\right)_{i, j = 1, \dotsc, k}.

  * 閉 1 形式 :math:`\displaystyle [\alpha] = \sum_{i = 1}^k b_i [\alpha_i]`
    となるように各 :math:`b_i \in \RR` をとる。

    * :math:`\displaystyle \int_{\gamma_j}\!\alpha = \sum_{i = 1}^k b_i \int_{\gamma_j}\!\alpha_i = 0,`
    * :math:`\det\left(\int_{\gamma_j}\!\alpha_i\right) \ne 0`

    より、すべての :math:`b_j = 0`

  * ゆえに :math:`\int_{\gamma_i}\!\alpha = 0 \implies \H^1(M) \owns [\alpha] = 0.`
  * 前ページの黒丸より :math:`\alpha = \dd f.`

.. _tsuboi08.3.1.2:

* 例 3.1.2: トーラス :math:`T^n = \RR^n/\ZZ^n` での事情

  * :math:`\H^1(T^n) \cong \RR^n` であるので（前章で何度か言及された）
    基底として :math:`[\dd x_1], \dotsc, [\dd x_n]` がとれる。
  * 曲線 :math:`\fnm{\gamma_j}{[0, 1]}{\RR^n}{t}t\bm e_j` に対して
    :math:`\displaystyle \int_{\gamma_j}\!\dd x_i = \delta_{ji}` が成り立つ。
    右辺はクロネッカーの記号。

  * 閉形式 :math:`\alpha \in \Omega^1(T^n)` に対して、
    各曲線に沿う積分がゼロであるならば、:math:`\alpha = \dd f` を満たす
    トーラス上の関数 :math:`f` が存在する。

  * 一般には次を満たす関数 :math:`f` が存在する：

    .. math::

       \alpha - \sum_{i = 1}^n \int_{\gamma_i}\!\alpha \,\dd x_i = \dd f.

.. _tsuboi08.3.1.3:

* 問題 3.1.3: :math:`C^\infty` ホモトピックならば積分値は経路の取り方に依らない

  * :math:`C^\infty` 級関数 :math:`\fn{F}{[0, 1]\times[0, 1]}M` が

    .. math::

       \begin{align*}
       F(0, t) &= \gamma_0(t),\quad F(s, 0) = x_0,\\
       F(1, t) &= \gamma_1(t),\quad F(s, 1) = x_1
       \end{align*}

    を満たすとすると、すべての閉 1 形式 :math:`\alpha` の経路積分は同じである：

    .. math::

       \begin{align*}
       \int_{\gamma_1}\!\alpha - \int_{\gamma_0}\!\alpha
       &= \int_0^1\!\gamma_1^*\alpha - \int_0^1\!\gamma_0^*\alpha\\
       &= \int_{[0, 1]\times\set{0}}\!F^*\alpha
        + \int_{\set{1}\times[0, 1]}\!F^*\alpha
        - \int_{[0, 1]\times\set{1}}\!F^*\alpha
        - \int_{\set{0}\times[0, 1]}\!F^*\alpha\\
       &= \int_{[0, 1]\times[0, 1]}\!F^*\,\dd \alpha\\
       &= 0.
       \end{align*}

    * 最初の等号は 1 形式の積分の定義による。本節冒頭参照。
    * 二番目の等号はホモトピックであるという仮定による。
    * 三番目の等号は長方形上の 1 形式に対する積分であることによる。
      :ref:`命題 1.3.1 <tsuboi08.1.3.1>` 参照。
    * 最後の等号は与えられた微分形式が閉形式であることによる。

3.2 単体からの写像に沿う積分
======================================================================
TBW



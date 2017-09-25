======================================================================
幾何学 I 多様体入門 読書ノート 5/8
======================================================================

:doc:`note4` からの続き。

.. contents:: ノート目次

第 5 章 多様体上の関数
======================================================================

5.1 関数の台
----------------------------------------------------------------------
関数の台
  多様体 :math:`M` で定義された関数 :math:`f` に対する次の部分集合のことを関数の台という。

  .. math::
     :nowrap:

     \begin{align*}
     \operatorname{supp}f = \overline{\{x \in M \mid f(x) \ne 0\}}
     \end{align*}

  補集合について次のことが成り立つことに注意する：

  .. math::
     :nowrap:

     \begin{align*}
     x \in M \setminus \operatorname{supp}F \Leftrightarrow \exists U \owns x: f(U) = \{0\}
     \end{align*}

  * 定義上、多様体という条件を位相空間まで緩められる。

* 定理 5.1.1: 任意の :math:`x_0 \in M` とその任意の近傍 :math:`V \in M` に対して、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\mu` が存在する：

  #. :math:`\mu(x) \ge 0`
  #. :math:`\mu(x_0) > 0, \operatorname{supp} \mu \in V`
  #. :math:`\operatorname{supp} \mu` がコンパクトである。

  証明方針：問題 3.7.1 の関数 :math:`\rho(x)` を加工してなんとか関数 :math:`\mu(x)` を構成する。

* 定理 5.1.2: :math:`M` のコンパクト集合 :math:`K` とそれを含む開集合 :math:`U` があるとき、
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  #. :math:`\nu(x) \ge 0`
  #. :math:`\nu|K(x) > 0`
  #. :math:`\operatorname{supp} \nu` が :math:`U` のコンパクト集合である。

  証明方針：定理 5.1.1 の関数 :math:`\mu(x)` をいくつか足して関数 :math:`\nu(x)` を構成する。

* 定理 5.1.3: 定理 5.1.2 と同じ仮定の下で
  次のような :math:`M` を定義域とする :math:`C^\infty` 級関数 :math:`\nu` が存在する：

  #. :math:`0 \le \nu(x) \le 1`
  #. :math:`\nu|K(x) = 1`
  #. :math:`\operatorname{supp} \nu` が :math:`U` のコンパクト集合である。

* 注意 5.1.4 の :math:`\nu f: M \to \mathbb R,\ \nu|K = f|K` の意味とは？

ここまでの議論で、多様体上には多くの :math:`C^\infty` 級関数が存在することがわかった。

* 補題 5.1.5: アダマール。

  :math:`\mathbb R^n` 内の原点の開近傍で定義されている :math:`C^\infty` 級関数 :math:`f` に対して、
  次のように書けるような :math:`C^\infty` 関数 :math:`g_k (k = 0, \dotsc, n)` が存在する：

  .. math::
     :nowrap:

     \begin{align*}
     f(x_1, \dotsc, x_n) & = f(0, \dotsc, 0) + \sum_{k = i}^{n}x_k g_k(x_1, \dotsc, x_n)\\
     \frac{\partial f}{\partial x_k}(0, \dotsc, 0) & = g_k(0, \dotsc, 0)
     \end{align*}

  初等的な方法で示せる。
  :math:`{ \displaystyle g_k(x_1, \dotsc, x_n) = \int_0^1 \frac{\partial f}{\partial x_k} (tx_1, \dotsc, tx_n) dt}`

* 問題 5.1.6: 方向微分。
  多様体 :math:`M` 上で定義されている :math:`C^\infty` 級関数 :math:`f, g` と点 :math:`p \in M` に対して、
  演算 :math:`D` が定義できて :math:`D(f \cdot g) = Df g(p) + f(p) Dg` が成り立つとする（これを方向微分と呼ぶ）。

  #. 点 :math:`p \in M` における方向微分全てからなる空間 :math:`\mathcal{D}_p` は実ベクトル空間である。
  #. 多様体 :math:`M` 上の曲線 :math:`c(t)\ (c(0) = p)` について
     :math:`{ \displaystyle D_c: f \mapsto \frac{d(f \circ c)}{dt}(0)}` は点 :math:`p` における方向微分である。
  #. :math:`\mathcal{D}_p` の基底は :math:`{ \displaystyle
     \left\{
     \left(\frac{\partial}{\partial x_1} \right)_p,
     \dotsc,
     \left(\frac{\partial}{\partial x_n} \right)_p
     \right\}}` である。

     * :math:`{ \displaystyle \left(\frac{\partial}{\partial x_k} \right)_p}` は関数
       :math:`{ \displaystyle t \mapsto \varphi^{-1}(0, \dotsc, \overset{(k)}t, \dotsc, 0)}` における方向微分とする (cf. p. 76)。
     * これを証明するのに補題 5.1.5 を利用する。

----

:doc:`note6` へ。

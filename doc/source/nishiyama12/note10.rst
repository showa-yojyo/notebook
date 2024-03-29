======================================================================
幾何学と不変量 読書ノート 10/10
======================================================================

.. contents:: ノート目次

第 10 章 射影空間とグラスマン多様体
======================================================================

10.1 n 次元射影空間
----------------------------------------------------------------------

序盤を忘れているのならば 8 章を読み直せ。

:math:`(1, n)` 型放物型部分群 :math:`P_{(1, n)}`
  次のような :math:`\mathit{GL}_{n + 1}(\CC)` の部分群のことをそう呼ぶ：

  .. math::

     \begin{align*}
     \Set{
     \left(
     \begin{array}{c|c}
       \lambda & \begin{array}{ccc} u_2 & \cdots & u_n \end{array} \\ \hline
     \begin{array}{c} 0 \\ \vdots \\ 0 \end{array}  & {\Huge{A}}
     \end{array}
     \right)
     \Sth \lambda \in \CC^\times,\ A \in \mathit{GL}_{n + 1}(\CC)
     }.
     \end{align*}

* 定理 10.2: 等質空間 :math:`{\mathbb{P}^{n}(\CC) \cong \mathit{GL}_{n + 1}(\CC)
  / P_{(1, n)}}`
* 定理 10.3: 等質空間 :math:`{\mathbb{P}^{n}(\CC) \cong \mathit{U}_{n +
  1}/(\mathit{U}_1(\CC) \times \mathit{U}_n(\CC))}`
* 定理 10.4: :math:`\mathbb{P}^{n}(\CC)` はコンパクト。

10.2 2 次曲面と点の配置空間
----------------------------------------------------------------------

2 次曲面
  :math:`{{}^t\!\bm x S \bm x = 0}`,
  :math:`{S \in \mathit{Sym}_{n + 1}(\CC)}`,
  :math:`{{}^t\!\bm x = (x_0, \cdots, x_n)}` は同次座標で
  :math:`{\det S \ne 0}.`
最大階数の行列
  本文の説明ではピンと来ない。おそらく ``rank(A) = max(A.nrow, A.ncol)`` のよう
  な行列 ``A`` の意味と思われる。
:math:`{\mathit{M}_{n + 1, m}^{\circ}(\CC)}`
  上で述べた最大階数行列全てからなる空間。
:math:`{\mathit{Sym}_{n + 1}^{\circ}(\CC)}`
  :math:`{\coloneqq \set{S \in \mathit{Sym}_{n + 1}(\CC) \sth \det S \ne 0}}.`

* :math:`{m \le n}` とする。

  * 作用 :math:`{\rho(g)(S, A) = ({}^t\! g\inv S g\inv, gA)}.`
  * :math:`{\mathit{Sym}_{n + 1}^{\circ}(\CC) \times \mathit{M}_{n + 1,
    m}^{\circ}(\CC) / (\mathit{GL}_{n + 1}(\CC) \times T^m)}` が非退化 2 次曲面
    と:math:`\mathbb{P}^{n}(\CC)` の :math:`m` 点配置を表す。

    * :math:`T^m \coloneqq (\CC^\times)^m` を :math:`n` 次元トーラス群と呼ぶ。

* 定理 10.7 不変式環の生成元に関する定理。どうなっているか。
* 定理 10.8 :math:`{m = 2}` のときの :math:`{\mathit{GL}_{n + 1}(\CC) \times
  T^m}`の :math:`{\mathit{Sym}_{n + 1}^{\circ}(\CC) \times \mathit{M}_{n + 1,
  m}^{\circ}(\CC)}` への作用に関する不変式環の生成元についての定理。

10.3 グラスマン多様体
----------------------------------------------------------------------

部分空間
  ベクトル空間 :math:`V = \CC^n` から線形独立なベクトルを :math:`d` 個取ってきて
  それらの張る部分空間を :math:`{W = \langle v_1, \cdots, v_d \rangle}` とする。
  このとき :math:`{\mathbb{P}(W) \coloneqq \set{[w] \sth w \in W} \subset
  \mathbb{P}(V)}` は :math:`{n - 1}` 次元部分空間であるという。

  * ベクトル 2 個だけからなるものならば :math:`\mathbb{P}(W)` は射影直線。

* 定理 10.9: :math:`{\mathscr{W} = \set{\mathbb{P}(W_{v_1}, \cdots, W_{v_d}) \sth
  v_i \in V}}.` つまり射影部分空間の全体に対し、:math:`{\mathit{GL}(V) =
  \mathit{GL}_n(\CC)}` が射影変換として推移的に作用する。

`グラスマン多様体 <http://mathworld.wolfram.com/GrassmannManifold.html>`__
  ベクトル空間の部分空間全体のことをそう呼ぶ。

  * 記号は :math:`Gr_d(V)`, :math:`Gr_d^n(\CC)` を用いる。ここで :math:`d` と
    :math:`n` は部分空間の次元と元のベクトル空間の次元をそれぞれ表す。
  * :math:`{Gr_1(V) = \mathbb{P}(V)}` は :math:`{n - 1}` 次元射影空間だ。

放物型部分群
  :math:`\mathit{GL}_n(\CC)` の部分群で、次の形のものを言う：

  .. math::

     \begin{align*}
     P_{(d, n - d)} \coloneqq
     \Set{
     \begin{pmatrix} A & B\\ 0 & D \end{pmatrix}
     \Sth
     A \in \mathit{GL}_d(\CC),\
     D \in \mathit{GL}_{n - d}(\CC),\
     B \in \mathit{M}_{d, n - d}(\CC)
     }.
     \end{align*}

  #. 等質空間の全単射 :math:`{\mathit{GL}(V)/P_{(d, n - d)} \longto Gr_d(V)}` が
     存在する。
  #. この全単射を利用して :math:`Gr_d(V)` に位相を入れる（複素多様体）。

* 定理 10.11

  * :math:`{V = \CC^n}` として :math:`U_n(\CC)` は :math:`Gr_d(V)` に推移的に作
    用する。
  * :math:`{W_{std} \coloneqq \langle \bm e_1, \cdots, \bm e_d \rangle}` におけ
    る固定部分群は :math:`{U_d(\CC^n) \times U_{n - d}(\CC^n)}` に同型だ。
  * よって :math:`{Gr_d(V) \cong U_n(\CC^n)/(U_d(\CC^n) \times U_{n -
    d}(\CC^n))}.`
  * :math:`Gr_d(V)` はコンパクトかつエルミート対称空間だ。

10.4 プリュッカー座標
----------------------------------------------------------------------

目標はグラスマン多様体を高次の射影空間に埋め込むことだ。

プリュッカー座標
  プリュッカー座標とは、次の写像 :math:`{\fn{\mathscr{P}}{\mathit{M}_{4,
  2}^{\circ}(\CC)}\mathbb{P}^5(\CC)}` の値を言う。

  .. math::

     A \longmapsto [D_{12}(A) : D_{13}(A) : D_{14}(A) : D_{32}(A) : D_{42}(A) :
     D_{34}(A)].

* 定理 10.3: 写像 :math:`\mathscr{P}` は :math:`Gr_2(\CC^4)` から
  :math:`\mathbb{P}^5(\CC)` 内の二次曲面への同型写像である。

  * これをプリュッカー埋め込みという。

10.5 点配置と多重旗多様体
----------------------------------------------------------------------

旗多様体
  群の放物型部分群による商空間。
多重旗多様体
  旗多様体いくつかによる直積。

* この節の主題は次の対象の記述だ。

  * :math:`{(\mathit{GL}_n(\CC)/P_{1, n - 1})^k / \mathit{GL}_n(\CC)}`
  * :math:`{(Gr_{d_1}^n(V) \times \cdots \times Gr_{d_k}^n(V))/G \cong (G/P_{(d_1, n - d_1)} \times \cdots \times G/P_{(d_k, n - d_k)})/G}`

附録：集合と写像
======================================================================

本書を手に取るような人ならば、読むに及ばない内容なのかもしれない。

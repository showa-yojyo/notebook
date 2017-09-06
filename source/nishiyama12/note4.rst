======================================================================
幾何学と不変量 読書ノート 4/4
======================================================================

:doc:`note3` からの続き。

.. include:: /_include/book-details/nishiyama12.txt

.. contents:: ノート目次

第 9 章 射影変換と不変量
======================================================================

9.1 射影空間と連比
----------------------------------------------------------------------
連比
  :math:`[z_0 : ... : z_n] = [\alpha z_0 : ... : \alpha z_n ] (z_i \in \mathbb{C}, \alpha \in \mathbb{C}^\times)`
  オールゼロのものを除く。

射影空間
  連比全ての集合であり、これを :math:`\mathbb{P}^n` と記す。

斉次座標
  上記の各 :math:`z_i` のことを言う。本ノートでは漢字変換の都合で同次座標と記す。

包含写像
  写像 :math:`\iota: \mathbb{C}^n \hookrightarrow \mathbb{P}^n` で、
  複素ベクトルに、そのベクトルの全成分に加えて、最後に 1 を付け加えた連比を対応させるもの。

  * これは単射。
  * 包含写像を表すのに、本文にあるような変な矢印を描く。

有限点 or 通常点
  射影空間の点であり、最後の成分がゼロでないものをそう呼ぶ。

無限遠点
  :math:`w = [w_0 : ... : w_{n - 1} : 0]` のタイプの点。

  * :math:`\mathbb{P}^n = \mathbb{C}^n \cup \mathbb{P}^{n - 1}`

基本アフィン開集合
  開集合 :math:`U_j = \lbrace [w_0 : ... : 1 : ... w_n] \mid (w_0, ..., \widehat{w_j}, ..., w_n) \in \mathbb{C}^n \rbrace`
  のことをそう呼ぶ。

  * :math:`U_j` が :math:`\mathbb{C}^n` と同型になる。
  * :math:`U_j` で :math:`\mathbb{P}^n` に位相を入れられる。

9.2 射影
----------------------------------------------------------------------
1 次元トーラス群
  :math:`\mathbb{C}^\times` のこと。

  この群は :math:`\mathbb{C}^{n + 1} \setminus \lbrace 0 \rbrace` にスカラーの乗算により自然に作用している。
  :math:`\mathbb{P}^n \cong (\mathbb{C}^{n + 1} \setminus \lbrace 0 \rbrace) / \mathbb{C}^\times` と書ける。

射影空間
  ベクトル空間 V に対して :math:`\mathbb{P}(V) = (V \setminus \lbrace 0 \rbrace) / \mathbb{C}^\times` をそう呼ぶ。

  * :math:`\mathbb{P}(V) = \mathbb{P}^n` とも記す。肩の n は多様体次元であって、ベクトル空間のそれではない。
  * :math:`\mathbb{P}(V)` は多様体だが :math:`V / \mathbb{C}^\times` のほうはハウスドルフ空間ですらない。
  * 2 ベクトルの張る部分空間を射影化すると、射影直線と同型となる。

（射影）部分空間
  k 点 :math:`[a_1], ..., [a_k] \in \mathbb{P}^{n}` を含む最小の射影空間のことをそう呼ぶ。

一般の位置
  各 :math:`\lbrace a_i \rbrace` が V で一次独立であること。
  :math:`\mathbb{P}(W) \cong \mathbb{P}^{k - 1}`

9.3 射影変換
----------------------------------------------------------------------
射影変換
  射影空間から自身への自己同型写像。行列を使う。
  :math:`g \in \mathit{GL}_{n + 1}(\mathbb{C}), V = \mathbb{C}` をとる。
  自己同型写像 :math:`\pi_g: [v] \mapsto [gv]` は :math:`\mathbb{P}(V)` の射影変換であるという。

射影一般線形群
  :math:`\mathit{PGL}_{n + 1}(\mathbb{C}) := \mathit{GL}_{n + 1}(\mathbb{C})/\mathbb{C}^\times` は
  :math:`\mathbb{P}^n` 上の射影変換のなす群となる。

アフィン変換群
  スペースの都合で書けないが、この三次正方行列のなす群を :math:`A_2(\mathbb{C})` と書いてアフィン変換群と呼ぶ。

  * この変換は複素平面を保つ。

9.4 一次分数変換
----------------------------------------------------------------------
:math:`n = 1` として射影変換 :math:`\pi_g` を考える。
この写像は以下のようにして :math:`\mathbb{P}^1` に作用する。

.. math::
   :nowrap:

   \begin{eqnarray*}
   \pi_g(z)      &=& \cfrac{az + b}{cz + d} & (cz + d \ne 0) & \text{or} & \infty (cz + d = 0)\\
   \pi_g(\infty) &=& \cfrac{a}{c}           & (c \ne 0)      & \text{or} & \infty (c = 0)
   \end{eqnarray*}

* 定理 9.9: :math:`\mathbb{P}^1` 上の一次分数変換のうち、上半平面を保つものは :math:`\mathit{SL}_2(\mathbb{R})` から取れる。
* 定理 9.10: 上半平面は :math:`\mathit{SL}_2(\mathbb{R})/\mathit{SO}_2(\mathbb{R})` と同型。

9.5 複比
----------------------------------------------------------------------
複比
  :math:`\mathbb{P}^1` 上の相異なる 4 点 :math:`[v_i]` に対する次の値を複比という。

  .. math::

     \operatorname{cr}([v_1], [v_2]; [v_3], [v_4]) = \cfrac{D_{13} D_{24}}{D_{14} D_{23}}

  ここで :math:`D_{ij} = \det(v_i v_j)` とする。

* 定理 9.13: 射影変換による複比の不変性。
* 定理 9.14: それは一時分数変換である。
* 定理 9.15 は見覚えのある主張のはず。

9.6 円と複比
----------------------------------------------------------------------
* 複素数に対してはその複比を次のように計算してもよい。

  .. math::

     \operatorname{cr}([z_1], [z_2]; [z_3], [z_4]) = \cfrac{z_1 - z_3}{z_1 - z_4} \cfrac{z_2 - z_4}{z_2 - z_3}

* 定理 9.19

  #. 円円対応
  #. 円周上の相異なる 4 点の複比は実数。
  #. 前節の 3 点定理を用いる。

9.7 不変式としての複比
----------------------------------------------------------------------
この節を読むのには相当な気力が要る。

9.8 プリュッカーの関係式とプトレマイオスの定理
----------------------------------------------------------------------
* 定理 9.26: 射影直線上の 4 点の複比 :math:`\lambda = \operatorname{cr}(p_1, p_2; p_3, p_4)` について、
  点の順序を入れ替えた複比はどれも :math:`\lambda` の有理関数として表される（全部で 6 通り）。

* 定理 9.27: プリュッカーの関係式。
  :math:`(v_1, ..., v_4) \in M_{2,4}(\mathbb{C})` に対して 9.5 の記号と同じものを用いると
  :math:`D_{12}D_{34} + D_{13}D_{42} + D_{14}D_{23} = 0`

* 定理 9.29: プトレマイオス。
  円に内接する四角形の相対する二組の辺の積の和は、対角線の積に等しい。

9.9 射影直線上の点配置と j 不変量
----------------------------------------------------------------------
9.7 節同様に難しい。

半直積群
  :math:`(\tau, t) \cdot (\sigma, s) = (\tau \sigma, t^\sigma s)` という演算で直積に群の構造を入れる。

j 不変量
  :math:`j(p_1, p_2; p_3, p_4) = 2^8 (\lambda^2 - \lambda + 1)/(\lambda^2 (1 - \lambda))`

不変量に関するトピックが全然頭に入らなくなって来ている。

第 10 章 射影空間とグラスマン多様体
======================================================================

10.1 n 次元射影空間
----------------------------------------------------------------------
序盤を忘れているのならば 8 章を読み直せ。

(1, n) 型放物型部分群 :math:`P_{(1, n)}`
  次のような :math:`\mathit{GL}_{n + 1}(\mathbb{C})` の部分群のことをそう呼ぶ：

  .. math::
     :nowrap:

     \begin{align*}
     \lbrace
     \left(
     \begin{array}{c|c}
       \lambda & \begin{array}{ccc} u_2 & \cdots & u_n \end{array} \\ \hline
     \begin{array}{c} 0 \\ \vdots \\ 0 \end{array}  & {\Huge{A}}
     \end{array}
     \right)
     \mid \lambda \in \mathbb{C}^\times,\ A \in \mathit{GL}_{n + 1}(\mathbb{C}) \rbrace
     \end{align*}

* 定理 10.2: 等質空間 :math:`\mathbb{P}^{n}(\mathbb{C}) \cong \mathit{GL}_{n + 1}(\mathbb{C}) / P_{(1, n)}`
* 定理 10.3: 等質空間 :math:`\mathbb{P}^{n}(\mathbb{C}) \cong \mathit{U}_{n + 1}/(\mathit{U}_1(\mathbb{C}) \times \mathit{U}_n(\mathbb{C}))`
* 定理 10.4: :math:`\mathbb{P}^{n}(\mathbb{C})` はコンパクト。

10.2 2 次曲面と点の配置空間
----------------------------------------------------------------------
2 次曲面
  :math:`{}^t\mathbf{x} S \mathbf{x} = 0`,
  :math:`S \in \mathit{Sym}_{n + 1}(\mathbb{C})`,
  :math:`{}^t\mathbf{x} = (x_0, \cdots, x_n)` は同次座標で
  :math:`\det S \ne 0`

最大階数の行列
  本文の説明ではピンと来ない。おそらく ``rank(A) = max(A.nrow, A.ncol)`` のような行列 ``A`` の意味と思われる。

:math:`\mathit{M}_{n + 1, m}^{\circ}(\mathbb{C})`
  上で述べた最大階数行列全てからなる空間。

:math:`\mathit{Sym}_{n + 1}^{\circ}(\mathbb{C})`
  :math:`:= \lbrace S \in \mathit{Sym}_{n + 1}(\mathbb{C}) \mid \det S \ne 0 \rbrace`

* :math:`m \le n` とする。

  * 作用 :math:`\rho(g)(S, A) = ({}^t g^{-1} S g^{-1}, gA)`
  * :math:`\mathit{Sym}_{n + 1}^{\circ}(\mathbb{C}) \times \mathit{M}_{n + 1, m}^{\circ}(\mathbb{C}) / (\mathit{GL}_{n + 1}(\mathbb{C}) \times T^m)`
    が非退化 2 次曲面と :math:`\mathbb{P}^{n}(\mathbb{C})` の m 点配置を表す。

    * :math:`T^m := (\mathbb{C}^\times)^m` を n 次元トーラス群と呼ぶ。

* 定理 10.7 不変式環の生成元に関する定理。どうなっているか。
* 定理 10.8 :math:`m = 2` のときの :math:`\mathit{GL}_{n + 1}(\mathbb{C}) \times T^m` の
  :math:`\mathit{Sym}_{n + 1}^{\circ}(\mathbb{C}) \times \mathit{M}_{n + 1, m}^{\circ}(\mathbb{C})` への作用に関する
  不変式環の生成元についての定理。

10.3 グラスマン多様体
----------------------------------------------------------------------
部分空間
  ベクトル空間 :math:`V = \mathbb{C}^n` から線形独立なベクトルを d 個取ってきて
  それらの張る部分空間を :math:`W = \langle v_1, \cdots, v_d \rangle` とする。
  このとき :math:`\mathbb{P}(W) := \lbrace [w] \mid w \in W \rbrace \subset \mathbb{P}(V)` は
  n - 1 次元部分空間であるという。

  * ベクトル 2 個だけからなるものならば :math:`\mathbb{P}(W)` は射影直線。

* 定理 10.9: :math:`\mathscr{W} = \lbrace \mathbb{P}(W_{v_1}, \cdots, W_{v_d}) \mid v_i \in V \rbrace`
  つまり射影部分空間の全体に対し、
  :math:`\mathit{GL}(V) = \mathit{GL}_n(\mathbb{C})` が射影変換として推移的に作用する。

グラスマン多様体
  ベクトル空間の部分空間全体のことをそう呼ぶ。

  * 記号は :math:`Gr_d(V)`, :math:`Gr_d^n(\mathbb{C})` を用いる。
    ここで d と n は部分空間の次元と元のベクトル空間の次元をそれぞれ表す。

  * :math:`Gr_1(V) = \mathbb{P}(V)` は n - 1 次元射影空間だ。

放物型部分群
  :math:`\mathit{GL}_n(\mathbb{C})` の部分群で、次の形のものを言う。

  .. math::
     :nowrap:

     \begin{align*}
     P_{(d, n - d)} := 
     \lbrace
     \left(\begin{array}{cc} A & B\\ 0 & D \end{array}\right)
     \mid
     A \in \mathit{GL}_d(\mathbb{C}),\ 
     D \in \mathit{GL}_{n - d}(\mathbb{C}),\ 
     B \in \mathit{M}_{d, n - d}(\mathbb{C})
     \rbrace
     \end{align*}

  #. 等質空間の全単射 :math:`\mathit{GL}(V)/P_{(d, n - d)} \to Gr_d(V)` が存在する。
  #. この全単射を利用して :math:`Gr_d(V)` に位相を入れる（複素多様体）。

* 定理 10.11

  * :math:`V = \mathbb{C}^n` として :math:`U_n(\mathbb{C})` は :math:`Gr_d(V)` に推移的に作用する。
  * :math:`W_{std} := \langle \mathbf{e}_1, \cdots, \mathbf{e}_d \rangle` における
    固定部分群は :math:`U_d(\mathbb{C}^n) \times U_{n - d}(\mathbb{C}^n)` に同型だ。

  * よって :math:`Gr_d(V) \cong U_n(\mathbb{C}^n)/(U_d(\mathbb{C}^n) \times U_{n - d}(\mathbb{C}^n))`
  * :math:`Gr_d(V)` はコンパクトかつエルミート対称空間だ。

10.4 プリュッカー座標
----------------------------------------------------------------------
目標はグラスマン多様体を高次の射影空間に埋め込むことだ。

プリュッカー座標
  プリュッカー座標とは、次の写像 :math:`\mathscr{P}: \mathit{M}_{4, 2}^{\circ}(\mathbb{C}) \to \mathbb{P}^5(\mathbb{C})` の値を言う。

  .. math::
     :nowrap:

     \begin{align*}
     A \mapsto [D_{12}(A) : D_{13}(A) : D_{14}(A) : D_{32}(A) : D_{42}(A) : D_{34}(A)]
     \end{align*}

* 定理 10.3: 写像 :math:`\mathscr{P}` は :math:`Gr_2(\mathbb{C}^4)` から
  :math:`\mathbb{P}^5(\mathbb{C})` 内の二次曲面への同型写像である。

  * これをプリュッカー埋め込みという。

10.5 点配置と多重旗多様体
----------------------------------------------------------------------
旗多様体
  群の放物型部分群による商空間。

多重旗多様体
  旗多様体いくつかによる直積。

* この節の主題は次の対象の記述だ。

  * :math:`(\mathit{GL}_n(\mathbb{C})/P_{1, n - 1})^k / \mathit{GL}_n(\mathbb{C})`
  * :math:`(Gr_{d_1}^n(V) \times \cdots \times Gr_{d_k}^n(V))/G \cong (G/P_{(d_1, n - d_1)} \times \cdots \times G/P_{(d_k, n - d_k)})/G`

附録：集合と写像
======================================================================
本書を手に取るような人ならば、読むに及ばない内容なのかもしれない。
